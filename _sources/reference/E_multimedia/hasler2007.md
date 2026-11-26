---
cle: hasler2007
reference: "Hasler, B. S., Kersten, B. et Sweller, J. (2007). Learner control, cognitive load and instructional animation. Applied Cognitive Psychology, 21(6), 713-729."
doi: 10.1002/acp.1345
axe: [E1, E3]
type_etude: essai randomisé individuel en une séance, quatre conditions (animation continue, animation segmentée, animation avec boutons stop/lecture, narration seule), 72 élèves
public: garçons de 9 à 11 ans d'une école préparatoire pour garçons de Sydney (Scots College) ; astronomie (alternance du jour et de la nuit)
lecture: texte complet, 09/11/2026
regles:
  - outil: CapsuleForge
    regle: "animation narrée d'un phénomène où plusieurs éléments interagissent : découper en segments d'environ 20 s avec arrêt automatique et bouton Lecture, ou au minimum offrir des boutons pause et lecture ; jamais d'animation continue sans contrôle"
    niveau: C
    transferabilite: moyenne
    note: "enfants de 9-11 ans ; effet seulement sur les questions qui relient plusieurs éléments"
  - outil: ExoForge
    regle: "toute animation insérée dans un exercice a des boutons pause et lecture et ne se relance pas seule en boucle"
    niveau: C
    transferabilite: moyenne
  - outil: QuizForge
    regle: "dans le quiz qui suit une capsule, inclure des questions qui obligent à relier plusieurs éléments (expliquer, prédire) et pas seulement du rappel : c'est sur elles que la présentation fait une différence"
    niveau: C
    transferabilite: forte
---

# Contrôle du rythme d'une animation par l'élève (Hasler et al., 2007)

Hasler, B. S., Kersten, B. et Sweller, J. (2007). Learner control, cognitive load and instructional animation. *Applied Cognitive Psychology*, 21(6), 713-729. [DOI](https://doi.org/10.1002/acp.1345)

**En une phrase.** Chez des enfants de 9-11 ans, une animation narrée découpée en 11 segments ou munie de boutons stop/lecture donne de meilleurs résultats aux questions complexes qu'une animation continue (d ≈ 1,2 [calcul]), alors que 11 élèves sur 18 n'ont jamais touché aux boutons : pour CapsuleForge, une animation doit être découpée ou contrôlable, mais l'effet du simple bouton reste inexpliqué.

## La source

| | |
| --- | --- |
| **Équipe** | Psychologie, universités de Zurich et de Berne ; J. Sweller (université de Nouvelle-Galles du Sud, Sydney), auteur de la théorie de la charge cognitive, cadre que l'étude veut confirmer. |
| **Nature** | Académique ; financement non rapporté ; remerciements à l'école (p. 725). |
| **Support** | *Applied Cognitive Psychology* (Wiley), numéro spécial sur les animations. |
| **Audience** | 399 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Moyenne : les 13 questions et leur indice de difficulté sont publiés (annexe B, p. 729), exemples de segments (annexe A, p. 728) ; animation Flash et données non publiées. La démarche se refait ; les chiffres se vérifient sur le tableau 1. |

## Ce que fait l'étude

- **Participants** (p. 718) : 72 garçons de 9 à 11 ans, habitués aux ordinateurs portables, sujet pas encore enseigné ; tirage au sort en quatre groupes de 18.
- **Matériel** (p. 718-719) : animation Flash narrée par une voix masculine sur le jour et la nuit, 3 min 45 s en continu. Segmentée : 11 segments de 19,1 s en moyenne (47 mots), arrêt automatique, reprise au clic. Stop/lecture : boutons utilisables à tout moment. Continue et narration seule : sans contrôle, mais relançables à la fin.
- **Temps d'étude égalisé** (p. 718-719) : 10 min pour tous, temps restant affiché ; les élèves relancent la présentation autant qu'ils le peuvent.
- **Consignes** (p. 720) : les groupes segmenté et stop/lecture sont invités à « penser à ce qu'ils viennent de voir » quand l'animation s'arrête ; les autres groupes reçoivent seulement la consigne d'apprendre.
- **Mesures** (p. 719-721) : difficulté perçue sur 9 points ; 13 questions ouvertes, classées avant l'expérience en 8 à faible interactivité des éléments (3 éléments ou moins) et 5 à forte interactivité (4 ou plus) ; deux correcteurs (r = 0,94), alpha = 0,64 ; efficience = (z performance − z charge)/√2.

## Résultats

| Mesure (tableau 1, p. 722) | Stop/lecture | Segmentée | Continue | Narration seule |
| --- | --- | --- | --- | --- |
| Total (sur 13) | 9,03 (2,46) | 8,69 (2,32) | 6,96 (1,94) | 6,92 (1,99) |
| Faible interactivité (sur 8) | 5,90 (1,65) | 5,49 (1,48) | 5,06 (1,33) | 5,10 (1,27) |
| Forte interactivité (sur 5) | 3,13 (1,08) | 3,20 (1,16) | 1,90 (1,00) | 1,82 (1,04) |
| Difficulté perçue (sur 9) | 2,78 (1,44) | 2,61 (1,58) | 3,22 (1,06) | 3,22 (1,44) |

- **Usage des contrôles** (p. 720-721) : dans le groupe stop/lecture, 11 élèves sur 18 n'utilisent jamais les boutons ; 6 arrêtent une fois pour poser une question ; un seul s'en sert régulièrement (4 fois). Dans le groupe segmenté, les arrêts durent en moyenne 2,4 s ; 10 élèves ont dû être invités à relancer après le premier segment.
- **Scores** (p. 721-722) : effet du groupe F(3, 68) = 4,71, η² = 0,17 ; interaction groupe × interactivité non significative, F(3, 68) = 2,23, p = 0,09. Analyses séparées : différence sur les questions à forte interactivité, F(3, 68) = 9,09, p < 0,001, η² = 0,29, due à l'écart entre groupes contrôlés et groupes continus (Tukey) ; rien sur les questions à faible interactivité (p = 0,27).
- **Tailles d'effet** [calcul, tableau 1] : questions à forte interactivité, stop/lecture contre continue d ≈ 1,18 ; segmentée contre continue d ≈ 1,20 ; total, stop/lecture contre continue d ≈ 0,93.
- **Élèves qui ont arrêté contre ceux qui n'ont pas arrêté**, dans le groupe stop/lecture (p. 722) : 9,77 contre 8,57, p = 0,33.
- **Charge perçue** (p. 722) : pas de différence, F(3, 68) = 0,91 ; matériel jugé facile (2,96 sur 9).
- **Animation continue = narration seule** (p. 722-724) : l'animation sans contrôle n'apporte rien par rapport à la voix seule.

## Avis critique

**Apport.** Essai souvent cité pour deux constats : découper ou rendre contrôlable une animation transitoire aide pour les contenus où les éléments interagissent ; et les apprenants n'utilisent presque pas les boutons qu'on leur donne. Le temps d'étude identique pour tous (10 min) écarte l'explication par la durée.

**Points forts**
- Tirage au sort individuel, temps d'étude égalisé, même narration dans les quatre versions.
- Questions classées a priori selon le nombre d'éléments à relier, et publiées.
- Usage réel des boutons observé.

**Réserves**
1. **Majeure** — Public très éloigné du nôtre : enfants de 9-11 ans, une seule école de garçons, sujet simple. Un contrôle du rythme utile à des enfants novices peut l'être moins à des étudiants de master (inversion d'expertise).
2. **Importante** — Le groupe stop/lecture a vu, en pratique, une animation continue (17 sur 18 ne s'arrêtent pas ou presque) ; son avantage vient donc d'autre chose que les pauses : les auteurs proposent la consigne de « penser à ce qu'on a vu » ou la surveillance du moment où s'arrêter (p. 724-725), explication non testée. La consigne diffère entre groupes contrôlés et continus : variable confondue.
3. **Importante** — Interaction groupe × type de question non significative (p = 0,09), suivie d'analyses séparées : la conclusion « seulement pour les questions complexes » est fragile.
4. **Mineure** — Fiabilité du test modeste (alpha = 0,64, 13 questions) ; prétest de 2 questions dont les résultats ne sont pas rapportés ; charge mesurée par un seul item, sans différence.
5. **Mineure** — Les arrêts entre segments ne durent que 2,4 s en moyenne : le bénéfice du découpage ne tient pas au temps de pause.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Animation découpée ou contrôlable > animation continue, surtout pour les questions à éléments interactifs | C | Un essai randomisé, effet grand, mais enfants, une séance, interaction non significative |
| Les apprenants utilisent rarement les boutons de contrôle | C | Mesuré ici ; répliqué chez des étudiants (biard2018, liu2021) |
| Le seul fait d'avoir des boutons (sans s'en servir) améliore l'apprentissage | D | Explication non testée, consignes différentes entre groupes |

**Transférabilité** : moyenne pour le principe (découper une animation transitoire, mesurer sur des questions qui relient plusieurs éléments), faible pour la valeur chiffrée (enfants).

**Pour conclure, il faudrait** comparer, avec des étudiants de L3, une animation de mécanique (par exemple un mécanisme bielle-manivelle) en version continue et en version segmentée, à même consigne et même temps d'étude, avec un quiz QuizForge séparant questions de rappel et questions de prédiction.

## Pour Forge

- **CapsuleForge** : animation découpée en segments d'environ 20 s avec arrêt automatique, ou au minimum pause et lecture ; pas d'animation continue sans contrôle (niveau C).
- **ExoForge** : animation d'exercice toujours pilotable (pause, lecture), sans boucle automatique (niveau C).
- **QuizForge** : quiz post-capsule avec des questions qui relient plusieurs éléments, pas seulement du rappel (niveau C).
- Renvois : [biard2018](biard2018.md), [liu2021](liu2021.md) (même constat d'usage des boutons chez des étudiants), [rey2019](rey2019.md), [berney2016](berney2016.md), [hoffler2007](hoffler2007.md) (animation contre image fixe).
