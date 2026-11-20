#!/usr/bin/env python3
"""QuizForge — banques de questions Moodle à partir d'Excel ou de GIFT.

Commandes principales ::

    python quizforge.py convertir Quizz.xlsx [autres fichiers…] [--categorie MMC/TP3] [--sortie dossier]
        Excel, GIFT (.txt) ou banque (.yaml) -> GIFT par catégorie + Moodle XML + banque YAML + rapport.
    python quizforge.py importer dossier_ou_fichiers… --banque banque.yaml
        Reprend des fichiers GIFT / Excel existants dans une banque YAML unique, dédoublonnée.
    python quizforge.py modele [--sortie modele_QuizForge.xlsx]
        Crée un classeur modèle avec un onglet par type de question.
    python quizforge.py profils [Ecole1]
        Liste les profils d'établissement, ou affiche les réglages de l'un d'eux.

Autres commandes : ``valider`` (vérifier classeurs, projets du pointeur et profils), ``bilan``
(DiagForge : analyse des résultats d'un test Moodle), ``reparer``, ``fusionner`` et ``assistant``
(menu pas à pas) ; ``python quizforge.py --help`` les décrit toutes.

Option ``--profil Ecole1`` (convertir, importer) : barème, types autorisés, formats, langues et charte
lus dans ``profils/Ecole1/profil.yaml`` ; les options de la ligne de commande l'emportent.

Types gérés : vf (vrai/faux), qcm (une ou plusieurs bonnes réponses), appariement,
courte (réponse courte), numerique (avec tolérance), essai (réponse libre), et en Moodle XML
seulement schema (glisser-déposer sur image) et trous (texte à trous).
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "commun"))
import chemins  # noqa: E402
from charte import COULEUR_PRINCIPALE  # noqa: E402
from xml.sax.saxutils import escape as xml_escape

import yaml

VERSION = "0.2"

# --------------------------------------------------------------------------- profils d'établissement

TYPES = ["vf", "qcm", "appariement", "courte", "numerique", "essai", "schema", "trous"]
XML_SEUL = ("schema", "trous")      # types que le format GIFT ne sait pas décrire
NUMEROTATIONS = ["abc", "ABCD", "123", "iii", "IIII", "none"]

PROFIL_DEFAUT = {
    "nom": "",
    "categorie": "",
    "langues": {"base": "fr", "mode": "separe"},
    "formats": ["xml", "gift", "yaml"],
    "types": TYPES,
    "bareme": {
        "note": 1,
        "penalite": {"vf": 1, "defaut": 0.3333333},
        "qcm": {"melanger": True, "numerotation": "abc", "mauvaise_option": "negative"},
        "appariement": {"melanger": True},
        "numerique": {"penalite_unite": 0},
    },
    # composition des quiz de séance (plan écrit par convertir --seance n ; lu par DiagForge)
    #   partiel : k questions tirées sur N dans chaque catégorie ; commun : mêmes questions pour tous, ordre mélangé ;
    #   mixte : questions de la séance en commun, rappels des séances précédentes en tirage partiel
    "quiz": {"tirage": "partiel", "part_tiree": 0.33, "max_tire": 10, "rappel": 0.3},
    "charte": {},
    # tags ajoutés à chaque question : fixes + automatiques (type, onglet, classeur)
    "tags": {"fixes": [], "automatiques": ["type"]},
}
P = PROFIL_DEFAUT  # profil actif (remplacé par charger_profil)

# --------------------------------------------------------------------------- saisie tolérante (accessibilité)
# Les noms courts (commandes, onglets, types, modes…) sont reconnus par leur première lettre ; on ne lit au plus
# que les 3 premières lettres, sans tenir compte des accents ni des majuscules : « Schemas », « schéma », « S »
# désignent tous l'onglet Schema ; « QMC » désigne QCM. Ce qui a été compris est affiché.


def _cle(t) -> str:
    """Normalise une saisie pour la comparaison : sans accents, en minuscules, lettres et chiffres seulement."""
    t = unicodedata.normalize("NFKD", str(t)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", t)


def comprendre(saisie, choix, quoi: str, annoncer: bool = True):
    """Interprète une saisie tolérante et renvoie l'élément de ``choix`` correspondant.

    ``choix`` : liste, ou dictionnaire alias → nom. La saisie est reconnue en entier, sinon par ses 1 à 3
    premières lettres si elles ne désignent qu'un élément. Ce qui a été compris est affiché si ``annoncer``
    est vrai. Quitte le programme avec la liste des possibles si rien ne correspond.
    """
    table = dict(choix) if isinstance(choix, dict) else {c: c for c in choix}
    s = _cle(saisie)
    if not s:
        sys.exit(f"{quoi[:1].upper() + quoi[1:]} vide. Possibles : {', '.join(sorted(set(table.values())))}")
    trouve = next((v for k, v in table.items() if _cle(k) == s), None)
    if trouve is None:
        for n in (1, 2, 3):
            cands = {v for k, v in table.items() if _cle(k)[:n] == s[:n]}
            if len(cands) == 1:
                trouve = cands.pop()
                break
            if not cands:
                break
    if trouve is None:
        sys.exit(f"{quoi[:1].upper() + quoi[1:]} « {saisie} » non compris. Possibles : {', '.join(sorted(set(table.values())))}")
    if annoncer and _cle(trouve) != s:
        print(f"Compris : {quoi} « {saisie} » → {trouve}")
    return trouve


EXT_CLASSEURS = (".xlsx", ".txt", ".gift", ".yaml", ".yml")


def _ext_proche(suffixe: str, ext: str) -> bool:
    """Indique si l'extension ``suffixe`` est une faute de frappe probable de ``ext`` (« .slxs », « .xlxs », « .xslx » pour ``.xlsx``)."""
    import difflib
    a, b = _cle(suffixe), _cle(ext)
    return bool(a) and (sorted(a) == sorted(b) or difflib.SequenceMatcher(None, a, b).ratio() >= 0.6)


def trouver_fichier(nom: str, exts=EXT_CLASSEURS, quoi="fichier") -> Path:
    """Renvoie le fichier ou dossier existant désigné par ``nom``, avec tolérance : extension absente ou mal tapée, nom proche.

    Ce qui a été compris est affiché ; quitte le programme si rien ne convient (avec des suggestions).
    """
    import difflib
    f = Path(nom)
    if f.exists():
        return f
    dossier = f.parent if str(f.parent) not in ("", ".") else Path(".")
    if not dossier.exists():
        sys.exit(f"Dossier introuvable : {dossier}")
    presents = [x for x in dossier.iterdir() if x.is_file() and x.suffix.lower() in exts and not x.name.startswith("~$")]
    tige = f.stem if (f.suffix.lower() in exts or any(_ext_proche(f.suffix, e) for e in exts)) else f.name
    memes = [x for x in presents if _cle(x.stem) == _cle(tige)]
    if len(memes) > 1:          # même nom, plusieurs extensions : préférer celle qui ressemble à la saisie
        memes = [x for x in memes if _ext_proche(f.suffix, x.suffix)] or sorted(memes, key=lambda x: exts.index(x.suffix.lower()))
    if memes:
        if memes[0].name != f.name:
            print(f"Compris : {quoi} « {nom} » → {memes[0]}")
        return memes[0]
    proches = difflib.get_close_matches(_cle(tige), [_cle(x.stem) for x in presents], n=3, cutoff=0.75)
    cands = [x for x in presents if _cle(x.stem) in proches]
    if len(cands) == 1:
        print(f"Compris : {quoi} « {nom} » → {cands[0]} (nom le plus proche)")
        return cands[0]
    aide = f" Vouliez-vous dire : {', '.join(x.name for x in cands)} ?" if cands else ""
    sys.exit(f"{quoi.capitalize()} introuvable : {nom}.{aide}")


def nom_sortie(nom: str, ext: str) -> Path:
    """Renvoie le nom de fichier de sortie avec l'extension ``ext`` : ajoutée si elle manque, corrigée si elle est mal tapée (« Test » → ``Test.xlsx``)."""
    f = Path(nom)
    if f.suffix.lower() == ext:
        return f
    if f.suffix and _ext_proche(f.suffix, ext):
        g = f.with_suffix(ext)
    else:
        g = f.with_name(f.name + ext)
    print(f"Compris : fichier de sortie « {nom} » → {g}")
    return g


def _fusion(base: dict, ajout: dict) -> dict:
    """Fusionne récursivement deux dictionnaires ; les valeurs de ``ajout`` l'emportent."""
    out = dict(base)
    for k, v in (ajout or {}).items():
        out[k] = _fusion(base[k], v) if isinstance(v, dict) and isinstance(base.get(k), dict) else v
    return out


def dossiers_profils():
    """Renvoie les dossiers de profils, dans l'ordre de priorité (voir :func:`chemins.dossiers_profils`)."""
    return chemins.dossiers_profils()


def lister_profils() -> dict:
    """Renvoie ``{nom: {fichier, alias, description, defaut}}`` pour tous les profils trouvés (``profils/<nom>/profil.yaml``).

    Pour un même nom, le premier trouvé l'emporte (local, puis privé, puis dépôt) ; un profil illisible est signalé et ignoré.
    """
    out = {}
    for f in chemins.fichiers_profils():
        nom = chemins.nom_profil(f)
        if nom in out:                        # le premier trouvé l'emporte (local, puis privé, puis dépôt)
            continue
        try:
            lu = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        except yaml.YAMLError as e:
            print(f"ATTENTION : profil illisible {f} ({e})")
            continue
        out[nom] = {"fichier": str(f), "alias": [str(x) for x in lu.get("alias", [])],
                    "description": lu.get("description", ""), "defaut": bool(lu.get("defaut"))}
    return out


def chemin_profil(nom: str) -> Path:
    """Renvoie le fichier d'un profil désigné par un chemin ``.yaml``, son nom, un alias ou ses premières lettres.

    Quitte le programme si aucun profil n'est trouvé ou si le nom n'est pas compris.
    """
    f = Path(nom)
    if f.suffix in (".yaml", ".yml") and f.exists():
        return f
    profils = lister_profils()
    if not profils:
        sys.exit("Aucun profil trouvé (dossier profils/ du dépôt, data/profils ou profils/ du répertoire courant)")
    table = {n: n for n in profils}
    for n, d in profils.items():
        for a in d["alias"]:
            table.setdefault(a, n)          # alias partagé : le premier profil trouvé l'emporte
    return Path(profils[comprendre(nom, table, "profil")]["fichier"])


def profil_par_defaut() -> str | None:
    """Renvoie le nom du premier profil marqué ``defaut``, ou ``None``."""
    d = [n for n, v in lister_profils().items() if v["defaut"]]
    return d[0] if d else None


def ecrire_index_profils(force: bool = False):
    """Écrit ``index_profils.json`` dans chaque dossier de profils : profils, alias et valeurs acceptées de chaque réglage.

    L'index donne aussi la valeur par défaut de chaque réglage, les commandes et les onglets du modèle.
    Il n'est régénéré que si un profil ``.yaml`` est plus récent que lui, sauf avec ``force``.
    """
    import json
    for d in dossiers_profils():
        idx = d / "index_profils.json"
        yamls = chemins.fichiers_profils(d)
        if not yamls or (not force and idx.exists() and idx.stat().st_mtime >= max(y.stat().st_mtime for y in yamls)):
            continue
        profils = {k: v for k, v in lister_profils().items() if Path(v["fichier"]).resolve().is_relative_to(d.resolve())}
        doc = {
            "_note": "Fichier généré par quizforge.py à partir des profils de ce dossier : ne pas modifier à la main.",
            "profil_par_defaut": next((n for n, v in profils.items() if v["defaut"]), None),
            "profils": {n: {"fichier": Path(v["fichier"]).resolve().relative_to(d.resolve()).as_posix(), "alias": v["alias"], "description": v["description"]}
                        for n, v in profils.items()},
            "reglages": {
                "langues.mode": {"possibles": ["separe", "multilang"], "defaut": PROFIL_DEFAUT["langues"]["mode"]},
                "langues.base": {"possibles": list(LANGUES), "defaut": PROFIL_DEFAUT["langues"]["base"]},
                "formats": {"possibles": ["xml", "gift", "yaml"], "defaut": PROFIL_DEFAUT["formats"]},
                "types": {"possibles": TYPES, "defaut": TYPES},
                "bareme.note": {"possibles": "nombre", "defaut": PROFIL_DEFAUT["bareme"]["note"]},
                "bareme.penalite": {"possibles": "0 à 1 par type, + defaut", "defaut": PROFIL_DEFAUT["bareme"]["penalite"]},
                "bareme.qcm.melanger": {"possibles": [True, False], "defaut": True},
                "bareme.qcm.numerotation": {"possibles": NUMEROTATIONS, "defaut": "abc"},
                "bareme.qcm.mauvaise_option": {"possibles": ["negative", "equilibree", "zero"], "defaut": "negative"},
                "bareme.appariement.melanger": {"possibles": [True, False], "defaut": True},
                "bareme.numerique.penalite_unite": {"possibles": "0 à 1", "defaut": 0},
                "tags.fixes": {"possibles": "liste libre", "defaut": []},
                "tags.automatiques": {"possibles": ["type", "onglet", "classeur"], "defaut": ["type"]},
                "quiz.tirage": {"possibles": ["partiel", "commun", "mixte"], "defaut": "partiel"},
                "quiz.part_tiree": {"possibles": "0 à 1 (part des questions d'une catégorie tirée)", "defaut": 0.33},
                "quiz.max_tire": {"possibles": "entier", "defaut": 10},
                "quiz.rappel": {"possibles": "0 à 1 (part des rappels dans le quiz)", "defaut": 0.3},
            },
            "commandes": list(COMMANDES),
            "onglets_du_modele": list(MODELE),
            "noms_des_types_en_tags": NOMS_TYPES,
        }
        idx.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")


def charger_profil(nom: str | None) -> dict:
    """Charge un profil (réglages par défaut d'un établissement) dans la variable globale ``P`` et le renvoie.

    Sans ``nom`` : réglages par défaut de QuizForge. Les valeurs du profil sont fusionnées avec ``PROFIL_DEFAUT``
    et les noms courts (types, modes) sont interprétés ; les options de la ligne de commande l'emportent ensuite
    (voir :func:`appliquer_profil`). Quitte le programme si une valeur n'est pas comprise.
    """
    global P
    if not nom:
        P = PROFIL_DEFAUT
        return P
    f = chemin_profil(nom)
    lu = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
    P = _fusion(PROFIL_DEFAUT, lu)
    P["_fichier"] = str(f)
    P["types"] = [comprendre(t, TYPES, f"type du profil {chemins.nom_profil(f)}") for t in P["types"]]
    P["tags"]["automatiques"] = [comprendre(t, ["type", "onglet", "classeur"], f"tag automatique du profil {chemins.nom_profil(f)}")
                                 for t in P["tags"].get("automatiques") or []]
    P["bareme"]["qcm"]["mauvaise_option"] = comprendre(P["bareme"]["qcm"]["mauvaise_option"], ["negative", "equilibree", "zero"],
                                                       f"mauvaise_option du profil {chemins.nom_profil(f)}")
    P["langues"]["mode"] = comprendre(P["langues"]["mode"], ["separe", "multilang"], f"langues.mode du profil {chemins.nom_profil(f)}")
    P["quiz"]["tirage"] = comprendre(P["quiz"]["tirage"], ["partiel", "commun", "mixte"], f"quiz.tirage du profil {chemins.nom_profil(f)}")
    if P["bareme"]["qcm"]["numerotation"] not in NUMEROTATIONS:
        sys.exit(f"{f.name} : numerotation possible : {', '.join(NUMEROTATIONS)}")
    return P


def couleur(nom_ou_hex: str) -> str:
    """Renvoie une couleur ``#RRGGBB`` à partir d'un rôle ou d'un nom de couleur de la charte du profil, ou d'un code hexadécimal."""
    ch = P.get("charte") or {}
    nom_ou_hex = (ch.get("roles") or {}).get(nom_ou_hex, nom_ou_hex)
    c = (ch.get("couleurs") or {}).get(nom_ou_hex, nom_ou_hex)
    c = str(c).lstrip("#")
    return "#" + c


def habiller_retroaction(html: str) -> str:
    """Encadre la rétroaction générale aux couleurs du profil (Moodle XML)."""
    st = (P.get("charte") or {}).get("retroaction")
    if not html or not st:
        return html
    css = "padding:.6em .9em;"
    if st.get("cadre"):
        css += f"border-left:4px solid {couleur(st['cadre'])};"
    if st.get("fond"):
        css += f"background:{couleur(st['fond'])};"
    if st.get("arrondi"):
        css += f"border-radius:{st['arrondi']}px;"
    titre = ""
    if st.get("titre"):
        c = couleur(st.get("couleur_titre") or st.get("cadre") or "texte")
        titre = f'<p style="margin:0 0 .3em;font-weight:bold;color:{c}">{st["titre"]}</p>'
    return f'<div style="{css}">{titre}{html}</div>'


def filtrer_types(qs: list, rapport: list) -> list:
    """Renvoie les questions dont le type est autorisé par le profil ; les autres sont signalées dans ``rapport``."""
    autorises = set(P["types"])
    gardees = [q for q in qs if q["type"] in autorises]
    exclues = [q for q in qs if q["type"] not in autorises]
    for q in exclues:
        rapport.append(f"EXCLUE (type « {q['type']} » non prévu par le profil {P['nom']}) : {q['titre']} — "
                       f"{re.sub(r'<[^>]+>', '', q['question'])[:60]}")
    return gardees

# --------------------------------------------------------------------------- outils


def txt(v) -> str:
    """Convertit une valeur de cellule en texte sans espaces autour (``None`` → ``""``, ``3.0`` → ``"3"``)."""
    if v is None:
        return ""
    if isinstance(v, float) and v.is_integer():
        v = int(v)
    return str(v).strip()


def norm(s) -> str:
    """Normalise un texte pour la comparaison : sans accents, en minuscules, espaces réduits."""
    s = unicodedata.normalize("NFKD", txt(s)).encode("ascii", "ignore").decode().lower()
    return re.sub(r"\s+", " ", s).strip()


VRAI = {"t", "true", "v", "vrai", "oui", "yes", "1", "{t}", "{true}"}
FAUX = {"f", "false", "faux", "non", "no", "0", "{f}", "{false}"}


def lire_booleen(v):
    """Lit une réponse vrai/faux (T/F, V/F, Vrai/Faux, oui/non, 1/0…) ; renvoie ``True``, ``False`` ou ``None``."""
    n = norm(v).replace(" ", "")
    if n in VRAI:
        return True
    if n in FAUX:
        return False
    return None


# fractions autorisées par Moodle
FRACTIONS = [100, 90, 83.33333, 80, 75, 70, 66.66667, 60, 50, 40, 33.33333, 30, 25,
             20, 16.66667, 14.28571, 12.5, 11.11111, 10, 5, 0]


def fraction_mauvaise(nb_bons: int, n_options: int, mode: str | None = None) -> float:
    """Renvoie la fraction (en %) d'une mauvaise case cochée dans un QCM à plusieurs réponses, avant arrondi Moodle.

    Selon ``mode`` (par défaut ``bareme.qcm.mauvaise_option`` du profil) :

    - ``negative`` : -100/t (t bonnes réponses) ;
    - ``equilibree`` : -100/(n - t), cocher toutes les cases vaut alors 0
      (voir ``reference/B_conception_qcm/schmidt2021.md`` et ``schmidt2022.md``) ;
    - ``zero`` : 0 (cocher tout donne 100 %).
    """
    mode = mode or P["bareme"]["qcm"]["mauvaise_option"]
    if mode == "zero":
        return 0.0
    if mode == "equilibree" and n_options > nb_bons:
        return -100 / (n_options - nb_bons)
    return -100 / nb_bons


def fraction_moodle(x: float) -> float:
    """Arrondit une fraction (en %, signe conservé) à la valeur autorisée par Moodle la plus proche (``FRACTIONS``)."""
    s = -1 if x < 0 else 1
    return s * min(FRACTIONS, key=lambda f: abs(f - abs(x)))


def cle_question(q: dict) -> str:
    """Renvoie la clé de dédoublonnage d'une question : type + énoncé normalisé."""
    return q["type"] + "|" + re.sub(r"[^a-z0-9]", "", norm(re.sub(r"<[^>]+>", "", q["question"])))


# --------------------------------------------------------------------------- texte abîmé par un remplacement V→T / F→F

_MIN = "a-zàâçéèêëîïôûùüÿœ"
_ABIME = re.compile(rf"([{_MIN}])([TF])(?=[{_MIN}])")


def texte_abime(s: str) -> bool:
    """Indique si le texte porte la trace d'un Rechercher/Remplacer « V » → « T » sans casse ni mot entier (« plusFin », « deTon »)."""
    return isinstance(s, str) and bool(_ABIME.search(s))


def reparer_texte(s: str) -> str:
    """Répare un texte abîmé par un remplacement « V » → « T » : « plusFin » → « plus fin », « deTon » → « de von »."""
    return _ABIME.sub(lambda m: m.group(1) + " " + ("v" if m.group(2) == "T" else "f"), s)


def reparer_classeur(chemin: Path) -> tuple:
    """Écrit une copie réparée ``<classeur>_corrige.xlsx`` ; renvoie ``(chemin, liste des corrections)``.

    Le classeur d'origine n'est pas modifié.
    """
    import openpyxl
    wb = openpyxl.load_workbook(chemin)
    corrections = []
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if texte_abime(c.value):
                    nouveau = reparer_texte(c.value)
                    corrections.append(f"{ws.title}!{c.coordinate} : « {c.value.strip()[:70]} » → « {nouveau.strip()[:70]} »")
                    c.value = nouveau
    sortie = chemin.with_name(chemin.stem + "_corrige.xlsx")
    wb.save(sortie)
    return sortie, corrections


# --------------------------------------------------------------------------- lecture Excel


def _col(entetes, *noms, motif=None):
    """Renvoie l'indice de la première colonne dont l'en-tête est l'un des ``noms`` (ou correspond à ``motif``), sinon ``None``."""
    for i, h in enumerate(entetes):
        if h is None:
            continue
        if h in noms or (motif and re.fullmatch(motif, h)):
            return i
    return None


def _cols(entetes, motif):
    """Renvoie ``[(numéro, indice de colonne)]`` des colonnes numérotées qui correspondent à ``motif`` (Option 1, Option b…).

    Le groupe 1 du motif donne le numéro : chiffres, ou lettre a à j convertie en 1 à 10.
    """
    entetes = [h if h is not None else "" for h in entetes]
    return [(int(re.fullmatch(motif, h).group(1)) if re.fullmatch(motif, h).group(1).isdigit()
             else "abcdefghij".index(re.fullmatch(motif, h).group(1)) + 1, i)
            for i, h in enumerate(entetes) if re.fullmatch(motif, h)]


def detecter_type(H):
    """Reconnaît le type de question d'un onglet d'après ses en-têtes normalisés ; ``None`` si aucun type ne correspond."""
    H = [h for h in H if h is not None]
    if "projet" in H or "projet pointeur" in H:
        return "schema"
    if any(re.fullmatch(r"mot ?\d+", h) for h in H):
        return "trous"
    if any(re.fullmatch(r"choix ?\d+", h) for h in H) and any(re.fullmatch(r"rep ?\d+", h) for h in H):
        return "appariement"
    if "reponse correcte" in H or any(re.fullmatch(r"option ?(\d+|[a-j])", h) for h in H):
        return "qcm"
    if "valeur" in H:
        return "numerique"
    if "reponses acceptees" in H:
        return "courte"
    if "reponse attendue" in H or "essai" in H:
        return "essai"
    if "reponse" in H or "response" in H:
        return "vf"
    return None


NOMS_TYPES = {"vf": "VF", "qcm": "QCM", "appariement": "Appariement", "numerique": "Numerique",
              "courte": "ReponseCourte", "essai": "Essai", "schema": "Schema", "trous": "Trous"}


def decouper_tags(t: str) -> list:
    """Découpe une liste de tags séparés par ``;`` ou ``,`` (espaces retirés, éléments vides ignorés)."""
    return [x.strip() for x in re.split(r"[;,]", t or "") if x.strip()]


def ajouter_tags(qs: list, extra: list, rapport: list):
    """Complète les tags de chaque question, sur place.

    Tags = tags du profil + ``--tags`` + ligne ``$TAGS`` de l'onglet + automatiques + colonne Tags,
    sans doublon (sans tenir compte des majuscules, comme Moodle).
    """
    conf = P.get("tags") or {}
    auto = conf.get("automatiques") or []
    inconnus = [a for a in auto if a not in ("type", "onglet", "classeur")]
    if inconnus:
        rapport.append(f"Profil : tags automatiques inconnus {inconnus} (possibles : type, onglet, classeur)")
    for q in qs:
        info = q.pop("_tags_auto", {})
        tags = list(conf.get("fixes") or []) + list(extra) + list(info.get("liste", []))
        if "type" in auto:
            tags.append(NOMS_TYPES.get(q["type"], q["type"]))
        if "onglet" in auto and info.get("onglet"):
            tags.append(info["onglet"])
        if "classeur" in auto and info.get("classeur"):
            tags.append(info["classeur"])
        tags += q.get("tags", [])
        vus, propres = set(), []
        for t in tags:                      # Moodle ne distingue pas les majuscules dans les tags
            if t.lower() not in vus:
                vus.add(t.lower()); propres.append(t)
        if propres:
            q["tags"] = propres


ENTETES_FIXES = ["num", "numero", "no", "n", "titre", "title", "question", "retroaction", "feedback", "feedback general",
                 "retroaction generale", "tags", "mots cles", "reponse", "response", "reponse correcte",
                 "feedback juste", "feedback faux", "valeur", "tolerance", "unite", "reponses acceptees", "casse",
                 "reponse attendue", "essai", "projet", "projet pointeur", "mode", "seance", "session"]
ENTETES_NUMEROTES = ["option", "feedback", "choix", "rep", "mot", "leurre", "erreur", "feedback erreur", "code erreur", "indice"]
_SUFFIXE_LANGUE = re.compile(r"(.+?) \(?(en|fr|es|de|it)\)?")


def entete_connu(h: str) -> bool:
    """Indique si un en-tête normalisé est reconnu (en-tête fixe ou numéroté, avec ou sans suffixe de langue)."""
    if not h:
        return True
    m = _SUFFIXE_LANGUE.fullmatch(h)
    h = m.group(1) if m else h
    return h in ENTETES_FIXES or bool(re.fullmatch(r"(option|feedback|choix|rep|mot|leurre) ?(\d+|[a-j])", h)) \
        or bool(re.fullmatch(r"((feedback|retroaction|code) )?erreur ?\d+|code erreur ?[a-j]|indice ?\d+", h))


def corriger_entete(h: str):
    """Corrige un en-tête mal tapé proche d'un en-tête connu : renvoie ``(en-tête corrigé, True)``, sinon ``(h, False)``."""
    import difflib
    if not h or entete_connu(h):
        return h, False
    m = _SUFFIXE_LANGUE.fullmatch(h)
    base, langue = (m.group(1), " " + m.group(2)) if m else (h, "")
    num = re.search(r"(\d+)$", base)
    cands = list(ENTETES_FIXES) + ([f"{n} {num.group(1)}" for n in ENTETES_NUMEROTES] if num else [])
    proche = difflib.get_close_matches(base if not num else re.sub(r" ?(\d+)$", r" \1", base), cands, n=1, cutoff=0.8)
    return (proche[0] + langue, True) if proche else (h, False)


def lire_excel(chemin: Path, racine: str = "", rapport: list | None = None, reparer: bool = False,
               nom: str = "") -> list:
    """Lit un classeur Excel QuizForge et renvoie la liste de ses questions (dictionnaires).

    Chaque onglet est un lot de questions d'un même type, reconnu d'après ses en-têtes ; les lignes
    ``$CATEGORY``, ``$SEANCE`` et ``$TAGS`` au-dessus des en-têtes sont prises en compte, ainsi que les
    colonnes de traduction (« Question EN »…).

    - ``racine`` : début de la catégorie Moodle ; ``nom`` : nom de catégorie à la place du nom du classeur ;
    - ``reparer`` : réparer les textes abîmés (sinon ils sont seulement signalés) ;
    - ``rapport`` : reçoit les remarques de lecture.
    """
    import openpyxl

    rapport = rapport if rapport is not None else []
    wb = openpyxl.load_workbook(chemin, data_only=True)
    out = []
    for ws in wb.worksheets:
        lignes = [list(r) for r in ws.iter_rows(values_only=True)]
        categorie, ih, tags_onglet, seance_onglet = None, None, [], ""
        for i, r in enumerate(lignes[:12]):
            cellules = [txt(c) for c in r if txt(c)]
            if cellules and cellules[0].startswith("$CATEGORY"):
                categorie = "".join(cellules).split(":", 1)[1].strip()
                continue
            if cellules and norm(cellules[0]).upper().startswith("$SEANCE"):
                seance_onglet = " ".join(cellules).split(":", 1)[1].strip() if ":" in " ".join(cellules) else ""
                continue
            if cellules and cellules[0].upper().startswith("$TAGS"):
                tags_onglet = decouper_tags(" ".join(cellules).split(":", 1)[1] if ":" in " ".join(cellules) else "")
                continue
            H = [corriger_entete(norm(c))[0] for c in r]
            if "question" in H:
                ih = i
                break
        if ih is None:
            if ws.title != "Lisez-moi":           # onglet d'explications du classeur modèle
                rapport.append(f"{chemin.name} › {ws.title} : ignorée (pas d'en-tête « Question »)")
            continue
        H_brut = []
        for c in lignes[ih]:
            h, corrige = corriger_entete(norm(c))
            if corrige:
                rapport.append(f"{chemin.name} › {ws.title} : en-tête « {txt(c)} » compris comme « {h} »")
            elif h and not entete_connu(h):
                rapport.append(f"{chemin.name} › {ws.title} : colonne « {txt(c)} » non reconnue, ignorée")
            H_brut.append(h)
        H, trad = separer_langues(H_brut)
        typ = detecter_type(H)
        if typ is None:
            rapport.append(f"{chemin.name} › {ws.title} : ignorée (type de question non reconnu, en-têtes {H})")
            continue
        if not categorie:
            parties = [p for p in (racine, nom or chemin.stem, ws.title) if p]
            categorie = "$course$/top/" + "/".join(parties)
        c_titre = _col(H, "titre", "title")
        c_q = _col(H, "question")
        c_fb = _col(H, "retroaction", "feedback", "feedback general", "retroaction generale")
        c_tags = _col(H, "tags", "mots cles")
        n_ok = 0
        for k, r in enumerate(lignes[ih + 1:], start=ih + 2):
            r = list(r) + [None] * (len(H) - len(r))
            for j, v in enumerate(r):
                if texte_abime(v):
                    if reparer:
                        r[j] = reparer_texte(v)
                        rapport.append(f"{chemin.name} › {ws.title} › ligne {k} : texte réparé « {txt(r[j])[:60]} »")
                    else:
                        rapport.append(f"ATTENTION {chemin.name} › {ws.title} › ligne {k} : texte abîmé « {txt(v)[:50]} » "
                                       f"(remplacement V→T ?) — proposé : « {reparer_texte(txt(v))[:50]} »")
            question = txt(r[c_q])
            if not question and typ != "schema":
                continue
            if typ == "schema" and not txt(r[_col(H, "projet", "projet pointeur")]):
                continue
            titre = txt(r[c_titre]) if c_titre is not None else ""
            if not titre or re.fullmatch(r"[qQ]\d+", titre):
                titre = f"{ws.title}-{titre or k}"
            q = {"type": typ, "titre": titre, "question": question, "categorie": categorie,
                 "source": f"{chemin.name} › {ws.title} › ligne {k}"}
            if c_fb is not None and txt(r[c_fb]):
                q["feedback"] = txt(r[c_fb])
            if c_tags is not None and txt(r[c_tags]):
                q["tags"] = decouper_tags(txt(r[c_tags]))
            # séance où la notion est vue (colonne Séance ou ligne « $SEANCE: n » de l'onglet) -> tag S01, S02…
            c_se = _col(H, "seance", "session")
            se = (txt(r[c_se]) if c_se is not None else "") or seance_onglet
            if se:
                q["seance"] = int(float(se)) if re.fullmatch(r"\d+(\.0)?", se) else se
                q.setdefault("tags", []).append(f"S{q['seance']:02d}" if isinstance(q["seance"], int) else str(q["seance"]))
            q["_tags_auto"] = {"onglet": ws.title, "classeur": nom or chemin.stem, "liste": tags_onglet}
            q["_dossier"] = str(chemin.parent)
            erreur = _remplir(q, typ, H, r)
            q.pop("_dossier", None)
            if not erreur and typ == "trous":
                if q.pop("inutilises", None):
                    rapport.append(f"{chemin.name} › {ws.title} › ligne {k} : des colonnes Mot n'ont pas de trou "
                                   "dans le texte (elles servent de leurres)")
                groupes_trous = {m["groupe"] for m in q["mots"]}
                for l in q["leurres"]:
                    if l["groupe"] not in groupes_trous:
                        rapport.append(f"{chemin.name} › {ws.title} › ligne {k} : leurre « {l['texte']} » dans le groupe "
                                       f"{l['groupe']}, où il n'y a aucun trou : il ne sera jamais proposé")
            if erreur:
                rapport.append(f"{q['source']} : ignorée ({erreur})")
                continue
            for lang, cols in trad.items():
                r2 = list(r)
                for ib, it in cols.items():
                    r2[ib] = r[it]          # pas de repli sur la langue de base : une case vide reste vide
                if c_q not in cols or not txt(r[cols[c_q]]):
                    rapport.append(f"{q['source']} : pas de traduction {lang.upper()}")
                    continue
                q2 = {"type": typ, "question": txt(r2[c_q]), "_dossier": str(chemin.parent)}
                if c_fb is not None and txt(r2[c_fb]):
                    q2["feedback"] = txt(r2[c_fb])
                err2 = _remplir(q2, typ, H, r2)
                if err2:
                    rapport.append(f"{q['source']} : traduction {lang.upper()} ignorée ({err2})")
                    continue
                q2.pop("type"); q2.pop("_dossier", None); q2.pop("schema", None)
                for cle_ in ("reutilises", "inutilises", "mode"):
                    q2.pop(cle_, None)
                for champ in ("choix", "paires", "distracteurs", "mots", "leurres"):
                    if len(q.get(champ, [])) != len(q2.get(champ, [])):
                        rapport.append(f"ATTENTION {q['source']} : {champ} différents entre FR ({len(q.get(champ, []))}) "
                                       f"et {lang.upper()} ({len(q2.get(champ, []))})")
                q.setdefault("traductions", {})[lang] = q2
            out.append(q)
            n_ok += 1
        rapport.append(f"{chemin.name} › {ws.title} : {n_ok} question(s) de type {typ}")
    return out


LANGUES = ("en", "fr", "es", "de", "it")


def separer_langues(H):
    """Sépare les colonnes de traduction (« Question EN », « Option 1 (EN) »…).

    Renvoie ``(en-têtes de base, avec None à la place des colonnes de traduction, {langue: {col_base: col_trad}})``.
    """
    base, trad = list(H), {}
    for j, h in enumerate(H):
        m = re.fullmatch(r"(.+?) \(?(" + "|".join(LANGUES) + r")\)?", h)
        if m and m.group(1) in H:
            base[j] = None
            trad.setdefault(m.group(2), {})[H.index(m.group(1))] = j
    return base, trad


def lire_projet_pointeur(chemin: Path) -> dict:
    """Lit un projet enregistré par ``scripts/quizforge/outils/pointeur.html`` et renvoie les données utiles à l'export Moodle.

    Lève ``ValueError`` si le projet n'a pas d'image de fond ou si son type est inconnu.
    """
    import json
    d = json.loads(chemin.read_text(encoding="utf-8"))
    if not d.get("image"):
        raise ValueError("projet sans image de fond")
    if d.get("type") not in ("ddimageortext", "ddmarker"):
        raise ValueError(f"type de projet inconnu : {d.get('type')}")
    return {"moodle": d["type"], "image": {"nom": d["image"]["nom"], "url": d["image"]["url"]},
            "etiquettes": d.get("etiquettes", []), "zones": d.get("zones", []), "medias": d.get("medias") or {},
            "enonce": d.get("enonce", ""), "feedback": d.get("feedback", ""), "projet": chemin.name}


def _mot(v):
    """Lit un mot de texte à trous, « n » ou « n|2 » : renvoie ``{"texte", "groupe"}`` (groupe Moodle 1 à 8, 1 par défaut)."""
    t = txt(v)
    m = re.fullmatch(r"(.*?)\s*\|\s*([1-8])", t)
    return {"texte": m.group(1), "groupe": int(m.group(2))} if m else {"texte": t, "groupe": 1}


def _remplir_trous(q, H, r):
    """Complète une question « texte à trous » : ``[[1]]``, ``[[2]]``… dans la question, colonnes Mot n (bonnes réponses) et Leurre n.

    Renvoie un message d'erreur, ou ``None`` si la ligne est correcte.
    """
    mots = {n: _mot(r[j]) for n, j in _cols(H, r"mot ?(\d+)") if txt(r[j])}
    leurres = [_mot(r[j]) for _, j in sorted(_cols(H, r"leurre ?(\d+)")) if txt(r[j])]
    trous = [int(k) for k in re.findall(r"\[\[(\d+)\]\]", q["question"])]
    if not trous:
        return "aucun trou [[1]], [[2]]… dans la question"
    manquants = sorted({k for k in trous if k not in mots})
    if manquants:
        return "trou(s) sans mot : " + ", ".join(f"[[{k}]]" for k in manquants)
    n = max(mots)
    if sorted(mots) != list(range(1, n + 1)):
        return "les colonnes Mot doivent être numérotées sans saut (Mot 1, Mot 2…)"
    q["mots"] = [mots[k] for k in range(1, n + 1)]
    q["leurres"] = leurres
    q["reutilises"] = sorted({k for k in trous if trous.count(k) > 1})
    q["inutilises"] = [k for k in range(1, n + 1) if k not in trous]
    c = _col(H, "mode")
    mode = norm(r[c]) if c is not None else ""
    q["mode"] = "liste" if mode.startswith(("l", "m", "s", "d")) else "glisser"   # liste, menu, sélection, déroulant
    return None


def _remplir(q, typ, H, r):
    """Complète la question ``q`` avec les colonnes propres à son type (ligne ``r``, en-têtes ``H``).

    Renvoie un message d'erreur, ou ``None`` si la ligne est correcte.
    """
    # indices entre deux essais (balises <hint> du XML ; mode « interactif avec plusieurs essais » du test Moodle)
    indices = [txt(r[i]) for _, i in sorted(_cols(H, r"indice ?(\d+)")) if txt(r[i])]
    if indices:
        q["indices"] = indices
    if typ == "trous":
        return _remplir_trous(q, H, r)
    if typ == "schema":
        c = _col(H, "projet", "projet pointeur")
        f = Path(q.get("_dossier", ".")) / txt(r[c])
        if not f.exists():
            return f"projet du pointeur introuvable : {f.name}"
        try:
            sc = lire_projet_pointeur(f)
        except Exception as e:      # projet abîmé ou d'un autre format
            return f"projet du pointeur illisible ({e})"
        if not sc["zones"]:
            return f"{f.name} : aucune zone placée"
        q["schema"] = sc
        if q.get("question"):
            # l'énoncé d'Excel remplace celui du projet, mais les images insérées dans le pointeur (le signal…) restent
            for img in re.findall(r'<p>\s*<img[^>]*@@PLUGINFILE@@/[^>]*>\s*</p>|<img[^>]*@@PLUGINFILE@@/[^>]*>', sc["enonce"]):
                nom_img = re.search(r"@@PLUGINFILE@@/([^\"' ]+)", img).group(1)
                if f"@@PLUGINFILE@@/{nom_img}" not in q["question"]:
                    q["question"] += "\n" + img
        else:
            q["question"] = sc["enonce"]
        if not q["question"]:
            return "pas d'énoncé (ni dans Excel ni dans le projet)"
        if not q.get("feedback") and sc["feedback"]:
            q["feedback"] = sc["feedback"]
        return None
    if typ == "vf":
        c = _col(H, "reponse", "response")
        b = lire_booleen(r[c])
        if b is None:
            return f"réponse vrai/faux illisible : « {txt(r[c])} »"
        q["reponse"] = b
        for nom, champ in (("feedback juste", "feedback_juste"), ("feedback faux", "feedback_faux")):
            ci = _col(H, nom)
            if ci is not None and txt(r[ci]):
                q[champ] = txt(r[ci])
    elif typ == "qcm":
        options = sorted(_cols(H, r"option ?(\d+|[a-j])"))
        fbs = dict(_cols(H, r"(?:feedback|retroaction) ?(?:option )?(\d+|[a-j])"))
        # Code erreur n : erreur type que vise le leurre n (rapport inversé, force interne dans le DCL…) ;
        # gardé dans la banque YAML, lu par DiagForge pour compter les erreurs (axes B et H : steif2006, gierl2017)
        codes = dict(_cols(H, r"code erreur ?(\d+|[a-j])"))
        choix = [{"texte": txt(r[i]), "feedback": txt(r[fbs[n]]) if n in fbs else "",
                  **({"erreur": txt(r[codes[n]])} if n in codes and txt(r[codes[n]]) else {})}
                 for n, i in options if txt(r[i])]
        if len(choix) < 2:
            return "moins de 2 options"
        brut = txt(r[_col(H, "reponse correcte", "reponses correctes")])
        bons = set()
        for part in re.split(r"[;,+ ]+", brut):
            if not part:
                continue
            if part.isdigit() and 1 <= int(part) <= len(choix):
                bons.add(int(part) - 1)
            elif len(part) == 1 and part.upper() in "ABCDEFGHIJ" and "ABCDEFGHIJ".index(part.upper()) < len(choix):
                bons.add("ABCDEFGHIJ".index(part.upper()))
        if not bons:  # réponse donnée en texte
            bons = {i for i, c in enumerate(choix) if norm(c["texte"]) == norm(brut)}
        if not bons:
            return f"bonne réponse introuvable : « {brut} »"
        for i, c in enumerate(choix):
            c["correct"] = i in bons
            if not c["feedback"]:
                del c["feedback"]
        q["choix"] = choix
        q["plusieurs"] = len(bons) > 1
    elif typ == "appariement":
        cs, rs = dict(_cols(H, r"choix ?(\d+)")), dict(_cols(H, r"rep ?(\d+)"))
        paires, distracteurs = [], []
        for n in sorted(set(cs) | set(rs)):
            g = txt(r[cs[n]]) if n in cs else ""
            d = txt(r[rs[n]]) if n in rs else ""
            if g and d:
                paires.append([g, d])
            elif d:
                distracteurs.append(d)
        if len(paires) < 2:
            return "moins de 2 paires"
        q["paires"] = paires
        if distracteurs:
            q["distracteurs"] = distracteurs
    elif typ == "numerique":
        v = txt(r[_col(H, "valeur")]).replace(",", ".")
        try:
            q["valeur"] = float(v)
        except ValueError:
            return f"valeur non numérique : « {v} »"
        ct = _col(H, "tolerance")
        t = txt(r[ct]).replace(",", ".") if ct is not None else ""
        if t.endswith("%"):
            q["tolerance"] = abs(q["valeur"]) * float(t[:-1]) / 100
        else:
            q["tolerance"] = float(t) if t else 0.0
        # erreurs types : valeur obtenue avec l'erreur, même tolérance (relative ou absolue) que la bonne réponse,
        # et sa rétroaction (axe H : gill2008, sikurajapathi2020)
        fbe = dict(_cols(H, r"(?:feedback|retroaction) erreur ?(\d+)"))
        codes = dict(_cols(H, r"code erreur ?(\d+)"))
        erreurs = []
        for n, i in sorted(_cols(H, r"erreur ?(\d+)")):
            ve = txt(r[i]).replace(",", ".")
            if not ve:
                continue
            try:
                ve = float(ve)
            except ValueError:
                return f"erreur {n} non numérique : « {ve} »"
            te = abs(ve) * float(t[:-1]) / 100 if t.endswith("%") else q["tolerance"]
            erreurs.append({"valeur": ve, "tolerance": te, "feedback": txt(r[fbe[n]]) if n in fbe else "",
                            **({"code": txt(r[codes[n]])} if n in codes and txt(r[codes[n]]) else {})})
        if erreurs:
            q["erreurs"] = erreurs
        for nom, champ in (("feedback juste", "feedback_juste"), ("feedback faux", "feedback_faux")):
            ci = _col(H, nom)
            if ci is not None and txt(r[ci]):
                q[champ] = txt(r[ci])
        cu = _col(H, "unite")
        if cu is not None and txt(r[cu]):
            q["unite"] = txt(r[cu])
    elif typ == "courte":
        q["reponses"] = [a.strip() for a in txt(r[_col(H, "reponses acceptees")]).split(";") if a.strip()]
        if not q["reponses"]:
            return "aucune réponse acceptée"
        cc = _col(H, "casse", "sensible a la casse")
        q["casse"] = bool(cc is not None and lire_booleen(r[cc]))
    elif typ == "essai":
        ca = _col(H, "reponse attendue", "essai")
        if ca is not None and txt(r[ca]):
            q["reponse_attendue"] = txt(r[ca])
    return None


# --------------------------------------------------------------------------- lecture GIFT

SPECIAUX = "~=#{}:"


def _desechapper(s: str) -> str:
    """Retire les échappements GIFT (``\\~``, ``\\=``, ``\\#``…) ; ``\\n`` devient un saut de ligne."""
    return re.sub(r"\\([~=#{}:\\n])", lambda m: "\n" if m.group(1) == "n" else m.group(1), s).strip()


def _decouper(bloc: str, seps="~="):
    """Découpe le contenu d'accolades GIFT en ``(marqueur, texte)`` au niveau des ``~`` et ``=`` non échappés."""
    items, cour, marque, i = [], "", None, 0
    while i < len(bloc):
        ch = bloc[i]
        if ch == "\\" and i + 1 < len(bloc):
            cour += bloc[i:i + 2]
            i += 2
            continue
        if ch in seps:
            if marque is not None or cour.strip():
                items.append((marque, cour))
            marque, cour = ch, ""
        else:
            cour += ch
        i += 1
    if marque is not None or cour.strip():
        items.append((marque, cour))
    return items


def _fb(s: str):
    """Sépare ``texte#feedback`` au premier dièse non échappé ; renvoie ``(texte, feedback)``."""
    m = re.search(r"(?<!\\)#", s)
    return (s[:m.start()], s[m.end():]) if m else (s, "")


def lire_gift(chemin: Path, racine: str = "", rapport: list | None = None) -> list:
    """Lit un fichier GIFT et renvoie la liste de ses questions (dictionnaires).

    Les blocs sont séparés par une ligne vide ; ``$CATEGORY:`` change la catégorie, sinon elle est
    construite à partir de ``racine`` et du nom du fichier. Un bloc illisible est signalé dans ``rapport``.
    """
    rapport = rapport if rapport is not None else []
    brut = chemin.read_text(encoding="utf-8-sig", errors="replace")
    categorie = None
    out = []
    blocs = re.split(r"\n\s*\n", brut.replace("\r\n", "\n"))
    for n, bloc in enumerate(blocs, 1):
        lignes = [l for l in bloc.split("\n") if not l.strip().startswith("//")]
        b = "\n".join(lignes).strip()
        if not b:
            continue
        if b.startswith("$CATEGORY:"):
            categorie = b.split(":", 1)[1].strip()
            continue
        titre = ""
        m = re.match(r"::(.*?)(?<!\\)::", b, re.S)
        if m:
            titre, b = _desechapper(m.group(1)), b[m.end():]
        fmt = re.match(r"\s*\[(html|moodle|markdown|plain)\]", b)
        if fmt:
            b = b[fmt.end():]
        m1 = re.search(r"(?<!\\)\{", b)
        m2 = re.search(r"(?<!\\)\}", b[m1.end():]) if m1 else None
        if not m1 or not m2:
            rapport.append(f"{chemin.name} bloc {n} : ignoré (pas d'accolades) « {b[:50]} »")
            continue
        avant, dedans, apres = b[:m1.start()], b[m1.end():m1.end() + m2.start()], b[m1.end() + m2.end():]
        fb_general = ""
        g = re.search(r"(?<!\\)####", dedans)
        if g:
            dedans, fb_general = dedans[:g.start()], _desechapper(dedans[g.end():])
        question = _desechapper(avant) + (" _____ " + _desechapper(apres) if apres.strip() else "")
        q = {"titre": titre or f"{chemin.stem}-{len(out)+1}", "question": question.strip(),
             "categorie": categorie or "$course$/top/" + "/".join(p for p in (racine, chemin.stem) if p),
             "source": f"{chemin.name} › bloc {n}"}
        if fb_general:
            q["feedback"] = fb_general
        d = dedans.strip()
        try:
            _gift_reponses(q, d, rapport)
        except ValueError as e:
            rapport.append(f"{q['source']} : ignorée ({e})")
            continue
        out.append(q)
    rapport.append(f"{chemin.name} : {len(out)} question(s)")
    return out


def _gift_reponses(q, d, rapport=None):
    """Complète la question ``q`` d'après le contenu ``d`` des accolades GIFT (type, réponses, rétroactions).

    Lève ``ValueError`` pour un appariement de moins de 2 paires ou un QCM sans bonne réponse.
    """
    tf = re.fullmatch(r"(T|F|TRUE|FALSE|V|VRAI|FAUX)((?:#[^#]*)?)((?:#[^#]*)?)", d.replace("\n", " ").strip(), re.I)
    if tf:
        mot = tf.group(1).upper()
        q["type"], q["reponse"] = "vf", mot in ("T", "TRUE", "V", "VRAI")
        if mot in ("V", "VRAI", "FAUX") and rapport is not None:
            rapport.append(f"{q['source']} : « {tf.group(1)} » n'est pas reconnu par Moodle, corrigé en {'TRUE' if q['reponse'] else 'FALSE'}")
        if tf.group(2):
            q["feedback_faux"] = _desechapper(tf.group(2)[1:])
        if tf.group(3):
            q["feedback_juste"] = _desechapper(tf.group(3)[1:])
        return
    if d == "":
        q["type"] = "essai"
        if rapport is not None:
            rapport.append(f"{q['source']} : accolades vides {{}} = question ouverte (essai). "
                           "À vérifier : réponse oubliée lors d'un export ?")
        return
    if d.startswith("#") and re.match(r"#\s*=", d):
        # numérique à plusieurs réponses : =%100%valeur:tol#retour  =%0%erreur:tol#retour
        def _val(s):
            if ".." in s:
                a_, b_ = (float(x) for x in s.split(".."))
                return (a_ + b_) / 2, abs(b_ - a_) / 2
            v_, _, t_ = s.partition(":")
            return float(v_), float(t_ or 0)
        q["type"], erreurs = "numerique", []
        for _, item in _decouper(d[1:], "="):
            corps, fb = _fb(item.strip())
            m = re.match(r"%(-?[\d.]+)%(.*)", corps.strip())
            frac, val = (float(m.group(1)), m.group(2)) if m else (100.0, corps.strip())
            v, tol = _val(val)
            if frac >= 100 and "valeur" not in q:
                q.update(valeur=v, tolerance=tol)
                if fb:
                    q["feedback_juste"] = _desechapper(fb)
            elif frac == 0:
                erreurs.append({"valeur": v, "tolerance": tol, "feedback": _desechapper(fb)})
            elif rapport is not None:
                rapport.append(f"{q['source']} : réponse numérique à {frac:g} % de la note ignorée")
        if erreurs:
            q["erreurs"] = erreurs
        return
    if d.startswith("#"):
        corps = _fb(d[1:])[0].strip()
        if ".." in corps:
            a, b = (float(x) for x in corps.split(".."))
            q.update(type="numerique", valeur=(a + b) / 2, tolerance=abs(b - a) / 2)
        else:
            v, _, t = corps.partition(":")
            q.update(type="numerique", valeur=float(v), tolerance=float(t or 0))
        return
    items = _decouper(d)
    if any(re.search(r"(?<!\\)->", t) for _, t in items):
        q["type"], q["paires"], dis = "appariement", [], []
        for _, t in items:
            g, _, r = re.split(r"(?<!\\)(->)", t, maxsplit=1) if "->" in t else (t, "", "")
            g, r = _desechapper(g), _desechapper(r)
            if g and r:
                q["paires"].append([g, r])
            elif r:
                dis.append(r)
        if dis:
            q["distracteurs"] = dis
        if len(q["paires"]) < 2:
            raise ValueError("appariement avec moins de 2 paires")
        return
    if all(m == "=" for m, _ in items):
        q["type"] = "courte"
        q["reponses"] = [_desechapper(_fb(t)[0]) for _, t in items]
        q["casse"] = False
        return
    choix = []
    for m, t in items:
        pct = re.match(r"\s*%(-?[\d.]+)%", t)
        texte, fb = _fb(t[pct.end():] if pct else t)
        c = {"texte": _desechapper(texte), "correct": (m == "=") or bool(pct and float(pct.group(1)) > 0)}
        if fb.strip():
            c["feedback"] = _desechapper(fb)
        choix.append(c)
    if not any(c["correct"] for c in choix):
        raise ValueError("QCM sans bonne réponse")
    q.update(type="qcm", choix=choix, plusieurs=sum(c["correct"] for c in choix) > 1)


# --------------------------------------------------------------------------- versions linguistiques

CHAMPS_TEXTE = ("question", "feedback", "feedback_juste", "feedback_faux", "reponse_attendue")


def _localiser(q: dict, lang: str, base: str) -> dict:
    """Renvoie la version de la question dans la langue ``lang`` (catégorie préfixée par la langue), ou ``None`` sans traduction."""
    v = {k: val for k, val in q.items() if k != "traductions"}
    if lang != base:
        t = q.get("traductions", {}).get(lang)
        if not t:
            return None
        for k in CHAMPS_TEXTE + ("choix", "paires", "distracteurs", "reponses", "mots", "leurres"):
            if k not in t:
                v.pop(k, None)      # rien de la langue de base ne doit fuiter dans la traduction
        v.update(t)
        v["titre"] = f"{q['titre']}-{lang.upper()}"
    parts = v["categorie"].split("/")
    i = 2 if parts[:2] == ["$course$", "top"] else 0
    v["categorie"] = "/".join(parts[:i] + [lang.upper()] + parts[i:])
    return v


def _ml(textes: dict) -> str:
    """Écrit des textes ``{langue: texte}`` dans la syntaxe du filtre Moodle « Contenu multilingue » (filter_multilang)."""
    return "".join(f'<span lang="{l}" class="multilang">{t}</span>' for l, t in textes.items() if t)


def _fusion_multilang(q: dict, base: str) -> dict:
    """Renvoie une version bilingue de la question : chaque texte réunit ses langues (filtre « Contenu multilingue »)."""
    tr = q.get("traductions") or {}
    if not tr:
        return {k: v for k, v in q.items() if k != "traductions"}
    v = {k: val for k, val in q.items() if k != "traductions"}
    langs = {base: q, **tr}
    for c in CHAMPS_TEXTE:
        if c in q:
            v[c] = _ml({l: d.get(c, "") for l, d in langs.items()})
    if "choix" in q:
        v["choix"] = [dict(ch, texte=_ml({l: d["choix"][i]["texte"] for l, d in langs.items() if i < len(d.get("choix", []))}),
                           **({"feedback": _ml({l: d["choix"][i].get("feedback", "") for l, d in langs.items()
                                                if i < len(d.get("choix", []))})} if ch.get("feedback") else {}))
                      for i, ch in enumerate(q["choix"])]
    if "paires" in q:
        v["paires"] = [[_ml({l: d["paires"][i][0] for l, d in langs.items() if i < len(d.get("paires", []))}),
                        _ml({l: d["paires"][i][1] for l, d in langs.items() if i < len(d.get("paires", []))})]
                       for i in range(len(q["paires"]))]
    if "distracteurs" in q:
        v["distracteurs"] = [_ml({l: d["distracteurs"][i] for l, d in langs.items() if i < len(d.get("distracteurs", []))})
                             for i in range(len(q["distracteurs"]))]
    if "reponses" in q:  # réponse courte : on accepte les réponses des deux langues
        v["reponses"] = list(dict.fromkeys(a for d in langs.values() for a in d.get("reponses", [])))
    return v


def versions(qs: list, mode: str = "separe", base: str = "fr") -> list:
    """Renvoie les versions linguistiques à écrire, ``[(suffixe, questions)]``.

    Une version par langue (``separe``) ou une version bilingue (``multilang``) ; une seule version, de suffixe vide,
    si aucune question n'a de traduction.
    """
    langs = sorted({l for q in qs for l in q.get("traductions", {})})
    if not langs:
        return [("", [{k: v for k, v in q.items() if k != "traductions"} for q in qs])]
    if mode == "multilang":
        return [("_multilang", [_fusion_multilang(q, base) for q in qs])]
    out = []
    for l in [base] + [x for x in langs if x != base]:
        lot = [v for v in (_localiser(q, l, base) for q in qs) if v]
        out.append((f"_{l.upper()}", lot))
    return out


# --------------------------------------------------------------------------- écriture GIFT


def g_esc(s: str) -> str:
    """Échappe un texte pour GIFT (caractères spéciaux ``~=#{}:``, barre oblique inverse, sauts de ligne)."""
    s = txt(s).replace("\\", "\\\\")
    for c in SPECIAUX:
        s = s.replace(c, "\\" + c)
    return s.replace("\n", "\\n")


def gift_question(q: dict) -> str:
    """Renvoie le texte GIFT d'une question (un commentaire pour les types décrits seulement en Moodle XML)."""
    if q["type"] in XML_SEUL:
        return f"// {q['titre']} : question {'glisser-déposer sur image' if q['type'] == 'schema' else 'texte à trous'}, disponible seulement en Moodle XML"
    fmt = "[html]" if "<" in q["question"] else ""
    tete = f"::{g_esc(q['titre'])}::{fmt}{g_esc(q['question'])}"
    t = q["type"]
    if t == "vf":
        rep = "TRUE" if q["reponse"] else "FALSE"
        if q.get("feedback_faux") or q.get("feedback_juste"):
            rep += f"#{g_esc(q.get('feedback_faux', ''))}#{g_esc(q.get('feedback_juste', ''))}"
        corps = rep
    elif t == "qcm":
        parts = []
        nb = sum(c["correct"] for c in q["choix"])
        for c in q["choix"]:
            if q.get("plusieurs"):
                f = fraction_moodle(100 / nb if c["correct"] else fraction_mauvaise(nb, len(q["choix"])))
                m = f"~%{f:g}%"
            else:
                m = "=" if c["correct"] else "~"
            fb = f"#{g_esc(c['feedback'])}" if c.get("feedback") else ""
            parts.append(f"\t{m}{g_esc(c['texte'])}{fb}")
        corps = "\n" + "\n".join(parts) + "\n"
    elif t == "appariement":
        parts = [f"\t={g_esc(g)} -> {g_esc(d)}" for g, d in q["paires"]]
        parts += [f"\t= -> {g_esc(d)}" for d in q.get("distracteurs", [])]
        corps = "\n" + "\n".join(parts) + "\n"
    elif t == "courte":
        corps = " ".join("=" + g_esc(a) for a in q["reponses"])
    elif t == "numerique":
        if q.get("erreurs") or q.get("feedback_juste"):
            parts = [f"\t=%100%{q['valeur']:g}:{q.get('tolerance', 0):g}"
                     + (f"#{g_esc(q['feedback_juste'])}" if q.get("feedback_juste") else "")]
            parts += [f"\t=%0%{e['valeur']:g}:{e['tolerance']:g}" + (f"#{g_esc(e['feedback'])}" if e.get("feedback") else "")
                      for e in q.get("erreurs", [])]
            corps = "#\n" + "\n".join(parts) + "\n"
        else:
            corps = f"#{q['valeur']:g}:{q.get('tolerance', 0):g}"
    elif t == "essai":
        corps = ""
    else:
        raise ValueError(t)
    if q.get("feedback"):
        corps += f"####{g_esc(q['feedback'])}"
    return f"{tete}{{{corps}}}"


def ecrire_gift(questions: list, chemin: Path):
    """Écrit les questions au format GIFT dans ``chemin``, avec une ligne ``$CATEGORY`` à chaque changement de catégorie."""
    out, cat = [f"// Généré par QuizForge {VERSION}"], None
    for q in questions:
        if q.get("categorie") != cat:
            cat = q.get("categorie")
            out.append(f"\n$CATEGORY: {cat}")
        out.append("\n" + gift_question(q))
    chemin.write_text("\n".join(out) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- écriture Moodle XML


def _x(s: str) -> str:
    """Prépare un texte pour le XML : section CDATA s'il contient ``<``, ``>`` ou ``&``, sinon échappement simple."""
    s = txt(s)
    return f"<![CDATA[{s}]]>" if any(c in s for c in "<>&") else xml_escape(s)


def _texte(balise: str, s: str, fmt="html", indent="    ") -> str:
    """Renvoie un élément XML Moodle ``<balise format="…"><text>…</text></balise>``."""
    return f'{indent}<{balise} format="{fmt}"><text>{_x(s)}</text></{balise}>'


def _b64(url: str) -> str:
    """Renvoie la partie base64 d'une URL ``data:``."""
    return url.split(",", 1)[1]


def xml_schema(q: dict) -> str:
    """Renvoie le XML Moodle d'une question glisser-déposer sur image (``ddimageortext``) ou à marqueurs (``ddmarker``), depuis un projet du pointeur."""
    B, sc = P["bareme"], q["schema"]
    t = sc["moodle"]
    medias = "".join(f'\n      <file name="{n}" path="/" encoding="base64">{_b64(u)}</file>'
                     for n, u in sc["medias"].items() if f"@@PLUGINFILE@@/{n}" in q["question"])
    nom_img = re.sub(r"[^\w.-]+", "_", sc["image"]["nom"])
    L = [f'  <question type="{t}">',
         f"    <name><text>{_x(q['titre'])}</text></name>",
         f'    <questiontext format="html"><text>{_x(q["question"])}</text>{medias}</questiontext>',
         _texte("generalfeedback", habiller_retroaction(q.get("feedback", ""))),
         f"    <defaultgrade>{B['note']:g}</defaultgrade>",
         f"    <penalty>{B['penalite'].get('schema', B['penalite']['defaut']):.7g}</penalty>",
         "    <hidden>0</hidden>", "    <shuffleanswers/>",
         '    <correctfeedback format="html"><text>Votre réponse est correcte.</text></correctfeedback>',
         '    <partiallycorrectfeedback format="html"><text>Votre réponse est partiellement correcte.</text></partiallycorrectfeedback>',
         '    <incorrectfeedback format="html"><text>Votre réponse est incorrecte.</text></incorrectfeedback>',
         "    <shownumcorrect/>"]
    if q.get("tags"):
        L.append("    <tags>" + "".join(f"<tag><text>{_x(x)}</text></tag>" for x in q["tags"]) + "</tags>")
    if t == "ddmarker":
        L.append("    <showmisplaced/>")
    L.append(f'    <file name="{nom_img}" path="/" encoding="base64">{_b64(sc["image"]["url"])}</file>')
    ids = [e["id"] for e in sc["etiquettes"]]
    brut = lambda h: re.sub(r"<[^>]+>", "", re.sub(r"<br\s*/?>", " ", h))
    for i, e in enumerate(sc["etiquettes"], 1):
        if t == "ddimageortext":
            if e.get("image"):
                alt = e["texte"].strip() if e.get("formule") else brut(e["texte"]) or f"étiquette {i}"
                L.append(f"    <drag><no>{i}</no><text>{xml_escape(alt)}</text><draggroup>1</draggroup>"
                         f'<file name="etiquette_{i}.png" path="/" encoding="base64">{_b64(e["image"]["url"])}</file></drag>')
            else:
                L.append(f"    <drag><no>{i}</no><text>{_x(e['texte'])}</text><draggroup>1</draggroup></drag>")
        else:
            n = e.get("nombre", "auto")
            if n in (None, "auto"):
                n = max(1, sum(z["etiq"] == e["id"] for z in sc["zones"]))
            L.append(f"    <drag><no>{i}</no><text>{xml_escape(brut(e['texte']))}</text><noofdrags>{n}</noofdrags></drag>")
    for i, z in enumerate(sc["zones"], 1):
        choix = ids.index(z["etiq"]) + 1
        if t == "ddimageortext":
            L.append(f"    <drop><text></text><no>{i}</no><choice>{choix}</choice>"
                     f"<xleft>{z['x']}</xleft><ytop>{z['y']}</ytop></drop>")
        else:
            forme = {"rect": "rectangle", "cercle": "circle", "poly": "polygon"}[z["forme"]]
            co = (f"{z['x']},{z['y']};{z['w']},{z['h']}" if z["forme"] == "rect" else
                  f"{z['x']},{z['y']};{z['r']}" if z["forme"] == "cercle" else
                  ";".join(f"{x},{y}" for x, y in z["pts"]))
            L.append(f"    <drop><no>{i}</no><shape>{forme}</shape><coords>{co}</coords><choice>{choix}</choice></drop>")
    L.append("  </question>")
    return "\n".join(L)


def xml_trous(q: dict) -> str:
    """Renvoie le XML Moodle d'un texte à trous : glisser-déposer dans le texte (``ddwtos``) ou listes déroulantes (``gapselect``)."""
    B = P["bareme"]
    t = "gapselect" if q.get("mode") == "liste" else "ddwtos"
    L = [f'  <question type="{t}">',
         f"    <name><text>{_x(q['titre'])}</text></name>",
         _texte("questiontext", q["question"]),
         _texte("generalfeedback", habiller_retroaction(q.get("feedback", ""))),
         f"    <defaultgrade>{B['note']:g}</defaultgrade>",
         f"    <penalty>{B['penalite'].get('trous', B['penalite']['defaut']):.7g}</penalty>",
         "    <hidden>0</hidden>",
         f"    <shuffleanswers>{1 if B['qcm']['melanger'] else 0}</shuffleanswers>",
         '    <correctfeedback format="html"><text>Votre réponse est correcte.</text></correctfeedback>',
         '    <partiallycorrectfeedback format="html"><text>Votre réponse est partiellement correcte.</text></partiallycorrectfeedback>',
         '    <incorrectfeedback format="html"><text>Votre réponse est incorrecte.</text></incorrectfeedback>',
         "    <shownumcorrect/>"]
    if q.get("tags"):
        L.append("    <tags>" + "".join(f"<tag><text>{_x(x)}</text></tag>" for x in q["tags"]) + "</tags>")
    balise = "selectoption" if t == "gapselect" else "dragbox"
    for k, m in enumerate(q["mots"] + q["leurres"], 1):
        infini = "<infinite/>" if t == "ddwtos" and k in q.get("reutilises", []) else ""
        L.append(f"    <{balise}><text>{_x(m['texte'])}</text><group>{m['groupe']}</group>{infini}</{balise}>")
    L.append("  </question>")
    return "\n".join(L)


def xml_question(q: dict) -> str:
    """Renvoie le XML Moodle d'une question, avec le barème du profil actif."""
    if q["type"] == "trous":
        return xml_trous(q)
    if q["type"] == "schema":
        return xml_schema(q)
    t, B = q["type"], P["bareme"]
    mtype = {"vf": "truefalse", "qcm": "multichoice", "appariement": "matching",
             "courte": "shortanswer", "numerique": "numerical", "essai": "essay"}[t]
    L = [f'  <question type="{mtype}">',
         f"    <name><text>{_x(q['titre'])}</text></name>",
         _texte("questiontext", q["question"]),
         _texte("generalfeedback", habiller_retroaction(q.get("feedback", ""))),
         f"    <defaultgrade>{B['note']:g}</defaultgrade>",
         f"    <penalty>{B['penalite'].get(t, B['penalite']['defaut']):.7g}</penalty>",
         "    <hidden>0</hidden>"]
    if q.get("tags"):
        L.append("    <tags>" + "".join(f"<tag><text>{_x(x)}</text></tag>" for x in q["tags"]) + "</tags>")

    def rep(texte, fraction, fb="", fmt="html", extra=""):
        return (f'    <answer fraction="{fraction:g}" format="{fmt}"><text>{_x(texte)}</text>'
                f'<feedback format="html"><text>{_x(fb)}</text></feedback>{extra}</answer>')

    if t == "vf":
        L.append(rep("true", 100 if q["reponse"] else 0,
                     q.get("feedback_juste" if q["reponse"] else "feedback_faux", ""), "moodle_auto_format"))
        L.append(rep("false", 0 if q["reponse"] else 100,
                     q.get("feedback_faux" if q["reponse"] else "feedback_juste", ""), "moodle_auto_format"))
    elif t == "qcm":
        nb = sum(c["correct"] for c in q["choix"])
        Q = B["qcm"]
        L += [f"    <single>{'false' if q.get('plusieurs') else 'true'}</single>",
              f"    <shuffleanswers>{str(bool(Q['melanger'])).lower()}</shuffleanswers>",
              f"    <answernumbering>{Q['numerotation']}</answernumbering>"]
        for c in q["choix"]:
            if q.get("plusieurs"):
                f = fraction_moodle(100 / nb if c["correct"] else fraction_mauvaise(nb, len(q["choix"])))
            else:
                f = 100 if c["correct"] else 0
            L.append(rep(c["texte"], f, c.get("feedback", "")))
    elif t == "appariement":
        L.append(f"    <shuffleanswers>{str(bool(B['appariement']['melanger'])).lower()}</shuffleanswers>")
        for g, d in q["paires"]:
            L.append(f'    <subquestion format="html"><text>{_x(g)}</text><answer><text>{_x(d)}</text></answer></subquestion>')
        for d in q.get("distracteurs", []):
            L.append(f'    <subquestion format="html"><text></text><answer><text>{_x(d)}</text></answer></subquestion>')
    elif t == "courte":
        L.append(f"    <usecase>{1 if q.get('casse') else 0}</usecase>")
        L += [rep(a, 100, fmt="moodle_auto_format") for a in q["reponses"]]
    elif t == "numerique":
        # Moodle retient la première réponse dont l'intervalle contient la saisie : bonne réponse d'abord,
        # puis les erreurs types, puis « * » (toute autre valeur) si une rétroaction « Feedback faux » est donnée
        L.append(rep(f"{q['valeur']:g}", 100, q.get("feedback_juste", ""), fmt="moodle_auto_format",
                     extra=f"<tolerance>{q.get('tolerance', 0):g}</tolerance>"))
        for e in q.get("erreurs", []):
            L.append(rep(f"{e['valeur']:g}", 0, e.get("feedback", ""), fmt="moodle_auto_format",
                         extra=f"<tolerance>{e['tolerance']:g}</tolerance>"))
        if q.get("feedback_faux"):
            L.append(rep("*", 0, q["feedback_faux"], fmt="moodle_auto_format", extra="<tolerance>0</tolerance>"))
        if q.get("unite"):
            L += ["    <units><unit><multiplier>1</multiplier>"
                  f"<unit_name>{_x(q['unite'])}</unit_name></unit></units>",
                  f"    <unitgradingtype>0</unitgradingtype><unitpenalty>{B['numerique']['penalite_unite']:g}</unitpenalty>",
                  "    <showunits>3</showunits><unitsleft>0</unitsleft>"]
    elif t == "essai":
        L += ["    <responseformat>editor</responseformat>", "    <responserequired>1</responserequired>",
              "    <responsefieldlines>10</responsefieldlines>", "    <attachments>0</attachments>",
              _texte("graderinfo", q.get("reponse_attendue", "")),
              _texte("responsetemplate", "")]
    L += [f'    <hint format="html"><text>{_x(h)}</text></hint>' for h in q.get("indices", [])]
    L.append("  </question>")
    return "\n".join(L)


def ecrire_xml(questions: list, chemin: Path):
    """Écrit les questions au format Moodle XML dans ``chemin``, avec une question « category » à chaque changement de catégorie."""
    out, cat = ['<?xml version="1.0" encoding="UTF-8"?>', f"<!-- Généré par QuizForge {VERSION} -->", "<quiz>"], None
    for q in questions:
        if q.get("categorie") != cat:
            cat = q.get("categorie")
            out.append(f'  <question type="category"><category><text>{_x(cat)}</text></category></question>')
        out.append(xml_question(q))
    out.append("</quiz>")
    chemin.write_text("\n".join(out) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------- banque YAML


def ecrire_banque(questions: list, chemin: Path):
    """Écrit la banque YAML de QuizForge (version et liste des questions) dans ``chemin``."""
    doc = {"quizforge": VERSION, "questions": questions}
    chemin.write_text(yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=110), encoding="utf-8")


def lire_banque_yaml(chemin: Path, rapport: list | None = None) -> list:
    """Lit une banque YAML de QuizForge et renvoie ses questions."""
    doc = yaml.safe_load(chemin.read_text(encoding="utf-8")) or {}
    qs = doc.get("questions", [])
    if rapport is not None:
        rapport.append(f"{chemin.name} : {len(qs)} question(s)")
    return qs


def dedoublonner(questions: list, rapport: list) -> list:
    """Garde une question par énoncé ; une version avec réponse l'emporte sur un « essai » vide.

    Les doublons écartés, et ceux qui divergent, sont signalés dans ``rapport``.
    """
    vues = {}
    for q in questions:
        k = cle_question(q).split("|", 1)[1]
        if k in vues:
            ancien = vues[k]
            if ancien["type"] == "essai" and q["type"] != "essai":
                vues[k] = q
                rapport.append(f"Doublon : {q.get('source')} remplace {ancien.get('source')} (version avec réponse)")
            elif q["type"] == "essai" and ancien["type"] != "essai":
                rapport.append(f"Doublon ignoré : {q.get('source')} (sans réponse) = {ancien.get('source')}")
            else:
                if ancien["type"] != q["type"] or ancien.get("reponse") != q.get("reponse"):
                    rapport.append(f"ATTENTION doublon divergent : {q.get('source')} ≠ {ancien.get('source')} "
                                   f"« {q['question'][:60]} » — version gardée : {ancien.get('source')}")
                else:
                    rapport.append(f"Doublon ignoré : {q.get('source')} = {ancien.get('source')} « {q['question'][:60]} »")
            continue
        vues[k] = q
    return list(vues.values())


# --------------------------------------------------------------------------- modèle Excel

MODELE = {
    "VF": (["Num", "Titre", "Question", "Réponse", "Rétroaction", "Tags", "Question EN", "Rétroaction EN"],
           [[1, "Maillage fin", "Un maillage plus fin garantit toujours une meilleure précision des résultats.",
             "F", "La convergence dépend aussi du type d'élément et des singularités.", "MEF;maillage",
             "A finer mesh always guarantees more accurate results.",
             "Convergence also depends on the element type and on singularities."]]),
    "QCM": (["Num", "Titre", "Question", "Réponse correcte", "Option 1", "Option 2", "Option 3", "Option 4",
             "Feedback 1", "Feedback 2", "Feedback 3", "Feedback 4", "Code erreur 1", "Code erreur 2", "Code erreur 3",
             "Code erreur 4", "Rétroaction"],
            [[1, "Unité fréquence", "La pulsation propre d'un oscillateur vaut √(k/m). Quelle est sa fréquence propre ?",
              "2", "√(k/m)", "√(k/m) / 2π", "2π √(k/m)", "", "C'est la pulsation, en rad/s.", "",
              "Vous avez multiplié au lieu de diviser par 2π.", "", "pulsation pour fréquence", "", "facteur 2π inversé", "",
              "f = ω / 2π, en Hz."],
             [2, "Conditions de Dirichlet", "Quelles conditions sont de type Dirichlet ?", "1;3",
              "Déplacement imposé", "Force imposée", "Température imposée", "Flux imposé", "", "", "", "",
              "", "Neumann pris pour Dirichlet", "", "Neumann pris pour Dirichlet",
              "Dirichlet : on impose la valeur de l'inconnue (déplacement, température) ; Neumann : sa dérivée (force, flux)."]]),
    "Appariement": (["Num", "Titre", "Question", "Choix1", "Rep1", "Choix2", "Rep2", "Choix3", "Rep3",
                     "Choix4", "Rep4", "Rétroaction"],
                    [[1, "Éléments SDOF", "Associer chaque élément à son rôle.", "Masse", "Inertie", "Ressort",
                      "Élasticité", "Amortisseur", "Dissipation", "", "Rigidité infinie",
                      "La masse stocke l'énergie cinétique, le ressort l'énergie de déformation, l'amortisseur la dissipe."]]),
    "Numerique": (["Num", "Titre", "Question", "Valeur", "Tolérance", "Unité", "Feedback juste", "Erreur 1",
                   "Feedback erreur 1", "Code erreur 1", "Feedback faux", "Indice 1", "Rétroaction"],
                  [[1, "Dommage Miner", "D1 = n1/N1 avec n1 = 5000 et N1 = 10000. Que vaut D1 ?", 0.5, "2%", "",
                    "Exact.", 2, "Rapport inversé : le dommage vaut n/N (cycles appliqués / cycles à rupture), pas N/n.",
                    "rapport inversé",
                    "Reprenez la définition du dommage partiel d'un bloc.",
                    "Le dommage est une fraction de la durée de vie consommée : il est compris entre 0 et 1.",
                    "D1 = 5000 / 10000 = 0,5"]]),
    "ReponseCourte": (["Num", "Titre", "Question", "Réponses acceptées", "Casse", "Rétroaction"],
                      [[1, "Condition naturelle", "Une condition aux limites portant sur la dérivée est dite condition de …",
                        "Neumann;Von Neumann", "F", "Neumann : condition sur la dérivée (flux, effort) ; Dirichlet : sur la valeur."]]),
    "Essai": (["Num", "Titre", "Question", "Réponse attendue", "Rétroaction"],
              [[1, "Corps rigide", "Pourquoi le modèle de corps rigide ne suffit-il pas à décrire les efforts intérieurs ?",
                "Éléments attendus : mouvements rigidifiants, puissance nulle…", ""]]),
    "Schema": (["Num", "Titre", "Question", "Projet", "Rétroaction", "Tags"],
               [[1, "Vecteur contrainte", "", "vecteur_contrainte_pointeur.json", "", "MMC"],
                [2, "Matrice Rainflow", "Placez les 3 cycles du signal dans la matrice Rainflow.", "rainflow_pointeur.json", "", "Fatigue"]]),
    "Trous": (["Num", "Titre", "Question", "Mot 1", "Mot 2", "Mot 3", "Leurre 1", "Leurre 2", "Mode", "Rétroaction"],
              [[1, "Miner", "Le dommage partiel d'un bloc vaut [[1]] divisé par [[2]] ; la règle de Miner prédit la rupture "
                "quand la somme des dommages atteint [[3]].", "n", "N", "1|2", "σ", "0|2", "glisser",
                "D = Σ nᵢ/Nᵢ ; rupture prédite pour D = 1."],
               [2, "Domaines", "La fatigue [[1]] se termine vers 10⁴ cycles ; l'endurance [[2]] commence vers 10⁷ cycles.",
                "oligocyclique", "illimitée", "", "polycyclique", "limitée", "liste",
                "Oligocyclique : peu de cycles, déformation plastique à chaque cycle ; endurance illimitée au-delà d'environ 10⁷ cycles."]]),
}

LISEZMOI = [
    "QuizForge — classeur modèle",
    "",
    "Un onglet = un lot de questions d'un même type. Le type est reconnu d'après les en-têtes, pas d'après le nom de l'onglet.",
    "VF : Réponse = T/F, V/F, Vrai/Faux. Colonnes facultatives : Feedback juste, Feedback faux.",
    "QCM : Réponse correcte = numéro de l'option (1, 2…), lettre (A, B…) ou texte. Plusieurs bonnes réponses : 1;3.",
    "Appariement : Choix n / Rep n. Une Rep sans Choix = mauvaise réponse supplémentaire (distracteur).",
    "Numérique : Tolérance absolue (0.01) ou relative (2%). Unité facultative. Erreur n = valeur obtenue avec une erreur type",
    "  (même tolérance), Feedback erreur n = son retour ; Feedback faux = retour pour toute autre valeur (XML seulement).",
    "Séance (tous les types) : numéro de la séance où la notion est vue (ou ligne « $SEANCE: 3 » en tête d'onglet) -> tag S03 ;",
    "  convertir --seance 3 écrit le plan du quiz de la séance 3 (sections, nombre à tirer, rappels) selon quiz.tirage du profil.",
    "Code erreur n (QCM et Numérique) : nom court de l'erreur type visée par le leurre n ou l'erreur n, écrit toujours de la",
    "  même façon d'une question à l'autre ; gardé dans la banque YAML et lu par DiagForge (bilan -q banque.yaml).",
    "Indice n (tous les types sauf Trous et Schéma) : indices montrés entre deux essais, si le test Moodle est en mode",
    "  « interactif avec plusieurs essais » (XML seulement).",
    "Réponse courte : réponses acceptées séparées par ;",
    "Essai : réponse libre corrigée à la main ; Réponse attendue = aide au correcteur.",
    "Trous : texte à trous. Dans la Question, [[1]], [[2]]… renvoient aux colonnes Mot 1, Mot 2… ; Leurre n = mots en trop.",
    "  « n|2 » met le mot dans le groupe 2 (un trou n'accepte que les mots de son groupe). Un même [[k]] répété = mot illimité.",
    "  Mode : glisser (glisser-déposer dans le texte, par défaut) ou liste (listes déroulantes). Export en Moodle XML seulement.",
    "Schéma : glisser-déposer sur image ou marqueurs. Projet = fichier enregistré par scripts/quizforge/outils/pointeur.html (« Enregistrer le projet »),",
    "  chemin relatif au classeur. Question vide = énoncé du projet ; idem pour la Rétroaction. Export en Moodle XML seulement.",
    "Partout : Titre (si vide ou Q1, Q2… il devient <onglet>-<numéro>), Rétroaction générale, Tags séparés par ;",
    "Tags : colonne Tags (par question), ligne « $TAGS: S1; MEF » au-dessus des en-têtes (tout l'onglet),",
    "  option --tags \"MEF;S1\" (tout le classeur), tags du profil ; le type de question (VF, QCM…) est ajouté automatiquement.",
    "Colonnes : on peut en ajouter (Option 5, Choix 5 / Rep 5, Mot 4, Leurre 3…) ; une colonne inconnue est ignorée.",
    "Catégorie Moodle : $course$/top/<racine>/<classeur>/<onglet>, ou une ligne « $CATEGORY: … » au-dessus des en-têtes.",
    "Formules : préférez l'export Moodle XML et la syntaxe \\( … \\) (filtre MathJax).",
    "Bilingue : ajoutez une colonne « <en-tête> EN » à côté de chaque colonne de texte (Question EN, Option 1 EN, Rep1 EN, Rétroaction EN…).",
    "  Les réponses (V/F, numéro de la bonne option, valeur) ne se traduisent pas. Voir outils/quizforge/README.md pour les deux modes de sortie.",
    "",
    "Commande (depuis le dossier Forge_E-Learning) : python scripts/quizforge/quizforge.py convertir ce_classeur.xlsx",
]


def creer_modele(chemin: Path, vide: bool = False, onglets=None):
    """Écrit le classeur modèle dans ``chemin`` : un onglet « Lisez-moi » puis un onglet par type de question.

    ``vide`` : en-têtes seulement, sans exemples ; ``onglets`` : onglets à garder (tous par défaut).
    """
    import openpyxl
    from openpyxl.styles import Alignment, Font, PatternFill

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Lisez-moi"
    for i, l in enumerate(LISEZMOI, 1):
        ws.cell(i, 1, l).font = Font(bold=(i == 1), size=14 if i == 1 else 11)
    ws.column_dimensions["A"].width = 120
    for nom, (entetes, exemples) in MODELE.items():
        if onglets and nom not in onglets:
            continue
        w = wb.create_sheet(nom)
        w.append(entetes)
        for e in ([] if vide else exemples):
            w.append(e)
        for c in w[1]:
            c.font = Font(bold=True, color="FFFFFF")
            c.fill = PatternFill("solid", fgColor=COULEUR_PRINCIPALE)
        for i, h in enumerate(entetes, 1):
            w.column_dimensions[openpyxl.utils.get_column_letter(i)].width = 60 if h == "Question" else 22
        for row in w.iter_rows(min_row=2):
            for c in row:
                c.alignment = Alignment(wrap_text=True, vertical="top")
        w.freeze_panes = "A2"
    wb.save(chemin)


# --------------------------------------------------------------------------- commandes


def lire_fichiers(fichiers, racine, rapport, reparer=False, nom=""):
    """Lit des classeurs Excel, fichiers GIFT et banques YAML (ou les dossiers qui les contiennent) et renvoie leurs questions.

    Dans un dossier, les sous-dossiers prolongent la catégorie ; les sorties de QuizForge et les rapports sont ignorés.
    """
    qs = []
    for f in fichiers:
        f = Path(f)
        if f.is_dir():
            for p in sorted(f.rglob("*")):
                if p.suffix.lower() not in (".xlsx", ".txt", ".gift", ".yaml") or p.name.startswith("~$") \
                        or "_QuizForge" in str(p) or p.name.endswith("_rapport.txt") or p.name == "rapport.txt":
                    continue
                sous = "/".join(p.relative_to(f).parent.parts)
                qs += lire_fichiers([p], "/".join(x for x in (racine, sous) if x), rapport, reparer)
        elif f.suffix.lower() == ".xlsx":
            qs += lire_excel(f, racine, rapport, reparer, nom)
        elif f.suffix.lower() in (".txt", ".gift"):
            qs += lire_gift(f, racine, rapport)
        elif f.suffix.lower() in (".yaml", ".yml"):
            qs += lire_banque_yaml(f, rapport)
        else:
            rapport.append(f"{f.name} : format non pris en charge")
    return qs


def chemin_court(p) -> str:
    """Chemin relatif au dépôt quand il y est (rapports sans chemin personnel), sinon tel quel."""
    try:
        return Path(p).resolve().relative_to(chemins.RACINE).as_posix()
    except (ValueError, OSError):
        return str(p)


def appliquer_cours(a) -> list:
    """Option ``--cours`` : complète profil, catégorie, effectif et étiquettes avec ceux du cours, de sa déclinaison
    et de son édition (les options données l'emportent ; les étiquettes s'ajoutent). Renvoie les lignes du rapport."""
    a._cours = None
    if not getattr(a, "cours", None):
        return []
    import cours_options
    try:
        r = cours_options.resoudre(a.cours)
    except Exception as e:                           # cours inconnu ou illisible : on le dit, on continue sans lui
        return [f"Cours « {a.cours} » non appliqué : {e}"]
    a._cours = r
    if not getattr(a, "profil", None) and r["profil"]:
        a.profil = r["profil"]
    if hasattr(a, "categorie") and a.categorie is None and r["categorie"]:
        a.categorie = r["categorie"]
    if hasattr(a, "tags"):
        a.tags = ";".join(dict.fromkeys(decouper_tags(a.tags) + r["tags"]))
    if hasattr(a, "etudiants") and a.etudiants is None and r["effectif"]:
        a.etudiants = int(r["effectif"])
    return [f"Cours : {r['libelle']}" + (f" (profil {r['profil']})" if r["profil"] else "")]


def appliquer_profil(a):
    """Charge le profil puis complète les options laissées vides sur la ligne de commande."""
    ecrire_index_profils()
    nom = getattr(a, "profil", None)
    if not nom and profil_par_defaut():
        nom = profil_par_defaut()
        print(f"Profil par défaut : {nom} (option --profil pour en choisir un autre)")
    charger_profil(nom)
    if getattr(a, "categorie", None) is None:
        a.categorie = P.get("categorie", "")
    if hasattr(a, "langues"):
        a.langues = comprendre(a.langues, ["separe", "multilang"], "--langues") if a.langues else P["langues"]["mode"]
    if hasattr(a, "langue_base") and a.langue_base is None:
        a.langue_base = P["langues"]["base"]
    a.formats = ([comprendre(x, ["xml", "gift", "yaml"], "--formats") for x in decouper_tags(a.formats)]
                 if getattr(a, "formats", None) else P["formats"])
    ligne = f"Profil : {P['nom']} ({chemin_court(P['_fichier'])})" if P.get("nom") else "Profil : aucun (réglages par défaut)"
    return [ligne]


def cmd_convertir(a):
    """Commande ``convertir`` : écrit pour chaque fichier, selon les formats retenus, la banque YAML, le Moodle XML,
    les GIFT par catégorie, et ``rapport.txt``.

    Les sorties vont dans ``<fichier>_QuizForge`` (ou ``--sortie``) ; avec ``--seance``, le plan du quiz de séance est écrit aussi.
    """
    a.fichiers = [trouver_fichier(f, quoi="classeur") for f in a.fichiers]
    lignes_cours = appliquer_cours(a)
    rapport = lignes_cours + appliquer_profil(a)
    for f in a.fichiers:
        f = Path(f)
        version = None
        if getattr(a, "_cours", None) and not a.sortie:   # version rangée dans l'édition (ou le cours), jamais écrasée
            import registre
            reglages = {k: getattr(a, k, None) for k in ("profil", "categorie", "nom", "tags", "seance", "etudiants",
                                                          "formats", "reparer", "langues", "langue_base", "rappel", "graine")}
            b, emp = registre.base(a._cours), registre.empreinte(f, reglages)
            version = registre.preparer(b, f, getattr(a, "seance", None), emp)
            if version["identique"]:
                v = version["identique"]
                rapport.append(f"{f.name} : identique à la version {v['id']} (même classeur, mêmes réglages) : rien d'écrit")
                print(f"Version : {v['dossier']}")
                continue
        qs = filtrer_types(lire_fichiers([f], a.categorie, rapport, a.reparer, a.nom), rapport)
        ajouter_tags(qs, decouper_tags(a.tags), rapport)
        if not qs:
            continue
        if version:
            sortie, prefixe = Path(version["dossier"]), f"{f.stem}_{version['label']}"
        else:
            sortie, prefixe = (Path(a.sortie) if a.sortie else f.parent / f"{f.stem}_QuizForge"), f.stem
            if not a.sortie:
                rapport.append(f"   (sans cours choisi, {sortie.name} est réécrit à chaque conversion ; avec --cours, "
                               "chaque conversion devient une version rangée dans l'édition)")
        a._prefixe = prefixe
        sortie.mkdir(parents=True, exist_ok=True)
        if "yaml" in a.formats:
            ecrire_banque(qs, sortie / f"{prefixe}_banque.yaml")
        for suffixe, lot_v in versions(qs, a.langues, a.langue_base):
            if "xml" in a.formats:
                ecrire_xml(lot_v, sortie / f"{prefixe}_moodle{suffixe}.xml")
            par_cat = {}
            for q in lot_v:
                par_cat.setdefault(q["categorie"].rstrip("/").split("/")[-1], []).append(q)
            for nom, lot in par_cat.items():
                if any(q["type"] in XML_SEUL for q in lot) and "gift" in a.formats:
                    rapport.append(f"   {nom} : questions « Schéma » ou « Texte à trous » en Moodle XML seulement "
                                   "(GIFT ne les décrit pas)")
                lot = [q for q in lot if q["type"] not in XML_SEUL]
                if lot and "gift" in a.formats:
                    ecrire_gift(lot, sortie / f"{re.sub(r'[^A-Za-z0-9_-]+', '_', nom)}{suffixe}.gift.txt")
            if suffixe:
                rapport.append(f"   version {suffixe[1:]} : {len(lot_v)} question(s)")
        if getattr(a, "seance", None):
            rapport += ecrire_quiz_seance(qs, a, f, sortie)
        elif any("seance" in q for q in qs):
            par = Counter(q["seance"] for q in qs if "seance" in q)
            rapport.append("   Séances : " + ", ".join(f"{k} : {v} q." for k, v in sorted(par.items(), key=lambda x: str(x[0])))
                           + " (tags S01, S02… ; --seance n compose le quiz de la séance n avec des rappels)")
        rapport.append(f"→ {len(qs)} question(s) écrites dans {chemin_court(sortie)}")
        import qualite
        rapport += qualite.rapport_hasard(qs, P["bareme"]["qcm"]["mauvaise_option"])
        (sortie / (f"{prefixe}_rapport.txt" if version else "rapport.txt")).write_text("\n".join(rapport) + "\n", encoding="utf-8")
        if version:
            registre.enregistrer(b, version, f, reglages, qs, getattr(a, "seance", None), emp, a._cours["cours"])
            rapport.append(f"Version {version['id']} inscrite au registre de {registre.rel(b)}")
            print(f"Version : {registre.rel(version['dossier'])}")
    print("\n".join(rapport))


def ecrire_quiz_seance(qs: list, a, f: Path, sortie: Path) -> list:
    """Écrit le plan du quiz de la séance n (``<classeur>_plan_Snn.md``) et renvoie les lignes à ajouter au rapport.

    Rien n'est recopié dans la banque. Le plan donne une section par catégorie de la séance, puis une section
    de rappels par séance précédente, avec le nombre de questions à tirer selon ``quiz.tirage`` du profil.
    Il donne aussi le score au hasard et le seuil du quiz tel qu'il sera tiré, et le nombre de réponses attendu
    par question (DiagForge calcule la discrimination à partir de 20 réponses et la juge solide à partir de 50).
    Rappels : pratique de récupération espacée (``reference/A_tests_retroaction/yang2021.md``, ``murray2025.md``).
    """
    import random
    import qualite
    Z = P["quiz"]
    n, mode = a.seance, Z["tirage"]
    part = a.rappel if a.rappel is not None else Z["rappel"]
    hasard = random.Random(a.graine if a.graine is not None else n)
    pools = defaultdict(list)                     # (séance, catégorie) -> questions
    for q in qs:
        if isinstance(q.get("seance"), int) and q["seance"] <= n:
            pools[(q["seance"], q["categorie"])].append(q)
    if not any(s == n for s, _ in pools):
        return [f"Quiz de la séance {n} : aucune question de la séance {n} (colonne Séance ou ligne $SEANCE de l'onglet)"]
    seances_cat = defaultdict(set)
    for q in qs:
        seances_cat[q["categorie"]].add(q.get("seance"))

    def k_partiel(N):
        return max(1, min(N, int(Z["max_tire"]), round(N * float(Z["part_tiree"]))))

    sections = []
    for (s, cat), L in sorted(pools.items(), key=lambda x: (x[0][0] != n, x[0][0], x[0][1])):
        if s != n:
            continue
        k = len(L) if mode in ("commun", "mixte") else k_partiel(len(L))
        sections.append({"seance": s, "cat": cat, "N": len(L), "k": k, "L": L, "rappel": False})
    nouvelles = sum(x["k"] for x in sections)
    voulu = round(nouvelles * part / (1 - part)) if 0 < part < 1 else 0
    # rappels : une section par séance passée (filtre tag Snn sur la catégorie commune, sous-catégories comprises),
    # nombre réparti au prorata des questions disponibles (plus forts restes)
    passees = defaultdict(list)
    for (s, cat), L in pools.items():
        if s < n:
            passees[s] += L
    total = sum(len(L) for L in passees.values())
    if voulu and total:
        parts = {s: voulu * len(L) / total for s, L in passees.items()}
        alloc = {s: int(v) for s, v in parts.items()}
        for s in sorted(parts, key=lambda s: -(parts[s] - alloc[s]))[:voulu - sum(alloc.values())]:
            alloc[s] += 1
        for s in sorted(passees):
            L = passees[s]
            if alloc[s]:
                cats = [q["categorie"].rstrip("/").split("/") for q in L]
                commun_ = [c[0] for c in zip(*cats) if len(set(c)) == 1]
                sections.append({"seance": s, "cat": "/".join(commun_), "N": len(L),
                                 "k": min(alloc[s], len(L)), "L": L, "rappel": True})
    infos = None
    if getattr(a, "_cours", None):
        import cours_options
        infos = cours_options.seance(a._cours, n)
    lignes = [f"# Plan du quiz de la séance {n}", ""]
    if getattr(a, "_cours", None):
        lignes += [f"Cours : {a._cours['libelle']}" + (f" ; {cours_options.decrire_seance(infos)}" if infos else ""), ""]
    lignes += [
              f"Profil : tirage « {mode} » (part tirée {float(Z['part_tiree']):.0%}, au plus {Z['max_tire']} par catégorie), "
              f"rappels : {part:.0%} du quiz.", "",
              "| Section | Catégorie Moodle | Filtre | Disponibles | À tirer | Questions à ajouter |", "| --- | --- | --- | --- | --- | --- |"]
    h_tot = s_tot = k_tot = 0
    for x in sections:
        filtre = (f"tag S{x['seance']:02d}, sous-catégories comprises" if x["rappel"] else
                  f"tag S{x['seance']:02d}" if len(seances_cat[x["cat"]]) > 1 else "catégorie seule")
        commun = x["commun"] = (mode == "commun") or (mode == "mixte" and not x["rappel"])
        if commun and x["rappel"]:
            filtre = "questions listées, ajoutées depuis la banque"
        if commun and x["k"] < x["N"]:                # rappels communs : mêmes questions pour tous, tirées une fois
            choisies = sorted(hasard.sample(x["L"], x["k"]), key=lambda q: q["titre"])
        else:
            choisies = x["L"] if commun else []
        quoi = ("toutes (depuis la banque)" if commun and x["k"] == x["N"] else
                "; ".join(q["titre"] for q in choisies) if commun else f"{x['k']} au hasard")
        lignes.append(f"| {'Rappel S%02d' % x['seance'] if x['rappel'] else 'Séance S%02d' % x['seance']} | "
                      f"{x['cat'].replace('$course$/top/', '')} | {filtre} | {x['N']} | {x['k']} | {quoi} |")
        r = [qualite.hasard_question(q, P["bareme"]["qcm"]["mauvaise_option"]) for q in x["L"]]
        h_tot += x["k"] * sum(v[0] if v else 0 for v in r) / len(r)
        s_tot += x["k"] * sum(v[1] if v else 0.5 for v in r) / len(r)
        k_tot += x["k"]
    lignes += ["", f"Quiz de {k_tot} questions ({nouvelles} de la séance, {k_tot - nouvelles} rappels). Au hasard : "
               f"{100 * h_tot / k_tot:.0f} % ; seuil pour la moitié des connaissances : {100 * s_tot / k_tot:.0f} %."]
    if a.etudiants:
        rep_q = lambda x: a.etudiants if x["commun"] else a.etudiants * x["k"] / x["N"]  # noqa: E731
        faibles = [x for x in sections if rep_q(x) < 20]
        lignes.append(f"Pour {a.etudiants} étudiants, réponses attendues par question : "
                      + ", ".join(f"{'rappel S%02d' % x['seance'] if x['rappel'] else x['cat'].rsplit('/', 1)[-1]} "
                                  f"{rep_q(x):.0f}" for x in sections)
                      + (". Sous 20 réponses, DiagForge ne calcule pas la discrimination : tirer plus, ou réunir plusieurs "
                         "groupes ou années." if faibles else "."))
    if mode != "commun":
        lignes.append("Dans Moodle : une section par ligne, « Ajouter une question aléatoire » avec le filtre indiqué et le "
                      "nombre à tirer ; cocher « Mélanger » dans chaque section.")
    nom_plan = f"{a._prefixe}_plan.md" if getattr(a, "_prefixe", f.stem) != f.stem else f"{f.stem}_plan_S{n:02d}.md"
    (sortie / nom_plan).write_text("\n".join(lignes) + "\n", encoding="utf-8")
    return [f"Plan du quiz de la séance {n} -> {nom_plan} :"] + ["   " + l for l in lignes[2:] if l]


def cmd_importer(a):
    """Commande ``importer`` : réunit des fichiers existants dans une banque YAML unique, dédoublonnée.

    Écrit aussi ``<banque>_rapport.txt`` et, avec ``--xml`` (ou un profil qui le prévoit), la banque en Moodle XML.
    """
    a.fichiers = [trouver_fichier(f, quoi="fichier") for f in a.fichiers]
    a.banque = str(nom_sortie(a.banque, ".yaml")) if not a.banque.lower().endswith((".yaml", ".yml")) else a.banque
    rapport = appliquer_profil(a)
    qs = filtrer_types(lire_fichiers(a.fichiers, a.categorie, rapport, a.reparer), rapport)
    ajouter_tags(qs, decouper_tags(a.tags), rapport)
    qs = dedoublonner(qs, rapport)
    banque = Path(a.banque)
    ecrire_banque(qs, banque)
    if a.xml or (a.profil and "xml" in a.formats):
        ecrire_xml(qs, banque.with_suffix(".xml"))
    rapport.append(f"→ banque {banque} : {len(qs)} question(s) distinctes")
    banque.with_name(banque.stem + "_rapport.txt").write_text("\n".join(rapport) + "\n", encoding="utf-8")
    print("\n".join(rapport))


TEXTES_TRADUISIBLES = re.compile(r"(question|titre|retroaction.*|feedback.*|option ?\w+|choix ?\d+|rep ?\d+|mot ?\d+|leurre ?\d+|"
                                 r"reponses acceptees|reponse attendue)")


def fusionner_classeurs(fr: Path, autre: Path, lang: str = "en") -> tuple:
    """Ajoute à une copie du classeur FR les colonnes « … EN » lues dans le classeur traduit (même structure).

    Écrit ``<classeur>_bilingue.xlsx`` et renvoie ``(chemin, rapport)`` ; les réponses qui diffèrent entre les deux
    classeurs sont signalées.
    """
    import openpyxl
    wa, wb_ = openpyxl.load_workbook(fr), openpyxl.load_workbook(autre, data_only=True)
    rapport = []
    if len(wa.worksheets) != len(wb_.worksheets):
        rapport.append(f"ATTENTION : {len(wa.worksheets)} onglets d'un côté, {len(wb_.worksheets)} de l'autre ; "
                       "appariement par ordre sur les premiers")
    for sa, sb in zip(wa.worksheets, wb_.worksheets):
        la = [list(r) for r in sa.iter_rows(values_only=True)]
        lb = [list(r) for r in sb.iter_rows(values_only=True)]
        ia = next((i for i, r in enumerate(la[:12]) if "question" in [norm(c) for c in r]), None)
        ib = next((i for i, r in enumerate(lb[:12]) if "question" in [norm(c) for c in r]), None)
        if ia is None or ib is None:
            rapport.append(f"{sa.title} / {sb.title} : ignoré (en-tête « Question » introuvable)")
            continue
        Ha = [norm(c) for c in la[ia]]
        Hb = [norm(c) for c in lb[ib]]
        da = [r for r in la[ia + 1:] if any(txt(c) for c in r)]
        db = [r for r in lb[ib + 1:] if any(txt(c) for c in r)]
        if len(da) != len(db):
            rapport.append(f"ATTENTION {sa.title} / {sb.title} : {len(da)} lignes FR, {len(db)} lignes {lang.upper()}")
        c_rep_a, c_rep_b = _col(Ha, "reponse", "response", "reponse correcte"), _col(Hb, "reponse", "response", "reponse correcte")
        cols = [j for j, h in enumerate(Ha) if h and TEXTES_TRADUISIBLES.fullmatch(h) and h != "titre" and j < len(Hb)]
        depart = sa.max_column + 1
        for n, j in enumerate(cols):
            sa.cell(ia + 1, depart + n, f"{txt(la[ia][j])} {lang.upper()}")
        lignes_a = [i for i, r in enumerate(la) if i > ia and any(txt(c) for c in r)]
        for k, (i, rb) in enumerate(zip(lignes_a, db)):
            if c_rep_a is not None and c_rep_b is not None and \
                    norm(la[i][c_rep_a]).strip("{} ") != norm(rb[c_rep_b]).strip("{} ") and \
                    lire_booleen(la[i][c_rep_a]) != lire_booleen(rb[c_rep_b]):
                rapport.append(f"ATTENTION {sa.title} ligne {i + 1} : réponse FR « {txt(la[i][c_rep_a])} » ≠ "
                               f"{lang.upper()} « {txt(rb[c_rep_b])} »")
            for n, j in enumerate(cols):
                if j < len(rb) and txt(rb[j]):
                    sa.cell(i + 1, depart + n, txt(rb[j]))
        rapport.append(f"{sa.title} + {sb.title} : {min(len(da), len(db))} ligne(s), colonnes ajoutées : "
                       + ", ".join(f"{txt(la[ia][j])} {lang.upper()}" for j in cols))
    sortie = fr.with_name(fr.stem + "_bilingue.xlsx")
    wa.save(sortie)
    return sortie, rapport


def cmd_fusionner(a):
    """Commande ``fusionner`` : réunit un classeur FR et sa traduction en un classeur bilingue."""
    sortie, rapport = fusionner_classeurs(trouver_fichier(a.classeur, (".xlsx",), "classeur"),
                                          trouver_fichier(a.traduction, (".xlsx",), "classeur traduit"), a.langue)
    print("\n".join(rapport))
    print(f"→ classeur bilingue : {sortie}")


def cmd_reparer(a):
    """Commande ``reparer`` : écrit une copie corrigée d'un classeur abîmé par un remplacement « V » → « T »."""
    sortie, corr = reparer_classeur(trouver_fichier(a.classeur, (".xlsx",), "classeur"))
    print("\n".join(corr) or "Aucun texte abîmé détecté.")
    print(f"→ {len(corr)} cellule(s) corrigée(s) dans {sortie} (l'original n'est pas modifié)")


def cmd_modele(a):
    """Commande ``modele`` : crée le classeur modèle (ou un classeur vide), sans écraser un fichier existant sauf avec ``--ecraser``."""
    sortie = nom_sortie(a.sortie, ".xlsx") if a.sortie else Path("vide_QuizForge.xlsx" if a.vide else "modele_QuizForge.xlsx")
    if sortie.exists() and not a.ecraser:
        sys.exit(f"{sortie} existe déjà : rien n'est écrasé. Choisissez un autre nom (-s) ou ajoutez --ecraser.")
    onglets = [comprendre(o, list(MODELE), "onglet") for o in decouper_tags(a.onglets)]
    creer_modele(sortie, a.vide, onglets)
    print(f"{'Classeur vide' if a.vide else 'Modèle'} créé : {sortie}")


CLES_PROFIL = set(PROFIL_DEFAUT) | {"nom", "description", "alias", "defaut", "charte", "categorie", "campus",
                                    "vocabulaire", "parcours", "structure", "formations",
                                    "codes", "promo", "habillage"}


def valider_profil(f: Path) -> list:
    """Vérifie un fichier de profil (YAML lisible, clés connues, valeurs comprises) et renvoie la liste des problèmes."""
    pbs = []
    try:
        lu = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as e:
        return [f"YAML illisible : {str(e).splitlines()[0]}"]
    for k in lu:
        if k not in CLES_PROFIL:
            pbs.append(f"clé « {k} » inconnue (possibles : {', '.join(sorted(CLES_PROFIL))})")
    try:
        charger_profil(str(f))
    except SystemExit as e:
        pbs.append(str(e))
    return pbs


def valider_projet(f: Path) -> list:
    """Vérifie un projet du pointeur (JSON) et renvoie la liste des problèmes : type, image, zones, énoncé, leurres."""
    import json
    try:
        d = json.loads(f.read_text(encoding="utf-8"))
    except (ValueError, UnicodeDecodeError) as e:
        return [f"JSON illisible ({e})"]
    pbs = []
    if d.get("type") not in ("ddimageortext", "ddmarker"):
        pbs.append(f"type « {d.get('type')} » inconnu")
    if not d.get("image"):
        return pbs + ["pas d'image de fond"]
    ids = {e["id"] for e in d.get("etiquettes", [])}
    zones = d.get("zones", [])
    if not zones:
        pbs.append("aucune zone placée")
    if any(z.get("etiq") not in ids for z in zones):
        pbs.append("zone liée à une étiquette supprimée")
    if not d.get("enonce"):
        pbs.append("énoncé vide (à donner dans la colonne Question du classeur)")
    w = d["image"].get("w", 0)
    if w > 800:
        pbs.append(f"image de fond de {w} px : Moodle la réduira (choisir 700 px dans le pointeur)")
    if d.get("type") == "ddimageortext" and len(d.get("etiquettes", [])) == len(zones):
        pbs.append("pas de leurre (autant d'étiquettes que de cases)")
    return pbs


def cmd_valider(a):
    """Commande ``valider`` : vérifie classeurs, projets du pointeur et profils, sans rien écrire.

    Signale aussi les points d'écriture à vérifier dans les questions (rétroaction absente, indices qui
    trahissent la clé, défauts d'écriture : voir ``qualite``).
    """
    import qualite
    try:
        charger_profil(profil_par_defaut())      # barème du profil par défaut, pour les alertes sur les QCM à plusieurs réponses
    except Exception:
        pass
    cibles = [trouver_fichier(c, EXT_CLASSEURS + (".json",), "fichier") for c in a.fichiers] or [Path(".")]
    fichiers = []
    for c in cibles:
        if c.is_dir():
            fichiers += [x for x in sorted(c.rglob("*")) if x.is_file() and not any(d.endswith("_QuizForge") for d in x.parent.parts)
                         and not x.name.startswith("~$")
                         and (x.suffix.lower() == ".xlsx" or x.name.endswith("_pointeur.json"))]
        else:
            fichiers.append(c)
    bilan = {}
    for f in fichiers:
        if f.suffix.lower() == ".xlsx":
            rapport = []
            try:
                qs = lire_excel(f, "", rapport)
            except Exception as e:
                bilan[f] = [f"classeur illisible ({e})"]
                continue
            gardes = ("ATTENTION", "ignorée", "compris comme", "non reconnue", "texte abîmé", "sans mot",
                      "jamais proposé", "pas de trou", "différents")
            pbs = [r.split(" › ", 1)[-1] for r in rapport if any(g in r for g in gardes)]
            bilan[f] = pbs + ([] if qs else ["aucune question lue"]) + qualite.controler(qs, P["bareme"]["qcm"]["mauvaise_option"])
        elif f.name.endswith(".json"):
            bilan[f] = valider_projet(f)
    for d in dossiers_profils():
        for f in chemins.fichiers_profils(d):
            bilan[f] = valider_profil(f)
        defauts = [n for n, v in lister_profils().items() if v["defaut"]]
        if len(defauts) > 1:
            bilan.setdefault(d / "index_profils.json", []).append(f"plusieurs profils par défaut : {', '.join(defauts)}")
    n_ok = 0
    for f, pbs in bilan.items():
        if pbs:
            print(f"\nÀ VOIR  {f}")
            for x in pbs:
                print(f"   - {x}")
        else:
            n_ok += 1
            print(f"OK      {f}")
    print(f"\n{n_ok} fichier(s) sans remarque, {len(bilan) - n_ok} à voir.")
    if any(x.startswith("[!") for pbs in bilan.values() for x in pbs):
        print("Points d'écriture : [!!!] indice fort ou défaut qui fausse la question, [!!] à revoir, [!] à considérer. "
              "Ce sont des points à vérifier, pas des erreurs : une clé longue ou un « toujours » peuvent être voulus.")


def cmd_bilan(a):
    """Commande ``bilan`` (DiagForge) : bilan des résultats d'un test Moodle (exports Notes + Réponses) → classeur d'analyse.

    La couleur principale et le mode de tirage sont pris dans le profil s'il y en a un (voir :func:`bilan.bilan`).
    """
    for ligne in appliquer_cours(a):
        print(ligne)
    sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "diagforge"))
    import bilan
    couleur = COULEUR_PRINCIPALE
    try:
        nom = (a.profil or profil_par_defaut()) if lister_profils() else None
        if nom:
            pr = charger_profil(nom)
            ch = (pr or {}).get("charte") or {}
            role = (ch.get("roles") or {}).get("principal")
            couleur = str((ch.get("couleurs") or {}).get(role, role) or couleur).lstrip("#")
    except Exception:
        pass
    bilan.bilan(a.cibles, xml=a.questions, mode=comprendre(a.tentatives, ["toutes", "premiere", "derniere", "meilleure"], "tentatives"),
                sortie=a.sortie, couleur=couleur, roster=a.roster, images=not a.sans_images,
                tirage=(P.get("quiz") or {}).get("tirage") if P.get("_fichier") else None)
    noter_version_bilan(a)


def noter_version_bilan(a):
    """Reconnaît la version QuizForge du test d'après les noms des questions de l'export XML (registres des cours),
    l'écrit dans le bilan (onglet « Version ») et inscrit le bilan au registre."""
    try:
        import registre
    except ImportError:
        return
    xmls = [Path(x) for x in a.questions or []]
    for c in a.cibles:
        c = Path(c)
        xmls += sorted(c.glob("*.xml")) if c.is_dir() else ([c] if c.suffix.lower() == ".xml" else [])
    noms = registre.noms_xml(xmls)
    if not noms:
        print("Version du quiz : non cherchée (pas d'export XML des questions)")
        return
    if getattr(a, "_cours", None):
        bases = [registre.base(a._cours)] + ([registre.base({"cours": a._cours["cours"]})] if a._cours.get("edition") else [])
    else:
        bases = registre.tous()
    m = registre.reconnaitre(noms, bases)
    if not m or m["score"] < 0.5:
        print("Version du quiz : non reconnue dans les registres des cours")
        return
    v = m["version"]
    ecarts = (f" ; écarts : {m['manquantes']} question(s) de la version absente(s) de l'export, {m['en_trop']} en plus"
              if m["manquantes"] or m["en_trop"] else "")
    texte = f"Version du quiz : {v['id']} (registre de {registre.rel(m['base'])}){ecarts}"
    print(texte)
    d = Path(a.cibles[0]) if Path(a.cibles[0]).is_dir() else Path(a.cibles[0]).parent
    bilans = [Path(a.sortie)] if a.sortie else sorted(d.glob("bilan_*.xlsx"), key=lambda x: x.stat().st_mtime, reverse=True)[:1]
    b = bilans[0] if bilans and bilans[0].is_file() else None
    if b:
        try:
            import openpyxl
            wb = openpyxl.load_workbook(b)
            if "Version" in wb.sheetnames:
                del wb["Version"]
            ws = wb.create_sheet("Version")
            for ligne in (["Version du quiz", v["id"]], ["Registre", registre.rel(m["base"])], ["Dossier", v.get("dossier", "")],
                          ["Convertie le", v.get("date", "")], ["Questions communes", f"{m['score']:.0%}"],
                          ["Absentes de l'export", m["manquantes"]], ["En plus dans l'export", m["en_trop"]]):
                ws.append(ligne)
            ws.column_dimensions["A"].width, ws.column_dimensions["B"].width = 24, 70
            wb.save(b)
        except Exception as e:                       # le bilan reste valable sans cet onglet
            print(f"(onglet « Version » non écrit : {e})")
    registre.noter_bilan(m["base"], v["id"], b, b.with_name(b.stem + "_fiche_prof.html") if b else None)


def cmd_profils(a):
    """Commande ``profils`` : liste les profils, ou affiche les réglages complets de l'un d'eux ; régénère les index."""
    ecrire_index_profils(force=True)
    if a.nom:
        charger_profil(a.nom)
        print(f"# {P['_fichier']}")
        print(yaml.safe_dump({k: v for k, v in P.items() if not k.startswith("_")},
                             allow_unicode=True, sort_keys=False))
        return
    profils = lister_profils()
    for n, v in profils.items():
        alias = f"  alias : {', '.join(v['alias'])}" if v["alias"] else ""
        print(f"{n:12}{' (défaut)' if v['defaut'] else ''}  {v['description']}{alias}")
    if not profils:
        print("Aucun profil trouvé (dossier profils/).")
    for d in dossiers_profils():
        if (d / "index_profils.json").exists():
            print(f"Réglages acceptés : {d / 'index_profils.json'}")


COMMANDES = ["convertir", "importer", "reparer", "fusionner", "profils", "modele", "valider", "bilan", "assistant"]


def _demander(question: str, defaut: str = "") -> str:
    """Pose une question dans le terminal et renvoie la réponse, ou ``defaut`` si elle est vide."""
    r = input(f"{question}{f' [Entrée = {defaut}]' if defaut else ''} : ").strip()
    return r or defaut


def _choisir(titre: str, options: list, defaut=None, plusieurs=False):
    """Propose une liste numérotée et renvoie le choix ; réponse par numéro(s) (« 1,3 »), ou par les premières lettres."""
    print(f"\n{titre}")
    for k, o in enumerate(options, 1):
        print(f"  {k}. {o}{'   (défaut)' if o == defaut else ''}")
    while True:
        r = input(f"{'Numéros séparés par des virgules' if plusieurs else 'Numéro'}"
                  f"{' [Entrée = ' + (defaut if defaut else 'aucun') + ']' if (defaut or plusieurs) else ''} : ").strip()
        if not r:
            if defaut is not None or plusieurs:
                return ([defaut] if defaut else []) if plusieurs else defaut
            continue
        try:
            choix = []
            for x in re.split(r"[;, ]+", r):
                choix.append(options[int(x) - 1] if x.isdigit() else comprendre(x, options, "choix"))
            return choix if plusieurs else choix[0]
        except (IndexError, SystemExit) as e:
            print(f"   Pas compris ({e if isinstance(e, SystemExit) else 'numéro hors liste'}), recommencez.")


def _classeurs(dossier=None):
    """Renvoie les classeurs proposés par l'assistant.

    Ceux du dossier courant ; lancé depuis la racine du dépôt, ceux de ``data/quizforge`` (vos classeurs)
    et des exemples d'``outils/quizforge``.
    """
    if dossier is None:
        ici = Path(".").resolve()
        racines = ([chemins.DATA / "quizforge", chemins.OUTILS / "quizforge" / "exemples"]
                   if ici == chemins.RACINE.resolve() else [Path(".")])
    else:
        racines = [dossier]
    out = []
    for r in racines:
        if r.is_dir():
            out += [x for x in sorted(r.rglob("*.xlsx")) if not any(d.endswith("_QuizForge") for d in x.parent.parts) and not x.name.startswith("~$")
                    and len(x.relative_to(r).parts) <= 3]
    if racines != [Path(".")]:
        out = [x.relative_to(chemins.RACINE) if x.is_absolute() and x.is_relative_to(chemins.RACINE) else x for x in out]
    return out


def assistant():
    """Lance l'assistant : menu pas à pas où chaque choix se fait par un numéro.

    La commande équivalente est affichée avant d'être lancée ; Ctrl+C ou fin de saisie quitte l'assistant.
    """
    try:
        _assistant()
    except (EOFError, KeyboardInterrupt):
        print("\nAu revoir.")


def _assistant():
    """Boucle du menu de l'assistant (voir :func:`assistant`)."""
    print("QuizForge — assistant (Ctrl+C pour quitter)")
    while True:
        action = _choisir("Que voulez-vous faire ?", ["Convertir des classeurs pour Moodle", "Créer un classeur",
                          "Vérifier mes fichiers", "Réunir des fichiers dans une banque", "Réparer un classeur abîmé",
                          "Analyser les résultats d'un test (exports Moodle)",
                          "Voir les profils", "Quitter"])
        profils = list(lister_profils())
        defaut = profil_par_defaut()
        argv = []
        if action.startswith("Quitter"):
            return
        if action.startswith(("Convertir", "Réparer")):
            cls = _classeurs()
            if not cls:
                print("Aucun classeur .xlsx dans ce dossier."); continue
            choix = _choisir("Quel(s) classeur(s) ?", [str(c) for c in cls], plusieurs=action.startswith("Convertir"))
            if action.startswith("Réparer"):
                argv = ["reparer", choix]
            else:
                if not choix:
                    continue
                argv = ["convertir", *choix]
                if profils:
                    p_ = _choisir("Profil ?", profils, defaut=defaut)
                    if p_ and p_ != defaut:
                        argv += ["-p", p_]
                t = _demander("Tags pour toutes les questions (ex. MEF;S1)", "aucun")
                if t != "aucun":
                    argv += ["-t", t]
                f_ = _choisir("Formats à produire ?", ["xml", "gift", "yaml"], plusieurs=True)
                if f_:
                    argv += ["-f", ";".join(f_)]
                if _demander("Réparer les textes abîmés (plusFin) ? o/n", "n").lower().startswith("o"):
                    argv.append("-r")
        elif action.startswith("Créer"):
            vide = _choisir("Avec ou sans exemples ?", ["vide (en-têtes seulement)", "avec exemples"],
                            defaut="vide (en-têtes seulement)").startswith("vide")
            ong = _choisir("Quels onglets ?", list(MODELE), plusieurs=True)
            nom = _demander("Nom du classeur", "vide_QuizForge" if vide else "modele_QuizForge")
            argv = ["modele", "-s", nom] + (["-v"] if vide else []) + (["-o", ";".join(ong)] if ong else [])
            sortie = nom_sortie(nom, ".xlsx") if not nom.lower().endswith(".xlsx") else Path(nom)
            if sortie.exists():
                if not _demander(f"{sortie} existe déjà. Le remplacer ? o/n", "n").lower().startswith("o"):
                    continue
                argv.append("--ecraser")
        elif action.startswith("Vérifier"):
            argv = ["valider", _demander("Dossier ou fichier à vérifier", ".")]
        elif action.startswith("Réunir"):
            argv = ["importer", _demander("Dossier à réunir", "."), "-b", _demander("Nom de la banque", "banque"), "-x"]
        elif action.startswith("Voir"):
            argv = ["profils"]
        elif action.startswith("Analyser"):
            argv = ["bilan", _demander("Dossier des exports Moodle (Notes + Réponses avec texte de la question)",
                                       "data/diagforge" if (chemins.DATA / "diagforge").is_dir() else "donnees/diagforge/promotion_groupes")]
            t = _choisir("Quelles tentatives ?", ["toutes", "premiere", "derniere", "meilleure"], defaut="toutes")
            if t != "toutes":
                argv += ["-t", t]
        lanceur = Path(__file__).resolve()
        lanceur = lanceur.relative_to(Path.cwd().resolve()) if lanceur.is_relative_to(Path.cwd().resolve()) else lanceur
        print(f"\nCommande équivalente (à copier pour la prochaine fois) :\n  python {lanceur.as_posix()} "
              + " ".join(f'"{x}"' if re.search(r"[\s;&|]", x) else x for x in argv))
        if _demander("Lancer ? o/n", "o").lower().startswith("o"):
            try:
                main(argv)
            except SystemExit as e:
                if e.code not in (0, None):
                    print(f"\n{e}")
        print("\n" + "-" * 60)


def preparer_arguments(argv):
    """Prépare les arguments de la ligne de commande avec une saisie tolérante de la commande.

    « con », « -c », « C », « Convertir »… sont compris ; un fichier seul (glissé sur ``QuizForge.bat``) vaut
    ``convertir``. Sans argument, renvoie ``["--help"]``.
    """
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv:
        return ["--help"]
    premier = argv[0]
    if premier in ("-h", "--help"):
        return argv
    if premier not in COMMANDES and Path(premier).exists() and not premier.startswith("-"):
        print(f"Compris : convertir {premier}")
        return ["convertir"] + argv
    if premier.startswith("--"):
        return argv
    argv[0] = comprendre(premier.lstrip("-"), COMMANDES, "commande")
    return argv


def main(argv=None):
    """Point d'entrée : interprète les arguments (``sys.argv`` par défaut) et lance la commande demandée."""
    argv = preparer_arguments(argv)
    p = argparse.ArgumentParser(description="QuizForge : Excel / GIFT -> GIFT + Moodle XML + banque YAML. "
                                "Commandes et noms courts reconnus par leur première lettre (c = convertir).")
    sp = p.add_subparsers(dest="cmd", required=True)
    c = sp.add_parser("convertir", help="convertir un ou plusieurs classeurs / fichiers")
    c.add_argument("fichiers", nargs="+")
    c.add_argument("-p", "--profil", help="profil d'établissement (ex. Ecole1, ou D pour Delattre) ; défaut : le profil marqué defaut")
    c.add_argument("-c", "--categorie", default=None, help="racine de catégorie Moodle, ex. MMC/TP3")
    c.add_argument("-f", "--formats", help="formats à écrire, ex. xml ou x;g (défaut : ceux du profil)")
    c.add_argument("-t", "--tags", default="", help="tags ajoutés à toutes les questions, ex. \"MEF;S1\"")
    c.add_argument("-s", "--sortie", help="dossier de sortie (défaut : <fichier>_QuizForge à côté du fichier)")
    c.add_argument("-r", "--reparer", action="store_true", help="réparer les textes abîmés (plusFin → plus fin)")
    c.add_argument("-n", "--nom", default="", help="nom de catégorie à la place du nom du classeur (ex. MEF_P2026)")
    c.add_argument("-l", "--langues", default=None,
                   help="classeur bilingue : une version par langue (separe) ou une question bilingue (multilang)")
    c.add_argument("--langue-base", default=None, help="langue des colonnes sans suffixe (défaut fr)")
    c.add_argument("--seance", type=int, default=None,
                   help="écrire aussi le plan du quiz de la séance n (sections, nombre à tirer, rappels ; tirage du profil)")
    c.add_argument("--rappel", type=float, default=None, help="part des rappels dans le quiz de séance (défaut : quiz.rappel du profil)")
    c.add_argument("--etudiants", type=int, default=None, help="effectif, pour le nombre de réponses attendu par question")
    c.add_argument("--graine", type=int, default=None, help="graine du tirage des rappels (défaut : le numéro de séance)")
    c.add_argument("--cours", default=None, help="cours[:déclinaison[/édition]] : profil, catégorie, étiquettes, effectif et séances de l'édition")
    c.set_defaults(f=cmd_convertir)
    i = sp.add_parser("importer", help="reprendre des fichiers existants dans une banque unique")
    i.add_argument("fichiers", nargs="+")
    i.add_argument("-b", "--banque", default="banque.yaml", help="fichier banque (extension .yaml ajoutée si absente)")
    i.add_argument("-c", "--categorie", default=None)
    i.add_argument("-p", "--profil", help="profil d'établissement (ex. Ecole1, ou D pour Delattre)")
    i.add_argument("-t", "--tags", default="", help="tags ajoutés à toutes les questions, ex. \"MEF;S1\"")
    i.add_argument("-x", "--xml", action="store_true", help="écrire aussi la banque en Moodle XML")
    i.add_argument("-r", "--reparer", action="store_true", help="réparer les textes abîmés (plusFin → plus fin)")
    i.set_defaults(f=cmd_importer)
    r = sp.add_parser("reparer", help="écrire une copie corrigée d'un classeur abîmé par un remplacement V→T")
    r.add_argument("classeur")
    r.set_defaults(f=cmd_reparer)
    fu = sp.add_parser("fusionner", help="réunir un classeur FR et sa traduction en un classeur bilingue")
    fu.add_argument("classeur")
    fu.add_argument("traduction")
    fu.add_argument("-l", "--langue", default="en")
    fu.set_defaults(f=cmd_fusionner)
    pr = sp.add_parser("profils", help="lister les profils disponibles et afficher leurs réglages")
    pr.add_argument("nom", nargs="?")
    pr.set_defaults(f=cmd_profils)
    m = sp.add_parser("modele", help="créer le classeur modèle")
    m.add_argument("-s", "--sortie", default=None, help="nom du classeur (.xlsx ajouté si absent) ; défaut : modele_QuizForge.xlsx")
    m.add_argument("-v", "--vide", action="store_true", help="en-têtes seulement, sans exemples")
    m.add_argument("--ecraser", action="store_true", help="remplacer un classeur existant du même nom")
    m.add_argument("-o", "--onglets", default="", help="onglets à garder, ex. \"VF;Q;T\" (première lettre suffit ; défaut : tous)")
    m.set_defaults(f=cmd_modele)
    v = sp.add_parser("valider", help="vérifier classeurs, projets du pointeur et profils (sans rien écrire)")
    v.add_argument("fichiers", nargs="*", help="fichiers ou dossiers (défaut : dossier courant)")
    v.set_defaults(f=cmd_valider)
    b = sp.add_parser("bilan", help="analyser les résultats d'un test Moodle (exports Notes + Réponses) -> classeur")
    b.add_argument("cibles", nargs="+", help="dossier(s) ou fichiers des exports Moodle (.csv ou .xlsx), et l'export XML des questions")
    b.add_argument("-q", "--questions", nargs="*", help="export XML des questions (sinon : les .xml trouvés dans les dossiers)")
    b.add_argument("-t", "--tentatives", default="toutes", help="toutes (défaut : statistiques sur toutes les tentatives, notes sur la meilleure, comme Moodle) | premiere | derniere | meilleure (première lettre suffit)")
    b.add_argument("-s", "--sortie", default=None, help="classeur produit (défaut : bilan_<test>.xlsx dans le dossier des exports)")
    b.add_argument("-p", "--profil", help="profil (couleurs des en-têtes et des graphiques)")
    b.add_argument("-r", "--roster", nargs="*", help="liste des étudiants avec une colonne Groupe (sinon : groupe = suffixe du nom du test, ex. Quizz1_SMA)")
    b.add_argument("--sans-images", action="store_true", help="ne pas produire les images PNG")
    b.add_argument("--cours", default=None, help="cours[:déclinaison[/édition]] : profil de l'école de l'édition")
    b.set_defaults(f=cmd_bilan)
    asst = sp.add_parser("assistant", help="menu pas à pas (lancé par un double-clic sur QuizForge.bat)")
    asst.set_defaults(f=lambda a: assistant())
    a = p.parse_args(argv)
    a.f(a)


if __name__ == "__main__":
    main()
