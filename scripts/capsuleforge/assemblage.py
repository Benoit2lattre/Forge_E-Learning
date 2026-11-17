"""CapsuleForge — du journal d'enregistrement au fichier source de la capsule (capsule.yaml).

Partie sans dépendance à Windows : elle se teste partout. L'enregistreur (``enregistreur.py``) écrit
un journal JSON Lines (un événement par ligne) et les images ; ce module en fait les pas, les
regroupe en étapes (Ctrl+Maj+E pendant l'enregistrement) et rédige les bulles.

Format du fichier source : voir ``outils/capsuleforge/README.md`` (section « Le fichier capsule.yaml »).
Licence : GPL v3.
"""
from __future__ import annotations

import json
import math
import re
from pathlib import Path

import yaml

FORMAT = "capsuleforge/1"

# --------------------------------------------------------------------------- bulles

# type de contrôle (UI Automation, sans le suffixe « Control ») -> groupe nominal français
TYPES_CONTROLE = {
    "Button": "le bouton",
    "SplitButton": "le bouton",
    "Edit": "la zone de texte",
    "Document": "la zone de texte",
    "ComboBox": "la liste déroulante",
    "List": "la liste",
    "ListItem": "l'élément",
    "DataItem": "l'élément",
    "Tree": "l'arbre",
    "TreeItem": "l'élément",
    "Menu": "le menu",
    "MenuItem": "la commande",
    "MenuBar": "la barre de menus",
    "TabItem": "l'onglet",
    "Tab": "l'onglet",
    "CheckBox": "la case",
    "RadioButton": "l'option",
    "Hyperlink": "le lien",
    "Spinner": "le compteur",
    "Slider": "le curseur",
    "ToolBar": "la barre d'outils",
    "HeaderItem": "la colonne",
    "Header": "l'en-tête",
    "Table": "le tableau",
    "Text": "le texte",
    "Image": "l'image",
    "Pane": "la zone",
    "Window": "la fenêtre",
    "TitleBar": "la barre de titre",
    "ScrollBar": "la barre de défilement",
    "Group": "le groupe",
}

VERBES = {
    "clic": "Cliquez sur",
    "double_clic": "Double-cliquez sur",
    "clic_droit": "Cliquez avec le bouton droit sur",
    "clic_milieu": "Cliquez avec la molette sur",
}

# noms que l'accessibilité renvoie mais qui n'aident pas l'étudiant
NOMS_VIDES = {"", "desktop", "bureau", "pane", "volet", "zone", "window", "fenêtre"}


def type_court(t: str | None) -> str:
    """Renvoie le type de contrôle sans le suffixe « Control » (``ButtonControl`` -> ``Button``)."""
    t = (t or "").strip()
    return t[:-7] if t.endswith("Control") else t


def bulle_auto(action: str, cible: dict | None, texte: str | None = None, touches: str | None = None) -> str:
    """Renvoie le texte de bulle proposé à partir de l'action et de la cible.

    Le texte est en Markdown (nom du contrôle en gras) ; l'auteur le réécrit dans le YAML au besoin.
    """
    if action == "saisie":
        nom = ((cible or {}).get("nom") or "").strip()
        if nom and nom.lower() not in NOMS_VIDES and (cible or {}).get("origine") == "accessibilite":
            groupe = TYPES_CONTROLE.get(type_court((cible or {}).get("type")), "")
            return f"Tapez **{texte or ''}** dans {groupe + ' ' if groupe else ''}**{nom}**."
        return f"Tapez **{texte or ''}**."
    if action == "touche":
        return f"Appuyez sur **{touches or ''}**."
    if action == "molette":
        return "Faites tourner la molette ici."
    if action == "glisser":
        return "Faites glisser jusqu'ici."
    verbe = VERBES.get(action, "Cliquez sur")
    nom = ((cible or {}).get("nom") or "").strip()
    if len(nom) > 60:
        nom = nom[:57].rstrip() + "…"
    groupe = TYPES_CONTROLE.get(type_court((cible or {}).get("type")), "")
    if (cible or {}).get("origine") == "accessibilite" and nom.lower() in NOMS_VIDES and groupe:
        return f"{verbe} {groupe}."
    if nom.lower() in NOMS_VIDES or (cible or {}).get("origine") != "accessibilite":
        return {"clic": "Cliquez ici.", "double_clic": "Double-cliquez ici.",
                "clic_droit": "Cliquez ici avec le bouton droit.",
                "clic_milieu": "Cliquez ici avec la molette."}.get(action, "Cliquez ici.")
    groupe = TYPES_CONTROLE.get(type_court((cible or {}).get("type")), "")
    sur = verbe + " " + (groupe + " " if groupe else "")
    return f"{sur}**{nom}**."


# --------------------------------------------------------------------------- géométrie

def simplifier_trajet(points: list[list[float]], tolerance: float = 6.0, max_points: int = 40) -> list[list[int]]:
    """Allège un trajet de souris par l'algorithme de Ramer-Douglas-Peucker sur (x, y).

    ``points`` est une liste de ``[x, y, t_ms]`` ; le temps de chaque point retenu est gardé. La tolérance est
    augmentée tant qu'il reste plus de ``max_points`` points. Renvoie une liste allégée d'entiers.
    """
    pts = [p for p in points if p is not None and len(p) >= 3]
    if len(pts) <= 2:
        return [[int(round(v)) for v in p[:3]] for p in pts]

    def dist(p, a, b):
        (x, y), (x1, y1), (x2, y2) = p[:2], a[:2], b[:2]
        dx, dy = x2 - x1, y2 - y1
        if dx == dy == 0:
            return math.hypot(x - x1, y - y1)
        return abs(dy * x - dx * y + x2 * y1 - y2 * x1) / math.hypot(dx, dy)

    tol = tolerance
    out = _rdp_tol(pts, tol, dist)
    while len(out) > max_points:
        tol *= 1.6
        out = _rdp_tol(pts, tol, dist)
    return [[int(round(v)) for v in p[:3]] for p in out]


def _rdp_tol(pts, tol, dist):
    """Applique récursivement Ramer-Douglas-Peucker avec la tolérance ``tol`` et la distance ``dist``."""
    if len(pts) < 3:
        return pts
    i, dmax = 0, -1.0
    for k in range(1, len(pts) - 1):
        d = dist(pts[k], pts[0], pts[-1])
        if d > dmax:
            i, dmax = k, d
    if dmax <= tol:
        return [pts[0], pts[-1]]
    return _rdp_tol(pts[: i + 1], tol, dist)[:-1] + _rdp_tol(pts[i:], tol, dist)


def cadre_par_defaut(point, ecran, l=120, h=48):
    """Renvoie une zone de clic de secours ``[x, y, l, h]`` centrée sur le clic, gardée dans l'écran.

    Sert quand l'accessibilité n'a pas donné de cadre.
    """
    x, y = point
    L, H = ecran.get("largeur", 10**6), ecran.get("hauteur", 10**6)
    x0 = max(0, min(int(x - l / 2), L - l))
    y0 = max(0, min(int(y - h / 2), H - h))
    return [x0, y0, l, h]


def cadre_valide(cadre, point, ecran, max_part=0.6) -> bool:
    """Indique si un cadre d'accessibilité est utile : il contient le clic et ne couvre pas tout l'écran.

    ActivePresenter garde parfois le bureau entier (zone 2560 × 1600 pour « Bureau »). Le cadre est refusé si
    son aire dépasse ``max_part`` au carré de celle de l'écran.
    """
    if not cadre or len(cadre) != 4:
        return False
    x, y, l, h = cadre
    if l <= 2 or h <= 2:
        return False
    px, py = point
    if not (x - 2 <= px <= x + l + 2 and y - 2 <= py <= y + h + 2):
        return False
    L, H = ecran.get("largeur") or 1, ecran.get("hauteur") or 1
    return (l * h) / (L * H) <= max_part * max_part


# --------------------------------------------------------------------------- journal -> pas

def lire_journal(chemin: Path) -> list[dict]:
    """Lit un journal JSON Lines et renvoie la liste des événements ; les lignes illisibles sont ignorées."""
    evts = []
    for ligne in Path(chemin).read_text(encoding="utf-8").splitlines():
        ligne = ligne.strip()
        if ligne:
            try:
                evts.append(json.loads(ligne))
            except json.JSONDecodeError:
                pass          # ligne coupée par un arrêt brutal : on garde le reste
    return evts


def appliquer_modifs(evts: list[dict]) -> list[dict]:
    """Applique les événements « modif » aux pas du journal et renvoie les événements sans eux.

    Ces événements complètent un pas après coup (double-clic reconnu, cible lue plus tard).
    """
    par_id = {e["id"]: e for e in evts if e.get("e") == "pas"}
    for e in evts:
        if e.get("e") == "modif" and e.get("id") in par_id:
            par_id[e["id"]].update({k: v for k, v in e.items() if k not in ("e", "id")})
    return [e for e in evts if e.get("e") != "modif"]


def assembler(evts: list[dict], titre: str | None = None) -> dict:
    """Construit le dictionnaire de la capsule (prêt à écrire en YAML) à partir des événements du journal.

    Les pas sont regroupés en étapes, ceux faits dans un autre programme que le principal sont signalés
    (``autre_programme``), et une saisie sans cible reprend celle du clic qui l'a précédée au même endroit.

    Événements reconnus (champ ``e``) : ::

      debut   {ecran:{largeur,hauteur,echelle}, application?, date}
      pas     {id, action, image, point, trajet, cible?, texte?, touches?, t, crans?, arrivee?}
      etape   {t, titre?}         raccourci « nouvelle étape » : une nouvelle étape commence au pas suivant
      fin     {t, image?}
    """
    evts = appliquer_modifs(evts)
    entete = next((e for e in evts if e.get("e") == "debut"), {})
    ecran = entete.get("ecran") or {}
    etapes: list[dict] = []
    courante = None
    t_prec = None

    def nouvelle(titre_e=None):
        nonlocal courante
        courante = {"titre": titre_e or f"Étape {len(etapes) + 1}", "narration": "", "arret": True, "pas": []}
        etapes.append(courante)

    for e in evts:
        k = e.get("e")
        if k == "etape":
            if courante is None or courante["pas"]:
                nouvelle(e.get("titre"))
            elif e.get("titre"):
                courante["titre"] = e["titre"]
        elif k == "pas":
            if courante is None:
                nouvelle()
            p = construire_pas(e, ecran, t_prec)
            t_prec = e.get("t", t_prec)
            courante["pas"].append(p)

    etapes = [et for et in etapes if et["pas"]]
    # programme principal (le plus fréquent) : les pas faits dans un autre programme sont signalés
    from collections import Counter
    procs = Counter(p.get("processus") for et in etapes for p in et["pas"] if p.get("processus") and not p.get("ignorer"))
    principal = procs.most_common(1)[0][0] if procs else None
    for et in etapes:
        for p in et["pas"]:
            if principal and p.get("processus") and p["processus"] != principal and not p.get("ignorer"):
                p["autre_programme"] = True
    # une saisie sans cible hérite de celle du clic qui l'a précédée au même endroit (le champ cliqué)
    prec = None
    for et in etapes:
        for p in et["pas"]:
            if (p["action"] == "saisie" and p["cible"].get("origine") != "accessibilite" and prec
                    and prec["action"] in ("clic", "double_clic") and abs(prec["point"][0] - p["point"][0]) <= 8
                    and abs(prec["point"][1] - p["point"][1]) <= 8):
                p["cible"] = dict(prec["cible"])
                p["bulle"] = bulle_auto("saisie", p["cible"], p.get("texte"))
            prec = p
    fin = next((e for e in reversed(evts) if e.get("e") == "fin"), {})
    cap = {
        "format": FORMAT,
        "titre": titre or entete.get("titre") or "Capsule sans titre",
        "langue": entete.get("langue", "fr"),
        "ecran": ecran,
        "source": {k: v for k, v in {"outil": "capsuleforge enregistrer", "date": entete.get("date"),
                                      "application": entete.get("application")}.items() if v},
        "reglages": {"mode": "les_deux", "essais": 3},
        "masques": [],
        "etapes": etapes,
    }
    if fin.get("image"):
        cap["image_finale"] = fin["image"]
    return cap


def construire_pas(e: dict, ecran: dict, t_prec) -> dict:
    """Construit un pas de la capsule à partir d'un événement « pas » du journal.

    Nettoie la cible, propose la bulle, simplifie le trajet et calcule ``duree_ms`` depuis l'instant ``t_prec``
    du pas précédent ; un pas hors de l'application enregistrée est marqué ``ignorer`` avec sa ``raison``.
    """
    action = e.get("action", "clic")
    point = [int(v) for v in (e.get("point") or [0, 0])]
    p: dict = {"id": e.get("id"), "action": action, "image": e.get("image"), "point": point}
    if action == "glisser" and e.get("arrivee"):
        p["arrivee"] = [int(v) for v in e["arrivee"]]
    if action == "molette":
        p["crans"] = int(e.get("crans", 1))
    if action == "saisie":
        p["texte"] = e.get("texte", "")
    if action == "touche":
        p["touches"] = e.get("touches", "")

    brute = dict(e.get("cible") or {})
    p["cible"] = nettoyer_cible(brute, point, ecran, action)
    if action == "saisie" and p["cible"].get("origine") == "accessibilite":
        c = p["cible"]["cadre"]
        p["point"] = [c[0] + c[2] // 2, c[1] + c[3] // 2]
    if brute.get("processus"):
        p["processus"] = brute["processus"]
    raison = hors_application(action, point, brute, ecran, p.get("touches"))
    if raison:
        p = {"ignorer": True, "raison": raison, **p}

    p["bulle"] = bulle_auto(action, p["cible"], p.get("texte"), p.get("touches"))
    traj = e.get("trajet") or []
    if traj:
        t0 = traj[0][2] if len(traj[0]) > 2 else 0
        traj = [[x, y, (t - t0)] for x, y, t in (q[:3] for q in traj if len(q) >= 3)]
        p["trajet"] = simplifier_trajet(traj)
    if e.get("t") is not None and t_prec is not None:
        p["duree_ms"] = int(e["t"] - t_prec)
    return p


# types de contrôle qui contiennent la cible sans l'être (fenêtre, vue 3D, panneau) : pas de nom dans la bulle
CONTENEURS = {"Window", "Pane", "Group", "Custom", "List", "Tree", "Table", "TitleBar", "ToolBar", "MenuBar",
              "Tab", "Header", "Document"}

# fenêtres et programmes du système : un clic dedans n'appartient pas à la manipulation enregistrée
CLASSES_SYSTEME = {"Shell_TrayWnd", "Shell_SecondaryTrayWnd", "NotifyIconOverflowWindow",
                   "TopLevelWindowForOverflowXamlIsland", "Windows.UI.Core.CoreWindow", "XamlExplorerHostIslandWindow"}
PROCESSUS_SYSTEME = {"shellexperiencehost.exe", "startmenuexperiencehost.exe", "searchhost.exe", "searchapp.exe",
                     "textinputhost.exe", "lockapp.exe", "systemsettings.exe"}


def nettoyer_nom(nom: str | None) -> str:
    """Renvoie le nom d'un contrôle sans espaces insécables ni deux-points finaux."""
    nom = (nom or "").replace("\xa0", " ").replace("\u202f", " ").strip()
    while nom.endswith(":"):
        nom = nom[:-1].rstrip()
    return nom


def nettoyer_cible(cible: dict, point, ecran, action: str = "clic") -> dict:
    """Renvoie une cible utilisable à partir de celle lue par l'accessibilité.

    Le nom est nettoyé, les conteneurs et les cadres douteux sont écartés ; à défaut de cadre, une zone de
    secours est centrée sur le clic.
    """
    c = {k: cible.get(k) for k in ("nom", "type", "cadre", "origine")}
    c["nom"] = nettoyer_nom(c.get("nom"))
    cadre = c.get("cadre")
    if cadre and len(cadre) == 4 and action == "saisie":
        # champ qui avait le focus : le texte s'y tape, où que soit la souris
        point = [cadre[0] + cadre[2] // 2, cadre[1] + cadre[3] // 2]
    elif cadre and len(cadre) == 4:
        x, y, l, h = cadre
        m = max(10, h / 2)                  # flèche d'un élément d'arbre, bord d'un bouton
        dedans = x - m <= point[0] <= x + l + m and y - m <= point[1] <= y + h + m
        if not dedans:                      # lecture d'accessibilité périmée (menu refermé, survol ancien)
            c = {"origine": "aucune"}
        else:                               # le clic juste à côté (flèche d'arbre) : on élargit la zone
            x0, y0 = min(x, point[0] - 4), min(y, point[1] - 4)
            x1, y1 = max(x + l, point[0] + 4), max(y + h, point[1] + 4)
            c["cadre"] = [int(x0), int(y0), int(x1 - x0), int(y1 - y0)]
    if type_court(c.get("type")) in CONTENEURS:
        dans = c.get("nom")
        c = {"origine": "aucune"}
        if dans:
            c["dans"] = dans                # pour information : « Corps actif requis », « FreeCAD »…
    if c.get("cadre") and not cadre_valide(c["cadre"], point, ecran):
        c.pop("cadre")
    if c.get("origine") == "accessibilite" and (not c.get("nom") or c["nom"].lower() in NOMS_VIDES):
        # sans nom, le type suffit s'il est parlant (« la liste déroulante ») et la zone exacte
        if not (c.get("cadre") and type_court(c.get("type")) in TYPES_CONTROLE):
            c["origine"] = "aucune"
        c.pop("nom", None)
    if not c.get("cadre"):
        c["cadre"] = cadre_par_defaut(point, ecran)
    c["origine"] = c.get("origine") or "aucune"
    return {k: c[k] for k in ("nom", "type", "dans", "cadre", "origine") if c.get(k) not in (None, "")}


def hors_application(action, point, cible: dict, ecran: dict, touches=None) -> str | None:
    """Renvoie la raison d'écarter un pas étranger à la manipulation (barre des tâches, raccourci Windows…), ou ``None``."""
    if action == "touche" and (touches or "").startswith("Win+"):
        return f"raccourci Windows {touches}"
    if cible.get("classe") in CLASSES_SYSTEME:
        return "barre des tâches ou fenêtre du système"
    if (cible.get("processus") or "").lower() in PROCESSUS_SYSTEME:
        return f"programme du système ({cible['processus']})"
    if not cible.get("processus") and action not in ("touche", "saisie"):
        # enregistrement sans ces informations : barre des tâches en bas de l'écran (48 px à 100 %)
        bande = round(48 * (ecran.get("echelle") or 1.0)) + 2
        if ecran.get("hauteur") and point[1] >= ecran["hauteur"] - bande:
            return "barre des tâches (bas de l'écran)"
    return None


# --------------------------------------------------------------------------- écriture YAML lisible

class _Dumper(yaml.SafeDumper):
    """Écrivain YAML lisible : listes de nombres sur une ligne, textes multilignes en bloc."""
    pass


def _liste_courte(dumper, data):
    # listes de nombres (point, cadre, points du trajet) sur une ligne : le fichier reste lisible
    if all(isinstance(v, (int, float)) for v in data) and len(data) <= 4:
        return dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=True)
    if data and all(isinstance(v, list) and all(isinstance(w, (int, float)) for w in v) for v in data):
        return dumper.represent_sequence("tag:yaml.org,2002:seq", data, flow_style=True)
    return dumper.represent_sequence("tag:yaml.org,2002:seq", data)


def _texte(dumper, data):
    if "\n" in data:
        return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


_Dumper.add_representer(list, _liste_courte)
_Dumper.add_representer(str, _texte)

ENTETE_YAML = """\
# CapsuleForge — fichier source de la capsule (format {fmt}).
# À modifier à la main : titres et narration des étapes, bulles, regroupement des pas.
# Pour fusionner deux étapes, supprimer les lignes titre/narration/arret/pas de la seconde.
# Coordonnées en pixels de l'écran enregistré ; cadre = [x, y, largeur, hauteur].
# Mode d'emploi : outils/capsuleforge/README.md
"""


def ecrire_yaml(cap: dict, chemin: Path) -> None:
    """Écrit la capsule dans ``chemin`` en YAML lisible, précédée d'un en-tête de commentaires."""
    texte = yaml.dump(cap, Dumper=_Dumper, allow_unicode=True, sort_keys=False, width=110)
    Path(chemin).write_text(ENTETE_YAML.format(fmt=cap.get("format", FORMAT)) + texte, encoding="utf-8")


def lire_yaml(chemin: Path) -> dict:
    """Lit un fichier YAML et renvoie son contenu (dictionnaire vide si le fichier est vide)."""
    return yaml.safe_load(Path(chemin).read_text(encoding="utf-8")) or {}


# --------------------------------------------------------------------------- contrôle

ACTIONS = {"clic", "double_clic", "clic_droit", "clic_milieu", "glisser", "molette", "saisie", "touche",
           "montrer"}        # montrer : élément ajouté dans l'éditeur (zone signalée + bulle, sans geste)


def verifier(cap: dict, dossier: Path) -> tuple[list[str], list[str]]:
    """Contrôle une capsule et renvoie le couple (erreurs bloquantes, avertissements).

    ``dossier`` est celui de la capsule : les images et sons y sont cherchés.
    """
    err, av = [], []
    if cap.get("format") != FORMAT:
        av.append(f"format « {cap.get('format')} » (attendu {FORMAT})")
    ecran = cap.get("ecran") or {}
    if not ecran.get("largeur") or not ecran.get("hauteur"):
        err.append("ecran.largeur et ecran.hauteur sont obligatoires")
    ids = set()
    ignores: list[str] = []
    etapes = cap.get("etapes") or []
    if not etapes:
        err.append("aucune étape")
    for i, et in enumerate(etapes, 1):
        nom = f"étape {i} ({et.get('titre', '')})"
        if not et.get("pas"):
            err.append(f"{nom} : aucun pas")
            continue
        if et.get("audio") and not (dossier / et["audio"]).is_file():
            err.append(f"{nom} : audio introuvable {et['audio']}")
        for p in et["pas"]:
            pid = p.get("id") or "?"
            if pid in ids:
                err.append(f"pas {pid} : identifiant en double")
            ids.add(pid)
            if p.get("action") not in ACTIONS:
                err.append(f"pas {pid} : action inconnue « {p.get('action')} »")
            if not p.get("image"):
                err.append(f"pas {pid} : pas d'image")
            elif not (dossier / p["image"]).is_file():
                err.append(f"pas {pid} : image introuvable {p['image']}")
            if p.get("ignorer"):
                ignores.append(f"{pid} ({p.get('raison', 'à la main')})")
                continue
            if p.get("autre_programme"):
                av.append(f"pas {pid} : fait dans un autre programme ({p.get('processus')}) ; à garder ? sinon « ignorer: true »")
            if (p.get("cible") or {}).get("origine") == "aucune" and p.get("action") in VERBES \
                    and re.match(r"^(Cliquez|Double-cliquez) ici", p.get("bulle", "")):
                av.append(f"pas {pid} : bulle générique « {p.get('bulle')} » (à réécrire)")
    if ignores:
        av.append(f"{len(ignores)} pas écartés (ignorer: true), absents du lecteur : " + ", ".join(ignores))
    n = sum(1 for e in etapes for p in (e.get("pas") or []) if not p.get("ignorer"))
    if etapes and len(etapes) == 1 and n > 8:
        av.append(f"une seule étape pour {n} pas : découper avec Ctrl+Maj+E pendant l'enregistrement "
                  "ou à la main dans le YAML (une étape par idée : des étapes courtes aident à apprendre une procédure)")
    for et in etapes:
        if et.get("pas") and all(p.get("ignorer") for p in et["pas"]):
            av.append(f"étape « {et.get('titre')} » : tous ses pas sont écartés, elle n'apparaîtra pas")
        if not (et.get("narration") or "").strip() and not et.get("audio"):
            av.append(f"étape « {et.get('titre')} » sans narration")
    return err, av
