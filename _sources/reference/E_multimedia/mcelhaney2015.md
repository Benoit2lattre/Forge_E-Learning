---
cle: mcelhaney2015
reference: "McElhaney, K. W., Chang, H.-Y., Chiu, J. L. et Linn, M. C. (2015). Evidence for effective uses of dynamic visualisations in science curriculum materials. Studies in Science Education, 51(1), 49-85."
doi: 10.1080/03057267.2014.984506
axe: [E3]
type_etude: deux méta-analyses (47 comparaisons dynamique contre statique ; 76 comparaisons d'une caractéristique de conception), sciences, 2000-2012
public: du primaire au supérieur ; 37 comparaisons sur 47 dans le post-secondaire pour l'étude 1
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "accompagner chaque visualisation ou simulation d'une question qui oblige à l'interpréter (prédire, expliquer, comparer) plutôt que de la laisser seule"
    niveau: C
    transferabilite: moyenne
    note: "invites de questionnement g = 0,26 (k = 20) ; dans le post-secondaire, dynamique seul contre statique g = 0,07 ns"
  - outil: ExoForge
    regle: "dans une simulation, laisser varier un seul paramètre à la fois au début plutôt que tous les paramètres d'emblée"
    niveau: D
    transferabilite: forte
    note: "appuyé sur deux études contrastées citées p. 71, pas sur un résultat agrégé"
  - outil: CapsuleForge
    regle: "signaler visuellement (flèche, couleur, surbrillance) l'élément qui change au moment où il change dans une animation"
    niveau: C
    transferabilite: forte
    note: "repères visuels g = 0,50 (k = 20)"
  - outil: CapsuleForge
    regle: "présenter plusieurs représentations d'un même phénomène l'une après l'autre plutôt que simultanément"
    niveau: C
    transferabilite: moyenne
    note: "séquentielles g = 0,52 (k = 6) ; simultanées g = -0,02 (k = 8)"
  - outil: CapsuleForge
    regle: "ne pas ajouter de 3D quand une vue 2D suffit"
    niveau: C
    transferabilite: moyenne
    note: "3D g = 0,00 (k = 6)"
---

# Visualisations dynamiques en sciences : ce qui les rend utiles (McElhaney et al., 2015)

McElhaney, K. W., Chang, H.-Y., Chiu, J. L. et Linn, M. C. (2015). Evidence for effective uses of dynamic visualisations in science curriculum materials. *Studies in Science Education*, 51(1), 49-85. [DOI](https://doi.org/10.1080/03057267.2014.984506)

**En une phrase.** En sciences, une visualisation dynamique fait à peine mieux qu'une image fixe (g = 0,12, et 0,07 dans le supérieur), mais certaines aides la rendent nettement plus efficace : repères visuels, représentations successives, contrôle du déroulement, questions d'interprétation ; pour ExoForge et CapsuleForge, une animation ou une simulation ne vaut que par ce qui l'accompagne.

## La source

| | |
| --- | --- |
| **Équipe** | SRI International, National Kaohsiung Normal University, University of Virginia, UC Berkeley (Linn, projets WISE et TELS sur l'enseignement des sciences assisté par ordinateur). Part des études des auteurs dans le corpus non décomptée. |
| **Nature** | Académique ; financement de la National Science Foundation (DRL-0918743 et ESI-0334199, p. 75). |
| **Support** | *Studies in Science Education* (Taylor & Francis). |
| **Audience** | 151 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : bases, revues dépouillées, critères (p. 55-56, 64), listes des études (annexes 1 et 2) ; double codage de 50 % des études de l'étude 2 (accord > 95 %, p. 66). |

## Ce que fait l'étude

- **Recherche** (p. 55-56) : ERIC, PsycINFO, dépouillement de revues (dont *Journal of Engineering Education*) et d'actes, 2000-2012 ; visualisations informatiques de phénomènes scientifiques ou de systèmes mécaniques.
- **Étude 1** (p. 56-58) : 26 articles, 47 comparaisons dynamique contre statique, instruction identique par ailleurs ; modérateurs : cadre (classe ou laboratoire), niveau, durée, domaine, échelle, interactivité, nombre d'images fixes ; tests de rappel (33 effets) et d'inférence (39).
- **Étude 2** (p. 64-66) : 52 articles, 76 comparaisons qui isolent une caractéristique (repères visuels, invites, interactivité, représentations simultanées ou successives, 3D, narration personnalisée).
- **Analyse** (p. 58) : g de Hedges, effets indépendants par échantillon, effets aléatoires (Comprehensive Meta-Analysis).

## Résultats

**Étude 1** (p. 58-60, tableau 2)
- Effet global : g = 0,12, IC95 [−0,01 ; 0,24], p = 0,06 ; hétérogénéité forte (Q = 212,56, ddl = 46). Sans trois articles très négatifs, g = 0,27.
- Rappel g = 0,00 ; inférence g = 0,16, IC95 [0,02 ; 0,29].
- Post-secondaire g = 0,07 (k = 37, non significatif) ; primaire-secondaire g = 0,27 (k = 10).
- Durée longue (> 60 min) g = 0,33 contre 0,06 en séance courte (p = 0,02) ; classe 0,28 contre laboratoire 0,06 (p = 0,10).
- Interactivité nulle, simple ou complexe : 0,13, 0,11, 0,11 (non significatif).

**Étude 2** (p. 67, tableau 3) : effet global des améliorations g = 0,35, IC95 [0,25 ; 0,44].

| Caractéristique ajoutée | k | g |
| --- | --- | --- |
| Repères visuels | 20 | 0,50 |
| Représentations successives | 6 | 0,52 |
| Interactivité (rythme, segmentation, intégration active) | 10 | 0,45 |
| Narration personnalisée | 4 | 0,47 |
| Invites (prédire, expliquer, réfléchir) | 20 | 0,26 |
| Représentations simultanées | 8 | −0,02 |
| 3D | 6 | 0,00 |

- **Paramètres** (p. 71) : laisser l'étudiant régler six paramètres de mouvement nuit à la résolution de problèmes (Lee et al., 2004) ; faire varier une seule variable aide (Timpe et Wichmann, 2012).

## Avis critique

**Apport.** Déplace la question « animation ou image fixe ? » vers « avec quelles aides ? », avec des chiffres par type d'aide ; constat utile pour nous : sans aide, la visualisation dynamique n'apporte presque rien dans le supérieur.

**Points forts**
- Restreint aux sciences et à des comparaisons à instruction égale.
- Étude 2 limitée aux comparaisons qui isolent une seule caractéristique.
- Distinction rappel et inférence.

**Réserves**
1. **Importante** — Biais de publication mal contrôlé : pas de test d'Egger ni de trim and fill ; fail-safe N = 190 pour l'étude 2, que les auteurs jugent eux-mêmes insuffisant (p. 68). Les études d'amélioration de conception sont publiées surtout quand elles réussissent.
2. **Importante** — Sous-groupes petits (k = 4 à 10 pour plusieurs caractéristiques), comparaisons entre études ; « interactivité » regroupe contrôle du rythme, segmentation et intégration active.
3. **Mineure** — Les repères visuels sont souvent évalués sur exactement l'information signalée, ce qui peut gonfler l'effet ; les auteurs le notent (p. 69).
4. **Mineure** — Intervalle de prédiction et τ² non rapportés.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Seule, une visualisation dynamique apporte peu dans le supérieur | C | Sous-groupe de 37 comparaisons, non significatif ; absence de preuve d'effet |
| Les repères visuels améliorent l'apprentissage avec une animation | C | 20 comparaisons isolant la caractéristique, mais biais de publication non contrôlé ; à confronter à [schneider2018](schneider2018.md) |
| Représentations successives meilleures que simultanées | C | 6 et 8 comparaisons |
| Un paramètre à la fois plutôt que tous | D | Deux études citées, non agrégé |

**Transférabilité** : moyenne. Une grande part des comparaisons concerne le supérieur et des systèmes mécaniques, mais en laboratoire et en séances courtes.

**Pour conclure, il faudrait** comparer dans ExoForge une simulation de mécanique avec et sans question de prédiction avant manipulation, à temps égal, avec un test d'inférence différé.

## Pour Forge

- **ExoForge** : chaque simulation ou visualisation accompagnée d'une question de prédiction ou d'explication (niveau C).
- **ExoForge** : un paramètre à la fois au départ, avant l'exploration libre (niveau D).
- **CapsuleForge** : repères visuels synchronisés sur ce qui change (niveau C).
- **CapsuleForge** : représentations d'un même phénomène présentées successivement (niveau C) ; pas de 3D superflue (niveau C).
- À lire avec hoffler2007 et berney2016 (effet modeste de l'animation seule) et vlahos2026 (outil interactif en mécanique).
