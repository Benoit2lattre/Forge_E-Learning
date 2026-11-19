"""Atelier Forge — écrans « Questions » (QuizForge) et « Bilans » (DiagForge) : listes et commandes.

Questions : classeurs QuizForge de ``data/quizforge`` et des exemples ; valider, convertir pour Moodle (avec plan de
séance), créer un classeur modèle, réunir un classeur et sa traduction.
Bilans : dossiers d'exports Moodle de ``data/diagforge`` et des exemples ``donnees/diagforge`` ; faire le bilan.

Licence : GPL v3.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / "commun"))
import chemins                    # noqa: E402

QUIZFORGE = chemins.SCRIPTS / "quizforge" / "quizforge.py"
DIAGFORGE = chemins.SCRIPTS / "diagforge" / "diagforge.py"
EXEMPLES_Q = chemins.OUTILS / "quizforge" / "exemples" / "classeurs"
EXEMPLES_D = chemins.RACINE / "donnees" / "diagforge"


def rel(p: Path) -> str:
    try:
        return Path(p).resolve().relative_to(chemins.RACINE).as_posix()
    except ValueError:
        return str(p)


def _date(p: Path):
    return p.stat().st_mtime if p.exists() else None


# ------------------------------------------------------------------------------------------------ Questions
def _resume_classeur(f: Path, origine: str) -> dict:
    sortie = f.parent / f"{f.stem}_QuizForge"
    plans = sorted(f.parent.glob(f"{f.stem}_plan_S*.md"))
    converti = _date(sortie / "rapport.txt") or _date(sortie)
    return {"classeur": rel(f), "nom": f.name, "dossier": rel(f.parent), "origine": origine,
            "modifie": _date(f), "converti": converti, "a_refaire": bool(converti and f.stat().st_mtime > converti),
            "sortie": rel(sortie) if sortie.exists() else None, "plans": [rel(p) for p in plans]}


def _bases_cours(type_: str) -> list[Path]:
    try:
        import cours
        return cours.Index().dossiers(type_)
    except Exception:
        return []


def classeurs(ajoutes: list | None = None) -> list[dict]:
    """Classeurs QuizForge : data/quizforge (privés), classeurs ajoutés par l'atelier, puis exemples."""
    out, vus = [], set()
    for f in sorted((chemins.DATA / "quizforge").rglob("*.xlsx") if (chemins.DATA / "quizforge").is_dir() else [], key=lambda x: str(x).lower()):
        if f.name.startswith(("~$", "bilan_")) or any(p.endswith("_QuizForge") for p in f.relative_to(chemins.DATA).parts[:-1]):
            continue
        out.append(_resume_classeur(f, "data"))
        vus.add(f.resolve())
    for base in _bases_cours("questions"):              # dossiers désignés par les cours (et leur questions/)
        for f in sorted(base.rglob("*.xlsx") if base.is_dir() else [base], key=lambda x: str(x).lower()):
            if (f.suffix.lower() != ".xlsx" or f.name.startswith(("~$", "bilan_")) or f.resolve() in vus
                    or any(p.endswith("_QuizForge") for p in f.parts[:-1])):
                continue
            out.append(_resume_classeur(f, "cours"))
            vus.add(f.resolve())
    for c in ajoutes or []:
        f = Path(c)
        if f.is_file() and f.resolve() not in vus:
            out.append(_resume_classeur(f, "ajoute"))
            vus.add(f.resolve())
    for f in sorted(EXEMPLES_Q.glob("*.xlsx")) if EXEMPLES_Q.is_dir() else []:
        if not f.name.startswith("~$") and f.resolve() not in vus:
            out.append(_resume_classeur(f, "exemple"))
    return out


def classeur_valide(chemin: str) -> Path:
    f = Path(chemin)
    f = f if f.is_absolute() else chemins.RACINE / f
    if f.suffix.lower() != ".xlsx" or not f.is_file():
        raise ValueError("classeur introuvable (fichier .xlsx)")
    return f


def texte_court(v: str, maxi: int = 80) -> str:
    v = (v or "").strip()
    if len(v) > maxi or any(c in v for c in "\r\n\0"):
        raise ValueError("texte trop long ou sur plusieurs lignes")
    return v


# ------------------------------------------------------------------------------------------------ Bilans
def dossiers_exports() -> list[dict]:
    """Dossiers qui contiennent un export « notes » de Moodle (CSV ou classeur), avec leur bilan s'il existe."""
    out, vus = [], set()
    for base, origine in [(chemins.DATA / "diagforge", "data")] + [(b, "cours") for b in _bases_cours("exports")] + [(EXEMPLES_D, "exemple")]:
        if not base.is_dir():
            continue
        for f in sorted(base.rglob("*")):
            if f.suffix.lower() not in (".csv", ".xlsx") or f.name.startswith(("~$", "bilan_")):
                continue
            if not re.search(r"notes|grades", f.name, re.IGNORECASE) or len(f.relative_to(base).parts) > 5:
                continue
            d = f.parent
            if d in vus:
                continue
            vus.add(d)
            fichiers = sorted(x.name for x in d.iterdir() if x.is_file() and x.suffix.lower() in (".csv", ".xlsx", ".xml")
                              and not x.name.startswith(("~$", "bilan_")))
            bilans = sorted(d.glob("bilan_*.xlsx"), key=lambda x: x.stat().st_mtime, reverse=True)
            fiche = bilans[0].with_name(bilans[0].stem + "_fiche_prof.html") if bilans else None
            out.append({"dossier": rel(d), "nom": d.name, "parent": rel(d.parent), "origine": origine, "fichiers": fichiers,
                        "xml": [x for x in fichiers if x.lower().endswith(".xml")],
                        "roster": [x for x in fichiers if x.lower().startswith(("roster", "etudiants", "liste"))],
                        "bilan": rel(bilans[0]) if bilans else None, "bilan_date": _date(bilans[0]) if bilans else None,
                        "fiche": rel(fiche) if fiche and fiche.is_file() else None,
                        "a_refaire": bool(bilans and max(_date(d / x) or 0 for x in fichiers) > bilans[0].stat().st_mtime)})
    return out


def dossier_valide(chemin: str) -> Path:
    d = Path(chemin)
    d = d if d.is_absolute() else chemins.RACINE / d
    if not d.is_dir():
        raise ValueError("dossier d'exports introuvable")
    return d


def fichier_dans(d: Path, nom: str, extensions: tuple) -> Path:
    """Fichier ``nom`` du dossier ``d`` (nom simple) ou chemin choisi par Parcourir."""
    f = Path(nom)
    f = f if f.is_absolute() else d / f
    if f.suffix.lower() not in extensions or not f.is_file():
        raise ValueError(f"fichier introuvable : {nom}")
    return f


def liens_bilan(d: Path, debut: float) -> dict:
    neufs = sorted((b for b in d.glob("bilan_*.xlsx") if b.stat().st_mtime >= debut - 1), key=lambda b: b.stat().st_mtime)
    if not neufs:
        return {}
    b = neufs[-1]
    out = {"classeur": rel(b)}
    fiche = b.with_name(b.stem + "_fiche_prof.html")
    if fiche.is_file():
        out["fiche"] = rel(fiche)
    return out
