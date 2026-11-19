---
cle: martinblas2010
reference: "Martín-Blas, T., Seidel, L. et Serrano-Fernández, A. (2010). Enhancing Force Concept Inventory diagnostics to identify dominant misconceptions in first-year engineering physics. European Journal of Engineering Education, 35(6), 597-606."
doi: 10.1080/03043797.2010.497552
axe: [H2]
type_etude: étude descriptive (une passation du Force Concept Inventory en début d'année, deux groupes)
public: entrants en 1re année de deux écoles d'ingénieurs de l'Universidad Politécnica de Madrid (110 et 33 étudiants), cours de physique préparatoire facultatif
lecture: texte complet, 10/11/2026
regles:
  - outil: DiagForge
    regle: "pour chaque question, calculer la part de la réponse fausse dominante parmi les seules réponses fausses (en regroupant les leurres qui relèvent de la même erreur type) et la signaler au-dessus de 50 %"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "regrouper les questions par erreur type déclenchant la réponse fausse dominante, et comparer les groupes ou promotions sur ce profil d'erreurs, pas seulement sur le score"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "mécanique du point : leurres « force nette parallèle à la vitesse », « dans une paire action-réaction, le plus lourd ou celui qui bouge exerce la plus grande force », « durée de chute dépendant de la masse », « confusion position, vitesse, accélération »"
    niveau: C
    transferabilite: forte
---

# Réponses fausses dominantes au Force Concept Inventory (Martín-Blas et al., 2010)

Martín-Blas, T., Seidel, L. et Serrano-Fernández, A. (2010). Enhancing Force Concept Inventory diagnostics to identify dominant misconceptions in first-year engineering physics. *European Journal of Engineering Education*, 35(6), 597-606. [DOI](https://doi.org/10.1080/03043797.2010.497552)

**En une phrase.** Au Force Concept Inventory (FCI) passé le premier jour par deux groupes d'entrants très différents (53 % et 32 % de réussite), 24 questions sur 30 ont une réponse fausse dominante, et ce sont les mêmes erreurs types dans les deux groupes ; pour DiagForge, la mesure proposée (part de la réponse fausse dominante parmi les réponses fausses) est simple à calculer et à lire.

## La source

| | |
| --- | --- |
| **Équipe** | Enseignants de physique de 1re année, Universidad Politécnica de Madrid (EUIT Forestal ; ETSI Industriales) ; groupe de recherche en enseignement de l'ingénierie (p. 597, 606). |
| **Nature** | Académique ; financement non rapporté. Les auteurs enseignent dans les écoles étudiées. |
| **Support** | *European Journal of Engineering Education* (SEFI, Taylor & Francis). |
| **Audience** | 68 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Bonne pour le calcul : tableau 1 complet (bonnes réponses, réponse fausse dominante, part normalisée) ; FCI disponible pour les enseignants. Les codes de regroupement des leurres d'une même erreur ne sont pas détaillés question par question. |

## Ce que fait l'étude

- **Public** (p. 599-600) : septembre 2009, cours préparatoire facultatif avant la rentrée ; ETSII (110 étudiants, admission sur note minimale de 8/10, physique au lycée pour tous) et EUITF (33 étudiants, sans condition de note, parcours hétérogènes).
- **Passation** (p. 600) : FCI version 1995 en espagnol, 30 questions, 30 minutes, le premier jour ; consigne d'éviter de répondre au hasard. Pas de post-test.
- **Analyse** (p. 602) : une réponse fausse est « dominante » si elle représente plus de 50 % des réponses fausses à la question ; les leurres relevant de la même erreur type sont additionnés. Comparaison avec l'analyse de concentration de Bao et Redish (p. 602-605).

## Résultats

- **Scores** (p. 600) : 53 % de bonnes réponses en moyenne à l'ETSII, 32 % à l'EUITF ; seules les questions 3 et 7 sont réussies par plus de 70 % des deux groupes.
- **Réponses fausses dominantes** (p. 602, tableau 1 p. 603) : 24 questions sur 30, regroupées en 9 erreurs types (tableau 2). Les plus présentes :
  - **force nette parallèle à la vitesse** : 8 questions ; réussite de 25 % à 40 % à l'ETSII (77 % pour Q27) et de 3 % à 21 % à l'EUITF (70 % pour Q27) ; la réponse dominante regroupe 70 % à 96 % des réponses fausses (65 % pour Q27 à l'ETSII) ;
  - **paire action-réaction inégale** (le plus massif ou celui qui bouge exerce la plus grande force) : 4 questions ; Q4 : 45 % et 18 % de réussite, 95 % et 96 % des réponses fausses sur le même leurre ;
  - durée de chute dépendant de la masse (3 questions), confusion position, vitesse, accélération (2), impetus (2), trajectoire courbe sans force (2), composition non vectorielle des vitesses, référentiel égocentré, gravité constante sans accélération constante (1 chacune).
- **Accord entre les deux groupes** (figure 4, p. 604) : décrit comme une « corrélation remarquable », sans coefficient. [calcul] r = 0,77 entre les parts normalisées des deux groupes sur les 24 questions du tableau 1.
- **Concentration** (p. 604-605) : conclusions semblables, mais l'indice de Bao et Redish sous-estime une erreur répartie sur plusieurs leurres : Q5 a 92 % et 95 % de réponses fausses dominantes une fois les leurres équivalents regroupés, pour un indice de 0,08 et 0,20.

## Avis critique

**Apport.** Un indicateur lisible pour un enseignant (part de la réponse fausse dominante, leurres regroupés par erreur type) et la constatation que deux groupes de niveaux très différents se trompent de la même façon : un catalogue d'erreurs types peut servir à plusieurs promotions.

**Points forts**
- Tableau 1 complet, qui permet de refaire les calculs.
- Regroupement des leurres par erreur plutôt que par option, avec un exemple (Q5) où cela change la conclusion.
- Deux publics contrastés dans la même université.

**Réserves**
1. **Importante** — Petits effectifs (33 étudiants à l'EUITF) : avec 3 % de réussite, une part normalisée repose sur une trentaine de réponses ; aucun intervalle, aucun test pour l'accord entre groupes.
2. **Importante** — Une seule passation, avant tout enseignement, chez des volontaires d'un cours préparatoire : rien sur la persistance de ces erreurs après le cours ni sur un public plus avancé.
3. **Mineure** — Le seuil de 50 % n'est pas appliqué strictement : certaines lignes du tableau 1 sont sous 50 % dans un groupe (Q19 : 44 % à l'ETSII ; Q22 : 44 % à l'EUITF), sans explication.
4. **Mineure** — La conclusion « les étudiants n'ont que quelques erreurs bien identifiées » et la généralisation à « tout cours de physique » (p. 605) vont au-delà de deux groupes d'une université.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| La plupart des questions du FCI ont une réponse fausse dominante | C | Une passation, 143 étudiants, chiffres vérifiables |
| Les erreurs dominantes sont les mêmes dans deux groupes de niveaux différents | C | Accord net (r = 0,77 [calcul]) mais petits effectifs, une université |
| Regrouper les leurres d'une même erreur change le diagnostic | B | Propriété du calcul, montrée sur Q5 |

**Transférabilité** : moyenne à forte. Mécanique du point d'entrée en école ; nos L3 ont dépassé ce niveau, mais `poutot2015` retrouve les mêmes erreurs après le cours en école d'ingénieurs française.

**Pour conclure, il faudrait** calculer dans DiagForge la part de la réponse fausse dominante sur nos quiz de mécanique, en début et en fin de module, et comparer les profils d'erreurs de deux promotions.

## Pour Forge

- **DiagForge** : indicateur « réponse fausse dominante » par question = part du leurre le plus choisi parmi les réponses fausses, leurres d'une même erreur type additionnés ; alerte au-dessus de 50 % (niveau C). Complète l'alerte « leurre égal ou supérieur à la bonne réponse » de `steif2006`.
- **DiagForge** : regrouper les questions par erreur type et comparer les promotions sur ce profil (niveau C).
- **QuizForge** : leurres de mécanique du point : force parallèle à la vitesse, action-réaction inégale, durée de chute fonction de la masse, confusion position-vitesse-accélération (niveau C). Nécessite dans la banque le lien leurre -> erreur type (règle de l'axe).
- Renvois : `poutot2015` (mêmes erreurs au FCI en école d'ingénieurs française) ; `steif2006` (leurres dominants en statique) ; `sikurajapathi2020` (part des réponses fausses expliquée par l'erreur principale).
