---
cle: matcha2020
reference: "Matcha, W., Ahmad Uzir, N., Gašević, D. et Pardo, A. (2020). A systematic review of empirical studies on learning analytics dashboards: A self-regulated learning perspective. IEEE Transactions on Learning Technologies, 13(2), 226-245."
doi: 10.1109/tlt.2019.2916802
axe: [G2]
type_etude: revue systématique (29 études empiriques de tableaux de bord, 2010 à septembre 2017), codage des 266 indicateurs selon le modèle d'autorégulation de Winne et Hadwin, grille de qualité ; sans méta-analyse
public: tableaux de bord d'apprentissage pour étudiants et enseignants, surtout dans le supérieur (informatique et ingénierie en majorité)
lecture: "texte complet, 09/11/2026"
regles:
  - outil: DiagForge
    regle: "afficher explicitement le standard visé (seuil de maîtrise par notion) à côté du résultat de l'étudiant"
    niveau: D
    transferabilite: forte
    note: "aucun des 266 indicateurs des 29 tableaux de bord recensés ne représentait un standard ou une évaluation par rapport à un standard"
  - outil: DiagForge
    regle: "privilégier les indicateurs de maîtrise (réussite par notion, erreurs typiques) aux indicateurs d'activité (connexions, nombre de tentatives, temps passé)"
    niveau: D
    transferabilite: forte
---

# Les tableaux de bord vus par la théorie de l'autorégulation (Matcha et al., 2020)

Matcha, W., Ahmad Uzir, N., Gašević, D. et Pardo, A. (2020). A systematic review of empirical studies on learning analytics dashboards: A self-regulated learning perspective. *IEEE Transactions on Learning Technologies*, 13(2), 226-245. [DOI](https://doi.org/10.1109/tlt.2019.2916802)

**En une phrase.** En codant les 266 indicateurs de 29 tableaux de bord évalués empiriquement, les auteurs constatent qu'aucun ne montre le standard que l'étudiant doit atteindre ni de stratégie d'apprentissage, que plus des deux tiers ne s'appuient sur aucune théorie, et que 5 études seulement comparent un groupe avec et sans tableau de bord : ces outils, disent-ils, ne peuvent pas soutenir la métacognition.

## La source

| | |
| --- | --- |
| **Équipe** | École d'informatique de l'université d'Édimbourg, faculté des technologies de l'information de Monash (Melbourne), université d'Australie-Méridionale ; Gašević et Pardo sont des figures de l'analytique d'apprentissage. |
| **Nature** | Académique ; financements de la Commission européenne (projets LALA et EMBED) et de l'Australian Research Council (page de titre). Les auteurs défendent une approche fondée sur la théorie, qu'ils formalisent dans leur propre modèle (MULAS). |
| **Support** | *IEEE Transactions on Learning Technologies*. Renvois aux sections, tableaux et figures. |
| **Audience** | 472 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Moyenne : requête et bases publiées, double codage (accord 86,7 %, κ = 0,64), liste des études en annexe (tableau VIII) ; grille de qualité construite pour l'étude. Sans objet pour les chiffres d'effet. |

## Ce que fait l'étude

- **Recherche** (§ III, figure 2) : « dashboard AND (learning analytics OR educational data mining) » dans ACM, IEEE, SpringerLink, ScienceDirect, Wiley et Google Scholar ; 488 articles, 140 sur les tableaux de bord, 29 avec une évaluation empirique.
- **Codage** (§ III, tableaux I à IV) : chaque indicateur affiché est rattaché aux éléments du modèle COPES de Winne et Hadwin (conditions, opérations, produits, évaluations, standards) et aux quatre phases de l'autorégulation (définition de la tâche, objectifs et planification, mise en œuvre, adaptation).
- **Qualité** (§ III, figure 11) : grille de 13 questions inspirée d'outils de recherche médicale.

## Résultats

- **Théorie** (§ IV.A.2 et § V.A) : la majorité des tableaux de bord ne s'appuient sur aucune théorie de l'apprentissage (69 % en § IV.A.2, 68 % en § V.A).
- **Indicateurs** (§ IV.A.3, tableau VI) : 266 indicateurs ; 66 « opérations primitives » (connexions, messages, questions répondues), 74 de connaissances du domaine (scores, exercices réussis), 80 motivationnels (surtout des badges) ; un seul sur les tactiques d'étude ; **aucun** sur les standards ni sur l'évaluation par rapport à un standard.
- **Phases** (§ IV.A.4) : 2 indicateurs seulement pour la phase « objectifs et planification ».
- **Cadres de référence** (§ IV.B, figure 5) : pour les tableaux de bord étudiants, indicateurs individuels surtout, puis comparaison à la moyenne des pairs (31) et de la classe (32) ; un seul face aux meilleurs.
- **Qualité des études** (§ IV.C) : 5 études avec groupe expérimental et témoin ; 11 rapportent leurs limites ; aucune ne discute la généralisation ; évaluation surtout par questionnaires d'utilisabilité.
- **Recommandations** (§ V.C) : fonder les indicateurs sur une théorie ; inclure standards et stratégies ; répondre aux trois questions « où vais-je, où en suis-je, que faire ensuite » ; laisser l'étudiant contester son modèle.

## Avis critique

**Apport.** La revue montre, indicateur par indicateur, ce qui manque aux tableaux de bord : le standard (le critère) et la stratégie. C'est l'argument théorique de la règle « le critère d'abord » de cet axe, que [weidlich2024](weidlich2024.md) teste ensuite expérimentalement.

**Points forts**
- Grille théorique explicite appliquée à chaque indicateur.
- Double codage avec accord rapporté.
- Évaluation de la qualité des études, rare dans le domaine.

**Réserves**
1. **Importante** — Revue de conception, pas d'effets : elle ne montre pas qu'un tableau de bord avec standards fonctionne mieux. Les recommandations sont déduites de la théorie, et le modèle proposé est celui des auteurs.
2. **Mineure** — Recherche limitée au mot « dashboard » et à 2017 ; codage parfois fait à partir de captures d'écran (§ VI) ; chiffre « sans théorie » donné à 69 % et 68 % selon la section.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les tableaux de bord recensés n'affichent ni standard ni stratégie | C | Codage systématique et double, corpus de 2017 |
| Afficher le standard et la stratégie rendrait le tableau de bord plus efficace | D | Déduction théorique non testée dans la revue |
| Les preuves d'effet causal manquent | C | 5 études expérimentales sur 29 |

**Transférabilité** : forte pour les principes de conception ; le corpus est surtout en informatique et ingénierie dans le supérieur.

**Pour conclure, il faudrait** comparer, dans DiagForge, un rapport « score par notion » et un rapport « score par notion + seuil de maîtrise + stratégie », et mesurer l'exactitude de l'auto-évaluation de l'étudiant avant le quiz suivant.

## Pour Forge

- **DiagForge** : afficher le standard (seuil de maîtrise) à côté du résultat (niveau D) ; **confirme** sur le plan théorique la règle « le critère est le repère principal » ([weidlich2024](weidlich2024.md), niveau C).
- **DiagForge** : indicateurs de maîtrise plutôt que d'activité (niveau D) ; voir [hatala2024](hatala2024.md) (indicateurs actionnables).
