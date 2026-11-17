---
cle: valle2021b
reference: "Valle, N., Antonenko, P., Valle, D., Sommer, M., Huggins-Manley, A. C., Dawson, K., Kim, D. et Baiser, B. (2021). Predict or describe? How learning analytics dashboard design influences motivation and statistics anxiety in an online statistics course. Educational Technology Research and Development, 69, 1405-1431."
doi: 10.1007/s11423-021-09998-z
axe: [G2]
type_etude: essai randomisé à trois bras sur deux semestres (tableau prédictif centré sur soi, tableau descriptif avec moyenne de classe, témoin avec le tableau standard de Canvas), questionnaires avant et après, 10 entretiens (N = 179)
public: étudiants de master et doctorat, cours d'introduction aux statistiques entièrement en ligne, une université publique du sud-est des États-Unis
lecture: "texte complet, 09/11/2026"
regles:
  - outil: DiagForge
    regle: "pas de prédiction de note (probabilité d'obtenir telle mention) dans le rapport par défaut : elle n'a pas changé les notes et a fait baisser la motivation intrinsèque des étudiants peu motivés au départ"
    niveau: C
    transferabilite: moyenne
  - outil: DiagForge
    regle: "expliquer en une ou deux phrases comment lire chaque graphique du rapport à sa première apparition"
    niveau: D
    transferabilite: forte
    note: "la plupart des étudiants interrogés ne comprenaient pas les tableaux de bord au premier abord, malgré une vidéo d'explication"
---

# Prédire ou décrire : tableau de bord en statistiques en ligne (Valle et al., 2021b)

Valle, N., Antonenko, P., Valle, D., Sommer, M., Huggins-Manley, A. C., Dawson, K., Kim, D. et Baiser, B. (2021). Predict or describe? How learning analytics dashboard design influences motivation and statistics anxiety in an online statistics course. *Educational Technology Research and Development*, 69, 1405-1431. [DOI](https://doi.org/10.1007/s11423-021-09998-z)

**En une phrase.** Dans un cours de statistiques en ligne, 179 étudiants de master et doctorat reçoivent au hasard un tableau qui prédit leur mention finale à partir des quiz, un tableau qui compare leurs scores à la moyenne de la classe, ou le tableau standard de Canvas ; aucun ne change les notes, le tableau prédictif réduit un peu l'anxiété d'interprétation mais fait baisser la motivation intrinsèque des étudiants peu motivés au départ, et les témoignages montrent que se voir sous la moyenne décourage certains.

## La source

| | |
| --- | --- |
| **Équipe** | Université de Floride (éducation, technologies éducatives, mesure, écologie et statistique) et université Sungkyunkwan (Séoul) ; deux auteurs enseignent le cours étudié (p. 1410). Même première autrice que [valle2021](valle2021.md). |
| **Nature** | Académique ; financement non rapporté ; aucun conflit déclaré (p. 1428). Les auteurs ont conçu les tableaux de bord et enseignent le cours. |
| **Support** | *Educational Technology Research and Development* (Springer). |
| **Audience** | 55 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Moyenne : modèles décrits (régression de Tobit bayésienne, a priori publiés, p. 1415-1417), instruments publics (MSLQ, STARS) ; données et code non publiés. La démarche se refait ; les chiffres ne se vérifient pas. |

## Ce que fait l'étude

- **Participants** (p. 1410) : 179 étudiants sur 261 invités (69 %) : 69 témoins, 56 descriptif, 54 prédictif ; 63 % en master ; prétest de 12 questions comparable (64,7 %, 65,8 %, 65,7 %).
- **Tableau prédictif** (p. 1411-1412, figure 2) : probabilité d'obtenir A, B, C ou D/E en fin de cours, mise à jour chaque semaine par un classifieur bayésien naïf entraîné sur les promotions précédentes, avec un avertissement sur la précision ; pas de comparaison aux autres.
- **Tableau descriptif** (p. 1412, figure 3) : score de l'étudiant par module contre la moyenne de la classe.
- **Témoin** (p. 1412, figure 4) : tableau standard de Canvas, qui montre déjà moyennes et boîte à moustaches par devoir. Rappels hebdomadaires pour tous.
- **Mesures** (p. 1413-1414) : motivation (MSLQ, 6 échelles) et anxiété statistique (STARS, 6 échelles) en début et fin de semestre ; notes aux quiz et à l'examen final ; 10 entretiens et questions ouvertes.
- **Analyse** (p. 1414-1417) : seuls les étudiants ayant rempli les deux questionnaires et ouvert au moins une fois leur tableau sont retenus ; modèles de Tobit bayésiens ; l'indicateur « p » est la plus petite des deux probabilités a posteriori que le coefficient soit positif ou négatif.

## Résultats

- **Notes** (tableaux 3 et 4, p. 1421) : pas d'effet ; examen final 78,5 (témoin), 83,8 (descriptif), 80,9 (prédictif) ; quiz 91,9, 93,0, 92,2.
- **Motivation intrinsèque** (tableau 1, p. 1418 ; p. 1417) : interaction tableau prédictif × motivation initiale (β = 0,24, p = 0,026) ; pour une motivation initiale de 2 sur 7, −0,86 en fin de semestre par rapport aux témoins ; pour 6 sur 7, +0,10. Aucun effet du tableau descriptif. Aucun effet sur les cinq autres échelles de motivation.
- **Anxiété d'interprétation** (tableau 2, p. 1420 ; p. 1418-1419) : tableau prédictif β = −0,52 (p = 0,041 au tableau, 0,027 dans le texte) ; baisse de 0,12 pour une anxiété initiale de 2, mais hausse de 0,28 pour une anxiété initiale de 4 (interaction p = 0,053).
- **Rejet de l'utilité des statistiques** (tableau 2) : baisse avec les deux tableaux chez les étudiants qui partaient avec une forte aversion (interactions p = 0,040 et 0,046) ; environ −0,75 pour une valeur initiale de 4.
- **Entretiens et questions ouvertes** (p. 1422-1424) : se voir sous la moyenne « a fait des dégâts sur mon moral » et confirme « que je n'ai pas la capacité de faire des maths » ; une étudiante cesse de regarder le graphique dans les modules difficiles ; la plupart des étudiants interrogés ne comprenaient pas leur tableau au premier abord.

## Avis critique

**Apport.** Un des rares essais randomisés sur un semestre, dans un cours de mathématiques appliquées en ligne proche du nôtre, qui compare prédiction centrée sur soi et comparaison à la moyenne. Il ne montre aucun gain de note, et un effet indésirable de la prédiction chez les étudiants les moins motivés.

**Points forts**
- Tirage au sort, cours réel en ligne, durée d'un semestre, deux cohortes.
- Mesure de réussite objective (quiz, examen) en plus des questionnaires.
- Modèle adapté aux effets plafond (beaucoup de notes au maximum), analyse de sensibilité aux a priori.

**Réserves**
1. **Majeure** — Le groupe témoin n'est pas « sans tableau de bord », comme le dit le résumé (p. 1405) : il voit le tableau Canvas avec moyennes et boîte à moustaches (p. 1412). La comparaison « descriptif contre témoin » oppose donc deux affichages comparatifs, ce qui peut expliquer l'absence d'effet du tableau descriptif.
2. **Importante** — Les étudiants des groupes tableau de bord qui ne l'ont jamais ouvert sont exclus, pas leurs homologues témoins (p. 1414) ; les effectifs analysés ne sont pas donnés.
3. **Importante** — 12 échelles et 2 notes testées ; les effets retenus ont des « p » entre 0,026 et 0,046 ; cet indicateur bayésien est l'équivalent d'un test unilatéral (le double correspond à un test bilatéral, soit 0,05 à 0,09 [calcul]). Valeurs de p différentes entre texte et tableau.
4. **Mineure** — Le tableau prédictif change deux choses à la fois (prédiction et absence de comparaison) ; les bornes des échelles sont inversées dans la description du modèle (p. 1415 contre p. 1413-1414).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Ni le tableau prédictif ni le descriptif n'améliorent les notes | C | Un essai d'un semestre, témoin qui a déjà un tableau comparatif |
| La prédiction de mention fait baisser la motivation intrinsèque des étudiants peu motivés | C | Interaction dans un essai, comparaisons multiples, seuil limite |
| Le tableau prédictif réduit l'anxiété d'interprétation | D | Effet dépendant du niveau initial (hausse chez les plus anxieux), seuil limite |
| Se voir sous la moyenne décourage certains étudiants | D | Témoignages |

**Transférabilité** : moyenne à forte. Statistiques en ligne, quiz hebdomadaires, étudiants de master : très proche de nos M1-M2 en autonomie ; la mesure de motivation reste déclarative.

**Pour conclure, il faudrait** tirer au sort, dans DiagForge, rapport « maîtrise par notion » contre « maîtrise par notion + probabilité de réussite à l'examen », et suivre la participation aux quiz suivants et la note chez les étudiants dont la motivation initiale est faible.

## Pour Forge

- **DiagForge** : pas de prédiction de note par défaut (niveau C). Cela **renforce** la règle existante « pas de prédiction de note sans explication de son calcul » ([herodotou2025](herodotou2025.md), niveau D) : même expliquée et assortie d'un avertissement, la prédiction a eu un effet indésirable.
- **DiagForge** : une courte aide de lecture à la première apparition de chaque graphique (niveau D).
- **Confirme** [kaliisa2024](kaliisa2024.md) (pas d'effet démontré sur les notes) et, par les témoignages, les risques de la moyenne de classe ([harvey2020](harvey2020.md), [zheng2026](zheng2026.md)). L'apport noté jusqu'ici (« tableau prédictif moins anxiogène, sauf pour les buts d'évitement ») est corrigé dans le README de l'axe.
