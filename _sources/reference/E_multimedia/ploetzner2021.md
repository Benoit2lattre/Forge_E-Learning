---
cle: ploetzner2021
reference: "Ploetzner, R., Berney, S. et Bétrancourt, M. (2021). When learning from animations is more successful than learning from static pictures: learning the specifics of change. Instructional Science, 49, 497-514."
doi: 10.1007/s11251-021-09541-w
axe: [E3]
type_etude: essai randomisé à trois groupes (une image, quatre images, animation), une séance d'environ 50 minutes, 88 participants ; pré-étude de validation du test (33 participants)
public: étudiants en formation d'enseignants (STEM et autres disciplines), université du sud-ouest de l'Allemagne ; mécanisme à six barres (engrenage plan)
lecture: texte complet, 09/11/2026
regles:
  - outil: CapsuleForge
    regle: "animer un mécanisme quand l'objectif est le détail du mouvement (vitesse non uniforme, arrêts, oscillation asymétrique, sens) ; une suite de quelques images fixes ne remplace pas l'animation dans ce cas"
    niveau: C
    transferabilite: forte
    note: "76 % contre 33-35 % de reconnaissance des mouvements, d = 2,3-2,4 ; quatre images pas mieux qu'une seule"
  - outil: CapsuleForge
    regle: "montrer une image fixe du mécanisme quand l'objectif est la disposition (quelle pièce est liée à quelle autre, positions relatives), en plus de l'animation"
    niveau: C
    transferabilite: forte
    note: "98 % avec une image contre 73 % avec quatre images ou l'animation, d = 1,1-1,3 ; effet plafond"
  - outil: ExoForge
    regle: "dans un exercice de cinématique ou de mécanisme, fournir l'animation pour les questions sur le mouvement et une figure fixe cotée pour les questions sur la géométrie et les liaisons"
    niveau: C
    transferabilite: forte
---

# Animer pour apprendre le détail d'un mouvement (Ploetzner et al., 2021)

Ploetzner, R., Berney, S. et Bétrancourt, M. (2021). When learning from animations is more successful than learning from static pictures: learning the specifics of change. *Instructional Science*, 49, 497-514. [DOI](https://doi.org/10.1007/s11251-021-09541-w)

**En une phrase.** Après deux minutes devant un mécanisme à six barres, les étudiants qui ont vu l'animation reconnaissent le mouvement de chaque barre bien mieux (76 %) que ceux qui ont vu une ou quatre images fixes (33-35 %, près du hasard), mais retiennent moins bien la disposition des barres que ceux qui ont vu une seule image (73 % contre 98 %) : l'animation sert à apprendre comment les choses bougent, l'image fixe à apprendre comment elles sont agencées.

## La source

| | |
| --- | --- |
| **Équipe** | Département de psychologie, Université d'éducation de Fribourg-en-Brisgau ; TECFA, Université de Genève. Berney et Bétrancourt sont les auteurs de la méta-analyse [berney2016](berney2016.md), dont l'équipe a tiré en 2020 l'hypothèse testée ici : les auteurs mettent à l'épreuve leur propre hypothèse. |
| **Nature** | Académique ; aucun financement spécifique, pas de conflit d'intérêts (p. 512) ; participants rémunérés. |
| **Support** | *Instructional Science* (Springer), libre accès (CC BY). |
| **Audience** | 63 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Bonne pour les données (OSF, doi 10.17605/OSF.IO/QP6UG, p. 512) et le protocole ; matériel non diffusé (droits sur la reconstruction du mécanisme), mais animation d'origine en ligne (p. 501). La démarche se refait ; les chiffres se vérifient. |

## Ce que fait l'étude

- **Contenu** (p. 501-502) : mécanisme plan à six barres qui transforme une rotation uniforme en rotation discontinue de la sortie avec trois arrêts ; coupleurs non uniformes, manivelle à oscillation asymétrique.
- **Pré-étude** (p. 502-504) : 33 étudiants vérifient qu'on distingue bien les quatre mouvements ou dispositions proposés ; 92,7 % et 97,3 % de réussite.
- **Groupes** (p. 504-506) : tirage au sort entre une image (30), quatre images numérotées tirées de l'animation (28) et animation non interactive (30) ; sens de rotation de la roue d'entrée indiqué à tous. Présentation de 2 minutes, deux fois (une avant chaque tâche, ordre contrebalancé), après un exemple d'entraînement de 90 s sur un quadrilatère articulé.
- **Mesures** (p. 506-507) : reconnaissance du mouvement de chaque barre parmi quatre animations (5 points) ; reconnaissance de la disposition de chaque paire de barres parmi quatre images (4 points) ; covariables : aptitude mécanique (12 items) et aptitude spatiale (15 items de pliage).

## Résultats

| Mesure (tableau 1, p. 509) | Une image | Quatre images | Animation |
| --- | --- | --- | --- |
| Mouvements (/5) | 1,77 (35 %) | 1,64 (33 %) | 3,80 (76 %) |
| Dispositions (/4) | 3,93 (98 %) | 2,93 (73 %) | 2,93 (73 %) |

- **Analyse multivariée** (tableau 3, p. 510) : lambda de Wilks 0,35 ; mouvements F = 52,29, η² = 0,55 ; dispositions F = 11,17, η² = 0,21 ; p < 0,001.
- **Comparaisons** (p. 509) : mouvements, animation > une image (d = 2,33) et > quatre images (d = 2,41) ; une image = quatre images (p = 0,606). Dispositions, une image > quatre images (d = 1,11) et > animation (d = 1,30) ; quatre images = animation (p = 0,985).
- **Hasard** : 25 % pour chaque item à quatre choix ; les groupes « images » sont à 33-35 % sur les mouvements, à peine au-dessus [calcul].
- **Covariables** (p. 508-509) : groupes équivalents ; ni l'aptitude mécanique ni l'aptitude spatiale ne prédisent les résultats (corrélations de −0,08 à 0,19).

## Avis critique

**Apport.** Précise quand une animation vaut l'effort de production : quand il faut apprendre le détail d'un changement (vitesse, arrêts, asymétrie), ce qui est le cas en cinématique et en mécanismes. Résultat cohérent avec la ré-analyse de [berney2016](berney2016.md) (g = 0,65 pour les changements complexes à apprendre, cité p. 498).

**Points forts**
- Tirage au sort, trois groupes dont une suite d'images qui contrôle la quantité d'information.
- Test validé dans une pré-étude ; données ouvertes.
- Contenu de génie mécanique.

**Réserves**
1. **Importante** — Mesure perceptive et immédiate : reconnaître un mouvement vu deux minutes plus tôt, sans compréhension du fonctionnement ni test différé ; les auteurs le reconnaissent (p. 510).
2. **Importante** — Tests très courts (5 et 4 items) : effet plafond pour la disposition avec une image (98 %, ET 0,25) et tailles d'effet gonflées (d de 1,1 à 2,4) ; les valeurs ne se transposent pas.
3. **Importante** — Le test de mouvement est lui-même fait d'animations : le groupe animation compare ce qu'il a vu à ce qu'on lui montre, les autres doivent imaginer le mouvement ; c'est précisément l'hypothèse testée, mais cela favorise la forme animée.
4. **Mineure** — Public : futurs enseignants, 76 % de femmes, sans mesure de connaissances en mécanique au-delà des tests d'aptitude ; une séance unique de laboratoire, animation sans narration ni contrôle.
5. **Mineure** — Les auteurs valident une hypothèse issue de leur propre ré-analyse.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| L'animation fait mieux que des images fixes pour reconnaître des mouvements complexes | C | Un essai randomisé net, mais mesure perceptive immédiate, une séance |
| Une image fixe fait mieux qu'une animation pour retenir une disposition spatiale | C | Même essai, effet plafond, 4 items |
| Quatre images ne suffisent pas pour inférer un mouvement non uniforme | C | Une seule étude, un seul mécanisme |

**Transférabilité** : forte pour le contenu (mécanismes, cinématique du solide) ; moyenne pour le public. Nos étudiants, qui connaissent la cinématique, inféreraient peut-être mieux le mouvement à partir d'images, ce qui n'est pas testé.

**Pour conclure, il faudrait** proposer dans ExoForge un exercice de cinématique d'un mécanisme (bielle-manivelle, quadrilatère articulé) avec animation ou suite d'images, tiré au sort, et mesurer à la fois la reconnaissance du mouvement, la prévision de la vitesse d'un point et un test différé.

## Pour Forge

- **CapsuleForge** : animer quand il faut apprendre le détail du mouvement ; quelques images clés ne le remplacent pas (niveau C). Montrer aussi une image fixe pour la disposition des pièces (niveau C).
- **ExoForge** : animation pour les questions sur le mouvement, figure fixe pour la géométrie et les liaisons (niveau C).
- Nuance la règle du README « pour un schéma abstrait, une suite d'images fixes annotées peut suffire » ([berney2016](berney2016.md), [kalyuga2008](kalyuga2008.md)) : elle vaut pour les changements simples ou abstraits, pas pour un mouvement non uniforme. Renvois : [hoffler2007](hoffler2007.md), [mcelhaney2015](mcelhaney2015.md).
