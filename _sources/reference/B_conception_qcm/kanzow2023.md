---
cle: kanzow2023
reference: "Kanzow, A. F., Schmidt, D. et Kanzow, P. (2023). Scoring single-response multiple-choice items: Scoping review and comparison of different scoring methods. JMIR Medical Education, 9, e44084."
doi: 10.2196/44084
axe: [B3]
type_etude: revue de la portée (scoping review) des barèmes du QCM à réponse unique et calculs des scores attendus
public: sans objet (calculs) ; contexte des examens de médecine et d'odontologie
lecture: texte complet, 09/11/2026
regles:
  - outil: QuizForge
    regle: "QCM à réponse unique : barème 1 point pour la bonne réponse, 0 sinon, sans point négatif"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "afficher le score au hasard (1/n) et le seuil qui correspond à 50 % de connaissances (50 % + 50 %/n : 75 % pour 2 options, 66,7 % pour 3, 62,5 % pour 4, 60 % pour 5)"
    niveau: B
    transferabilite: forte
  - outil: QuizForge
    regle: "si une pénalité est imposée sur une question à réponse unique, la fixer à −1/(n−1) : le score au hasard tombe à 0 et le seuil à 50 % quel que soit n"
    niveau: B
    transferabilite: forte
  - outil: QuizForge
    regle: "dans un même quiz, ne pas mélanger sans correction des questions à 2 options (vrai/faux) et à 4-5 options : signaler l'écart de score au hasard ou noter les parties séparément"
    niveau: C
    transferabilite: forte
---

# Barèmes du QCM à réponse unique (Kanzow et al., 2023)

Kanzow, A. F., Schmidt, D. et Kanzow, P. (2023). Scoring single-response multiple-choice items: Scoping review and comparison of different scoring methods. *JMIR Medical Education*, 9, e44084. [DOI](https://doi.org/10.2196/44084)

**En une phrase.** 21 barèmes existent pour le QCM à réponse unique ; tous donnent une note proportionnelle aux connaissances, mais le score au hasard et le seuil de réussite varient énormément ; les auteurs recommandent le barème 1/0 sans point négatif, avec un seuil relevé selon le nombre d'options (60 % pour 5 options, 75 % pour 2, pour exiger 50 % de connaissances).

## La source

| | |
| --- | --- |
| **Équipe** | Centre médical universitaire de Göttingen (doyenné des études, odontologie) ; mêmes auteurs que [Schmidt et al. (2021)](schmidt2021.md) et [Schmidt et al. (2022)](schmidt2022.md). |
| **Nature** | Académique ; frais de publication payés par le fonds de l'université ; pas de conflit d'intérêts déclaré (p. 12). |
| **Support** | *JMIR Medical Education* (JMIR Publications), libre accès. |
| **Audience** | 17 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Bonne : formules de chaque barème et du score attendu publiées, tableau complet pour 2 et 5 options ; la démarche se refait et les chiffres se vérifient (vérifié ici pour les méthodes 1 et 6 [calcul]). Pages citées : celles de l'article (1 à 12). |

## Ce que fait l'étude

- **Champ** (p. 2) : QCM à réponse unique (« meilleure réponse », 5 options en général ; questions à 2 options ; vrai/faux simple). Exclus : degré de confiance, élimination, réponse jusqu'à la bonne (p. 3).
- **Recherche** (p. 3-4) : ERIC, PsycInfo, Embase, MEDLINE, septembre 2020, double sélection ; 3 892 références, 129 sources retenues plus 129 par recherche manuelle.
- **Calculs** (p. 3-4) : score moyen au hasard (k = 0) et score attendu selon la part de connaissances, pour des examens fictifs de 100 questions à 2 ou 5 options ; questions de même difficulté, sans indice, toutes répondues.

## Résultats

- **21 barèmes** (p. 4-8, tableau 2), de −3 à +1 point par question.
- **Score au hasard** (p. 8-9, tableau 3) : de −1 à +0,75 point pour 2 options, de −2,2 à +0,84 pour 5 options. Barème 1/0 : 0,50 (2 options) et 0,20 (5 options). Pénalité −1/(n−1) (méthode 6) : 0 dans les deux cas.
- **Relation linéaire** (p. 9) : pour tous les barèmes, la note est une droite de la part de connaissances ; seule la méthode 6 donne la même droite quel que soit le nombre d'options.
- **Seuil pour 50 % de connaissances** (p. 1, 10, fig. 3) : de 0 % à 87,5 % (2 options) et de −60 % à 92 % (5 options) selon le barème ; barème 1/0 : 75,0 % (2 options) et 60,0 % (5 options) ; méthode 6 : 50 %.
- **Points négatifs** (p. 11) : la formule « bonnes moins mauvaises » suppose qu'on sait ou qu'on devine, alors que les étudiants ont des connaissances partielles ; la décision de répondre dépend aussi du goût du risque ; la pénalité ne change pas le classement si tous répondent à tout ; elle est contestée en droit allemand.
- **Recommandation** (p. 11-12) : barème 1/0, simple et accepté, avec un seuil qui tient compte du nombre d'options ; questions à nombres d'options différents notées séparément ou corrigées (2 options : 50 % de hasard, 5 options : 20 %).

## Avis critique

**Apport.** Complète [Schmidt et al. (2021)](schmidt2021.md) et [(2022)](schmidt2022.md) pour le format le plus courant : il donne la règle simple « seuil = 50 % + 50 %/n » pour le barème 1/0, que QuizForge peut calculer pour chaque quiz.

**Points forts**
- Recherche large (258 sources) et formules explicites.
- Relation linéaire : contrairement au « choisir N », la note se convertit directement en part de connaissances.
- Recommandation conditionnelle (règlement local, seuil fixe).

**Réserves**
1. **Importante** — Modèle « sait ou devine au hasard » avec options également plausibles et sans indice ; les auteurs notent que ces hypothèses sont souvent fausses en examen réel (p. 11) : un leurre peu plausible relève la réussite au hasard.
2. **Mineure** — Calculs donnés pour 2 et 5 options seulement ; les valeurs pour 3 et 4 options se déduisent de la formule [calcul].
3. **Mineure** — Revue de la portée : pas d'évaluation de la qualité des sources ni de données d'examen réel.

**Calculs pour QuizForge** [calcul] (barème 1/0, formule de l'article) : 3 options : hasard 33,3 %, seuil 66,7 % ; 4 options : hasard 25 %, seuil 62,5 %. C'est le seuil de 25 sur 40 déjà retenu dans [lesage2013](lesage2013.md) pour 4 options.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Score au hasard et seuil de chaque barème | B | Calcul exact sous un modèle simple |
| Préférer le barème 1/0 sans point négatif | C | Raisonnement et contraintes juridiques, pas de données |

**Transférabilité** : forte ; les mêmes barèmes se règlent dans Moodle (fraction de chaque option).

**Pour conclure, il faudrait** comparer, sur un quiz réel analysé par DiagForge, le seuil calculé et la note des étudiants jugés compétents par l'enseignant.

## Pour Forge

- **QuizForge** : QCM à réponse unique noté 1/0 (niveau C).
- **QuizForge** : afficher score au hasard et seuil 50 % + 50 %/n dans le rapport (niveau B).
- **QuizForge** : si une pénalité est exigée, −1/(n−1) (fraction Moodle −100/(n−1) %) (niveau B).
- **QuizForge** : signaler les quiz qui mélangent vrai/faux simples et QCM à 4-5 options (niveau C).
- **Trois options** : la règle des trois options ([sridharan2025](../C_analyse_items/sridharan2025.md), [haladyna2022](haladyna2022.md)) porte sur ce format à réponse unique ; elle relève le score au hasard à 33 % et le seuil à 66,7 %.
