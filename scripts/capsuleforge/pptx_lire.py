"""CapsuleForge — lecture d'un diaporama PowerPoint (.pptx), sans PowerPoint.

Lit dans l'archive : titre, notes, durée (minutage enregistré), audio de narration et états d'animation de
chaque diapositive. Un état = ce qui est visible après un clic ; l'état 0 est la diapositive à son ouverture.
Le fichier n'est jamais modifié. Les images sont produites à part, par PowerPoint lui-même (``pptx_images.py``).

Formes d'annotation : une forme nommée « cf spot », « cf cadre », « cf pointeur » ou « cf cache » (volet Sélection de
PowerPoint) n'est jamais sur les images ; elle devient un objet du pas. Un pointeur tracé en ligne brisée
(forme libre) ou en trait donne une trajectoire.

Limite connue : PowerPoint n'enregistre pas l'instant des clics pendant une narration, seulement la durée de
la diapositive ; les apparitions sont donc réparties sur cette durée, à régler ensuite.
Licence : GPL v3.
"""
from __future__ import annotations

import posixpath
import re
import wave
import zipfile
import io
from pathlib import Path
from xml.etree import ElementTree as ET

NS = {"p": "http://schemas.openxmlformats.org/presentationml/2006/main",
      "a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
P = "{%s}" % NS["p"]
EMU_PAR_POUCE = 914400


def _rels(z: zipfile.ZipFile, chemin: str) -> dict:
    """Renvoie les relations d'une partie de l'archive : ``{rId: (type court, cible résolue)}``."""
    d, f = posixpath.split(chemin)
    nom = f"{d}/_rels/{f}.rels"
    if nom not in z.namelist():
        return {}
    out = {}
    for r in ET.fromstring(z.read(nom)):
        cible = r.get("Target", "")
        if r.get("TargetMode") != "External":
            cible = posixpath.normpath(posixpath.join(d, cible))
        out[r.get("Id")] = (r.get("Type", "").rsplit("/", 1)[-1], cible)
    return out


def _texte(noeud) -> str:
    """Renvoie le texte d'un nœud, un paragraphe non vide par ligne."""
    lignes = []
    for par in noeud.iter("{%s}p" % NS["a"]):
        lignes.append("".join(t.text or "" for t in par.iter("{%s}t" % NS["a"])))
    return "\n".join(l for l in lignes if l.strip()).strip()


PREFIXE = "cf"                                     # formes d'annotation : nommées « cf spot », « cf pointeur »…
TYPES_CF = {"spot": "spot", "cadre": "cadre", "pointeur": "pointeur", "pointer": "pointeur", "cache": "cache"}


def _type_cf(nom: str) -> str | None:
    """Renvoie le type d'objet d'un nom de forme d'annotation (« cf spot », « CF-Pointeur 2 », « cf: cadre »…).

    Renvoie ``None`` si le nom n'est pas celui d'une annotation.
    """
    m = re.match(r"^\s*cf[\s:_-]+([a-zà-ÿ]+)", (nom or "").lower())
    return TYPES_CF.get(m.group(1)) if m else None


def _formes_cf(racine, journal: list) -> list[dict]:
    """Renvoie les formes d'annotation d'une diapositive (premier niveau), en unités du diaporama (EMU).

    Chaque forme est un dictionnaire ``{spid, type, nom, cadre: [x, y, l, h], forme, trajet: [[x, y], …]}``
    (``forme`` et ``trajet`` seulement s'ils s'appliquent). Les remarques (formes ignorées, rotation non lue)
    sont ajoutées à ``journal``.
    """
    A = "{%s}" % NS["a"]
    arbre = racine.find("p:cSld/p:spTree", NS)
    out = []
    if arbre is None:
        return out
    for g in arbre.iter(P + "grpSp"):                                 # dans un groupe : position relative, non lue
        for c in g.iter(P + "cNvPr"):
            if _type_cf(c.get("name")) and c is not g.find("p:nvGrpSpPr/p:cNvPr", NS):
                journal.append(f"forme « {c.get('name')} » dans un groupe : ignorée (la sortir du groupe)")
    for sp in arbre:
        if sp.tag not in (P + "sp", P + "cxnSp", P + "pic"):
            continue
        c = sp.find("*/p:cNvPr", NS)
        typ = _type_cf(c.get("name")) if c is not None else None
        if not typ:
            continue
        xfrm = sp.find("p:spPr/a:xfrm", NS)
        if xfrm is None or xfrm.find("a:off", NS) is None:
            journal.append(f"forme « {c.get('name')} » sans position : ignorée")
            continue
        off, ext = xfrm.find("a:off", NS), xfrm.find("a:ext", NS)
        x, y, l, h = int(off.get("x")), int(off.get("y")), int(ext.get("cx")), int(ext.get("cy"))
        fh, fv = xfrm.get("flipH") == "1", xfrm.get("flipV") == "1"
        if xfrm.get("rot") not in (None, "0"):
            journal.append(f"forme « {c.get('name')} » : rotation non lue (position approchée)")
        f = {"spid": int(c.get("id")), "type": typ, "nom": c.get("name"), "cadre": [x, y, l, h]}
        geo = sp.find("p:spPr/a:prstGeom", NS)
        if geo is not None and geo.get("prst") == "ellipse":
            f["forme"] = "ellipse"
        if typ == "pointeur":
            pts = []
            chemin = sp.find("p:spPr/a:custGeom/a:pathLst/a:path", NS)
            if chemin is not None:                                     # forme libre : sommets de la ligne brisée
                w, hh = float(chemin.get("w") or 1) or 1.0, float(chemin.get("h") or 1) or 1.0
                for seg in chemin:
                    pt = seg.findall(A + "pt")
                    if pt and seg.tag in (A + "moveTo", A + "lnTo", A + "cubicBezTo", A + "quadBezTo"):
                        u, v = float(pt[-1].get("x")) / w, float(pt[-1].get("y")) / hh
                        pts.append([x + (1 - u if fh else u) * l, y + (1 - v if fv else v) * h])
            elif sp.tag == P + "cxnSp" or (geo is not None and geo.get("prst") in ("line", "straightConnector1")):
                pts = [[x + (l if fh else 0), y + (h if fv else 0)], [x + (0 if fh else l), y + (0 if fv else h)]]
            if len(pts) >= 2:
                f["trajet"] = pts
        out.append(f)
    return out


def _etats(racine, ignorer: set | None = None) -> tuple[list[list], bool]:
    """Renvoie les états d'animation d'une diapositive et l'indication d'une animation par paragraphe.

    Pour chaque état, la liste de ce qui est caché : une forme (son identifiant) ou des paragraphes d'une forme
    (``[identifiant, premier, dernier]``, comptés à partir de 0). Le booléen renvoyé est vrai si une animation
    vise des paragraphes. Les formes de ``ignorer`` (annotations) ne sont pas prises en compte.
    """
    seq = next((n for n in racine.iter(P + "cTn") if n.get("nodeType") == "mainSeq"), None)
    if seq is None:
        return [[]], False
    groupes = []                                   # [(automatique, [(classe, forme)])]
    par_paragraphe = False
    enfants = seq.find(P + "childTnLst")
    for par in (enfants if enfants is not None else []):
        ctn = par.find(P + "cTn")
        if ctn is None:
            continue
        auto = any(c.get("evt") == "onBegin" for c in ctn.iter(P + "cond"))
        effets = []
        for e in ctn.iter(P + "cTn"):
            classe = e.get("presetClass")
            if classe not in ("entr", "exit"):
                continue
            formes = []
            for cible in e.iter(P + "spTgt"):
                s = int(cible.get("spid"))
                rg = cible.find(P + "txEl/" + P + "pRg")
                if rg is not None:
                    par_paragraphe = True
                    s = (s, int(rg.get("st")), int(rg.get("end")))
                if (s[0] if isinstance(s, tuple) else s) in (ignorer or ()):
                    continue                                          # annotation : jamais sur l'image
                if s not in formes:
                    formes.append(s)
            effets += [(classe, s) for s in formes]
        groupes.append((auto, effets))
    premier = {}
    for _, effets in groupes:
        for classe, s in effets:
            premier.setdefault(s, classe)
    cachees = {s for s, c in premier.items() if c == "entr"}       # ce qui entre plus tard est caché au départ
    etats: list[list[int]] = []
    for i, (auto, effets) in enumerate(groupes):
        if not (auto and i == 0) and not etats:
            etats.append(_tri(cachees))                           # état 0 avant le premier clic
        for classe, s in effets:
            cachees.discard(s) if classe == "entr" else cachees.add(s)
        if auto and i == 0:
            continue                                                # effets joués à l'ouverture : dans l'état 0
        if effets:
            etats.append(_tri(cachees))
    if not etats:
        etats.append(_tri(cachees))
    # deux états identiques de suite (effets d'emphase seulement) n'en font qu'un
    out = [etats[0]]
    for e in etats[1:]:
        if e != out[-1]:
            out.append(e)
    return out, par_paragraphe


def _tri(cachees) -> list:
    """Renvoie les éléments cachés triés, les paragraphes sous forme de listes."""
    return [list(c) if isinstance(c, tuple) else c for c in sorted(cachees, key=lambda c: (c if isinstance(c, tuple) else (c, -1, -1)))]


def lire(fichier: Path) -> dict:
    """Lit un diaporama et renvoie sa structure : taille et, par diapositive, titre, notes, durée, audio, états.

    Chaque diapositive porte aussi les identifiants des formes à cacher à l'export (``medias``) et, s'il y en a,
    ses formes d'annotation (``formes``) et les remarques de lecture (``remarques``).
    """
    fichier = Path(fichier)
    with zipfile.ZipFile(fichier) as z:
        pres = ET.fromstring(z.read("ppt/presentation.xml"))
        taille = pres.find("p:sldSz", NS)
        rels = _rels(z, "ppt/presentation.xml")
        diapos = []
        for n, sld in enumerate(pres.find("p:sldIdLst", NS), 1):
            chemin = rels[sld.get("{%s}id" % NS["r"])][1]
            brut = z.read(chemin)
            racine = ET.fromstring(brut)
            r = _rels(z, chemin)
            titre = ""
            for sp in racine.iter(P + "sp"):
                ph = sp.find("p:nvSpPr/p:nvPr/p:ph", NS)
                if ph is not None and ph.get("type") in ("title", "ctrTitle"):
                    titre = _texte(sp).replace("\n", " ")
                    break
            notes = ""
            for typ, cible in r.values():
                if typ == "notesSlide" and cible in z.namelist():
                    for sp in ET.fromstring(z.read(cible)).iter(P + "sp"):
                        ph = sp.find("p:nvSpPr/p:nvPr/p:ph", NS)
                        if ph is not None and ph.get("type") == "body":
                            notes = _texte(sp)
            m = re.search(rb'advTm="(\d+)"', brut)
            audio = next((c for t, c in r.values() if t in ("audio", "media") and c.lower().endswith((".wav", ".m4a", ".mp3", ".wma"))), None)
            # formes de média (icône du haut-parleur) : toujours cachées à l'export
            medias = [int(pic.find("p:nvPicPr/p:cNvPr", NS).get("id")) for pic in racine.iter(P + "pic")
                      if pic.find("p:nvPicPr/p:nvPr", NS) is not None
                      and any(e.tag.endswith(("audioFile", "videoFile", "wavAudioFile")) for e in pic.find("p:nvPicPr/p:nvPr", NS))]
            notes_cf: list = []
            formes = _formes_cf(racine, notes_cf)
            medias += [f["spid"] for f in formes]                    # annotations : cachées à l'export, comme les médias
            etats, par_par = _etats(racine, {f["spid"] for f in formes})
            d = {"n": n, "titre": titre, "notes": notes, "duree_s": round(int(m.group(1)) / 1000, 1) if m else None,
                 "audio": audio, "etats": etats, "medias": medias}
            if formes:
                d["formes"] = formes
            if notes_cf:
                d["remarques"] = notes_cf
            if audio and audio.lower().endswith(".wav"):
                try:
                    with wave.open(io.BytesIO(z.read(audio))) as w:
                        d["audio_s"] = round(w.getnframes() / w.getframerate(), 1)
                except Exception:
                    pass
            if par_par:
                d["animation_par_paragraphe"] = True
            diapos.append(d)
    return {"fichier": fichier.name, "largeur_emu": int(taille.get("cx")), "hauteur_emu": int(taille.get("cy")),
            "largeur_pouces": int(taille.get("cx")) / EMU_PAR_POUCE, "hauteur_pouces": int(taille.get("cy")) / EMU_PAR_POUCE,
            "diapos": diapos}


def extraire_audio(fichier: Path, diapos: list[dict], dossier: Path) -> dict:
    """Copie l'audio de narration des diapositives données dans ``<dossier>/audio/dNN.<ext>``.

    Renvoie ``{numéro de diapositive: chemin relatif}``.
    """
    out = {}
    (Path(dossier) / "audio").mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(fichier) as z:
        for d in diapos:
            if not d.get("audio"):
                continue
            rel = f"audio/d{d['n']:02d}{Path(d['audio']).suffix.lower()}"
            (Path(dossier) / rel).write_bytes(z.read(d["audio"]))
            out[d["n"]] = rel
    return out


def plage(texte: str | None, maxi: int) -> list[int]:
    """Convertit une plage (« 6-12 », « 6,8,10-12 ») en liste de numéros de diapositives compris entre 1 et ``maxi``.

    Un texte vide donne toutes les diapositives.
    """
    if not texte:
        return list(range(1, maxi + 1))
    out = []
    for bloc in re.split(r"[,; ]+", texte.strip()):
        if not bloc:
            continue
        a, _, b = bloc.partition("-")
        out += list(range(int(a), int(b or a) + 1))
    return [n for n in out if 1 <= n <= maxi]
