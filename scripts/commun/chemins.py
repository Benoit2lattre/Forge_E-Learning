"""Forge E-Learning — chemins communs à tous les outils (un seul endroit à modifier si l'arborescence change).

Chaque script ajoute scripts/commun au chemin d'import puis fait ``import chemins``.
"""
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]       # dossier du dépôt
SCRIPTS = RACINE / "scripts"
OUTILS = RACINE / "outils"                          # modes d'emploi et exemples
PROFILS = RACINE / "profils"                        # profils d'école (.yaml, jeux de couleurs LaTeX)
STYLE = RACINE / "style"                            # style générique
LATEX = STYLE / "latex"                             # préambule et commandes LaTeX communes
STATIC = RACINE / "_static"                         # logos, icônes, captures
DONNEES = RACINE / "donnees"                        # données d'exemple suivies
DATA = RACINE / "data"                              # données personnelles, non suivies
SORTIES = RACINE / "dist"                           # sorties construites, non suivies


def _uniques(dossiers):
    vus, out = set(), []
    for d in dossiers:
        if d.is_dir() and d.resolve() not in vus:
            vus.add(d.resolve()); out.append(d)
    return out


def dossiers_profils():
    """Renvoie les dossiers où chercher les profils, dans l'ordre de priorité.

    Un dossier ``profils/`` du répertoire courant (profil local), puis ``data/profils``
    (profils privés, non publiés), puis ``profils/`` du dépôt ; seuls les dossiers existants
    sont gardés, sans doublon.
    """
    return _uniques([Path.cwd() / "profils", DATA / "profils", PROFILS])


def nom_profil(f: Path) -> str:
    """Renvoie le nom d'un profil à partir de son fichier.

    C'est le nom de son dossier (``profils/Ecole1/profil.yaml`` → ``Ecole1``),
    ou celui du fichier pour un profil isolé (``profils/Ecole1.yaml``).
    """
    return f.parent.name if f.stem.lower() == "profil" else f.stem


def fichiers_profils(dossier: Path | None = None):
    """Renvoie la liste des fichiers de profil.

    Un profil est ``<dossier>/<nom>/profil.yaml`` (un dossier par profil, avec son jeu de couleurs)
    ou ``<dossier>/<nom>.yaml`` (ancienne forme). Sans ``dossier`` : tous les dossiers de
    :func:`dossiers_profils`, dans l'ordre.
    """
    out = []
    for d in ([dossier] if dossier else dossiers_profils()):
        out += sorted(d.glob("*/profil.y*ml")) + sorted(g for g in d.glob("*.y*ml") if g.stem.lower() != "profil")
    return out


def dossiers_latex():
    """Renvoie les dossiers où chercher un fichier LaTeX nommé sans chemin valide.

    D'abord le style commun (``style/latex``), puis les dossiers des profils.
    """
    return _uniques([LATEX] + [f.parent for f in fichiers_profils()] + dossiers_profils())


def media_exoforge(dossier_fiche: Path, ident: str) -> Path:
    """Renvoie le dossier des médias d'un exercice ExoForge.

    D'abord ``data/exoforge/media/<id>`` s'il existe (privé : enregistrements de l'auteur),
    sinon ``media/<id>`` à côté de la fiche (exemples publiés, sans audio tant qu'ils ne sont pas prêts).
    """
    pres = dossier_fiche / "media" / ident
    priv = DATA / "exoforge" / "media" / ident
    return priv if priv.is_dir() else pres


def fichier_exoforge(dossier_fiche: Path, rel: str) -> Path:
    """Renvoie le chemin d'un fichier cité par une fiche (image ``media/<id>/…``).

    Le fichier est cherché d'abord sous ``data/exoforge``, sinon à côté de la fiche.
    """
    priv = DATA / "exoforge" / rel
    return priv if priv.exists() else dossier_fiche / rel
