---
cle: aguilar2022
reference: "Aguilar, S. J. (2022). Experimental evidence of performance feedback vs. mastery feedback on students' academic motivation. In LAK22: 12th International Learning Analytics and Knowledge Conference (p. 556-562). ACM."
doi: 10.1145/3506860.3506916
axe: [G1]
type_etude: expérience en ligne randomisée à trois conditions (score seul, « au-dessus de la moyenne », « en dessous de la moyenne »), une seule exposition, mesures auto-déclarées immédiates (N = 445 analysés sur 620)
public: étudiants américains de premier cycle recrutés par un panel en ligne (âge moyen 25,8 ans), hors de tout cours
lecture: "texte complet, 09/11/2026"
regles:
  - outil: DiagForge
    regle: "ne pas compter sur la position par rapport à la moyenne pour motiver les étudiants en difficulté : se savoir en dessous de la moyenne ne change rien par rapport au score seul, et le bénéfice ne concerne que ceux qui sont au-dessus"
    niveau: C
    transferabilite: moyenne
  - outil: DiagForge
    regle: "ne jamais modifier ni inventer un score ou une moyenne de référence pour produire un effet de comparaison : la restitution affiche les vraies valeurs"
    niveau: D
    transferabilite: forte
    note: "l'étude ajoute ou retire 5 points au score et fixe une moyenne fictive de 80 % ; acceptable en laboratoire, pas dans un cours"
---

# Score seul ou position par rapport à la moyenne (Aguilar, 2022)

Aguilar, S. J. (2022). Experimental evidence of performance feedback vs. mastery feedback on students' academic motivation. In *LAK22: 12th International Learning Analytics and Knowledge Conference* (p. 556-562). ACM. [DOI](https://doi.org/10.1145/3506860.3506916)

**En une phrase.** Après un test de calcul de proportions, 445 étudiants voient au hasard leur score seul, ou leur score présenté comme au-dessus ou en dessous d'une moyenne fictive de 80 % ; ceux qui se voient au-dessus déclarent un peu moins de buts d'évitement (ne pas paraître moins bon que les autres) que ceux qui ont le score seul, tandis que se voir en dessous ne change rien par rapport au score seul : l'effet est petit, immédiat et mesuré hors de tout cours.

## La source

| | |
| --- | --- |
| **Équipe** | Un seul auteur, école d'éducation de l'université de Californie du Sud ; travaux antérieurs sur les tableaux de bord et la recherche d'information motivée (questionnaire MISQ, Aguilar et Baek, 2019, cité dans l'article). |
| **Nature** | Académique ; financement non rapporté ; aucune déclaration de conflit d'intérêts. L'auteur utilise son propre questionnaire (MISQ). |
| **Support** | Actes de la conférence LAK (ACM), 7 pages, libre accès (CC BY-NC). |
| **Audience** | 15 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Faible à moyenne : conditions décrites (formules de score, figure 2), moyennes et écarts-types publiés (tableau 2) ; items du test et données non publiés. La démarche se refait ; les chiffres se vérifient en partie. L'article n'ayant que 7 pages en double colonne, les renvois se font aux sections et tableaux. |

## Ce que fait l'étude

- **Participants** (§ 2.1, tableau 1) : 620 étudiants inscrits dans le supérieur américain (hiver 2020), recrutés et rémunérés par un panel Qualtrics, équilibrés sur le sexe et la bourse Pell ; 445 retenus après exclusions.
- **Tâche** (§ 2.2, § 2.3.3) : test de 20 questions de raisonnement proportionnel (« 16 % de 80 », « 6/5 + 17/7 »), score brut borné artificiellement entre 4/20 et 16/20.
- **Trois conditions** tirées au sort (§ 2.2.1, figure 2) : score brut seul (témoin dit « maîtrise ») ; score + 5 points présenté comme au-dessus de « l'étudiant moyen » à 80 % ; score − 5 points présenté comme en dessous. Les scores et la moyenne sont donc manipulés.
- **Mesures** (§ 2.3) : buts d'accomplissement (PALS : maîtrise, approche-performance, évitement-performance) et orientation de recherche d'information (MISQ), échelles en 5 points, une seule fois juste après le retour.
- **Exclusions** (§ 2.4) : 137 étudiants (22 %) ratent les questions de contrôle d'attention ; 38 autres sont exclus parce que leur score affiché ne correspondait pas à leur condition (par exemple « en dessous » avec un score affiché au-dessus de 80 %).
- **Analyse** (§ 2.5) : ANOVA à un facteur par mesure, puis test de Tukey.

## Résultats

| Mesure (échelle 1 à 5) | Au-dessus (n = 122) | En dessous (n = 156) | Score seul (n = 167) | Source |
| --- | --- | --- | --- | --- |
| Buts d'évitement-performance | 3,48 (0,93) | 3,64 (0,95) | 3,76 (0,80) | tableau 2 |
| Recherche d'information, évitement | 2,87 (0,92) | 3,19 (1,09) | 3,17 (0,83) | tableau 2 |
| Score au test de calcul | 17,1 (2,30) | 15,4 (3,70) | 15,0 (3,63) | tableau 2 |

- **Buts d'évitement** (§ 3.1, tableau 3) : F(2, 442) = 3,66, p = 0,027 ; seule la différence « score seul contre au-dessus » est significative (+0,286 ; p = 0,019) ; d ≈ 0,33 [calcul : 0,286 rapporté à l'écart-type commun des deux groupes, 0,86].
- **Recherche d'information d'évitement** (§ 3.2, tableau 3) : F(2, 442) = 4,29, rapporté p = 0,009 (p ≈ 0,014 d'après F et ses degrés de liberté [calcul]) ; « en dessous contre au-dessus » +0,322 (p = 0,015) et « score seul contre au-dessus » +0,300 (p = 0,023) ; d ≈ 0,35 [calcul].
- **Ce qui ne bouge pas** (tableau 2 et 3) : buts de maîtrise, buts d'approche-performance et les deux autres orientations de recherche d'information ; « en dessous » ne diffère jamais du score seul (p = 0,43 et 0,98).
- **Interprétation de l'auteur** (§ 4) : la comparaison « n'a pas toujours besoin d'être évitée » ; effet « subtil mais causal ».

## Avis critique

**Apport.** Un des rares essais qui isolent le cadre de référence d'un retour chiffré. Il nuance l'idée que toute comparaison à la moyenne est nuisible : au moment du retour, le message « en dessous » ne fait pas pire que le score seul, et le message « au-dessus » apaise un peu la crainte de paraître moins bon.

**Points forts**
- Tirage au sort, trois bras de taille suffisante, seule la présentation du score change.
- Deux questionnaires validés, résultats concordants entre les deux.
- Moyennes, écarts-types et contrastes publiés : les tailles d'effet se recalculent.

**Réserves**
1. **Majeure** — Exclusions après tirage au sort selon le score obtenu (38 étudiants « mal classés », § 2.4) : les groupes ne sont plus comparables. Le groupe « au-dessus » a un meilleur score au test (17,1 contre 15,0, tableau 2) ; la différence de motivation peut venir du niveau en mathématiques et non du message. Le tableau 2 donne d'ailleurs des moyennes au test supérieures au maximum annoncé de 16/20, ce qui empêche de vérifier la règle de construction.
2. **Importante** — Situation artificielle : panel rémunéré, test sans enjeu, score et moyenne fictifs, une seule exposition, mesure immédiate ; l'auteur le reconnaît (§ 4).
3. **Importante** — Six mesures testées, deux significatives, sans correction entre mesures ; p de la deuxième ANOVA incohérent avec F (0,009 rapporté, 0,014 recalculé).
4. **Mineure** — Pourcentages du tableau 1 incohérents avec les effectifs (169 étudiants de première année = « 3,67 % ») ; les données démographiques portent sur 483 personnes et non sur les 445 analysées [calcul : 238 femmes = 49,28 % de 483].

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Se savoir au-dessus de la moyenne réduit un peu les buts d'évitement par rapport au score seul | C | Un essai, effet petit, exclusions après tirage qui déséquilibrent les groupes, une seule exposition |
| Se savoir en dessous ne nuit pas plus que le score seul | C | Absence de différence, mesure immédiate et sans enjeu |
| La comparaison à la moyenne a un effet durable dans un cours | D | Non mesuré |

**Transférabilité** : moyenne. Étudiants du supérieur et contenu mathématique, mais hors cours, sans enjeu et sur une seule exposition ; le mécanisme (cadre de référence) se transpose, pas la taille de l'effet.

**Pour conclure, il faudrait** tirer au sort, dans un cours réel avec DiagForge, la restitution « score par notion seul » contre « score + position par rapport à la moyenne de la classe », avec les vraies valeurs, et suivre la participation et la réussite au quiz suivant chez les étudiants au-dessous et au-dessus de la moyenne.

## Pour Forge

- **DiagForge** : la position par rapport à la moyenne n'aide pas les étudiants sous la moyenne ; elle ne doit pas servir de levier de motivation (niveau C). Cela nuance sans contredire [weidlich2024](weidlich2024.md) (percentile seul défavorable) et [harvey2020](harvey2020.md) (estime de soi plus basse sous la moyenne).
- **DiagForge** : n'afficher que des valeurs réelles ; aucune manipulation de score ou de référence (niveau D, règle de déontologie).
- Voir aussi [goulas2021](goulas2021.md) (rang réel en lycée : gain pour les forts, perte pour les faibles).
