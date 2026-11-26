---
cle: steele2014
reference: "Steele, K. M., Brunhaver, S. R. et Sheppard, S. D. (2014). Feedback from in-class worksheets and discussion improves performance on the statics concept inventory. International Journal of Engineering Education, 30(4), 992-999."
doi: non attribué (voir forge.bib)
axe: [H2]
type_etude: quasi-expérimental en classe, plan contrebalancé (4 thèmes avec fiches dans une session, les 4 autres dans la session suivante), prétest et post-test à l'inventaire de statique ; comparaison historique
public: deux sessions d'un cours de statique de 10 semaines (75 inscrits chacune, surtout 2e et 3e année d'ingénierie), université privée sélective, États-Unis, 2011-2012
lecture: texte complet, 10/11/2026
regles:
  - outil: QuizForge
    regle: "après chaque thème de statique, un quiz conceptuel court (2 à 3 QCM, environ 5 minutes) dont chaque leurre code une conception erronée nommée"
    niveau: C
    transferabilite: moyenne
    note: "fiches papier en classe suivies d'une discussion ; l'effet en ligne et sans discussion n'est pas testé"
  - outil: DiagForge
    regle: "restituer à la classe, pour chaque question du quiz, la répartition des réponses et le leurre dominant avec la conception erronée qu'il code, pour préparer le retour collectif"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "ne pas interpréter individuellement le score d'un quiz de 2 à 3 questions : alpha de 0,16 à 0,73 selon le thème ; agréger par concept sur plusieurs quiz"
    niveau: C
    transferabilite: forte
---

# Fiches conceptuelles en classe et inventaire de statique (Steele et al., 2014)

Steele, K. M., Brunhaver, S. R. et Sheppard, S. D. (2014). Feedback from in-class worksheets and discussion improves performance on the statics concept inventory. *International Journal of Engineering Education*, 30(4), 992-999. Pas de DOI dans `forge.bib`.

**En une phrase.** Huit fiches de 2 à 3 QCM conceptuels (5 minutes, puis 10 minutes de discussion des erreurs au cours suivant), réparties entre deux sessions d'un cours de statique, s'accompagnent d'un gain plus fort à l'inventaire de statique sur les thèmes travaillés (52 contre 42 points, puis 46 contre 38) ; l'effet est plausible mais mesuré avec un test proche des fiches, par un seul enseignant.

## La source

| | |
| --- | --- |
| **Équipe** | Génie mécanique, Stanford (Brunhaver, Sheppard) et université de Washington (Steele) (p. 992). |
| **Nature** | Académique ; bourses doctorales (NSF Graduate Research Fellowship, Stanford) (p. 998). Les fiches ont été conçues sans l'enseignant du cours, pour éviter d'« enseigner pour le test » (p. 994). |
| **Support** | *International Journal of Engineering Education* (revue à comité de lecture). |
| **Audience** | Non disponible : pas de DOI dans forge.bib (voir forge.bib). |
| **Reproductibilité** | Moyenne : fiches publiées en ligne par les auteurs, inventaire gratuit (p. 998) ; données non publiques ; calcul des tailles d'effet non décrit. |

## Ce que fait l'étude

- **Public** (tableau 1, p. 993) : session A (automne 2011) et B (hiver 2012), 75 étudiants chacune, même enseignant (plus de 20 ans d'expérience, pédagogie active et instruction par les pairs, p. 995).
- **Mesure** (p. 994) : inventaire de statique en ligne en début et fin de cours (devoir noté sur la participation, pas sur le score) ; 8 thèmes retenus (frottement non traité) ; passations complètes 65 (87 %) en A et 50 (67 %) en B.
- **Intervention** (p. 994, tableau 2 p. 995) : 8 fiches papier de 2 à 3 QCM, chaque leurre codant une conception erronée (exemple de la fig. 1 : déplacer un couple change son moment ; un couple remplacé par une force seule ; erreur de calcul du couple équivalent) ; 5 minutes en fin de cours, résultats et discussion des erreurs 10 minutes au cours suivant (au moins 48 heures plus tard). A : équivalence statique, équilibre, rouleau, diagramme du corps isolé ; B : axe dans une rainure, surface sans frottement, 3e loi, représentation des efforts inconnus ; groupes de thèmes équilibrés en difficulté sur deux sessions antérieures.
- **Analyse** (p. 995) : gain par étudiant sur les thèmes avec et sans fiche (test de Mann-Whitney) ; comparaison des scores finaux avec deux sessions antérieures du même enseignant (test de Wilcoxon) ; corrélations de Spearman.

## Résultats

- **Prétest** (p. 995) : 23 % (écart-type 13) en A, 27 % (13) en B, à peine au-dessus du hasard (20 %) ; sous le hasard sur le thème « surface sans frottement » (p = 0,001).
- **Score final** (p. 996) : 70 % (18) en A et 69 % (19) en B contre 61 % (19) dans les sessions antérieures (p < 0,001).
- **Gain par thème** (p. 996) : A, 52 points avec fiche contre 42 sans (p = 0,002) ; B, 46 contre 38 (p = 0,019). Les auteurs donnent d = 3,9 et 2,8.
- **Fiches et post-test** (p. 996-997) : sur 5 des 8 thèmes, le post-test dépasse le score de la fiche ; en équilibre, le post-test est plus bas que la fiche ; en 3e loi et efforts inconnus, pas de progrès après la discussion.
- **Égalisation** (p. 997) : corrélation prétest-post-test 0,48 sur les thèmes sans fiche, 0,18 (non significative) sur les thèmes avec fiche.
- **Fiabilité des fiches** (tableau 3, p. 995) : alpha de 0,16 (équivalence statique) à 0,73 (rouleau, diagramme du corps isolé).

## Avis critique

**Apport.** Une des rares mesures d'effet d'un retour sur les erreurs types en statique, avec un plan contrebalancé par thème qui contrôle l'enseignant et la cohorte ; le dispositif (quelques QCM par thème, répartition des réponses, discussion du leurre dominant) se transpose dans un quiz Moodle suivi d'un retour collectif.

**Points forts**
- Contrebalancement : chaque groupe de thèmes sert de témoin à l'autre, et le résultat se répète dans les deux sessions.
- Fiches écrites sans l'enseignant ; matériel publié.
- Effet par thème examiné, y compris les thèmes où il n'apparaît pas.

**Réserves**
1. **Majeure** — Mesure alignée sur l'intervention : fiches « inspirées » de l'inventaire, de même format ; les auteurs reconnaissent que le gain peut refléter la familiarité avec les questions plus que la compréhension (p. 995). Aucun transfert à des problèmes ouverts.
2. **Importante** — Tests inadaptés : thèmes avec et sans fiche comparés chez les mêmes étudiants par un test pour échantillons indépendants (Mann-Whitney), et sessions différentes comparées par un test apparié (Wilcoxon) (p. 995). Les d de 3,9 et 2,8 supposent un écart-type du gain d'environ 2,6 points pour un écart de 10 points [calcul : 10 / 3,9], peu compatible avec les écarts-types de 13 à 19 points des scores (p. 995-996) ; le calcul n'est pas décrit.
3. **Importante** — Attrition : 33 % des étudiants de B sans prétest et post-test [calcul : 100 - 67 %] (p. 994) ; la comparaison historique (70 contre 61 %) ne tient compte ni de cette sélection ni d'autres changements de cours.
4. **Mineure** — Un seul enseignant, pédagogie déjà active, établissement sélectif, scores finaux supérieurs à la littérature (p. 995) ; fiches papier en classe, retour différé de 48 heures.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Des QCM conceptuels courts avec discussion des erreurs augmentent le score à l'inventaire sur les thèmes travaillés | C | Plan contrebalancé répliqué sur deux sessions, mais mesure alignée, tests inadaptés, un enseignant |
| Ils améliorent la compréhension conceptuelle transférable | D | Non mesuré |
| Ils réduisent l'écart entre étudiants faibles et forts | D | Différence de deux corrélations, non testée |

**Transférabilité** : moyenne. Statique d'introduction, proche de nos L3 ; mais fiches papier et discussion en classe, pas de travail en ligne en autonomie.

**Pour conclure, il faudrait** reprendre le contrebalancement dans QuizForge : deux groupes reçoivent des quiz conceptuels sur des moitiés différentes des thèmes, avec retour par leurre ; mesurer à l'examen sur des problèmes ouverts, pas sur les mêmes QCM.

## Pour Forge

- **QuizForge** : quiz conceptuel court par thème, leurres codant une conception nommée (niveau C).
- **DiagForge** : répartition des réponses par question et leurre dominant pour préparer le retour collectif (niveau C).
- **DiagForge** : pas de diagnostic individuel sur 2 à 3 questions ; agréger par concept (niveau C).
- Le retour différé (48 heures) n'est pas comparé à un retour immédiat : question ouverte, que les auteurs soulèvent eux-mêmes (p. 998).
- Renvois : [steif2006b](steif2006b.md) (restitution par concept), [steif2006](steif2006.md) et [steif2005](steif2005.md) (leurres de l'inventaire).
