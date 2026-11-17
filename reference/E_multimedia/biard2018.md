---
cle: biard2018
reference: "Biard, N., Cojean, S. et Jamet, E. (2018). Effects of segmentation and pacing on procedural learning by video. Computers in Human Behavior, 89, 411-417."
doi: 10.1016/j.chb.2017.12.002
axe: [E1]
type_etude: essai en classe, trois groupes (vidéo continue, vidéo avec bouton pause, vidéo segmentée avec pauses imposées et bouton pause), 68 étudiants, une séance
public: étudiants de 2e année d'ergothérapie, université Rennes 2 (87 % de femmes), novices ; procédure clinique (fabrication d'une orthèse de main)
lecture: texte complet, 09/11/2026
regles:
  - outil: CapsuleForge
    regle: "vidéo de procédure (suite d'étapes) : arrêt imposé à la fin de chaque étape, reprise par un bouton Lecture ou Continuer, en plus du bouton pause libre"
    niveau: C
    transferabilite: moyenne
    note: "procédure gestuelle en ergothérapie ; à transposer aux étapes d'une méthode de calcul ou d'une manipulation de TP"
  - outil: CapsuleForge
    regle: "ne pas compter sur le bouton pause pour découper une capsule : près de la moitié des étudiants ne s'en servent pas, les autres deux fois en moyenne ; le découpage est fait par l'enseignant"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "correction ou démonstration d'une procédure en plusieurs étapes : faire avancer étape par étape au clic plutôt qu'en déroulé continu"
    niveau: D
    transferabilite: moyenne
    note: "extrapolation de la vidéo à une correction HTML"
---

# Segmentation imposée d'une vidéo de procédure (Biard et al., 2018)

Biard, N., Cojean, S. et Jamet, E. (2018). Effects of segmentation and pacing on procedural learning by video. *Computers in Human Behavior*, 89, 411-417. [DOI](https://doi.org/10.1016/j.chb.2017.12.002)

**En une phrase.** Pour apprendre une procédure par vidéo, des étudiants novices qui disposent d'un bouton pause ne s'en servent presque pas et ne font pas mieux que ceux qui regardent une vidéo continue ; une vidéo arrêtée automatiquement à chaque étape améliore la reproduction de la procédure (44,8 contre 37,1 et 38,4 sur 60) mais pas le rappel verbal : pour CapsuleForge, c'est l'enseignant qui découpe, pas l'étudiant.

## La source

| | |
| --- | --- |
| **Équipe** | Laboratoire de psychologie LP3C, université Rennes 2 ; E. Jamet travaille de longue date sur le multimédia (signalement, vidéo). |
| **Nature** | Académique ; déclaration d'absence d'intérêt financier ou personnel (p. 416) ; financement non rapporté. |
| **Support** | *Computers in Human Behavior* (Elsevier). |
| **Audience** | 174 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Moyenne : découpage en 7 étapes et 25 sections décrit (p. 413-414), barème de la tâche procédurale donné (p. 414) ; vidéo, lecteur, questions de rappel et données non publiés. La démarche se refait ; les chiffres ne se vérifient qu'à partir des tableaux 1 et 2. |

## Ce que fait l'étude

- **Participants** (p. 413) : 68 étudiants de 2e année d'ergothérapie, âge moyen 21,9 ans, tous novices en fabrication d'orthèses ; « répartis de façon égale et équitable » entre trois groupes (le tirage au sort n'est pas explicitement décrit). Vidéo intégrée au cursus.
- **Matériel** (p. 413-414) : vidéo de 312 s (mains de l'enseignant et du patient) en 7 étapes principales. Vidéo continue sans pause (n = 23) ; vidéo avec bouton lecture/pause (n = 23) ; vidéo segmentée en 25 sections par un expert, soit 24 arrêts imposés, avec reprise au clic et bouton pause libre (n = 22). Ni retour en arrière, ni second visionnage, ni prise de notes.
- **Déroulement** (p. 414) : par groupes de 4, pendant un cours réel de 45 min ; consigne explicite d'utiliser la pause si besoin.
- **Mesures** (p. 414) : tâche procédurale immédiate (tracer le patron sur un gabarit d'avant-bras : 10 repères et 20 lignes, sur 60, notée par un expert) ; test de rappel de 5 questions ouvertes (sur 15). Pas de mesure de charge, pas de test différé.

## Résultats

| Mesure (tableaux 1 et 2, p. 414-415) | Continue (n = 23) | Bouton pause (n = 23) | Segmentée (n = 22) |
| --- | --- | --- | --- |
| Pauses libres (nombre moyen) | — | 2,35 (3,70) | 2,18 (3,63) |
| Durée totale des pauses (s) | — | 16,33 (28,01) | 158,06 (70,25) |
| Tâche procédurale (sur 60) | 38,43 (8,52) | 37,09 (9,92) | 44,77 (8,86) |
| Rappel (sur 15) | 4,52 (3,10) | 4,52 (2,96) | 4,73 (2,93) |

- **Usage du bouton** (p. 414) : 47,83 % (bouton seul) et 40,91 % (segmentée) des étudiants ne font aucune pause ; ceux qui en font en font environ deux, courtes. Durée totale des pauses 10 fois plus longue avec la segmentation, F(1, 43) = 80,31, η² = 0,65. Pause imposée moyenne ≈ 6 s ((158,06 − 10,23)/24 [calcul]).
- **Tâche procédurale** (p. 415) : F(2, 65) = 4,51, p = 0,015, η²p = 0,12. Segmentée contre continue : t(65) = 2,44, p = 0,023 rapporté (≈ 0,017 recalculé en bilatéral [calcul]), d ≈ 0,73 [calcul, moyennes et écarts-types du tableau 2]. Segmentée contre bouton seul : t(65) = 2,74, p = 0,006 rapporté (≈ 0,008 [calcul]), d ≈ 0,82 [calcul]. Bouton seul contre continue : p = 0,618.
- **Rappel** (p. 415) : aucun effet (F < 1) ; les auteurs invoquent un effet plancher (moins d'un tiers de bonnes réponses dans chaque groupe).

## Avis critique

**Apport.** Montre, dans un vrai cours et sur une procédure, que fournir un bouton pause ne suffit pas à des novices et qu'un découpage imposé aux étapes de la procédure améliore l'exécution. Avec Hasler et al. (2007) et Liu et al. (2021), c'est le troisième essai lu où la majorité des étudiants n'utilise pas la pause.

**Points forts**
- Cours réel, contenu du cursus, étudiants réellement novices.
- Usage des contrôles enregistré (nombre et durée des pauses).
- Mesure alignée sur l'objectif : reproduire la procédure, notée sur un barème explicite.

**Réserves**
1. **Importante** — Temps confondu : le groupe segmenté passe environ 2,5 min de plus devant la vidéo (158 s de pauses contre 16 s) ; on ne sait pas si l'effet vient du découpage ou du temps supplémentaire. Les auteurs proposent eux-mêmes cette explication (p. 415).
2. **Importante** — Petits groupes (22-23), une séance, test immédiat seulement (limite reconnue p. 415) ; tirage au sort non explicitement décrit ; notation par un seul expert, sans mention d'aveugle ni d'accord inter-juges.
3. **Mineure** — Incohérences de rapport : test de rappel décrit comme « cinq questions notées chacune sur 15 » (p. 414) mais échelle totale 0-15 (tableau 2) ; p rapportés différents de ceux qui découlent des t (0,023 contre ≈ 0,017 ; 0,006 contre ≈ 0,008 [calcul]) ; moyenne 44,7 dans le texte, 44,77 dans le tableau. Aucune ne change la conclusion.
4. **Mineure** — Pas de groupe « segmentée sans bouton » : l'apport propre du bouton dans la condition segmentée n'est pas testé (choix justifié p. 414).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les novices utilisent peu le bouton pause | C | Mesuré ici, concordant avec Hasler et al. (2007) et Liu et al. (2021) ; petits effectifs |
| Segmentation imposée par étapes > vidéo continue ou bouton seul pour exécuter une procédure | C | Un essai, une séance, temps d'étude confondu, d ≈ 0,7-0,8 |
| Segmentation sans effet sur le rappel verbal | D | Effet plancher, pas de conclusion possible |

**Transférabilité** : moyenne. Étudiants du supérieur novices, vidéo en autonomie, mais procédure gestuelle hors sciences ; le mécanisme (l'étudiant ne sait pas où couper) vaut pour une méthode de calcul en étapes ou une manipulation de TP.

**Pour conclure, il faudrait** comparer, dans CapsuleForge, une capsule de méthode (par exemple les étapes d'un calcul de réactions d'appui) en version continue avec bouton pause et en version arrêtée à chaque étape, à durée totale égale (pauses compensées par un temps de revisionnage), avec un exercice d'application dans ExoForge une semaine après.

## Pour Forge

- **CapsuleForge** : dans une capsule de procédure, un arrêt imposé par étape, reprise par « Continuer », bouton pause conservé (niveau C).
- **CapsuleForge** : ne pas déléguer le découpage à l'étudiant ; le bouton pause seul ne change rien ici (niveau C).
- **ExoForge** : correction d'une procédure déroulée étape par étape au clic (niveau D).
- Renvois : [rey2019](rey2019.md) (méta-analyse de la segmentation), [hasler2007](hasler2007.md) et [liu2021](liu2021.md) (usage du bouton pause), [fyfield2022](fyfield2022.md), [mayer2019](mayer2019.md).
