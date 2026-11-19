---
cle: attali2017
reference: "Attali, Y. et van der Kleij, F. (2017). Effects of feedback elaboration and feedback timing during computer-based practice in mathematics problem solving. Computers & Education, 110, 154-169."
doi: 10.1016/j.compedu.2017.03.012
axe: [A2]
type_etude: essai randomisé en ligne (plan 2 × 2 × 2), paires d'items de même structure
public: 2 445 candidats adultes à un test d'admission (partie quantitative), États-Unis
lecture: texte complet, 08/11/2026
regles:
  - outil: QuizForge
    regle: "après une réponse fausse, donner une explication de la solution, pas seulement la bonne réponse"
    niveau: B
    transferabilite: forte
  - outil: QuizForge
    regle: "après une réponse juste, se limiter à confirmer et donner la bonne réponse ; l'explication peut rester accessible sur demande"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "donner le retour immédiatement et permettre de revoir le test corrigé ensuite"
    niveau: C
    transferabilite: forte
---

# Explication et moment du retour en mathématiques (Attali et van der Kleij, 2017)

Attali, Y. et van der Kleij, F. (2017). Effects of feedback elaboration and feedback timing during computer-based practice in mathematics problem solving. *Computers & Education*, 110, 154-169. [DOI](https://doi.org/10.1016/j.compedu.2017.03.012)

**En une phrase.** Sur des tests d'entraînement en mathématiques, l'explication de la solution aide à réussir un problème analogue seulement après une erreur ; après une bonne réponse elle n'apporte rien, et le meilleur moment du retour dépend aussi de la justesse de la première réponse.

## La source

| | |
| --- | --- |
| **Équipe** | Educational Testing Service (ETS, Princeton), concepteur de tests standardisés, et Australian Catholic University (van der Kleij, autrice de la méta-analyse de 2015). |
| **Nature** | Mixte : étude menée par l'organisme qui produit le test d'admission concerné, sur ses candidats. |
| **Support** | *Computers & Education* (Elsevier). |
| **Audience** | 131 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Faible : items issus du test (en partie publiés), données non disponibles ; plan expérimental bien décrit (p. 158-160). |

## Ce que fait l'étude

- **Participants** (p. 158) : 22 142 candidats invités à des tests d'entraînement quantitatifs 2 à 4 semaines avant l'examen ; 3 709 participants, dont 2 445 ayant passé au moins deux tests (âge moyen 25,6 ans).
- **Matériel** (p. 158-159) : sept tests de 20 questions ; 24 paires d'items de même structure placées dans deux tests consécutifs (au moins 2 h d'écart).
- **Conditions tirées au sort** (p. 159) : bonne réponse seule ou bonne réponse avec explication ; retour immédiat après chaque question ou après le test ; QCM ou réponse construite. Une erreur du système a attribué deux fois plus de participants à la bonne réponse seule.
- **Mesure** : probabilité de réussir la seconde version d'une paire selon la réponse à la première, le niveau initial et les conditions (régression logistique, p. 160-161).

## Résultats

- **Après une erreur** (p. 164-165) : l'explication augmente la réussite à la seconde version (b = 0,21 en log-odds), soit de 65 % à 69 % environ pour un participant moyen [calcul à partir de l'ordonnée à l'origine de 0,60, p. 164].
- **Après une bonne réponse** : l'explication ne fait pas mieux, et fait même un peu moins bien (non significatif).
- **Moment** (p. 164-165) : après une erreur, le meilleur résultat est le retour immédiat suivi d'une relecture du test corrigé, puis le retour différé, puis le retour immédiat sans relecture ; après une bonne réponse, le retour différé fait mieux.
- **Relecture** : avec retour différé, presque tous relisent ; avec retour immédiat, environ la moitié (moins encore avec explication) (fig. 2, p. 162).

## Avis critique

**Apport.** Montre que l'effet de l'explication dépend de la réponse de l'étudiant : utile après une erreur, inutile après une réussite. C'est un argument direct pour un retour qui s'adapte à la réponse.

**Points forts**
- Grand échantillon, tirage au sort de trois facteurs.
- Mesure fine : réussite à une question analogue juste après, selon la première réponse.
- Contexte réel de préparation à un examen.

**Réserves**
1. **Importante** — La relecture du test après coup est choisie par le participant : la comparaison « retour immédiat avec ou sans relecture » n'est pas randomisée.
2. **Importante** — Mesure de transfert très proche (items de même structure) et à court terme (test suivant).
3. **Importante** — Participants volontaires en préparation d'un examen à fort enjeu, qui font d'autres révisions en parallèle (p. 167) ; nombre de tests très variable (1 à 7).
4. **Mineure** — Effet de l'explication de quelques points de pourcentage seulement.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| L'explication aide après une erreur, pas après une bonne réponse | B | Essai randomisé, grand effectif, transfert proche |
| Retour immédiat puis relecture vaut mieux après une erreur | C | Relecture non randomisée |

**Transférabilité** : forte. Problèmes de mathématiques en ligne, adultes, QCM et réponses numériques comme dans QuizForge.

**Pour conclure, il faudrait** tester dans QuizForge un retour qui s'adapte à la réponse : explication détaillée après une erreur, simple confirmation après une réussite, avec une question analogue juste après.

## Pour Forge

- **QuizForge** : après une réponse fausse, afficher l'explication de la solution (niveau B).
- **QuizForge** : après une réponse juste, confirmer et laisser l'explication accessible sur demande (niveau C).
- **QuizForge** : retour immédiat, puis possibilité de revoir le test corrigé (niveau C).
- Une question analogue juste après l'explication (paire d'items) permet de vérifier que l'erreur est corrigée ; c'est aussi l'idée du second essai de Moreno et al. (2009, axe D).
