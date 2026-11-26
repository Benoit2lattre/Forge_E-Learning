---
cle: brassil2019
reference: "Brassil, C. E. et Couch, B. A. (2019). Multiple-true-false questions reveal more thoroughly the complexity of student thinking than multiple-choice questions: A Bayesian item response model comparison. International Journal of STEM Education, 6, article 16."
doi: 10.1186/s40594-019-0169-0
axe: [B3]
type_etude: essai croisé dans quatre examens (36 questions posées en QCM ou en vrai/faux multiples), modèle bayésien de réponse aux items
public: 194 étudiants d'un cours d'introduction à la biologie (États-Unis)
lecture: texte complet, 08/11/2026
regles:
  - outil: QuizForge
    regle: "pour un diagnostic formatif, préférer le vrai/faux multiple (chaque affirmation jugée séparément) au QCM à réponse unique"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "ne pas lire un QCM réussi comme une maîtrise complète : une partie des étudiants qui ont la bonne réponse acceptent aussi un leurre"
    niveau: C
    transferabilite: forte
---

# Vrai/faux multiples contre QCM (Brassil et Couch, 2019)

Brassil, C. E. et Couch, B. A. (2019). Multiple-true-false questions reveal more thoroughly the complexity of student thinking than multiple-choice questions: A Bayesian item response model comparison. *International Journal of STEM Education*, 6, article 16. [DOI](https://doi.org/10.1186/s40594-019-0169-0)

**En une phrase.** Les mêmes questions posées en vrai/faux multiples plutôt qu'en QCM à réponse unique estiment mieux la part d'étudiants qui maîtrisent toutes les options et repèrent mieux les conceptions erronées, parce que beaucoup d'étudiants qui choisissent la bonne réponse jugeraient aussi vrai un leurre.

## La source

| | |
| --- | --- |
| **Équipe** | École des sciences biologiques de l'université du Nebraska ; recherche sur l'évaluation en biologie. |
| **Nature** | Académique ; étude menée dans les examens d'un cours de leur université. |
| **Support** | *International Journal of STEM Education* (Springer), libre accès. |
| **Audience** | 83 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : plan et modèle décrits, matériel complémentaire ; données d'examen non publiques. Les références renvoient aux sections, la revue numérotant les articles. |

## Ce que fait l'étude

- **Plan** (Méthodes) : 36 questions intégrées à quatre examens d'un cours d'introduction à la biologie ; deux versions d'examen distribuées de façon semi-aléatoire ; chaque question apparaît en QCM dans une version et en vrai/faux multiples dans l'autre, avec le même texte ; 194 étudiants.
- **Modèle** : modèle bayésien de réponse aux items qui suppose trois états (maîtrise, maîtrise partielle, raisonnement informé) plutôt qu'un hasard uniforme, ajusté aux deux formats à la fois.

## Résultats

- **Modèle** : les données soutiennent un traitement des questions par degrés de compréhension plutôt que par hasard pur (Résultats).
- **Maîtrise** : le vrai/faux multiple estime de plus près la part d'étudiants qui maîtrisent toutes les options ; le QCM la surestime, car des étudiants trouvent la bonne réponse avec une maîtrise partielle.
- **Conceptions erronées** : le vrai/faux multiple repère mieux les étudiants qui tiennent un leurre pour vrai.
- **Prédiction** : les réponses en vrai/faux multiples prédisent les réponses en QCM, pas l'inverse.
- Résultat antérieur de la même équipe : près de la moitié des étudiants qui réussissent un QCM auraient accepté au moins un leurre en vrai/faux multiples (Couch et al., 2018, cité en introduction).

## Avis critique

**Apport.** Argument solide pour utiliser le vrai/faux multiple quand l'objectif est de savoir ce que les étudiants pensent de chaque option, notamment pour le retour en classe ou dans DiagForge.

**Points forts**
- Même énoncé dans les deux formats, plan croisé dans de vrais examens.
- Modèle qui teste explicitement l'hypothèse du hasard et le biais vers « vrai ».
- Conséquences pratiques discutées pour l'enseignant.

**Réserves**
1. **Importante** — Les conclusions passent par un modèle statistique : elles dépendent de ses hypothèses (trois états de compréhension).
2. **Importante** — Le modèle comparé se limite aux questions à une seule affirmation vraie (Discussion).
3. **Mineure** — Un cours de biologie, une université ; répartition semi-aléatoire des versions.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Le vrai/faux multiple révèle des conceptions partielles que le QCM masque | C | Essai croisé dans un cours, conclusions par modèle |

**Transférabilité** : forte. QuizForge et Moodle proposent les deux formats ; en mécanique, une même situation se prête à plusieurs affirmations à juger.

**Pour conclure, il faudrait** reprendre le plan croisé dans un cours de mécanique et comparer l'information que DiagForge tire des deux formats.

## Pour Forge

- **QuizForge** : pour les quiz de diagnostic, proposer des vrai/faux multiples sur une même situation (niveau C). Le barème est traité dans la fiche de Schmidt et al. (2021).
- **DiagForge** : ne pas présenter un QCM réussi comme une maîtrise complète ; avec le vrai/faux multiple, afficher le taux d'acceptation de chaque affirmation fausse (niveau C).
