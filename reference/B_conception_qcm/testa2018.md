---
cle: testa2018
reference: "Testa, S., Toscano, A. et Rosato, R. (2018). Distractor efficiency in an item pool for a statistics classroom exam: Assessing its relation with item cognitive level classified according to Bloom's taxonomy. Frontiers in Psychology, 9, article 1585."
doi: 10.3389/fpsyg.2018.01585
axe: [B2]
type_etude: étude corrélationnelle sur une banque d'items d'examen (analyse secondaire de copies archivées)
public: 848 étudiants de licence de psychologie (université de Turin), examen de statistique, 2012-2015
lecture: texte complet, 10/11/2026
regles:
  - outil: DiagForge
    regle: "déclarer un leurre fonctionnel s'il est choisi par au moins 5 % des étudiants et si ceux qui le choisissent ont un score moyen inférieur à ceux qui choisissent la bonne réponse (discrimination d'Attali et Fraenkel)"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "lire le taux de leurres fonctionnels d'une question avec sa réussite : une question facile a mécaniquement peu de leurres choisis ; comparer des questions de réussite voisine"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "questions de calcul : construire les leurres numériques en refaisant le calcul avec les données de l'énoncé et une opération ou une formule voisine fausse"
    niveau: C
    transferabilite: forte
    note: "les questions d'application ont plus de leurres fonctionnels en analyse simple (84 % contre 69 %), lien non significatif après ajustement sur la difficulté"
  - outil: QuizForge
    regle: "adapter le nombre d'options à la question : pour une question de connaissance, préférer 3 ou 4 options plutôt que des leurres de remplissage"
    niveau: D
    transferabilite: moyenne
    note: "interprétation des auteurs (p. 6) ; avec 5 options plutôt que 4, moins de questions ont plus de la moitié de leurres fonctionnels (rapport de cotes 0,14)"
---

# Efficacité des leurres selon le niveau cognitif des questions (Testa et al., 2018)

Testa, S., Toscano, A. et Rosato, R. (2018). Distractor efficiency in an item pool for a statistics classroom exam: Assessing its relation with item cognitive level classified according to Bloom's taxonomy. *Frontiers in Psychology*, 9, article 1585. [DOI](https://doi.org/10.3389/fpsyg.2018.01585)

**En une phrase.** Dans une banque de 164 QCM de statistique passés par 848 étudiants, environ 70 % des leurres fonctionnent ; les questions d'application (calcul) en ont davantage que les questions de connaissance (84 % contre 69 % avec l'indice d'Attali et Fraenkel), mais ce lien disparaît une fois tenu compte de la difficulté, plus forte pour les questions d'application.

## La source

| | |
| --- | --- |
| **Équipe** | Département de psychologie, université de Turin (méthodes quantitatives, psychométrie) ; une auteure aussi à l'unité INSERM 1246 SPHERE (Nantes, Tours) (p. 1). Deux auteures ont relu et révisé la banque d'items qu'elles analysent (p. 3). |
| **Nature** | Académique ; financement non rapporté ; pas de conflit d'intérêts déclaré (p. 8). Analyse secondaire de copies anonymes, sans avis éthique demandé (p. 7). |
| **Support** | *Frontiers in Psychology*, section mesure, libre accès. |
| **Audience** | 43 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Moyenne : définitions et formules des indices (p. 4), trois exemples d'items (annexe 1, p. 9) ; banque d'items et données non publiées. La démarche se refait sur une banque de quiz ; les chiffres ne se vérifient pas. |

## Ce que fait l'étude

- **Banque et passation** (p. 3) : 174 QCM de statistique écrits par des enseignants en 2012 ; chaque étudiant reçoit 30 items tirés au hasard par ordinateur ; chaque item est vu par 120 à 185 étudiants (moyenne 145) ; barème 1/0 sans pénalité ; score moyen 16,0 sur 30.
- **Items analysés** (p. 3) : 164 items (10 modifiés en cours d'étude exclus), 635 leurres ; 143 items à 5 options, 21 à 4 ; « aucune de ces réponses » dans 42 items.
- **Niveau cognitif** (p. 3-4) : classement en Connaissance (84 items), Compréhension (34), Application (46) par deux auteures (kappa 0,67), désaccords tranchés par consensus.
- **Leurre fonctionnel** (p. 4) : choisi par au moins 5 % des étudiants et discrimination négative, mesurée de deux façons : point-bisériale classique (contre tous les autres étudiants) et indice d'Attali et Fraenkel (contre ceux qui ont la bonne réponse seulement). Par item : DE1 et DE2 = part de leurres fonctionnels ; versions binaires (plus de la moitié fonctionnels ou non).
- **Analyses** (p. 4) : modèle de Rasch pour la qualité de la banque ; khi-deux et analyses de variance ; régressions logistiques avec difficulté, discrimination, contenu, nombre d'options et « aucune de ces réponses » comme variables de contrôle.

## Résultats

- **Qualité de la banque** (p. 5) : fiabilité de Rasch 0,76 ; 40,2 % des items avec une discrimination ≥ 0,40, 21 items (12,8 %) sous 0,20 ; réussite moyenne 54,8 %, 68,9 % des items entre 30 et 70 %.
- **Leurres** (tableau 2, p. 5) :

| Critère | Leurres (sur 635) |
| --- | --- |
| Choisi par au moins 5 % | 474 (74,6 %) |
| Point-bisériale négative | 561 (88,3 %) |
| Indice d'Attali et Fraenkel négatif | 605 (95,3 %) |
| Fonctionnel, point-bisériale | 435 (68,5 %) |
| Fonctionnel, Attali et Fraenkel | 465 (73,2 %) |

- **Selon le niveau cognitif** (tableau 3, p. 6) :

| | Connaissance (84) | Compréhension (34) | Application (46) | p |
| --- | --- | --- | --- | --- |
| Réussite moyenne | 57,1 % | 59,9 % | 46,8 % | 0,002 |
| Part de leurres fonctionnels (point-bisériale) | 64,9 % | 65,0 % | 77,0 % | 0,013 |
| Part de leurres fonctionnels (Attali et Fraenkel) | 69,1 % | 68,1 % | 84,4 % | 0,001 |
| Items avec plus de la moitié de leurres fonctionnels (Attali et Fraenkel) | 64,3 % | 61,8 % | 89,1 % | < 0,005 |

  Tailles d'effet faibles : η² = 0,013 et 0,024 ; phi = 0,18 et 0,25 (p. 5). La discrimination des items ne dépend pas du niveau cognitif (0,35 à 0,36, p = 0,891).
- **Régressions** (tableau 4, p. 6) : la difficulté et la discrimination de l'item prédisent l'efficacité des leurres ; le niveau « application » n'est plus significatif (rapport de cotes 1,71, p = 0,261 ; 2,93, p = 0,079). Sans la variable « réussite », il le redevient (2,50, p < 0,05 ; 5,15, p < 0,01 ; résultats non montrés, p. 5). Chaque point de réussite en plus multiplie la cote par 0,93 (indice d'Attali et Fraenkel), soit environ 0,48 pour 10 points [calcul : 0,93¹⁰]. Avec 5 options plutôt que 4, rapport de cotes 0,14 (p = 0,011) pour l'indice d'Attali et Fraenkel, 0,33 (p = 0,071) pour la point-bisériale.
- **Choix de l'indice** (p. 5, 7) : l'indice d'Attali et Fraenkel retient plus de leurres et le modèle explique davantage (R² de Nagelkerke 0,41 contre 0,28).
- **Exemple d'item d'application** (annexe 1, p. 9) : « 40 personnes, moyenne 179,3 cm, variance 129,7 ; calculer la somme des carrés » ; clé 5188 ; les leurres sont des calculs faux avec les données : 7172 = 40 × 179,3 (somme des valeurs), 3,24 = 129,7 / 40, −49,6 = 129,7 − 179,3, 1,38 = 179,3 / 129,7 [calcul].

## Avis critique

**Apport.** Valeurs de référence pour une banque d'items de statistique à l'université (environ 70 % de leurres fonctionnels avec 5 options) et argument empirique pour l'indice d'Attali et Fraenkel ; indice, non démontré, que les questions de calcul se prêtent mieux à des leurres efficaces.

**Points forts**
- Banque réelle, tirage aléatoire des items pour chaque étudiant, effectif total élevé (848).
- Deux indices de discrimination comparés sur les mêmes données.
- Analyse ajustée qui montre honnêtement la confusion entre niveau cognitif et difficulté.

**Réserves**
1. **Majeure** — Étude corrélationnelle : le niveau cognitif est confondu avec la difficulté (les questions d'application sont plus difficiles, donc plus d'étudiants se trompent et choisissent les leurres). Après ajustement, le lien n'est plus significatif (tableau 4). L'affirmation « les questions d'application ont de meilleurs leurres » reste au niveau C au mieux.
2. **Importante** — L'effet du nombre d'options est en partie mécanique : avec 4 leurres plutôt que 3, il est plus difficile d'en avoir plus de la moitié choisis par au moins 5 % ; ce n'est pas une mesure propre de la qualité des leurres.
3. **Importante** — Environ 145 étudiants par item (p. 7) : discrimination de chaque leurre instable ; les auteures le reconnaissent.
4. **Mineure** — Incohérence : le texte annonce 68,3 % et 73,2 % d'items avec plus de la moitié de leurres fonctionnels (p. 5), le tableau 3 donne 103 / 164 = 62,8 % et 116 / 164 = 70,7 % [décompte] ; le même passage parle d'« items » pour une part de leurres (73,2 %).
5. **Mineure** — Étudiants de psychologie (78 % de femmes) dans un cours de statistique de service ; une seule université ; Bloom limité aux trois premiers niveaux.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Environ 70 % de leurres fonctionnels dans une banque soignée à 5 options | C | Une banque, description |
| L'indice d'Attali et Fraenkel est préférable à la point-bisériale | C | Argument de méthode et meilleur ajustement, sans critère externe ; convergent avec attali2000 |
| Les questions d'application ont plus de leurres fonctionnels | C | Lien bivarié, confondu avec la difficulté |
| Réduire les options pour les questions de connaissance | D | Interprétation des auteures (p. 6) |

**Transférabilité** : forte pour les indicateurs (quiz en ligne à l'université, statistique proche des mathématiques) ; moyenne pour les valeurs (5 options, étudiants non scientifiques).

**Pour conclure, il faudrait** tirer au sort, dans QuizForge, des versions à 3 et à 5 options de mêmes questions de connaissance et de calcul, et comparer dans DiagForge le taux de leurres fonctionnels et la discrimination à réussite égale.

## Pour Forge

- **DiagForge** : leurre fonctionnel = choisi par au moins 5 % (ou seuil ajusté à la réussite, voir [raymond2018](../C_analyse_items/raymond2018.md)) et score moyen de ceux qui le choisissent inférieur à celui des étudiants qui ont la bonne réponse ([attali2000](../C_analyse_items/attali2000.md)) (niveau C).
- **DiagForge** : afficher le taux de leurres fonctionnels avec la réussite de la question ; ne pas pénaliser une question facile (niveau C).
- **QuizForge** : leurres numériques obtenus en refaisant le calcul avec les données de l'énoncé et une opération fausse (exemple de la somme des carrés, p. 9) (niveau C).
- **QuizForge** : moins d'options pour les questions de connaissance, plutôt que des leurres de remplissage (niveau D).
- Renvois : [gierl2017](../C_analyse_items/gierl2017.md), [sridharan2025](../C_analyse_items/sridharan2025.md) (nombre d'options), [hingorjo2012](../C_analyse_items/hingorjo2012.md) (seuil de 5 %), [slepkov2021](../C_analyse_items/slepkov2021.md) (valeurs de référence).
