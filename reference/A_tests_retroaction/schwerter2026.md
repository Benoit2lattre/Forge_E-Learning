---
cle: schwerter2026
reference: "Schwerter, J., Lauermann, F., Dimpfl, T. et Bernacki, M. L. (2026). Retrieval practice in higher education: Causality and content transfer effects in a gateway math course. Journal of Educational Psychology, publication en ligne avant parution."
doi: 10.1037/edu0001042
axe: [A1]
type_etude: essai randomisé intra-individuel répété sur trois promotions, estimation par variable instrumentale
public: 1 791 étudiants de 1re année en gestion (Allemagne), cours de mathématiques obligatoire
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "proposer chaque semaine des exercices en ligne paramétrés sur les problèmes types du cours, à faire sans aide et corrigés après envoi"
    niveau: B
    transferabilite: forte
  - outil: QuizForge
    regle: "attendre un effet surtout sur les problèmes de même structure, moindre sur les problèmes nouveaux ; varier les problèmes s'il faut viser le transfert"
    niveau: B
    transferabilite: forte
  - outil: ExoForge
    regle: "prévoir une incitation à la participation et suivre la participation réelle (temps passé, exercices complets), qui baisse au fil du semestre"
    niveau: C
    transferabilite: forte
---

# Exercices de récupération dans un cours de mathématiques (Schwerter et al., 2026)

Schwerter, J., Lauermann, F., Dimpfl, T. et Bernacki, M. L. (2026). Retrieval practice in higher education: Causality and content transfer effects in a gateway math course. *Journal of Educational Psychology*, publication en ligne avant parution. [DOI](https://doi.org/10.1037/edu0001042)

**En une phrase.** Dans un cours de mathématiques de première année suivi par trois promotions, résoudre chaque semaine en ligne de nouvelles versions des problèmes du cours augmente de 4 à 5 points la probabilité de réussir ces problèmes aux contrôles, surtout pour les problèmes de même structure, peu pour les problèmes nouveaux, et de façon irrégulière à l'examen final.

## La source

| | |
| --- | --- |
| **Équipe** | Universités de Tübingen, Dortmund, Bonn, Hohenheim et de Caroline du Nord ; recherche en éducation, statistique et économétrie. |
| **Nature** | Académique ; recherche menée dans un cours ordinaire, avec l'accord du comité d'éthique de l'université. |
| **Support** | *Journal of Educational Psychology* (APA). |
| **Audience** | 1 citation (OpenAlex, 08/11/2026) ; article paru en mai 2026. |
| **Reproductibilité** | Bonne : matériel complémentaire et documents sur l'OSF, méthode d'identification détaillée (p. 8-9). |

## Ce que fait l'étude

- **Public** (p. 5-6) : trois promotions (2022 à 2025) d'un cours de mathématiques pour étudiants en gestion d'une grande université allemande ; 636, 584 et 571 étudiants consentants ; 73 à 80 % passent l'examen final.
- **Intervention** (p. 7) : exercices en ligne hebdomadaires, publiés après les travaux dirigés, versions paramétrées des problèmes du cours ; aucune aide pendant la résolution, correction (bonne réponse) après l'envoi ; 2 points bonus à l'examen si 11 séries sur 13 sont faites.
- **Tirage au sort** (p. 8-9) : deux groupes d'étudiants reçoivent des problèmes différents ; un même problème du contrôle est ainsi « entraîné » pour un groupe et non pour l'autre. Chaque étudiant sert de témoin à lui-même.
- **Mesures** : trois contrôles en ligne et l'examen final ; problèmes de même structure, de transfert proche et de transfert éloigné. Estimations : effet de l'assignation, effet chez ceux qui participent vraiment (au moins 20 minutes et tous les sous-problèmes) par variable instrumentale (p. 8-9).

## Résultats

- **Participation** (p. 8) : 33 à 36 % des problèmes assignés en entraînement, mais la participation réelle baisse à 13-17 % en fin de semestre.
- **Contrôles** (p. 11) : effet de l'assignation de 2,3 à 2,7 points ; effet chez les participants effectifs de 4,3 à 5,0 points de probabilité de réussite, selon la promotion.
- **Transfert** : effet le plus fort pour les problèmes de même structure, moindre en transfert proche, limité en transfert éloigné (résumé, p. 1).
- **Examen final** : environ 8 points dans une promotion, effets plus faibles et non significatifs dans les deux autres (résumé, p. 1).
- **Délai** : pas de modération systématique par le temps entre l'entraînement et le contrôle (résumé, p. 1).

## Avis critique

**Apport.** L'essai le plus proche de nos conditions : université, mathématiques, exercices en ligne paramétrés, sur trois semestres, avec une méthode qui sépare l'effet de l'exercice de la motivation de ceux qui le font.

**Points forts**
- Grands effectifs, trois répétitions annuelles.
- Tirage au sort à l'intérieur de chaque étudiant, qui neutralise les différences de niveau et de motivation.
- Distinction explicite entre problèmes identiques, transfert proche et éloigné.

**Réserves**
1. **Importante** — L'effet par variable instrumentale ne vaut que pour les étudiants qui font l'exercice quand on le leur assigne ; la participation chute en fin de semestre, après le seuil du bonus.
2. **Importante** — Effets modestes (quelques points) et peu nets à l'examen final, qui est la mesure qui compte le plus.
3. **Mineure** — Public de gestionnaires, cours de mathématiques appliquées ; les exercices de mécanique sont plus longs.
4. **Mineure** — Le seuil de 20 minutes pour définir une participation réelle est un choix des auteurs (analyse de sensibilité fournie).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les exercices de récupération hebdomadaires améliorent la réussite aux contrôles en mathématiques à l'université | B | Essai randomisé, trois promotions, effet modeste |
| L'effet s'affaiblit du problème identique au transfert éloigné | B | Même essai, mesure prévue à l'avance |
| Effet sur l'examen final | C | Une promotion sur trois |

**Transférabilité** : forte. Même dispositif qu'ExoForge et QuizForge dans Moodle : exercices paramétrés hebdomadaires avec correction après envoi.

**Pour conclure, il faudrait** reproduire ce plan (deux groupes, problèmes assignés en alternance) dans un cours de mécanique avec ExoForge, ce qui est faisable sans priver aucun étudiant d'exercices.

## Pour Forge

- **ExoForge** : séries hebdomadaires de problèmes paramétrés, sans aide pendant la résolution, avec correction après envoi (niveau B).
- **QuizForge** : ne pas attendre de transfert large d'exercices identiques ; varier les problèmes quand l'objectif est le transfert (niveau B).
- **ExoForge** : suivre la participation réelle (temps, exercices complets) et prévoir une incitation, la participation baissant au fil du semestre (niveau C). DiagForge peut afficher cette courbe de participation.
- Le plan d'étude lui-même (alternance des problèmes assignés entre deux groupes) est un modèle pour évaluer les outils Forge.
