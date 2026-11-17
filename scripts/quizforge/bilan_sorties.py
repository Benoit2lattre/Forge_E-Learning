"""QuizForge — DiagForge, sorties exploitées du bilan :

1. étudiants : notes de la promotion et par groupe (images PNG anonymes) ;
2. étudiants + professeur : réussite par tag, par type de question, par catégorie (images + détail) ;
3. professeur : questions à revoir en priorité (onglet « À revoir » + fiche HTML).

Groupes : roster (fichier avec une colonne Groupe) en priorité, sinon suffixe du nom du test (``Quizz1_SMA`` → ``SMA``).
"""
import base64
import html
import statistics
from collections import defaultdict
from datetime import date
from pathlib import Path

import bilan as B
import graphiques as G

TYPES = {"multichoice": "QCM", "truefalse": "Vrai / Faux", "numerical": "Numérique", "shortanswer": "Réponse courte",
         "matching": "Appariement", "ddwtos": "Texte à trous (glisser)", "gapselect": "Texte à trous (menus)",
         "ddimageortext": "Schéma (glisser)", "ddmarker": "Schéma (marqueurs)", "essay": "Question ouverte",
         "calculated": "Calculée", "calculatedsimple": "Calculée", "calculatedmulti": "Calculée (QCM)",
         "multianswer": "Cloze", "randomsamatch": "Appariement aléatoire"}


# ------------------------------------------------------------------ roster et groupes
def est_roster(p: Path) -> bool:
    """Indique si le fichier est une liste d'étudiants avec leur groupe (colonne Groupe, sans colonne de début de tentative)."""
    lignes = B.lire_table(p)
    if not lignes:
        return False
    cles = [B.cle(h) for h in lignes[0]]
    return any(c in ("groupe", "group", "groupes", "groups", "section", "td") for c in cles) and \
        not any(c in ("started", "commencele", "debut") for c in cles)


def lire_roster(fichiers, avert):
    """Lit les rosters et renvoie ``{clé: groupe}``, avec pour clés le courriel, nom+prénom et prénom+nom.

    Ajoute à ``avert`` un message par fichier (nombre d'étudiants, groupes).
    """
    table = {}
    for p in fichiers:
        lignes = B.lire_table(p)
        cles = [B.cle(h) for h in lignes[0]]
        idx = lambda *noms: next((i for i, c in enumerate(cles) if c in noms), None)  # noqa: E731
        ig = idx("groupe", "group", "groupes", "groups", "section", "td")
        ie = idx("email", "emailaddress", "adressedecourriel", "courriel", "adressemail", "mail")
        inom = idx("nom", "lastname", "nomdefamille", "surname")
        ipre = idx("prenom", "firstname")
        n = 0
        for l in lignes[1:]:
            l = l + [""] * (len(cles) - len(l))
            g = l[ig].strip()
            if not g:
                continue
            if ie is not None and l[ie].strip():
                table[l[ie].strip().lower()] = g
            if inom is not None and ipre is not None:
                table[B.cle(l[inom] + l[ipre])] = g; table[B.cle(l[ipre] + l[inom])] = g
            elif inom is not None:                                # « NOM Prénom » dans une seule colonne
                table[B.cle(l[inom])] = g
            n += 1
        avert.append(f"{p.name} : roster, {n} étudiant(s), groupes : {', '.join(sorted(set(table.values())))}")
    return table


def affecter_groupes(tent, roster, avert):
    """Renseigne le groupe de chaque tentative (clé ``groupe``), en modifiant les tentatives sur place.

    Le roster est cherché par courriel puis par nom+prénom ; à défaut, le groupe est le suffixe du nom
    du test. Les étudiants absents du roster sont signalés dans ``avert``.
    """
    absents = set()
    for t in tent:
        g = ""
        if roster:
            g = roster.get(t["email"].strip().lower()) or roster.get(B.cle(t["nom"] + t["prenom"])) or ""
            if not g:
                absents.add(f"{t['nom']} {t['prenom']}".strip())
        t["groupe"] = g or B.groupe_du_test(t["test"])
    if absents:
        avert.append(f"absents du roster ({len(absents)}) : " + ", ".join(sorted(absents)[:12]) + (" …" if len(absents) > 12 else "")
                     + " — groupe pris dans le nom du test")


def notes_par_etudiant(tent, mode):
    """Renvoie une note sur 20 par étudiant : ``[{"id", "groupe", "note20"}]``.

    En mode ``toutes`` ou ``meilleure`` : meilleure tentative, comme la méthode par défaut de Moodle ;
    sinon la tentative déjà retenue.
    """
    par = defaultdict(list)
    for t in tent:
        if t["note"] is not None and t["note_max"]:
            par[t["id"]].append(t)
    out = []
    for ts in par.values():
        t = max(ts, key=lambda x: x["note"]) if mode in ("toutes", "meilleure") else ts[0]
        out.append({"id": t["id"], "groupe": t["groupe"], "note20": 20 * t["note"] / t["note_max"]})
    return out


def stats_groupes(notes):
    """Calcule les statistiques des notes sur 20 par groupe (et pour la promotion s'il y a plusieurs groupes).

    Renvoie ``(lignes, par_groupe)`` : une ligne par groupe (effectif, moyenne, médiane, écart-type,
    min, max, part ≥ 10/20) et le dictionnaire groupe → notes. Les étudiants sans groupe sont rangés sous « — ».
    """
    par = defaultdict(list)
    for x in notes:
        par[x["groupe"] or "—"].append(x["note20"])
    lignes = []
    for g in sorted(par):
        v = par[g]
        lignes.append({"groupe": g, "n": len(v), "moyenne": statistics.fmean(v), "mediane": statistics.median(v),
                       "ecart": statistics.stdev(v) if len(v) > 1 else None, "min": min(v), "max": max(v),
                       "reussite10": sum(1 for x in v if x >= 10) / len(v)})
    tout = [x["note20"] for x in notes]
    if len(par) > 1 and tout:
        lignes.append({"groupe": "Promotion", "n": len(tout), "moyenne": statistics.fmean(tout), "mediane": statistics.median(tout),
                       "ecart": statistics.stdev(tout) if len(tout) > 1 else None, "min": min(tout), "max": max(tout),
                       "reussite10": sum(1 for x in tout if x >= 10) / len(tout)})
    return lignes, {g: par[g] for g in sorted(par)}


# ------------------------------------------------------------------ regroupements de questions
def regroupements(obs, infos, groupes):
    """Calcule la réussite par regroupement de questions (tag, type, catégorie), pour la promotion et par groupe.

    Renvoie ``{"tag": [...], "type": [...], "categorie": [...]}`` ; chaque ligne : ``nom``, ``n_questions``, ``n``,
    ``promo``, ``groupes``, ``detail``, triées de la moins à la plus réussie. Les tags sans information
    (sur presque toutes les questions, ou identiques à un type) sont ignorés.
    """
    membres = {"tag": defaultdict(set), "type": defaultdict(set), "categorie": defaultdict(set)}
    for nom, info in infos.items():
        q = info["banque"]
        if not q:
            continue
        membres["type"][TYPES.get(q["type"], q["type"])].add(nom)
        if q.get("categorie"):
            membres["categorie"][q["categorie"]].add(nom)
        for tg in q.get("tags", []):
            membres["tag"][tg].add(nom)
    nq = len([1 for i in infos.values() if i["banque"]])
    # tags sans information : présents sur (presque) toutes les questions, ou identiques à un type
    ensembles_types = {frozenset(v) for v in membres["type"].values()}
    for tg in list(membres["tag"]):
        v = membres["tag"][tg]
        if (nq >= 3 and len(v) >= 0.9 * nq) or frozenset(v) in ensembles_types:
            del membres["tag"][tg]
    out = {}
    for sorte, m in membres.items():
        lignes = []
        for nom_g, qs in m.items():
            fr = [o["f"] for q in qs for o in obs[q] if o["f"] is not None]
            if not fr:
                continue
            par_g = {}
            for g in groupes:
                v = [o["f"] for q in qs for o in obs[q] if o["f"] is not None and o["t"]["groupe"] == g]
                par_g[g] = statistics.fmean(v) if v else None
            detail = []
            for q in sorted(qs):
                v = [o["f"] for o in obs[q] if o["f"] is not None]
                if v:
                    detail.append((q, statistics.fmean(v), len(v)))
            lignes.append({"nom": nom_g, "n_questions": len(qs), "n": len(fr), "promo": statistics.fmean(fr),
                           "groupes": par_g, "detail": sorted(detail, key=lambda x: x[1])})
        out[sorte] = sorted(lignes, key=lambda x: x["promo"])
    return out


# ------------------------------------------------------------------ questions à revoir
def a_revoir(questions):
    """Classe les questions à revoir par priorité : ce qu'il faut changer dans la question, et ce qu'il faut retravailler en cours.

    Le score additionne les problèmes repérés (discrimination, erreur dominante, difficulté, leurres) ;
    la priorité le pondère par le nombre de réponses. Renvoie les lignes triées, numérotées par ``rang``.
    """
    S = B.SEUILS
    out = []
    for q in questions:
        n, r, fac, al = q["n_notees"], q["discrimination"], q["facilite"], q["alertes"] or ""
        if n < S["n_min"] or fac is None:
            continue
        # discrimination « peu fiable » (réussite hors de 30-90 %) : on n'en tire pas de priorité (macdonald2002)
        rfiable = r is not None and q["n_discrim"] >= S["discrim_n_min"] and q.get("discrim_lecture") != "peu fiable"
        ac = "" if q["n_discrim"] >= 50 else ", à confirmer"
        score, raisons, sur_q, en_cours = 0, [], [], []
        erreur = ""
        if any(m in al for m in ("plus choisie que la bonne", "plus choisi que la bonne",
                                 "autant choisie que la bonne", "autant choisi que la bonne")):
            erreur = next((x.strip() for x in al.split(" ; ") if "plus choisi" in x or "autant choisi" in x), "")
        if rfiable and r < S["discrim_negative"]:
            score += 5; raisons.append(f"discrimination négative (r = {r:.2f}{ac})")
            sur_q.append("vérifier le corrigé et l'énoncé : les étudiants qui réussissent le reste du test échouent ici")
        if erreur and q.get("discrim_lecture") == "peu fiable":
            score += 3; raisons.append("erreur dominante")
            sur_q.append(f"vérifier que l'énoncé n'induit pas l'erreur ({erreur})")
            en_cours.append("si l'énoncé est clair, erreur répandue à retravailler en cours "
                            "(discrimination peu fiable à ce niveau de réussite)")
        elif erreur:
            if rfiable and r >= S["discrim_faible"]:
                score += 3; raisons.append("erreur dominante")
                en_cours.append(f"erreur répandue à retravailler en cours ({erreur}) ; la question fonctionne")
            else:
                score += 4; raisons.append("erreur dominante, y compris chez les bons étudiants")
                sur_q.append(f"énoncé ambigu ou piège involontaire ? ({erreur})")
        if fac <= q.get("plancher", S["difficile"]):
            score += 3; raisons.append(f"très difficile ({fac:.0%})")
            (en_cours if rfiable and r >= S["discrim_faible"] else sur_q).append(
                "notion mal acquise : la reprendre avant le prochain test" if rfiable and r >= S["discrim_faible"]
                else "trop difficile ou ambiguë : reformuler, découper en étapes ou ajouter un rappel")
        elif rfiable and S["discrim_negative"] <= r < S["discrim_faible"]:
            score += 2; raisons.append(f"peu discriminante (r = {r:.2f}{ac})")
            sur_q.append("reformuler : la réussite dépend peu du niveau (devinette, indice dans l'énoncé, ou hors sujet ?)")
        if fac >= S["facile"]:
            score += 1; raisons.append(f"très facile ({fac:.0%})")
            sur_q.append("rendre les leurres plus crédibles (erreurs réellement observées) ou retirer la question")
        if "aussi forts que ceux qui ont juste" in al:
            score += 3; raisons.append("leurre choisi par de bons étudiants")
            sur_q.append("vérifier la clé : un leurre attire des étudiants aussi forts que ceux qui ont juste "
                         "(deuxième bonne réponse, énoncé ambigu ?)")
        if "leurre non fonctionnel" in al:
            score += 1; raisons.append("leurre non fonctionnel")
            sur_q.append("remplacer le leurre peu choisi par une erreur fréquente observée, ou le retirer (3 options suffisent)")
        if not score:
            continue
        confiance = "faible" if n < 20 else "moyenne" if n < 50 else "bonne"
        out.append({"question": q["question"], "type": TYPES.get(q["type"], q["type"]), "score": score,
                    "priorite": round(score * (0.6 if n < 20 else 0.85 if n < 50 else 1.0), 2),
                    "raisons": " ; ".join(raisons), "sur_question": " ; ".join(sur_q), "en_cours": " ; ".join(en_cours),
                    "reussite": fac, "discrimination": r, "n": n, "confiance": confiance,
                    "fausse": q["fausse_frequente"]})
    out.sort(key=lambda x: (-x["priorite"], x["reussite"]))
    for k, x in enumerate(out, 1):
        x["rang"] = k
    return out


# ------------------------------------------------------------------ images
def images(dossier: Path, nom_test, notes, par_groupe, regr, couleur, mode="meilleure"):
    """Produit les images PNG pour les étudiants dans ``dossier`` (notes, comparaison des groupes, réussite par regroupement).

    ``mode`` : tentatives retenues (voir :func:`notes_par_etudiant`), rappelé sous le titre de l'histogramme.
    Renvoie ``(chemins des images, message)`` ; sans matplotlib, aucune image et un message d'explication.
    """
    if not G.disponible():
        return [], "images non produites : matplotlib absent (dans le dossier du dépôt : uv pip install matplotlib)"
    dossier.mkdir(parents=True, exist_ok=True)
    base, couleurs = G.palette(couleur)
    faits = []
    tout = [x["note20"] for x in notes]
    groupes = [g for g in par_groupe if g != "—"]
    critere = {"premiere": "première tentative", "derniere": "dernière tentative"}.get(mode, "meilleure tentative") + " de chaque étudiant"
    faits.append(G.histogramme(tout, f"{nom_test} — notes de la promotion", dossier / "notes_promotion.png", base,
                               f"{len(tout)} étudiants ({critere})"))
    if len(groupes) > 1:
        for k, g in enumerate(groupes):
            faits.append(G.histogramme(par_groupe[g], f"{nom_test} — groupe {g}", dossier / f"notes_groupe_{B.cle(g)}.png",
                                       couleurs[(k + 1) % len(couleurs)], f"{len(par_groupe[g])} étudiants"))
        faits.append(G.comparaison_groupes({g: par_groupe[g] for g in groupes}, f"{nom_test} — comparaison des groupes",
                                           dossier / "notes_par_groupe.png", couleurs[1:]))
    titres = {"tag": "Réussite par thème (tag)", "type": "Réussite par type de question", "categorie": "Réussite par catégorie"}
    for sorte, lignes in regr.items():
        if len(lignes) >= 2:
            faits.append(G.reussite(lignes, f"{nom_test} — {titres[sorte]}", dossier / f"reussite_par_{sorte}.png", base,
                                    groupes if len(groupes) > 1 else (), couleurs))
    return faits, f"{len(faits)} image(s) dans {dossier.name}"


# ------------------------------------------------------------------ fiche du professeur (HTML autonome)
def fiche(sortie: Path, nom_test, synth_lignes, stats_g, regr, revoir, imgs, couleur, avert):
    """Écrit la fiche du professeur, page HTML autonome (images intégrées), et renvoie son chemin.

    Sections : notes, où se produisent les erreurs, questions à revoir en priorité, indicateurs du test.
    """
    e = html.escape
    c = "#" + couleur.lstrip("#")
    def img(p):
        return f'<img alt="{e(p.stem)}" src="data:image/png;base64,{base64.b64encode(p.read_bytes()).decode()}">'
    def pc(v):
        return "—" if v is None else f"{100 * v:.0f} %"
    h = [f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><title>Bilan {e(nom_test)}</title>
<style>body{{font-family:"Segoe UI",system-ui,sans-serif;max-width:1000px;margin:24px auto;padding:0 16px;color:#1d1d1d;line-height:1.45}}
h1{{color:{c};margin-bottom:0}} h2{{color:{c};border-bottom:2px solid {c};padding-bottom:3px;margin-top:32px}}
table{{border-collapse:collapse;width:100%;font-size:14px;margin:8px 0}} th{{background:{c};color:#fff;text-align:left}}
th,td{{padding:5px 8px;border-bottom:1px solid #ddd;vertical-align:top}} img{{max-width:100%;margin:8px 0}}
.p{{color:#666;font-size:13px}} .hi{{background:#FDECEC}} details{{margin:4px 0}} summary{{cursor:pointer;color:{c}}}
@media print{{h2{{break-before:auto}} details{{display:block}}}}</style></head><body>
<h1>Bilan du test « {e(nom_test)} »</h1><p class="p">Fiche du professeur — produite par QuizForge le {date.today():%d/%m/%Y}</p>"""]
    h.append("<h2>1. Notes</h2>")
    if stats_g:
        h.append("<table><tr><th>Groupe</th><th>Étudiants</th><th>Moyenne /20</th><th>Médiane</th><th>Écart-type</th>"
                 "<th>Min – max</th><th>≥ 10</th></tr>")
        for s in stats_g:
            ec = "—" if s["ecart"] is None else f"{s['ecart']:.1f}"
            h.append(f"<tr><td><b>{e(s['groupe'])}</b></td><td>{s['n']}</td><td>{s['moyenne']:.1f}</td><td>{s['mediane']:.1f}</td>"
                     f"<td>{ec}</td>"
                     f"<td>{s['min']:.1f} – {s['max']:.1f}</td><td>{pc(s['reussite10'])}</td></tr>")
        h.append("</table>")
    for p in imgs:
        if p.name.startswith("notes_promotion") or p.name.startswith("notes_par_groupe"):
            h.append(img(p))
    h.append("<h2>2. Où se produisent les erreurs</h2>")
    titres = {"tag": "Par thème (tag)", "type": "Par type de question", "categorie": "Par catégorie"}
    for sorte, lignes in regr.items():
        if not lignes:
            continue
        h.append(f"<h3>{titres[sorte]}</h3>")
        p = next((x for x in imgs if x.name == f"reussite_par_{sorte}.png"), None)
        if p:
            h.append(img(p))
        groupes = list(lignes[0]["groupes"])
        h.append("<table><tr><th>" + titres[sorte].split(" ", 1)[1].capitalize() + "</th><th>Réussite</th>"
                 + "".join(f"<th>{e(g)}</th>" for g in groupes) + "<th>Réponses</th><th>Questions (de la moins à la plus réussie)</th></tr>")
        for l in lignes:
            det = "<br>".join(f"{e(q)} : {pc(v)} (n = {n})" for q, v, n in l["detail"])
            h.append(f"<tr{' class=hi' if l['promo'] < 0.5 else ''}><td><b>{e(l['nom'])}</b></td><td>{pc(l['promo'])}</td>"
                     + "".join(f"<td>{pc(l['groupes'].get(g))}</td>" for g in groupes)
                     + f"<td>{l['n']}</td><td><details><summary>{l['n_questions']} question(s)</summary>{det}</details></td></tr>")
        h.append("</table>")
    if not any(regr.values()):
        h.append("<p>Pas de regroupement possible : ajoutez l'export XML des questions (tags, types, catégories).</p>")
    h.append("<h2>3. Questions à revoir en priorité</h2>")
    if revoir:
        h.append("<table><tr><th>#</th><th>Question</th><th>Pourquoi</th><th>Sur la question</th><th>En cours</th>"
                 "<th>Réussite</th><th>r</th><th>n</th></tr>")
        for x in revoir:
            rd = "—" if x["discrimination"] is None else f"{x['discrimination']:.2f}"
            h.append(f"<tr><td>{x['rang']}</td><td><b>{e(x['question'])}</b><br><span class=p>{e(x['type'])}</span></td>"
                     f"<td>{e(x['raisons'])}</td><td>{e(x['sur_question'])}</td><td>{e(x['en_cours'])}</td>"
                     f"<td>{pc(x['reussite'])}</td><td>{rd}</td>"
                     f"<td>{x['n']}<br><span class=p>{x['confiance']}</span></td></tr>")
        h.append("</table><p class=p>Priorité = gravité des problèmes, pondérée par le nombre de réponses (confiance faible "
                 "sous 20, moyenne sous 50). « Sur la question » : ce qu'il faut changer dans la question. « En cours » : la "
                 "question fonctionne, c'est la notion qui est à retravailler.</p>")
    else:
        h.append("<p>Aucune question à revoir (ou trop peu de réponses par question pour conclure).</p>")
    h.append("<h2>4. Indicateurs du test</h2><table>")
    for k, v in synth_lignes:
        if k.strip() and k not in ("Lecture",) and not k.startswith("Bilan du test"):
            h.append(f"<tr><td><b>{e(k)}</b></td><td>{e(str(v)).replace(chr(10), '<br>')}</td></tr>")
    h.append("</table></body></html>")
    sortie.write_text("\n".join(h), encoding="utf-8")
    return sortie
