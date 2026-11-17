---
cle: vanderkleij2015
reference: "Van der Kleij, F. M., Feskens, R. C. W. et Eggen, T. J. H. M. (2015). Effects of feedback in a computer-based learning environment on students' learning outcomes: A meta-analysis. Review of Educational Research, 85(4), 475-511."
doi: 10.3102/0034654314564881
axe: [A2]
type_etude: méta-analyse (40 études, 70 tailles d'effet)
public: surtout université (56 effets sur 70) ; retour automatique par question dans un environnement informatique
lecture: texte complet, 08/11/2026
regles:
  - outil: QuizForge
    regle: "donner un retour élaboré (explication, indication) plutôt que seulement juste/faux"
    niveau: B
    transferabilite: forte
  - outil: QuizForge
    regle: "ne jamais se limiter à « juste/faux » sans la bonne réponse"
    niveau: B
    transferabilite: forte
  - outil: ExoForge
    regle: "pour les exercices d'application et de compréhension, privilégier l'explication à la seule bonne réponse"
    niveau: C
    transferabilite: forte
---

# Le type de retour dans les environnements informatiques (Van der Kleij et al., 2015)

Van der Kleij, F. M., Feskens, R. C. W. et Eggen, T. J. H. M. (2015). Effects of feedback in a computer-based learning environment on students' learning outcomes: A meta-analysis. *Review of Educational Research*, 85(4), 475-511. [DOI](https://doi.org/10.3102/0034654314564881)

**En une phrase.** Dans les quiz et exercices informatisés, le retour élaboré (explication, indication) a un effet moyen (0,49), la bonne réponse un effet plus faible (0,33) et le simple juste/faux pratiquement aucun (0,05) ; l'écart en faveur de l'explication est plus net pour les apprentissages de haut niveau.

## La source

| | |
| --- | --- |
| **Équipe** | Cito (institut néerlandais de mesure en éducation) et université de Twente ; psychométrie et évaluation informatisée. |
| **Nature** | Académique et institutionnelle (organisme public d'évaluation). |
| **Support** | *Review of Educational Research* (AERA), revue de synthèse de référence. |
| **Audience** | 898 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : critères et codage décrits, liste et tailles d'effet de chaque étude publiées (tableau 2, p. 491-492). |

## Ce que fait l'étude

- **Inclusion** (p. 484-486) : articles, livres ou thèses en anglais (rapports et actes exclus) ; retour automatique, propre à chaque question et identique pour tous les étudiants d'une condition ; comparaison avec un groupe recevant un autre retour ou aucun ; même contenu et même mode de test dans les deux groupes ; au moins 10 participants par groupe.
- **Particularité** : chaque type de retour est comparé à des témoins différents (aucun retour, juste/faux ou bonne réponse) ; les effets de la bonne réponse et de l'explication sont donc sous-estimés par rapport à « aucun retour » (p. 490).
- **Corpus** (p. 488-490) : recherche de mai 2011 ; 40 études, 70 tailles d'effet de −0,78 à 2,29 ; 58 effets avec retour immédiat, 12 avec retour différé ; 43 sur des apprentissages de bas niveau (mémorisation), 27 de haut niveau ou mixtes.
- **Analyse** : régression avec pondération aléatoire ; dépendance entre effets d'une même étude non modélisée, faute d'effectif ; biais de publication testé par le seul « fail-safe N » (p. 490).

## Résultats

| Variable (tableau 3, p. 495) | Effet moyen | Nombre d'effets |
| --- | --- | --- |
| Juste/faux | 0,05 (non significatif) | 8 |
| Bonne réponse | 0,33 | 9 |
| Retour élaboré | 0,49 | 53 |
| Retour immédiat | 0,46 | 58 |
| Retour différé | 0,22 (non significatif) | 12 |
| Apprentissages de bas niveau | 0,31 | 43 |
| Apprentissages de haut niveau ou mixtes | 0,59 | 27 |
| Université | 0,44 | 56 |
| Primaire et secondaire | 0,34 | 14 |
| Mathématiques | 0,93 | 8 |

- Le retour élaboré est plus efficace que le juste/faux et la bonne réponse surtout pour les apprentissages de haut niveau (résumé, p. 475).

## Avis critique

**Apport.** La référence pour choisir le contenu d'un retour automatique : jamais le juste/faux seul, de préférence une explication. Le public est majoritairement universitaire et les quiz sont proches de ceux de Moodle.

**Points forts**
- Définition précise du retour automatique, proche de ce que produisent QuizForge et ExoForge.
- Tailles d'effet de chaque étude publiées.
- Public universitaire majoritaire.

**Réserves**
1. **Importante** — Effectifs faibles par catégorie : 8 effets pour le juste/faux, 9 pour la bonne réponse, 12 pour le retour différé, 8 en mathématiques. Les intervalles sont larges et l'effet de 0,93 en mathématiques repose sur 8 effets.
2. **Importante** — Effets d'une même étude traités comme indépendants ; témoins hétérogènes selon les comparaisons.
3. **Importante** — Biais de publication testé seulement par un « fail-safe N », et rapports et actes exclus.
4. **Mineure** — Recherche arrêtée en 2011.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Le retour élaboré vaut mieux que la bonne réponse, qui vaut mieux que le juste/faux | B | 40 études, cohérent avec d'autres synthèses, catégories petites |
| L'avantage de l'explication est plus net pour les apprentissages de haut niveau | C | Comparaison entre études |
| Le retour immédiat vaut mieux que le retour différé | C | 12 effets différés seulement |

**Transférabilité** : forte. Retour automatique par question, université, mathématiques bien représentées.

**Pour conclure, il faudrait** des essais qui comparent les types de retour dans la même étude ; voir Attali et van der Kleij (2017), qui montre que l'effet de l'explication dépend de la justesse de la réponse.

## Pour Forge

- **QuizForge** : ne jamais se limiter au juste/faux ; au minimum la bonne réponse, de préférence une explication (niveau B).
- **ExoForge** : pour les questions d'application, donner l'explication de la démarche (niveau C).
- À nuancer avec Attali et van der Kleij (2017) : l'explication est surtout utile après une erreur ; et avec Say et al. (2023) : pendant des essais multiples, le retour détaillé immédiat peut encourager l'essai-erreur.
