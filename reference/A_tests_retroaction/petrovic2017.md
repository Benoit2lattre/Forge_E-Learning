---
cle: petrovic2017
reference: "Petrović, J., Pale, P. et Jeren, B. (2017). Online formative assessments in a digital signal processing course: Effects of feedback type and content difficulty on students learning achievements. Education and Information Technologies, 22(6), 3047-3061."
doi: 10.1007/s10639-016-9571-0
axe: [A2]
type_etude: quasi-expérimental, trois promotions successives (sans quiz, bonne réponse, explication)
public: étudiants en traitement du signal, faculté d'électrotechnique de Zagreb (70, 34 et 35 étudiants)
lecture: texte complet, 08/11/2026
regles:
  - outil: QuizForge
    regle: "mettre à disposition des quiz formatifs en ligne, tirés d'une banque, avant chaque contrôle"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "ne pas supposer qu'une explication détaillée vaut toujours mieux que la bonne réponse : mesurer sur ses propres cours"
    niveau: D
    transferabilite: forte
---

# Quiz en ligne en traitement du signal (Petrović et al., 2017)

Petrović, J., Pale, P. et Jeren, B. (2017). Online formative assessments in a digital signal processing course: Effects of feedback type and content difficulty on students learning achievements. *Education and Information Technologies*, 22(6), 3047-3061. [DOI](https://doi.org/10.1007/s10639-016-9571-0)

**En une phrase.** Dans un cours de traitement du signal, des quiz formatifs en ligne avec la bonne réponse sont associés à de meilleurs résultats aux contrôles que l'absence de quiz, et, de façon inattendue, à de meilleurs résultats que des quiz avec explication sur le contenu le plus difficile ; mais les groupes sont trois promotions différentes.

## La source

| | |
| --- | --- |
| **Équipe** | Faculté d'électrotechnique et d'informatique de l'université de Zagreb ; enseignants du cours étudié. |
| **Nature** | Académique ; les auteurs évaluent leur propre cours. |
| **Support** | *Education and Information Technologies* (Springer). |
| **Audience** | 66 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Faible : banques de questions et données non publiées ; dispositif décrit (p. 3051-3052). |

## Ce que fait l'étude

- **Cours** : traitement numérique du signal, sept séances de travaux pratiques ; trois contrôles écrits au début des séances 2, 3 et 4 (p. 3051).
- **Quiz formatifs** (p. 3051) : trois quiz de QCM tirés de banques (10 questions parmi 80, 6 parmi 20, 10 parmi 80), 10 minutes, nombre d'essais illimité ; les questions diffèrent de celles des contrôles mais portent sur les mêmes notions. Contenus de difficulté moyenne, faible et élevée.
- **Groupes** (p. 3052) : promotion 2013-2014 sans quiz (70), 2014-2015 avec la bonne réponse (34), 2015-2016 avec explication (bonne réponse, erreur de raisonnement probable, développement, lien vers le cours) (35). Pas de tirage au sort ; les notes de travaux pratiques servent de covariables.

## Résultats

- **Usage** : plus de 90 % des étudiants utilisent les quiz (résumé, p. 3047).
- **Bonne réponse contre sans quiz** : meilleurs résultats aux contrôles, d = 0,69 à 1,08 selon le contenu (p. 3055).
- **Bonne réponse contre explication** : la bonne réponse fait mieux sur le contenu le plus difficile (d = 0,88) (p. 3055).
- **Comportement** : pas de différence de nombre d'essais, de score ni de temps de résolution entre les deux groupes avec quiz ; seul le temps entre deux essais est plus long avec l'explication, sur le quiz le plus difficile (p. 3056).

## Avis critique

**Apport.** Un des rares travaux en génie électrique sur des quiz formatifs en ligne ; il confirme l'intérêt des quiz et rappelle que l'explication n'est pas automatiquement meilleure.

**Points forts**
- Cours réel de niveau licence en ingénierie, proche de nos cours de signal.
- Questions des quiz différentes de celles des contrôles.
- Les auteurs discutent eux-mêmes les limites (p. 3056-3057).

**Réserves**
1. **Majeure** — Chaque condition est une promotion différente : l'effet du type de retour est confondu avec l'année (niveau d'entrée, contrôles, contexte). Les covariables de travaux pratiques ne suffisent pas à l'écarter (les auteurs le reconnaissent, p. 3056).
2. **Importante** — Petits groupes (34 et 35) pour la comparaison bonne réponse contre explication.
3. **Importante** — Nombre d'essais illimité sur des banques limitées (20 questions pour l'un des quiz) : les étudiants peuvent retenir les réponses, et l'avantage de la bonne réponse peut venir d'essais plus rapides et plus nombreux.
4. **Mineure** — Pas d'explication du résultat contraire à la littérature au-delà d'hypothèses.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Des quiz formatifs en ligne améliorent les contrôles en traitement du signal | C | Comparaison entre promotions, effet grand |
| La bonne réponse fait mieux que l'explication sur un contenu difficile | D | Promotions différentes, 35 étudiants, contraire aux méta-analyses |

**Transférabilité** : forte pour le contexte (ingénierie, signal) ; faible pour les conclusions sur le type de retour.

**Pour conclure, il faudrait** comparer les deux types de retour dans la même promotion, par tirage au sort des étudiants ou des questions, comme dans Attali et van der Kleij (2017).

## Pour Forge

- **QuizForge** : quiz formatifs tirés d'une banque avant chaque contrôle (niveau C, conforté par Yang et al., 2021).
- **QuizForge** : ne pas tenir pour acquis qu'une explication longue vaut mieux que la bonne réponse ; l'effet dépend de la réponse de l'étudiant (Attali et van der Kleij, 2017) et peut être mesuré dans nos cours (niveau D ici).
