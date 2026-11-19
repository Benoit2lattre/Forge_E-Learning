"""QuizForge — contrôle de la qualité d'écriture des questions (appelé par ``quizforge valider``).

Règles simples, sans modèle de langue, tirées des fiches de lecture (``reference/A_tests_retroaction``, ``B_conception_qcm``) :

- rétroaction absente (vanderkleij2015, attali2017) ;
- défauts d'écriture et indices qui trahissent la clé (downing2005, tarrant2008, haladyna2022, moore2023, menze2026) ;
- QCM à 4 options ou plus (haladyna2022, raymond2018) ; options numériques dans l'ordre (gierl2017).

Chaque alerte est un point à vérifier, pas un verdict : une clé plus longue ou un « toujours » peuvent être voulus.
"""
import itertools
import re
import unicodedata
from collections import Counter, defaultdict

# Poids d'une alerte : 3 = indice fort ou défaut qui fausse la question ; 2 = à revoir ; 1 = à considérer.
CLE_LONGUE = 1.3          # clé au moins 1,3 fois plus longue que la moyenne des leurres
VF_PLAGE = (0.35, 0.65)   # part de « vrai » acceptable dans un onglet de vrai/faux
N_MIN_ONGLET = 4          # nombre de questions d'un onglet à partir duquel on regarde les régularités

ABSOLUS = re.compile(r"\b(toujours|jamais|nécessairement|forcément|uniquement|seulement|aucun|aucune|"
                     r"always|never|necessarily|only|none)\b", re.I)
TOUTES_AUCUNE = re.compile(r"(toutes? (les|ces) (réponses|propositions)|aucune (des|de ces) (réponses|propositions)|"
                           r"tout ce qui précède|aucune de ces réponses|all of the above|none of the above|"
                           r"les deux réponses|both of the above)", re.I)
COMBINEE = re.compile(r"^\s*(réponses?\s+|options?\s+)?[A-Ea-e1-5]\s*(,\s*[A-Ea-e1-5]\s*)*(et|and|&|\+)\s*[A-Ea-e1-5]\s*$", re.I)
NEGATION = re.compile(r"(\bne\b|\bn')[^.?!]{0,40}\bpas\b|\bsauf\b|\bexcepté\b|\bNOT\b|\bEXCEPT\b|\bfausse\b|\bincorrecte?\b", re.I)
CONSIGNE = re.compile(r"(\?|choisi|coch|indique|sélectionn|donne|complét|associ|reli|parmi|laquelle|lequel|lesquel|"
                      r"quel|quelle|:\s*$|…\s*$|\.\.\.\s*$|which|select|choose)", re.I)
MOTS_VIDES = set("avec dans pour sont cette entre leurs leur plus moins elle elles alors comme donc ainsi être avoir "
                 "quelle quel quels quelles laquelle lequel suivante suivantes suivant réponse réponses which there "
                 "their about these those where valeur".split())


def _texte(s) -> str:
    """Renvoie le texte brut : sans balises HTML, sans LaTeX entre ``\\( \\)`` ou ``$ $``, espaces réduits."""
    s = re.sub(r"<[^>]+>", " ", str(s or ""))
    s = re.sub(r"\\\(.*?\\\)|\$[^$]*\$", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def _norm(s) -> str:
    """Renvoie le texte brut en minuscules et sans accents (pour comparer des textes)."""
    s = unicodedata.normalize("NFKD", _texte(s).casefold())
    return "".join(c for c in s if not unicodedata.combining(c))


def _nombre(s):
    """Renvoie la valeur numérique d'une option (« 12,5 MPa », « -3e4 ») ou ``None``."""
    m = re.fullmatch(r"\s*([-+−]?\d+(?:[.,]\d+)?(?:[eE][-+]?\d+)?)\s*[^\d\s]{0,6}\s*", _texte(s))
    return float(m.group(1).replace(",", ".").replace("−", "-")) if m else None


def _a_retroaction(q) -> bool:
    """Indique si la question a au moins une rétroaction (générale, par option, juste/faux ou par erreur type)."""
    if _texte(q.get("feedback")):
        return True
    if q["type"] == "vf":
        return bool(_texte(q.get("feedback_faux")) or _texte(q.get("feedback_juste")))
    if q["type"] == "qcm":
        return any(_texte(c.get("feedback")) for c in q.get("choix", []))
    if q["type"] == "numerique":
        return bool(_texte(q.get("feedback_juste")) or _texte(q.get("feedback_faux"))
                    or any(_texte(e.get("feedback")) for e in q.get("erreurs", [])))
    return False


def _negation_visible(html: str) -> bool:
    """Indique si chaque négation de l'énoncé est mise en évidence (gras, souligné, majuscules)."""
    for m in NEGATION.finditer(html):
        avant = html[:m.start()].lower()
        ouvert = sum(avant.count(f"<{b}") for b in ("b>", "b ", "strong", "u>")) \
            - sum(avant.count(f"</{b}") for b in ("b>", "strong", "u>"))
        if ouvert > 0 or any(w.isupper() and len(w) > 1 for w in re.findall(r"\w+", m.group(0))):
            continue
        return False
    return True


def controler_question(q) -> list:
    """Contrôle une question lue par ``lire_excel`` et renvoie la liste des alertes ``[(poids, message)]``.

    Poids : 3 = indice fort ou défaut qui fausse la question ; 2 = à revoir ; 1 = à considérer.
    """
    out = []
    typ, enonce = q["type"], q.get("question", "")
    if typ == "qcm":
        choix = q.get("choix", [])
        textes = [_texte(c["texte"]) for c in choix]
        bons = [i for i, c in enumerate(choix) if c.get("correct")]
        # défauts d'écriture
        if any(TOUTES_AUCUNE.search(t) for t in textes):
            out.append((3, "option « toutes / aucune des réponses » : à remplacer par une erreur type"))
        if any(COMBINEE.match(t) for t in textes):
            out.append((3, "option combinée (« A et B ») : préférer un QCM à plusieurs réponses ou des vrai/faux multiples"))
        dbl = [t for t, n in Counter(_norm(t) for t in textes).items() if n > 1]
        if dbl:
            out.append((3, f"options en double : « {dbl[0][:40]} »"))
        if not CONSIGNE.search(_texte(enonce)):
            out.append((1, "énoncé sans question ni consigne : formuler la question dans l'énoncé"))
        if not _negation_visible(enonce):
            out.append((2, "négation dans l'énoncé : la mettre en gras (« ne … pas », « sauf ») ou reformuler"))
        # indices qui trahissent la clé (QCM à une réponse)
        if len(bons) == 1 and len(choix) >= 3:
            k = bons[0]
            lg = [len(t) for t in textes]
            leurres = [l for i, l in enumerate(lg) if i != k]
            texte_redige = all(len(re.findall(r"[^\W\d_]{3,}", t)) >= 2 for t in textes)   # pas pour des formules
            if texte_redige and leurres and lg[k] > max(leurres) and lg[k] >= CLE_LONGUE * (sum(leurres) / len(leurres)):
                out.append((3, f"clé nettement plus longue que les leurres ({lg[k]} caractères contre "
                               f"{sum(leurres) / len(leurres):.0f} en moyenne)"))
            mots_enonce = {w for w in re.findall(r"\w{5,}", _norm(enonce)) if w not in MOTS_VIDES}
            repris = [w for w in re.findall(r"\w{5,}", _norm(textes[k])) if w in mots_enonce
                      and not any(w in _norm(t) for i, t in enumerate(textes) if i != k)]
            if repris:
                out.append((2, f"la clé seule reprend un mot de l'énoncé (« {repris[0]} »)"))
            absolus = [i for i, t in enumerate(textes) if i != k and ABSOLUS.search(t)]
            if absolus:
                out.append((2, "terme absolu dans un leurre (« " + ABSOLUS.search(textes[absolus[0]]).group(0)
                               + " ») : il désigne souvent une réponse fausse"))
        # erreurs types visées par les leurres (Code erreur n)
        if any(c.get("erreur") for c in choix):
            if any(c.get("erreur") and c.get("correct") for c in choix):
                out.append((2, "code d'erreur sur une bonne réponse : à retirer"))
            sans = [i + 1 for i, c in enumerate(choix) if not c.get("correct") and not c.get("erreur")]
            if sans:
                out.append((1, f"leurre(s) {', '.join(map(str, sans))} sans erreur type : le remplacer par une erreur "
                               "observée, ou le retirer"))
            dbl = [k for k, n in Counter(_norm(c["erreur"]) for c in choix if c.get("erreur")).items() if n > 1]
            if dbl and not q.get("plusieurs"):
                out.append((1, f"deux leurres pour la même erreur (« {dbl[0]} ») : un seul suffit"))
        nums = [_nombre(t) for t in textes]
        if len(nums) >= 3 and all(v is not None for v in nums) and nums != sorted(nums) and nums != sorted(nums, reverse=True):
            out.append((1, "options numériques : les présenter dans l'ordre croissant (et désactiver le mélange)"))
    elif typ == "numerique":
        # une erreur type dont l'intervalle touche celui de la bonne réponse ne sera jamais reconnue (Moodle retient la
        # première réponse qui contient la saisie) : la clé et l'erreur se confondent (sikurajapathi2023)
        v, tv = q.get("valeur", 0), q.get("tolerance", 0)
        errs = q.get("erreurs", [])
        for k, e in enumerate(errs, 1):
            if abs(e["valeur"] - v) <= e["tolerance"] + tv:
                out.append((3, f"erreur {k} ({e['valeur']:g}) dans la tolérance de la bonne réponse ({v:g} ± {tv:g}) : "
                               "changer les données de l'énoncé pour séparer la clé de l'erreur type"))
            for j, f in enumerate(errs[k:], k + 1):
                if abs(e["valeur"] - f["valeur"]) <= e["tolerance"] + f["tolerance"]:
                    out.append((2, f"erreurs {k} et {j} confondues ({e['valeur']:g} et {f['valeur']:g}) : "
                                   "la seconde ne sera jamais reconnue"))
            if not e.get("feedback"):
                out.append((2, f"erreur {k} sans rétroaction : dire quelle erreur a probablement été faite"))
    elif typ == "vf":
        m = ABSOLUS.search(_texte(enonce))
        if m:
            out.append((2, f"terme absolu dans l'affirmation (« {m.group(0)} ») : indice de réponse « faux »"))
        if not _negation_visible(enonce):
            out.append((1, "négation dans l'affirmation : la mettre en gras ou reformuler à l'affirmative"))
    return out


def _cle_index(q):
    """Renvoie l'indice de la bonne option d'un QCM à une seule bonne réponse, sinon ``None``."""
    bons = [i for i, c in enumerate(q.get("choix", [])) if c.get("correct")]
    return bons[0] if len(bons) == 1 else None


# --------------------------------------------------------------------------- score au hasard et seuil conseillé
# Score moyen obtenu en répondant au hasard, et score moyen d'un étudiant qui connaît la moitié de la matière
# (seuil de réussite qui correspond à « la moitié des connaissances »), pour le barème du profil.
#   - vrai/faux, QCM à une réponse (n options), appariement (m réponses proposées) : hasard 1/n, seuil 50 % + 50 %/n
#     (kanzow2023 ; schmidt2021 pour le vrai/faux) ;
#   - QCM à plusieurs réponses : calcul exact sur toutes les façons de cocher, avec la note de Moodle ramenée entre 0 et 1 ;
#     hasard = chaque case cochée avec une probabilité 1/2 ; moitié des connaissances = chaque case connue avec une
#     probabilité 1/2, les autres cochées au hasard (chaque case juste avec une probabilité 3/4) [modèle simplifié de
#     schmidt2021 et schmidt2022].
# Les questions numériques, à réponse courte, à trous et ouvertes ont un score au hasard proche de 0.

def _note_multi(coches, bons, pen):
    """Calcule la note Moodle d'un QCM à plusieurs réponses.

    Chaque bonne case cochée rapporte 1/t (t = nombre de bonnes cases), chaque mauvaise case cochée ``pen`` ;
    le total est ramené entre 0 et 1.
    """
    t = sum(bons)
    s = sum((1 / t if b else pen) for c, b in zip(coches, bons) if c)
    return min(1.0, max(0.0, s))


def penalite(t, n, mode):
    """Renvoie la pénalité d'une mauvaise case cochée dans un QCM à plusieurs réponses (t bonnes sur n).

    ``mode`` (barème ``mauvaise_option`` du profil) : ``"zero"`` → 0 ; ``"equilibree"`` → -1/(n - t)
    (si n > t) ; sinon (``"negative"``) → -1/t.
    """
    if mode == "zero":
        return 0.0
    if mode == "equilibree" and n > t:
        return -1 / (n - t)
    return -1 / t


def hasard_question(q, mode="negative"):
    """Renvoie ``(score au hasard, score avec la moitié des connaissances, score en cochant tout)`` en fraction, ou ``None``.

    Le troisième terme ne vaut que pour un QCM à plusieurs réponses (``None`` sinon). Les questions
    numériques, à réponse courte, à trous et ouvertes renvoient ``None``.
    """
    typ = q["type"]
    if typ == "vf":
        return 0.5, 0.75, None
    if typ == "appariement":
        m = len(q.get("paires", [])) + len(q.get("distracteurs", []))
        return (1 / m, 0.5 + 0.5 / m, None) if m else None
    if typ == "qcm":
        choix = q.get("choix", [])
        n = len(choix)
        bons = [bool(c.get("correct")) for c in choix]
        if not q.get("plusieurs"):
            return 1 / n, 0.5 + 0.5 / n, None
        t = sum(bons)
        pen = penalite(t, n, mode)
        h = s = 0.0
        for coches in itertools.product((0, 1), repeat=n):
            note = _note_multi(coches, bons, pen)
            justes = sum(1 for c, b in zip(coches, bons) if bool(c) == b)
            h += note / 2 ** n
            s += note * 0.75 ** justes * 0.25 ** (n - justes)
        return h, s, _note_multi([1] * n, bons, pen)
    return None


def rapport_hasard(qs: list, mode="negative") -> list:
    """Renvoie les lignes du rapport de ``convertir`` : score au hasard et seuil conseillé, par onglet et pour le classeur."""
    par = defaultdict(list)
    for q in qs:
        src = (q.get("source") or "").split(" › ")
        par[(q.get("_tags_auto") or {}).get("onglet") or (src[1] if len(src) > 2 else "?")].append(q)
    lignes = [f"Score au hasard et seuil conseillé (barème du profil ; QCM à plusieurs réponses : mauvaise_option = {mode}) :"]
    tout_h, tout_s = [], []
    for onglet, L in par.items():
        r = [hasard_question(q, mode) for q in L]
        h = [x[0] if x else 0.0 for x in r]
        s = [x[1] if x else 0.5 for x in r]
        tout_h += h; tout_s += s
        lignes.append(f"   {onglet} ({len(L)} q.) : au hasard {100 * sum(h) / len(h):.0f} % ; "
                      f"avec la moitié des connaissances {100 * sum(s) / len(s):.0f} %")
    if tout_h:
        lignes.append(f"   Toutes les questions, même poids : au hasard {100 * sum(tout_h) / len(tout_h):.0f} % ; seuil conseillé "
                      f"pour exiger la moitié des connaissances : {100 * sum(tout_s) / len(tout_s):.0f} %. Seuil calculé pour un "
                      "test qui reprend toutes ces questions avec le même poids ; à refaire pour un tirage."
                      + (" QCM à plusieurs réponses avec des points négatifs : annoncez le barème aux étudiants (lesage2013)."
                         if mode != "zero" and any(q["type"] == "qcm" and q.get("plusieurs") for q in qs) else ""))
    return lignes


def controler(qs: list, mode: str = "negative") -> list:
    """Contrôle les questions d'un classeur et renvoie des lignes « [poids] source : message », triées par poids décroissant.

    Les régularités d'un onglet (rétroactions absentes, position et longueur des clés, vrai/faux) sont regroupées ;
    le poids est écrit en points d'exclamation (``[!!!]`` pour 3).
    """
    lignes = []
    par_onglet = defaultdict(list)
    for q in qs:
        par_onglet[(q.get("_tags_auto") or {}).get("onglet", "?")].append(q)
        for poids, msg in controler_question(q):
            lignes.append((poids, q.get("source", q.get("titre", "")), msg))
        if q["type"] == "qcm" and q.get("plusieurs"):
            r = hasard_question(q, mode)
            if r and r[2] and r[2] > 0:
                lignes.append((3 if mode == "zero" else 2, q.get("source", ""),
                               f"cocher toutes les cases rapporte {100 * r[2]:.0f} % (barème mauvaise_option = {mode}) : "
                               + ("passer à « equilibree » ou « negative »" if mode == "zero" else
                                  "passer à « equilibree » (-1/(n-t) par mauvaise case) ou mettre moins de bonnes réponses que de mauvaises")))
    for onglet, L in par_onglet.items():
        # rétroaction absente (les essais ont leur propre correction)
        sans = [q for q in L if q["type"] != "essai" and not _a_retroaction(q)]
        if sans:
            num = ", ".join(q.get("source", "").rsplit("ligne ", 1)[-1] for q in sans[:12]) + (" …" if len(sans) > 12 else "")
            lignes.append((3, onglet, f"{len(sans)} question(s) sur {len(L)} sans rétroaction (lignes {num}) : "
                                      "donner au moins la bonne réponse, de préférence une explication"))
        qcm1 = [q for q in L if q["type"] == "qcm" and _cle_index(q) is not None]
        if len(qcm1) >= N_MIN_ONGLET:
            pos = Counter(_cle_index(q) for q in qcm1)
            p, n = pos.most_common(1)[0]
            k_moy = sum(len(q["choix"]) for q in qcm1) / len(qcm1)
            if n == len(qcm1) or n / len(qcm1) > max(0.6, 2 / k_moy):
                lignes.append((1, onglet, f"clé en position {p + 1} dans {n} QCM sur {len(qcm1)} : sans effet pour les "
                                          "étudiants si les options sont mélangées (profil, XML) et si le test Moodle "
                                          "mélange les réponses ; à répartir sinon (import GIFT, mélange désactivé)"))
            plus_longue = sum(1 for q in qcm1 if len(_texte(q["choix"][_cle_index(q)]["texte"]))
                              >= max(len(_texte(c["texte"])) for c in q["choix"]))
            if plus_longue / len(qcm1) > 0.5:
                lignes.append((3, onglet, f"la clé est l'option la plus longue (ou ex aequo) dans {plus_longue} QCM sur "
                                          f"{len(qcm1)} (attendu par hasard : environ {100 / k_moy:.0f} %)"))
        # règle des 3 options : établie pour les QCM à une seule bonne réponse, pas pour les réponses multiples
        # une quatrième option se justifie si chaque leurre vise une erreur type nommée
        qcm4 = [q for q in L if q["type"] == "qcm" and not q.get("plusieurs") and len(q.get("choix", [])) >= 4
                and not all(c.get("erreur") for c in q["choix"] if not c.get("correct"))]
        if qcm4:
            lignes.append((1, onglet, f"{len(qcm4)} QCM à une réponse et 4 options ou plus : 3 options suffisent si la quatrième "
                                      "n'est pas une erreur fréquente"))
        vf = [q for q in L if q["type"] == "vf"]
        if len(vf) >= N_MIN_ONGLET:
            nv = sum(1 for q in vf if q.get("reponse"))
            if not VF_PLAGE[0] <= nv / len(vf) <= VF_PLAGE[1]:
                lignes.append((2, onglet, f"vrai/faux déséquilibrés : {nv} « vrai » pour {len(vf) - nv} « faux » "
                                          "(répondre toujours pareil rapporte des points)"))
    # codes d'erreur écrits de façons proches (casse, accents, espaces) : DiagForge les compterait séparément
    codes = Counter(c.get("erreur") or c.get("code") for q in qs for c in (q.get("choix", []) + q.get("erreurs", []))
                    if c.get("erreur") or c.get("code"))
    formes = defaultdict(set)
    for c in codes:
        formes[re.sub(r"[\W_]+", "", _norm(c))].add(c)
    for v in formes.values():
        if len(v) > 1:
            lignes.append((2, "classeur", "codes d'erreur écrits de plusieurs façons : " + " ; ".join(f"« {x} »" for x in sorted(v))
                                          + " (DiagForge les compterait comme des erreurs différentes)"))
    lignes.sort(key=lambda x: -x[0])
    return [f"[{'!' * p}] {src.split(' › ', 1)[-1]} : {msg}" for p, src, msg in lignes]
