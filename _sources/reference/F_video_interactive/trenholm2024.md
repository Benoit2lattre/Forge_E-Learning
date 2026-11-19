---
cle: trenholm2024
reference: "Trenholm, S. et Marmolejo-Ramos, F. (2024). When video improves learning in higher education. Education Sciences, 14(3), article 311."
doi: 10.3390/educsci14030311
axe: [F2]
type_etude: critique et réanalyse (méta-régression robuste) des données de la méta-analyse de Noetel et al. (2021), avec un classement des disciplines selon Biglan
public: les 105 essais randomisés de Noetel et al. (106 contextes), supérieur, à plus de 80 % en santé
lecture: texte complet, 09/11/2026
regles:
  - outil: CapsuleForge
    regle: "en mécanique et en mathématiques, utiliser la capsule en complément d'une séance ou d'exercices, pas en remplacement : l'effet du remplacement est plus faible dans les disciplines « dures »"
    niveau: C
    transferabilite: moyenne
    note: "remplacement : effet médian 0,15 (disciplines dures) contre 0,37 (molles), p = 0,008 ; comparaison entre études"
  - outil: CapsuleForge
    regle: "pour un contenu conceptuel ou abstrait, faire suivre la capsule d'une tâche qui oblige à raisonner (exercice ExoForge, question ouverte), pas seulement de questions de rappel"
    niveau: D
    transferabilite: moyenne
    note: "hypothèse des auteurs : la vidéo aiderait surtout les apprentissages de bas niveau ; non testée dans leurs données"
  - outil: DiagForge
    regle: "évaluer l'effet d'une capsule séparément sur les items de rappel ou de procédure et sur les items conceptuels ou de transfert"
    niveau: D
    transferabilite: forte
---

# Quand la vidéo améliore-t-elle l'apprentissage ? Réanalyse de Noetel et al. (Trenholm et Marmolejo-Ramos, 2024)

Trenholm, S. et Marmolejo-Ramos, F. (2024). When video improves learning in higher education. *Education Sciences*, 14(3), article 311. [DOI](https://doi.org/10.3390/educsci14030311)

**En une phrase.** La méta-analyse de [Noetel et al. (2021)](noetel2021b.md) repose à 80 % sur des études de santé et à 89 % sur des disciplines appliquées ; en réanalysant ses données, les auteurs trouvent que remplacer un enseignement par une vidéo aide moins dans les disciplines « dures » (effet médian 0,15 contre 0,37) et en déduisent, sans le mesurer, que le bénéfice de la vidéo se limite aux apprentissages de bas niveau.

## La source

| | |
| --- | --- |
| **Équipe** | Université d'Australie-Méridionale : « Education Futures » (didactique des mathématiques, premier auteur) et centre C3L (statistique). Le premier auteur a publié sur les vidéos de cours enregistrées en mathématiques, études qu'il cite à l'appui de sa thèse (références 15, 50 et 54). |
| **Nature** | Académique ; aucun financement externe ; pas de conflit d'intérêts (p. 8). |
| **Support** | *Education Sciences* (MDPI), rubrique « Review », libre accès. |
| **Audience** | 24 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Moyenne : données de Noetel et al. publiques, modèle écrit (p. 6), annexes en ligne ; le codage Biglan de chaque étude n'est pas donné dans l'article. La démarche se refait ; les chiffres se vérifient avec les annexes. Pages citées : « N of 11 ». |

## Ce que fait l'étude

- **Question 1** (p. 3-5) : décrire les domaines des études de Noetel et al. (tableau 1), puis les classer selon la taxonomie des disciplines de Biglan (dur/mou, pur/appliqué, vivant/non vivant ; tableau 2).
- **Question 2** (p. 5-6) : réanalyser les deux jeux de données (vidéo en remplacement, vidéo en complément) par un modèle linéaire mixte robuste, en ajoutant les trois axes de Biglan aux modérateurs de Noetel et al. (cadre, comparaison, type de mesure, interactivité, thème ou cours), avec l'étude en effet aléatoire ; comparaisons deux à deux.
- **Discussion** (p. 6-8) : interprétation en termes de niveau cognitif (taxonomie de Bloom) et d'autorégulation.

## Résultats

- **Domaines** (tableau 1, p. 3-4) : médecine 52 sur 106 (49 %), soins infirmiers 13, dentisterie 8 ; ingénierie 1, physique 1, informatique 2 ; plus de 80 % en santé ; 102 sur 106 dans des formations professionnalisantes.
- **Biglan** (tableau 2, p. 5) : 94 sur 106 en disciplines appliquées, 79 « dures » ; dur-appliqué-non vivant (le plus proche de l'ingénierie) : 11.
- **Remplacement** (p. 6) : disciplines molles 0,37 [0,19 ; 0,55] contre dures 0,15 [0,07 ; 0,23], p = 0,008 ; devoirs à la maison 0,59 contre TD 0,40 (p = 0,018) ; connaissances 0,16 contre savoir-faire 0,27, différence non significative (p = 0,238), contrairement à Noetel et al.
- **Complément** (p. 6) : tendance inverse, disciplines dures plus favorables (p = 0,08) ; supports statiques 1,07 contre enseignant 0,30 comme comparaison (p < 0,001) ; savoir-faire 1,05 contre connaissances 0,54 (p = 0,048).
- **Conclusion des auteurs** (p. 6-8) : la vidéo profite aux apprentissages de bas niveau (faits, procédures) ; des effets négatifs « émergeraient » pour les apprentissages de haut niveau, par exemple en mathématiques pures.

## Avis critique

**Apport.** Rappelle que la base de preuves sur la vidéo vient presque entièrement de la santé et qu'une seule étude porte sur l'ingénierie ; donne le seul chiffre qui sépare disciplines « dures » et « molles » dans ces données.

**Points forts**
- Données publiques réutilisées, modèle robuste adapté à des résidus non normaux.
- Description des domaines que Noetel et al. ne donnaient pas.
- Distingue remplacement et complément, comme l'étude d'origine.

**Réserves**
1. **Majeure** — L'affirmation principale (« seulement pour les apprentissages de bas niveau ») n'est pas mesurée : le niveau cognitif des tests n'est codé dans aucune étude ; il est déduit de la discipline (médecine = faits) par renvoi à la littérature (p. 4). C'est une hypothèse.
2. **Importante** — Les modérateurs restent des comparaisons entre études, non causales ; nombreuses comparaisons deux à deux sans correction annoncée, plusieurs p proches de 0,05 (0,046 ; 0,048). Les effets restent positifs partout, y compris dans les disciplines dures.
3. **Importante** — L'argument sur les mathématiques (effets négatifs des vidéos de cours enregistrées) s'appuie sur d'autres travaux, en partie du premier auteur, portant sur des captations de cours facultatives et corrélationnelles, pas sur des capsules conçues avec questions (p. 7).
4. **Mineure** — Codage Biglan de la dentisterie et des soins infirmiers par une révision de la taxonomie ; une étude comptée deux fois (106 pour 105, p. 5).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| La base de Noetel et al. est surtout en santé et en disciplines appliquées | B | Décompte vérifiable sur données publiques |
| Remplacer par une vidéo aide moins dans les disciplines dures | C | Modérateur entre études, un seul test |
| La vidéo n'aide que les apprentissages de bas niveau | D | Niveau cognitif non mesuré |
| La vidéo nuirait aux apprentissages de haut niveau | D | Extrapolation, aucune donnée dans la réanalyse |

**Transférabilité** : moyenne. Le constat sur la base de preuves concerne directement la mécanique et les mathématiques ; le mécanisme proposé reste à tester.

**Pour conclure, il faudrait** comparer, dans un cours de mécanique, une capsule suivie de questions de rappel et la même capsule suivie d'un exercice ExoForge, avec un test différé qui sépare items procéduraux et items conceptuels.

## Pour Forge

- **CapsuleForge** : en mécanique et mathématiques, capsule en complément, pas en remplacement (niveau C).
- **CapsuleForge** : après une capsule conceptuelle, une tâche de raisonnement, pas seulement du rappel (niveau D).
- **DiagForge** : séparer items de rappel ou de procédure et items conceptuels dans l'analyse d'une capsule (niveau D).
- Renvois : [Noetel et al., 2021](noetel2021b.md) (méta-analyse réanalysée), [Brame, 2016](brame2016.md).
