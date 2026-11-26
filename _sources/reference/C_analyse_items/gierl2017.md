---
cle: gierl2017
reference: "Gierl, M. J., Bulut, O., Guo, Q. et Zhang, X. (2017). Developing, analyzing, and using distractors for multiple-choice tests in education: A comprehensive review. Review of Educational Research, 87(6), 1082-1116."
doi: 10.3102/0034654317726529
axe: [C2, B2]
type_etude: revue narrative de la littérature sur les leurres
public: évaluation en éducation, tous niveaux
lecture: texte complet, 08/11/2026
regles:
  - outil: QuizForge
    regle: "écrire chaque leurre à partir d'une erreur type ou d'une conception erronée identifiée, pas au hasard"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "pour une réponse numérique, construire les leurres en refaisant le calcul avec l'erreur type (facteur oublié, inversé, mauvaise unité)"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "après usage, repérer les leurres choisis par très peu d'étudiants et les réécrire ou les supprimer"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "mélanger l'ordre des options, sauf pour les valeurs numériques, présentées dans l'ordre"
    niveau: D
    transferabilite: forte
---

# Écrire et analyser les leurres (Gierl et al., 2017)

Gierl, M. J., Bulut, O., Guo, Q. et Zhang, X. (2017). Developing, analyzing, and using distractors for multiple-choice tests in education: A comprehensive review. *Review of Educational Research*, 87(6), 1082-1116. [DOI](https://doi.org/10.3102/0034654317726529)

**En une phrase.** La revue de référence sur les leurres : les écrire à partir des erreurs courantes des étudiants ou par similarité avec la bonne réponse, les analyser après usage (taux de choix, courbes selon le niveau), en mettre deux plutôt que trois ou quatre, et mélanger l'ordre des options sauf pour les valeurs ordonnées.

## La source

| | |
| --- | --- |
| **Équipe** | Centre de mesure appliquée de l'université de l'Alberta ; Gierl est spécialiste de la génération automatique d'items. |
| **Nature** | Académique. |
| **Support** | *Review of Educational Research* (AERA), revue de synthèse de référence. |
| **Audience** | 271 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : bases et mots-clés de recherche indiqués (p. 1086-1087), pas de critères de sélection quantifiés. |

## Ce que fait l'article

- **Écrire les leurres** (p. 1088) : deux stratégies, (1) partir des erreurs et conceptions erronées courantes (réponses à des questions ouvertes, entretiens, avis d'experts : « avec quoi les étudiants confondent-ils cette notion ? ») ; (2) partir de la similarité avec la bonne réponse (même catégorie, même forme ; pour une valeur numérique, refaire le calcul en retirant ou en inversant un facteur).
- **Analyser les leurres** (p. 1088-1096) : part d'étudiants qui choisissent chaque leurre, niveau moyen de ceux qui le choisissent, courbes de choix selon le niveau ; modèles de réponse aux items à réponse nominale, fonctionnement différentiel, modèles diagnostiques.
- **Règles d'usage** (p. 1096-1097) : leurres plausibles, indépendants, homogènes, sans indice, formulés positivement ; « aucune » et « toutes les réponses » avec prudence.
- **Nombre d'options** (p. 1098-1099) : trois options (deux leurres) recommandées par plusieurs études, en particulier la méta-analyse de Rodriguez (2005).
- **Ordre** (p. 1099-1101) : pas de consensus ; ordre logique ou numérique, ou ordre aléatoire pour la sécurité et l'égalité ; la position de la bonne réponse peut modifier la difficulté.
- **Six recommandations** (p. 1101-1103) et perspectives sur la génération automatique de leurres (p. 1103-1107).

## Avis critique

**Apport.** Rassemble en un seul texte tout ce qu'un générateur de QCM doit savoir sur les leurres : comment les écrire, comment vérifier qu'ils fonctionnent, combien en mettre.

**Points forts**
- Revue large (de 1929 à 2017) et recommandations explicites.
- Lien direct entre écriture des leurres et analyse après usage, donc entre QuizForge et DiagForge.
- Méthodes de génération automatique adaptées aux réponses numériques.

**Réserves**
1. **Importante** — Revue narrative : pas de quantification des effets ni d'évaluation de la qualité des études ; les recommandations reprennent souvent des guides d'experts.
2. **Mineure** — Les auteurs promeuvent la génération automatique d'items, leur propre domaine.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les meilleurs leurres viennent des erreurs courantes des étudiants | C | Consensus des guides, peu d'essais directs |
| Trois options suffisent | B | Méta-analyse de Rodriguez (2005) citée, confirmée par Sridharan et Sivaramakrishnan (2025) |
| Ordre des options | D | Pas de consensus |

**Transférabilité** : forte. La construction des leurres numériques par erreur de calcul correspond exactement aux règles erronées d'ExoForge (axe H).

**Pour conclure, il faudrait** comparer, dans QuizForge, des leurres tirés des erreurs types et des leurres écrits librement, par leur taux de choix et leur discrimination.

## Pour Forge

- **QuizForge** : un leurre = une erreur type nommée (« oubli du facteur 2 », « signe inversé », « mauvaise unité ») ; pour les valeurs numériques, recalcul avec l'erreur (niveau C).
- **QuizForge** et **DiagForge** : après usage, signaler les leurres choisis par moins de 5 % des étudiants et ceux choisis surtout par les bons étudiants (niveau C ; seuils traités dans l'axe C).
- **QuizForge** : mélanger les options, sauf les valeurs numériques présentées dans l'ordre croissant (niveau D).
