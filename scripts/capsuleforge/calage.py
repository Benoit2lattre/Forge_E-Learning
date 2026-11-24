"""CapsuleForge — calage des objets d'un pas sur ses phrases.

Un objet (apparition, spot, cadre, pointeur…) peut être accroché à une phrase du texte dit au lieu d'un instant
fixe ::

    objets:
      - id: e2
        type: apparition
        phrase: 3            # numéro de la phrase (à partir de 1)
        ancre: debut         # debut (par défaut) ou fin de la phrase
        decalage_s: -0.4     # facultatif : réglage par défaut du chapitre sinon
        debut_s: 6.5         # recalculé d'après la phrase ; gardé pour les outils qui le lisent

Son instant suit alors la phrase : une nouvelle voix, une phrase coupée ou une pause ajoutée le déplacent sans
rien retoucher. Un objet sans ``phrase`` garde son ``debut_s``. Sans voix, les instants des phrases sont estimés
d'après le débit de la langue. Une phrase peut porter ``pause_s`` : le silence à laisser après elle.

Réglages par défaut, modifiables dans la clé ``calage`` du chapitre ::

    calage:
      decalage_s: -0.4       # l'objet apparaît juste avant d'être nommé
      pause_s: 0.4           # silence après chaque phrase
      debit_mots_min: {fr: 150, en: 160}

Licence : GPL v3.
"""
from __future__ import annotations

import format_chapitre as F

DEFAUTS = {"ancre": "debut", "decalage_s": -0.4, "pause_s": 0.4, "avant_s": 0.5}
DEBITS = {"fr": 150, "en": 160, "es": 160, "it": 150, "de": 130, "pt": 150}
ANCRES = ("debut", "fin")
CLES = ("phrase", "ancre", "decalage_s")


def reglages(chap: dict) -> dict:
    """Réglages de calage du chapitre, complétés par les valeurs par défaut."""
    r = dict(DEFAUTS)
    r.update({k: v for k, v in (chap.get("calage") or {}).items() if v is not None})
    return r


def debit(chap: dict, langue: str | None = None) -> float:
    """Débit (mots par minute) de la langue : chapitre, sinon table par défaut, sinon ``MOTS_PAR_MINUTE``."""
    langue = langue or (chap.get("langues") or {}).get("source") or "fr"
    d = (chap.get("calage") or {}).get("debit_mots_min")
    if isinstance(d, dict) and d.get(langue):
        return float(d[langue])
    if isinstance(d, (int, float)) and d > 0:
        return float(d)
    return float(DEBITS.get(langue, F.MOTS_PAR_MINUTE))


def mots(texte: str) -> int:
    return len(texte.replace("**", "").split())


def estimer(textes: list[str], pauses: list[float | None], debit_mm: float, reg: dict) -> list[list[float]]:
    """Instants estimés ``[[début, fin], …]`` de phrases dites au débit donné, avec leurs pauses."""
    t, out = float(reg["avant_s"]), []
    for k, x in enumerate(textes):
        d = max(0.8, mots(x) * 60 / debit_mm)
        out.append([round(t, 2), round(t + d, 2)])
        p = pauses[k] if k < len(pauses) and pauses[k] is not None else reg["pause_s"]
        t += d + float(p)
    return out


def temps(pas: dict, chap: dict, langue: str | None = None) -> list[list[float]]:
    """Instants des phrases du pas dans la langue : ceux de la voix s'il y en a une complète, sinon estimés."""
    src = (chap.get("langues") or {}).get("source") or "fr"
    langue = langue or src
    phrases = pas.get("phrases") or []
    if not phrases:
        return []
    if langue == src:
        if all(ph.get("debut_s") is not None and ph.get("fin_s") is not None for ph in phrases):
            return [[float(ph["debut_s"]), float(ph["fin_s"])] for ph in phrases]
    else:
        v = (pas.get("voix") or {}).get(langue) or {}
        if len(v.get("phrases") or []) == len(phrases):
            return [[float(a), float(b)] for a, b in v["phrases"]]
    textes = [F.texte(ph.get("texte"), langue) for ph in phrases]
    return estimer(textes, [ph.get("pause_s") for ph in phrases], debit(chap, langue), reglages(chap))


def instant(objet: dict, t: list[list[float]], reg: dict) -> float | None:
    """Instant d'un objet accroché (``None`` s'il ne l'est pas ou si le pas n'a pas de phrase)."""
    if objet.get("phrase") is None or not t:
        return None
    k = min(max(int(objet["phrase"]) - 1, 0), len(t) - 1)
    base = t[k][1] if objet.get("ancre", reg["ancre"]) == "fin" else t[k][0]
    dec = objet.get("decalage_s")
    return round(max(0.0, base + float(reg["decalage_s"] if dec is None else dec)), 2)


def decalage(objet: dict, t_objet: float, t: list[list[float]], reg: dict) -> None:
    """Règle ``decalage_s`` d'un objet accroché pour qu'il tombe à ``t_objet`` (« Poser à cet instant »)."""
    k = min(max(int(objet["phrase"]) - 1, 0), len(t) - 1)
    base = t[k][1] if objet.get("ancre", reg["ancre"]) == "fin" else t[k][0]
    d = round(float(t_objet) - base, 2)
    if abs(d - float(reg["decalage_s"])) < 0.005:
        objet.pop("decalage_s", None)
    else:
        objet["decalage_s"] = d


PROCHE_S = 1.0     # un objet à moins d'une seconde avant une phrase l'annonce ; plus tôt, il illustre la phrase en cours


def accrocher_objet(objet: dict, t_objet: float, t: list[list[float]], reg: dict) -> None:
    """Accroche un objet à une phrase, en gardant son instant ``t_objet``.

    La phrase choisie est celle qui commence dans la seconde qui suit l'objet (il l'annonce) ; sinon celle qui est
    en cours à cet instant (il l'illustre) ; avant la première phrase, la première.
    """
    suiv = next((i for i, (a, _) in enumerate(t) if a + 1e-6 >= t_objet), None)
    if suiv is not None and t[suiv][0] - t_objet <= PROCHE_S:
        k = suiv
    else:
        k = max([i for i, (a, _) in enumerate(t) if a <= t_objet] or [0])
    objet["phrase"] = k + 1
    objet.pop("ancre", None)
    decalage(objet, t_objet, t, reg)


def appliquer_pas(pas: dict, chap: dict) -> int:
    """Recalcule ``debut_s`` des objets accrochés du pas (langue source) ; renvoie le nombre d'instants changés."""
    reg, t, n = reglages(chap), None, 0
    for o in pas.get("objets") or []:
        if o.get("phrase") is None:
            continue
        t = t if t is not None else temps(pas, chap)
        v = instant(o, t, reg)
        if v is not None and o.get("debut_s") != v:
            o["debut_s"] = v
            n += 1
    return n


def appliquer(chap: dict) -> int:
    """Recalcule les instants des objets accrochés de tout le chapitre ; renvoie le nombre d'instants changés."""
    return sum(appliquer_pas(q, chap) for p in chap.get("parties") or [] for s in p.get("sections") or []
               for q in s.get("pas") or [])


def instants_langue(pas: dict, chap: dict, langue: str) -> dict:
    """``{id: instant}`` des objets accrochés du pas, dans une langue (instants de sa voix ou estimés)."""
    reg, t = reglages(chap), temps(pas, chap, langue)
    return {o.get("id"): instant(o, t, reg) for o in pas.get("objets") or [] if o.get("phrase") is not None}


def accrocher_pas(pas: dict, chap: dict, remplacer: bool = False) -> int:
    """Accroche aux phrases les objets du pas qui ont un instant ; renvoie le nombre d'objets accrochés.

    Chaque objet est rattaché à la phrase qu'il annonce ou qu'il illustre (voir :func:`accrocher_objet`), avec le
    décalage observé. Il faut des
    instants de phrases (voix ou transcription) : sans eux, rien n'est fait. ``remplacer`` refait aussi les accroches
    existantes.
    """
    phrases = pas.get("phrases") or []
    if not phrases or not all(ph.get("debut_s") is not None for ph in phrases):
        return 0
    reg, t, n = reglages(chap), temps(pas, chap), 0
    for o in pas.get("objets") or []:
        if o.get("debut_s") is None or o.get("type") == "cache" or (o.get("phrase") is not None and not remplacer):
            continue
        accrocher_objet(o, float(o["debut_s"]), t, reg)
        n += 1
    return n


def _mots(texte) -> list[str]:
    return [m for m in (w.strip(".,;:!?…«»\"'()").lower() for w in F.texte(texte).replace("**", "").split()) if m]


def _position(petit: list[str], grand: list[str]) -> int | None:
    """Rang du premier mot de ``petit`` dans ``grand`` s'il y figure d'un seul tenant, sinon ``None``."""
    n = len(petit)
    if not n:
        return None
    return next((i for i in range(len(grand) - n + 1) if grand[i:i + n] == petit), None)


def suivre_decoupage(pas: dict, chap: dict, nouvelles: list[dict]) -> None:
    """Garde les accroches quand les phrases du pas changent (coupe, fusion, réécriture).

    À appeler avant de remplacer ``pas["phrases"]`` par ``nouvelles``. D'après les mots des phrases :

    - une phrase gardée telle quelle garde ses objets, même déplacée ;
    - une phrase coupée donne ses objets au morceau où ils tombaient (au premier s'ils l'annonçaient) ;
    - une phrase fondue dans une autre lui donne ses objets, décalés de la place qu'elle y occupe ;
    - une phrase réécrite garde son numéro.
    """
    accroches = [o for o in pas.get("objets") or [] if o.get("phrase") is not None]
    if not accroches or not nouvelles:
        return
    anciens = [_mots(ph.get("texte")) for ph in pas.get("phrases") or []]
    neufs = [_mots(ph.get("texte")) for ph in nouvelles]
    if anciens == neufs:
        return
    reg = reglages(chap)
    t_av = temps(pas, chap)
    t_ap = temps({**pas, "phrases": nouvelles}, chap)                 # estimés si les nouvelles n'ont pas d'instants
    for o in accroches:
        k = min(max(int(o["phrase"]) - 1, 0), len(anciens) - 1)
        a = anciens[k] if anciens else []
        if a and anciens.count(a) == 1 and neufs.count(a) == 1:      # gardée, peut-être déplacée
            o["phrase"] = neufs.index(a) + 1
            continue
        morceaux = [j for j, b in enumerate(neufs) if b and _position(b, a) is not None]
        if a and len(morceaux) > 1 and sum(len(neufs[j]) for j in morceaux) <= len(a):   # coupée
            d0, d1 = t_av[k]
            t_o = instant(o, t_av, reg)
            frac = 0.0 if t_o is None or t_o <= d0 else min((t_o - d0) / max(d1 - d0, 0.1), 1.0)
            cumul, total = 0, sum(len(neufs[j]) for j in morceaux)
            for j in morceaux:
                part = len(neufs[j]) / total
                if frac < (cumul + part) or j == morceaux[-1]:
                    o["phrase"] = j + 1
                    if j != morceaux[0]:
                        o.pop("ancre", None)
                        o["decalage_s"] = round(max(0.0, (frac - cumul)) * (d1 - d0), 2)
                    break
                cumul += part
            continue
        hote = next((j for j, b in enumerate(neufs) if a and _position(a, b) is not None), None)
        if hote is not None:                                          # fondue dans une autre phrase
            o["phrase"] = hote + 1
            avant_mots = _position(a, neufs[hote])
            if avant_mots:
                b0, b1 = t_ap[hote]
                dec = o.get("decalage_s", reg["decalage_s"])
                o["decalage_s"] = round(float(dec) + avant_mots / len(neufs[hote]) * (b1 - b0), 2)
            continue
        o["phrase"] = min(k + 1, len(nouvelles))                      # réécrite : même numéro
