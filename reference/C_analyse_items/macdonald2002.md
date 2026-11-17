---
cle: macdonald2002
reference: "MacDonald, P. et Paunonen, S. V. (2002). A Monte Carlo comparison of item and person statistics based on item response theory versus classical test theory. Educational and Psychological Measurement, 62(6), 921-943."
doi: 10.1177/0013164402238082
axe: [C2]
type_etude: simulation de Monte-Carlo (tests de 20, 40 et 60 items ; 2 × 1 000 répondants simulés ; 100 répétitions par condition)
public: données simulées selon un modèle de réponse aux items à un ou deux paramètres
lecture: texte complet, 08/11/2026
regles:
  - outil: DiagForge
    regle: "garder les indicateurs classiques (taux de réussite, corrélation item-reste) plutôt qu'un modèle de réponse aux items : la difficulté et le classement des étudiants sont presque identiques"
    niveau: C
    transferabilite: moyenne
    note: "simulation à 1 000 répondants ; à nos effectifs, un modèle de réponse aux items serait de toute façon mal estimé (voir weber2026, à lire)"
  - outil: DiagForge
    regle: "lire avec prudence la discrimination d'une question très facile ou très difficile : l'indice classique y sous-estime la discrimination réelle"
    niveau: C
    transferabilite: forte
---

# Théorie classique ou théorie des réponses aux items ? (MacDonald et Paunonen, 2002)

MacDonald, P. et Paunonen, S. V. (2002). A Monte Carlo comparison of item and person statistics based on item response theory versus classical test theory. *Educational and Psychological Measurement*, 62(6), 921-943. [DOI](https://doi.org/10.1177/0013164402238082)

**En une phrase.** Sur des tests simulés, la théorie classique (taux de réussite, score total) donne la même difficulté des items et le même classement des répondants que la théorie des réponses aux items ; seule la discrimination classique devient imprécise quand les items ont des difficultés très étalées.

## La source

| | |
| --- | --- |
| **Équipe** | Département de psychologie, université de Western Ontario. |
| **Nature** | Académique, psychométrie. |
| **Support** | *Educational and Psychological Measurement* (Sage). |
| **Audience** | 130 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Bonne : procédure de simulation entièrement décrite (p. 926-929). |

## Ce que fait l'étude

- **Simulation** (p. 926-927) : 1 000 répondants simulés ; tests de 20, 40 ou 60 items ; plusieurs plages de difficulté et de discrimination ; deux échantillons indépendants par condition ; 100 répétitions.
- **Comparaison** (p. 927-929) : difficulté (taux de réussite contre paramètre b), discrimination (corrélation item-total contre paramètre a), niveau des répondants (score total contre θ) ; comparabilité, stabilité d'un échantillon à l'autre, exactitude par rapport aux vraies valeurs.

## Résultats

- **Difficulté et niveau des répondants** (p. 940-941) : très comparables entre les deux théories, stables et exacts dans toutes les conditions.
- **Stabilité** : les indicateurs classiques sont même un peu plus stables d'un échantillon à l'autre.
- **Discrimination** : exacte avec le modèle de réponse aux items dans toutes les conditions ; exacte avec l'indice classique seulement quand les difficultés des items sont resserrées (p. 941-942).

## Avis critique

**Apport.** Justifie de rester, pour des quiz de classe, sur les indicateurs classiques, plus simples à expliquer, en sachant que la discrimination d'une question très facile ou très difficile est mal mesurée.

**Points forts**
- Plan de simulation systématique, vraies valeurs connues.
- Conclusions nuancées, sans parti pris pour l'une des théories.

**Réserves**
1. **Importante** — 1 000 répondants simulés : la question des petits effectifs, la nôtre, n'est pas traitée.
2. **Importante** — Données générées par le modèle de réponse aux items lui-même, ce qui le favorise sur l'exactitude de la discrimination.
3. **Mineure** — Discrimination classique calculée avec l'item inclus dans le total.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Difficulté et classement des répondants identiques en théorie classique | B | Simulation systématique, concordante avec d'autres travaux cités |
| La discrimination classique est imprécise quand les difficultés sont étalées | C | Simulation, modèle générateur favorable à la théorie des réponses aux items |

**Transférabilité** : moyenne. Les conclusions valent pour de grands effectifs ; à nos effectifs, l'argument penche encore plus vers la théorie classique.

**Pour conclure, il faudrait** vérifier, sur nos données, la stabilité de la discrimination d'une session à l'autre pour une même question.

## Pour Forge

- **DiagForge** : rester en théorie classique (niveau C).
- **DiagForge** : pour une question réussie à moins de 30 % ou à plus de 90 %, signaler que la discrimination est peu fiable plutôt que la juger mauvaise (niveau C ; voir Slepkov et al., 2021).
