---
cle: herodotou2025
reference: "Herodotou, C., Carr, J., Shrestha, S., Comfort, C., Bayer, V., Maguire, C., Lee, J., Mulholland, P. et Fernandez, M. (2025). Prescriptive analytics motivating distance learning students to take remedial action: A case study of a student-facing dashboard. In Proceedings of the 15th International Learning Analytics and Knowledge Conference (LAK '25) (p. 306-316). ACM."
doi: 10.1145/3706468.3706508
axe: [G2]
type_etude: étude de cas sans groupe de comparaison (30 étudiants ; questionnaire 23, entretiens 10, traces de connexion)
public: étudiants de licence à distance, cours de gestion, Open University (Royaume-Uni)
lecture: texte complet, 08/11/2026
regles:
  - outil: DiagForge
    regle: "terminer chaque rapport individuel par des recommandations explicites : notions à revoir et ressources ou exercices précis, avec lien direct"
    niveau: D
    transferabilite: forte
    note: "partie la mieux jugée par les étudiants ; aucun effet sur la réussite mesuré"
  - outil: DiagForge
    regle: "ne pas afficher de prédiction de note sans expliquer comment elle est calculée"
    niveau: D
    transferabilite: forte
  - outil: DiagForge
    regle: "indiquer dans le rapport comment obtenir de l'aide (contact de l'enseignant, séance de questions)"
    niveau: D
    transferabilite: moyenne
---

# Dire quoi faire ensuite : un tableau de bord prescriptif (Herodotou et al., 2025)

Herodotou, C., Carr, J., Shrestha, S., Comfort, C., Bayer, V., Maguire, C., Lee, J., Mulholland, P. et Fernandez, M. (2025). Prescriptive analytics motivating distance learning students to take remedial action: A case study of a student-facing dashboard. In *Proceedings of LAK '25* (p. 306-316). ACM. [DOI](https://doi.org/10.1145/3706468.3706508)

**En une phrase.** Trente étudiants à distance utilisent pendant un semestre un tableau de bord qui montre leur activité, une prédiction de réussite au prochain devoir et des recommandations (ressources à étudier, contact de l'enseignant) ; les recommandations et le contact sont les seules fonctions qu'aucun étudiant ou presque ne juge peu utiles, mais l'effet sur la réussite n'est pas mesuré.

## La source

| | |
| --- | --- |
| **Équipe** | Open University (Royaume-Uni), équipe d'analytique d'apprentissage qui a conçu le tableau de bord avec 20 étudiants (p. 308). |
| **Nature** | Académique ; les auteurs évaluent leur propre outil ; financement et conflits non rapportés. |
| **Support** | Actes de la conférence LAK (ACM), libre accès. |
| **Audience** | 7 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Faible : pas de données ni d'algorithme de recommandation publiés ; questions d'entretien indicatives. Étude de cas, la démarche se refait mais pas les chiffres. |

## Ce que fait l'étude

- **Tableau de bord** (p. 308-309, fig. 1) : activité sur la plateforme ; prédiction de réussite au prochain devoir ; ressources recommandées (automatiquement et par l'équipe enseignante) ; boutons de contact de l'enseignant et du service d'aide ; badges.
- **Participants** (p. 308-310) : 30 volontaires ; bons d'achat de 20 £ pour une consultation hebdomadaire et le questionnaire, 20 £ de plus pour l'entretien ; rappel hebdomadaire par courriel.
- **Usage** (p. 310) : 1 à 65 consultations sur 15 semaines (17,4 en moyenne).
- **Mesures** : questionnaire (23 répondants), entretiens (10), corrélations de Spearman entre utilité perçue de chaque fonction et motivation (p. 312).

## Résultats

- **Utilité** (p. 310-311) : fonctions jugées très ou extrêmement utiles par 18 (graphique d'activité et prédiction), 17 (ressources recommandées), 15 (recommandations de l'équipe), 11 (contact) étudiants sur 23 ; les ressources recommandées et le contact ne sont jugés peu utiles que par 0 ou 1 étudiant. Badges, présence aux séances et prédiction sont les moins appréciés.
- **Motivation et actions déclarées** (p. 311) : 14 sur 23 disent que le tableau de bord les a motivés à étudier ; 15 déclarent une action (planifier, étudier les ressources recommandées, contacter l'enseignant).
- **Corrélations** (p. 312) : motivation liée à l'utilité perçue des ressources recommandées (rs = 0,47 ; p = 0,032) et du « matériel le plus consulté » (rs = 0,54 ; p = 0,022) ; 7 autres fonctions sans lien significatif.
- **Entretiens** (p. 312-314) : prédiction ignorée faute d'explication de son calcul ; activité mal mesurée pour qui imprime les documents ou regarde les enregistrements ; rappels par courriel décisifs pour l'usage.

## Avis critique

**Apport.** Montre, du point de vue des étudiants, que la partie « que faire maintenant » est la plus utile d'un rapport, et que des indicateurs mal mesurés ou inexpliqués (activité, prédiction) perdent leur crédit.

**Points forts**
- Usage réel sur un semestre, traces de connexion.
- Triangulation questionnaire, entretiens, traces.
- Retours concrets sur la conception (explication des prédictions, accessibilité, liens directs).

**Réserves**
1. **Majeure** — Aucun groupe de comparaison ni mesure de réussite ; la conclusion des auteurs sur un « impact positif sur le comportement et la performance » (p. 315) dépasse ce qui est mesuré (déclarations).
2. **Importante** — Volontaires rémunérés et relancés chaque semaine ; 23 répondants ; 9 corrélations sans correction, sur 15 à 21 étudiants.
3. **Mineure** — Les auteurs évaluent leur propre outil ; limites non discutées.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les étudiants jugent les recommandations d'action plus utiles que les indicateurs descriptifs | C | Accord du questionnaire et des entretiens, petit échantillon volontaire |
| Le tableau de bord améliore la réussite | D | Non mesuré |
| Une prédiction inexpliquée est ignorée | D | Quelques témoignages |

**Transférabilité** : forte pour les principes de conception (dire quoi faire, expliquer les indicateurs), faible pour les chiffres (étudiants à distance adultes, cours de gestion).

**Pour conclure, il faudrait** comparer dans DiagForge, par tirage au sort, un rapport sans recommandations et un rapport avec recommandations liées aux questions manquées, et mesurer l'ouverture des ressources et le score au quiz suivant.

## Pour Forge

- **DiagForge** : chaque rapport individuel se termine par les notions à revoir et des ressources ou exercices précis, avec lien direct (niveau D ici, C avec [weidlich2024](weidlich2024.md)).
- **DiagForge** : pas de prédiction de note sans explication de son calcul (niveau D).
- **DiagForge** : indiquer comment obtenir de l'aide (niveau D). Voir [kaliisa2024](kaliisa2024.md) : aucun effet des tableaux de bord sur la réussite n'est établi.
