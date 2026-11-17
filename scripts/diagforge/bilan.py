"""QuizForge — DiagForge : bilan des résultats d'un test Moodle (exports « Notes » et « Réponses »).

Usage ::

    python quizforge.py bilan <dossier ou fichiers> [-q questions.xml] [-t toutes|premiere|derniere|meilleure] [-s sortie.xlsx]

Lit les exports du rapport de test Moodle, en anglais ou en français, en CSV ou en XLSX :

- « Notes » (Grades) : note de chaque tentative et note de chaque position (Q. 1 /1,00…) ;
- « Réponses » (Responses), de préférence avec « Texte de la question » et « Bonne réponse » cochés :
  indispensable quand le test tire des questions au hasard (Q. 1 désigne alors une position, pas une question).

Les deux sont réunis tentative par tentative (courriel, début, fin, durée).
L'export XML des questions (facultatif) donne le nom de chaque question et ses options (leurres jamais choisis).
L'export « Statistiques » de Moodle n'est pas utilisé pour les calculs : les indicateurs sont recalculés ici,
son résumé n'est affiché que pour comparaison.

Produit un classeur : Synthèse, Questions, Réponses, Éléments, Étudiants, Tentatives, et selon les données
À revoir, Tirage, Rétention, Par erreur, Groupes, Par tag / type / catégorie ; ainsi qu'une fiche du
professeur (HTML) et des images pour les étudiants (voir ``bilan_sorties``).
"""
import csv
import html
import math
import re
import statistics
import sys
import unicodedata
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "commun"))
from charte import COULEUR_PRINCIPALE  # noqa: E402

# Seuils des alertes (feuille Questions)
# Seuils tirés de la bibliographie (reference/C_analyse_items/README.md) : discrimination item-reste < 0 à revoir,
# < 0,15 faible, > 0,35 très bonne, peu fiable si la réussite est hors de 0,30-0,90 (slepkov2021, macdonald2002) ;
# leurre non fonctionnel sous 0,1 x (1 - réussite) (raymond2018).
SEUILS = {"n_min": 10, "facile": 0.90, "difficile": 0.30, "discrim_faible": 0.15, "discrim_negative": 0.0,
          "discrim_tres_bonne": 0.35, "fiable_min": 0.30, "fiable_max": 0.90,
          "discrim_n_min": 20, "leurre_n_min": 20, "leurre_facteur": 0.1, "leurre_echecs_min": 10, "leurre_n_score": 5}

# Alpha typique d'un test de connaissances selon son nombre de questions, avec l'intervalle de prédiction à 90 %
# (Edelsbrunner et al., 2025, tableau 3) : repère, pas verdict.
ALPHA_ATTENDU = {10: (0.77, 0.18, 0.94), 20: (0.84, 0.44, 0.96), 50: (0.90, 0.65, 0.97)}


def plancher_difficulte(k):
    """Renvoie la réussite sous laquelle une question à ``k`` options est « très difficile ».

    C'est environ le hasard + 0,10 (slepkov2021 : 0,43 à 3 options, 0,35 à 4, 0,30 à 5 ; 0,60 à 2 options,
    par extension), jamais moins de 0,30 ; 0,30 si le nombre d'options est inconnu.
    """
    if not k or k < 2:
        return SEUILS["difficile"]
    return max(SEUILS["difficile"], round(1 / k + 0.10, 2))


def lecture_discrimination(r, reussite):
    """Renvoie la lecture de la discrimination item-reste ``r`` : « à revoir », « faible », « correcte », « très bonne » ou « peu fiable ».

    « Peu fiable » quand la réussite est hors de l'intervalle ``fiable_min`` – ``fiable_max`` de ``SEUILS`` ;
    chaîne vide si ``r`` est ``None``.
    """
    if r is None:
        return ""
    if reussite is not None and not (SEUILS["fiable_min"] <= reussite <= SEUILS["fiable_max"]):
        return "peu fiable"
    if r < SEUILS["discrim_negative"]:
        return "à revoir"
    if r < SEUILS["discrim_faible"]:
        return "faible"
    return "très bonne" if r > SEUILS["discrim_tres_bonne"] else "correcte"


def alpha_cronbach(colonnes):
    """Calcule l'alpha de Cronbach, ou ``None`` s'il n'est pas calculable.

    ``colonnes`` : une liste de notes par question, mêmes tentatives dans le même ordre.
    """
    k = len(colonnes)
    tot = [sum(v) for v in zip(*colonnes)]
    if k < 2 or len(tot) < 2 or statistics.pvariance(tot) == 0:
        return None
    return k / (k - 1) * (1 - sum(statistics.pvariance(c) for c in colonnes) / statistics.pvariance(tot))


def alpha_ramene(alpha, k, cible=50):
    """Applique la formule de Spearman-Brown : alpha d'un test de même qualité allongé (ou raccourci) de ``k`` à ``cible`` questions.

    Renvoie ``None`` si ``alpha`` est absent, négatif ou nul, ou si ``k`` < 2.
    """
    if alpha is None or alpha <= 0 or k < 2:
        return None
    m = cible / k
    return m * alpha / (1 + (m - 1) * alpha)


# ------------------------------------------------------------------ outils
def cle_texte(t) -> str:
    """Renvoie une clé de comparaison : sans accents, en minuscules, lettres et chiffres seulement."""
    t = unicodedata.normalize("NFKD", str(t or "")).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", t)


def propre(t) -> str:
    """Renvoie le texte sans balises HTML, entités décodées, espaces insécables et multiples réduits."""
    t = html.unescape(re.sub(r"<[^>]+>", " ", str(t or "")))
    return re.sub(r"\s+", " ", t.replace(" ", " ").replace(" ", " ")).strip()


def nombre(t):
    """Lit un nombre écrit à l'anglaise ou à la française (virgule, espaces, %) ; renvoie ``None`` si ce n'en est pas un."""
    s = str(t if t is not None else "").strip().replace(" ", "").replace(" ", "").replace(" ", "")
    s = s.replace("%", "").replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return None


def duree_s(t):
    """Convertit une durée Moodle (« 3 mins 20 secs », « 1 heure 5 min »…) en secondes ; ``None`` si rien n'est reconnu."""
    t = str(t or "").lower()
    s = 0
    for v, u in re.findall(r"(\d+)\s*(heures?|hours?|h|jours?|days?|mins?|minutes?|secs?|secondes?|s)\b", t):
        v = int(v)
        s += v * (86400 if u.startswith(("j", "d")) else 3600 if u.startswith("h") else 60 if u.startswith("m") else 1)
    return s or None


MOIS = {"january": 1, "janvier": 1, "february": 2, "fevrier": 2, "march": 3, "mars": 3, "april": 4, "avril": 4,
        "may": 5, "mai": 5, "june": 6, "juin": 6, "july": 7, "juillet": 7, "august": 8, "aout": 8,
        "september": 9, "septembre": 9, "october": 10, "octobre": 10, "november": 11, "novembre": 11,
        "december": 12, "decembre": 12}


def date(t):
    """Convertit une date Moodle en ``datetime`` (sinon ``None``).

    Formes reconnues : « 6 November 2026  12:12 AM », « 6 novembre 2026, 00:12 », « 06/11/2026 00:12 ».
    """
    s = unicodedata.normalize("NFKD", str(t or "")).encode("ascii", "ignore").decode().lower()
    m = re.search(r"(\d{1,2})\s+([a-z]+)\s+(\d{4})\D+(\d{1,2}):(\d{2})\s*(am|pm)?", s)
    if m and m.group(2) in MOIS:
        h = int(m.group(4)) % 12 + (12 if m.group(6) == "pm" else 0) if m.group(6) else int(m.group(4))
        return datetime(int(m.group(3)), MOIS[m.group(2)], int(m.group(1)), h, int(m.group(5)))
    m = re.search(r"(\d{1,2})/(\d{1,2})/(\d{4})\D+(\d{1,2}):(\d{2})", s)
    if m:
        return datetime(int(m.group(3)), int(m.group(2)), int(m.group(1)), int(m.group(4)), int(m.group(5)))
    return None


def pearson(x, y):
    """Renvoie le coefficient de corrélation de Pearson, ou ``None`` (moins de 3 points ou variance nulle)."""
    if len(x) < 3:
        return None
    mx, my = statistics.fmean(x), statistics.fmean(y)
    sx = math.sqrt(sum((a - mx) ** 2 for a in x)); sy = math.sqrt(sum((b - my) ** 2 for b in y))
    if sx == 0 or sy == 0:
        return None
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy)


# ------------------------------------------------------------------ lecture des exports
def lire_table(p: Path):
    """Lit un export CSV ou XLSX et renvoie ses lignes non vides (listes de chaînes).

    Pour un CSV : encodage UTF-8 ou Windows-1252, séparateur deviné sur la première ligne ; un export
    interrompu par une page d'erreur HTML est coupé avant celle-ci.
    """
    if p.suffix.lower() in (".xlsx", ".xlsm"):
        import openpyxl
        ws = openpyxl.load_workbook(p, read_only=True, data_only=True).active
        lignes = [["" if v is None else str(v) for v in r] for r in ws.iter_rows(values_only=True)]
    else:
        brut = p.read_bytes()
        for enc in ("utf-8-sig", "cp1252"):
            try:
                txt = brut.decode(enc); break
            except UnicodeDecodeError:
                continue
        coupe = min([i for i in (txt.find("<!DOCTYPE"), txt.find("<html")) if i >= 0], default=-1)
        if coupe >= 0:                       # export Moodle interrompu par une page d'erreur : on garde le début
            txt = txt[:coupe]
        if not txt.strip():
            return []
        sep = max(",;\t", key=lambda c: txt.split("\n", 1)[0].count(c))
        lignes = list(csv.reader(txt.splitlines(), delimiter=sep))
    return [l for l in lignes if any(str(c).strip() for c in l)]


def colonnes(entete):
    """Repère le rôle de chaque colonne d'un en-tête d'export Moodle.

    Renvoie ``(fixes, slots, total)`` : ``fixes = {"nom": i, ...}`` (identité, état, dates, durée),
    ``slots = {k: {"note": i, "max": m, "question": i, "reponse": i, "bonne": i}}`` par position,
    ``total = (indice, note maximale)`` de la colonne de note globale, ou ``None``.
    """
    fixes, slots, total = {}, defaultdict(dict), None
    noms = {"nom": ["lastname", "nom", "nomdefamille", "surname"], "prenom": ["firstname", "prenom"],
            "email": ["emailaddress", "adressedecourriel", "adressecourriel", "courriel", "email", "adressemail"],
            "etat": ["status", "state", "etat"], "debut": ["started", "startedon", "commencele", "debut", "commence"],
            "fin": ["completed", "termine", "terminele", "fin"], "duree": ["duration", "timetaken", "tempsutilise", "duree"]}
    for i, h in enumerate(entete):
        c, bas = cle_texte(h), str(h).strip().lower()
        for role, alias in noms.items():
            if c in alias and role not in fixes:
                fixes[role] = i
        m = re.match(r"^(grade|note)\s*/\s*([\d.,]+)", bas)
        if m:
            total = (i, nombre(m.group(2)))
        m = re.match(r"^q\.?\s*(\d+)\s*/\s*([\d.,]+)", bas)
        if m:
            slots[int(m.group(1))].update(note=i, max=nombre(m.group(2)))
        m = re.match(r"^(question|response|réponse|reponse|right answer|bonne réponse|bonne reponse)\s*(\d+)$", bas)
        if m:
            role = {"question": "question", "response": "reponse", "réponse": "reponse", "reponse": "reponse"}.get(m.group(1), "bonne")
            slots[int(m.group(2))][role] = i
    return fixes, dict(slots), total


def nom_du_test(stem: str) -> str:
    """Extrait le nom du test d'un nom de fichier : « MMC-Quizz1_SMA-grades » → « Quizz1_SMA ».

    Moodle nomme ses exports ``<cours>-<test>-<rapport>``.
    """
    s = re.sub(r"[-_ ]*(grades|responses|notes|reponses|réponses|completestats|questionstats|statistiques)( \(\d+\))?$", "",
               stem, flags=re.I)
    return s.rsplit("-", 1)[-1].strip() if "-" in s else s.strip()


def groupe_du_test(test: str) -> str:
    """Extrait le groupe d'un nom de test : « Quizz1_SMA » → « SMA » (suffixe court après le dernier ``_``), sinon ``""``."""
    if "_" in test:
        suf = test.rsplit("_", 1)[1]
        if 1 <= len(suf) <= 8 and suf.isalnum():
            return suf
    return ""


def lire_exports(fichiers, avert, moodle=None):
    """Lit les exports « Notes » et « Réponses » et renvoie la liste des tentatives (dictionnaires).

    Les lignes des différents exports sont réunies sur (test, courriel, début, fin, durée) et leur rang
    d'apparition, pour séparer deux tentatives commencées à la même minute.
    ``avert`` reçoit un message par fichier ; ``moodle``, s'il est fourni, reçoit le résumé de l'export
    « Statistiques ».
    """
    tent, ordre = {}, []
    for p in fichiers:
        lignes = lire_table(p)
        if not lignes:
            avert.append(f"{p.name} : ignoré (vide ou page d'erreur Moodle)")
            continue
        fixes, slots, total = colonnes(lignes[0])
        if "debut" not in fixes or not (slots or total):
            if cle_texte(lignes[0][0]) in ("quizname", "nomdutest", "test"):
                if moodle is not None and len(lignes) > 1 and not moodle:
                    moodle.update({h: v.lstrip("'") for h, v in zip(lignes[0], lignes[1])})
                avert.append(f"{p.name} : export « Statistiques » : résumé du test lu pour comparaison"
                             + ("" if len(lignes) > 1 else " (vide)") + " ; statistiques par question recalculées par QuizForge")
            else:
                avert.append(f"{p.name} : en-têtes non reconnus, ignoré")
            continue
        sorte = "réponses" if any("reponse" in s or "question" in s for s in slots.values()) else "notes"
        n, vus = 0, Counter()
        for l in lignes[1:]:
            l = l + [""] * (len(lignes[0]) - len(l))
            if cle_texte(l[fixes.get("nom", 0)]) in ("overallaverage", "moyennegenerale", "moyenne"):
                continue
            ident = (l[fixes["email"]].strip().lower() if "email" in fixes else
                     f"{l[fixes.get('nom', 0)]} {l[fixes.get('prenom', 1)]}".strip().lower())
            # début à la minute près : on ajoute fin, durée et rang dans le fichier pour séparer deux tentatives
            base = (nom_du_test(p.stem), ident, l[fixes["debut"]].strip(), l[fixes["fin"]].strip() if "fin" in fixes else "",
                    l[fixes["duree"]].strip() if "duree" in fixes else "")
            vus[base] += 1
            k = base + (vus[base],)
            if k not in tent:
                tent[k] = {"id": ident, "nom": l[fixes["nom"]] if "nom" in fixes else "", "prenom": l[fixes["prenom"]] if "prenom" in fixes else "",
                           "email": l[fixes["email"]] if "email" in fixes else "", "debut": l[fixes["debut"]], "date": date(l[fixes["debut"]]),
                           "etat": l[fixes["etat"]] if "etat" in fixes else "", "duree": duree_s(l[fixes["duree"]]) if "duree" in fixes else None,
                           "note": None, "note_max": None, "a_corriger": False, "slots": {}, "rang": len(ordre),
                           "test": nom_du_test(p.stem), "groupe": ""}
                ordre.append(k)
            t = tent[k]
            if total:
                v = nombre(l[total[0]])
                t["note_max"] = total[1]
                if v is not None:
                    t["note"] = v
                elif sorte == "notes" and l[total[0]].strip() not in ("", "-"):
                    t["a_corriger"] = True
            for s, c in slots.items():
                d = t["slots"].setdefault(s, {})
                if "note" in c:
                    brut = l[c["note"]].strip()
                    d["max"] = c["max"]
                    v = nombre(brut)
                    if v is not None:
                        d["note"] = v; d.pop("a_corriger", None)
                    elif brut not in ("", "-"):
                        d["a_corriger"] = True; t["a_corriger"] = True
                for r in ("question", "reponse", "bonne"):
                    if r in c and l[c[r]].strip() != "":
                        d[r] = l[c[r]].strip()
            n += 1
        avert.append(f"{p.name} : export « {sorte} », {n} tentative(s)")
    return [tent[k] for k in ordre]


# ------------------------------------------------------------------ banque de questions (export XML Moodle)
def lire_banque_xml(xmls):
    """Lit les exports XML Moodle des questions et renvoie la banque (liste de dictionnaires).

    Chaque question : ``nom``, ``type``, ``texte``, ``options``, ``single``, ``tags`` et ``categorie``.
    Un fichier illisible est ignoré.
    """
    banque = []
    for p in xmls:
        try:
            r = ET.parse(p).getroot()
        except ET.ParseError:
            continue
        categorie = ""
        for q in r.findall("question"):
            t = q.get("type")
            if t == "category":
                categorie = re.sub(r"^\$(course|system|module|cat\w*)\$/(top/)?", "", propre(q.findtext("category/text")))
                continue
            if t is None:
                continue
            opts = [propre(a.findtext("text")) for a in q.findall("answer")]
            opts += [propre(a.findtext("text")) for a in q.findall("selectoption")] + [propre(a.findtext("text")) for a in q.findall("dragbox")]
            banque.append({"nom": propre(q.findtext("name/text")), "type": t, "texte": propre(q.findtext("questiontext/text")),
                           "options": [o for o in opts if o], "single": (q.findtext("single") or "true") == "true",
                           "tags": [propre(x.findtext("text")) for x in q.findall("tags/tag") if propre(x.findtext("text"))],
                           "categorie": categorie})
    return banque


TYPES_YAML = {"vf": "truefalse", "qcm": "multichoice", "appariement": "matching", "courte": "shortanswer",
              "numerique": "numerical", "essai": "essay", "schema": "ddimageortext", "trous": "ddwtos"}


def completer_banque_yaml(chemins, banque):
    """Complète la banque avec les banques YAML de QuizForge (``convertir`` → ``<classeur>_banque.yaml``).

    Ajoute les erreurs types visées par les leurres (Code erreur n) aux questions de même nom ;
    une question absente de l'export XML est ajoutée. Renvoie la banque.
    """
    import yaml
    for p in chemins:
        try:
            doc = yaml.safe_load(Path(p).read_text(encoding="utf-8")) or {}
        except Exception:
            continue
        for q in doc.get("questions", []) if isinstance(doc, dict) else []:
            nom = propre(q.get("titre", ""))
            erreurs = {forme(propre(c["texte"])).casefold(): c["erreur"] for c in q.get("choix", []) if c.get("erreur")}
            erreurs_num = [(e["valeur"], e.get("tolerance", 0), e["code"]) for e in q.get("erreurs", []) if e.get("code")]
            cible = next((b for b in banque if b["nom"] == nom), None)
            if cible is None:
                cible = {"nom": nom, "type": TYPES_YAML.get(q.get("type"), q.get("type")), "texte": propre(q.get("question", "")),
                         "options": [propre(c["texte"]) for c in q.get("choix", [])], "single": not q.get("plusieurs"),
                         "tags": list(q.get("tags", [])), "categorie": q.get("categorie", "")}
                if isinstance(q.get("seance"), int):
                    cible["seance"] = q["seance"]
                banque.append(cible)
            if erreurs:
                cible["erreurs"] = erreurs
            if erreurs_num:
                cible["erreurs_num"] = erreurs_num
    return banque


def codes_erreur(rep, q):
    """Renvoie les erreurs types (Code erreur n de QuizForge) que trahit une réponse ; ``[]`` si la banque n'en donne pas."""
    if not q or not rep:
        return []
    if q.get("erreurs_num"):
        try:
            v = float(str(rep).replace(",", ".").replace("−", "-").split()[0])
        except (ValueError, IndexError):
            return []
        return next(([c] for x, tol, c in q["erreurs_num"] if abs(v - x) <= tol), [])
    if q.get("erreurs"):
        morceaux = [rep] if q.get("single", True) else sorted(cases(rep))
        return [q["erreurs"][k] for k in (forme(m).casefold() for m in morceaux) if k in q["erreurs"]]
    return []


def par_erreur(obs, infos):
    """Renvoie une ligne par erreur type, de la plus fréquente à la moins fréquente.

    Chaque ligne donne les questions qui la visent, les réponses, la part des réponses qui la trahissent, les
    étudiants qui la font, et ceux qui la font sur au moins deux questions (un diagnostic sur une seule
    question est fragile : klingbeil2024).
    """
    rec = defaultdict(lambda: {"questions": set(), "exposees": 0, "choix": 0, "etu": defaultdict(set), "etu_vus": set()})
    for nom, L in obs.items():
        q = infos[nom]["banque"]
        if not q or not (q.get("erreurs") or q.get("erreurs_num")):
            continue
        visees = set(q.get("erreurs", {}).values()) | {c for _, _, c in q.get("erreurs_num", [])}
        for o in L:
            for c in visees:
                rec[c]["questions"].add(nom); rec[c]["exposees"] += 1; rec[c]["etu_vus"].add(o["t"]["id"])
            for c in set(codes_erreur(o["rep"], q)):
                rec[c]["choix"] += 1; rec[c]["etu"][o["t"]["id"]].add(nom)
    lignes = []
    for c, r in rec.items():
        plusieurs = sum(1 for qs in r["etu"].values() if len(qs) >= 2)
        lignes.append({"erreur": c, "n_questions": len(r["questions"]), "questions": ", ".join(sorted(r["questions"])),
                       "exposees": r["exposees"], "choix": r["choix"], "taux": r["choix"] / r["exposees"] if r["exposees"] else None,
                       "etudiants": len(r["etu"]), "part_etudiants": len(r["etu"]) / len(r["etu_vus"]) if r["etu_vus"] else None,
                       "repetee": plusieurs if len(r["questions"]) >= 2 else None})
    lignes.sort(key=lambda x: -(x["taux"] or 0))
    return lignes


GREC = {"alpha": "α", "beta": "β", "gamma": "γ", "delta": "δ", "epsilon": "ϵ", "varepsilon": "ε", "zeta": "ζ", "eta": "η",
        "theta": "θ", "vartheta": "ϑ", "kappa": "κ", "lambda": "λ", "mu": "μ", "nu": "ν", "xi": "ξ", "pi": "π", "rho": "ρ",
        "sigma": "σ", "tau": "τ", "phi": "φ", "varphi": "φ", "chi": "χ", "psi": "ψ", "omega": "ω", "Gamma": "Γ",
        "Delta": "Δ", "Theta": "Θ", "Lambda": "Λ", "Sigma": "Σ", "Phi": "Φ", "Psi": "Ψ", "Omega": "Ω", "nabla": "∇",
        "partial": "∂", "infty": "∞", "times": "×", "cdot": "·", "leq": "≤", "geq": "≥", "neq": "≠", "approx": "≈",
        "sqrt": "√", "pm": "±", "to": "→", "rightarrow": "→"}


def _latex_lisible(f: str) -> str:
    """Convertit une formule LaTeX simple en texte Unicode lisible.

    Par exemple σ̲̲ pour ``\\underline{\\underline{\\sigma}}``, a/b pour ``\\frac{a}{b}``.
    """
    def marque(t, m):                         # trait combinant après chaque caractère (et ses traits déjà posés)
        out = ""
        for c in t:
            if out and not unicodedata.combining(c):
                out += m
            out += c
        return out + m if out else out

    f = re.sub(r"\\(?!(?:d?frac|underline|overline|bar|vec|overrightarrow|mathrm|text|mathbf|boldsymbol|operatorname|mathit)\b)([A-Za-z]+)",
               lambda m: GREC.get(m.group(1), m.group(1)), f)
    for _ in range(6):                        # des accolades les plus intérieures vers l'extérieur
        g = re.sub(r"\\d?frac\{([^{}]*)\}\{([^{}]*)\}", r"\1/\2", f)
        g = re.sub(r"\\underline\{([^{}]*)\}", lambda m: marque(m.group(1), "\u0332"), g)
        g = re.sub(r"\\(?:overline|bar)\{([^{}]*)\}", lambda m: marque(m.group(1), "\u0305"), g)
        g = re.sub(r"\\(?:vec|overrightarrow)\{([^{}]*)\}", lambda m: m.group(1) + "\u20d7", g)
        g = re.sub(r"\\(?:mathrm|text|mathbf|boldsymbol|operatorname|mathit)\{([^{}]*)\}", r"\1", g)
        g = re.sub(r"([_^])\{([^{}]*)\}", r"\1\2", g)
        if g == f:
            break
        f = g
    return f.replace("{", "").replace("}", "").replace("\\", "")


def lisible(t) -> str:
    """Renvoie le texte d'une réponse pour un message : formules ``$…$`` ou ``\\(…\\)`` rendues en Unicode, numéro d'étiquette « 5. » retiré."""
    t = str(t)
    t = re.sub(r"\$([^$]+)\$|\\\((.+?)\\\)", lambda m: _latex_lisible(m.group(1) or m.group(2)), t)
    return re.sub(r"^\d+\.\s+", "", t.strip())


def abrege(t, n: int) -> str:
    """Renvoie :func:`lisible` de ``t`` coupé à ``n`` caractères au plus, à une fin de mot, avec « … »."""
    t = lisible(t)
    if len(t) <= n:
        return t
    c = t[:n].rsplit(" ", 1)[0] if " " in t[:n] else t[:n]
    return c.rstrip(" ,;:") + " …"


def tronc(resume: str) -> str:
    """Renvoie le texte de la question sans la liste d'options que Moodle ajoute au résumé (ordre mélangé)."""
    r = resume
    for motif in (r";\s*\[\[", r"\s\{[^{}]*\}\s*->\s*\{", r"\?:\s"):
        m = re.search(motif, r)
        if m:
            r = r[:m.start() + (1 if motif == r"\?:\s" else 0)]
    m = re.search(r":\s[^:]*;\s", r)
    if m and ";" in r[m.start():]:
        r = r[:m.start()]
    return r.strip()


def identifier(resume, banque):
    """Renvoie la question de la banque dont le texte commence le résumé Moodle (la plus longue correspondance), sinon ``None``."""
    c = cle_texte(resume)
    meilleure = None
    for q in banque:
        cq = cle_texte(q["texte"])[:60]
        if cq and c.startswith(cq[:max(12, len(cq))]) and (meilleure is None or len(cq) > len(cle_texte(meilleure["texte"])[:60])):
            meilleure = q
    return meilleure


# ------------------------------------------------------------------ formes des réponses
def accolades(t):
    """Renvoie les groupes entre accolades de premier niveau : ``'{a} {b{c}}'`` → ``['a', 'b{c}']``."""
    out, prof, cur = [], 0, ""
    for ch in t:
        if ch == "{":
            if prof > 0:
                cur += ch
            prof += 1
        elif ch == "}":
            prof -= 1
            if prof > 0:
                cur += ch
            elif prof == 0:
                out.append(cur.strip()); cur = ""
        elif prof > 0:
            cur += ch
    return out


def elements(rep: str):
    """Découpe une réponse composée (zones, paires, trous) en ``[(élément, valeur)]`` ; ``None`` si la réponse est simple."""
    rep = rep or ""
    zones = list(re.finditer(r"(Drop zone|Zone de dépôt|Zone)\s*(\d+)\s*->", rep, re.I))
    if zones and zones[0].start() == 0:
        out = []
        for k, m in enumerate(zones):
            fin = zones[k + 1].start() if k + 1 < len(zones) else len(rep)
            g = accolades(rep[m.end():fin])
            out.append((f"{m.group(1)} {m.group(2)}", g[0] if g else rep[m.end():fin].strip()))
        return out
    if " -> " in rep and ";" in rep or re.match(r"^[^;{}]+ -> [^;]+$", rep):
        return [(a.strip(), b.strip()) for a, b in (x.split("->", 1) for x in rep.split(";") if "->" in x)]
    if rep.startswith("{"):
        return [(f"trou {k}", v) for k, v in enumerate(accolades(rep), 1)]
    return None


def forme(rep: str) -> str:
    """Renvoie une forme canonique pour regrouper les réponses identiques (ordre des paires et des cases cochées ignoré)."""
    rep = (rep or "").strip()
    el = elements(rep)
    if el is not None and not rep.startswith("{") and not re.match(r"^(drop zone|zone)", rep, re.I):
        return "; ".join(sorted(f"{a} -> {b}" for a, b in el))
    if ";" in rep and "->" not in rep and "{" not in rep:
        return "; ".join(sorted(x.strip() for x in rep.split(";")))
    return rep


def cases(rep):
    """Renvoie l'ensemble des cases cochées d'une réponse de QCM à plusieurs réponses (séparées par ``;``)."""
    return {x.strip() for x in (rep or "").split(";") if x.strip()}


# ------------------------------------------------------------------ analyse
def choisir_tentatives(tent, mode):
    """Garde les tentatives terminées et, sauf en mode ``"toutes"``, une seule par étudiant.

    ``mode`` : ``"toutes"``, ``"premiere"``, ``"derniere"`` ; toute autre valeur garde la meilleure note.
    Renvoie les tentatives dans l'ordre de lecture.
    """
    termines = [t for t in tent if cle_texte(t["etat"]) in ("finished", "termine", "terminee", "")]
    if mode == "toutes":
        return termines
    par = defaultdict(list)
    for t in termines:
        par[t["id"]].append(t)
    out = []
    for ts in par.values():
        ts.sort(key=lambda t: (t["date"] or datetime.min, t["rang"]))
        if mode == "premiere":
            out.append(ts[0])
        elif mode == "derniere":
            out.append(ts[-1])
        else:
            out.append(max(ts, key=lambda t: (t["note"] if t["note"] is not None else -1)))
    return sorted(out, key=lambda t: t["rang"])


def analyser(tent, banque, avert):
    """Calcule les statistiques par question à partir des tentatives retenues.

    Identifie chaque question (par la banque, sinon par le début de son texte, sinon par sa position),
    puis calcule réussite, discrimination item-reste, répartition des réponses, alertes et détail des
    réponses composées. Renvoie ``(questions, reponses, elems, obs, infos)`` ; ``obs`` et ``infos`` sont
    les observations et informations par question, reprises par les autres analyses.
    """
    noms = {}                 # tronc -> nom affiché
    obs = defaultdict(list)   # nom -> [{fraction, reste, reponse, bonne, a_corriger, tentative}]
    infos = {}
    for t in tent:
        notees = [d for d in t["slots"].values() if d.get("note") is not None and d.get("max")]
        tot = sum(d["note"] for d in notees); tmax = sum(d["max"] for d in notees)
        for s, d in sorted(t["slots"].items()):
            resume = d.get("question")
            if resume:
                q = identifier(resume, banque) if banque else None
                nom = q["nom"] if q else (noms.setdefault(tronc(resume), tronc(resume)[:80]))
            else:
                q, nom = None, f"Position {s}"
            infos.setdefault(nom, {"banque": q, "resume": resume or "", "positions": set(), "bonne": Counter()})
            infos[nom]["positions"].add(s)
            if d.get("bonne"):
                infos[nom]["bonne"][d["bonne"]] += 1
            if d.get("note") is not None and d.get("max"):
                f = d["note"] / d["max"]
                reste = (tot - d["note"]) / (tmax - d["max"]) if tmax - d["max"] > 0 and not t["a_corriger"] else None
            elif d.get("reponse") is not None and d.get("bonne") and not d.get("a_corriger") and d.get("bonne") != "-":
                f, reste = (1.0 if forme(d["reponse"]).casefold() == forme(d["bonne"]).casefold() else 0.0), None
            else:
                f, reste = None, None
            obs[nom].append({"f": f, "reste": reste, "rep": d.get("reponse", ""), "bonne": d.get("bonne", ""),
                             "a_corriger": bool(d.get("a_corriger")), "t": t})
    if not banque and any(i["resume"] for i in infos.values()):
        avert.append("sans export XML des questions : questions nommées par le début de leur texte")
    if not any(i["resume"] for i in infos.values()):
        avert.append("pas de texte de question dans l'export « Réponses » : statistiques par position "
                     "(fausses si le test tire des questions au hasard)")

    questions, reponses, elems = [], [], []
    for nom, L in obs.items():
        info = infos[nom]
        fr = [o["f"] for o in L if o["f"] is not None]
        paires = [(o["f"], o["reste"]) for o in L if o["f"] is not None and o["reste"] is not None]
        r = pearson([a for a, _ in paires], [b for _, b in paires])
        bonne = info["bonne"].most_common(1)[0][0] if info["bonne"] else ""
        q = info["banque"]
        typ = q["type"] if q else ""
        # répartition des réponses
        groupes = defaultdict(list)
        for o in L:
            groupes[forme(o["rep"]).casefold()].append(o)
        rep_lignes = []
        for g, os_ in groupes.items():
            fs = [o["f"] for o in os_ if o["f"] is not None]
            aff = Counter(o["rep"] for o in os_).most_common(1)[0][0]
            moy = statistics.fmean(fs) if fs else None
            rs = [o["reste"] for o in os_ if o["reste"] is not None]
            rep_lignes.append({"question": nom, "reponse": aff or "(sans réponse)", "n": len(os_), "part": len(os_) / len(L),
                               "fraction": moy, "juste": None if moy is None else (moy >= 0.999),
                               "a_corriger": sum(o["a_corriger"] for o in os_),
                               "score_reste": statistics.fmean(rs) if rs else None, "n_score": len(rs), "ecart_score": None,
                               "erreur": " ; ".join(dict.fromkeys(codes_erreur(os_[0]["rep"], info["banque"])))})
        rep_lignes.sort(key=lambda x: -x["n"])
        reponses += rep_lignes
        # alertes
        alertes = []
        n = len(fr)
        moy = statistics.fmean(fr) if fr else None
        if n < SEUILS["n_min"]:
            alertes.append(f"peu de données (n = {n})")
        k_opt = (len(q["options"]) if q and typ == "multichoice" and q["single"] and len(q["options"]) >= 2
                 else 2 if typ == "truefalse" else None)
        plancher = plancher_difficulte(k_opt)
        if moy is not None and n >= 3:
            if moy >= SEUILS["facile"]:
                alertes.append("très facile")
            elif moy <= plancher:
                alertes.append("très difficile" + (f" (sous {100 * plancher:.0f} % avec {k_opt} options : proche du hasard)"
                                                   if k_opt and plancher > SEUILS["difficile"] else ""))
        lect = ""
        if r is not None and len(paires) >= SEUILS["discrim_n_min"]:
            lect = lecture_discrimination(r, moy)
            prudence = "" if len(paires) >= 50 else f" (n = {len(paires)}, à confirmer)"
            if lect == "peu fiable":
                if r < SEUILS["discrim_faible"]:
                    alertes.append(f"discrimination peu fiable (r = {r:.2f}, réussite {100 * moy:.0f} % hors de 30-90 %) : "
                                   "ne pas conclure sur la discrimination")
            elif r < SEUILS["discrim_negative"]:
                alertes.append("discrimination négative : à revoir (corrigé, énoncé ambigu ?)" + prudence)
            elif r < SEUILS["discrim_faible"]:
                alertes.append("peu discriminante" + prudence)
            if prudence and lect != "peu fiable":
                lect += " (à confirmer)"
        fausses = [x for x in rep_lignes if x["juste"] is False]
        simple = typ not in ("essay", "matching", "ddimageortext", "ddmarker", "ddwtos", "gapselect", "multianswer") \
            and elements(bonne) is None and not (q and typ == "multichoice" and not q["single"]) and bonne != "-"
        if fausses and moy is not None and simple:
            top = fausses[0]
            justes = sum(x["n"] for x in rep_lignes if x["juste"])
            if top["n"] >= justes and len(L) >= SEUILS["n_min"]:
                alertes.append(f"réponse fausse {'plus' if top['n'] > justes else 'autant'} choisie que la bonne : "
                               f"« {abrege(top['reponse'], 40)} »")
        choix_unique = (typ in ("multichoice", "truefalse") and (not q or q["single"])) or (not typ and elements(bonne) is None and ";" not in bonne)
        # leurres : score moyen (reste du test) de ceux qui les choisissent, comparé à celui des bonnes réponses (attali2000)
        if choix_unique and simple and moy is not None:
            sj = [o["reste"] for o in L if o["f"] is not None and o["f"] >= 0.999 and o["reste"] is not None]
            mj = statistics.fmean(sj) if len(sj) >= SEUILS["leurre_n_score"] else None
            suspects = []
            for x in rep_lignes:
                if mj is not None and x["score_reste"] is not None:
                    x["ecart_score"] = x["score_reste"] - mj
                    if x["juste"] is False and x["n_score"] >= SEUILS["leurre_n_score"] and x["score_reste"] >= mj:
                        suspects.append(x)
            if suspects:
                alertes.append("leurre choisi par des étudiants aussi forts que ceux qui ont juste : "
                               + " ; ".join(f"« {abrege(x['reponse'], 30)} »" for x in suspects)
                               + " (clé fausse ou deuxième bonne réponse ?)")
        # leurres non fonctionnels : choisis par moins de 0,1 x (1 - réussite) des étudiants (raymond2018) ;
        # pas d'alerte si la question est très réussie ou s'il y a trop peu d'étudiants en échec
        if q and typ == "multichoice" and q["single"] and len(L) >= SEUILS["leurre_n_min"] and moy is not None:
            N = len(L)
            if moy <= SEUILS["facile"] and N * (1 - moy) >= SEUILS["leurre_echecs_min"]:
                seuil = SEUILS["leurre_facteur"] * (1 - moy)
                compte = Counter(forme(o["rep"]).casefold() for o in L)
                cle_b = forme(bonne).casefold()
                faibles = [(o, compte.get(o.casefold(), 0)) for o in q["options"]
                           if o.casefold() != cle_b and compte.get(o.casefold(), 0) / N < seuil]
                if faibles:
                    alertes.append(f"leurre non fonctionnel (choisi par moins de {100 * seuil:.0f} % des étudiants) : "
                                   + " ; ".join(f"« {abrege(x, 30)} » ({'jamais choisi' if c == 0 else f'{100 * c / N:.0f} %'})"
                                                for x, c in faibles))
        a_corr = sum(o["a_corriger"] for o in L)
        if a_corr:
            alertes.append(f"{a_corr} réponse(s) à corriger")
        questions.append({"question": nom, "type": typ, "positions": ", ".join(map(str, sorted(info["positions"]))),
                          "n": len(L), "n_notees": n, "facilite": moy, "ecart": statistics.pstdev(fr) if n > 1 else None,
                          "reussite": (sum(1 for f in fr if f >= 0.999) / n) if n else None,
                          "zero": (sum(1 for f in fr if f <= 1e-9) / n) if n else None,
                          "discrimination": r, "n_discrim": len(paires), "discrim_lecture": lect, "plancher": plancher,
                          "a_corriger": a_corr,
                          "fausse_frequente": f"{abrege(fausses[0]['reponse'], 60)} ({fausses[0]['part']:.0%})" if fausses else "",
                          "bonne": bonne, "alertes": " ; ".join(alertes), "texte": info["resume"][:300]})
        # éléments des réponses composées (paires, zones, trous, cases cochées)
        cpt = defaultdict(Counter)
        attendu = {}
        multi = [o for o in L if elements(o["bonne"]) is None and (";" in (o["bonne"] or "") or (q and typ == "multichoice" and not q["single"]))]
        toutes_cases = set().union(*(cases(o["rep"]) | cases(o["bonne"]) for o in multi)) if multi else set()
        if q and typ == "multichoice" and not q["single"]:
            toutes_cases |= set(q["options"])
        for o in L:
            el, bel = elements(o["rep"]), elements(o["bonne"])
            if el is not None and bel is not None:
                b = dict(bel)
                for a, v in el:
                    cpt[a][v] += 1
                    attendu[a] = b.get(a, "")
            elif o in multi:
                rc, bc = cases(o["rep"]), cases(o["bonne"])
                for x in sorted(toutes_cases):
                    cpt[x]["cochée" if x in rc else "non cochée"] += 1
                    attendu[x] = "cochée" if x in bc else "non cochée"
        pieges = []
        for a, c in cpt.items():
            tot = sum(c.values())
            for v, k in c.most_common():
                elems.append({"question": nom, "element": a, "valeur": v, "n": k, "part": k / tot, "juste": v == attendu.get(a)})
            faux = [(v, k) for v, k in c.most_common() if v != attendu.get(a)]
            if faux and tot >= SEUILS["n_min"] and faux[0][1] >= c.get(attendu.get(a), 0):
                plus_ = "plus" if faux[0][1] > c.get(attendu.get(a), 0) else "autant"
                pieges.append(f"{a} : « {abrege(faux[0][0], 30)} » {plus_} choisi que la bonne réponse ({faux[0][1] / tot:.0%})")
        if pieges:
            questions[-1]["alertes"] = " ; ".join(x for x in [questions[-1]["alertes"]] + pieges if x)
    questions.sort(key=lambda x: x["question"])
    return questions, reponses, elems, obs, infos


def indicateurs(tent):
    """Calcule les indicateurs du test comme Moodle, sur les tentatives entièrement notées.

    Moyenne, médiane, écart-type (échantillon), asymétrie, aplatissement, cohérence interne (alpha de
    Cronbach sur les positions), alpha ramené à 50 questions, ratio d'erreur, erreur type, en % de la note
    maximale. Renvoie ``{}`` s'il y a moins de 4 tentatives.
    """
    ok = [t for t in tent if not t["a_corriger"] and t["slots"] and all(d.get("note") is not None for d in t["slots"].values())]
    if len(ok) < 4:
        return {}
    nmax = ok[0]["note_max"] or sum(d.get("max") or 0 for d in ok[0]["slots"].values()) or 1
    x = [sum(d["note"] for d in t["slots"].values()) for t in ok]
    n, m = len(x), statistics.fmean(x)
    s2 = sum((v - m) ** 2 for v in x) / n; s3 = sum((v - m) ** 3 for v in x) / n; s4 = sum((v - m) ** 4 for v in x) / n
    k2 = n * s2 / (n - 1); k3 = n * n * s3 / ((n - 1) * (n - 2)); k4 = n * n * ((n + 1) * s4 - 3 * (n - 1) * s2 * s2) / ((n - 1) * (n - 2) * (n - 3))
    out = {"n": n, "moyenne": 100 * m / nmax, "mediane": 100 * statistics.median(x) / nmax, "ecart": 100 * math.sqrt(k2) / nmax,
           "asymetrie": k3 / k2 ** 1.5 if k2 else None, "aplatissement": k4 / k2 ** 2 if k2 else None}
    pos = sorted(set().union(*(t["slots"] for t in ok)))
    if len(pos) > 1 and all(set(t["slots"]) == set(pos) for t in ok) and statistics.pvariance(x) > 0:
        cols = [[t["slots"][k]["note"] for t in ok] for k in pos]
        alpha = alpha_cronbach(cols)
        out["coherence"] = 100 * alpha
        out["k"] = len(pos)
        rs = [pearson(cols[i], cols[j]) for i in range(len(cols)) for j in range(i + 1, len(cols))]
        rs = [v for v in rs if v is not None]
        out["r_moyen"] = statistics.fmean(rs) if rs else None
        a50 = alpha_ramene(alpha, len(pos))
        out["alpha50"] = None if a50 is None else 100 * a50
        if alpha < 1:
            out["ratio_erreur"] = 100 * math.sqrt(1 - alpha)
            out["erreur_type"] = out["ratio_erreur"] * out["ecart"] / 100
    return out


def alpha_par_tag(obs, infos, n_min=10):
    """Calcule l'alpha de Cronbach par tag (au moins 3 questions), sur les tentatives notées à toutes les questions du tag.

    Renvoie ``[(tag, alpha, k, n)]`` ; ``alpha`` vaut ``None`` si moins de ``n_min`` tentatives contiennent toutes
    les questions (tirage au hasard). Les tags portés par presque toutes les questions sont ignorés.
    """
    membres = defaultdict(set)
    for nom, info in infos.items():
        for tg in (info["banque"] or {}).get("tags", []):
            membres[tg].add(nom)
    nq = len([1 for i in infos.values() if i["banque"]])
    out = []
    for tg, qs in sorted(membres.items()):
        if len(qs) < 3 or (nq >= 3 and len(qs) >= 0.9 * nq):
            continue
        notes = defaultdict(dict)
        for nom in qs:
            for o in obs[nom]:
                if o["f"] is not None:
                    notes[id(o["t"])][nom] = o["f"]
        lignes = [d for d in notes.values() if len(d) == len(qs)]
        qs_ = sorted(qs)
        a = alpha_cronbach([[d[q] for d in lignes] for q in qs_]) if len(lignes) >= n_min else None
        out.append((tg, a, len(qs), len(lignes)))
    return out


def etudiants(tent_toutes):
    """Renvoie une ligne par étudiant : notes (première, dernière, meilleure, moyenne), durée médiane et remarques.

    Signale les tentatives très rapides et faibles (réponses au hasard ?) et les tentatives à corriger.
    Les lignes sont triées par nom puis prénom.
    """
    par = defaultdict(list)
    for t in tent_toutes:
        par[t["id"]].append(t)
    durees = [t["duree"] for t in tent_toutes if t["duree"]]
    med = statistics.median(durees) if durees else None
    notes = [t["note"] for t in tent_toutes if t["note"] is not None]
    medn = statistics.median(notes) if notes else None
    out = []
    for ident, ts in par.items():
        ts.sort(key=lambda t: (t["date"] or datetime.min, t["rang"]))
        nt = [t["note"] for t in ts if t["note"] is not None]
        rem = []
        if med and any(t["duree"] and t["duree"] < 0.33 * med and (t["note"] or 0) < (medn or 0) for t in ts):
            rem.append("tentative très rapide et faible : réponses au hasard ?")
        acorr = sum(t["a_corriger"] for t in ts)
        if acorr:
            rem.append(f"{acorr} tentative(s) à corriger")
        out.append({"nom": ts[0]["nom"], "prenom": ts[0]["prenom"], "email": ts[0]["email"], "groupe": ts[0]["groupe"],
                    "test": ", ".join(sorted({t["test"] for t in ts})), "tentatives": len(ts),
                    "premiere": ts[0]["note"], "derniere": ts[-1]["note"], "meilleure": max(nt) if nt else None,
                    "moyenne": statistics.fmean(nt) if nt else None, "note_max": ts[0]["note_max"],
                    "duree": statistics.median([t["duree"] for t in ts if t["duree"]]) if any(t["duree"] for t in ts) else None,
                    "a_corriger": acorr, "remarques": " ; ".join(rem)})
    return sorted(out, key=lambda x: (x["nom"].lower(), x["prenom"].lower()))


# ------------------------------------------------------------------ classeur
def ecrire(sortie: Path, synth, questions, reponses, elems, etus, tent, couleur=COULEUR_PRINCIPALE, plus=None):
    """Écrit le classeur du bilan (XLSX) dans ``sortie``.

    ``synth`` : ``{"lignes": [(titre, texte)], "histo": [(classe, effectif)]}`` pour la feuille Synthèse ;
    ``plus`` : feuilles facultatives (``revoir``, ``equite``, ``retention``, ``erreurs``, ``groupes``,
    ``regroupements``) ; ``couleur`` : couleur des en-têtes.
    """
    import openpyxl
    from openpyxl.chart import BarChart, Reference
    from openpyxl.styles import Alignment, Font, PatternFill
    from openpyxl.utils import get_column_letter
    wb = openpyxl.Workbook()
    tete = PatternFill("solid", fgColor=couleur); blanc = Font(color="FFFFFF", bold=True)
    alerte = PatternFill("solid", fgColor="FDECEC"); vert = PatternFill("solid", fgColor="E8F5E9")

    def feuille(titre, cols, lignes, largeurs=None, alertes_col=None, juste_col=None):
        ws = wb.create_sheet(titre)
        ws.append([c[0] for c in cols])
        for c in ws[1]:
            c.fill, c.font, c.alignment = tete, blanc, Alignment(wrap_text=True, vertical="center")
        for l in lignes:
            ws.append([l.get(c[1]) for c in cols])
        for j, c in enumerate(cols, 1):
            ws.column_dimensions[get_column_letter(j)].width = (largeurs or {}).get(c[1], 14)
            fmt = c[2] if len(c) > 2 else None
            if fmt:
                for (cell,) in ws.iter_rows(min_row=2, min_col=j, max_col=j):
                    cell.number_format = fmt
        for row in ws.iter_rows(min_row=2):
            for cell in row:
                cell.alignment = Alignment(wrap_text=True, vertical="top")
            if alertes_col is not None and row[alertes_col].value:
                for cell in row:
                    cell.fill = alerte
            if juste_col is not None and row[juste_col].value is True:
                row[juste_col].fill = vert
        ws.freeze_panes = "B2"
        ws.auto_filter.ref = ws.dimensions
        return ws

    ws = wb.active; ws.title = "Synthèse"
    ws.column_dimensions["A"].width = 38; ws.column_dimensions["B"].width = 90
    for k, v in synth["lignes"]:
        ws.append([k, v])
        ws.cell(ws.max_row, 1).font = Font(bold=True)
        ws.cell(ws.max_row, 2).alignment = Alignment(wrap_text=True, vertical="top")
    ws.cell(1, 1).font = Font(bold=True, size=14, color=couleur)
    if synth["histo"]:
        d = ws.max_row + 2
        ws.cell(d, 1, "Répartition des notes"); ws.cell(d, 2, "Tentatives")
        for i, (lab, n) in enumerate(synth["histo"], 1):
            ws.cell(d + i, 1, lab); ws.cell(d + i, 2, n)
        ch = BarChart(); ch.title = "Répartition des notes"; ch.legend = None; ch.height, ch.width = 7, 16
        ch.add_data(Reference(ws, min_col=2, min_row=d, max_row=d + len(synth["histo"])), titles_from_data=True)
        ch.set_categories(Reference(ws, min_col=1, min_row=d + 1, max_row=d + len(synth["histo"])))
        ws.add_chart(ch, f"D{d}")

    feuille("Questions", [("Question", "question"), ("Type", "type"), ("Séance", "seance"), ("Bloc", "bloc"),
                          ("Alertes", "alertes"), ("Tirages", "n"),
                          ("Notées", "n_notees"), ("Réussite moyenne", "facilite", "0%"), ("Entièrement juste", "reussite", "0%"),
                          ("Nul", "zero", "0%"), ("Discrimination (r)", "discrimination", "0.00"), ("Lecture de r", "discrim_lecture"),
                          ("n discrimination", "n_discrim"), ("À corriger", "a_corriger"), ("Réponse fausse la plus fréquente", "fausse_frequente"),
                          ("Bonne réponse", "bonne"), ("Positions", "positions"), ("Texte (Moodle)", "texte")],
            questions, {"question": 28, "alertes": 42, "fausse_frequente": 34, "bonne": 30, "texte": 60}, alertes_col=4)
    plus = plus or {}
    if plus.get("revoir") is not None:
        feuille("À revoir", [("Rang", "rang"), ("Question", "question"), ("Type", "type"), ("Pourquoi", "raisons"),
                             ("Sur la question", "sur_question"), ("En cours", "en_cours"), ("Priorité", "priorite"),
                             ("Réussite", "reussite", "0%"), ("Discrimination (r)", "discrimination", "0.00"), ("Réponses", "n"),
                             ("Confiance", "confiance"), ("Réponse fausse la plus fréquente", "fausse")],
                plus["revoir"], {"question": 26, "raisons": 34, "sur_question": 46, "en_cours": 46, "fausse": 30})
    if plus.get("equite"):
        feuille("Tirage", [("Catégorie", "categorie"), ("Séance", "seance"), ("Questions tirées", "questions"),
                           ("Réussite la plus basse", "min", "0%"), ("Question", "q_min"), ("Réussite la plus haute", "max", "0%"),
                           ("Question ", "q_max"), ("Écart", "ecart", "0%"), ("Alerte", "alerte")],
                plus["equite"], {"categorie": 30, "q_min": 26, "q_max": 26, "alerte": 36})
    if plus.get("retention"):
        feuille("Rétention", [("Question", "question"), ("Séance", "seance"), ("Réussite le jour de la séance", "reussite_seance", "0%"),
                              ("Réponses", "n_seance"), ("Réussite en rappel", "reussite_rappel", "0%"), ("Réponses ", "n_rappel"),
                              ("Écart", "ecart", "+0%;-0%;0%")],
                plus["retention"], {"question": 28})
    if plus.get("erreurs"):
        feuille("Par erreur", [("Erreur type", "erreur"), ("Questions", "n_questions"), ("Réponses", "exposees"),
                               ("Choisie", "choix"), ("Part des réponses", "taux", "0%"), ("Étudiants", "etudiants"),
                               ("Part des étudiants", "part_etudiants", "0%"), ("Étudiants, sur au moins 2 questions", "repetee"),
                               ("Questions qui la visent", "questions")],
                plus["erreurs"], {"erreur": 30, "questions": 60})
    if plus.get("groupes"):
        feuille("Groupes", [("Groupe", "groupe"), ("Étudiants", "n"), ("Moyenne /20", "moyenne", "0.0"), ("Médiane /20", "mediane", "0.0"),
                            ("Écart-type", "ecart", "0.0"), ("Min", "min", "0.0"), ("Max", "max", "0.0"), ("≥ 10 /20", "reussite10", "0%")],
                plus["groupes"])
    noms = {"tag": "Par tag", "type": "Par type", "categorie": "Par catégorie"}
    for sorte, lignes in (plus.get("regroupements") or {}).items():
        if not lignes:
            continue
        gs = list(lignes[0]["groupes"])
        rows = []
        for l in lignes:
            d = {"nom": l["nom"], "nq": l["n_questions"], "n": l["n"], "promo": l["promo"],
                 "detail": "\n".join(f"{q} : {v:.0%} (n = {n})" for q, v, n in l["detail"])}
            d.update({f"g_{g}": l["groupes"].get(g) for g in gs})
            rows.append(d)
        feuille(noms[sorte], [(noms[sorte][4:].capitalize(), "nom"), ("Questions", "nq"), ("Réponses", "n"),
                              ("Réussite promotion", "promo", "0%")] + [(f"Réussite {g}", f"g_{g}", "0%") for g in gs]
                + [("Détail par question (de la moins à la plus réussie)", "detail")], rows, {"nom": 24, "detail": 60})
    feuille("Réponses", [("Question", "question"), ("Réponse", "reponse"), ("Nombre", "n"), ("Part", "part", "0%"),
                         ("Note moyenne obtenue", "fraction", "0%"), ("Juste", "juste"), ("À corriger", "a_corriger"),
                         ("Score moyen au reste du test", "score_reste", "0%"),
                         ("Écart avec les bonnes réponses", "ecart_score", "+0%;-0%;0%"), ("Erreur type", "erreur")],
            reponses, {"question": 28, "reponse": 70}, juste_col=5)
    feuille("Éléments", [("Question", "question"), ("Élément (paire, zone, trou, case)", "element"), ("Réponse donnée", "valeur"),
                         ("Nombre", "n"), ("Part", "part", "0%"), ("Juste", "juste")],
            elems, {"question": 28, "element": 34, "valeur": 40}, juste_col=5)
    feuille("Étudiants", [("Nom", "nom"), ("Prénom", "prenom"), ("Courriel", "email"), ("Groupe", "groupe"), ("Test", "test"), ("Tentatives", "tentatives"),
                          ("Note max", "note_max"), ("Première", "premiere", "0.00"), ("Dernière", "derniere", "0.00"),
                          ("Meilleure", "meilleure", "0.00"), ("Moyenne", "moyenne", "0.00"), ("Durée médiane (s)", "duree"),
                          ("À corriger", "a_corriger"), ("Remarques", "remarques")],
            etus, {"email": 26, "remarques": 46}, alertes_col=13)
    nmax = max((max(t["slots"]) for t in tent if t["slots"]), default=0)
    lignes = []
    for t in tent:
        l = {"nom": t["nom"], "prenom": t["prenom"], "groupe": t["groupe"], "test": t["test"], "debut": t["debut"], "duree": t["duree"], "note": t["note"],
             "a_corriger": "oui" if t["a_corriger"] else ""}
        for s in range(1, nmax + 1):
            d = t["slots"].get(s, {})
            l[f"q{s}"] = d.get("question", "")[:60]; l[f"r{s}"] = d.get("reponse", "")
            l[f"n{s}"] = d.get("note") if d.get("note") is not None else ("à corriger" if d.get("a_corriger") else None)
        lignes.append(l)
    cols = [("Nom", "nom"), ("Prénom", "prenom"), ("Groupe", "groupe"), ("Test", "test"), ("Début", "debut"), ("Durée (s)", "duree"), ("Note", "note"), ("À corriger", "a_corriger")]
    for s in range(1, nmax + 1):
        cols += [(f"Question {s}", f"q{s}"), (f"Réponse {s}", f"r{s}"), (f"Note {s}", f"n{s}")]
    feuille("Tentatives", cols, lignes, {**{f"q{s}": 30 for s in range(1, nmax + 1)}, **{f"r{s}": 30 for s in range(1, nmax + 1)}, "debut": 22})
    wb.save(sortie)


# ------------------------------------------------------------------ commande
def trouver_fichiers(cibles):
    """Sépare les fichiers donnés (ou contenus dans les dossiers donnés) en exports et banques.

    Renvoie ``(exports, banques)`` : exports ``.csv`` / ``.xlsx`` (sauf fichiers temporaires et bilans
    déjà produits) ; banques ``.xml`` et ``*_banque.yaml``.
    """
    exports, xmls = [], []
    for c in cibles:
        p = Path(c)
        liste = sorted(p.iterdir()) if p.is_dir() else [p]
        for f in liste:
            if f.suffix.lower() in (".csv", ".xlsx") and not f.name.startswith(("~$", "bilan_")):
                exports.append(f)
            elif f.suffix.lower() == ".xml" or (f.suffix.lower() in (".yaml", ".yml") and f.stem.endswith("_banque")):
                xmls.append(f)
    return exports, xmls


def bilan(cibles, xml=None, mode="toutes", sortie=None, couleur=COULEUR_PRINCIPALE, roster=None, images=True, tirage=None):
    """Produit le bilan complet d'un test et renvoie le chemin du classeur.

    - ``cibles`` : dossiers ou fichiers d'exports Moodle ;
    - ``xml`` : banques de questions (XML ou YAML, fichiers ou dossiers), sinon celles trouvées dans ``cibles`` ;
    - ``mode`` : tentatives retenues (voir :func:`choisir_tentatives`) ;
    - ``roster`` : listes d'étudiants avec leur groupe ;
    - ``images`` : produire les graphiques pour les étudiants ;
    - ``tirage`` : mode de tirage déclaré dans le profil.

    Écrit ``bilan_<test>.xlsx`` (ou ``sortie``), la fiche du professeur ``…_fiche_prof.html`` et, si demandé,
    le dossier ``…_images``. Quitte le programme si aucun export ou aucune tentative n'est lu.
    """
    import bilan_sorties as BS
    exports, xmls = trouver_fichiers(cibles)
    if xml:
        xmls = [y for x in map(Path, xml) for y in (sorted([*x.glob("*.xml"), *x.glob("*_banque.yaml")]) if x.is_dir() else [x])]
    rosters = [Path(r) for r in (roster or [])] + [p for p in exports if BS.est_roster(p)]
    exports = [p for p in exports if p not in rosters]
    if not exports:
        raise SystemExit("Aucun export Moodle (.csv ou .xlsx) trouvé.")
    avert, moodle = [], {}
    tent_toutes = lire_exports(exports, avert, moodle)
    if not tent_toutes:
        raise SystemExit("Aucune tentative lue :\n - " + "\n - ".join(avert))
    BS.affecter_groupes(tent_toutes, BS.lire_roster(rosters, avert) if rosters else {}, avert)
    banque = lire_banque_xml([x for x in xmls if x.suffix.lower() == ".xml"])
    banque = completer_banque_yaml([x for x in xmls if x.suffix.lower() in (".yaml", ".yml")], banque)
    if banque:
        avert.append(f"banque : {len(banque)} question(s) lue(s) dans {', '.join(x.name for x in xmls)}")
    tent = choisir_tentatives(tent_toutes, mode)
    questions, reponses, elems, obs, infos = analyser(tent, banque, avert)
    etus = etudiants([t for t in tent_toutes if cle_texte(t["etat"]) in ("finished", "termine", "terminee", "")])
    notes = [t["note"] for t in tent if t["note"] is not None]
    nmax = next((t["note_max"] for t in tent if t["note_max"]), None)
    acorr = sum(t["a_corriger"] for t in tent)
    exclues = len(tent_toutes) - len([t for t in tent_toutes if cle_texte(t["etat"]) in ("finished", "termine", "terminee", "")])
    tests = sorted({t["test"] for t in tent_toutes})
    sans_groupe = sorted({t["test"][:-len(groupe_du_test(t["test"])) - 1] if groupe_du_test(t["test"]) else t["test"] for t in tent_toutes})
    nom_test = tests[0] if len(tests) == 1 else (sans_groupe[0] if len(sans_groupe) == 1 else " + ".join(tests))
    surv = [q for q in questions if q["alertes"] and not q["alertes"].startswith("peu de données") or
            (q["alertes"] and "à corriger" in q["alertes"])]
    L = [(f"Bilan du test « {nom_test} »", ""),
         ("Fichiers lus", "\n".join(avert)),
         ("Tentatives analysées", f"{len(tent)} (mode : {mode}) ; {len({t['id'] for t in tent})} étudiant(s)"
                                  + (f" ; {exclues} tentative(s) non terminée(s) écartée(s)" if exclues else "")),
         ("Tentatives à corriger", f"{acorr} (notes partielles : exclues du calcul de la discrimination)" if acorr else "aucune")]
    if notes:
        sur20 = (lambda v: f"{v:.2f} / {nmax:g}" + (f"  ({20 * v / nmax:.1f} / 20)" if nmax else "")) if nmax else (lambda v: f"{v:.2f}")
        L += [("Note moyenne", sur20(statistics.fmean(notes))), ("Note médiane", sur20(statistics.median(notes))),
              ("Écart-type", f"{statistics.stdev(notes):.2f}" if len(notes) > 1 else "-"),
              ("Note minimale / maximale", f"{min(notes):g} / {max(notes):g}")]
    ind = indicateurs(tent)
    if ind:
        def mdl(*cles):
            for c in cles:
                for h, v in moodle.items():
                    if cle_texte(h).startswith(c):
                        return f"   (Moodle : {v})"
            return ""
        pc = lambda v: "-" if v is None else f"{v:.2f} %"  # noqa: E731
        L += [("Indicateurs du test", f"sur {ind['n']} tentative(s) entièrement notée(s), en % de la note maximale, calculés comme Moodle"),
              ("  Moyenne", pc(ind["moyenne"]) + mdl("averagegradeofall", "moyennedesnotesdetoutes")),
              ("  Médiane", pc(ind["mediane"]) + mdl("mediangrade", "notemediane")),
              ("  Écart-type", pc(ind["ecart"]) + mdl("standarddeviation", "ecarttype")),
              ("  Asymétrie", "-" if ind["asymetrie"] is None else f"{ind['asymetrie']:.4f}" + mdl("scoredistributionskew", "asymetrie")),
              ("  Aplatissement", "-" if ind["aplatissement"] is None else f"{ind['aplatissement']:.4f}" + mdl("scoredistributionkurt", "aplatissement")),
              ("  Cohérence interne (alpha)", pc(ind.get("coherence")) + mdl("coefficientofinternal", "coefficientdecoherence")
               + ("  — négative : les positions ne mesurent pas la même chose (questions tirées au hasard, peu de tentatives)"
                  if (ind.get("coherence") or 0) < 0 else "")),
              ("  Questions par tentative", str(ind.get("k", "-"))
               + ("" if not ind.get("k") else
                  (lambda ref: f"  — alpha typique d'un test de connaissances de {ref} questions : {100 * ALPHA_ATTENDU[ref][0]:.0f} % "
                               f"(de {100 * ALPHA_ATTENDU[ref][1]:.0f} % à {100 * ALPHA_ATTENDU[ref][2]:.0f} % dans 90 % des tests "
                               "publiés, Edelsbrunner et al., 2025)")
                  (min(ALPHA_ATTENDU, key=lambda c: abs(math.log(c / ind["k"])))))),
              ("  Corrélation moyenne entre questions", "-" if ind.get("r_moyen") is None else f"{ind['r_moyen']:.2f}"),
              ("  Alpha ramené à 50 questions", pc(ind.get("alpha50")) + "  — pour comparer des tests de longueurs différentes"),
              ("  Ratio d'erreur", pc(ind.get("ratio_erreur")) + mdl("errorratio", "ratiodeserreurs", "tauxderreur")),
              ("  Erreur type", pc(ind.get("erreur_type")) + mdl("standarderror", "erreurtype", "erreurstandard"))]
    apt = alpha_par_tag(obs, infos)
    if apt:
        L.append(("  Alpha par thème (tag)", "\n".join(
            f"{tg} : {'non calculable (aucune tentative ne contient toutes ses questions)' if a is None else f'{100 * a:.0f} %'}"
            f" ({k} questions, {n} tentative(s) complète(s))" for tg, a, k, n in apt)))
    import tirage as TG
    tir = TG.analyser_tirage(obs, infos, tirage)
    for q in questions:
        s = tir["seance"].get(q["question"])
        q["seance"] = f"S{s:02d}" if s else ""
        q["bloc"] = tir["bloc"].get(q["question"], "")
    if tir["lignes"]:
        L.append(("Tirage des questions", "\n".join(tir["lignes"])))
    erreurs = par_erreur(obs, infos)
    if erreurs:
        L.append(("Erreurs types les plus fréquentes", "\n".join(
            f"{e['erreur']} : {100 * e['taux']:.0f} % des réponses aux {e['n_questions']} question(s) qui la visent"
            + (f" ; {e['repetee']} étudiant(s) la font sur au moins 2 questions" if e["repetee"] is not None else
               " (une seule question : à confirmer sur d'autres)") for e in erreurs[:5])))
    L += [("Questions à surveiller", "\n".join(f"{q['question']} : {q['alertes']}" for q in surv) or "aucune"),
          ("Lecture", "Réussite moyenne = note moyenne obtenue sur la question. Discrimination (r) = corrélation entre la note "
                      "de la question et la note du reste du test (question exclue) : au-dessus de 0,35 très bonne, de 0,15 à 0,35 "
                      "correcte, sous 0,15 faible, négative à revoir (Slepkov et al., 2021). Peu fiable quand la réussite est sous "
                      "30 % ou au-dessus de 90 %, et à confirmer sous une cinquantaine de réponses ; quand le test tire peu de "
                      "questions par tentative, le « reste du test » est court et r varie beaucoup. L'alpha (cohérence interne) "
                      "dépend du nombre de questions : c'est un repère, pas une note de qualité du test ; ne retirez pas une question "
                      "pertinente pour le faire monter. Toutes les alertes sont des points à vérifier, pas des verdicts.")]
    histo = []
    if notes and nmax:
        bornes = [nmax * k / 5 for k in range(6)]
        for k in range(5):
            n = sum(1 for v in notes if bornes[k] <= v < bornes[k + 1] or (k == 4 and v == nmax))
            histo.append((f"{bornes[k]:g} à {bornes[k + 1]:g}", n))
    groupes = sorted({t["groupe"] for t in tent if t["groupe"]})
    notes_e = BS.notes_par_etudiant(tent, mode)
    stats_g, par_groupe = BS.stats_groupes(notes_e)
    regr = BS.regroupements(obs, infos, groupes)
    revoir = BS.a_revoir(questions)
    base = re.sub(r"[^\w+-]+", "_", nom_test.replace(" + ", "_"))
    sortie = Path(sortie) if sortie else Path(cibles[0] if Path(cibles[0]).is_dir() else Path(cibles[0]).parent) / f"bilan_{base or 'test'}.xlsx"
    if sortie.suffix.lower() != ".xlsx":
        sortie = sortie.with_name(sortie.name + ".xlsx")
    imgs, msg_img = BS.images(sortie.with_name(sortie.stem + "_images"), nom_test, notes_e, par_groupe, regr, couleur, mode) if images else ([], "")
    if msg_img:
        avert.append(msg_img)
    L[1] = ("Fichiers lus", "\n".join(avert))
    ecrire(sortie, {"lignes": L, "histo": histo}, questions, reponses, elems, etus, tent, couleur,
           {"revoir": revoir, "groupes": stats_g, "regroupements": regr, "erreurs": erreurs,
            "equite": tir["equite"], "retention": tir["retention"]})
    fp = BS.fiche(sortie.with_name(sortie.stem + "_fiche_prof.html"), nom_test, L, stats_g, regr, revoir, imgs, couleur)
    print(f"OK : {sortie}")
    print(f"OK : {fp}")
    if imgs:
        print(f"OK : {len(imgs)} image(s) pour les étudiants dans {imgs[0].parent}")
    print(f"{len(tent)} tentative(s), {len(questions)} question(s) ; à surveiller : {len(surv)} ; à corriger : {acorr}")
    for a in avert:
        print("  -", a)
    return sortie
