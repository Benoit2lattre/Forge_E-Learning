---
cle: slepkov2019
reference: "Slepkov, A. D. et Godfrey, A. T. K. (2019). Partial credit in answer-until-correct multiple-choice tests deployed in a classroom setting. Applied Measurement in Education, 32(2), 138-150."
doi: 10.1080/08957347.2019.1577249
axe: [A3]
type_etude: étude psychométrique de 26 examens réels à essais jusqu'à la bonne réponse (cartes à gratter IFAT), rescorés sans crédit partiel et avec crédit partiel simulé au hasard
public: examens d'introduction en physique et en chimie, université Trent (Ontario) ; 2950 copies, 484 questions à 5 options
lecture: texte complet, 09/11/2026
regles:
  - outil: QuizForge
    regle: "QCM noté en mode « interactif avec plusieurs essais » : accorder un crédit partiel nettement dégressif (de l'ordre de 1 ; 0,5 ; 0,1 puis 0) plutôt que tout ou rien ; il rend la note plus discriminante et plus fiable"
    niveau: B
    transferabilite: forte
    note: "dans Moodle, la pénalité par essai est linéaire (1 ; 1 − p ; 1 − 2p...) et le nombre d'essais vaut le nombre d'indices + 1 ; une pénalité p = 0,5 donne 1 ; 0,5 ; 0"
  - outil: QuizForge
    regle: "afficher le score attendu au hasard d'une question à essais multiples selon la pénalité et le nombre d'options (5 options : 0,20 en tout ou rien, 0,32 avec 1 ; 0,5 ; 0,1, 0,40 avec la pénalité 1/3 par défaut)"
    niveau: C
    transferabilite: forte
    note: "[calcul] sous l'hypothèse de choix au hasard parmi les options restantes"
  - outil: DiagForge
    regle: "pour un test à essais multiples, calculer difficulté, discrimination item exclu et alpha sur la note avec crédit partiel et sur le premier essai seul, et le rapport crédit partiel obtenu / crédit attendu au hasard (signaler une question sous 1)"
    niveau: B
    transferabilite: forte
  - outil: ExoForge
    regle: "garder un barème dégressif par tentative (points_par_tentative) avec un crédit réel au deuxième essai ; pour une étape à choix, vérifier que le score au hasard reste bas"
    niveau: C
    transferabilite: moyenne
---

# Crédit partiel dans les QCM à essais jusqu'à la bonne réponse (Slepkov et Godfrey, 2019)

Slepkov, A. D. et Godfrey, A. T. K. (2019). Partial credit in answer-until-correct multiple-choice tests deployed in a classroom setting. *Applied Measurement in Education*, 32(2), 138-150. [DOI](https://doi.org/10.1080/08957347.2019.1577249)

**En une phrase.** Sur 26 examens de physique et de chimie où l'étudiant répond jusqu'à trouver la bonne réponse, le crédit partiel pour le 2e ou le 3e essai augmente la note de 10 points en moyenne, mais aussi la discrimination des questions (0,30 à 0,33) et la fiabilité (alpha 0,70 à 0,73), alors qu'un crédit donné au hasard les ferait baisser : le crédit partiel mesure une connaissance partielle réelle. Pour QuizForge, cela soutient le mode Moodle « interactif avec plusieurs essais » avec pénalité par essai.

## La source

| | |
| --- | --- |
| **Équipe** | Département de physique et d'astronomie, université Trent (Ontario) ; A. D. Slepkov a construit la plupart des examens et enseigné plusieurs des cours (p. 140-141). Même équipe que [slepkov2021](../C_analyse_items/slepkov2021.md). |
| **Nature** | Académique ; financement non rapporté ; pas de conflit d'intérêts déclaré (p. 149). Les auteurs analysent des examens qu'ils ont conçus. |
| **Support** | *Applied Measurement in Education* (Taylor et Francis), revue de mesure en éducation. |
| **Audience** | 21 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Moyenne : méthode et simulation décrites (p. 141-142), indicateurs de chaque examen publiés (tableaux 1 et 2) ; réponses individuelles et code non publiés. Les effectifs se recomptent à partir du tableau 1 (à une question près). Pages de la revue (138 à 150). |

## Ce que fait l'étude

- **Format** (p. 139) : feuille de réponses à gratter (IFAT) ; l'étudiant gratte une case, une étoile indique la bonne réponse, sinon il recommence ; la note dépend du nombre de cases grattées.
- **Corpus** (p. 140-141, tableau 1) : tous les examens IFAT de mi-semestre et finaux de physique et de chimie d'introduction depuis 2011 passés par au moins 30 étudiants : 26 examens, 8 à 47 questions, 36 à 406 étudiants ; 2950 copies, 484 questions et environ 66 700 réponses [calcul ; l'article annonce 485 questions et environ 67 000 réponses].
- **Barèmes** (p. 141, tableau 2) : [1 ; 0,5 ; 0,1 ; 0 ; 0] pour 16 examens ; aussi [1 ; 0,4 ; 0 ; 0 ; 0], [1 ; 0,25 ; 0,125 ; 0 ; 0], [1 ; 0,5 ; 0,125 ; 0 ; 0].
- **Comparaisons** (p. 141-142) : chaque examen est noté (a) tel quel avec crédit partiel, (b) au premier essai seul, (c) au premier essai plus un crédit partiel tiré au hasard (10 000 simulations). Indicateurs : difficulté moyenne, discrimination item exclu moyenne, alpha de Cronbach (comparaison de Feldt).

## Résultats

- **Note** (p. 142) : 61 % avec crédit partiel contre 51 % au premier essai seul ; gain de 4 à 13 points selon l'examen.
- **Crédit au-dessus du hasard** (p. 142, tableau 2) : avec [1 ; 0,5 ; 0,1], le hasard donnerait 32 % du crédit partiel disponible ; les étudiants en obtiennent 44 % ± 5 % ; rapport crédit obtenu / hasard de 1,2 à 1,9 (moyenne 1,47) sur les 26 examens.
- **Discrimination** (p. 142, tableau 1) : moyenne item exclu 0,33 avec crédit partiel, 0,30 au premier essai seul (plus élevée pour 25 examens sur 26 ; d = 0,40), 0,29 avec crédit au hasard (d = 0,23).
- **Fiabilité** (p. 143-144, tableau 1) : alpha 0,73 avec crédit partiel contre 0,70 au premier essai (d = 0,23) ; supérieur de façon significative pour 17 examens sur 26 ; 0,68 avec crédit au hasard. Pour deux examens (8 et 22), l'alpha avec crédit partiel est un peu plus bas, sans différence significative [décompte].
- **Validité** (p. 144-146, figure 3) : sur l'examen 15 (328 étudiants), la part du crédit partiel obtenu croît avec le score au premier essai (r = 0,52 ; 0,85 sur les moyennes par score) ; même tendance sur l'examen 16 (r = 0,48 et 0,90).
- **Limite reconnue** (p. 147-148) : la note « premier essai » est reconstruite après coup ; les étudiants auraient pu répondre autrement s'ils avaient su qu'il n'y avait pas de crédit partiel. On ne sait pas si le 2e choix est réfléchi ou pris automatiquement dans un classement initial.

## Avis critique

**Apport.** Répond à l'objection « le crédit partiel gonfle les notes » sur des examens réels de physique : la hausse de la note s'accompagne d'une meilleure mesure. C'est l'argument psychométrique pour une pénalité par essai plutôt que le tout ou rien en mode interactif.

**Points forts**
- 26 examens réels, sans sélection autre que l'effectif, en physique et en chimie.
- Contrôle par simulation d'un crédit partiel donné au hasard, qui sépare connaissance partielle et chance.
- Indicateurs publiés pour chaque examen.

**Réserves**
1. **Importante** — Comparaison intra-test reconstruite après coup, pas d'essai où un groupe ne bénéficierait pas du crédit partiel (les auteurs le disent, p. 147).
2. **Importante** — Cartes à gratter en examen surveillé : pas de recherche dans le cours entre deux essais, ce qui n'est pas le cas d'un quiz Moodle fait à la maison.
3. **Mineure** — Gains faibles en valeur absolue (+0,03 sur la discrimination et sur l'alpha) ; les auteurs les jugent forts au regard du maximum possible (p. 147), argument qui reste une estimation.
4. **Mineure** — Petits écarts de décompte (485 questions annoncées pour 484 dans le tableau) ; le hasard pour [1 ; 0,5 ; 0,1] donne 30 % du crédit disponible avec un choix uniforme parmi les options restantes [calcul : (1/4 x 0,5 + 1/4 x 0,1) / 0,5], l'article indique 32 %.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Le crédit partiel en essais multiples rend le test plus discriminant et plus fiable | B | 26 examens réels concordants, contrôle par simulation |
| Le crédit partiel reflète une connaissance partielle, pas la chance | B | Rapport au hasard > 1 partout ; corrélation sur deux grands examens |
| Le choix exact du barème dégressif importe peu | C | Affirmé en renvoyant à une étude antérieure des auteurs (p. 141) |

**Transférabilité** : forte. Examens de physique d'université à questions fermées ; le mécanisme (essais successifs et crédit dégressif) existe tel quel dans Moodle.

**Pour conclure, il faudrait** analyser avec DiagForge les quiz Moodle en mode interactif : comparer discrimination et alpha avec la note réelle et avec la note du premier essai, question par question.

## Pour Forge

**Score au hasard d'une question à 5 options** [calcul, choix uniforme parmi les options restantes] :

| Barème par essai | Score au hasard |
| --- | --- |
| Tout ou rien [1 ; 0 ; ...] | 0,20 |
| Slepkov [1 ; 0,5 ; 0,1 ; 0 ; 0] | 0,32 |
| Moodle, pénalité 0,5 [1 ; 0,5 ; 0 ; ...] | 0,30 |
| Moodle, pénalité 1/3 (défaut de QuizForge) [1 ; 0,67 ; 0,33 ; 0 ; 0] | 0,40 |

- **QuizForge** : en mode « interactif avec plusieurs essais », crédit dégressif plutôt que tout ou rien (niveau B) ; une pénalité de 0,5 est plus proche des barèmes étudiés que la pénalité 1/3 par défaut (niveau C). Le nombre d'essais dépend du nombre d'indices (colonnes `Indice 1`, `Indice 2`...).
- **QuizForge** : afficher le score au hasard selon la pénalité et le nombre d'options (niveau C).
- **DiagForge** : indicateurs sur la note avec crédit partiel et sur le premier essai ; rapport au hasard par question (niveau B). La difficulté du premier essai est aussi celle à comparer aux seuils de [slepkov2021](../C_analyse_items/slepkov2021.md).
- **ExoForge** : barème `points_par_tentative` dégressif avec un vrai crédit au 2e essai (niveau C) ; le défaut [1 ; 0,75 ; 0,5] est plus généreux que les barèmes étudiés, ce qui compte surtout pour les étapes à choix.
- Mertens et Lindner (2025, [fiche](mertens2025.md)) citent cette étude pour la valeur diagnostique des essais multiples ; [rhodes2015](rhodes2015.md) montre le revers quand les essais portent sur le devoir entier avec la meilleure note retenue.
