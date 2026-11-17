"""CapsuleForge — format capsuleforge/2 : le chapitre (cours interactif ou didacticiel).

Quatre niveaux : Chapitre > Partie (tronc, annexe, exercice) > Section (5 à 6 min au plus ; l'« étape » d'un
didacticiel) > Pas (une scène : fond, vue, objets, gestes attendus, retours).
Spécification complète : ``outils/capsuleforge/FORMAT.md``.

Ce module ne dépend que de PyYAML : conversion d'une capsule au format 1, noms dynamiques (B-S2-P4),
déroulé d'un parcours, vérification, écriture.
Licence : GPL v3.
"""
from __future__ import annotations

import re
import string
from pathlib import Path

import yaml

import assemblage as A

FORMAT = "capsuleforge/2"
FICHIER = "chapitre.yaml"

TYPES_PARTIE = ("tronc", "annexe", "exercice")
PLACES = ("debut", "libre", "fin")
TYPES_GESTE = ("clic", "double_clic", "clic_droit", "clic_milieu", "glisser", "molette", "saisie", "touche")
TYPES_OBJET = ("bulle", "texte", "formule", "cadre", "spot", "fleche", "pointeur", "image", "video", "bouton",
               "apparition", "cache")
MODES = ("regarder", "a_vous")
ANNEXES = ("aucune", "a_la_demande", "integrees")
QUESTIONS = ("aucune", "proposees", "obligatoires")
MOTS_PAR_MINUTE = 150
DUREE_MAX_SECTION_S = 360

ORDRE_CHAPITRE = ["format", "titre", "langues", "ecran", "vue", "source", "reglages", "masques", "parcours",
                  "variantes", "parties", "image_finale"]
ORDRE_PARTIE = ["id", "titre", "type", "place", "prerequis", "parcours", "variantes", "exercice", "sections"]
ORDRE_SECTION = ["id", "titre", "objectif", "source", "narration", "audio", "arret", "ouverture", "questions",
                 "annexes", "pas"]
ORDRE_PAS = ["ecarte", "raison", "id", "fond", "video", "camera", "vue", "source", "narration", "phrases", "audio", "duree_s", "voix", "objets", "gestes",
             "a_vous", "retours"]
ORDRE_GESTE = ["type", "zone", "point", "arrivee", "crans", "texte", "accepte", "tolerance", "touches", "cible",
               "trajectoire", "trajet"]
ORDRE_OBJET = ["id", "type", "forme", "texte", "position", "cadre", "ouvre", "trajet", "fichier", "couleur", "debut_s", "duree_s", "origine", "modes",
               "parcours"]


def _ordonner(d: dict, ordre: list[str]) -> dict:
    """Renvoie une copie de ``d`` dont les clés suivent ``ordre`` (les autres clés à la suite)."""
    return {**{k: d[k] for k in ordre if k in d}, **{k: v for k, v in d.items() if k not in ordre}}


def texte(valeur, langue: str | None = None) -> str:
    """Renvoie un texte dans la langue demandée.

    Un texte est une chaîne (langue source) ou un dictionnaire par langue ``{fr: …, en: …}`` ; si la langue
    manque, la première valeur non vide est renvoyée.
    """
    if isinstance(valeur, dict):
        return valeur.get(langue) or next((v for v in valeur.values() if v), "") if valeur else ""
    return valeur or ""


FIN_DE_PHRASE = re.compile(r"(?<=[.!?…])\s+(?=[A-ZÀ-ÖØ-Þ«\"])")


def decouper_phrases(texte: str) -> list[str]:
    """Découpe un texte en phrases : seule règle de CapsuleForge (relecture, transcription, voix de synthèse).

    Coupure après « . ! ? … » suivis d'un espace puis d'une majuscule ou d'un guillemet ; un chiffre ne commence
    pas une phrase (« fig. 2 », « p. 12 » restent entiers). Les espaces sont normalisés ; le gras ``**…**`` est
    gardé (il est affiché, pas prononcé : la voix de synthèse le retire au moment de dire la phrase).
    """
    morceaux = FIN_DE_PHRASE.split(" ".join(str(texte or "").split()))
    return [m for m in morceaux if m.strip()]


# --------------------------------------------------------------------------- conversion du format 1

def narration_pas(pas: dict, langue: str | None = None) -> str:
    """Renvoie le texte dit pendant un pas : ses phrases horodatées mises bout à bout, sinon son champ ``narration``."""
    if pas.get("phrases"):
        return " ".join(texte(ph.get("texte"), langue).strip() for ph in pas["phrases"]).strip()
    return texte(pas.get("narration"), langue)


def convertir_v1(cap: dict, nom_fichier: str = "capsule.yaml") -> dict:
    """Convertit une capsule au format 1 (étapes, pas à action unique) en chapitre au format 2, sans perte.

    Une seule partie « tronc » ; chaque étape devient une section ; chaque pas devient une scène :
    la bulle devient un objet, l'action devient le premier geste attendu, les variantes (``ou``) les suivants.
    """
    reg = dict(cap.get("reglages") or {})
    mode = reg.pop("mode", "les_deux")
    reglages = {"modes": {"les_deux": ["regarder", "a_vous"], "demonstration": ["regarder"],
                          "pratique": ["a_vous"]}.get(mode, ["regarder", "a_vous"]),
                "essais": reg.pop("essais", 3),
                "retours": {"juste": "Oui.", "faux": "Pas tout à fait.", "indice_apres": "essais"}}
    reglages.update(reg)                                   # trajectoire, etc.
    source = dict(cap.get("source") or {})
    source["conversion"] = nom_fichier
    sections = []
    for i, et in enumerate(cap.get("etapes") or [], 1):
        s = {"id": f"s{i:02d}", "titre": et.get("titre") or f"Étape {i}", "narration": et.get("narration") or "",
             "arret": et.get("arret", True), "pas": [_pas_v1(p) for p in et.get("pas") or []]}
        if et.get("audio"):
            s["audio"] = et["audio"]
        sections.append(_ordonner(s, ORDRE_SECTION))
    langue = cap.get("langue") or "fr"
    chap = {"format": FORMAT, "titre": cap.get("titre") or "Sans titre", "langues": {"source": langue},
            "ecran": cap.get("ecran") or {}, "source": source, "reglages": reglages,
            "masques": cap.get("masques") or [],
            "parcours": [{"id": "complet", "titre": "Parcours complet", "annexes": "integrees",
                          "questions": "proposees"}],
            "parties": [{"id": "principale", "titre": cap.get("titre") or "Sans titre", "type": "tronc",
                         "place": "libre", "sections": sections}]}
    if cap.get("image_finale"):
        chap["image_finale"] = cap["image_finale"]
    return _ordonner(chap, ORDRE_CHAPITRE)


def _pas_v1(p: dict) -> dict:
    """Convertit un pas du format 1 en pas (scène) du format 2."""
    cible = dict(p.get("cible") or {})
    zone = cible.pop("cadre", None)
    action = p.get("action", "clic")
    q: dict = {"id": p.get("id"), "fond": p.get("image")}
    if p.get("ignorer"):
        q["ecarte"] = True
        if p.get("raison"):
            q["raison"] = p["raison"]
    src = {k: p[k] for k in ("duree_ms", "processus", "autre_programme") if p.get(k)}
    src["type"] = "ajout" if str(p.get("id", "")).startswith("a") else "captation"
    q["source"] = src
    if p.get("lecture_s"):
        q["duree_s"] = p["lecture_s"]

    objets = []
    if p.get("bulle"):
        o = {"id": "bulle", "type": "bulle", "texte": p["bulle"]}
        if p.get("bulle_position"):
            o["position"] = p["bulle_position"]
        objets.append(o)
    if action == "montrer":
        if zone:
            objets.append({"id": "cadre", "type": "cadre", "cadre": zone})
    else:
        g = {"type": action}
        if zone and action != "touche":
            g["zone"] = zone
        if action != "touche":
            g["point"] = p.get("point")
        for k in ("arrivee", "crans", "texte", "accepte", "tolerance", "touches", "trajectoire", "trajet"):
            if p.get(k) not in (None, "", []):
                g[k] = p[k]
        if cible:
            g["cible"] = cible
        gestes = [_ordonner(g, ORDRE_GESTE)]
        for v in p.get("ou") or []:
            h = {"type": v.get("action", "clic")}
            if v.get("cadre"):
                h["zone"] = v["cadre"]
            if v.get("touches"):
                h["touches"] = v["touches"]
            gestes.append(_ordonner(h, ORDRE_GESTE))
        q["gestes"] = gestes
    if objets:
        q["objets"] = [_ordonner(o, ORDRE_OBJET) for o in objets]
    av = {k: p[k] for k in ("observer", "indice") if p.get(k) is not None}
    if av:
        q["a_vous"] = av
    ret = {a: p[b] for a, b in (("juste", "retour_juste"), ("faux", "retour_faux")) if p.get(b)}
    if ret:
        q["retours"] = ret
    return _ordonner(q, ORDRE_PAS)


# --------------------------------------------------------------------------- noms dynamiques

def lettre(i: int) -> str:
    """Renvoie la lettre de rang ``i`` (compté à partir de 0) : 0 → A, 25 → Z, 26 → AA."""
    s = ""
    i += 1
    while i:
        i, r = divmod(i - 1, 26)
        s = string.ascii_uppercase[r] + s
    return s


def noms(chap: dict) -> dict:
    """Renvoie les noms dynamiques : partie « B », section « B-S2 », pas « B-S2-P4 ».

    Un pas écarté prend une décimale (B-S2-P4.1). Clés du dictionnaire : ``("partie", id)``,
    ``("section", id partie, id section)``, ``("pas", id du pas)``.
    """
    out = {}
    for ip, partie in enumerate(chap.get("parties") or []):
        L = lettre(ip)
        out[("partie", partie.get("id"))] = L
        for js, sec in enumerate(partie.get("sections") or [], 1):
            out[("section", partie.get("id"), sec.get("id"))] = f"{L}-S{js}"
            n = k = 0
            for p in sec.get("pas") or []:
                if p.get("ecarte"):
                    k += 1
                    out[("pas", p.get("id"))] = f"{L}-S{js}-P{n}.{k}"
                else:
                    n, k = n + 1, 0
                    out[("pas", p.get("id"))] = f"{L}-S{js}-P{n}"
    return out


# --------------------------------------------------------------------------- durées, parcours

def duree_pas_s(p: dict, depuis, largeur: float) -> tuple[float, list | None]:
    """Renvoie la durée d'un pas en mode « regarder » et la position du curseur à la sortie.

    Même calcul que le lecteur (``tempsPas``) : déplacement de 0,45 à 1,5 s selon la distance, geste,
    lecture de la bulle de 1,8 à 5 s. ``depuis`` : position du curseur à l'entrée (ou ``None``).
    """
    g = (p.get("gestes") or [None])[0]
    bulle = next((o for o in p.get("objets") or [] if o.get("type") == "bulle"), None)
    lettres = len((bulle or {}).get("texte", "").replace("**", "")) if bulle else 0
    t_bulle = min(5.0, max(1.8, 0.9 + 0.045 * lettres)) if bulle else 0.6
    if p.get("duree_s"):
        fin = (g.get("arrivee") or g.get("point")) if g and g.get("type") not in ("touche", "saisie") else depuis
        return float(p["duree_s"]), fin or depuis
    if not g or g.get("type") in ("touche", "saisie"):
        geste = (0.09 * len(g.get("texte") or "") + 0.7) if g and g.get("type") == "saisie" else 0.0
        return geste + t_bulle, depuis or (g or {}).get("point")
    pt = g.get("point") or [0, 0]
    d = ((pt[0] - depuis[0]) ** 2 + (pt[1] - depuis[1]) ** 2) ** 0.5 if depuis else 0.0
    trajet = min(1.5, max(0.45, 0.35 + 1.3 * d / max(1.0, largeur)))
    geste = {"glisser": 0.9, "molette": 0.0, "double_clic": 0.41}.get(g.get("type"), 0.25)
    return trajet + geste + t_bulle, g.get("arrivee") or pt


def duree_section_s(sec: dict, langue: str | None = None, largeur: float = 1920) -> float | None:
    """Renvoie la durée estimée d'une section en secondes (``None`` si rien ne l'indique).

    C'est celle de la source si elle est connue (diaporama minuté) ; sinon la plus longue de la narration
    (150 mots/min, section et pas) et de la somme des pas.
    """
    src = sec.get("source") or {}
    if src.get("duree_s"):
        return float(src["duree_s"])
    actifs = [p for p in sec.get("pas") or [] if not p.get("ecarte")]
    mots = len(texte(sec.get("narration"), langue).split()) + sum(len(narration_pas(p, langue).split()) for p in actifs)
    total, pos = 0.0, None
    for p in actifs:
        d, pos = duree_pas_s(p, pos, largeur)
        total += d
    return max(mots * 60 / MOTS_PAR_MINUTE, total) or None


def _retenue(element: dict, parcours: str | None, variante: str | None) -> bool:
    """Indique si une partie est retenue pour ce parcours et cette variante."""
    if parcours and element.get("parcours") and parcours not in element["parcours"]:
        return False
    if variante and element.get("variantes") and variante not in element["variantes"]:
        return False
    return True


def derouler(chap: dict, parcours: str | None = None, variante: str | None = None) -> dict:
    """Renvoie ce qu'un étudiant voit sur un parcours.

    Le tronc est rangé dans l'ordre (début, parties libres, fin), les annexes suivent le réglage du parcours.
    Renvoie ``{"tronc": [parties], "annexes": [parties appelables], "regles": parcours}``.
    """
    regles = next((p for p in chap.get("parcours") or [] if p.get("id") == parcours), None) \
        or {"id": None, "annexes": "a_la_demande", "questions": "proposees"}
    parties = [p for p in chap.get("parties") or [] if _retenue(p, parcours, variante)]
    tronc = [p for p in parties if p.get("type", "tronc") == "tronc"]
    ordre = {"debut": 0, "libre": 1, "fin": 2}
    tronc.sort(key=lambda p: ordre.get(p.get("place", "libre"), 1))      # tri stable : l'ordre du fichier est gardé
    annexes = [] if regles.get("annexes") == "aucune" else [p for p in parties if p.get("type") in ("annexe", "exercice")]
    return {"tronc": tronc, "annexes": annexes, "regles": regles}


def plan(chap: dict, parcours: str | None = None, variante: str | None = None) -> list[str]:
    """Renvoie les lignes du plan lisible d'un parcours, avec noms et durées (commande « capsuleforge plan »)."""
    N = noms(chap)
    d = derouler(chap, parcours, variante)
    par_id = {p.get("id"): p for p in chap.get("parties") or []}
    visibles = {p.get("id") for p in d["annexes"]}
    integrees = d["regles"].get("annexes") == "integrees"
    lignes, total, vues = [], 0.0, set()

    def ecrire_partie(p, retrait=""):
        nonlocal total
        etiquette = {"annexe": " (annexe)", "exercice": " (exercice)"}.get(p.get("type"), "")
        place = {"debut": " [ouvre le chapitre]", "fin": " [ferme le chapitre]"}.get(p.get("place"), "")
        lignes.append(f"{retrait}{N[('partie', p.get('id'))]}  {texte(p.get('titre'))}{etiquette}{place}")
        for s in p.get("sections") or []:
            ds = duree_section_s(s, largeur=(chap.get('ecran') or {}).get('largeur') or 1920)
            total += ds or 0
            n_pas = sum(1 for q in s.get("pas") or [] if not q.get("ecarte"))
            lignes.append(f"{retrait}  {N[('section', p.get('id'), s.get('id'))]:<7} {texte(s.get('titre'))}"
                          f"  ({_minsec(ds)}, {n_pas} pas, {len(s.get('questions') or [])} question(s))")
            for a in s.get("annexes") or []:
                if a not in visibles:
                    continue
                if integrees and a not in vues:
                    vues.add(a)
                    ecrire_partie(par_id[a], retrait + "      ↳ ")
                else:
                    lignes.append(f"{retrait}      ↳ annexe à la demande : {N[('partie', a)]}  {texte(par_id[a].get('titre'))}")

    for p in d["tronc"]:
        ecrire_partie(p)
    for p in d["annexes"]:
        if integrees and p.get("id") not in vues:
            lignes.append(f"(annexe jamais appelée : {N[('partie', p.get('id'))]} {texte(p.get('titre'))})")
    lignes.append(f"Total estimé : {_minsec(total)}")
    return lignes


def _minsec(s: float | None) -> str:
    """Écrit une durée en minutes et secondes (« durée inconnue » si elle est nulle ou absente)."""
    if not s:
        return "durée inconnue"
    return f"{int(s // 60)} min {int(round(s % 60)):02d}"


# --------------------------------------------------------------------------- vérification

def verifier(chap: dict, dossier: Path) -> tuple[list[str], list[str]]:
    """Vérifie un chapitre au format 2 et renvoie ``(erreurs bloquantes, avertissements)``.

    ``dossier`` : dossier du chapitre, où sont cherchés les fichiers cités (fonds, sons, vidéos).
    """
    err, av = [], []
    dossier = Path(dossier)
    if chap.get("format") != FORMAT:
        err.append(f"format « {chap.get('format')} » (attendu {FORMAT})")
    ecran = chap.get("ecran") or {}
    if not ecran.get("largeur") or not ecran.get("hauteur"):
        err.append("ecran.largeur et ecran.hauteur sont obligatoires")
    N = noms(chap)
    parties = chap.get("parties") or []
    if not parties:
        err.append("aucune partie")
    ids_parcours = {p.get("id") for p in chap.get("parcours") or []}
    ids_variantes = {v.get("id") for v in chap.get("variantes") or []}
    for p in chap.get("parcours") or []:
        if p.get("annexes", "a_la_demande") not in ANNEXES:
            err.append(f"parcours {p.get('id')} : annexes « {p.get('annexes')} » (attendu {', '.join(ANNEXES)})")
        if p.get("questions", "proposees") not in QUESTIONS:
            err.append(f"parcours {p.get('id')} : questions « {p.get('questions')} » (attendu {', '.join(QUESTIONS)})")
    ids_parties, ids_pas = {}, set()
    for p in parties:
        if p.get("id") in ids_parties:
            err.append(f"partie « {p.get('id')} » : identifiant en double")
        ids_parties[p.get("id")] = p
    appelees: set = set()
    squelette = (chap.get("source") or {}).get("statut") == "squelette"
    for p in parties:
        nom_p = f"partie {N[('partie', p.get('id'))]} ({texte(p.get('titre'))})"
        if p.get("type", "tronc") not in TYPES_PARTIE:
            err.append(f"{nom_p} : type « {p.get('type')} » (attendu {', '.join(TYPES_PARTIE)})")
        if p.get("place", "libre") not in PLACES:
            err.append(f"{nom_p} : place « {p.get('place')} » (attendu {', '.join(PLACES)})")
        for r in p.get("prerequis") or []:
            if r not in ids_parties:
                err.append(f"{nom_p} : prérequis inconnu « {r} »")
        for r in p.get("parcours") or []:
            if r not in ids_parcours:
                err.append(f"{nom_p} : parcours inconnu « {r} »")
        for r in p.get("variantes") or []:
            if r not in ids_variantes:
                err.append(f"{nom_p} : variante inconnue « {r} »")
        if not p.get("sections") and p.get("type", "tronc") != "exercice":
            err.append(f"{nom_p} : aucune section")
        ids_sec = set()
        for s in p.get("sections") or []:
            nom_s = f"{N[('section', p.get('id'), s.get('id'))]} ({texte(s.get('titre'))})"
            if s.get("id") in ids_sec:
                err.append(f"{nom_s} : identifiant de section en double dans la partie")
            ids_sec.add(s.get("id"))
            for a in s.get("annexes") or []:
                if a not in ids_parties or ids_parties[a].get("type") not in ("annexe", "exercice"):
                    err.append(f"{nom_s} : annexe inconnue « {a} »")
                appelees.add(a)
            actifs = [q for q in s.get("pas") or [] if not q.get("ecarte")]
            if not actifs:
                (av if squelette else err).append(f"{nom_s} : aucun pas")
            d = duree_section_s(s, largeur=ecran.get('largeur') or 1920)
            if d and d > DUREE_MAX_SECTION_S + 5:
                av.append(f"{nom_s} : {_minsec(d)}, plus de 6 min (à couper)")
            if s.get("audio") and not (dossier / s["audio"]).is_file():
                err.append(f"{nom_s} : audio introuvable {s['audio']}")
            for q in s.get("pas") or []:
                _verifier_pas(q, N, dossier, ids_pas, ids_parties, appelees, err, av)
    for p in parties:
        if p.get("type") in ("annexe", "exercice") and p.get("id") not in appelees:
            av.append(f"partie {N[('partie', p.get('id'))]} ({texte(p.get('titre'))}) : annexe appelée nulle part")
    if sum(1 for p in parties if p.get("place") == "debut") > 1:
        av.append("plusieurs parties ont place: debut")
    return err, av


def _verifier_pas(q, N, dossier, ids_pas, ids_parties, appelees, err, av):
    """Vérifie un pas ; ajoute erreurs et avertissements à ``err`` et ``av``, les annexes ouvertes à ``appelees``."""
    nom = f"{N.get(('pas', q.get('id')), '?')} ({q.get('id')})"
    if q.get("id") in ids_pas:
        err.append(f"pas {q.get('id')} : identifiant en double dans le chapitre")
    ids_pas.add(q.get("id"))
    if q.get("ecarte"):
        return
    if not q.get("fond"):
        err.append(f"{nom} : pas de fond")
    elif not (dossier / q["fond"]).is_file():
        err.append(f"{nom} : fond introuvable {q['fond']}")
    for g in q.get("gestes") or []:
        t = g.get("type")
        if t not in TYPES_GESTE:
            err.append(f"{nom} : geste inconnu « {t} »")
        elif t == "touche" and not g.get("touches"):
            err.append(f"{nom} : geste « touche » sans touches")
        elif t == "saisie" and g.get("texte") in (None, ""):
            av.append(f"{nom} : saisie sans texte attendu")
        elif t not in ("touche",) and not g.get("zone"):
            err.append(f"{nom} : geste « {t} » sans zone")
    if q.get("audio") and not (dossier / q["audio"]).is_file():
        err.append(f"{nom} : audio introuvable {q['audio']}")
    cam = q.get("camera")
    if cam and (not cam.get("fichier") or not (dossier / cam["fichier"]).is_file()):
        err.append(f"{nom} : vidéo de la caméra introuvable {cam.get('fichier')}")
    v = q.get("video")
    if v:
        if not v.get("fichier") or not (dossier / v["fichier"]).is_file():
            err.append(f"{nom} : vidéo introuvable {v.get('fichier')}")
        elif v.get("debut_s") is None or v.get("fin_s") is None or v["fin_s"] <= v["debut_s"]:
            err.append(f"{nom} : vidéo sans début ni fin valables (debut_s, fin_s)")
    avant = None
    for i, ph in enumerate(q.get("phrases") or [], 1):
        d, f = ph.get("debut_s"), ph.get("fin_s")
        if d is None:
            continue
        if (f is not None and f < d) or (avant is not None and d < avant):
            av.append(f"{nom} : phrase {i} mal placée dans le temps ({d} s)")
        if q.get("duree_s") and d > q["duree_s"] + 0.5:
            av.append(f"{nom} : phrase {i} après la fin du pas ({d} s)")
        avant = d
    for o in q.get("objets") or []:
        if o.get("fichier") and not (dossier / o["fichier"]).is_file():
            err.append(f"{nom} : fichier introuvable {o['fichier']} (objet {o.get('id')})")
        if o.get("type") not in TYPES_OBJET:
            err.append(f"{nom} : objet de type inconnu « {o.get('type')} »")
        if o.get("type") == "bouton" and o.get("ouvre"):
            if o["ouvre"] not in ids_parties:
                err.append(f"{nom} : le bouton ouvre une partie inconnue « {o['ouvre']} »")
            appelees.add(o["ouvre"])
        for m in o.get("modes") or []:
            if m not in MODES:
                err.append(f"{nom} : mode inconnu « {m} » sur un objet")
    bulle = next((o for o in q.get("objets") or [] if o.get("type") == "bulle"), None)
    g0 = (q.get("gestes") or [None])[0]
    if g0 and g0.get("type") in A.VERBES and (g0.get("cible") or {}).get("origine") == "aucune" \
            and re.match(r"^(Cliquez|Double-cliquez) ici", (bulle or {}).get("texte", "")):
        av.append(f"{nom} : bulle générique à réécrire")


# --------------------------------------------------------------------------- lecture, écriture

ENTETE = """\
# CapsuleForge — chapitre (format {fmt}).
# Chapitre > Partie > Section (5 à 6 min au plus) > Pas (une scène : fond, objets, gestes, retours).
# Coordonnées en pixels de l'écran enregistré ; zone et cadre = [x, y, largeur, hauteur].
# Description du format : outils/capsuleforge/FORMAT.md
"""
ENTETE_CONVERSION = """\
# Fichier produit par « capsuleforge convertir » à partir de {src} : tant que l'éditeur lit {src},
# c'est {src} qui fait foi et ce fichier se refait par la même commande.
"""


def _simple(v):
    """Convertit les nombres NumPy (transcription, son) en types Python : le YAML ne sait écrire que ceux-ci."""
    if isinstance(v, dict):
        return {k: _simple(x) for k, x in v.items()}
    if isinstance(v, (list, tuple)):
        return [_simple(x) for x in v]
    if type(v).__module__ == "numpy":
        return v.item() if hasattr(v, "item") else v.tolist()
    return v


def ecrire(chap: dict, chemin: Path) -> None:
    """Écrit le chapitre en YAML dans ``chemin``, précédé d'un en-tête de commentaires."""
    chap = _simple(chap)
    corps = yaml.dump(chap, Dumper=A._Dumper, allow_unicode=True, sort_keys=False, width=110)
    tete = ENTETE.format(fmt=chap.get("format", FORMAT))
    src = (chap.get("source") or {}).get("conversion")
    if src:
        tete += ENTETE_CONVERSION.format(src=src)
    Path(chemin).write_text(tete + corps, encoding="utf-8")


def lire(chemin: Path) -> dict:
    """Lit un chapitre YAML et le renvoie (dictionnaire vide si le fichier est vide)."""
    return yaml.safe_load(Path(chemin).read_text(encoding="utf-8")) or {}
