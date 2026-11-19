---
cle: zheng2026
reference: "Zheng, Z., Hatala, M. et Ahrar, A. (2026). An immediate and retrospective analysis of stability and change: Examining students' emotion and motivation profiles in response to outcome-presenting learning analytics dashboards. In Proceedings of LAK26: 16th International Learning Analytics and Knowledge Conference (p. 480-490). ACM."
doi: 10.1145/3785022.3785099
axe: [G2, G1]
type_etude: étude à méthodes mixtes, deux tableaux de bord attribués en alternance (127 étudiants, 217 cycles), sans test statistique
public: étudiants de premier cycle en cours d'introduction à la programmation, programme interdisciplinaire, une université nord-américaine
lecture: texte complet, 08/11/2026
regles:
  - outil: DiagForge
    regle: "ne pas faire de la moyenne de classe (ou d'une boîte à moustaches de la classe) le repère principal du rapport individuel ; la placer après le critère, ou ne pas l'afficher"
    niveau: D
    transferabilite: moyenne
  - outil: DiagForge
    regle: "tester une restitution sur les étudiants les plus faibles avant de la généraliser : un même affichage peut encourager les uns et décourager les autres"
    niveau: C
    transferabilite: forte
---

# Moyenne de classe ou pairs proches : émotions sur un semestre (Zheng et al., 2026)

Zheng, Z., Hatala, M. et Ahrar, A. (2026). An immediate and retrospective analysis of stability and change: Examining students' emotion and motivation profiles in response to outcome-presenting learning analytics dashboards. In *Proceedings of LAK26* (p. 480-490). ACM. [DOI](https://doi.org/10.1145/3785022.3785099)

**En une phrase.** Des étudiants en programmation voient leur note soit avec la moyenne, le minimum, le maximum et une boîte à moustaches de la classe (comme dans Canvas), soit avec 6 pairs anonymes un peu meilleurs pour un effort semblable ; le premier affichage ancre les étudiants sur la moyenne et s'accompagne de plus de désespoir chez certains, le second de plus d'espoir, y compris chez quelques étudiants faibles, mais l'étude est descriptive et sans test.

## La source

| | |
| --- | --- |
| **Équipe** | École des arts interactifs et de la technologie, université Simon Fraser (Canada) ; le laboratoire a conçu le tableau de bord « pairs proches » et l'étudie depuis plusieurs années (p. 482). |
| **Nature** | Académique ; subvention du CRSNG (Canada) (p. 490). Les auteurs évaluent leur propre dispositif. |
| **Support** | Actes de la conférence LAK26 (ACM), libre accès. |
| **Audience** | 1 citation (OpenAlex, 08/11/2026) ; article très récent. |
| **Reproductibilité** | Faible : questions ouvertes citées, instruments nommés, mais ni données ni grille de codage ; pourcentages lus sur des figures. |

## Ce que fait l'étude

- **Deux tableaux de bord** (p. 482, fig. 1-2) : CP-D, note de l'étudiant avec moyenne, maximum, minimum et boîte à moustaches de la classe ; IC-D, note et temps passé de l'étudiant à côté de 6 pairs anonymes « un peu meilleurs pour un effort semblable ». IC-D n'est pas une comparaison à sa propre progression.
- **Participants** (p. 483) : 157 recrutés en 2023-2024 (2 % de points bonus), 127 retenus ; attribution en alternance après tri sur les notes des prérequis ; 1 ou 2 cycles chacun, 217 cycles.
- **Mesures** (p. 483-484) : questionnaires d'émotions (AEQ révisé) avant le devoir et juste après la consultation ; orientation des buts (PALS) qui définit 3 profils par classification ; en fin de semestre, réponses ouvertes codées (κ = 0,761) pour repérer les émotions rappelées.
- **Analyse** : pourcentages par profil et par tableau de bord (cellules de 16 à 70 cycles, tableau 1, p. 484), nuages de points, citations ; aucun test statistique.

## Résultats

- **Espoir** (p. 484) : plus fréquent avec IC-D (profil « maîtrise » : 52 % immédiat, 65 % rappelé) ; profil « non compétitif » : 10 % d'espoir immédiat avec CP-D contre 28 % avec IC-D ; espoir immédiat et rappelé chez 19 % (IC-D) contre 2 % (CP-D).
- **Désespoir** (p. 484) : immédiat plus fréquent avec CP-D, surtout chez les « non compétitifs » (35 %) ; rarement rappelé en fin de semestre, quel que soit l'affichage.
- **Déception** (p. 485) : profil « performance » 44 % avec CP-D contre 24 % avec IC-D.
- **Notes basses** (p. 486, fig. 7) : quelques étudiants faibles du profil « non compétitif » avec IC-D rappellent de l'espoir.
- **Témoignages** (p. 486-488) : avec CP-D, la moyenne sert de repère (« au-dessus de la moyenne, ça m'a donné de l'espoir » ; « j'étais trop sûr de moi ») ; avec IC-D, des étudiants forts se disent refroidis par des pairs encore meilleurs, des étudiants faibles rassurés (« ils n'étaient pas loin de mes notes »).
- **Conclusion des auteurs** (p. 489-490) : aucun affichage ne convient à tous ; proposer des formes hybrides ou adaptées au profil.

## Avis critique

**Apport.** Suit les émotions au-delà de la réaction immédiate et montre, par des témoignages, comment la moyenne de classe devient le repère qui fixe l'ambition : utile pour choisir ce que DiagForge met au premier plan.

**Points forts**
- Cours réels, deux années, attribution équilibrée sur le niveau initial.
- Mesure immédiate et rappel en fin de semestre.
- Résultats lus selon le profil de motivation et la note, pas seulement en moyenne.

**Réserves**
1. **Majeure** — Aucun test statistique ; des pourcentages sur des cellules de 16 à 70 cycles, avec des étudiants comptés deux fois. Les écarts peuvent tenir au hasard.
2. **Importante** — Le rappel est codé dans des réponses ouvertes : ne pas mentionner une émotion n'est pas ne pas l'avoir eue. Aucune mesure de réussite ni de comportement.
3. **Importante** — Les deux affichages diffèrent sur plusieurs points (moyenne et extrêmes contre pairs choisis ; temps passé affiché seulement dans IC-D) ; les auteurs évaluent leur propre conception.
4. **Mineure** — Attribution en alternance et non par tirage au sort.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| La moyenne de classe sert d'ancre à l'interprétation | C | Témoignages concordants, cohérents avec Fleur et al. (2023) |
| La comparaison à des pairs proches soutient l'espoir des étudiants faibles | D | Quelques cas, pas de test |
| Aucun affichage ne convient à tous les profils | C | Réactions opposées observées sous le même affichage |

**Transférabilité** : moyenne. Premier cycle en programmation, notes de devoirs ; les mécanismes (ancrage sur la moyenne, réactions opposées des forts et des faibles) se transposent à un rapport de quiz.

**Pour conclure, il faudrait** un essai tiré au sort dans DiagForge comparant « critère seul » et « critère + boîte à moustaches de la classe », avec analyse séparée du quart le plus faible.

## Pour Forge

- **DiagForge** : la moyenne de classe n'est pas le repère principal du rapport individuel ; le critère vient d'abord (niveau D, appuyé par [fleur2023](fleur2023.md) et [weidlich2024](weidlich2024.md), niveau C).
- **DiagForge** : vérifier l'effet d'une forme de restitution sur les étudiants faibles avant de la généraliser (niveau C).
