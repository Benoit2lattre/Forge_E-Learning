---
cle: seidel2024
reference: "Seidel, N. (2024). Short, long, and segmented learning videos: From YouTube practice to enhanced video players. Technology, Knowledge and Learning, 29, 1965-1991."
doi: 10.1007/s10758-024-09745-2
axe: [E1]
type_etude: "étude 1 descriptive (métadonnées de 83 558 vidéos YouTube Éducation en allemand et 154 370 en anglais) ; étude 2 essai randomisé en ligne, 3 variantes de lecteur x 2 vidéos, 22 participants analysés sur 38, une séance"
public: "étude 2 : étudiants en informatique et collègues de la FernUniversität in Hagen, 17 sur 22 âgés de 25 à 45 ans ; vidéos sur le changement climatique"
lecture: texte complet, 09/11/2026
regles:
  - outil: CapsuleForge
    regle: "une capsule de plus de 10 min est découpée en chapitres de 6 à 10 min : titre de chapitre, transition courte (1-2 s) avec le titre, marqueurs de chapitre sur la barre de progression et sommaire cliquable"
    niveau: C
    transferabilite: moyenne
    note: "gain 7,43 contre 5,29 sur 10, d ≈ 1,6 [calcul], mais 7 participants par groupe ; concordant avec rey2019"
  - outil: CapsuleForge
    regle: "à contenu égal, préférer une capsule chapitrée dans un seul lecteur à une coupe en vidéos séparées si l'on veut laisser l'étudiant naviguer"
    niveau: D
    transferabilite: moyenne
    note: "variante sommaire + marqueurs : seule différence significative contre la vidéo d'un bloc ; vidéos séparées non significatives (p = 0,18)"
  - outil: CapsuleForge
    regle: "ne pas compter sur le bouton pause pour découper : placer les arrêts dans la capsule elle-même (fin de chapitre, question)"
    niveau: D
    transferabilite: moyenne
    note: "3 participants sur 22 ont utilisé la pause, une fois chacun ; observation, pas de comparaison"
---

# Vidéos longues, courtes et segmentées (Seidel, 2024)

Seidel, N. (2024). Short, long, and segmented learning videos: From YouTube practice to enhanced video players. *Technology, Knowledge and Learning*, 29, 1965-1991. [DOI](https://doi.org/10.1007/s10758-024-09745-2)

**En une phrase.** Sur YouTube Éducation, deux tiers des vidéos durent moins de 14 min (allemand) ou 23 min (anglais) et 8 à 21 % font partie d'une série découpée ; dans un petit essai en ligne (22 participants), la même vidéo de 50 à 66 min apprend davantage quand le lecteur affiche des chapitres titrés, des marqueurs et un sommaire cliquable : pour CapsuleForge, un argument (fragile) pour chapitrer les capsules longues plutôt que de les raccourcir à tout prix.

## La source

| | |
| --- | --- |
| **Équipe** | CATALPA (centre de recherche sur l'apprentissage assisté par la technologie et l'analyse prédictive), FernUniversität in Hagen ; auteur unique, qui conçoit et évalue son propre lecteur vidéo. |
| **Nature** | Académique ; soutien du CATALPA, libre accès financé par Projekt DEAL ; pas de conflit d'intérêts déclaré (p. 1989). |
| **Support** | *Technology, Knowledge and Learning* (Springer), libre accès. |
| **Audience** | 35 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Bonne pour l'étude 1 (scripts et jeux de données publiés, p. 1970) ; moyenne pour l'étude 2 : données et scripts d'analyse publiés (p. 1981), mais questions du test et découpage des vidéos non décrits. La démarche se refait ; les chiffres ne se vérifient pas tous (voir réserves). |

## Ce que fait l'étude

- **Étude 1** (p. 1969-1977) : métadonnées des chaînes classées « Éducation » (via channelcrawler.com) : toutes les chaînes en allemand, environ 1 % des chaînes en anglais ; regroupement par k-moyennes sur la durée ; repérage des séries par expressions régulières sur les titres (« partie », « épisode », numéros).
- **Étude 2, dispositif** (p. 1978-1981) : lecteur vidéo web à trois variantes : (1) vidéo d'un bloc, lecteur standard ; (2) même fichier découpé en 5 ou 6 chapitres de 6 à 10 min, transition (écran noir 1-2 s et titre), marqueurs sur la barre de progression, sommaire cliquable ; (3) chapitres en vidéos séparées, vignettes et bouton « Continuer » (tableau 5, p. 1982). Deux vidéos réelles : conférence (66 min) et documentaire télévisé (50 min).
- **Participants** (p. 1978-1979) : invitation à environ 100-150 personnes ; 38 commencent, 22 analysés (exclusions : abandons, moins de 10 % de la vidéo vue) ; 7, 7 et 8 par variante (tableau 4).
- **Mesures** (p. 1981) : prétest de 10 QCM (avec option « je ne sais pas »), même test après la vidéo ; gain = différence ; structuration perçue ; traces de navigation.

## Résultats

- **Étude 1** (tableau 3, p. 1975) : trois groupes de durée ; vidéos courtes jusqu'à 14,2 min (allemand) et 22,6 min (anglais), environ deux tiers du corpus ; part des vidéos en série : 8,9 % et 8,1 % (courtes), 21,2 % et 14,5 % (moyennes), 18,6 % et 13,9 % (longues). Corrélation durée-vues quasi nulle (r = 0,074 et −0,010, p. 1972).

| Étude 2, sur 10 (tableau 6, p. 1983) | n | Prétest | Post-test | Gain |
| --- | --- | --- | --- | --- |
| 1 — vidéo d'un bloc | 7 | 1,29 (1,11) | 6,57 (1,62) | 5,29 (1,49) |
| 2 — chapitres, marqueurs, sommaire | 7 | 1,00 (1,41) | 8,43 (0,98) | 7,43 (1,13) |
| 3 — vidéos séparées | 8 | 1,00 (0,93) | 7,60 (1,85) | 6,63 (2,13) |

- **Comparaisons** (p. 1983) : variante 2 contre 1, Kruskal-Wallis χ²(1) = 5,58, p = 0,018, soit d ≈ 1,6 sur le gain [calcul : (7,43 − 5,29) / 1,32] ; variante 3 contre 1, χ²(1) = 1,81, p = 0,18 (d ≈ 0,7 [calcul]).
- **Usage du lecteur** (p. 1984-1986) : pause utilisée par 3 participants sur 22, une fois chacun ; 14 sur 22 sautent dans la vidéo (34 sauts en avant sur 42) ; en variante 2, le sommaire est utilisé par la plupart ; en variante 3, tous suivent l'ordre imposé.
- **Structuration perçue** (p. 1985) : les deux variantes découpées sont jugées en moyenne 23 % mieux structurées.

## Avis critique

**Apport.** Montre qu'un découpage « signalé » dans un seul lecteur (chapitres titrés, marqueurs, sommaire), sans pause imposée, peut suffire à obtenir l'effet de segmentation ; c'est exactement ce que H5P et ActivePresenter permettent sans couper le fichier.

**Points forts**
- Même fichier vidéo dans les trois variantes : seule la présentation change.
- Vidéos réelles et longues, en ligne, sans surveillance ; données et scripts publiés.
- L'étude 1 donne un ordre de grandeur des durées réellement pratiquées.

**Réserves**
1. **Majeure** — 7 à 8 participants par variante après 42 % de pertes (22 sur 38), non réparties au hasard (les 4 exclusions pour visionnage insuffisant sont toutes en conférence) ; l'effet de d ≈ 1,6 est très imprécis.
2. **Importante** — Incohérences de rapport : la variante 2 vaut 8,43 au post-test et 7,43 de gain (tableau 6) mais « M = 7,25 » plus loin (p. 1986) ; le groupe 2 compte 7 personnes (tableau 4) mais « 8 » puis « 10 » participants (p. 1985-1986) ; 895 ou 824 chaînes en allemand (résumé contre tableaux 1-2) ; « environ 45 min » de vidéo pour des vidéos de 50 et 66 min.
3. **Importante** — Le test est un QCM de 10 questions identique avant et après (effet de test), en mesure immédiate seulement, avec un plafond proche (8,43 sur 10 en variante 2).
4. **Importante** — Conclusion d'équivalence entre variantes 2 et 3 (H3) tirée d'une différence non testée sur 15 personnes.
5. **Mineure** — Public d'informaticiens et de collègues de l'auteur, contenu de culture générale.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Chapitrer une vidéo longue (titres, marqueurs, sommaire) améliore l'apprentissage | C | Tirage au sort, même fichier, mais 7 par groupe ; concordant avec rey2019 |
| Vidéos séparées aussi efficaces que les chapitres | D | Non testé statistiquement, très petit effectif |
| La durée totale compte moins que le découpage | D | Interprétation de l'auteur |
| Durées pratiquées sur YouTube Éducation | B | Description exhaustive (allemand), vérifiable |

**Transférabilité** : moyenne. Le dispositif (chapitres dans un lecteur) se transpose directement à CapsuleForge ; la valeur de l'effet, non.

**Pour conclure, il faudrait** publier une même capsule de mécanique de 20 à 30 min sous Moodle en deux versions tirées au sort (chapitrée avec sommaire H5P, ou d'un bloc), avec un test de transfert différé et les traces de navigation.

## Pour Forge

- **CapsuleForge** : au-delà de 10 min, chapitres de 6 à 10 min avec titres, transition courte, marqueurs sur la barre et sommaire cliquable (niveau C).
- **CapsuleForge** : pour laisser naviguer, préférer les chapitres dans un seul lecteur aux vidéos séparées (niveau D).
- **CapsuleForge** : ne pas compter sur la pause ; placer les arrêts dans la capsule (niveau D).
- Renvois : [rey2019](rey2019.md) (méta-analyse de la segmentation), [fyfield2022](fyfield2022.md) (brièveté et contrôle de la lecture), [yu2023](yu2023.md) (sommaire et barre de progression), [biard2018](biard2018.md) (bouton pause peu utilisé).
