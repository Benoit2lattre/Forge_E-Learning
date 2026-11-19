"""Forge E-Learning — versions des conversions QuizForge et registre d'une édition (ou d'un cours).

Une conversion faite pour un cours devient une **version** : un dossier ``quiz/<classeur>/S03_v2/`` (séance si un
plan est demandé, numéro qui s'incrémente par classeur) sous l'édition, ou sous le cours pour un extrait commun à
plusieurs déclinaisons, avec des fichiers au nom explicite et une fiche ``version.yaml`` (date, classeur et son
empreinte, réglages, noms des questions). Rien n'est écrasé ; une reconversion sans changement du classeur ni des
réglages ne crée pas de version (« identique à v2 »).

Le **registre** (``registre.yaml`` du même dossier) a une ligne par version, que l'atelier et DiagForge complètent :
convertie → importée dans Moodle → passée → bilan fait (ou abandonnée), avec dates, test Moodle, bilans, remarques.
DiagForge reconnaît la version d'un bilan d'après les noms des questions de l'export XML de Moodle.
"""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import re
from pathlib import Path

import chemins

FICHIER = "registre.yaml"
ETATS = ("convertie", "importee", "passee", "bilan", "abandonnee")
LIBELLES = {"convertie": "convertie", "importee": "importée dans Moodle", "passee": "passée par les étudiants",
            "bilan": "bilan fait", "abandonnee": "abandonnée"}


def _yaml():
    import yaml
    return yaml


def rel(p) -> str:
    try:
        return Path(p).resolve().relative_to(chemins.RACINE).as_posix()
    except ValueError:
        return str(Path(p).resolve())


def absolu(chemin) -> Path:
    p = Path(chemin)
    return p if p.is_absolute() else chemins.RACINE / p


def maintenant() -> str:
    return dt.datetime.now().strftime("%Y-%m-%d %H:%M")


# --------------------------------------------------------------------------------------------- dossier et registre
def base(r: dict) -> Path:
    """Dossier du registre pour des réglages de cours (``cours_options.resoudre``) : l'édition, sinon le cours."""
    import cours_options  # noqa: F401  (met scripts/forge sur le chemin d'import)
    import cours as K
    c = K.trouver(r["cours"])
    d = K.dossier_cours(c)
    return d / r["declinaison"] / r["edition"] if r.get("declinaison") and r.get("edition") else d


def lire(b: Path) -> dict:
    f = Path(b) / FICHIER
    if not f.is_file():
        return {"versions": []}
    d = _yaml().safe_load(f.read_text(encoding="utf-8")) or {}
    d.setdefault("versions", [])
    return d


def ecrire(b: Path, reg: dict):
    f = Path(b) / FICHIER
    f.parent.mkdir(parents=True, exist_ok=True)
    tete = ("# Registre des versions (Forge) : une ligne par conversion de quiz ou paquet d'exercice, complétée par l'Atelier Forge et "
            "DiagForge ;\n# modifiable à la main (etat : convertie, importee, passee, bilan, abandonnee).\n")
    f.write_text(tete + _yaml().safe_dump(reg, allow_unicode=True, sort_keys=False, width=110), encoding="utf-8",
                 newline="\n")


def tous() -> list[Path]:
    """Dossiers qui ont un registre, dans data/cours et donnees/cours."""
    out = []
    for r in (chemins.DATA / "cours", chemins.DONNEES / "cours"):
        if r.is_dir():
            out += sorted(f.parent for f in r.rglob(FICHIER))
    return out


# --------------------------------------------------------------------------------------------- versions
def empreinte_fichier(f: Path) -> str:
    return hashlib.md5(Path(f).read_bytes()).hexdigest()


def empreinte(f: Path, reglages: dict) -> str:
    return hashlib.md5((empreinte_fichier(f) + json.dumps(reglages, sort_keys=True, ensure_ascii=False,
                                                          default=str)).encode("utf-8")).hexdigest()[:16]


DOSSIERS = {"quiz": "quiz", "exercice": "exercices"}


def genre(v: dict) -> str:
    return v.get("genre") or "quiz"


def nom_source(v: dict) -> str:
    """Nom de ce qui est versionné : classeur (quiz) ou identifiant de la fiche (exercice)."""
    return v.get("nom") or Path(v.get("classeur") or v.get("source") or "").stem


def preparer(b: Path, classeur: Path, seance, emp: str, genre_: str = "quiz", nom: str | None = None) -> dict:
    """Prochaine version d'un classeur ou d'une fiche (dossier, numéro, libellé) ; ``identique`` si une version a déjà
    cette empreinte."""
    reg = lire(b)
    stem = nom or Path(classeur).stem
    miennes = [v for v in reg["versions"] if nom_source(v) == stem and genre(v) == genre_]
    for v in miennes:
        if v.get("empreinte") == emp and absolu(v["dossier"]).is_dir():
            return {"identique": v}
    n = 1 + max([int(v.get("version") or 0) for v in miennes]
                + [int(m.group(1)) for d in (Path(b) / DOSSIERS[genre_] / stem).glob("*v*") if (m := re.search(r"v(\d+)$", d.name))]
                + [0])
    label = (f"S{int(seance):02d}_" if seance else "") + f"v{n}"
    d = Path(b) / DOSSIERS[genre_] / stem / label
    return {"identique": None, "version": n, "label": label, "dossier": d, "id": f"{stem}/{label}", "nom": stem}


def enregistrer_exercice(b: Path, v: dict, fiche: Path, reglages: dict, emp: str, cours: str):
    """Fiche ``version.yaml`` et ligne du registre pour un paquet ExoForge copié dans le dossier de la version."""
    d = Path(v["dossier"])
    date = maintenant()
    infos = {"id": v["id"], "genre": "exercice", "version": v["version"], "date": date, "cours": cours,
             "source": rel(fiche), "empreinte": emp, "reglages": reglages,
             "fichiers": sorted(x.name for x in d.iterdir() if x.is_file() and x.name != "version.yaml")}
    (d / "version.yaml").write_text(_yaml().safe_dump(infos, allow_unicode=True, sort_keys=False, width=110),
                                    encoding="utf-8", newline="\n")
    reg = lire(b)
    reg["versions"].append({"id": v["id"], "genre": "exercice", "nom": v["nom"], "source": rel(fiche),
                            "version": v["version"], "dossier": rel(d), "date": date, "empreinte": emp,
                            "etat": "convertie", "dates": {"convertie": date}, "test_moodle": "", "bilans": [],
                            "utilisee_par": [], "remarques": ""})
    ecrire(b, reg)


def enregistrer(b: Path, v: dict, classeur: Path, reglages: dict, questions: list, seance, emp: str, cours: str):
    """Écrit ``version.yaml`` dans le dossier de la version et ajoute sa ligne au registre."""
    d = Path(v["dossier"])
    fichiers = sorted(x.name for x in d.iterdir() if x.is_file() and x.name != "version.yaml")
    fiche = {"id": v["id"], "version": v["version"], "date": maintenant(), "cours": cours, "classeur": rel(classeur),
             "empreinte_classeur": empreinte_fichier(classeur), "empreinte": emp, "seance": seance, "reglages": reglages,
             "fichiers": fichiers, "questions": [{"nom": str(q.get("titre")), "categorie": str(q.get("categorie"))}
                                                 for q in questions]}
    (d / "version.yaml").write_text(_yaml().safe_dump(fiche, allow_unicode=True, sort_keys=False, width=110),
                                    encoding="utf-8", newline="\n")
    reg = lire(b)
    reg["versions"].append({"id": v["id"], "genre": "quiz", "classeur": rel(classeur), "version": v["version"], "seance": seance,
                            "dossier": rel(d), "date": fiche["date"], "questions": len(questions), "empreinte": emp, "etat": "convertie",
                            "dates": {"convertie": fiche["date"]}, "test_moodle": "", "bilans": [], "utilisee_par": [],
                            "remarques": ""})
    ecrire(b, reg)


def modifier(b: Path, ident: str, champs: dict) -> dict:
    """Change l'état (daté du jour si aucune date n'est donnée), le test Moodle, les remarques, « utilisée par »."""
    reg = lire(b)
    v = next((x for x in reg["versions"] if x.get("id") == ident), None)
    if not v:
        raise ValueError(f"version inconnue : {ident}")
    if champs.get("etat"):
        if champs["etat"] not in ETATS:
            raise ValueError("état inconnu")
        v["etat"] = champs["etat"]
        v.setdefault("dates", {})[champs["etat"]] = str(champs.get("date") or maintenant())
    for k, maxi in (("test_moodle", 120), ("remarques", 1000)):
        if k in champs:
            t = str(champs[k] or "").strip()
            if len(t) > maxi:
                raise ValueError(f"{k} trop long")
            v[k] = t
    if "utilisee_par" in champs:
        v["utilisee_par"] = [str(x) for x in champs["utilisee_par"] or []][:20]
    ecrire(b, reg)
    return v


# --------------------------------------------------------------------------------------------- reconnaissance
def noms_xml(fichiers) -> set[str]:
    """Noms des questions d'exports Moodle XML (les questions « category » ne comptent pas)."""
    import xml.etree.ElementTree as ET
    noms = set()
    for f in fichiers or []:
        try:
            for q in ET.parse(f).getroot().iter("question"):
                if q.get("type") != "category":
                    t = q.find("name/text")
                    if t is not None and (t.text or "").strip():
                        noms.add(t.text.strip())
        except (ET.ParseError, OSError):
            continue
    return noms


def reconnaitre(noms: set, bases) -> dict | None:
    """Version dont les questions ressemblent le plus à ``noms`` : {base, version, score, manquantes, en_trop}."""
    if not noms:
        return None
    meilleure = None
    for b in bases:
        for v in lire(b)["versions"]:
            fv = absolu(v.get("dossier", "")) / "version.yaml"
            try:
                vn = {q["nom"] for q in (_yaml().safe_load(fv.read_text(encoding="utf-8")) or {}).get("questions") or []}
            except OSError:
                continue
            if not vn:
                continue
            commun = len(noms & vn)
            score = commun / len(noms | vn)
            if commun and (not meilleure or score > meilleure["score"]):
                meilleure = {"base": Path(b), "version": v, "score": score, "manquantes": len(vn - noms),
                             "en_trop": len(noms - vn)}
    return meilleure


def noter_bilan(b: Path, ident: str, bilan: Path | None, fiche: Path | None):
    reg = lire(b)
    v = next((x for x in reg["versions"] if x.get("id") == ident), None)
    if not v:
        return
    lien = {"date": maintenant(), "bilan": rel(bilan) if bilan else None, "fiche": rel(fiche) if fiche and fiche.is_file() else None}
    v.setdefault("bilans", []).append({k: x for k, x in lien.items() if x})
    if v.get("etat") != "abandonnee":
        v["etat"] = "bilan"
        v.setdefault("dates", {})["bilan"] = lien["date"]
    ecrire(b, reg)
