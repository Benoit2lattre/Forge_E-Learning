---
cle: greenhow2015
reference: "Greenhow, M. (2015). Effective computer-aided assessment of mathematics; principles, practice and results. Teaching Mathematics and its Applications, 34, 117-137."
doi: 10.1093/teamat/hrv012
axe: [H1, H3]
type_etude: article de principes (retour d'expérience d'un auteur) avec analyse descriptive de 272 843 réponses à 809 questions sur six ans ; pas de groupe témoin
public: première année d'économie, module de mathématiques (environ 200 à 340 étudiants par an), université Brunel (Royaume-Uni)
lecture: texte complet (version en ligne avancée, pagination « n of 21 »), 08/11/2026
regles:
  - outil: ExoForge
    regle: "choisir les plages de paramètres à partir de la solution (rétro-conception) : exclure 0 et 1, garder des valeurs qui ne changent ni la méthode ni la difficulté, et regrouper en variantes distinctes ce qui change la difficulté (signes négatifs, formule fournie ou non)"
    niveau: D
    transferabilite: forte
  - outil: ExoForge
    regle: "vérifier, sur l'ensemble des tirages possibles, qu'aucun leurre issu d'une erreur type ne coïncide avec la clé ou avec un autre leurre"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "remplacer la saisie numérique simple par la saisie réactive : comparer la réponse à la clé puis à chaque erreur type, retour propre à l'erreur reconnue, sinon retour général"
    niveau: D
    transferabilite: forte
  - outil: ExoForge
    regle: "découper une question synthétique en parties, avec report de la saisie (même fausse) dans le calcul des parties suivantes, pour savoir quelle compétence manque"
    niveau: D
    transferabilite: forte
  - outil: QuizForge
    regle: "dans les QCM à paramètres, inclure une option « aucune de ces réponses » qui est parfois la bonne, et prévoir alors assez de leurres pour remplir toutes les options"
    niveau: D
    transferabilite: forte
  - outil: DiagForge
    regle: "suivre par question la réussite et la corrélation avec le score du test, et signaler en cours de semestre les questions et les thèmes difficiles ou peu discriminants"
    niveau: C
    transferabilite: forte
---

# Principes de l'évaluation assistée en mathématiques (Greenhow, 2015)

Greenhow, M. (2015). Effective computer-aided assessment of mathematics; principles, practice and results. *Teaching Mathematics and its Applications*, 34, 117-137. [DOI](https://doi.org/10.1093/teamat/hrv012)

**En une phrase.** Synthèse de quinze ans de pratique : questions à paramètres aléatoires choisis par rétro-conception, leurres et réponses numériques reconnues codés comme erreurs types (mal-rules), saisie numérique réactive, avec 272 843 réponses analysées en réussite et discrimination ; c'est un guide de conception pour ExoForge, pas une évaluation de l'effet sur l'apprentissage.

## La source

| | |
| --- | --- |
| **Équipe** | Un auteur, département de mathématiques de l'université Brunel ; auteur des systèmes Mathletics et maths e.g. qu'il évalue. |
| **Nature** | Académique ; évaluation de son propre dispositif et de son propre module. Financement non rapporté. |
| **Support** | *Teaching Mathematics and its Applications* (IMA, Oxford University Press). Pages citées dans la numérotation de la version en ligne (« n of 21 »). |
| **Audience** | 28 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Faible pour les résultats (données non publiées, figures sans valeurs dans le texte) ; principes de conception assez décrits pour être appliqués. Matériel d'évaluation téléchargeable selon l'auteur (p. 20). |

## Ce que fait l'étude

- **Principes** (p. 2-8) : limites de l'évaluation automatique (pas de preuve, pas de schéma saisi), choix des paramètres, codage des erreurs types, avantages et défauts de chaque type de question.
- **Intégration au module** (p. 9-10) : séances en salle encadrées ; jusqu'à 12 tests par module, meilleure note sur les cinq premières tentatives ; réussite réelle à l'examen exigée pour valider le module.
- **Données** (tableau 1, p. 7 ; p. 11-12) : 809 questions, 46 246 tests, 272 843 réponses de 2008-09 à 2013-14 ; réussite et corrélation question-test.
- **Difficulté** (p. 15-18) : hypothèse d'une « entropie » = logarithme du nombre d'états accessibles par les erreurs types, examinée sur la question la plus facile et la plus difficile de chaque thème.

## Résultats

- **Paramètres** (p. 4-5) : la valeur tirée peut changer la méthode (1/(x² + 4x + c) factorisable pour c = 3, carré parfait pour c = 4) ; une matrice 3x3 tirée au hasard donne en général des valeurs propres non calculables à la main.
- **Leurres** (p. 7) : un leurre 2a pour « a² » est faux si a peut valoir 2 (deux réponses 4 affichées). Avec « aucune de ces réponses », quatre leurres sont nécessaires.
- **Saisie réactive** (p. 8) : la réponse est comparée à la clé, puis à chaque erreur type ; sans correspondance, le retour peut être « je pense que vous devinez ».
- **Réussite par thème** (tableau 1, p. 7) : de 0,053 à 0,985 en saisie numérique ; pas de différence nette entre QCM et saisie numérique (p. 12), comparaison possible seulement pour les thèmes ayant assez de QCM.
- **Discrimination** (fig. 5, p. 11-14) : corrélation question-test élevée sauf pour les questions les plus faciles ; valeurs non données dans le texte.
- **Examen** (fig. 4, p. 12 ; annexe p. 20-21) : hausse des résultats après l'introduction en 2008-09 ; une hausse inexpliquée en 2011/12 ; critères d'admission relevés en 2009 et 2010 ; rattrapage : 50 réussites sur 55 en 2011, 23 sur 23 en 2012, 18 sur 19 en 2013.
- **Difficulté** (p. 15-18) : l'« entropie » classe la plus facile et la plus difficile de chaque thème, mais la familiarité avec les concepts et la mise en équation (énoncés longs) semblent dominer pour les questions les plus dures.

## Avis critique

**Apport.** Le texte le plus complet sur la conception concrète de questions à paramètres aléatoires avec erreurs types : rétro-conception des tirages, unicité des leurres sur tous les tirages, saisie réactive, report d'une saisie fausse dans les parties suivantes.

**Points forts**
- Règles de conception précises, avec exemples et contre-exemples.
- Très grand volume de réponses réelles, sur six ans.
- Limites reconnues (pas de taxonomie d'erreurs utilisable à grande échelle, p. 6 ; entropie trop simple, p. 18).

**Réserves**
1. **Majeure** — L'amélioration de l'examen (fig. 4) est une comparaison avant-après avec changement des critères d'admission, de l'enseignant (l'auteur reprend toute la promotion en 2009-10) et de l'examen ; la conclusion « performance nettement améliorée » (p. 18) n'est pas attribuable au dispositif.
2. **Importante** — La qualité des questions est jugée par la corrélation avec le test, sans valeurs ni seuils dans le texte ; la corrélation inclut la question dans le total (voir `slepkov2021`).
3. **Importante** — Public d'économie de première année, contenu de niveau lycée à L1 ; pas de mécanique.
4. **Mineure** — Mesure de difficulté par « entropie » examinée sur deux questions par thème, après coup.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les erreurs types doivent être vérifiées sur tous les tirages | C | Argument logique et exemples, pas de mesure de fréquence des collisions |
| La saisie réactive vaut mieux que la saisie simple | D | Opinion de l'auteur, non testée |
| Les questions sont « robustes et valides » | C | Réussite et corrélation sur un grand corpus, sans seuils publiés |
| Le dispositif améliore l'examen | D | Avant-après avec plusieurs changements simultanés |

**Transférabilité** : forte pour les principes de construction (mathématiques de l'ingénieur) ; faible pour les résultats chiffrés.

**Pour conclure, il faudrait** mesurer dans ExoForge la part des tirages où une erreur type coïncide avec la clé (voir [sikurajapathi2023](sikurajapathi2023.md)) et comparer saisie simple et saisie réactive par tirage au sort.

## Pour Forge

- **ExoForge** : rétro-conception des plages de paramètres et variantes distinctes quand la difficulté change (D) ; vérification des leurres sur tous les tirages (C) ; saisie réactive (D) ; questions en plusieurs parties avec report d'erreur (D), voir [pearson2022](pearson2022.md).
- **QuizForge** : option « aucune de ces réponses » parfois correcte (D).
- **DiagForge** : réussite et discrimination par question suivies pendant le semestre (C), avec l'indicateur item exclu de `slepkov2021`.
- Renvois : [gill2007](gill2007.md), [gill2008](gill2008.md) (même équipe, mécanique).
