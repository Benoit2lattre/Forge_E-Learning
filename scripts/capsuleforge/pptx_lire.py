"""CapsuleForge — lecture d'un diaporama PowerPoint (.pptx), sans PowerPoint.

Lit dans l'archive : titre, notes, durée (minutage enregistré), audio de narration et états d'animation de
chaque diapositive. Un état = ce qui est visible après un clic ; l'état 0 est la diapositive à son ouverture.
Le fichier n'est jamais modifié. Les images sont produites à part, par PowerPoint lui-même (``pptx_images.py``).
:func:`reprendre` fait la reprise complète dans un chapitre (commande ``capsuleforge pptx``).

Formes d'annotation : une forme nommée « cf spot », « cf cadre », « cf pointeur » ou « cf cache » (volet Sélection de
PowerPoint) n'est jamais sur les images ; elle devient un objet du pas. Un pointeur tracé en ligne brisée
(forme libre) ou en trait donne une trajectoire.

Habillage (lot 6) : une forme « cf édition » n'est montrée que dans une capsule habillée pour une édition,
« cf édition ecole1 » seulement pour ce public (école ou variante), « cf nu » seulement dans la capsule nue ;
un texte ``{cours}``, ``{code}``, ``{promo}``… est un champ, rempli à l'export d'une édition (vide dans la
capsule nue). La lecture les repère (``edition``, ``champs``, ``pieds``) ; l'export est fait par ``pptx_images``.

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
        morceaux = []
        for e in par.iter():
            if e.tag == "{%s}t" % NS["a"]:
                morceaux.append(e.text or "")
            elif e.tag == "{%s}br" % NS["a"]:              # retour à la ligne dans un paragraphe (Maj+Entrée)
                morceaux.append("\n")
        lignes.extend("".join(morceaux).split("\n"))
    return "\n".join(l for l in lignes if l.strip()).strip()


PREFIXE = "cf"                                     # formes d'annotation : nommées « cf spot », « cf pointeur »…
TYPES_CF = {"spot": "spot", "cadre": "cadre", "pointeur": "pointeur", "pointer": "pointeur", "cache": "cache"}


def _type_cf(nom: str) -> str | None:
    """Renvoie le type d'objet d'un nom de forme d'annotation (« cf spot », « CF-Pointeur 2 », « cf: cadre »…).

    Renvoie ``None`` si le nom n'est pas celui d'une annotation.
    """
    m = re.match(r"^\s*cf[\s:_-]+([a-zà-ÿ]+)", (nom or "").lower())
    return TYPES_CF.get(m.group(1)) if m else None


CHAMPS = ("cours", "code", "bloc", "promo", "annee", "ecole", "declinaison", "edition", "enseignant", "capsule")
CHAMP = re.compile(r"\{(" + "|".join(CHAMPS) + r")\}")
EDITION = re.compile(r"^\s*cf[\s:_-]+(édition|edition|nu)(?=$|[\s:_,;-])[\s:_,;-]*(.*)$")


def _cas_edition(nom: str) -> tuple[str, list[str]] | None:
    """Renvoie ``("edition", publics)`` pour « cf édition [public…] », ``("nu", [])`` pour « cf nu », sinon ``None``.

    Les publics (noms d'école ou de variante) sont séparés par des espaces ou des virgules ; une liste vide veut
    dire « toute édition ».
    """
    m = EDITION.match((nom or "").lower())
    if not m:
        return None
    if m.group(1) == "nu":
        return "nu", []
    return "edition", [x for x in re.split(r"[\s,;]+", m.group(2)) if x]


def _formes_edition(racine) -> list[dict]:
    """Renvoie les formes d'édition d'une diapositive (« cf édition … », « cf nu »), groupes compris :
    ``[{spid, nom, cas, publics}]``."""
    arbre = racine.find("p:cSld/p:spTree", NS)
    out = []
    if arbre is None:
        return out
    for c in arbre.iter(P + "cNvPr"):
        cas = _cas_edition(c.get("name"))
        if cas:
            out.append({"spid": int(c.get("id")), "nom": c.get("name"), "cas": cas[0], "publics": cas[1]})
    return out


def _champs(racine) -> dict:
    """Renvoie les champs (``{cours}``, ``{promo}``…) des formes de texte et des tableaux : ``{spid: [noms]}``.

    Un champ coupé en plusieurs morceaux de mise en forme est reconnu (le texte du paragraphe est recollé).
    """
    A = "{%s}" % NS["a"]
    out = {}
    arbre = racine.find("p:cSld/p:spTree", NS)
    if arbre is None:
        return out
    for el in arbre.iter():
        if el.tag not in (P + "sp", P + "graphicFrame"):
            continue
        c = el.find("*/p:cNvPr", NS)
        if c is None:
            continue
        noms = []
        for par in el.iter(A + "p"):
            t = "".join(x.text or "" for x in par.iter(A + "t"))
            noms += [m.group(1) for m in CHAMP.finditer(t)]
        if noms:
            out[int(c.get("id"))] = sorted(set(noms))
    return out


def _pieds(racine) -> list[int]:
    """Renvoie les espaces réservés de pied de page et de date d'une diapositive (cachés avec le masque nu)."""
    out = []
    for sp in racine.iter(P + "sp"):
        ph = sp.find("p:nvSpPr/p:nvPr/p:ph", NS)
        if ph is not None and ph.get("type") in ("ftr", "dt"):
            out.append(int(sp.find("p:nvSpPr/p:cNvPr", NS).get("id")))
    return out


SEPARATEURS = " \t·•|,;:/—–-"


def remplir_texte(texte: str, valeurs: dict) -> str:
    """Remplit les champs ``{cours}``… d'un texte ; un champ vide part avec un séparateur voisin, comme à l'export
    PowerPoint (« Benoit Delattre - {code} » → « Benoit Delattre » dans la capsule nue)."""
    lignes = []
    for t in str(texte or "").split("\n"):
        for _ in range(50):
            m = CHAMP.search(t)
            if not m:
                break
            v = str(valeurs.get(m.group(1)) or "")
            if v:
                t = t[:m.start()] + v + t[m.end():]
                continue
            i, j = m.start(), m.end()
            k = i
            while k > 0 and t[k - 1] in SEPARATEURS:
                k -= 1
            n = j
            while n < len(t) and t[n] in SEPARATEURS:
                n += 1
            t = t[:k] + t[j:] if n == len(t) else t[:i] + t[n:]
        lignes.append(t)
    return "\n".join(lignes).strip()


def vide(texte: str) -> bool:
    """Vrai si un texte n'a plus que des espaces et des séparateurs."""
    return not re.sub(r"[\s·•|,;:/—–\-()]+", "", texte or "")


def _latex_iguanatex(z: zipfile.ZipFile, rels_diapo: dict, el) -> str | None:
    """Renvoie la formule LaTeX d'une équation IguanaTeX (étiquette ``LATEXADDIN`` de la forme), sans préambule."""
    nv = next((x for x in el if x.tag.endswith("Pr") and x.tag.startswith(P + "nv")), None)
    if nv is None:
        return None
    for t in nv.iter(P + "tags"):
        cible = rels_diapo.get(t.get("{%s}id" % NS["r"]))
        if not cible or cible[1] not in z.namelist():
            continue
        for tag in ET.fromstring(z.read(cible[1])).iter(P + "tag"):
            if tag.get("name") == "LATEXADDIN":
                src = tag.get("val") or ""
                corps = src.split("\\begin{document}")[-1].split("\\end{document}")[0]
                corps = corps.strip()
                for a, b in (("$$", "$$"), ("\\[", "\\]"), ("$", "$")):
                    if corps.startswith(a) and corps.endswith(b) and len(corps) > len(a) + len(b):
                        corps = corps[len(a):-len(b)]
                        break
                return " ".join(corps.split()) or None
    return None


def _xfrm(el) -> tuple[int, int]:
    """Coin haut-gauche d'une forme (``y, x``) pour l'ordre de lecture ; (0, 0) si la forme n'a pas de position."""
    x = el.find("p:spPr/a:xfrm/a:off", NS)
    if x is None:
        x = el.find("p:grpSpPr/a:xfrm/a:off", NS)
    if x is None:
        x = el.find("p:xfrm/a:off", NS)
    return (int(x.get("y")), int(x.get("x"))) if x is not None else (0, 0)


def _etat_de(spids: list, par: int | None, etats: list) -> int:
    """Premier état où un élément est visible : la forme (ou l'un de ses groupes) et, s'il y a lieu, son paragraphe."""
    for k, caches in enumerate(etats):
        cache = False
        for c in caches:
            if isinstance(c, list):
                if par is not None and c[0] in spids and c[1] <= par <= c[2]:
                    cache = True
            elif c in spids:
                cache = True
        if not cache:
            return k
    return max(0, len(etats) - 1)


def texte_diapo(z: zipfile.ZipFile, chemin: str, racine, etats: list) -> list[dict]:
    """Texte d'une diapositive, dans l'ordre de lecture (titre d'abord, puis de haut en bas et de gauche à droite).

    Blocs : ``{texte, titre: true}``, ``{texte, niveau}`` (un paragraphe, niveau de puce à partir de 0),
    ``{formule}`` (LaTeX d'une équation IguanaTeX), ``{cellules: [[{texte}…]…]}`` (tableau). Chaque bloc porte, s'il
    y a lieu, ``etat`` (premier état où il est visible) et, pour une forme d'édition, ``cas`` et ``publics``. Les
    annotations « cf … », les médias, les images et les pieds de page n'y sont pas ; les champs ``{cours}``… restent
    écrits tels quels (remplis à la construction).
    """
    A = "{%s}" % NS["a"]
    rels = _rels(z, chemin)
    arbre = racine.find("p:cSld/p:spTree", NS)
    titres, autres = [], []

    def ajouter(liste, bloc, spids, par, ed):
        k = _etat_de(spids, par, etats)
        if k:
            bloc["etat"] = k
        if ed:
            bloc["cas"] = ed[0]
            if ed[1]:
                bloc["publics"] = ed[1]
        liste.append(bloc)

    def visiter(el, ancetres: list, ed):
        c = el.find("*/p:cNvPr", NS)
        if c is None:
            return
        spid, nom = int(c.get("id")), c.get("name") or ""
        if _type_cf(nom):
            return                                                    # annotation : jamais du texte de diapositive
        ed = _cas_edition(nom) or ed
        spids = ancetres + [spid]
        latex = _latex_iguanatex(z, rels, el)
        if latex:
            ajouter(autres, {"formule": latex}, spids, None, ed)
            return
        if el.tag == P + "grpSp":
            for e in sorted((e for e in el if e.tag in (P + "sp", P + "grpSp", P + "graphicFrame", P + "pic")), key=_xfrm):
                visiter(e, spids, ed)
            return
        if el.tag == P + "graphicFrame":
            tbl = el.find(".//" + A + "tbl")
            if tbl is not None:
                lignes = [[{"texte": _texte(tc).replace("\n", " ")} for tc in tr.findall(A + "tc")] for tr in tbl.findall(A + "tr")]
                if any(x["texte"] for l in lignes for x in l):
                    ajouter(autres, {"cellules": lignes}, spids, None, ed)
            return
        if el.tag != P + "sp":
            return                                                    # image, média, connecteur
        ph = el.find("p:nvSpPr/p:nvPr/p:ph", NS)
        if ph is not None and ph.get("type") in ("ftr", "dt", "sldNum"):
            return
        corps = el.find("p:txBody", NS)
        if corps is None:
            return
        titre = ph is not None and ph.get("type") in ("title", "ctrTitle")
        for i, par in enumerate(corps.findall(A + "p")):
            t = _texte(par).replace("\n", " ").strip()
            if not t:
                continue
            if titre:
                ajouter(titres, {"texte": t, "titre": True}, spids, i, ed)
            else:
                ppr = par.find(A + "pPr")
                niveau = int(ppr.get("lvl") or 0) if ppr is not None else 0
                ajouter(autres, {"texte": t, "niveau": niveau} if niveau else {"texte": t}, spids, i, ed)

    if arbre is None:
        return []
    for el in sorted((e for e in arbre if e.tag in (P + "sp", P + "grpSp", P + "graphicFrame", P + "pic")), key=_xfrm):
        visiter(el, [], None)
    out, vus = [], set()
    for b in titres + autres:
        if b.get("formule") is not None and _etiquette(b["formule"]):
            continue                                                  # « F », « σ » posés sur un schéma
        if b.get("texte") is not None and not re.search(r"[^\W\d_]", b["texte"]):
            continue                                                  # « 1. », « 0. » : numéros de section
        cle = repr({k: v for k, v in b.items() if k != "etat"})
        if cle in vus:
            continue
        vus.add(cle)
        out.append(b)
    return out


def _etiquette(latex: str) -> bool:
    """Vrai si une formule n'est qu'un symbole (lettre, lettre grecque), une fois retirées les commandes de couleur
    à un argument (``\\TR{F}``) : une étiquette de schéma, pas du texte à lire."""
    t = latex
    for _ in range(5):
        t2 = re.sub(r"\\[A-Za-z]+\s*\{\s*(.*?)\s*\}$", r"\1", t.strip())
        if t2 == t:
            break
        t = t2
    return bool(re.fullmatch(r"\s*(\\[A-Za-z]+|[A-Za-z])\s*(_\{?\w\}?)?\s*", t))


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
    ses formes d'annotation (``formes``), ses formes d'édition (``edition``), ses champs (``champs`` :
    ``{spid: [noms]}``), ses pieds de page (``pieds``) et les remarques de lecture (``remarques``). Le diaporama porte
    ``champs_masque`` : les champs écrits dans les masques et les dispositions.
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
            d["texte_diapo"] = texte_diapo(z, chemin, racine, etats)
            ed, ch, pi = _formes_edition(racine), _champs(racine), _pieds(racine)
            if ed:
                d["edition"] = ed
            if ch:
                d["champs"] = ch
            if pi:
                d["pieds"] = pi
            diapos.append(d)
        champs_masque = sorted({c for n in z.namelist() if re.match(r"ppt/(slideMasters|slideLayouts)/[^/]+\.xml$", n)
                                for v in _champs(ET.fromstring(z.read(n))).values() for c in v})
    return {"fichier": fichier.name, "champs_masque": champs_masque, "largeur_emu": int(taille.get("cx")), "hauteur_emu": int(taille.get("cy")),
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


def _recouvre(c1, c2) -> float:
    """Part de la plus petite des deux zones ``[x, y, l, h]`` couverte par l'autre."""
    lx = min(c1[0] + c1[2], c2[0] + c2[2]) - max(c1[0], c2[0])
    ly = min(c1[1] + c1[3], c2[1] + c2[3]) - max(c1[1], c2[1])
    return max(0, lx) * max(0, ly) / max(1, min(c1[2] * c1[3], c2[2] * c2[3]))


SOURCE_PPTX = ("type", "fichier", "diapo", "etats", "titre", "animation_par_paragraphe")
PAS_PPTX = ("id", "fond", "source", "narration", "phrases", "audio", "duree_s", "objets", "texte_diapo")


def garder_traductions(neuf: list[dict], vieux: list[dict] | None, src: str) -> list[dict]:
    """Reporte sur le texte de diapositive relu ``neuf`` les traductions de ``vieux`` dont le texte source n'a pas
    changé (textes ``{fr: …, en: …}`` du chapitre)."""
    connus: dict = {}

    def noter(v):
        if isinstance(v, dict) and v.get(src):
            connus.setdefault(" ".join(str(v[src]).split()), v)
    for b in vieux or []:
        noter(b.get("texte"))
        for l in b.get("cellules") or []:
            for c in l:
                noter(c.get("texte"))

    def reprendre_v(v):
        if not isinstance(v, str):
            return v
        ancien = connus.get(" ".join(v.split()))
        return {**ancien, src: v} if ancien else v
    for b in neuf:
        if "texte" in b:
            b["texte"] = reprendre_v(b["texte"])
        for l in b.get("cellules") or []:
            for c in l:
                c["texte"] = reprendre_v(c["texte"])
    return neuf


def _garder(q: dict, vieux: dict, enregistre: bool):
    """Reporte dans le pas repris ``q`` ce que l'ancien pas avait en plus de ce que donne le diaporama.

    Gardés : voix de synthèse des autres langues (``voix``), caméra, gestes et autres champs du pas, et les champs de
    ``source`` que la reprise ne réécrit pas. Une voix de synthèse en langue source (``source.voix: synthese``)
    est gardée avec son son seulement si la diapositive n'a pas d'enregistrement ; sinon l'enregistrement la remplace.
    """
    src = {k: v for k, v in (vieux.get("source") or {}).items() if k not in q["source"] and k not in SOURCE_PPTX}
    if enregistre:
        src = {k: v for k, v in src.items() if not k.startswith("voix")}
    elif src.get("voix") == "synthese" and vieux.get("audio"):
        q["audio"] = vieux["audio"]
        if vieux.get("duree_s"):
            q["duree_s"] = vieux["duree_s"]
    q["source"].update(src)
    for k, v in vieux.items():
        if k not in q and k not in PAS_PPTX:
            q[k] = v


def dispositions(fichier: Path) -> dict:
    """Lit sans PowerPoint ce qui compte pour appliquer un modèle : taille des diapositives (EMU), noms des
    dispositions du fichier et de chaque diapositive, champs des masques. Marche pour un .pptx ou un .potx."""
    out = {"taille": None, "dispositions": [], "diapos": {}, "champs_masque": []}
    with zipfile.ZipFile(fichier) as z:
        pres = ET.fromstring(z.read("ppt/presentation.xml"))
        t = pres.find("p:sldSz", NS)
        out["taille"] = [int(t.get("cx")), int(t.get("cy"))] if t is not None else None
        noms = {}
        champs = set()
        for n in z.namelist():
            if re.match(r"ppt/slideLayouts/slideLayout\d+\.xml$", n):
                r = ET.fromstring(z.read(n))
                c = r.find("p:cSld", NS)
                noms[n] = (c.get("name") if c is not None else "") or ""
            if re.match(r"ppt/(slideMasters|slideLayouts)/[^/]+\.xml$", n):
                champs |= {x for v in _champs(ET.fromstring(z.read(n))).values() for x in v}
        out["dispositions"] = sorted(set(noms.values()))
        out["champs_masque"] = sorted(champs)
        lst = pres.find("p:sldIdLst", NS)
        rels = _rels(z, "ppt/presentation.xml")
        for k, sld in enumerate(lst if lst is not None else [], 1):
            chemin = rels[sld.get("{%s}id" % NS["r"])][1]
            lay = next((c for t_, c in _rels(z, chemin).values() if t_ == "slideLayout"), None)
            out["diapos"][k] = noms.get(lay, "")
    return out


def masque_chapitre(chap: dict) -> str:
    """Masque des diapositives PowerPoint du chapitre (clé ``powerpoint: {masque: …}``) : ``nu`` (défaut, formes du
    masque et pieds de page cachés) ou ``garder`` (masque neutre, montré partout)."""
    m = str(((chap.get("powerpoint") or {}).get("masque")) or "nu").lower()
    return "garder" if m in ("garder", "garde", "montrer") else "nu"


def reprendre(src: Path, y: Path, diapos: str | None = None, largeur: int | None = None, images: bool = True) -> dict:
    """Reprend le diaporama ``src`` dans les sections du chapitre ``y`` qui y renvoient ; renvoie le chapitre écrit.

    Les sections visées sont celles dont ``source.fichier`` est le nom du diaporama et dont ``source.diapos``
    contient une des diapositives demandées (``diapos`` : « 6-12 », « 3,5 »… ; toutes si ``None``). Chaque
    diapositive devient un pas (image, audio, durée), chaque clic d'animation une apparition, et les formes
    d'annotation des objets ; le texte déjà relu et les réglages de temps existants sont conservés. Les images sont
    celles de la capsule nue : formes « cf édition » cachées, champs vides, masque caché sauf ``powerpoint: {masque:
    garder}`` dans le chapitre (``pptx_edition`` refait celles d'une édition).

    Écrit les images avec PowerPoint (``pptx_images``, sauf si ``images`` est faux), ``pptx_journal.txt``, une copie
    de l'ancien chapitre dans ``sauvegardes/`` et le nouveau ``chapitre.yaml``. ``largeur`` : largeur des images
    (par défaut celle de l'écran du chapitre, sinon 1440).
    """
    import shutil
    import time
    import format_chapitre as F
    src, y = Path(src), Path(y)
    dossier = y.parent
    chap = F.lire(y)
    lu = lire(src)
    voulues = set(plage(diapos, len(lu["diapos"])))
    par_n = {d["n"]: d for d in lu["diapos"]}
    cibles = [(p, s) for p in chap.get("parties") or [] for s in p.get("sections") or []
              if (s.get("source") or {}).get("fichier") == src.name
              and any(n in voulues for n in (s.get("source") or {}).get("diapos") or [])]
    if not cibles:
        raise SystemExit(f"Aucune section de {y.name} ne renvoie à {src.name} pour ces diapositives "
                         "(champ source: {fichier, diapos} de la section).")
    a_faire = sorted({n for _, s in cibles for n in s["source"]["diapos"] if n in voulues and n in par_n})
    a_lire = [par_n[n] for n in a_faire]
    print(f"{src.name} : {len(lu['diapos'])} diapositives ; {len(a_faire)} à reprendre, "
          f"{sum(len(d['etats']) for d in a_lire)} états d'animation")
    audios = extraire_audio(src, a_lire, dossier)
    largeur = largeur or (chap.get("ecran") or {}).get("largeur") or 1440
    journal = dossier / "pptx_journal.txt"          # relu ensuite sans avoir à copier la console

    def noter(ligne):
        print(ligne)
        with open(journal, "a", encoding="utf-8") as f:
            f.write(ligne + "\n")

    journal.write_text(f"{time.strftime('%Y-%m-%d %H:%M:%S')} {src.name} diapos {a_faire}\n", encoding="utf-8")
    if not images:
        noter("  images non produites (--sans-images)")
    else:
        import traceback
        import pptx_images
        masque = masque_chapitre(chap)
        for d in a_lire:                                # habillage repéré : à remplir pour chaque édition
            ed = ", ".join(f["nom"] for f in d.get("edition") or [])
            ch = ", ".join("{" + c + "}" for c in sorted({c for v in (d.get("champs") or {}).values() for c in v}))
            if ed or ch:
                noter(f"  diapositive {d['n']} : " + " ; ".join(x for x in (ed and f"formes d'édition {ed}",
                                                                             ch and f"champs {ch}") if x))
        if lu.get("champs_masque") and masque == "garder":
            noter(f"  masque : champs {', '.join('{' + c + '}' for c in lu['champs_masque'])}")
        noter(f"  capsule nue : formes « cf édition » cachées, champs vides, masque {'gardé' if masque == 'garder' else 'caché'}")
        try:
            ecrits = pptx_images.exporter(src, a_lire, dossier, largeur, journal=noter,
                                          edition={"publics": None, "champs": {}, "masque": masque})
            noter(f"  {len(ecrits)} images écrites dans {dossier / 'images'}")
        except BaseException:
            noter(traceback.format_exc())
            raise SystemExit(f"L'export des images a échoué : voir {journal}")
    import os
    try:                                                # noté pour retrouver le diaporama à la construction d'une édition
        chemin = Path(os.path.relpath(src.resolve(), dossier.resolve())).as_posix()
    except ValueError:                                  # autre lecteur (Windows) : pas de chemin relatif
        chemin = None
    N = F.noms(chap)
    for partie, sec in cibles:
        if chemin and chemin != src.name:
            sec["source"]["chemin"] = chemin
        anciens = {(q.get("source") or {}).get("diapo"): q for q in sec.get("pas") or [] if (q.get("source") or {}).get("type") == "pptx"}
        autres = [q for q in sec.get("pas") or [] if (q.get("source") or {}).get("type") != "pptx"]
        nouveaux = []
        for n in sec["source"]["diapos"]:
            d, vieux = par_n.get(n), anciens.get(n)
            if d is None or n not in voulues:
                if vieux:
                    nouveaux.append(vieux)
                continue
            K = len(d["etats"])
            duree = d.get("audio_s") or d.get("duree_s")
            q = {"id": f"d{n:02d}", "fond": f"images/d{n:02d}_e0.png",
                 "source": {"type": "pptx", "fichier": src.name, "diapo": n, "etats": K, "titre": d["titre"]},
                 "narration": (vieux or {}).get("narration") or d["notes"] or ""}
            if (vieux or {}).get("phrases"):            # texte déjà relu : gardé tel quel
                q["phrases"] = vieux["phrases"]; q.pop("narration")
            for cle in ("narration", "minutage", "relu"):
                if cle in ((vieux or {}).get("source") or {}):
                    q["source"][cle] = vieux["source"][cle]
            if n in audios:
                q["audio"] = audios[n]
            if duree:
                q["duree_s"] = duree
            if vieux:                                   # ce que la reprise ne produit pas est gardé
                _garder(q, vieux, enregistre=n in audios)
            deja = {o.get("id"): o for o in (vieux or {}).get("objets") or []}
            objets = []
            for k in range(1, K):                       # instants répartis, sauf réglage déjà fait
                o = {"id": f"e{k}", "type": "apparition", "fichier": f"images/d{n:02d}_e{k}.png",
                     "debut_s": (deja.get(f"e{k}") or {}).get("debut_s") or round((duree or 4.0 * K) * k / K, 1)}
                objets.append(o)
            # annotations dessinées dans PowerPoint (formes « cf … ») : géométrie relue, réglages de temps gardés
            k_emu = largeur / lu["largeur_emu"]
            formes = d.get("formes") or []
            manuels = [o for o in (vieux or {}).get("objets") or [] if o.get("type") == "cache" and o.get("origine") != "pptx"]

            for i, f in enumerate(formes):
                o = {"id": f"f{f['spid']}", "type": f["type"], "origine": "pptx"}
                if f["type"] == "cache":
                    zone = [round(v * k_emu) for v in f["cadre"]]
                    if any(_recouvre(zone, m["cadre"]) > 0.5 for m in manuels if m.get("cadre")):
                        noter(f"  diapositive {n} : « {f['nom']} » non repris, un cache posé dans la relecture couvre déjà cette zone")
                        continue
                if f.get("forme"):
                    o["forme"] = f["forme"]
                if f["type"] == "pointeur":
                    pts = f.get("trajet") or [[f["cadre"][0] + f["cadre"][2] / 2, f["cadre"][1] + f["cadre"][3] / 2]]
                    pts = [[round(px * k_emu), round(py * k_emu)] for px, py in pts]
                    o["position"] = list(pts[0])
                    if len(pts) > 1:
                        o["trajet"] = pts
                else:
                    o["cadre"] = [round(v * k_emu) for v in f["cadre"]]
                v = deja.get(o["id"]) or {}
                o["debut_s"] = v["debut_s"] if v.get("debut_s") is not None else round((duree or 20.0) * (i + 1) / (len(formes) + 1), 1)
                o["duree_s"] = v.get("duree_s") or 4.0
                if f["type"] == "cache":                # un cache part du début du pas ; sa durée est l'instant où il est levé
                    o["duree_s"] = v.get("duree_s") or o["debut_s"]
                    o["debut_s"] = 0.0
                    o["couleur"] = v.get("couleur") or "#ffffff"
                objets.append(F.ordonner(o, F.ORDRE_OBJET))
            for r in d.get("remarques") or []:
                noter(f"  diapositive {n} : {r}")
            objets += [o for o in (vieux or {}).get("objets") or []
                       if o.get("type") != "apparition" and o.get("origine") != "pptx"]
            if objets:
                q["objets"] = objets
            if d.get("animation_par_paragraphe"):
                q["source"]["animation_par_paragraphe"] = True
            if d.get("texte_diapo"):                    # texte de la diapositive, lisible et traduisible (volet Texte)
                q["texte_diapo"] = garder_traductions(d["texte_diapo"], (vieux or {}).get("texte_diapo"),
                                                      (chap.get("langues") or {}).get("source") or "fr")
            nouveaux.append(F.ordonner(q, F.ORDRE_PAS))
        sec["pas"] = nouveaux + autres
        d_tot = sum(q.get("duree_s") or 0 for q in nouveaux)
        sec["source"]["duree_s"] = round(d_tot, 1) or sec["source"].get("duree_s")
        print(f"  {N[('section', partie.get('id'), sec.get('id'))]} {F.texte(sec.get('titre'))} : {len(nouveaux)} pas, "
              f"{sum(1 for q in nouveaux for o in q.get('objets') or [] if o.get('type') == 'apparition')} apparitions, "
              f"{sum(1 for q in nouveaux for o in q.get('objets') or [] if o.get('origine') == 'pptx')} annotations, {F.minsec(d_tot)}")
    ecran = chap.setdefault("ecran", {})
    ecran["largeur"] = largeur
    ecran["hauteur"] = round(largeur * lu["hauteur_pouces"] / lu["largeur_pouces"])
    if y.is_file():
        (dossier / "sauvegardes").mkdir(exist_ok=True)
        shutil.copy2(y, dossier / "sauvegardes" / f"chapitre_{time.strftime('%Y%m%d_%H%M%S')}.yaml")
    F.ecrire(chap, y)
    print(f"-> {y}")
    return chap
