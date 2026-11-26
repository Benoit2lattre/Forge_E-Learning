---
cle: fleur2023b
reference: "Fleur, D. S., Marshall, M., Pieters, M., Brouwer, N., Oomens, G., Konstantinidis, A., Winnips, K., Moes, S., van den Bos, W., Bredeweg, B. et van Vliet, E. A. (2023). IguideME: Supporting self-regulated learning and academic achievement with personalized peer-comparison feedback in higher education. Journal of Learning Analytics, 10(2), 100-114."
doi: 10.18608/jla.2023.7853
axe: [G1]
type_etude: essai randomisé individuel (31 contre 31), accès au tableau de bord IguideME contre aucun accès, un cours de 8 semaines ; questionnaires en début et fin de cours (41 répondants complets)
public: étudiants de 3e année de licence, cours optionnel de l'université d'Amsterdam (questions d'examen sur hormones et maladies), 80 % de femmes
lecture: "texte complet, 09/11/2026"
regles:
  - outil: DiagForge
    regle: "accompagner chaque écart affiché par rapport aux pairs d'un message court orienté vers l'action (« vous rattrapez l'écart sur… », « à travailler : … ») plutôt que d'un chiffre seul, et ne pas afficher de message quand l'écart est trop grand pour être comblé"
    niveau: D
    transferabilite: moyenne
  - outil: DiagForge
    regle: "pour évaluer une forme de restitution, comparer l'évolution entre début et fin de période dans les deux groupes, pas seulement l'écart final, et tenir compte du nombre de mesures comparées"
    niveau: C
    transferabilite: forte
    note: "dans cette étude, l'écart final de métacognition reproduit un écart déjà présent au départ (d = 0,63, p = 0,05)"
---

# IguideME : comparaison aux pairs de même objectif (Fleur et al., 2023b)

Fleur, D. S., Marshall, M., Pieters, M., Brouwer, N., Oomens, G., Konstantinidis, A., Winnips, K., Moes, S., van den Bos, W., Bredeweg, B. et van Vliet, E. A. (2023). IguideME: Supporting self-regulated learning and academic achievement with personalized peer-comparison feedback in higher education. *Journal of Learning Analytics*, 10(2), 100-114. [DOI](https://doi.org/10.18608/jla.2023.7853)

**En une phrase.** Dans un cours de 62 étudiants de 3e année, l'accès à un tableau de bord qui compare l'étudiant à 10 à 12 camarades de même objectif de note s'accompagne de scores de fin de cours plus élevés en métacognition et en apprentissage entre pairs, de meilleures annotations de lecture et d'une meilleure note aux 3 questions d'examen de haut niveau, mais pas d'une meilleure note finale ; les tableaux annexes montrent que l'écart de métacognition existait déjà au départ, ce qui retire l'essentiel de la preuve d'un effet sur l'autorégulation.

## La source

| | |
| --- | --- |
| **Équipe** | Faculté des sciences de l'université d'Amsterdam (informatique, neurosciences, centre pédagogique), universités de Groningue et VU Amsterdam ; même groupe que [fleur2023](fleur2023.md) (Fleur, van den Bos, Bredeweg), avec un autre tableau de bord. |
| **Nature** | Académique ; financement du ministère néerlandais de l'Éducation via SURF (projet Feedback GO) et bourse doctorale de l'université d'Amsterdam ; aucun conflit déclaré (p. 111). Les auteurs ont conçu le tableau de bord et enseignent le cours. |
| **Support** | *Journal of Learning Analytics* (SoLAR), libre accès. |
| **Audience** | 17 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Bonne : logiciel libre (GitHub, p. 103), données anonymisées et scripts sur OSF (p. 106), tableaux complets en annexe (p. 110-111). Les chiffres se vérifient, la démarche se refait. |

## Ce que fait l'étude

- **Tableau de bord** (p. 103-104) : vue « radar » et vue « grille » de toutes les activités (présence, temps d'étude, quiz formatifs et sommatifs, lectures annotées sur Perusall), comparées à un groupe de 10 à 12 camarades ayant déclaré le même objectif de note à la première ouverture ; groupe formé sans manipulation (p. 102). Messages automatiques : « vous dépassez vos pairs » (un point au-dessus), « vous rattrapez l'écart » (un demi-point en dessous), « il faut fournir plus d'effort » (un point en dessous), l'idée étant de taire les comparaisons trop défavorables (p. 104). Prédiction de la note finale par régression (p. 104). Usage libre, sans rappel (p. 103).
- **Plan** (p. 105) : 62 étudiants tirés au sort individuellement (31 accès, 31 sans accès), moyenne antérieure comparable ; 4 abandons ; 41 questionnaires complets (23 contre 18).
- **Mesures** (p. 105-106) : 9 composantes du MSLQ et 6 buts d'accomplissement (AGQ) en début et fin de cours ; notes des 14 lectures annotées (6 notées, 8 non notées) ; examen final découpé en 17 questions « de bas niveau » et 3 « de haut niveau » selon Bloom ; note finale ; avis libre.
- **Analyse** (p. 106) : t de Student ou Kruskal-Wallis groupe contre groupe, seuil 0,05, sans correction pour le nombre de comparaisons.

## Résultats

| Mesure (fin de cours) | Accès | Sans accès | p ; d | Début de cours (p ; d) |
| --- | --- | --- | --- | --- |
| Autorégulation métacognitive (MSLQ) | 4,98 | 4,50 | 0,03 ; 0,70 | 4,76 contre 4,31 (0,05 ; 0,63) |
| Apprentissage entre pairs (MSLQ) | 4,01 | 3,09 | 0,02 ; 0,75 | 4,12 contre 3,61 (0,18 ; 0,42) |
| But « faire mieux que les autres » (AGQ) | 4,58 | 3,54 | 0,04 ; 0,71 | 4,55 contre 4,04 (0,28 ; 0,35) |
| Questions d'examen de haut niveau (sur 10) | 7,92 | 6,79 | 0,03 | — |
| Questions d'examen de bas niveau | 6,43 | 6,65 | 0,55 ; −0,16 | — |

Sources : tableaux annexes 1, 4 et 5 (p. 110-111) ; texte p. 106-107.

- **Évolution dans chaque groupe** (tableau annexe 3, p. 111) : l'autorégulation métacognitive monte autant dans les deux groupes (+0,22, d = 0,35 avec accès ; +0,19, d = 0,37 sans accès, aucune des deux significative) ; l'écart « apprentissage entre pairs » et l'écart « faire mieux que les autres » viennent d'une baisse dans le groupe sans accès (p = 0,03 et 0,09), pas d'une hausse avec accès.
- **Lectures annotées** (p. 107, tableau annexe 5) : 3 lectures sur 14 différent à p < 0,05 [décompte] ; 69 % des étudiants avec accès font les lectures contre 54 %.
- **Note finale et examens partiels** : pas de différence (p. 107).
- **Avis libres** (tableau 1, p. 108) : 12 étudiants sur 23 répondants aiment la comparaison aux pairs ; 1 la trouve démotivante.
- **Conclusion des auteurs** (p. 108) : les données « soutiennent l'hypothèse » que la comparaison personnalisée améliore l'autorégulation et la réussite ; ils reconnaissent ne pas pouvoir attribuer l'effet à la comparaison plutôt qu'à la prédiction de note ou au suivi de progression (p. 109).

## Avis critique

**Apport.** Un tableau de bord libre et documenté, qui forme les groupes de pairs de façon transparente (même objectif de note, sans tri caché, contrairement à [fleur2023](fleur2023.md)) et cadre chaque écart par un message court. C'est un modèle de conception intéressant pour DiagForge ; ce n'est pas une preuve d'effet.

**Points forts**
- Tirage au sort individuel en cours réel ; données et code ouverts.
- Mesures avant et après publiées, ce qui permet de vérifier les conclusions.
- Distinction des questions d'examen par niveau de Bloom.

**Réserves**
1. **Majeure** — L'effet annoncé sur l'autorégulation métacognitive n'en est pas un : l'écart existait au départ (d = 0,63, p = 0,05) et l'évolution est la même dans les deux groupes (tableaux annexes 1 et 3) ; le texte affirme pourtant que les groupes « ne différaient pas » au départ (p. 106). Les deux autres écarts viennent d'une baisse chez les témoins.
2. **Importante** — Très nombreuses comparaisons (15 échelles, 14 lectures, 2 niveaux d'examen, note finale) sans correction ; les résultats significatifs sont peu nombreux et proches de 0,05. Questionnaires sur 41 étudiants seulement (perte de 34 %).
3. **Importante** — Le gain aux questions de haut niveau repose sur 3 questions ; la note finale ne bouge pas.
4. **Mineure** — Tableau de bord composite (comparaison, prédiction, suivi des activités, messages) : impossible d'isoler la part de la comparaison, ce que les auteurs reconnaissent (p. 109). Le groupe témoin n'a aucun retour.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| IguideME améliore l'autorégulation métacognitive | D | Écart présent avant l'intervention, évolution identique dans les deux groupes |
| IguideME améliore les réponses aux questions de haut niveau | C | Un petit essai, 3 questions, comparaisons multiples |
| IguideME améliore la note finale | — | Non observé (pas de différence) |
| La comparaison aux pairs de même objectif est appréciée | C | Avis libres de 23 étudiants |

**Transférabilité** : moyenne. Étudiants de 3e année proches de nos L3, mais cours de sciences de la vie avec lectures annotées, et tableau de bord bien plus riche qu'un rapport de quiz.

**Pour conclure, il faudrait** tirer au sort, dans un même cours, « rapport DiagForge avec critère seul » contre « critère + pairs de même objectif annoncé », mesurer la métacognition (ou mieux, l'exactitude de l'auto-évaluation avant le quiz) avant et après, et comparer les gains, avec une correction pour les comparaisons multiples.

## Pour Forge

- **DiagForge** : si une comparaison aux pairs est affichée, la former de façon transparente (objectif déclaré, niveau proche) et la cadrer par un message orienté vers l'action ; taire les écarts trop grands (niveau D, idée de conception non testée isolément).
- **DiagForge** : évaluer toute forme de restitution sur des gains avant/après, pas sur un écart final (niveau C).
- Cette fiche **nuance** l'apport attribué jusqu'ici à Fleur et al. (2023b) (« autorégulation améliorée ») : il n'est pas établi. Elle ne contredit donc pas [fleur2023](fleur2023.md), qui ne trouvait pas d'effet sur la métacognition.
