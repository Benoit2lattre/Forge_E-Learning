---
cle: fleur2023
reference: "Fleur, D. S., van den Bos, W. et Bredeweg, B. (2023). Social comparison in learning analytics dashboard supporting motivation and academic achievement. Computers and Education Open, 4, article 100130."
doi: 10.1016/j.caeo.2023.100130
axe: [G1]
type_etude: deux essais randomisés individuels (79 et 83 étudiants), tableau de bord comparatif contre absence de tableau de bord
public: étudiants de licence en informatique, 1re et 2e année, université d'Amsterdam (cours de 8 semaines, le second entièrement en ligne)
lecture: texte complet, 08/11/2026
regles:
  - outil: DiagForge
    regle: "si le rapport situe l'étudiant par rapport à des pairs, utiliser un petit groupe de pairs proches de son niveau (une dizaine), légèrement au-dessus, plutôt que la moyenne de toute la classe"
    niveau: C
    transferabilite: moyenne
    note: "les auteurs choisissent les pairs à l'insu des étudiants ; DiagForge doit dire comment le groupe est formé"
  - outil: DiagForge
    regle: "ne pas attendre d'un simple affichage comparatif un progrès d'autorégulation : le rapport doit aussi dire quoi faire"
    niveau: C
    transferabilite: forte
---

# Se comparer à des pairs légèrement meilleurs (Fleur et al., 2023)

Fleur, D. S., van den Bos, W. et Bredeweg, B. (2023). Social comparison in learning analytics dashboard supporting motivation and academic achievement. *Computers and Education Open*, 4, article 100130. [DOI](https://doi.org/10.1016/j.caeo.2023.100130)

**En une phrase.** Dans deux cours de licence, un tableau de bord qui montre à l'étudiant sa moyenne à côté de celles de 9 pairs de même objectif, choisis pour être légèrement meilleurs, s'accompagne d'une note finale supérieure d'environ 0,4 point sur 10 et d'une motivation extrinsèque mieux maintenue, sans effet mesuré sur la métacognition ; le résultat est fragile (petits effectifs, tests unilatéraux, non-utilisateurs exclus).

## La source

| | |
| --- | --- |
| **Équipe** | Institut d'informatique et département de psychologie de l'université d'Amsterdam ; Max Planck (Berlin) pour le deuxième auteur. Thèse du premier auteur, qui a programmé le tableau de bord (p. 10). |
| **Nature** | Académique ; bourse doctorale de l'université d'Amsterdam ; financements européens et néerlandais du deuxième auteur ; aucun conflit déclaré (p. 10). Les auteurs évaluent leur propre outil. |
| **Support** | *Computers and Education Open* (Elsevier), libre accès. Version longue d'un article de congrès de 2020 (p. 4). |
| **Audience** | 57 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Bonne : code du tableau de bord publié (GitHub, p. 4), scripts d'analyse et préenregistrement de l'expérience 2 sur OSF (p. 6-7). Les chiffres se vérifient, la démarche se refait dans un autre cours. |

## Ce que fait l'étude

- **Tableau de bord** (p. 4, fig. 2) : à gauche, la moyenne de l'étudiant et celles de 9 pairs anonymes présentés comme « étudiants ayant un objectif de note semblable » ; le groupe est choisi pour avoir une moyenne de 0,5 à 1,5 point au-dessus de celle de l'étudiant, avec 20 à 40 % de pairs en dessous. Les étudiants ne savent pas que le groupe est choisi ainsi. À droite (expérience 1 seulement), une prédiction de la note finale.
- **Expérience 1** (p. 4-5) : 79 étudiants de première année, premier cours à l'université, en présentiel ; tirage au sort individuel ; 72 dans l'analyse des notes (34 avec tableau de bord), 26 seulement dans l'analyse des questionnaires.
- **Expérience 2** (p. 7) : 83 étudiants de deuxième année, cours en ligne (COVID), comparaison sociale seule ; 62 dans l'analyse des notes (22 avec tableau de bord) après exclusion de 14 étudiants du groupe tableau de bord qui ne l'ont jamais ouvert.
- **Mesures** : note finale des travaux individuels ; motivation intrinsèque et extrinsèque (MSLQ) et métacognition (MAI, et MSLQ en expérience 2) en début et fin de cours.

## Résultats

| | Expérience 1 (p. 6) | Expérience 2 (p. 7) |
| --- | --- | --- |
| Écart de note finale (sur 10) | +0,45 (t = 2,15 ; p = 0,03) ; d = 0,51 | +0,42 (t = 1,78 ; p = 0,04 unilatéral, environ 0,08 en bilatéral [calcul]) ; d = 0,49 |
| Notes insuffisantes | 3 % contre 18 % | 0 contre 2 étudiants |
| Motivation extrinsèque | baisse chez les témoins, stable avec tableau de bord | stable chez les témoins, hausse avec tableau de bord (p = 0,03 unilatéral) |
| Motivation intrinsèque, métacognition | pas de différence | pas de différence |

- **Médiation** (p. 6-7) : la hausse de motivation extrinsèque n'explique pas l'écart de notes.
- **Notes par devoir** (p. 7) : pas de différence significative entre groupes sur l'ensemble des devoirs de l'expérience 2.
- **Interprétation des auteurs** (p. 8-9) : l'écart viendrait surtout de moins d'échecs chez les étudiants peu motivés au départ ; ce n'est pas testé.

## Avis critique

**Apport.** Un des rares essais randomisés en classe réelle sur la forme de la comparaison sociale : il fonde le choix d'une comparaison proche et légèrement ascendante, plutôt qu'à la moyenne de classe, sur une théorie explicite (Gerber et al., 2018) et le teste deux fois.

**Points forts**
- Tirage au sort individuel, deux cours différents, effet de même taille dans les deux.
- Hypothèses de l'expérience 2 préenregistrées ; code et scripts publiés.
- Mesure de réussite réelle (note du cours) et non seulement des questionnaires.

**Réserves**
1. **Majeure** — Expérience 2 : les 14 étudiants du groupe tableau de bord qui ne l'ont jamais ouvert sont exclus (p. 7), mais pas leurs homologues témoins ; la comparaison n'est plus celle du tirage au sort et favorise le tableau de bord. Les auteurs indiquent que leur note ne différait pas (supplément), ce qui limite sans annuler le biais.
2. **Importante** — Effectifs faibles (22 à 34 étudiants par groupe) ; l'expérience 2 n'est significative qu'en test unilatéral (p ≈ 0,08 en bilatéral [calcul]) ; analyse des questionnaires de l'expérience 1 sur 26 étudiants.
3. **Importante** — Le groupe de comparaison est construit à l'insu des étudiants ; les auteurs notent que l'effet pourrait disparaître si la règle était connue et que l'outil ne convient pas à un usage répété (p. 9). On ne sait pas quelle part revient à la comparaison et quelle part au simple fait d'avoir un retour régulier (le groupe témoin n'a rien).
4. **Mineure** — Expérience 1 : prédiction de note et comparaison confondues ; l'expérience 2 retire la prédiction mais change aussi de cours et de mode (en ligne).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Un tableau de bord à comparaison proche et ascendante améliore la note finale | C | Deux essais concordants mais petits, test unilatéral, exclusion des non-utilisateurs, témoin sans aucun retour |
| La comparaison proche vaut mieux que la moyenne de classe | D | Non testé dans l'étude (pas de bras « moyenne de classe ») ; argument théorique |
| Le tableau de bord ne change pas la métacognition | C | Absence d'effet sur de petits effectifs |

**Transférabilité** : moyenne. Étudiants de licence en informatique, proche de nos L3 ; mais la comparaison porte sur des notes de cours et non sur un quiz de diagnostic, et la sélection cachée des pairs n'est pas reproductible honnêtement.

**Pour conclure, il faudrait** comparer dans DiagForge, sur deux groupes tirés au sort, une restitution « position par rapport à la classe » et une restitution « critère + pairs proches dont la règle de choix est annoncée », avec la note au quiz suivant comme mesure.

## Pour Forge

- **DiagForge** : si une comparaison aux pairs figure dans le rapport, la faire avec un petit groupe de niveau proche, légèrement au-dessus, et annoncer la règle de choix (niveau C ; la supériorité sur la moyenne de classe reste niveau D).
- **DiagForge** : la comparaison seule ne déclenche pas d'autorégulation mesurable ; associer toute position à une action proposée (niveau C). Voir [herodotou2025](herodotou2025.md) pour les recommandations d'action et [weidlich2024](weidlich2024.md) pour le cadre de référence critérié.
