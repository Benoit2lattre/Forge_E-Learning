"""CapsuleForge — créer une capsule neuve (commande ``capsuleforge nouvelle``).

Écrit ``data/capsuleforge/<nom>/chapitre.yaml`` : titre, langue, écran, réglages et les trois parcours habituels
(vue d'ensemble, lecture détaillée, lecture immersive), puis le plan :

- **à partir d'un diaporama** (``diaporama``) : une partie par section PowerPoint s'il y en a au moins deux, sinon une
  seule partie ; dans chaque partie, des sections de quelques minutes faites de diapositives qui se suivent
  (``decoupe`` : ``auto`` = au plus ``minutes`` min d'après le minutage enregistré, ``diapositive`` = une section
  par diapositive, ``une`` = une seule section par partie). Chaque section renvoie à ses diapositives
  (``source: {fichier, diapos}``) : la reprise du diaporama (``capsuleforge pptx``) remplit ensuite les pas ;
- **sans diaporama** : une partie vide, que l'import d'une vidéo ou un enregistrement d'écran remplira.

Le titre d'une section est celui de sa première diapositive (à corriger ensuite si besoin). Une diapositive
masquée dans PowerPoint est laissée de côté. Rien n'est écrasé : le dossier ne doit pas déjà contenir de capsule.

Licence : GPL v3.
"""
from __future__ import annotations

import re
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

import format_chapitre as F
import pptx_lire

P14 = "http://schemas.microsoft.com/office/powerpoint/2010/main"
DUREE_INCONNUE_S = 60.0                  # durée comptée pour une diapositive sans minutage ni son
PARCOURS = [
    {"id": "ensemble", "titre": "Vue d'ensemble", "annexes": "aucune", "questions": "proposees", "exercices": False},
    {"id": "detaillee", "titre": "Lecture détaillée", "annexes": "a_la_demande", "questions": "proposees", "exercices": False},
    {"id": "immersive", "titre": "Lecture immersive", "annexes": "integrees", "questions": "obligatoires", "exercices": True},
]
REGLAGES = {"modes": ["regarder"], "essais": 3, "retours": {"juste": "Oui.", "faux": "Pas tout à fait.", "indice_apres": "essais"}}


def nom_valide(nom: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,47}", nom or ""):
        raise SystemExit(f"Nom de dossier invalide : {nom!r} (lettres sans accent, chiffres, - et _ ; 48 caractères au plus).")
    return nom


def sections_powerpoint(fichier: Path) -> list[tuple[str, list[int]]]:
    """Sections PowerPoint d'un diaporama : [(nom, [numéros des diapositives])] ; [] s'il n'y en a pas."""
    with zipfile.ZipFile(fichier) as z:
        pres = ET.fromstring(z.read("ppt/presentation.xml"))
    ns = {"p": pptx_lire.NS["p"]}
    rang = {sld.get("id"): k for k, sld in enumerate(pres.find("p:sldIdLst", ns), 1)}
    out = []
    for sec in pres.iter("{%s}section" % P14):
        ids = [s.get("id") for s in sec.iter("{%s}sldId" % P14)]
        diapos = [rang[i] for i in ids if i in rang]
        if diapos:
            out.append((sec.get("name") or "", diapos))
    return out


def diapos_masquees(fichier: Path) -> set[int]:
    """Numéros des diapositives masquées dans PowerPoint (``show="0"``)."""
    with zipfile.ZipFile(fichier) as z:
        pres = ET.fromstring(z.read("ppt/presentation.xml"))
        rels = pptx_lire._rels(z, "ppt/presentation.xml")
        out = set()
        for n, sld in enumerate(pres.find("p:sldIdLst", pptx_lire.NS), 1):
            chemin = rels[sld.get("{%s}id" % pptx_lire.NS["r"])][1]
            if re.search(rb'<p:sld\b[^>]*\bshow="0"', z.read(chemin)[:2000]):
                out.add(n)
    return out


def _duree(d: dict) -> float:
    return float(d.get("duree_s") or d.get("audio_s") or DUREE_INCONNUE_S)


def _id(texte: str, pris: set, defaut: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFD", (texte or "").lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    mots = [m for m in re.split(r"[^a-z0-9]+", s) if len(m) > 2][:3]
    base = "_".join(mots)[:24] or defaut
    s, k = base, 2
    while s in pris:
        s, k = f"{base}_{k}", k + 1
    pris.add(s)
    return s


def decouper(diapos: list[dict], decoupe: str, minutes: float) -> list[list[dict]]:
    """Groupes de diapositives consécutives formant les sections d'une partie."""
    if decoupe == "une":
        return [diapos] if diapos else []
    if decoupe == "diapositive":
        return [[d] for d in diapos]
    groupes, courant, total = [], [], 0.0
    for d in diapos:
        if courant and total + _duree(d) > minutes * 60:
            groupes.append(courant)
            courant, total = [], 0.0
        courant.append(d)
        total += _duree(d)
    if courant:
        groupes.append(courant)
    return groupes


def plan_diaporama(fichier: Path, decoupe: str = "auto", minutes: float = 6.0, diapos: str | None = None) -> tuple[list, dict]:
    """Parties et sections proposées pour un diaporama ; renvoie (parties, infos)."""
    lu = pptx_lire.lire(fichier)
    voulues = set(pptx_lire.plage(diapos, len(lu["diapos"])))
    masquees = diapos_masquees(fichier)
    par_n = {d["n"]: d for d in lu["diapos"] if d["n"] in voulues and d["n"] not in masquees}
    secs_pp = [(nom, [n for n in ns if n in par_n]) for nom, ns in sections_powerpoint(fichier)]
    secs_pp = [(nom, ns) for nom, ns in secs_pp if ns]
    if len(secs_pp) < 2:
        secs_pp = [("", sorted(par_n))]
    pris_p, pris_s, parties = set(), set(), []
    for k, (nom, ns) in enumerate(secs_pp, 1):
        groupes = decouper([par_n[n] for n in ns], decoupe, minutes)
        sections = []
        for g in groupes:
            titre = next((d["titre"] for d in g if d["titre"].strip()), "") or (
                f"Diapositive {g[0]['n']}" if len(g) == 1 else f"Diapositives {g[0]['n']} à {g[-1]['n']}")
            sections.append({"id": _id(titre, pris_s, f"s{g[0]['n']}"), "titre": titre,
                             "source": {"fichier": fichier.name, "diapos": [d["n"] for d in g]}})
        titre_p = nom or (lu["diapos"][0]["titre"] if len(secs_pp) == 1 and lu["diapos"] else "") or f"Partie {k}"
        parties.append({"id": _id(titre_p, pris_p, f"p{k}"), "titre": titre_p, "type": "tronc", "place": "libre",
                        "sections": sections})
    infos = {"diapos": len(par_n), "masquees": len(masquees & voulues), "sections_powerpoint": len(secs_pp) if secs_pp[0][0] else 0,
             "duree_s": sum(_duree(d) for d in par_n.values()), "sans_minutage": sum(1 for d in par_n.values() if not (d.get("duree_s") or d.get("audio_s"))),
             "largeur_emu": lu["largeur_emu"], "hauteur_emu": lu["hauteur_emu"]}
    return parties, infos


def creer(dossier: Path, titre: str, langue: str = "fr", diaporama: Path | None = None, decoupe: str = "auto",
          minutes: float = 6.0, diapos: str | None = None) -> dict:
    """Crée la capsule dans ``dossier`` (qui ne doit pas contenir de capsule) ; renvoie le chapitre écrit."""
    dossier = Path(dossier)
    if (dossier / "chapitre.yaml").exists() or (dossier / "capsule.yaml").exists():
        raise SystemExit(f"{dossier.name} contient déjà une capsule : rien n'est écrasé.")
    if decoupe not in ("auto", "diapositive", "une"):
        raise SystemExit("découpe : auto, diapositive ou une")
    ecran = {"largeur": 1920, "hauteur": 1080}
    source = {"statut": "squelette"}
    if diaporama:
        diaporama = Path(diaporama)
        parties, infos = plan_diaporama(diaporama, decoupe, minutes, diapos)
        if len(parties) == 1 and not infos["sections_powerpoint"]:
            parties[0]["titre"] = titre                  # une seule partie : elle porte le titre de la capsule
        ratio = infos["largeur_emu"] / infos["hauteur_emu"]
        ecran = {"largeur": 1440, "hauteur": 1080} if abs(ratio - 4 / 3) < 0.05 else {"largeur": 1920, "hauteur": round(1920 / ratio)}
        source.update({"reference": diaporama.name, "note": "Découpage proposé par « capsuleforge nouvelle » d'après les sections PowerPoint, "
                                                            "les titres et le minutage des diapositives ; à corriger si besoin."})
    else:
        parties, infos = [{"id": "principale", "titre": titre, "type": "tronc", "place": "libre", "sections": []}], {}
    chap = {"format": F.FORMAT, "titre": titre, "langues": {"source": langue}, "ecran": ecran, "source": source,
            "reglages": REGLAGES, "masques": [], "parcours": PARCOURS, "parties": parties}
    dossier.mkdir(parents=True, exist_ok=True)
    F.ecrire(chap, dossier / "chapitre.yaml")
    nb = sum(len(p["sections"]) for p in parties)
    print(f"Capsule « {titre} » créée : {dossier}")
    if diaporama:
        print(f"{diaporama.name} : {infos['diapos']} diapositive(s) retenue(s)"
              + (f", {infos['masquees']} masquée(s) laissée(s) de côté" if infos["masquees"] else "")
              + f", {F.minsec(infos['duree_s'])} au total"
              + (f" ({infos['sans_minutage']} sans minutage, comptées {DUREE_INCONNUE_S:.0f} s)" if infos["sans_minutage"] else ""))
        print(f"Plan proposé : {len(parties)} partie(s), {nb} section(s)"
              + (f", d'après {infos['sections_powerpoint']} sections PowerPoint" if infos["sections_powerpoint"] else ""))
        for p in parties:
            print(f"  {p['titre']}")
            for s in p["sections"]:
                n = s["source"]["diapos"]
                print(f"    {s['titre']}  (diapositive{'s' if len(n) > 1 else ''} {n[0]}{f' à {n[-1]}' if len(n) > 1 else ''})")
        print("Étape suivante : reprendre le diaporama (capsuleforge pptx … --chapitre …) pour les images, les sons et les apparitions.")
    else:
        print("Capsule vide : importez une vidéo (capsuleforge video …) ou filmez l'écran (capsuleforge filmer …) pour créer ses sections.")
    return chap
