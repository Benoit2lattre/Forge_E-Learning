# Axe C — Analyse d'items

Question pour l'outil : quels indicateurs et quels seuils DiagForge doit-il calculer pour juger la qualité des questions d'un quiz, et comment les présenter à l'enseignant ?

## Vue d'ensemble

Après un quiz, on peut juger chaque question à partir des réponses des étudiants. C'est l'analyse d'items (item analysis) : la difficulté (part des étudiants qui réussissent la question), la discrimination (la question est-elle mieux réussie par ceux qui réussissent le reste du test ?), le fonctionnement des leurres (les mauvaises réponses proposées sont-elles choisies, et par qui ?) et la fiabilité du test entier, le plus souvent l'alpha de Cronbach. Moodle calcule une partie de ces indicateurs ; DiagForge les recalcule à partir des exports Moodle et y ajoute des alertes.

L'enjeu pour les outils Forge est de donner à l'enseignant des signaux justes. Un seuil mal choisi fait réécrire des questions correctes ou laisse passer une clé fausse. Or la plupart des seuils publiés (réussite entre 30 et 70 %, alpha au moins 0,70, leurre « inutile » sous 5 %) sont des règles empiriques venues d'examens de médecine. L'axe sert donc à fixer, pour DiagForge, les bons indicateurs, des seuils réalistes et leur formulation (« à revoir », jamais « mauvaise question ») ; il renseigne aussi QuizForge, qui écrit les questions et leurs leurres, en lien avec l'axe B.

Le public visé est celui de Forge : étudiants de L3 à M2 en mécanique et en mathématiques, qui passent des quiz Moodle en ligne, souvent de 10 à 20 questions, par groupes de 30 à 60. Les études lues portent sur des examens de dizaines à des milliers de candidats, surtout en médecine ; aucune ne porte sur des quiz de mécanique à ces effectifs.

## Historique du domaine

**Les indicateurs de la théorie classique des tests.** Les indicateurs de base (difficulté, discrimination, fiabilité) viennent de la théorie classique des tests (classical test theory) et ont peu changé depuis. Dès les années 1960, on sait que la corrélation entre une question et le score total doit exclure la question elle-même, sinon elle est gonflée (Cureton, 1966), surtout pour les tests courts (Berk, 1978). Pour la fiabilité, Cortina (1993) rappelle que l'alpha dépend de la longueur du test et ne prouve pas qu'il mesure une seule chose ; Tavakol et Dennick (2011) en donnent une lecture pour l'enseignement médical. Pour les leurres, Attali et Fraenkel (2000) montrent que l'indice le plus utilisé est souvent mal calculé ([Attali et Fraenkel, 2000](attali2000.md)). Une théorie concurrente, la théorie des réponses aux items (item response theory), modélise la probabilité de réussir une question selon le niveau de l'étudiant ; une simulation de MacDonald et Paunonen (2002) montre qu'elle donne la même difficulté et le même classement des étudiants que la théorie classique ([MacDonald et Paunonen, 2002](macdonald2002.md)).

**Des seuils repris d'examen en examen.** Dans les années 2010, de nombreuses analyses d'un seul examen, surtout en médecine, reprennent les mêmes bandes : réussite de 30 à 70 %, discrimination d'au moins 0,25, leurre non fonctionnel sous 5 % ([Hingorjo et Jaleel, 2012](hingorjo2012.md) ; Quaigrain et Arhin, 2017 ; Kumar et al., 2021). Ces seuils viennent de manuels et ne sont pas établis par ces études. La revue de [Gierl et al. (2017)](gierl2017.md) rassemble ce que l'on sait des leurres : comment les écrire, les analyser et combien en mettre.

**Depuis 2018 : la critique des seuils fixes.** Plusieurs travaux remettent en cause les conventions. La règle des 5 % dépend mécaniquement de la difficulté ([Raymond et al., 2018](raymond2018.md)). Le seuil de 0,70 pour l'alpha n'a pas de fondement général ([Taber, 2018](taber2018.md)) ; une méta-analyse montre que l'alpha des tests de connaissances varie beaucoup ([Edelsbrunner et al., 2025](edelsbrunner2025.md)), ce que discutent Zitzmann et Orona (2025) et Hussey et al. (2025). [Slepkov et al. (2021)](slepkov2021.md) donnent enfin des valeurs de référence tirées de tests écrits par des enseignants d'université, et non d'examens standardisés. Les études les plus récentes vérifient ce que les seuils détectent réellement ([Srisomsak et al., 2025](srisomsak2025.md)) et combien d'options mettre ([Sridharan et Sivaramakrishnan, 2025](sridharan2025.md) ; Sunsundegui et al., 2026).

## C1 — Indices classiques, seuils et fiabilité

La difficulté d'une question est sa part de réussite. Sa discrimination se mesure par la corrélation entre la réussite à la question et le score du reste du test (« item exclu ») : la corrélation avec le score total, qui contient la question, est gonflée sur un test court ([Slepkov et al., 2021](slepkov2021.md)). Les seuils usuels (réussite de 30 à 70 %, discrimination d'au moins 0,25) viennent d'examens isolés ([Hingorjo et Jaleel, 2012](hingorjo2012.md)) ; sur un grand corpus de tests d'enseignants, la plage utile de difficulté est plus large ([Slepkov et al., 2021](slepkov2021.md)). Les seuils fixes repèrent la plupart des questions défectueuses mais pas toutes ; les autres se voient dans la répartition des réponses ([Srisomsak et al., 2025](srisomsak2025.md)).

La fiabilité d'un test se résume souvent par l'alpha de Cronbach, qui mesure la cohérence des réponses entre questions. Il augmente avec le nombre de questions et baisse quand le test couvre des notions variées ; il ne dit ni si le test est valide ni s'il mesure une seule compétence ([Taber, 2018](taber2018.md)). Un alpha modéré n'est donc pas anormal pour un quiz qui couvre plusieurs notions ([Edelsbrunner et al., 2025](edelsbrunner2025.md)). Enfin, quand un quiz accorde un crédit partiel aux essais successifs, ce crédit augmente la discrimination et la fiabilité plutôt que de les dégrader ([Slepkov et Godfrey, 2019](../A_tests_retroaction/slepkov2019.md), fiche dans l'axe A).

## C2 — Leurres, petits effectifs, théorie classique contre réponse à l'item

Un leurre (distractor) est une mauvaise réponse proposée dans un QCM. Il est utile s'il attire des étudiants qui n'ont pas compris, et suspect s'il attire des étudiants aussi forts que ceux qui ont juste (clé fausse ou deuxième bonne réponse). Pour le juger, il faut comparer ceux qui le choisissent à ceux qui choisissent la bonne réponse ([Attali et Fraenkel, 2000](attali2000.md)) et lire son taux de choix en tenant compte de la difficulté de la question ([Raymond et al., 2018](raymond2018.md)). Les leurres se conçoivent à partir des erreurs types des étudiants et s'analysent en séparant étudiants forts et faibles ([Gierl et al., 2017](gierl2017.md)). Deux leurres bien écrits valent trois ou quatre médiocres ([Sridharan et Sivaramakrishnan, 2025](sridharan2025.md), certitude très faible).

Nos classes de 30 à 60 étudiants posent la question des petits effectifs. La théorie des réponses aux items demande beaucoup plus de répondants que nos classes (Weber et al., 2026, sans fiche) et n'apporte rien de décisif sur la difficulté ou le classement des étudiants ; la discrimination classique est seulement moins précise pour les questions très faciles ou très difficiles ([MacDonald et Paunonen, 2002](macdonald2002.md)). DiagForge reste donc en théorie classique, avec des alertes prudentes quand peu d'étudiants se trompent.

## Ce que disent les fiches

Synthèse rédigée à partir des 10 fiches de lecture écrites (3 de priorité 1 et 7 de priorité 2 ; toutes les fiches de priorité 1 et 2 de l'axe sont lues ; celles de Gierl et al., 2017, et de Sridharan et Sivaramakrishnan, 2025, sont partagées avec l'axe B). S'y ajoute une fiche de l'axe A sur le crédit partiel ([Slepkov et Godfrey, 2019](../A_tests_retroaction/slepkov2019.md)). Elle ne dit que ce que ces fiches soutiennent ; le niveau de preuve suit l'échelle de [fiches_methode.md](../fiches_methode.md).

**1. Mesurer la discrimination « item exclu ».** La point-bisériale classique contient la question dans le score total ; sur un test court, elle peut dépasser le seuil usuel de 0,20 même si les réponses sont données au hasard. La corrélation entre la question et le score du reste du test évite ce biais ([Slepkov et al., 2021](slepkov2021.md), niveau B). C'est l'indicateur que DiagForge utilise déjà. Sur 182 QCM d'examen réels, cette corrélation vaut 0,24 en moyenne ; 8 % des questions sont négatives, 20 % faibles (0 à 0,15), 45 % correctes (0,15 à 0,35), 25 % très bonnes (niveau C pour ces seuils, descriptifs). La théorie des réponses aux items n'apporte rien de décisif à nos effectifs : difficulté et classement des étudiants sont les mêmes qu'en théorie classique, mais la discrimination classique est imprécise pour les questions très faciles ou très difficiles ([MacDonald et Paunonen, 2002](macdonald2002.md), niveau C).

**2. Une plage de difficulté utile plus large que 30-70 %.** La règle « réussite entre 30 et 70 % » vient de manuels et d'études d'un seul examen ([Hingorjo et Jaleel, 2012](hingorjo2012.md), niveau D). Sur un grand corpus, les questions réussies de 0,4 à 0,9 discriminent à peu près autant ; la discrimination s'effondre sous 0,3. Plage proposée : de 0,43 (3 options), 0,35 (4 options) ou 0,30 (5 options) jusqu'à 0,90 ([Slepkov et al., 2021](slepkov2021.md), niveau C).

**3. L'alpha n'est pas une note de qualité.** L'alpha de Cronbach dépend du nombre de questions et de l'homogénéité du contenu ; un quiz qui couvre plusieurs notions de mécanique aura un alpha modéré sans être mauvais. Le seuil de 0,70 n'a pas de fondement général ([Taber, 2018](taber2018.md), niveau C) ; pour un test de 20 items, les alphas publiés vont de 0,35 à 0,96, avec un excès suspect juste au-dessus de 0,70, 0,80 et 0,90 ([Edelsbrunner et al., 2025](edelsbrunner2025.md), niveau B). Pour comparer des tests de longueurs différentes, on peut ramener l'alpha à 50 items ou utiliser la discrimination moyenne ([Slepkov et al., 2021](slepkov2021.md)).

**4. Juger les leurres avec la bonne comparaison et le bon seuil.** Un leurre se juge en comparant ceux qui le choisissent à ceux qui choisissent la bonne réponse, pas à tous les autres ; la méthode usuelle rejette à tort des leurres de questions difficiles ([Attali et Fraenkel, 2000](attali2000.md), niveau B). La règle « moins de 5 % = leurre inutile » dépend mécaniquement de la difficulté : au-dessus de 90 % de réussite, un seul leurre au plus peut la franchir ; un seuil de 0,1 × (1 − réussite) corrige ce biais ([Raymond et al., 2018](raymond2018.md), niveau C). Retirer le leurre le moins choisi ne change presque rien à la fiabilité (même fiche ; [Sridharan et Sivaramakrishnan, 2025](sridharan2025.md)). Les leurres se lisent aussi en séparant étudiants forts et faibles ([Gierl et al., 2017](gierl2017.md), niveau C).

**5. Les seuils signalent, l'enseignant décide.** Dans six ans d'examens de médecine, les questions à corriger avaient surtout plusieurs bonnes réponses ou une clé fausse ; les seuils « réussite < 0,25 ou discrimination < 0 » en repèrent 86 %, les autres se voient dans la répartition des réponses, quand la réponse attendue n'est pas la plus choisie ([Srisomsak et al., 2025](srisomsak2025.md), niveau C).

**6. Avec plusieurs essais, analyser aussi le premier essai.** Sur 26 examens de physique et de chimie où l'étudiant répond jusqu'à trouver la bonne réponse, le crédit partiel accordé au 2e ou au 3e essai augmente la discrimination des questions (0,30 à 0,33) et la fiabilité (alpha 0,70 à 0,73), alors qu'un crédit donné au hasard les ferait baisser ([Slepkov et Godfrey, 2019](../A_tests_retroaction/slepkov2019.md), niveau B). Cette fiche **conforte** le mode Moodle à essais multiples de QuizForge, et suggère à DiagForge de calculer les indicateurs sur la note avec crédit partiel et sur le premier essai seul (niveau B), ce qu'il ne fait pas encore.

## Règles pour DiagForge

| Règle | Niveau | Fiches | Dans DiagForge aujourd'hui |
| --- | --- | --- | --- |
| Discrimination = corrélation entre la question et le reste du test | B | slepkov2021 | oui |
| Seuils de discrimination : < 0 à revoir, < 0,15 faible, > 0,35 très bonne | C | slepkov2021 | oui |
| Plage de difficulté utile selon le nombre d'options, jusqu'à 0,90 | C | slepkov2021, hingorjo2012 | oui (environ hasard + 0,10 ; 0,30 si le nombre d'options est inconnu) |
| Discrimination d'une question réussie à moins de 30 % ou plus de 90 % signalée « peu fiable », pas « mauvaise » | C | macdonald2002, slepkov2021 | oui |
| Alpha présenté avec le nombre de questions et la plage attendue, sans verdict à 0,70 ; corrélation moyenne entre questions affichée | B | edelsbrunner2025, taber2018 | oui (valeur typique pour le nombre de questions, Edelsbrunner et al., 2025, tableau 3) |
| Ne jamais conseiller de retirer une question pour faire monter l'alpha | C | edelsbrunner2025, taber2018 | oui (aucun conseil de ce type) |
| Alpha ramené à 50 items pour comparer des tests | C | slepkov2021 | oui |
| Alpha par thème (tag) | D | taber2018 | oui (si des tentatives contiennent toutes les questions du thème) |
| Pour chaque leurre : score moyen (reste du test) de ceux qui le choisissent, comparé à celui des bonnes réponses | B | attali2000, gierl2017 | oui (onglet Réponses ; alerte si un leurre attire des étudiants aussi forts que ceux qui ont juste) |
| Alerte prioritaire : réponse attendue moins choisie ou autant choisie qu'une autre option | C | srisomsak2025, attali2000 | oui |
| Leurre non fonctionnel si choisi par moins de 0,1 × (1 − réussite), avec un minimum d'étudiants en échec ; pas d'alerte au-dessus de 90 % de réussite | C | raymond2018 | oui (au moins 10 étudiants en échec) |
| Toutes les alertes présentées comme des points à vérifier par l'enseignant | C | srisomsak2025 | oui (« à revoir ») |
| Rester en théorie classique | C | macdonald2002 | oui |
| Test à essais multiples : difficulté, discrimination et alpha calculés sur la note avec crédit partiel et sur le premier essai seul | B | slepkov2019 (axe A) | non |

Ces règles sont reprises sous forme lisible par un programme dans l'en-tête de chaque fiche (champ `regles`). La dernière colonne compare au code de `scripts/quizforge/bilan.py` après sa mise à jour du 08/11/2026.

## Ce qui reste ouvert

- Toutes les études portent sur des tests passés par des dizaines à des milliers de personnes et de 17 à 150 questions ; nos quiz Moodle ont souvent 10 à 20 questions tirées au sort et 30 à 60 étudiants. La stabilité des indicateurs à ces effectifs reste à mesurer sur nos propres données (Weber et al., 2026, priorité 3, traite de la théorie des réponses aux items sous 100 répondants).
- Aucun seuil n'est validé contre un critère externe (relecture experte systématique) ; Srisomsak et al. (2025) est ce qui s'en approche le plus.
- La question des questions tirées au sort (chaque étudiant voit un sous-ensemble) n'est traitée par aucune fiche.
- Les scores à essais multiples mêlent niveau et persévérance ; l'effet sur la difficulté et la discrimination calculées à partir des exports Moodle n'est pas documenté au-delà de [Slepkov et Godfrey (2019)](../A_tests_retroaction/slepkov2019.md).
- Les questions composites (appariement, glisser-déposer sur un schéma, textes à trous, réponses numériques) n'ont pas d'indicateurs établis : l'analyse élément par élément de DiagForge n'a pas de référence à laquelle se comparer.

Chacune de ces questions peut faire l'objet d'un essai avec DiagForge ; les fiches proposent le dispositif (rubrique « Pour conclure, il faudrait »).

## Références

Références complètes : [`../forge.bib`](../forge.bib). `gierl2017` et `sridharan2025` figurent aussi dans l'axe B ; `slepkov2019` a sa fiche dans l'axe A. La colonne « Fiche » donne le lien quand la fiche est écrite.

| Réf. (forge.bib) | Sous-axe | Apport | Priorité | Fiche |
| --- | --- | --- | --- | --- |
| `edelsbrunner2025` — Edelsbrunner et al. (2025) | C1 | alpha typique 0,85 ; intervalle 0,35-0,96 pour 20 items ; seuils fixes contestés | 1 | [fiche](edelsbrunner2025.md) |
| `slepkov2021` — Slepkov et al. (2021) | C1 | référence pour tests d'enseignants : 182 tests, discrimination hors item, fiabilité normalisée | 1 | [fiche](slepkov2021.md) |
| `hingorjo2012` — Hingorjo and Jaleel (2012) | C1 | seuils usuels repris d'un seul examen : difficulté 30-70 %, discrimination >= 0,25 | 2 | [fiche](hingorjo2012.md) |
| `srisomsak2025` — Srisomsak et al. (2025) | C1 | seuils fixes : 86 % des items défectueux détectés, 14 % manqués | 2 | [fiche](srisomsak2025.md) |
| `taber2018` — Taber (2018) | C1 | usage d'alpha en didactique des sciences ; un alpha très élevé n'est pas souhaitable | 2 | [fiche](taber2018.md) |
| `slepkov2019` — Slepkov and Godfrey (2019) | C1 | crédit partiel aux essais successifs : discrimination et fiabilité en hausse | — (axe A) | [fiche](../A_tests_retroaction/slepkov2019.md) |
| `berk1978` — Berk (1978) | C1 | correction nécessaire sous 0,4 avec 18-20 items | 3 | à lire |
| `cortina1993` — Cortina (1993) | C1 | ce que mesure alpha ; dépendance à la longueur | 3 | à lire |
| `cureton1966` — Cureton (1966) | C1 | corrélation item-total corrigée de l'item | 3 | à lire |
| `hussey2025` — Hussey et al. (2025) | C1 | excès suspect de valeurs d'alpha à 0,70 | 3 | à lire |
| `kumar2021` — Kumar et al. (2021) | C1 | mêmes bandes de seuils, 90 QCM de physiologie | 3 | à lire |
| `quaigrain2017` — Quaigrain and Arhin (2017) | C1 | discrimination maximale pour une difficulté de 40-60 % | 3 | à lire |
| `tavakol2011` — Tavakol and Dennick (2011) | C1 | lecture d'alpha ; > 0,90 = redondance possible | 3 | à lire |
| `zitzmann2025` — Zitzmann and Orona (2025) | C1 | réponse : garder des seuils pour alpha | 3 | à lire |
| `gierl2017` — Gierl et al. (2017) | C2 | revue de référence sur l'écriture et l'analyse des leurres | 1 | [fiche](gierl2017.md) |
| `attali2000` — Attali and Fraenkel (2000) | C2 | mauvais usage de la point-bisériale pour les leurres ; alternative | 2 | [fiche](attali2000.md) |
| `macdonald2002` — MacDonald and Paunonen (2002) | C2 | difficulté CTT et IRT comparables ; discrimination CTT fiable sous conditions | 2 | [fiche](macdonald2002.md) |
| `raymond2018` — Raymond et al. (2018) | C2 | règle < 5 % biaisée par la difficulté ; indice corrigé | 2 | [fiche](raymond2018.md) |
| `sridharan2025` — Sridharan and Sivaramakrishnan (2025) | C2 | 3 options valent 4 ou 5 (méta-analyse en réseau, certitude très faible) | 2 | [fiche](sridharan2025.md) |
| `rezigalla2024` — Rezigalla et al. (2024) | C2 | plus de leurres non fonctionnels = items plus faciles et moins discriminants | 3 | à lire |
| `shakurnia2022` — Shakurnia et al. (2022) | C2 | 734 QCM : leurres non fonctionnels liés à la facilité | 3 | à lire |
| `sunsundegui2026` — Sunsundegui et al. (2026) | C2 | 2 leurres bien écrits = 3 leurres (étude randomisée) | 3 | à lire |
| `weber2026` — Weber et al. (2026) | C2 | IRT insuffisante sous ~100 répondants | 3 | à lire |

Priorité 1 = à lire d'abord. « Fiche » passe à un lien quand la fiche de lecture `<clé>.md` est écrite (dans ce dossier ou dans un autre axe) ; « à lire » = priorité 3, pas encore de fiche.
