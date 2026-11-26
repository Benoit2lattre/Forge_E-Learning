---
cle: rhodes2015
reference: "Rhodes, M. T. et Sarbaum, J. K. (2015). Online homework management systems: Should we allow multiple attempts? The American Economist, 60(2), 120-131."
doi: 10.1177/056943451506000203
axe: [A3]
type_etude: quasi-expérimental, deux sessions d'été successives du même cours en ligne (deux tentatives contre une), sans tirage au sort
public: 100 étudiants (40 et 60) d'un cours en ligne d'introduction à la macroéconomie, université de Caroline du Nord à Greensboro
lecture: texte complet, 09/11/2026
regles:
  - outil: QuizForge
    regle: "devoir noté : ne pas combiner plusieurs tentatives sur les mêmes questions, note de la meilleure tentative et relecture « juste/faux par question » entre deux tentatives ; ce réglage gonfle la note sans gain à l'examen"
    niveau: C
    transferabilite: moyenne
    note: "réglages Moodle concernés : nombre de tentatives, méthode d'évaluation, options de relecture « immédiatement après la tentative »"
  - outil: QuizForge
    regle: "si plusieurs tentatives sont permises, changer les questions d'une tentative à l'autre (tirage dans une banque, questions calculées à valeurs aléatoires) ou noter la moyenne des tentatives"
    niveau: D
    transferabilite: forte
    note: "proposition des auteurs, non testée (p. 130)"
  - outil: ExoForge
    regle: "à chaque nouvelle tentative d'un exercice noté, tirer de nouvelles valeurs des paramètres"
    niveau: D
    transferabilite: forte
  - outil: DiagForge
    regle: "ne pas lire la note « meilleure tentative » d'un devoir à tentatives multiples comme une mesure de maîtrise ; analyser la première tentative"
    niveau: C
    transferabilite: forte
---

# Faut-il autoriser plusieurs tentatives aux devoirs en ligne ? (Rhodes et Sarbaum, 2015)

Rhodes, M. T. et Sarbaum, J. K. (2015). Online homework management systems: Should we allow multiple attempts? *The American Economist*, 60(2), 120-131. [DOI](https://doi.org/10.1177/056943451506000203)

**En une phrase.** Quand un devoir QCM en ligne peut être refait une seconde fois après avoir vu quelles questions étaient fausses, avec la meilleure note retenue, la note des devoirs monte de 4 à 15 points mais pas celle des examens, et les étudiants travaillent moins à la première tentative : pour QuizForge, ce trio de réglages Moodle est à éviter pour un devoir noté.

## La source

| | |
| --- | --- |
| **Équipe** | Économistes : College of Coastal Georgia et université de Caroline du Nord à Greensboro ; les auteurs enseignent le cours étudié. |
| **Nature** | Académique ; financement non rapporté ; avis d'un comité d'éthique jugé non nécessaire (p. 120). Les auteurs évaluent leurs propres réglages. |
| **Support** | *The American Economist* (Sage), revue d'économie, rubrique enseignement. |
| **Audience** | 23 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Faible : pas de données individuelles publiées ni de caractéristiques des étudiants ; réglages décrits précisément (p. 121-122) ; les tableaux de tests se vérifient en partie. Pages de la revue (120 à 131). |

## Ce que fait l'étude

- **Cours** (p. 121) : macroéconomie d'introduction en ligne, deux sessions d'été de 5 semaines en 2012 (40 et 60 inscrits) ; 10 devoirs (les 8 meilleurs comptent, 10 % chacun) et 2 examens ; mêmes contenus et mêmes réglages sauf un.
- **Devoirs** (p. 121) : MyEconLab, 8 à 15 questions (11 en moyenne), 98 % de QCM à 4 ou 5 options ; une question à la fois, réponse obligatoire pour avancer ; correction publiée après la date limite.
- **Variable** (p. 122) : session 1, deux tentatives ; après la première, score et liste des questions manquées ; seconde tentative sur les mêmes questions dans le même ordre ; meilleure des deux notes retenue. Session 2, une tentative, score seul.
- **Examens** (p. 121, 124) : 23 questions sur Blackboard, 4 h ; seules les questions fermées (QCM, vrai/faux, numériques) sont comparées.
- **Analyse** (p. 124-129) : tests t de différences de moyennes par devoir, unilatéraux et bilatéraux ; contrefactuel : la session à une tentative reçoit une seconde tentative fictive au hasard (note G + (100 − G) x P, P = 1/4 ou 1/3) ; la différence restante est attribuée au « réapprentissage », le reste à la devinette.

## Résultats

- **Devoirs** (tableau 1, p. 125) : la session à deux tentatives a de meilleures notes, de +4 à +15 points selon le devoir ; significatif en bilatéral (p < 0,05) pour 7 devoirs sur 10 [décompte].
- **Temps** (tableau 1, p. 125-126) : temps total semblable ou un peu plus long (−3 à +12 min), significatif en bilatéral pour 1 devoir sur 10 [décompte] ; à l'évaluation de fin de cours, 59 % (une tentative) contre 46 % (deux tentatives) déclarent avoir travaillé « plus que la moyenne ».
- **Examens** (tableau 2, p. 126) : différences de −0,23 et +0,20 point, non significatives.
- **Première tentative** (tableau 3, p. 127) : avec deux tentatives, la première est moins réussie (−1 à −7 points) et plus courte (−12 à −15 min sur les 3 premiers devoirs, p < 0,05 unilatéral).
- **Devinette** (tableaux 4 et 5, p. 129-130) : après le contrefactuel, le gain dû au réapprentissage n'est net que pour 2 à 4 devoirs ; gonflement de la note estimé à 5 à 13 points par devoir et 4,9 à 7,5 points sur la note du cours.
- **Propositions** (p. 130) : noter la moyenne des tentatives, tirer les questions d'une banque assez variée, générer des valeurs numériques aléatoires ; réduire le poids des devoirs ne supprime pas la devinette.

## Avis critique

**Apport.** Seule étude de l'axe qui teste un réglage de devoir noté (nombre de tentatives, meilleure note, retour entre tentatives) sur la note finale et sur l'examen : elle met en évidence un effet pervers concret des tentatives multiples sur les mêmes questions.

**Points forts**
- Une seule variable change entre deux sessions du même cours, même enseignant et même matériel.
- Mesure du temps passé et de la première tentative, qui éclaire le mécanisme.
- Réglages décrits assez précisément pour être reproduits dans Moodle.

**Réserves**
1. **Majeure** — Pas de tirage au sort, pas de données individuelles (niveau d'entrée, prétest) : la comparaison repose sur deux groupes de 40 et 60 et sur des indices indirects (moyenne cumulée déclarée, plus favorable à la session à une tentative, p. 122).
2. **Importante** — La décomposition devinette / réapprentissage repose sur un contrefactuel simplifié (devinette pure, options supposées toutes à 4 ou toutes à 5) ; elle borne l'effet, elle ne le mesure pas.
3. **Importante** — La seconde tentative montrait quelles questions étaient fausses sur des questions identiques, ce qui rend l'élimination facile ; le résultat ne dit rien de tentatives avec questions renouvelées, indices ou explication.
4. **Mineure** — Tests unilatéraux mis en avant ; formulations confuses des hypothèses testées (p. 124-127) ; quelques coquilles dans les tableaux ; cours d'économie de 5 semaines.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Deux tentatives (meilleure note, questions identiques) augmentent la note des devoirs sans changer l'examen | C | Quasi-expérimental, deux petits groupes, examen comme critère |
| Les étudiants s'investissent moins dans la première tentative | C | Temps et score de la première tentative, déclarations |
| Une grande partie du gain vient de la devinette | C | Contrefactuel simplifié |
| Moyenne des tentatives ou questions renouvelées suppriment le problème | D | Proposition non testée |

**Transférabilité** : moyenne. Devoirs QCM en ligne notés, comme nos quiz Moodle ; public et discipline différents (économie, premier cycle américain, cours d'été).

**Pour conclure, il faudrait** comparer, dans une même promotion et par tirage au sort, deux tentatives avec « meilleure note » et deux tentatives avec questions calculées à valeurs nouvelles (ou « moyenne des tentatives »), en mesurant la première tentative et l'examen.

## Pour Forge

- **QuizForge** : pour un devoir noté, éviter la combinaison « plusieurs tentatives + mêmes questions + meilleure tentative + relecture juste/faux par question juste après la tentative » (niveau C). Les réglages Moodle concernés sont le nombre de tentatives, la méthode d'évaluation (meilleure note, moyenne, première ou dernière tentative) et les options de relecture.
- **QuizForge** : si plusieurs tentatives, renouveler les questions (questions aléatoires tirées d'une catégorie, questions calculées) ou noter la moyenne (niveau D).
- **ExoForge** : nouvelles valeurs des paramètres à chaque tentative (niveau D) ; ExoForge tire déjà des paramètres, la règle porte sur le réglage des tentatives du paquet SCORM.
- **DiagForge** : analyser la première tentative (niveau C).
- Rejoint [say2023](say2023.md) : avec plusieurs essais, un retour question par question permet de trouver la réponse par élimination. À distinguer des essais multiples **à l'intérieur d'une question** avec indice ([schwerter2022](schwerter2022.md)) ou crédit partiel ([slepkov2019](slepkov2019.md)), qui ne se confondent pas avec des tentatives répétées du devoir entier.
