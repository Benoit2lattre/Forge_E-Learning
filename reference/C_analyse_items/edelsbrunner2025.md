---
cle: edelsbrunner2025
reference: "Edelsbrunner, P. A., Simonsmeier, B. A. et Schneider, M. (2025). The Cronbach's alpha of domain-specific knowledge tests before and after learning: A meta-analysis of published studies. Educational Psychology Review, 37, article 4."
doi: 10.1007/s10648-024-09982-y
axe: [C1]
type_etude: méta-analyse de 285 coefficients alpha (55 échantillons, 52 études) de tests de connaissances passés avant et après un apprentissage
public: tests de connaissances utilisés en recherche, tous âges et domaines (sciences, mathématiques, langues, sciences humaines)
lecture: texte complet, 08/11/2026
regles:
  - outil: DiagForge
    regle: "ne pas juger un quiz « mauvais » sur un seuil fixe d'alpha (0,70) : situer l'alpha par rapport à ce qu'on attend pour ce nombre de questions"
    niveau: B
    transferabilite: forte
  - outil: DiagForge
    regle: "afficher avec l'alpha le nombre de questions et la corrélation moyenne entre questions"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "ne pas conseiller de retirer des questions pour faire monter l'alpha si elles couvrent une partie du programme"
    niveau: C
    transferabilite: forte
---

# L'alpha de Cronbach des tests de connaissances (Edelsbrunner et al., 2025)

Edelsbrunner, P. A., Simonsmeier, B. A. et Schneider, M. (2025). The Cronbach's alpha of domain-specific knowledge tests before and after learning: A meta-analysis of published studies. *Educational Psychology Review*, 37, article 4. [DOI](https://doi.org/10.1007/s10648-024-09982-y)

**En une phrase.** Dans les études publiées, l'alpha typique d'un test de connaissances est de 0,85, mais il varie énormément (intervalle de prédiction de 0,35 à 0,96 pour un test de 20 items) et les alphas faibles sont sous-représentés ; les connaissances étant hétérogènes, un seuil fixe comme 0,70 est inadapté.

## La source

| | |
| --- | --- |
| **Équipe** | ETH Zurich (Edelsbrunner) et université de Trèves (Simonsmeier, Schneider), psychologie de l'éducation. |
| **Nature** | Académique ; libre accès financé par l'ETH (p. 37). |
| **Support** | *Educational Psychology Review* (Springer), libre accès. |
| **Audience** | 205 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Très bonne : données et scripts déposés sur OSF (osf.io/7ygc5). Pages du fichier PDF. |

## Ce que fait l'étude

- **Données** (p. 13-15) : reprise d'une méta-analyse antérieure sur les connaissances préalables (493 études) ; seules les études qui donnent l'alpha du même test avant et après l'apprentissage sont gardées (52 études, 285 alphas).
- **Analyses** : méta-analyse à effets aléatoires, intervalles de prédiction, modérateurs (nombre d'items, format de réponse, domaine, âge, moment), quatre méthodes pour détecter un biais de publication.

## Résultats

- **Alpha typique** (p. 18) : 0,85 [0,82 ; 0,87], pour une corrélation moyenne entre items de seulement 0,22 ; l'alpha est élevé parce que les tests sont longs (médiane 20 items, jusqu'à 150).
- **Dispersion** (p. 18) : intervalle de prédiction à 90 % de 0,35 à 0,96 ; presque toute la variabilité vient de différences réelles entre tests.
- **Valeurs attendues selon la longueur** (tableau 3, p. 27) : pour 10 items, alpha prévu 0,77 (de 0,18 à 0,94) ; pour 20 items, 0,84 (0,44 à 0,96) ; pour 50 items, 0,90 (0,65 à 0,97).
- **Biais** (p. 19-20, 28) : alphas faibles sous-représentés et pics juste au-dessus de 0,70, 0,80 et 0,90, signe que les tests sont retouchés ou que les alphas faibles ne sont pas publiés.
- **Modérateurs** : alpha plus élevé avec plus d'items, en réponse ouverte, après un enseignement, en mathématiques et en langues qu'en sciences.
- **Recommandations** (p. 34-36) : ne plus imposer de seuil fixe, publier l'alpha avec la corrélation moyenne entre items, ne pas retirer d'items pertinents pour faire monter l'alpha (au détriment de la couverture du programme).

## Avis critique

**Apport.** Fournit des valeurs attendues d'alpha selon le nombre de questions, et de bonnes raisons de ne pas lire l'alpha d'un quiz comme une note de qualité.

**Points forts**
- Données et scripts publics.
- Plusieurs méthodes concordantes pour le biais de publication.
- Lien explicite entre fiabilité et validité de contenu.

**Réserves**
1. **Importante** — Tests de recherche (avant et après une intervention), pas des examens de cours ; corpus hérité d'une autre méta-analyse.
2. **Importante** — L'intervalle de prédiction est très large : il dit surtout qu'un alpha bas n'est pas anormal, pas quelle valeur viser.
3. **Mineure** — Mode de calcul de l'alpha rarement précisé dans les études incluses (reconnu p. 34).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| L'alpha des tests de connaissances varie fortement ; un seuil fixe est inadapté | B | Méta-analyse, données ouvertes, argument théorique |
| Valeurs attendues selon le nombre d'items | C | Prédictions d'un modèle, très larges |

**Transférabilité** : forte pour le principe ; nos quiz de mécanique couvrent plusieurs notions, ce qui fait attendre des alphas modérés.

**Pour conclure, il faudrait** comparer, sur nos quiz, l'alpha et la corrélation moyenne entre questions aux valeurs du tableau 3.

## Pour Forge

- **DiagForge** : présenter l'alpha (« cohérence interne ») avec le nombre de questions et la plage attendue, sans verdict au seuil de 0,70 (niveau B).
- **DiagForge** : afficher la corrélation moyenne entre questions (niveau C).
- **DiagForge** : ne pas recommander de supprimer une question seulement pour faire monter l'alpha (niveau C ; voir Taber, 2018).
