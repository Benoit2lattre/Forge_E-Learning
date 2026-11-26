---
cle: mayer2019
reference: "Mayer, R. E., Wells, A., Parong, J. et Howarth, J. T. (2019). Learner control of the pacing of an online slideshow lesson: Does segmenting help? Applied Cognitive Psychology, 33(5), 930-935."
doi: 10.1002/acp.3560
axe: [E1, E2]
type_etude: expérience en laboratoire, plan 2 x 2 inter-sujets (taille des segments x voix ou texte), 99 étudiants, une séance
public: étudiants de première année d'une université américaine (hors géographie), leçon sur un système d'information géographique
lecture: texte complet, 08/11/2026
regles:
  - outil: CapsuleForge
    regle: "dans une diapositive dense parcourue au rythme de l'étudiant, révéler la diapositive par blocs (2 à 4) à chaque clic sur « Continuer » plutôt que de l'afficher entière"
    niveau: C
    transferabilite: forte
  - outil: CapsuleForge
    regle: "quand l'étudiant contrôle le rythme, ne pas compter sur la voix seule pour améliorer l'apprentissage : un texte écrit lu à son rythme fait aussi bien"
    niveau: C
    transferabilite: moyenne
    note: "pas d'effet de modalité ici ; durée d'étude plus longue avec la voix (626 s contre 501 s)"
  - outil: ExoForge
    regle: "dans une page de correction ou d'exemple résolu longue, afficher les étapes une à une sur demande (bouton « étape suivante ») plutôt que tout le développement d'un coup"
    niveau: D
    transferabilite: moyenne
    note: "extrapolation du diaporama à la page d'exercice"
---

# Révéler une diapositive par parties (Mayer et al., 2019)

Mayer, R. E., Wells, A., Parong, J. et Howarth, J. T. (2019). Learner control of the pacing of an online slideshow lesson: Does segmenting help? *Applied Cognitive Psychology*, 33(5), 930-935. [DOI](https://doi.org/10.1002/acp.3560)

**En une phrase.** Dans un diaporama de 12 diapositives parcouru au rythme de l'étudiant, ajouter chaque bloc de la diapositive à chaque appui sur « Continuer » améliore un test de transfert (effet annoncé d = 0,34, plutôt 0,47 recalculé) par rapport à l'affichage de la diapositive entière, que les mots soient lus ou écrits ; c'est un appui direct pour les révélations par clic dans CapsuleForge, au niveau indicatif.

## La source

| | |
| --- | --- |
| **Équipe** | Psychologie, université de Californie à Santa Barbara (Mayer, auteur des principes multimédia) ; géographie, Middlebury College (Howarth). Réplique une étude antérieure de la même équipe (Mayer et al., 2018). |
| **Nature** | Académique ; financement de la National Science Foundation (subvention 1504940, p. 934) ; pas de conflit d'intérêts déclaré. Les auteurs testent un principe qu'ils ont eux-mêmes formulé. |
| **Support** | *Applied Cognitive Psychology* (Wiley), format « short paper ». |
| **Audience** | 33 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : leçon et procédure décrites (fig. 1), test de 6 problèmes et barème non publiés, données non publiées. La démarche se refait ; les chiffres ne se vérifient qu'en partie (voir réserves). |

## Ce que fait l'étude

- **Participants** (p. 932) : 99 étudiants (âge moyen 18,4 ans), connaissance de la géographie jugée faible (2,60 sur 5) ; 24 à 26 par groupe.
- **Leçon** (p. 931-932) : 12 diapositives PowerPoint, exemple résolu d'utilisation de quatre outils d'un SIG (cartes, matrices de pixels) ; environ 177 mots par diapositive. Rythme contrôlé par l'étudiant (flèche droite = suite).
- **Facteurs** : grand segment (diapositive entière à chaque clic) ou petit segment (un rang de la diapositive ajouté à chaque clic, 2 à 4 par diapositive) ; mots écrits ou lus par une voix humaine enregistrée.
- **Tirage** (p. 932) : par séance de 1 à 3 participants, tous dans le même groupe.
- **Mesures** (p. 932) : 6 problèmes de transfert (2 min chacun, sur 6 points, deux correcteurs) ; questionnaire de goût, effort et difficulté (5 points) ; durée d'étude.

## Résultats

| Groupe (tableau 1, p. 932) | Transfert (sur 6) |
| --- | --- |
| Grand segment, voix | 1,78 (1,12) |
| Petit segment, voix | 2,23 (1,08) |
| Grand segment, texte | 1,68 (0,92) |
| Petit segment, texte | 2,21 (1,06) |

- **Segmentation** (p. 932) : 2,22 contre 1,73, F(1, 95) = 5,40, p = 0,02, d annoncé = 0,34 ; d ≈ 0,47 à partir des moyennes et écarts-types (écart-type commun ≈ 1,04) et ≈ 0,48 à partir du F [calcul]. L'effet reste significatif avec la durée d'étude en covariable.
- **Modalité** (p. 932-933) : pas d'effet (texte 1,95, voix 2,12 ; F = 0,09, p = 0,77) ni d'interaction (p = 0,84).
- **Durée** (p. 933) : petits segments 591 s contre 535 s (d = 0,46) ; voix 626 s contre texte 501 s (d = 1,16).
- **Ressenti** (p. 933) : MANOVA sans effet, sauf la difficulté perçue, plus faible avec les petits segments (3,75 contre 4,17, d = 0,43).

## Avis critique

**Apport.** Transpose la segmentation, établie surtout pour les animations, au cas du diaporama parcouru par clic : la bonne taille de segment est une idée par bloc, pas une diapositive. Sur un contenu procédural et graphique (matrices, règles), plus proche de la mécanique que bien des études du domaine.

**Points forts**
- Une seule différence entre petit et grand segment (même contenu, même rythme libre).
- Mesure de transfert, notée par deux correcteurs.
- Effet maintenu à durée d'étude contrôlée.
- Réplication d'une étude antérieure.

**Réserves**
1. **Importante** — Une séance de moins de 30 min, test immédiat, scores bas (environ 2 sur 6, effet plancher possible) : rien sur la rétention.
2. **Importante** — Même équipe que l'étude répliquée et que le principe testé ; pas de réplication indépendante dans ce format précis.
3. **Mineure** — Incohérences internes : d annoncé (0,34) inférieur au d qui découle des moyennes (≈ 0,47 [calcul]) ; durées par groupe mal étiquetées (deux « large-segment/text », deux « small-segment/voice », p. 933), les moyennes marginales permettent de les réattribuer [calcul].
4. **Mineure** — Tirage par séance (jusqu'à 3 personnes ensemble), analyse au niveau individuel ; effet faible vu la taille des grappes.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Révéler la diapositive par blocs sur clic améliore le transfert | C | Un essai de laboratoire en une séance, répliquant une étude de la même équipe ; cohérent avec rey2019 |
| Pas d'avantage de la voix sur le texte quand l'étudiant contrôle le rythme | C | Absence d'effet sur 99 personnes ; cohérent avec la condition limite du principe de modalité (mayer2017) |

**Transférabilité** : forte pour le mécanisme (diaporama en ligne, étudiants du supérieur, contenu procédural et graphique) ; moyenne pour la modalité (voix enregistrée lisant un texte long, pas une narration courte).

**Pour conclure, il faudrait** comparer dans CapsuleForge une capsule de statique ou de RDM avec révélation par blocs et la même avec diapositives entières, avec un quiz de transfert différé d'une semaine.

## Pour Forge

- **CapsuleForge** : en mode « au rythme de l'étudiant », un clic ajoute un bloc (texte + figure associée) ; 2 à 4 blocs par diapositive dense (niveau C).
- **CapsuleForge** : en rythme libre, une version texte écrit est acceptable ; la voix n'est pas obligatoire (niveau C), voir [adesope2012](adesope2012.md) pour la redondance.
- **ExoForge** : correction pas à pas révélée sur demande (niveau D, extrapolation).
- Renvois : [liu2022](liu2022.md) (apparitions synchronisées en rythme imposé), [rey2019](rey2019.md) (méta-analyse de la segmentation), [mayer2021](mayer2021.md).
