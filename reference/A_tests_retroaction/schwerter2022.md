---
cle: schwerter2022
reference: "Schwerter, J., Wortha, F. et Gerjets, P. (2022). E-learning with multiple-try-feedback: Can hints foster students' achievement during the semester? Educational Technology Research and Development, 70(3), 713-736."
doi: 10.1007/s11423-022-10105-z
axe: [A3]
type_etude: essai randomisé intra-individuel sur un semestre (alternance des conditions d'une séance à l'autre)
public: 87 étudiants de 3e semestre de sociologie, cours de statistique (Allemagne)
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "après une réponse fausse, donner un indice sur l'étape clé (formule, démarche) et laisser un nouvel essai, avant de montrer la bonne réponse"
    niveau: B
    transferabilite: forte
  - outil: QuizForge
    regle: "pour les questions à réponse numérique, autoriser plusieurs essais (par exemple trois) avec un indice entre les essais"
    niveau: C
    transferabilite: forte
---

# Essais multiples avec indices (Schwerter et al., 2022)

Schwerter, J., Wortha, F. et Gerjets, P. (2022). E-learning with multiple-try-feedback: Can hints foster students' achievement during the semester? *Educational Technology Research and Development*, 70(3), 713-736. [DOI](https://doi.org/10.1007/s11423-022-10105-z)

**En une phrase.** Dans les séances d'exercices en ligne d'un cours de statistique, ajouter un indice aux essais multiples (au lieu de la seule bonne réponse) améliore la réussite pendant la séance et sur une question d'examen une semaine plus tard.

## La source

| | |
| --- | --- |
| **Équipe** | TU Dortmund et Leibniz-Institut für Wissensmedien (Tübingen) ; recherche en éducation et technologies d'apprentissage. |
| **Nature** | Académique ; réseau doctoral LEAD financé par l'Initiative d'excellence allemande (p. 713). |
| **Support** | *Educational Technology Research and Development* (Springer), en libre accès. |
| **Audience** | 20 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : environnement (Qualtrics, MathJax) et plan décrits, exemple d'écran (p. 723-724) ; données non publiées. |

## Ce que fait l'étude

- **Cours** (p. 717-718) : statistique pour les sciences sociales (probabilités, lois, estimation, tests, régression), 3e semestre de licence de sociologie, université publique allemande, hiver 2018-2019 ; 87 étudiants analysés.
- **Séances** (p. 722-724) : 12 séances d'exercices en salle informatique, chacune avec un test différé (question d'examen de la semaine précédente), une phase d'exercices et un test immédiat (nouvelle question d'examen).
- **Conditions** : trois essais par champ de réponse ; après une erreur, bonne réponse seule (MCR) ou indice sur l'étape clé avec un nouvel essai (MCR + H). Exemple : pour un écart-type, l'indice rappelle qu'il faut utiliser la variance estimée et montre où elle entre dans la formule (p. 723).
- **Tirage au sort** (p. 723) : la moitié des étudiants commence par une condition, l'autre moitié par l'autre, puis alternance chaque semaine. Un incident technique a déséquilibré les deux premières séances ; les analyses sans ces séances donnent les mêmes résultats.
- **Analyse** : régressions de panel à effets aléatoires avec contrôles (préparation, présence au cours, note du cours précédent) (p. 725-726).

## Résultats

- **Pendant la séance** (tableau 4, p. 727) : avec indices, +3,7 points de réussite (+4,7 sur les exercices effectivement atteints) ; 14,3 % d'erreurs en moins. Regarder les vidéos de préparation compte davantage (+10,9 points).
- **Test immédiat** : pas de différence significative.
- **Test différé d'une semaine** : meilleure réussite après une séance avec indices (p. 727-728).
- **Examen final** : pas d'effet de groupe attendu ni trouvé, chaque étudiant ayant eu les deux conditions ; la réussite dans les séances prédit la note (p. 729-730).

## Avis critique

**Apport.** Essai en situation réelle, sur un semestre, qui montre qu'un indice entre deux essais fait mieux que la bonne réponse donnée tout de suite, y compris une semaine après.

**Points forts**
- Tirage au sort à l'intérieur de chaque étudiant, sur 12 séances.
- Test différé à une semaine.
- Indices décrits avec des exemples concrets.

**Réserves**
1. **Importante** — Petit effectif (87 étudiants) et effets de quelques points ; le test différé repose sur une seule question d'examen par semaine.
2. **Importante** — Absence d'effet au test immédiat, que les auteurs expliquent par la fatigue ou l'habitude du retour : le résultat différé est donc à confirmer.
3. **Mineure** — Les indices ont été mis à disposition de tous après chaque séance (p. 724) : la différence mesurée une semaine plus tard est d'autant plus notable, mais elle porte sur un écart d'exposition limité.
4. **Mineure** — Public de sociologie ; calculs de statistique plus courts que nos exercices de mécanique.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Un indice entre deux essais améliore la réussite pendant la séance | B | Essai randomisé intra-individuel, 12 séances |
| L'effet tient une semaine plus tard | C | Une question par semaine, pas d'effet immédiat |

**Transférabilité** : forte. Exercices de calcul en ligne avec réponses numériques et formules en MathJax, comme ExoForge.

**Pour conclure, il faudrait** reprendre la même alternance dans ExoForge sur un cours de mécanique, avec plusieurs questions au test différé.

## Pour Forge

- **ExoForge** : après une réponse fausse, un indice ciblé sur l'étape clé et un nouvel essai, avant la bonne réponse (niveau B). C'est la logique « indice puis réessayer » à rapprocher de Moreno et al. (2009, axe D).
- **QuizForge** : pour les réponses numériques, trois essais avec un indice entre les essais (niveau C).
- À distinguer de Say et al. (2023) : ici, l'indice aide sans donner la réponse ; ce qui pose problème, c'est un retour qui permet de trouver la bonne option par élimination.
