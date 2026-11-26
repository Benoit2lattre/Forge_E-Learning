# Axe G — Restitution aux étudiants

Question pour l'outil : que mettre dans le rapport que DiagForge rend à chaque étudiant (répartition des réponses, position par rapport au critère, à sa propre progression ou aux pairs, recommandations), et sous quelle forme ?

## Vue d'ensemble

Après un quiz, DiagForge sait beaucoup de choses sur chaque étudiant : son score par notion, les leurres qu'il a choisis, sa position dans la classe, son évolution depuis le quiz précédent. Cet axe étudie ce qu'il faut en rendre à l'étudiant et sous quelle forme. Deux littératures se rejoignent : la psychologie de la comparaison sociale et de la rétroaction (faut-il situer l'étudiant par rapport à un critère, à lui-même ou à ses camarades ?) et l'analytique d'apprentissage, qui conçoit depuis une quinzaine d'années des tableaux de bord destinés aux étudiants.

L'enjeu pour les outils Forge est double. D'une part, un rapport mal conçu peut nuire : un rang ou une moyenne de classe décourage les étudiants les plus faibles, qui sont précisément ceux qu'un quiz de diagnostic doit aider. D'autre part, un rapport bien conçu ne fait pas de miracle : les études ne montrent pas d'effet net des tableaux de bord sur les notes. L'axe sert donc surtout à fixer des règles de prudence (ce qu'il ne faut pas afficher) et des règles de forme (critère, diagnostic, action proposée), et à préparer une évaluation honnête de DiagForge.

Le public visé est celui de Forge : étudiants de L3 à M2 en mécanique et mathématiques, qui travaillent en ligne et en autonomie et reçoivent leur rapport sans enseignant à côté. Les études lues portent surtout sur des étudiants de licence ou de master dans d'autres disciplines (informatique, statistiques, formation des enseignants, sciences de la vie), parfois sur des lycéens ; aucune ne porte sur un rapport de quiz de diagnostic en sciences de l'ingénieur.

## Historique du domaine

**Les fondements : comparaison sociale et rétroaction.** Deux traditions de la psychologie précèdent les tableaux de bord. La première étudie la comparaison sociale : chacun juge ses capacités en se situant par rapport aux autres, ce qui peut motiver ou décourager selon la position. La seconde étudie la rétroaction : un retour efficace situe l'étudiant par rapport à un objectif et lui dit comment progresser, plutôt que de porter un jugement sur la personne (synthèse de [Wisniewski, Zierer et Hattie, 2020](../A_tests_retroaction/wisniewski2020.md), dans l'axe A). Les questions « où vais-je, où en suis-je, que faire ensuite » reviennent dans les études de cet axe ([theobald2022](theobald2022.md), [matcha2020](matcha2020.md)). Les modèles de l'apprentissage autorégulé (Pintrich, utilisé par [valle2021](valle2021.md) ; Winne et Hadwin, utilisé par [matcha2020](matcha2020.md)) donnent le cadre de la plupart des tableaux de bord : planifier, se surveiller, s'évaluer par rapport à un standard, s'adapter.

**Années 2010 : naissance des tableaux de bord étudiants.** L'analytique d'apprentissage (learning analytics), qui exploite les traces laissées par les étudiants sur les plateformes, se développe dans les années 2010, notamment autour de la conférence LAK où paraissent plusieurs études de cet axe. Les premiers tableaux de bord renvoient aux étudiants leurs traces d'activité, souvent à côté de la moyenne de la classe. La revue de [Bodily et Verbert (2017)](bodily2017.md), sur 93 articles publiés de 2005 à 2016, constate beaucoup de systèmes, peu d'évaluations de l'effet sur la réussite (15 % des articles) et un usage spontané faible (environ 30 % des étudiants).

**2019-2021 : le temps des critiques.** Deux revues systématiques montrent que les tableaux de bord reposent rarement sur une théorie, n'affichent ni standard ni stratégie ([Matcha et al., 2020](matcha2020.md)) et sont évalués par des questionnaires de satisfaction plutôt que par l'apprentissage qu'ils visent ([Valle et al., 2021](valle2021.md)). Les premiers essais comparent des formes de tableaux de bord : comparaison à des pairs choisis (article de congrès de 2020, version longue [Fleur et al., 2023](fleur2023.md)), prédiction de la note contre moyenne de classe ([Valle et al., 2021b](valle2021b.md)), scénarios où l'étudiant se voit sous ou au-dessus de la moyenne ([Harvey et Keyes, 2020](harvey2020.md) ; [Aguilar, 2022](aguilar2022.md)). En économie de l'éducation, une expérience naturelle sur plus de 40 000 lycéens grecs montre que connaître son rang aide les forts et pénalise les faibles ([Goulas et Megalokonomou, 2021](goulas2021.md)).

**2022-2026 : cadres de référence et action.** Les études récentes comparent directement critère, norme et soi ([Weidlich et al., 2024](weidlich2024.md)), relient l'état affiché à ce que l'étudiant fait ensuite ([Hatala et Nazeri, 2024](hatala2024.md) ; [Zheng et al., 2026](zheng2026.md), même équipe de l'université Simon Fraser) et passent de l'affichage de données à des recommandations ([Paulsen et Lindsay, 2024](paulsen2024.md) ; [Herodotou et al., 2025](herodotou2025.md)). La revue de [Kaliisa et al. (2024)](kaliisa2024.md) dresse le bilan : pas d'effet démontré des tableaux de bord sur la réussite.

## G1 — Partage des résultats et comparaison aux pairs

Un résultat peut être situé par rapport à un critère (« vous maîtrisez 6 notions sur 8 »), à la propre progression de l'étudiant, ou à ses camarades (moyenne, percentile, rang, groupe de pairs). Les études de cet axe convergent sur un point : la comparaison à la classe a des effets asymétriques. Connaître son rang fait progresser les meilleurs et reculer les plus faibles ([goulas2021](goulas2021.md)) ; se voir sous la moyenne baisse l'estime de soi sans rien apporter à ceux qui sont au-dessus ([harvey2020](harvey2020.md)) ; un percentile seul est le message le moins favorable pour la motivation ([weidlich2024](weidlich2024.md)). Un essai nuance ce tableau : se voir sous la moyenne ne nuit pas plus que le score seul, et se voir au-dessus réduit un peu la crainte de paraître moins bon ([aguilar2022](aguilar2022.md)).

Le cadre critérié est jugé le plus utile, mais il creuse lui aussi l'écart émotionnel entre étudiants au-dessus et au-dessous du critère ([weidlich2024](weidlich2024.md)) : la formulation pour ceux qui ne l'atteignent pas compte autant que le choix du cadre. Les comparaisons plus fines (petit groupe de pairs de même objectif, légèrement meilleurs) ont des résultats modestes et fragiles ([fleur2023](fleur2023.md)) ; l'effet annoncé d'IguideME sur l'autorégulation ne résiste pas à la lecture des données ([fleur2023b](fleur2023b.md)). L'évaluation par les pairs (double2020, li2020) relève d'un autre mécanisme et n'a pas de fiche ici.

## G2 — Tableaux de bord d'apprentissage

Les revues successives arrivent à la même conclusion : beaucoup de tableaux de bord, peu d'effets démontrés. Sur 38 études, pas d'effet net sur la réussite, un effet plus clair sur la participation ([kaliisa2024](kaliisa2024.md)) ; les évaluations confondent souvent utilisateurs motivés et outil, et mesurent la satisfaction plutôt que l'apprentissage visé ([valle2021](valle2021.md)). Les tableaux de bord décrivent et comparent, très rarement ils expliquent pourquoi ou disent quoi faire ([bodily2017](bodily2017.md) ; [matcha2020](matcha2020.md) ; [paulsen2024](paulsen2024.md)).

Les essais et études de traces apportent quelques règles de forme. Un retour qui situe l'étudiant par rapport à son objectif porte l'essentiel de l'effet, une suggestion de stratégie seule fait moins ([theobald2022](theobald2022.md)). Les recommandations (quoi revoir, qui contacter) sont la partie la plus appréciée ([herodotou2025](herodotou2025.md)). La prédiction de note n'améliore pas les résultats et peut décourager les étudiants peu motivés ([valle2021b](valle2021b.md)). La position affichée oriente l'action suivante : sous la référence on agit, au-dessus on s'arrête et on surveille ([hatala2024](hatala2024.md) ; [zheng2026](zheng2026.md)).

## Ce que disent les fiches

Synthèse rédigée à partir des 16 fiches de lecture écrites (les 4 de priorité 1 et 12 de priorité 2 ; 10 fiches ajoutées le 09/11/2026). Elle ne dit que ce que ces fiches soutiennent ; le niveau de preuve suit l'échelle de [fiches_methode.md](../fiches_methode.md).

**1. Ne pas promettre de gain de réussite.** Sur 38 études, les tableaux de bord étudiants n'ont pas d'effet démontré sur les notes ([kaliisa2024](kaliisa2024.md), niveau B). Les nouvelles fiches **confirment** : pas d'effet sur les notes d'un tableau prédictif ni d'un tableau descriptif pendant un semestre de statistiques en ligne ([valle2021b](valle2021b.md), niveau C), pas d'effet sur la note finale d'IguideME ([fleur2023b](fleur2023b.md)), effets mesurés dans 15 % seulement des 93 articles de [bodily2017](bodily2017.md), et « mitigés ». Le seul gain de note de cette série (d = 0,46, [theobald2022](theobald2022.md)) est exploratoire et déclaré par la moitié des participants (niveau C).

**2. Pas de rang ni de moyenne de classe comme repère.** Le percentile seul est le message le moins favorable ([weidlich2024](weidlich2024.md), niveau C) ; le rang réel aide les forts et pénalise les faibles ([goulas2021](goulas2021.md), niveau C). **Confirmé** : se voir sous la moyenne baisse l'estime de soi, sans bénéfice pour ceux qui sont au-dessus ([harvey2020](harvey2020.md), niveau C) ; des étudiants de statistiques cessent de consulter leur tableau quand ils se voient sous la moyenne ([valle2021b](valle2021b.md), témoignages, niveau D). **Nuancé** : sur les buts d'évitement, se voir sous la moyenne ne fait pas pire que le score seul, et se voir au-dessus aide un peu ([aguilar2022](aguilar2022.md), niveau C, une seule exposition, hors cours). La règle reste : la comparaison à la classe ne sert pas de levier pour les plus faibles.

**3. La position affichée oriente l'action, surtout chez ceux qui sont au-dessus.** Avec une moyenne de classe, les étudiants se jugent d'abord par rapport à elle ([zheng2026](zheng2026.md), niveau C). **Nouveau** : dans des forums notés, se voir sous la moyenne est suivi de plus de participation, se voir au-dessus de moins, et, avec un classement nominatif des 5 meilleurs, être à un seul message du classement ou dans le classement n'est pas suivi de publications, les étudiants classés revenant surtout surveiller leur place ([hatala2024](hatala2024.md), niveau C, association : l'état affiché n'est pas tiré au sort). D'où deux conséquences : pas de classement nominatif, et un objectif suivant pour ceux qui atteignent le critère.

**4. Le critère d'abord, puis la situation par rapport à l'objectif.** Le retour critérié est jugé le plus utile mais doit être formulé pour ceux qui ne l'atteignent pas ([weidlich2024](weidlich2024.md), niveau C). **Confirmé sur le plan théorique** : aucun des 266 indicateurs des tableaux de bord recensés par [matcha2020](matcha2020.md) n'affiche de standard, un seul porte sur les stratégies d'étude (constat de niveau C) ; afficher le seuil de maîtrise et une stratégie est une recommandation de niveau D. **Précisé** : un retour quotidien qui situe l'étudiant par rapport à ses objectifs réduit la procrastination déclarée le lendemain, et c'est cette situation, plus que la suggestion de stratégie, qui porte l'effet ([theobald2022](theobald2022.md), niveau B pour l'effet du retour, C pour la part de chaque ingrédient).

**5. Dire pourquoi et quoi faire ensuite.** Les recommandations sont la partie la plus appréciée d'un tableau de bord ([herodotou2025](herodotou2025.md), niveau C pour la préférence, D pour l'effet). **Confirmé, sans preuve d'effet** : 17 % seulement des systèmes combinent constat et recommandation ([bodily2017](bodily2017.md)), 6 tableaux de bord sur 39 seulement prescrivent une action et 7 publications expliquent pourquoi ([paulsen2024](paulsen2024.md)) (niveau D). **Nuancé** par [theobald2022](theobald2022.md) : la suggestion ne remplace pas la situation. Pour DiagForge, le leurre choisi permet de dire pourquoi une notion est manquée.

**6. Pas de prédiction de note.** La règle « pas de prédiction sans explication de son calcul » ([herodotou2025](herodotou2025.md), niveau D) est **renforcée** et devient « pas de prédiction de note par défaut » (niveau C) : dans un essai d'un semestre, une prédiction expliquée et assortie d'un avertissement n'a pas changé les notes et a fait baisser la motivation intrinsèque des étudiants peu motivés au départ ([valle2021b](valle2021b.md), niveau C). La baisse d'anxiété d'interprétation qu'elle apporte est incertaine (niveau D : hausse chez les plus anxieux).

**7. Comparaison aux pairs proches : prometteuse mais non établie.** La comparaison à un petit groupe de pairs de même objectif s'accompagne d'une note un peu plus haute dans deux petits essais ([fleur2023](fleur2023.md), niveau C). **Corrigé** : l'amélioration de la métacognition attribuée à IguideME ([fleur2023b](fleur2023b.md)) reproduit un écart présent avant l'intervention ; elle n'est pas établie (niveau D), ce qui lève la contradiction apparente avec [fleur2023](fleur2023.md).

**8. Évaluer correctement le rapport.** Tirage au sort entre accès et pas d'accès en gardant tous les étudiants ([kaliisa2024](kaliisa2024.md), niveau B) ; **nouveau** : écrire l'objectif du rapport avant de l'évaluer et mesurer ce qu'il vise, par exemple la réussite au quiz suivant sur les notions signalées, pas seulement la satisfaction ([valle2021](valle2021.md), niveau C) ; comparer des gains avant/après plutôt qu'un écart final ([fleur2023b](fleur2023b.md), niveau C) ; journaliser l'état affiché à chaque consultation ([hatala2024](hatala2024.md), niveau C).

## Règles pour DiagForge

**Contenu et forme du rapport**

| Règle | Niveau | Fiches |
| --- | --- | --- |
| Ne pas présenter le rapport comme un moyen d'améliorer les notes | B | kaliisa2024, valle2021b, bodily2017 |
| Pas de rang, de percentile individuel ni de classement nominatif ; jamais de position dans la classe sans la position par rapport au critère | C | weidlich2024, goulas2021, harvey2020, hatala2024 |
| Pas de moyenne de classe à côté du score individuel par défaut ; elle ne sert pas de levier pour les étudiants sous la moyenne | C | harvey2020, aguilar2022, zheng2026 |
| Le critère (seuil de maîtrise par notion) est affiché explicitement à côté du résultat et sert de repère principal ; la moyenne de classe vient après, ou pas du tout | C | weidlich2024, zheng2026, fleur2023, matcha2020 |
| Chaque message individuel suit le schéma objectif / situation / comment progresser ; la situation par rapport à l'objectif vient d'abord, la suggestion ne la remplace pas | C | weidlich2024, theobald2022, herodotou2025 |
| Sous le seuil de maîtrise, proposer une stratégie d'étude concrète (refaire tel exercice, revoir telle démonstration) en plus de la ressource | D | matcha2020, theobald2022 |
| Pour chaque notion manquée : une phrase de diagnostic tirée du leurre choisi, puis une ressource ou un exercice précis avec lien direct | D | paulsen2024, bodily2017, herodotou2025 |
| Indicateurs de maîtrise et directement actionnables (notions, exercices), pas des compteurs d'activité | D | matcha2020, hatala2024 |
| Au-dessus du critère : proposer aussi une suite (objectif suivant, exercice plus exigeant) plutôt qu'un simple constat | C | hatala2024 |
| Sous le critère ou en baisse : dire ce qui manque et quoi faire, sans verdict sur la capacité ni déclassement | D | weidlich2024, goulas2021, valle2021b |
| Si une comparaison aux pairs est affichée : petit groupe de niveau proche, formé de façon transparente (règle annoncée), cadré par un message orienté vers l'action | C | fleur2023, fleur2023b, zheng2026 |
| Pas de prédiction de note par défaut ; jamais sans explication de son calcul | C | valle2021b, herodotou2025, paulsen2024 |
| Une aide de lecture courte à la première apparition de chaque graphique | D | valle2021b |
| N'afficher que des valeurs réelles, sans manipulation de score ni de référence | D | aguilar2022, fleur2023 |
| Indiquer comment obtenir de l'aide | D | herodotou2025 |

**Diffusion et évaluation**

| Règle | Niveau | Fiches |
| --- | --- | --- |
| Envoyer le rapport (message Moodle ou courriel) après chaque quiz plutôt que de le déposer une fois en fin de module | D | bodily2017, theobald2022 |
| Journaliser chaque consultation du rapport avec l'état affiché (qui, quand, quelle position, quelles notions) | C | kaliisa2024, hatala2024, bodily2017 |
| Évaluer l'effet du rapport par tirage au sort en gardant tous les étudiants, jamais utilisateurs contre non-utilisateurs | B | kaliisa2024, fleur2023, valle2021b |
| Avant toute évaluation, écrire l'objectif du rapport et choisir une mesure alignée (réussite au quiz suivant sur les notions signalées), la satisfaction n'étant qu'une mesure secondaire | C | valle2021, kaliisa2024 |
| Comparer des gains avant/après entre groupes, pas seulement un écart final, en tenant compte du nombre de mesures comparées | C | fleur2023b |
| Tester une forme de restitution sur les étudiants les plus faibles avant de la généraliser | C | zheng2026, goulas2021, weidlich2024, valle2021b |

Ces règles sont reprises sous forme lisible par un programme dans l'en-tête de chaque fiche (champ `regles`).

## Ce qui reste ouvert

- Aucune fiche ne porte sur un rapport de quiz de diagnostic : les études concernent des notes de cours, des forums, des lectures annotées, un journal d'autorégulation ou des scénarios fictifs. La restitution de la répartition des réponses et des leurres choisis n'est évaluée par aucune.
- La comparaison à sa propre progression (quiz précédent) n'est testée isolément dans aucune fiche ; le tableau prédictif de [valle2021b](valle2021b.md), centré sur soi, mêle progression et prédiction. [zheng2026](zheng2026.md) la décrit comme favorable à l'espoir de quelques étudiants faibles, sans comparaison tirée au sort.
- Aucun essai ne mesure l'apprentissage après la restitution chez des étudiants proches des nôtres en mécanique ; l'essai le plus proche (statistiques en ligne, master, [valle2021b](valle2021b.md)) ne trouve pas d'effet sur les notes.
- Les petites classes (20 à 40 étudiants), où une moyenne est instable et une position facile à deviner, ne sont étudiées par aucune fiche.
- Les effets mesurés sont presque tous immédiats ou déclaratifs ; l'effet de rapports répétés sur un semestre reste inconnu.
- Montrer à toute la classe la répartition des réponses après un quiz, pratique courante en cours, n'a pas été trouvé comme objet d'étude contrôlée.
- Questions ouvertes par les fiches de priorité 2 : l'envoi du rapport augmente-t-il son ouverture et la participation au quiz suivant ([bodily2017](bodily2017.md)) ? Une phrase de diagnostic tirée du leurre choisi améliore-t-elle la réussite aux mêmes notions ([paulsen2024](paulsen2024.md)) ? Un objectif suivant relance-t-il l'activité des étudiants au-dessus du critère ([hatala2024](hatala2024.md)) ? Pour un rapport de quiz, la situation par notion suffit-elle, ou l'exercice conseillé ajoute-t-il quelque chose ([theobald2022](theobald2022.md)) ? Une prédiction de réussite décourage-t-elle aussi nos étudiants peu motivés ([valle2021b](valle2021b.md)) ?
- Priorité 3 non lue : double2020, li2020 (évaluation par les pairs), devreugd2025 (cadre de référence et fixation d'objectifs).

Chacune de ces questions peut faire l'objet d'un essai avec DiagForge ; les fiches proposent le dispositif (rubrique « Pour conclure, il faudrait »).

## Références

Références complètes : [`../forge.bib`](../forge.bib). La colonne « Fiche » donne le lien quand la fiche est écrite.

| Réf. (forge.bib) | Sous-axe | Apport | Priorité | Fiche |
| --- | --- | --- | --- | --- |
| `fleur2023` — Fleur et al. (2023) | G1 | comparaison avec 9 pairs de même objectif, légèrement au-dessus : note finale un peu plus haute et motivation extrinsèque maintenue, dans deux petits essais ; pas d'effet sur la métacognition | 1 | [fiche](fleur2023.md) |
| `weidlich2024` — Weidlich et al. (2024) | G1 | essai de terrain : percentile seul le moins favorable pour la motivation ; critère + norme sans perte ; critère seul creuse l'écart émotionnel entre étudiants au-dessus et au-dessous | 1 | [fiche](weidlich2024.md) |
| `aguilar2022` — Aguilar (2022) | G1 | panel en ligne, une exposition : « au-dessus de la moyenne » réduit un peu les buts d'évitement par rapport au score seul (d ≈ 0,3) ; « en dessous » ne diffère pas du score seul ; exclusions après tirage | 2 | [fiche](aguilar2022.md) |
| `fleur2023b` — Fleur et al. (2023b) | G1 | autre tableau de bord du même groupe (IguideME, pairs de même objectif) : écart de métacognition déjà présent avant l'intervention, effet sur l'autorégulation non établi ; résultat un peu meilleur sur 3 questions d'examen de haut niveau seulement (7,92 contre 6,79 sur 10) ; pas d'effet sur la note finale | 2 | [fiche](fleur2023b.md) |
| `goulas2021` — Goulas and Megalokonomou (2021) | G1 | expérience naturelle (lycée) : connaître son rang, forts +0,15 ET, faibles jusqu'à −0,3 ET, filles plus découragées | 2 | [fiche](goulas2021.md) |
| `harvey2020` — Harvey and Keyes (2020) | G1 | scénario fictif : se voir sous la moyenne de la classe baisse l'estime de soi immédiate ; pas de bénéfice au-dessus ; pas d'effet sur la persévérance ni le recours à l'aide | 2 | [fiche](harvey2020.md) |
| `hatala2024` — Hatala and Nazeri (2024) | G1, G2 | forums notés, traces : sous la moyenne de classe on publie plus, au-dessus moins ; un classement nominatif des 5 meilleurs ne pousse pas à agir ceux qui en sont proches (association, état non tiré au sort) | 2 | [fiche](hatala2024.md) |
| `double2020` — Double et al. (2020) | G1 | méta-analyse : l'évaluation par les pairs améliore les résultats (g ≈ 0,3) | 3 | sans fiche : priorité 3, non lue |
| `li2020` — Li et al. (2020) | G1 | méta-analyse : évaluation par les pairs plus efficace avec des évaluateurs formés | 3 | sans fiche : priorité 3, non lue |
| `kaliisa2024` — Kaliisa et al. (2024) | G2 | revue de 38 études : pas d'effet démontré des tableaux de bord sur la réussite, un peu sur la participation | 1 | [fiche](kaliisa2024.md) |
| `zheng2026` — Zheng et al. (2026) | G2, G1 | moyenne de classe (boîte à moustaches) contre 6 pairs légèrement meilleurs : la moyenne sert d'ancre ; les pairs proches soutiennent l'espoir de quelques étudiants faibles (étude descriptive) | 1 | [fiche](zheng2026.md) |
| `bodily2017` — Bodily and Verbert (2017) | G2 | revue de 93 articles : effets mesurés dans 15 % seulement, résultats mitigés ; usage spontané faible (environ 30 %) ; 17 % combinent constat et recommandation | 2 | [fiche](bodily2017.md) |
| `herodotou2025` — Herodotou et al. (2025) | G2 | Open University, 30 étudiants : les recommandations (quoi revoir, qui contacter) sont la partie la plus appréciée ; effet sur la réussite non mesuré | 2 | [fiche](herodotou2025.md) |
| `matcha2020` — Matcha et al. (2020) | G2 | revue de 29 tableaux de bord : aucun indicateur de standard ni de stratégie, plus des deux tiers sans théorie, 5 études expérimentales | 2 | [fiche](matcha2020.md) |
| `paulsen2024` — Paulsen and Lindsay (2024) | G2 | revue de 39 tableaux de bord : presque tous décrivent et comparent, 6 prescrivent une action ; tendance vers des tableaux fondés sur une théorie | 2 | [fiche](paulsen2024.md) |
| `theobald2022` — Theobald and Bellhäuser (2022) | G2 | retour automatique quotidien sur un journal d'apprentissage (30 jours) : moins de procrastination déclarée le lendemain ; la situation par rapport à l'objectif porte l'effet ; meilleure note d'examen en analyse exploratoire, note déclarée par la moitié des participants | 2 | [fiche](theobald2022.md) |
| `valle2021` — Valle et al. (2021) | G2 | revue de 28 études : objectifs surtout cognitifs, évaluations surtout par perceptions (6 sur 20 mesurent ce qu'elles visent) | 2 | [fiche](valle2021.md) |
| `valle2021b` — Valle et al. (2021b) | G2 | statistiques en ligne, un semestre : ni prédiction ni moyenne de classe ne changent les notes ; la prédiction baisse la motivation intrinsèque des peu motivés, réduit un peu l'anxiété d'interprétation | 2 | [fiche](valle2021b.md) |
| `devreugd2025` — de Vreugd et al. (2025) | G2 | ajouter un cadre de référence par les pairs change peu la fixation d'objectifs | 3 | sans fiche : priorité 3, non lue |

Priorité 1 = à lire d'abord. « Fiche » donne le lien vers la fiche de lecture `<clé>.md` de ce dossier, ou la raison de son absence.
