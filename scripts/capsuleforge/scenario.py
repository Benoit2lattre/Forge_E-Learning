"""CapsuleForge — scénario de lecture d'un diaporama : niveaux des dispositions, balises des notes, diagnostic.

Voir le guide « Préparer son diaporama pour CapsuleForge » (``outils/capsuleforge/DIAPORAMA.md``).

- **Niveaux des dispositions** (:func:`niveaux`) : une diapositive dont la disposition est déclarée ``chapitre``
  est la page de titre, ``partie`` ouvre une partie, ``section`` ouvre une section (quand le diaporama n'a pas de
  sections PowerPoint). Noms standard de PowerPoint par défaut, complétés par le profil de l'école puis par le
  chapitre (clé ``powerpoint: {dispositions: {nom: niveau}}``).
- **Balises des notes** (:func:`lire_notes`) : ``[clic]``, ``[pause]``, ``[pause 2 s]``, ``[note] … [/note]``,
  retirées du texte dit ; délimiteurs ``[`` ``]`` par défaut (clé ``powerpoint: {balises: ["⟦", "⟧"]}``).
- **Diagnostic** (:func:`diagnostiquer`) : degré atteint (0 brut à 5 enregistré) et ce qu'il faudrait ajouter.

Licence : GPL v3.
"""
from __future__ import annotations

import re
from pathlib import Path

import format_chapitre as F

NIVEAUX = ("chapitre", "partie", "section")
DISPOSITIONS = {"diapositive de titre": "chapitre", "title slide": "chapitre",
                "en-tête de section": "partie", "section header": "partie"}
DELIMITEURS = ("[", "]")
PAUSE_MARQUEE_S = 1.0          # [pause] sans durée
NOMS_DEGRES = ["brut", "structuré", "animé", "commenté", "balisé", "enregistré"]


# --------------------------------------------------------------------------- réglages

def _cle(nom: str) -> str:
    return " ".join(str(nom or "").lower().split())


def niveaux(profil: dict | None = None, chap: dict | None = None) -> dict:
    """Niveau de chaque disposition (nom en minuscules → ``chapitre`` | ``partie`` | ``section``)."""
    out = dict(DISPOSITIONS)
    for source in (profil, chap):
        for nom, niv in (((source or {}).get("powerpoint") or {}).get("dispositions") or {}).items():
            niv = _cle(niv)
            if niv in NIVEAUX:
                out[_cle(nom)] = niv
            elif niv in ("", "aucun", "none"):
                out.pop(_cle(nom), None)
    return out


def delimiteurs(profil: dict | None = None, chap: dict | None = None) -> tuple[str, str]:
    """Délimiteurs des balises : chapitre, sinon profil, sinon crochets."""
    for source in (chap, profil):
        d = ((source or {}).get("powerpoint") or {}).get("balises")
        if isinstance(d, (list, tuple)) and len(d) == 2 and all(isinstance(x, str) and x for x in d):
            return d[0], d[1]
    return DELIMITEURS


def profil_nomme(nom: str | None) -> dict | None:
    """Contenu du profil d'école ``nom`` (``None`` s'il n'est pas donné ou introuvable)."""
    if not nom:
        return None
    import yaml
    import habillage
    f = habillage._fichier_profil(nom)
    return (yaml.safe_load(f.read_text(encoding="utf-8")) or {}) if f else None


# --------------------------------------------------------------------------- balises des notes

def _motif(d: tuple[str, str]):
    o, f = map(re.escape, d)
    return re.compile(o + r"\s*(/?)\s*([^\s" + f + r"\d]+)\s*([^" + f + r"]*?)\s*" + f, re.I)


def a_des_balises(texte: str, d: tuple[str, str] = DELIMITEURS) -> bool:
    return bool(_motif(d).search(texte or ""))


def lire_notes(texte: str, d: tuple[str, str] = DELIMITEURS, debit_mm: float = 150.0) -> dict:
    """Lit les notes d'une diapositive et leurs balises.

    Renvoie ``{texte, phrases, clics, pauses, notes, inconnues}`` :

    - ``texte`` : le texte dit, sans balises ni notes pour l'enseignant ;
    - ``phrases`` : ses phrases (découpe de CapsuleForge) ;
    - ``clics`` : un ``(phrase, decalage_s)`` par balise ``[clic]``, dans l'ordre : la phrase où tombe la balise
      (numérotée à partir de 1) et, si elle est au milieu de la phrase, le temps estimé des mots qui précèdent ;
    - ``pauses`` : ``{phrase: secondes}``, silence après la phrase ;
    - ``notes`` : les textes ``[note] … [/note]`` ; ``inconnues`` : les balises non reconnues.
    """
    texte = texte or ""
    motif = _motif(d)
    notes, inconnues = [], []
    # notes pour l'enseignant : retirées avec leur contenu
    o, f = map(re.escape, d)
    bloc = re.compile(o + r"\s*note\s*" + f + r"(.*?)" + o + r"\s*/\s*note\s*" + f, re.I | re.S)
    texte = bloc.sub(lambda m: notes.append(" ".join(m.group(1).split())) or " ", texte)
    morceaux, evts = [], []                                # texte propre et événements (position, sorte, valeur)
    pos = 0
    for m in motif.finditer(texte):
        morceaux.append(texte[pos:m.start()])
        nom, arg = m.group(2).lower(), m.group(3).strip()
        lg = len(" ".join("".join(morceaux).split()))
        if m.group(1):
            inconnues.append(m.group(0))
        elif nom in ("clic", "click"):
            evts.append((lg, "clic", None))
        elif nom == "pause":
            v = re.search(r"\d+(?:[.,]\d+)?", arg)
            evts.append((lg, "pause", float(v.group(0).replace(",", ".")) if v else PAUSE_MARQUEE_S))
        else:
            inconnues.append(m.group(0))
        pos = m.end()
    morceaux.append(texte[pos:])
    brut = "".join(morceaux)
    propre = " ".join(brut.split())
    phrases = F.decouper_phrases(propre)
    # bornes de chaque phrase dans le texte propre
    bornes, cur = [], 0
    for p in phrases:
        i = propre.find(p, cur)
        i = cur if i < 0 else i
        bornes.append((i, i + len(p)))
        cur = i + len(p)
    clics, pauses = [], {}
    for lg, sorte, val in evts:
        if not phrases:
            if sorte == "clic":
                clics.append((None, 0.0))
            continue
        # phrase qui contient la position, ou la suivante si la balise est entre deux phrases
        k = next((j for j, (a, b) in enumerate(bornes) if lg < b), len(bornes) - 1)
        if sorte == "clic":
            a, _ = bornes[k]
            avant = len(propre[a:lg].split()) if lg > a else 0
            clics.append((k + 1, round(avant * 60 / debit_mm, 2) if avant else None))
        else:                                              # pause : après la phrase qui se termine avant la balise
            j = max([j for j, (a, b) in enumerate(bornes) if b <= lg + 1] or [0])
            pauses[j + 1] = round(pauses.get(j + 1, 0) + val, 2)
    return {"texte": propre, "phrases": phrases, "clics": clics, "pauses": pauses, "notes": notes, "inconnues": inconnues}


def accroches(n_actions: int, lu: dict, reg_decalage: float) -> tuple[list[dict], list[str]]:
    """Accroche des actions (apparitions e1…eK) aux phrases ; renvoie ``([{phrase, decalage_s?}…], remarques)``.

    Avec des balises ``[clic]`` : chaque action à la place de sa balise. Sans balise : la première action à la
    première phrase, la deuxième à la deuxième, et ainsi de suite (la dernière phrase reçoit le reste).
    """
    n_ph = len(lu["phrases"])
    if not n_ph or not n_actions:
        return [], []
    rem = []
    clics = [c for c in lu["clics"] if c[0] is not None]
    out = []
    if clics:
        if len(clics) != n_actions:
            rem.append(f"{len(clics)} balise(s) [clic] pour {n_actions} clic(s) d'animation"
                       + (" : les derniers clics suivent les phrases dans l'ordre" if len(clics) < n_actions
                          else " : les balises en trop sont ignorées"))
        for k in range(n_actions):
            if k < len(clics):
                ph, dec = clics[k]
                o = {"phrase": ph}
                if dec is not None:
                    o["decalage_s"] = round(dec + reg_decalage, 2)
            else:
                prec = out[-1]["phrase"] if out else 0
                o = {"phrase": min(prec + 1, n_ph)}
            out.append(o)
    else:
        out = [{"phrase": min(k + 1, n_ph)} for k in range(n_actions)]
    return out, rem


# --------------------------------------------------------------------------- plan et diagnostic

def structure(fichier: Path, niv: dict) -> dict:
    """Structure lue : sections PowerPoint, niveau de chaque diapositive d'après sa disposition."""
    import nouvelle
    import pptx_lire
    disp = pptx_lire.dispositions(fichier)["diapos"]
    return {"sections": nouvelle.sections_powerpoint(fichier),
            "niveaux": {n: niv.get(_cle(nom)) for n, nom in disp.items() if niv.get(_cle(nom))},
            "dispositions": disp}


def diagnostiquer(fichier: Path, profil: dict | None = None, chap: dict | None = None, lu: dict | None = None) -> dict:
    """Degré du diaporama et conseils pour monter d'un degré.

    Renvoie ``{degre, nom, criteres: {structure, animations, notes, balises, enregistrement}, details, conseils}``.
    """
    import pptx_lire
    fichier = Path(fichier)
    lu = lu or pptx_lire.lire(fichier)
    st = structure(fichier, niveaux(profil, chap))
    d = delimiteurs(profil, chap)
    contenu = [x for x in lu["diapos"] if st["niveaux"].get(x["n"]) not in ("chapitre", "partie")]
    animees = [x for x in contenu if len(x.get("etats") or []) > 1]
    commentees = [x for x in contenu if lire_notes(x.get("notes") or "", d)["texte"].strip()]
    balisees = [x for x in contenu if a_des_balises(x.get("notes") or "", d)]
    enregistrees = [x for x in lu["diapos"] if x.get("audio")]
    nom_sections = [s for s in st["sections"] if s[0].strip()]
    parties = [n for n, v in st["niveaux"].items() if v == "partie"]
    crit = {"structure": bool(nom_sections) or bool(parties),
            "animations": bool(animees),
            "notes": bool(contenu) and len(commentees) >= max(1, len(contenu) / 2),
            "balises": bool(balisees),
            "enregistrement": bool(enregistrees)}
    if crit["enregistrement"]:
        degre = 5
    elif crit["notes"] and crit["balises"]:
        degre = 4
    elif crit["notes"]:
        degre = 3
    elif crit["animations"]:
        degre = 2
    elif crit["structure"]:
        degre = 1
    else:
        degre = 0
    details = [f"{len(lu['diapos'])} diapositive(s), dont {len(contenu)} de contenu",
               f"{len(nom_sections)} section(s) PowerPoint, {len(parties)} diapositive(s) de partie",
               f"{len(animees)} diapositive(s) animée(s), {len(commentees)} commentée(s), {len(balisees)} balisée(s)"
               + (f", {len(enregistrees)} enregistrée(s)" if enregistrees else "")]
    conseils = []
    if not crit["structure"]:
        conseils.append("structurer : sections PowerPoint (une par section de la capsule) et diapositives de partie "
                        "(disposition « En-tête de section » ou déclarée dans le profil)")
    if not crit["animations"] and degre < 5:
        conseils.append("animer : un clic par élément à faire apparaître pendant le commentaire")
    if not crit["notes"] and degre < 5:
        manque = len(contenu) - len(commentees)
        conseils.append(f"commenter : écrire le texte à dire dans les notes ({manque} diapositive(s) sans notes)")
    if crit["notes"] and not crit["balises"]:
        conseils.append("baliser : [clic] dans les notes là où chaque clic doit tomber, [pause 2 s] pour laisser "
                        "le temps à une animation")
    if degre == 5 and not crit["balises"]:
        conseils.append("enregistrement sans balises : les clics sont répartis sur la durée, à caler à la relecture")
    inconnues = sorted({b for x in lu["diapos"] for b in lire_notes(x.get("notes") or "", d)["inconnues"]})
    if inconnues:
        conseils.append("balises inconnues (retirées) : " + ", ".join(inconnues[:8]))
    return {"degre": degre, "nom": NOMS_DEGRES[degre], "criteres": crit, "details": details, "conseils": conseils}


def resume_diagnostic(diag: dict) -> list[str]:
    """Lignes du diagnostic, pour le journal."""
    lignes = [f"Diagnostic : degré {diag['degre']} ({diag['nom']})" + (" — trop tôt pour une capsule : c'est le "
              "moment du plan et du squelette de leçon" if diag["degre"] < 2 else "")]
    lignes += ["  " + x for x in diag["details"]]
    lignes += ["  pour aller plus loin : " + c for c in diag["conseils"]]
    return lignes
