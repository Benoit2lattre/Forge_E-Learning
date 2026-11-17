"""DiagForge — tirage des questions d'un quiz : mode observé, équité entre questions tirées, rétention des rappels.

Modes (bloc ``quiz`` du profil QuizForge, voir ``outils/quizforge/README.md``) :

- ``commun`` : toutes les tentatives d'un même test contiennent les mêmes questions ;
- ``partiel`` : chaque tentative tire k questions sur N dans chaque catégorie ;
- ``mixte`` : questions de la séance communes à tous, rappels des séances précédentes tirés.

La séance d'une question vient de son tag ``S01``, ``S02``… (QuizForge, colonne Séance) ou du champ ``seance`` de la banque YAML.
Les seuils d'équité sont des règles d'usage (niveau D) : aucune fiche de la bibliographie ne porte sur l'équité entre
versions tirées. La rétention compare, pour une même question, la réussite le jour de sa séance et la réussite en rappel
(pratique de récupération espacée : ``reference/A_tests_retroaction/yang2021.md``, ``murray2025.md``).
"""
import re
import statistics
from collections import defaultdict

ECART_EQUITE = 0.30   # écart de réussite entre questions d'une même catégorie tirée au-delà duquel on alerte
N_MIN = 10            # réponses minimales par question pour comparer


def seance_question(q) -> int | None:
    """Renvoie le numéro de séance d'une question de la banque, ou ``None``.

    Le champ entier ``seance`` l'emporte ; sinon le premier tag de la forme ``S01``, ``s2``… (1 à 3 chiffres).
    """
    if not q:
        return None
    if isinstance(q.get("seance"), int):
        return q["seance"]
    for tg in q.get("tags", []):
        m = re.fullmatch(r"[Ss](\d{1,3})", str(tg).strip())
        if m:
            return int(m.group(1))
    return None


def test_de_base(test: str) -> str:
    """Retire le suffixe de groupe d'un nom de test : « Quizz1_SMA » → « Quizz1 » (même test passé par plusieurs groupes).

    Le suffixe retiré compte 1 à 8 caractères alphanumériques et n'est pas uniquement numérique.
    """
    if "_" in test:
        base, suf = test.rsplit("_", 1)
        if 1 <= len(suf) <= 8 and suf.isalnum() and not suf.isdigit():
            return base
    return test


def _reussite(L):
    """Renvoie ``(réussite moyenne, nombre de réponses notées)`` d'une liste d'observations, ou ``(None, 0)``."""
    fr = [o["f"] for o in L if o["f"] is not None]
    return (statistics.fmean(fr), len(fr)) if fr else (None, 0)


def analyser_tirage(obs, infos, declare=None):
    """Analyse le tirage des questions : mode observé par test, équité entre questions tirées, rétention.

    ``obs`` : observations par question ; ``infos`` : informations par question (dont ``banque``) ;
    ``declare`` : mode déclaré dans le profil, comparé au mode observé.

    Renvoie un dictionnaire ``{"tests": [...], "equite": [...], "retention": [...], "lignes": [lignes de synthèse],
    "bloc": {nom: bloc}, "seance": {nom: séance}}``.
    """
    seance = {nom: seance_question(i["banque"]) for nom, i in infos.items()}
    # questions vues par chaque tentative, regroupées par test (sans le suffixe de groupe)
    par_t = defaultdict(set)
    tentatives = {}
    for nom, L in obs.items():
        for o in L:
            par_t[id(o["t"])].add(nom)
            tentatives[id(o["t"])] = o["t"]
    par_test = defaultdict(list)
    for k, t in tentatives.items():
        par_test[test_de_base(t["test"])].append(par_t[k])
    tests, courante = [], {}
    for test, ensembles in sorted(par_test.items()):
        union, inter = set().union(*ensembles), set.intersection(*ensembles)
        ss = [seance[q] for q in union if seance.get(q) is not None]
        s_cour = max(ss) if ss else None
        courante[test] = s_cour
        if len(ensembles) < 3:
            mode = "indéterminé (moins de 3 tentatives)"
        elif inter == union:
            mode = "commun"
        elif s_cour is not None and {q for q in union if seance.get(q) == s_cour} <= inter \
                and any(seance.get(q) is not None and seance[q] < s_cour for q in union):
            mode = "mixte"
        else:
            mode = "partiel"
        tests.append({"test": test, "tentatives": len(ensembles), "questions_vues": len(union),
                      "communes": len(inter), "seance": s_cour, "mode": mode})
    lignes = []
    for x in tests:
        msg = (f"{x['test']} : tirage {x['mode']} ({x['questions_vues']} question(s) vues, {x['communes']} communes à "
               f"toutes les tentatives" + (f", séance S{x['seance']:02d}" if x["seance"] else "") + ")")
        premier = x["mode"] == "commun" and declare == "mixte" and not any(
            seance.get(q) is not None and x["seance"] and seance[q] < x["seance"] for e in par_test[x["test"]] for q in e)
        if declare and x["mode"] in ("commun", "partiel", "mixte") and x["mode"] != declare and not premier:
            msg += f" — le profil déclare « {declare} » : vérifier les sections du test dans Moodle"
        lignes.append(msg)

    # bloc de chaque question (séance ou rappel) dans le test où elle est posée
    bloc = {}
    for nom in obs:
        s = seance.get(nom)
        cs = {courante.get(test_de_base(o["t"]["test"])) for o in obs[nom]}
        if s is not None and cs and all(c is not None for c in cs):
            bloc[nom] = "rappel" if all(c > s for c in cs) else "séance" if all(c == s for c in cs) else "séance et rappel"

    # équité : questions d'une même catégorie et d'une même séance, tirées (pas vues par toutes les tentatives)
    tirees = set()                               # vues par une partie seulement des tentatives d'un même test
    for e in par_test.values():
        tirees |= set().union(*e) - set.intersection(*e)
    pools = defaultdict(list)
    for nom, L in obs.items():
        q = infos[nom]["banque"]
        if nom not in tirees or not q:
            continue
        pools[(q.get("categorie", ""), seance.get(nom))].append(nom)
    equite = []
    for (cat, s), noms in sorted(pools.items(), key=lambda x: (str(x[0][0]), x[0][1] or 0)):
        r = {n: _reussite(obs[n]) for n in noms}
        r = {n: v for n, v in r.items() if v[0] is not None and v[1] >= N_MIN}
        if len(r) < 2:
            continue
        lo, hi = min(r, key=lambda n: r[n][0]), max(r, key=lambda n: r[n][0])
        ecart = r[hi][0] - r[lo][0]
        equite.append({"categorie": cat.replace("$course$/top/", "") or "(catégorie unique)", "seance": f"S{s:02d}" if s else "",
                       "questions": len(r), "min": r[lo][0], "q_min": lo, "max": r[hi][0], "q_max": hi, "ecart": ecart,
                       "alerte": "à vérifier : le tirage pèse sur la note" if ecart >= ECART_EQUITE else ""})
    alertes = [e for e in equite if e["alerte"]]
    if alertes:
        lignes.append("Équité du tirage : " + " ; ".join(
            f"{e['categorie']} {e['seance']} : réussite de {100 * e['min']:.0f} % ({e['q_min']}) à {100 * e['max']:.0f} % "
            f"({e['q_max']})" for e in alertes[:4])
            + f". Au-delà de {100 * ECART_EQUITE:.0f} points d'écart, deux étudiants n'ont pas eu un quiz de même difficulté "
            "(règle d'usage) : rééquilibrer la catégorie ou la scinder.")

    # rétention : même question posée le jour de sa séance puis en rappel dans un test ultérieur
    retention = []
    for nom, L in obs.items():
        s = seance.get(nom)
        if s is None:
            continue
        jour = [o for o in L if courante.get(test_de_base(o["t"]["test"])) == s]
        apres = [o for o in L if (courante.get(test_de_base(o["t"]["test"])) or 0) > s]
        (r1, n1), (r2, n2) = _reussite(jour), _reussite(apres)
        if r1 is not None and r2 is not None:
            retention.append({"question": nom, "seance": f"S{s:02d}", "reussite_seance": r1, "n_seance": n1,
                              "reussite_rappel": r2, "n_rappel": n2, "ecart": r2 - r1})
    if retention:
        par_s = defaultdict(list)
        for x in retention:
            par_s[x["seance"]].append(x)
        lignes.append("Rétention (même question le jour de sa séance, puis en rappel) : " + " ; ".join(
            f"{s} : {100 * statistics.fmean(x['reussite_seance'] for x in v):.0f} % → "
            f"{100 * statistics.fmean(x['reussite_rappel'] for x in v):.0f} % ({len(v)} question(s))"
            for s, v in sorted(par_s.items())))
    elif any(x["mode"] == "mixte" or (x["seance"] and x["seance"] > 1) for x in tests) and len(par_test) == 1:
        lignes.append("Rétention : donnez aussi les exports du quiz de la séance précédente pour comparer la réussite "
                      "des rappels à celle du jour de la séance.")
    return {"tests": tests, "equite": equite, "retention": sorted(retention, key=lambda x: (x["seance"], x["ecart"])),
            "lignes": lignes, "bloc": bloc, "seance": seance}
