"""QuizForge — promotion fictive pour tester le bilan (DiagForge).

    python scripts/quizforge/outils/promotion_fictive.py <export_reponses.csv> <questions.xml> [-n 60] [--fr] [-s dossier] [--graine 7]

Fabrique, au format exact d'un vrai export Moodle (« Notes » + « Réponses » avec texte de la question
et bonne réponse), les tentatives d'une promotion fictive sur la même banque de questions :
4 positions tirées au hasard parmi les questions, niveau des étudiants variable, et des cas connus
à retrouver dans le bilan (liste écrite dans verite.txt). --fr : en-têtes et nombres à la française.
Les textes des questions et des bonnes réponses sont repris de l'export réel fourni.
"""
import argparse
import csv
import math
import random
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import bilan  # noqa: E402

# Paramètres par question : b = difficulté, a = discrimination (modèle logistique), et cas plantés
PARAMS = {
    "Maillage fin":            {"b": -3.5, "a": 0.6},   # très facile
    "Unité fréquence":         {"b": 1.2, "a": 1.4},    # leurre « 2π √(k/m) » très attractif ; « k/m » jamais choisi
    "Conditions de Dirichlet": {"b": -0.3, "a": 0.0},   # ne discrimine pas (réussite indépendante du niveau)
    "Domaines":                {"b": 1.6, "a": 1.2},    # très difficile
    "Corps rigide":            {"b": 0.3, "a": 1.5},    # 8 copies laissées à corriger
    "Dommage Miner":           {"b": -0.5, "a": 1.6},   # erreur fréquente : rapport inversé (2)
    "Miner":                   {"b": -0.2, "a": 1.3},   # trou 3 : « 0 » au lieu de « 1 »
    "Vecteur contrainte":      {"b": 0.0, "a": 1.4},    # zone 2 : tenseur σ̲̲ au lieu de σ
    "Éléments SDOF":           {"b": -0.8, "a": 1.2},   # Masse -> Rigidité infinie
    "Condition naturelle":     {"b": -0.2, "a": 1.5},
}
VERITE = """Cas plantés à retrouver dans le bilan :
- Maillage fin : très facile (réussite ≈ 90 %).
- Unité fréquence : réponse fausse « 2π √(k/m) » plus choisie que la bonne ; leurre « k/m » jamais choisi.
- Conditions de Dirichlet : peu discriminante (réussite indépendante du niveau).
- Domaines : très difficile.
- Corps rigide : 8 copies laissées à corriger.
- Dommage Miner : erreur fréquente 2 (rapport inversé).
- Miner : trou 3, « 0 » souvent à la place de « 1 ».
- Vecteur contrainte : zone 2, tenseur σ̲̲ souvent à la place de σ.
- Éléments SDOF : Masse -> Rigidité infinie.
- Étudiants 59 et 60 : tentatives très rapides au hasard.
- Étudiants 01 à 10 : deux tentatives (la seconde meilleure).
"""
ESSAIS = ["Le modèle rigide ne prend pas en compte les déformations, donc pas les efforts intérieurs.",
          "Parce que la puissance des efforts intérieurs est nulle pour tout mouvement rigidifiant : elle ne dit rien des contraintes.",
          "Il faut des déformations pour avoir des contraintes.", "je ne sais pas", "Car le solide se déforme.",
          "Le modèle n'a pas de paramètre de matériau."]


def proba(theta, p):
    """Renvoie la probabilité de bonne réponse d'un étudiant de niveau ``theta`` (modèle logistique).

    ``p`` : paramètres de la question, ``{"b": difficulté, "a": discrimination}`` ; avec ``a`` nul,
    la probabilité ne dépend pas du niveau.
    """
    return 1 / (1 + math.exp(-p["a"] * (theta - p["b"]))) if p["a"] else 1 / (1 + math.exp(p["b"]))


def modeles(export, banque):
    """Relève dans l'export réel, pour chaque question de la banque, les couples ``(résumé Moodle, bonne réponse)`` observés.

    Renvoie ``{nom: {"b": question de la banque, "vus": [(résumé, bonne réponse), …]}}``.
    """
    out = {}
    for r in csv.DictReader(open(export, encoding="utf-8-sig")):
        for k in range(1, 50):
            q = r.get(f"Question {k}")
            if q is None:
                break
            b = bilan.identifier(q, banque)
            if b:
                out.setdefault(b["nom"], {"b": b, "vus": []})["vus"].append((q, r.get(f"Right answer {k}", "")))
    return out


def repondre(nom, q, bonne, resume, theta, rng, hasard):
    """Simule la réponse d'un étudiant de niveau ``theta`` à une question.

    Renvoie ``(réponse au format Moodle, fraction obtenue, à corriger ?)`` ; le troisième terme vaut
    toujours ``False`` ici (les copies à corriger sont choisies dans :func:`main`). Avec ``hasard`` vrai,
    l'étudiant répond au hasard.
    """
    p = PARAMS.get(nom, {"b": 0, "a": 1})
    ok = lambda: rng.random() < (0.3 if hasard else proba(theta, p))  # noqa: E731
    t = q["type"]
    if t == "truefalse":
        j = ok(); return (bonne if j else ("True" if bonne == "False" else "False")), float(j), False
    if t == "numerical":
        if ok():
            return bonne, 1.0, False
        return rng.choices(["2", "5000", "0.05", "0.55", "0.45"], [6, 1, 1, 1, 1])[0], 0.0, False
    if t == "shortanswer":
        if ok():
            return rng.choice([bonne, bonne, bonne.lower()]), 1.0, False
        return rng.choice(["Dirichlet", "Robin", "Fourier"]), 0.0, False
    if t == "essay":
        f = min(1.0, max(0.0, round(proba(theta, p) + rng.uniform(-0.25, 0.25), 1)))
        return rng.choice(ESSAIS), f, False
    if t == "multichoice" and q["single"]:
        if ok():
            return bonne, 1.0, False
        fausses = [o for o in q["options"] if o != bonne and o != "k/m"]
        poids = [8 if "2π √" in o else 1 for o in fausses]
        return rng.choices(fausses, poids)[0], 0.0, False
    if t == "multichoice":
        ordre = [x.strip() for x in resume.split("?:", 1)[1].split(";")] if "?:" in resume else q["options"]
        justes = bilan.cases(bonne)
        if ok():
            choix = justes
        else:
            choix = set(justes)
            if rng.random() < 0.6:
                choix.add("Flux imposé")
            else:
                choix.discard(rng.choice(sorted(justes)))
        f = max(0.0, 0.5 * len(choix & justes) - 0.5 * len(choix - justes))
        return "; ".join(o for o in ordre if o in choix), f, False
    # réponses composées : appariement, zones, trous
    el = bilan.elements(bonne) or []
    mauvais = {"Masse": "Rigidité infinie", "Ressort": "Inertie", "Amortisseur": "Élasticité",
               "trou 1": "σ" if nom == "Miner" else "limitée", "trou 2": "n" if nom == "Miner" else "polycyclique",
               "trou 3": "0"}
    rep, justes = [], 0
    for a, v in el:
        pa = proba(theta, p) if not hasard else 0.4
        if a == "trou 3" and nom == "Miner":
            pa *= 0.6
        if t == "ddimageortext" and a.lower().endswith("2"):
            pa *= 0.6
        if rng.random() < pa:
            rep.append((a, v)); justes += 1
        else:
            if t == "ddimageortext":
                w = r"5. $\underline{\underline{\sigma}}$" if a.lower().endswith("2") else rng.choice([r"6. $\varepsilon$", r"2. $\sigma$"])
            else:
                w = mauvais.get(a, v)
            rep.append((a, w)); justes += (w == v)
    if t == "matching":
        txt = "; ".join(f"{a} -> {v}" for a, v in rep)
    elif t == "ddimageortext":
        txt = " ".join(f"{a} -> {{{v}}}" for a, v in rep)
    else:
        txt = " ".join(f"{{{v}}}" for _, v in rep)
    return txt, (justes / len(el) if el else 0.0), False


def fr_nombre(x, fr):
    """Écrit un nombre avec deux décimales, avec une virgule si ``fr`` est vrai."""
    s = f"{x:.2f}"
    return s.replace(".", ",") if fr else s


def fr_date(d, fr):
    """Écrit une date comme Moodle : « 2 novembre 2026, 10:05 » si ``fr`` est vrai, sinon « 2 November 2026  10:05 AM »."""
    mois = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
    if fr:
        return f"{d.day} {mois[d.month - 1]} {d.year}, {d:%H:%M}"
    return f"{d.day} {d:%B %Y}  {d.hour % 12 or 12}:{d:%M} {'AM' if d.hour < 12 else 'PM'}"


def fr_duree(s, fr):
    """Écrit une durée en secondes comme Moodle : « 3 min 20 s » si ``fr`` est vrai, sinon « 3 mins 20 secs »."""
    m, s = divmod(int(s), 60)
    if fr:
        return (f"{m} min {s} s" if m else f"{s} s")
    return (f"{m} min{'s' if m > 1 else ''} {s} secs" if m else f"{s} secs")


def main():
    """Lit les arguments, fabrique les exports de la promotion fictive et les écrit dans le dossier de sortie.

    Écrit les fichiers CSV « notes » et « réponses » (un couple par groupe avec ``--groupes``, plus
    ``roster.csv``) et ``verite.txt``, la liste des cas plantés.
    """
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("export"); ap.add_argument("xml")
    ap.add_argument("-n", type=int, default=60); ap.add_argument("--fr", action="store_true")
    ap.add_argument("-s", "--sortie", default="promotion_fictive"); ap.add_argument("--graine", type=int, default=7)
    ap.add_argument("-g", "--groupes", default="", help="ex. SMA;SMB : un test par groupe (Cours-Quizz1_SMA-…) + roster.csv ; "
                    "le dernier groupe est plus faible sur les textes à trous")
    a = ap.parse_args()
    rng = random.Random(a.graine)
    banque = bilan.lire_banque([Path(a.xml)])
    mod = modeles(a.export, banque)
    noms = sorted(mod)
    sortie = Path(a.sortie); sortie.mkdir(parents=True, exist_ok=True)
    fr = a.fr
    E = (["Nom", "Prénom", "Adresse de courriel", "État", "Commencé le", "Terminé", "Temps utilisé", "Note/4,00"] if fr else
         ["Last name", "First name", "Email address", "Status", "Started", "Completed", "Duration", "Grade/4.00"])
    notes = [E + [f"Q. {k} /{'1,00' if fr else '1.00'}" for k in range(1, 5)]]
    reps = [E + sum(([f"Question {k}", f"Réponse {k}" if fr else f"Response {k}", f"Bonne réponse {k}" if fr else f"Right answer {k}"]
                     for k in range(1, 5)), [])]
    a_corriger = 8
    groupes = [g for g in a.groupes.replace(",", ";").split(";") if g.strip()]
    par_groupe = {g: ([notes[0]], [reps[0]]) for g in groupes}
    roster = [["Nom", "Prénom", "Courriel", "Groupe"]]
    debut0 = datetime(2026, 11, 2, 10, 0)
    for i in range(1, a.n + 1):
        theta = rng.gauss(0, 1)
        hasard = i > a.n - 2
        grp = groupes[(i - 1) % len(groupes)] if groupes else ""
        if grp:
            roster.append([f"Étudiant{i:02d}", f"Prénom{i:02d}", f"etudiant{i:02d}@exemple.fr", grp])
        for essai in range(2 if i <= 10 else 1):
            th = theta + (0.8 if essai else 0)
            d0 = debut0 + timedelta(minutes=rng.randint(0, 90) + 120 * essai, seconds=rng.randint(0, 59))
            duree = rng.randint(35, 70) if hasard else rng.randint(180, 560)
            tirage = rng.sample(noms, 4)
            marks, cellr, pending = [], [], False
            for nom in tirage:
                q = mod[nom]["b"]
                resume, bonne = rng.choice(mod[nom]["vus"])
                faible = grp and grp == groupes[-1] and q["type"] in ("ddwtos", "gapselect")
                txt, f, _ = repondre(nom, q, bonne, resume, th - (1.2 if faible else 0), rng, hasard)
                if q["type"] == "essay" and a_corriger > 0 and rng.random() < 0.5:
                    a_corriger -= 1
                    marks.append(None); pending = True
                else:
                    marks.append(round(f, 2))
                cellr += [resume, txt, bonne]
            base = [f"Étudiant{i:02d}", f"Prénom{i:02d}", f"etudiant{i:02d}@exemple.fr", "Terminé" if fr else "Finished",
                    fr_date(d0, fr), fr_date(d0 + timedelta(seconds=duree), fr), fr_duree(duree, fr),
                    ("Pas encore évaluée" if fr else "Not yet graded") if pending else fr_nombre(sum(marks), fr)]
            ln = base + [("Évaluation requise" if fr else "Requires grading") if m is None else fr_nombre(m, fr) for m in marks]
            (par_groupe[grp][0] if grp else notes).append(ln)
            (par_groupe[grp][1] if grp else reps).append(base + cellr)
    if groupes:
        for g, (n_, r_) in par_groupe.items():
            for nom_f, lignes in (("notes" if fr else "grades", n_), ("reponses" if fr else "responses", r_)):
                with open(sortie / f"Cours-Quizz1_{g}-{nom_f}.csv", "w", encoding="utf-8-sig", newline="") as f:
                    csv.writer(f).writerows(lignes)
        with open(sortie / "roster.csv", "w", encoding="utf-8-sig", newline="") as f:
            csv.writer(f).writerows(roster)
        (sortie / "verite.txt").write_text(VERITE + f"- Groupe {groupes[-1]} : plus faible sur les textes à trous (Miner, Domaines).\n", encoding="utf-8")
        print(f"OK : {sortie} ({a.n} étudiants, groupes {', '.join(groupes)}, roster.csv)")
        return
    moy = lambda c: fr_nombre(sum(float(str(l[c]).replace(",", ".")) for l in notes[1:] if bilan.nombre(l[c]) is not None)  # noqa: E731
                              / max(1, sum(1 for l in notes[1:] if bilan.nombre(l[c]) is not None)), fr)
    notes.append(["Moyenne générale" if fr else "Overall average", "", "", "", "", "", ""] + [moy(c) for c in range(7, 12)])
    for nom_f, lignes in (("notes" if fr else "grades", notes), ("reponses" if fr else "responses", reps)):
        with open(sortie / f"Promotion fictive-test-{nom_f}.csv", "w", encoding="utf-8-sig", newline="") as f:
            csv.writer(f, quoting=csv.QUOTE_MINIMAL).writerows(lignes)
    (sortie / "verite.txt").write_text(VERITE, encoding="utf-8")
    print(f"OK : {sortie} ({len(notes) - 2} tentatives, {a.n} étudiants){' — format français' if fr else ''}")


if __name__ == "__main__":
    main()
