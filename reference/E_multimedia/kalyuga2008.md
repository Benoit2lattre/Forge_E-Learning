---
cle: kalyuga2008
reference: "Kalyuga, S. (2008). Relative effectiveness of animated and static diagrams: An effect of learner prior knowledge. Computers in Human Behavior, 24, 852-861."
doi: 10.1016/j.chb.2007.02.018
axe: [E3, D2]
type_etude: essai randomisé 2 × 2 (niveau de connaissances par partage à la médiane × animation ou images fixes), une séance de 2 minutes d'enseignement, 33 participants
public: étudiants d'une université australienne (UNSW), 18-25 ans, surtout lettres et sciences sociales ; transformations de graphes de fonctions affines et du second degré
lecture: texte complet, 09/11/2026
regles:
  - outil: CapsuleForge
    regle: "pour montrer une procédure sur un graphe (translation, dilatation, symétrie) à des débutants, préférer une suite numérotée d'images fixes annotées (flèches, coefficient en couleur) à une animation continue sans contrôle"
    niveau: C
    transferabilite: moyenne
    note: "8 à 9 participants par case, 2 minutes d'enseignement ; d ≈ 1,06 [calcul] chez les novices"
  - outil: ExoForge
    regle: "adapter le format au niveau : étapes fixes pour l'étudiant qui échoue au diagnostic, animation possible pour celui qui le réussit ; ne pas imposer le même format à tous"
    niveau: C
    transferabilite: moyenne
    note: "interaction significative (p < 0,05) ; avantage de l'animation chez les avancés non significatif (d = 0,46)"
  - outil: ExoForge
    regle: "diagnostic rapide possible par vérification d'étapes : montrer une étape intermédiaire proposée et demander en temps limité « correcte / incorrecte / je ne sais pas »"
    niveau: D
    transferabilite: moyenne
    note: "méthode validée ailleurs par l'auteur (corrélation 0,75 citée d'un article alors soumis, p. 855) ; voir kalyuga2004"
---

# Animation ou images fixes selon le niveau : graphes de fonctions (Kalyuga, 2008)

Kalyuga, S. (2008). Relative effectiveness of animated and static diagrams: An effect of learner prior knowledge. *Computers in Human Behavior*, 24, 852-861. [DOI](https://doi.org/10.1016/j.chb.2007.02.018)

**En une phrase.** Pour apprendre à transformer le graphe de y = x² (dilatation, symétrie, translation), les étudiants les plus faibles au prétest progressent davantage avec une suite d'images fixes numérotées qu'avec la même démonstration animée, tandis que les plus forts tendent à l'inverse ; l'interaction est significative mais l'étude est minuscule (8 ou 9 personnes par groupe, 2 minutes d'enseignement) : c'est un indice d'inversion d'expertise, utile pour ne pas animer par défaut une procédure présentée à des débutants.

## La source

| | |
| --- | --- |
| **Équipe** | School of Education, University of New South Wales (Sydney) ; auteur de la théorie de l'inversion d'expertise et de la méthode de diagnostic rapide utilisée ici ([kalyuga2003](../D_exemples_guidage/kalyuga2003.md), [kalyuga2004](../D_exemples_guidage/kalyuga2004.md), [kalyuga2007](../D_exemples_guidage/kalyuga2007.md)). |
| **Nature** | Académique ; financement et conflits d'intérêts non rapportés. |
| **Support** | *Computers in Human Behavior* (Elsevier). |
| **Audience** | 151 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Moyenne : tâches et procédure décrites (p. 855-858), matériel non publié, données non publiées. La démarche se refait ; les moyennes du tableau 1 se vérifient (gains = final − initial). |

## Ce que fait l'étude

- **Diagnostic** (p. 855-856) : test de vérification rapide de 4 tâches (graphes de y = x et y = x² à transformer) ; énoncé affiché 10 s, puis 4 étapes proposées à juger « correcte / incorrecte / je ne sais pas » ; score sur 16.
- **Répartition** (p. 857) : partage à la médiane en « novices » et « experts », puis tirage au sort dans chaque niveau : 8 novices animation, 9 novices images fixes, 8 experts animation, 8 experts images fixes.
- **Enseignement** (p. 857-858) : deux exemples résolus de transformation de y = x² (par exemple vers y = 2(x − 1)² − 3) ; animation continue d'environ une minute par exemple, ou 4 puis 5 images numérotées tirées de l'animation ; signes et coefficients en rouge, flèches et distances ; aucun texte ni narration ; même durée dans les deux conditions, 2 minutes au total.
- **Mesure** (p. 858) : nouveau test de vérification rapide, plus difficile (4 tâches à 3 ou 4 étapes) ; variable = gain (final − initial).

## Résultats

| Groupe (tableau 1, p. 859) | n | Initial /16 | Final /16 | Gain (ET) |
| --- | --- | --- | --- | --- |
| Novices, animation | 8 | 6,63 | 7,13 | 0,50 (2,51) |
| Novices, images fixes | 9 | 6,00 | 8,56 | 2,56 (1,24) |
| Experts, animation | 8 | 10,63 | 11,13 | 0,50 (3,02) |
| Experts, images fixes | 8 | 10,38 | 9,50 | −0,88 (2,53) |

- **Interaction** niveau × format : F(1, 31) = 4,25, p < 0,05 (p. 859). Pas d'effet principal du format (animation 0,50 ; images 0,94).
- **Novices** : images fixes > animation, F(1, 15) = 4,77, p < 0,05 (p. 859) ; d ≈ 1,06 [calcul : (2,56 − 0,50)/1,94, écart-type groupé de 2,51 et 1,24].
- **Experts** : animation > images fixes, non significatif, F(1, 14) = 0,97 ; d = 0,46 selon l'auteur (p. 859) [calcul : 0,50 avec l'écart-type groupé].
- **Gains négatifs** chez les experts : attribués au post-test plus difficile (p. 859).

## Avis critique

**Apport.** Une des rares études qui croise animation et niveau de connaissances sur un contenu mathématique ; elle va dans le sens de l'inversion d'expertise et nuance l'idée qu'une animation aide toujours à montrer une procédure.

**Points forts**
- Une seule variable change : mêmes images, même durée, sans texte ni voix (p. 858).
- Tirage au sort à l'intérieur de chaque niveau.
- Mesure de niveau rapide, adaptée à un usage en ligne.

**Réserves**
1. **Majeure** — Effectifs minuscules (8 ou 9 par groupe) et enseignement de 2 minutes : l'interaction est à la limite de la significativité (p < 0,05, valeur exacte non donnée) et seul l'effet chez les novices est significatif ; l'inversion complète n'est pas démontrée.
2. **Importante** — « Novices » et « experts » sont des moitiés d'un même petit groupe, surtout de lettres et sciences sociales (p. 857) : les « experts » restent à 10,5 sur 16 au prétest. Nos étudiants de L3-M2 seraient des experts pour ce contenu, mais des novices sur un contenu nouveau.
3. **Importante** — Prétest et post-test différents (post-test plus difficile) : les gains ne sont pas des progrès absolus ; la comparaison entre groupes reste valable, pas la lecture « les experts ont régressé ».
4. **Mineure** — Degrés de liberté de l'ANOVA incohérents : F(1, 31) annoncé alors qu'un plan 2 × 2 sur 33 personnes donne 29 degrés de liberté d'erreur [calcul] ; moyenne des experts « .19 » sans signe négatif dans le texte (p. 859), −0,19 d'après le tableau [calcul].
5. **Mineure** — Animation sans contrôle (ni pause ni retour) : le résultat ne dit rien d'une animation que l'étudiant peut arrêter.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Pour des novices, une procédure graphique s'apprend mieux en images fixes numérotées qu'en animation continue | C | Un essai randomisé, très petit, 2 minutes |
| Pour des étudiants avancés, l'animation devient préférable | D | Effet non significatif |
| Le format doit s'adapter au niveau | C | Interaction significative, cohérente avec l'inversion d'expertise ([kalyuga2003](../D_exemples_guidage/kalyuga2003.md)) |

**Transférabilité** : moyenne. Contenu mathématique simple, public peu scientifique ; le mécanisme (une animation rapide surcharge le débutant) se transpose, pas les valeurs.

**Pour conclure, il faudrait** proposer dans ExoForge une notion nouvelle pour nos étudiants (par exemple la construction d'un cercle de Mohr ou d'un diagramme de Bode) en images fixes numérotées ou en animation contrôlable, tirées au sort, avec un diagnostic initial et un test différé, sur au moins 30 étudiants par condition.

## Pour Forge

- **CapsuleForge** : pour une procédure graphique présentée à des débutants, suite numérotée d'images fixes annotées plutôt qu'une animation continue sans contrôle (niveau C). Cohérent avec [berney2016](berney2016.md) (représentations abstraites) ; nuancé par [ploetzner2021](ploetzner2021.md) quand c'est le détail d'un mouvement qu'il faut apprendre.
- **ExoForge** : adapter le format au niveau mesuré par un diagnostic (niveau C) ; vérification rapide d'étapes comme diagnostic possible (niveau D).
- Renvois : axe D, [kalyuga2001](../D_exemples_guidage/kalyuga2001.md), [kalyuga2004](../D_exemples_guidage/kalyuga2004.md) ; [chernikova2020](chernikova2020.md) (aides utiles aux débutants, gênantes pour les avancés).
