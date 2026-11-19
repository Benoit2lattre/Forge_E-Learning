#!/usr/bin/env python3
"""ExoForge — construit un exercice interactif à partir d'une fiche YAML.

Usage :
    python build.py exercices/<fiche>.yaml [--profil Ecole1] [--cours traction:ecole1-meca] [--auteur]
    (l'extension .yaml peut être omise)

--cours : profil de l'école de l'édition (cours[:déclinaison[/édition]]), si --profil n'est pas donné.
--profil (-p) : applique la charte (couleurs, police, jeu de couleurs LaTeX) de profils/<nom>/profil.yaml
                (nom, alias ou première lettre) ; sinon le profil de la fiche, ou le profil par défaut.

--auteur (-a) : affiche les outils auteur (emplacements audio, relevé des temps d'apparition, données tirées).

La fiche décrit des étapes (info, choix, numerique), l'encadré permanent (rappel), les données
tirées et calculées, les audios ; generique.py la vérifie et la construit.

Produit dans dist/exoforge/<id>/ :

    index.html            l'exercice autonome (s'ouvre dans un navigateur)
    imsmanifest.xml       manifeste SCORM 1.2

et dist/exoforge/<id>_scorm12.zip, prêt à déposer dans Moodle (activité SCORM).
"""
import sys
from pathlib import Path

import yaml

RACINE = Path(__file__).resolve().parent
sys.path.insert(0, str(RACINE.parent / "commun"))
import chemins  # noqa: E402


def style_profil(nom) -> str:
    """Renvoie un bloc ``<style>`` qui remplace les couleurs et la police du moteur par celles du profil.

    ``nom`` : fichier du profil, ou nom / alias / première lettre (même tolérance que QuizForge).
    Les rôles de couleur de la charte deviennent des variables CSS (``principal_clair`` → ``--principal-clair``).
    """
    import generique
    f = Path(nom) if Path(str(nom)).is_file() else generique.trouver_profil(nom)
    nom = chemins.nom_profil(f)
    charte = (yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("charte", {})
    couleurs = charte.get("couleurs") or {}
    # rôle dans la charte -> variable CSS de style/web/exercice.css (principal_clair -> --principal-clair)
    ROLES = ["principal", "principal_clair", "succes", "succes_clair", "erreur", "erreur_clair", "texte",
             "texte_secondaire", "fond", "carte", "bord", "focus", "graphique", "points"]
    variables = {}
    for role, val in (charte.get("roles") or {}).items():
        if role in ROLES and val:
            variables[role.replace("_", "-")] = "#" + str(couleurs.get(val, val)).lstrip("#")
    css = ":root{" + ";".join(f"--{k}:{v}" for k, v in variables.items()) + "}"
    if charte.get("polices_url"):
        css = f'@import url("{charte["polices_url"]}");' + css
    if charte.get("police_texte"):
        css += f'body{{font-family:"{charte["police_texte"]}","Segoe UI",system-ui,sans-serif}}'
    if charte.get("police_titres"):
        css += f'header h1{{font-family:"{charte["police_titres"]}",Georgia,serif}}'
    return f"<style>/* profil {nom} */{css}</style>\n"


def construire(fiche: Path, profil: str | None = None, auteur: bool = False) -> Path:
    """Construit l'exercice décrit par la fiche YAML ``fiche`` et renvoie le chemin du paquet SCORM.

    ``profil`` : nom du profil à appliquer (sinon celui de la fiche) ; ``auteur`` : active le mode auteur.
    Quitte le programme si la fiche ne contient pas ``etapes``. Le travail est délégué à
    :func:`generique.construire_generique`.
    """
    cfg = yaml.safe_load(fiche.read_text(encoding="utf-8")) or {}
    if "etapes" not in cfg:
        sys.exit(f"{fiche.name} : la fiche doit contenir « etapes » (l'ancien format du Miner n'est plus pris en charge).")
    import generique
    return generique.construire_generique(fiche, cfg, profil, auteur, style_profil)


def ranger_version(fiche: Path, paquet: Path, profil, cours: dict):
    """Avec --cours : copie le paquet SCORM dans l'édition comme une version (``exercices/<id>/v2/<id>_v2_scorm12.zip``),
    inscrite au registre ; une construction identique (même fiche, mêmes médias, même profil) n'en crée pas."""
    import hashlib
    import shutil
    import registre
    cfg = yaml.safe_load(fiche.read_text(encoding="utf-8")) or {}
    ident = str(cfg.get("id") or fiche.stem)
    h = hashlib.md5(fiche.read_bytes())
    media = chemins.media_exoforge(fiche.parent, ident)
    for f in sorted(media.rglob("*")) if media.is_dir() else []:
        if f.is_file():
            h.update(f.relative_to(media).as_posix().encode() + f.read_bytes())
    reglages = {"profil": profil or cfg.get("profil")}
    emp = registre.empreinte(fiche, {**reglages, "contenu": h.hexdigest()})
    b = registre.base(cours)
    v = registre.preparer(b, fiche, None, emp, "exercice", ident)
    if v["identique"]:
        print(f"Identique à la version {v['identique']['id']} (même fiche, mêmes médias, même profil) : rien de rangé")
        print(f"Version : {v['identique']['dossier']}")
        return
    d = Path(v["dossier"])
    d.mkdir(parents=True, exist_ok=True)
    shutil.copy2(paquet, d / f"{ident}_{v['label']}_scorm12.zip")
    registre.enregistrer_exercice(b, v, fiche, reglages, emp, cours["cours"])
    print(f"Version {v['id']} inscrite au registre de {registre.rel(b)}")
    print(f"Version : {registre.rel(d)}")


if __name__ == "__main__":
    args = sys.argv[1:]
    if any(o in args for o in ("-h", "--help")):
        print(__doc__)
        sys.exit(0)
    profil = None
    opt = next((o for o in ("--profil", "-p", "-P") if o in args), None)
    if opt:
        i = args.index(opt)
        profil = args[i + 1] if i + 1 < len(args) else sys.exit(__doc__)
        del args[i:i + 2]
    cours = None
    if "--cours" in args:                       # profil de l'école de l'édition, si --profil n'est pas donné
        i = args.index("--cours")
        spec = args[i + 1] if i + 1 < len(args) else sys.exit(__doc__)
        del args[i:i + 2]
        try:
            sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "commun"))
            import cours_options
            cours = cours_options.resoudre(spec)
            print(f"Cours : {cours['libelle']}" + (f" (profil {cours['profil']})" if cours["profil"] else ""))
            profil = profil or cours["profil"]
        except Exception as e:
            print(f"Cours « {spec} » non appliqué : {e}")
    auteur = False
    for o in ("--auteur", "-a"):
        if o in args:
            auteur = True
            args.remove(o)
    if len(args) != 1:
        sys.exit(__doc__)
    fiche = Path(args[0])
    if not fiche.exists() and fiche.with_name(fiche.name + ".yaml").exists():     # nom donné sans extension
        fiche = fiche.with_name(fiche.name + ".yaml")
    paquet = construire(fiche, profil, auteur)
    if cours and paquet and Path(paquet).is_file():
        ranger_version(fiche, Path(paquet), profil, cours)
