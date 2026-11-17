---
cle: orthaber2020
reference: "Orthaber, M., Stütz, D., Antretter, T. et Ebner, M. (2020). Concepts for E-Assessments in STEM on the Example of Engineering Mechanics. International Journal of Emerging Technologies in Learning (iJET), 15(12), 136-152."
doi: 10.3991/ijet.v15i12.13725
axe: [H1]
type_etude: rapport de conception (questions d'examen de mécanique dans Moodle), sans données d'étudiants
public: examen de mécanique de l'ingénieur, Montanuniversität Leoben (Autriche) ; environ 1 000 copies par an
lecture: texte complet, 10/11/2026
regles:
  - outil: ExoForge
    regle: "report d'erreur par recalcul des étapes suivantes à partir des saisies de l'étudiant, de préférence à la navigation à sens unique qui affiche les résultats intermédiaires justes"
    niveau: D
    transferabilite: forte
    note: "l'affichage de la bonne valeur révèle si la démarche était juste et peut décourager (p. 140) ; argument, non mesuré"
  - outil: ExoForge
    regle: "si un résultat intermédiaire juste est affiché pour la suite, l'afficher aussi sous forme littérale avec les données de l'énoncé"
    niveau: D
    transferabilite: forte
  - outil: ExoForge
    regle: "diagramme du corps libre en glisser-déposer : plus d'étiquettes que de zones, étiquettes réutilisables et étiquette vide « aucun effort » pour limiter le hasard ; ne pas le présenter comme équivalent au tracé à main levée"
    niveau: D
    transferabilite: forte
  - outil: ExoForge
    regle: "dans la phase de mise en place, recueillir les brouillons et les comparer aux saisies pour repérer les erreurs et les démarches que l'exercice ne capte pas"
    niveau: D
    transferabilite: forte
  - outil: QuizForge
    regle: "saisie numérique sans unité (question à variables de Moodle) : imposer l'unité dans l'énoncé et le dire dans la consigne"
    niveau: D
    transferabilite: forte
---

# Questions d'examen de mécanique en ligne avec report d'erreur (Orthaber et al., 2020)

Orthaber, M., Stütz, D., Antretter, T. et Ebner, M. (2020). Concepts for E-Assessments in STEM on the Example of Engineering Mechanics. *International Journal of Emerging Technologies in Learning (iJET)*, 15(12), 136-152. [DOI](https://doi.org/10.3991/ijet.v15i12.13725)

**En une phrase.** Les auteurs montrent comment transposer dans Moodle un problème d'examen de mécanique en plusieurs étapes (diagramme du corps libre en glisser-déposer, valeurs à paramètres aléatoires, saisie algébrique STACK) et comparent deux façons de gérer le report d'erreur ; c'est une description de conception, sans aucune donnée d'étudiants.

## La source

| | |
| --- | --- |
| **Équipe** | Institut de mécanique, Montanuniversität Leoben, et département de technologie éducative, université technique de Graz (p. 136, 152). Fondé sur un mémoire de licence de D. Stütz (p. 137). |
| **Nature** | Académique ; financement non rapporté. Les auteurs décrivent leurs propres questions. |
| **Support** | *iJET*, revue en libre accès ; « version finale publiée telle que soumise par les auteurs » (p. 152). |
| **Audience** | 10 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Moyenne pour la démarche (étapes STACK décrites, figures 6 à 11, p. 144-147) ; sans objet pour les résultats, qui n'existent pas. |

## Ce que fait l'étude

- **Contexte** (p. 136-137) : Moodle utilisé depuis 6 ans pour la partie théorique ; partie pratique sur papier, environ 1 000 copies de 2 problèmes par an, 10 min de correction par problème, soit environ 330 h par an (1 000 x 2 x 10 min = 333 h [calcul]).
- **Question** (p. 137) : peut-on évaluer en ligne, avec une validité suffisante, des problèmes complexes de mécanique, et avec quelles limites ?
- **Deux exemples** : dimensionnement d'un arbre en navigation à sens unique (p. 140-143) ; calcul d'efforts et de moments avec STACK et saisie vectorielle (p. 143-147).

## Résultats

- **Report d'erreur, première solution** (p. 140, 142-143) : problème découpé en sous-parties, navigation vers l'avant seulement ; après chaque partie, la bonne valeur est affichée, avec son expression littérale, pour la suite. Inconvénients notés : pas de retour en arrière, et l'étudiant apprend si sa démarche était juste, ce qui peut le décourager.
- **Report d'erreur, seconde solution** (p. 140, 145-146) : STACK recalcule les résultats suivants à partir de la saisie de l'étudiant ; une valeur fausse de S suivie de calculs justes donne des points pour la suite. Les arbres de décision de STACK permettent aussi de sauter des contrôles devenus impossibles (p. 146).
- **Diagramme du corps libre** (p. 141-142) : glisser-déposer sur une image ; toutes les zones doivent être remplies ; étiquettes réutilisables et étiquette vide pour une zone sans effort, afin de rendre la question moins devinable.
- **Saisies** (p. 142-144) : valeurs tirées dans des bornes qui gardent un sens physique ; unité imposée et non saisie, à dire dans la consigne (p. 143) ; en STACK, syntaxe stricte (rho lu comme une variable et non r*h*o) et aperçu de l'expression interprétée avant validation (p. 144, 146).
- **Limites** (p. 148-149) : le glisser-déposer est plus facile que le tracé ; la démarche disparaît en notation automatique, d'où la nécessité de choisir les sous-étapes notées ; garder les brouillons comme filet de sécurité et pour vérifier les saisies pendant la transition (p. 146-147).
- **Recommandation** (p. 149) : d'abord en formatif, puis un examen mixte (un problème en ligne, un sur papier).

## Avis critique

**Apport.** Mode d'emploi concret, en mécanique et dans Moodle, de deux choix qu'ExoForge doit faire : comment gérer le report d'erreur et comment évaluer un diagramme du corps libre.

**Points forts**
- Exemples de mécanique de l'ingénieur proches des nôtres.
- Inconvénients de chaque solution discutés, limites énoncées (p. 148-149).
- Étapes de construction STACK détaillées.

**Réserves**
1. **Majeure** — Aucune donnée : pas d'étudiants, pas de taux de réussite, pas d'indice de discrimination, alors que le résumé annonce des indices de discrimination « suffisamment élevés » (p. 136). La validité affirmée en conclusion (p. 149) n'est pas démontrée.
2. **Importante** — Les effets de l'affichage des bonnes valeurs sur l'étudiant (découragement, indice sur la démarche) sont des suppositions.
3. **Mineure** — Aucune analyse des erreurs types des étudiants : le report d'erreur traite l'erreur comme une valeur fausse, sans la nommer.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Un problème de mécanique en plusieurs étapes peut se transposer dans Moodle avec report d'erreur | D | Démonstration de faisabilité, sans passation |
| Le recalcul à partir des saisies vaut mieux que l'affichage des valeurs justes | D | Argument des auteurs |
| Le glisser-déposer facilite le diagramme du corps libre par rapport au tracé | D | Remarque des auteurs, non mesurée |

**Transférabilité** : forte pour la conception (mêmes outils Moodle et STACK, même discipline) ; aucun résultat chiffré à transférer.

**Pour conclure, il faudrait** faire passer un même problème de statique dans ExoForge en deux versions tirées au sort (affichage de la valeur juste ou recalcul à partir des saisies), et comparer notes, abandons et accord avec une correction des brouillons.

## Pour Forge

- **ExoForge** : report d'erreur par recalcul à partir des saisies ; si une valeur juste est affichée, la donner aussi en littéral ; diagramme du corps libre en glisser-déposer avec étiquettes en surnombre et étiquette vide ; comparaison aux brouillons pendant la mise en place (niveau D).
- **QuizForge** : unité imposée et annoncée dans les questions numériques sans saisie d'unité (niveau D). Nuance la règle de l'axe « faire saisir l'unité » (niveau D) : les deux choix existent, il faut en annoncer un.
- Renvois : `pearson2022` (report d'erreur et crédit partiel, seule mesure chiffrée de l'axe) ; `greenhow2015`, `gill2007` (même principe en mécanique) ; `davies2024` (STACK à l'échelle d'un département) ; `steif2005` (oubli d'une force difficile à tester par choix).
