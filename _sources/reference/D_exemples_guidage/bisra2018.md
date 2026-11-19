---
cle: bisra2018
reference: "Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F. et Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. Educational Psychology Review, 30(3), 703-725."
doi: 10.1007/s10648-018-9434-x
axe: [D3]
type_etude: méta-analyse (64 rapports, 69 tailles d'effet, 5 917 participants)
public: de l'école primaire à l'université, majoritairement des étudiants
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "demander à l'étudiant d'expliquer lui-même une étape ou une erreur (réponse rédigée ou phrase à compléter) plutôt que de lui donner d'emblée l'explication"
    niveau: B
    transferabilite: forte
  - outil: ExoForge
    regle: "ne pas compter sur une question à choix multiple pour produire l'effet d'une auto-explication rédigée"
    niveau: C
    transferabilite: moyenne
    note: "k = 2 seulement ; à rapprocher d'Atkinson et al. (2003), où le choix du principe avec retour est efficace"
---

# Les invites d'auto-explication (Bisra et al., 2018)

Bisra, K., Liu, Q., Nesbit, J. C., Salimi, F. et Winne, P. H. (2018). Inducing self-explanation: A meta-analysis. *Educational Psychology Review*, 30(3), 703-725. [DOI](https://doi.org/10.1007/s10648-018-9434-x)

**En une phrase.** Demander aux apprenants d'expliquer eux-mêmes ce qu'ils étudient ou résolvent améliore l'apprentissage (g = 0,55), un peu moins quand le groupe témoin reçoit l'explication toute faite (g = 0,35).

## La source

| | |
| --- | --- |
| **Équipe** | Simon Fraser University (Canada) ; Winne et Nesbit, spécialistes de l'autorégulation et des méta-analyses en technologies éducatives. |
| **Nature** | Académique ; financement du Conseil de recherches en sciences humaines du Canada ; pas de conflit d'intérêts (p. 721). |
| **Support** | *Educational Psychology Review* (Springer). |
| **Audience** | 311 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : critères d'inclusion et codage décrits (p. 708-710), études incluses listées ; données de codage non publiées. |

## Ce que fait l'étude

- **Recherche** : six bases de données, terme « self-expla* », 1 306 références examinées (p. 708).
- **Inclusion** (p. 708-709) : un groupe invité à s'expliquer et un groupe témoin sans cette invite ; pas d'autre tactique mêlée (résumé, retour) ; mesure cognitive ; comparaison entre groupes. Sont exclus : observer quelqu'un s'expliquer, expliquer à un autre, prédire sans expliquer, et **choisir une règle ou un principe sans l'expliquer**, avec Atkinson et al. (2003) cité comme exemple.
- **Analyse** : modèle à effets aléatoires, 20 modérateurs (tâche, format de l'invite, type de témoin, niveau scolaire, durée…) (p. 710-711).
- **Corpus** : 69 tailles d'effet, 5 917 participants ; 90 % des études avec tirage au sort individuel (p. 710).

## Résultats

- **Effet global** : g = 0,55 (IC 95 % 0,45 à 0,65) ; I² = 65 % (tableau 1, p. 711).
- **Selon le témoin** (tableau 1, p. 711) : sans explication supplémentaire, g = 0,67 ; avec une explication écrite fournie, g = 0,35 ; avec une autre stratégie, g = 0,30.
- **Selon le niveau** (tableau 7, p. 717) : université g = 0,61 (42 tailles d'effet, 3 349 participants) ; lycée 0,43 ; primaire 0,48 ; pas de différence significative.
- **Format de l'invite** (p. 718-719) : question à choix multiple, g = 0,24, non significatif (2 tailles d'effet seulement) ; invites métacognitives sans effet détectable.
- **Temps** (p. 719) : effet un peu plus grand quand l'auto-explication prend plus de temps que le témoin (0,72 contre 0,41), différence non significative ; le temps est rarement rapporté.
- **Biais de publication** (p. 717-718) : seulement des « fail-safe N » (classique et d'Orwin).

## Avis critique

**Apport.** La méta-analyse de référence sur les invites d'auto-explication : l'effet est net, y compris à l'université, et reste positif quand le témoin reçoit une explication rédigée. Elle contredit le modérateur négatif de Barbieri et al. (2023), qui compare des études différentes et ne mesure pas la même chose.

**Points forts**
- Définition stricte de l'auto-explication et critères d'inclusion explicites.
- Distinction utile selon ce que reçoit le groupe témoin.
- Public universitaire majoritaire.

**Réserves**
1. **Importante** — Biais de publication testé seulement par des « fail-safe N », jugés peu fiables ; ni test d'Egger ni correction.
2. **Importante** — Le temps de travail est rarement contrôlé : une partie de l'effet peut venir d'un temps plus long (p. 719).
3. **Importante** — Le résultat sur les questions à choix multiple repose sur 2 tailles d'effet ; il ne permet pas de conclure. En outre, le choix d'un principe sans explication est exclu de la définition, ce qui écarte Atkinson et al. (2003).
4. **Mineure** — Hétérogénéité notable (I² = 65 %) ; intervalle de prédiction non calculable, τ² n'étant pas rapporté.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les invites d'auto-explication améliorent l'apprentissage, à l'université aussi | A | Méta-analyse large, essais randomisés ; biais de publication mal testé |
| Elles font mieux qu'une explication fournie | B | 6 tailles d'effet seulement pour ce témoin |
| Les invites à choix multiple n'ont pas d'effet | D | 2 tailles d'effet |

**Transférabilité** : forte. Le public est surtout universitaire et les tâches incluent l'étude d'exemples et la résolution de problèmes.

**Pour conclure, il faudrait** comparer dans ExoForge une invite rédigée (phrase à compléter) et un choix du principe avec retour, à temps égal.

## Pour Forge

- **ExoForge** : après une étape ou une erreur, demander à l'étudiant de compléter une phrase d'explication avant d'afficher l'explication rédigée (niveau B).
- **ExoForge** : un menu de principes reste utile (Atkinson et al., 2003 ; Salden et al., 2010), mais ne remplace pas une explication rédigée (niveau C).
- **ExoForge** : contrôler le temps passé dans les comparaisons, la méta-analyse montrant qu'il est rarement mesuré.
