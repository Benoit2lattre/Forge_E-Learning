---
cle: kaliisa2024
reference: "Kaliisa, R., Misiejuk, K., López-Pernas, S., Khalil, M. et Saqr, M. (2024). Have learning analytics dashboards lived up to the hype? A systematic review of impact on students' achievement, motivation, participation and attitude. In Proceedings of the 14th Learning Analytics and Knowledge Conference (LAK '24) (p. 295-304). ACM."
doi: 10.1145/3636555.3636884
axe: [G2]
type_etude: revue systématique de 38 études (sans méta-analyse), tailles d'effet converties en d de Cohen quand c'était possible
public: études de tableaux de bord d'apprentissage, 68 % dans le supérieur, moitié en sciences et ingénierie
lecture: texte complet, 08/11/2026
regles:
  - outil: DiagForge
    regle: "ne pas présenter le rapport aux étudiants comme un moyen d'améliorer les notes : aucun effet sur la réussite n'est établi pour les tableaux de bord"
    niveau: B
    transferabilite: forte
  - outil: DiagForge
    regle: "pour évaluer l'effet du rapport, comparer des groupes tirés au sort (accès contre pas d'accès) en gardant tous les étudiants, jamais utilisateurs contre non-utilisateurs"
    niveau: B
    transferabilite: forte
  - outil: DiagForge
    regle: "enregistrer qui ouvre le rapport et quand, pour distinguer l'accès de l'usage"
    niveau: C
    transferabilite: forte
---

# Les tableaux de bord étudiants tiennent-ils leurs promesses ? (Kaliisa et al., 2024)

Kaliisa, R., Misiejuk, K., López-Pernas, S., Khalil, M. et Saqr, M. (2024). Have learning analytics dashboards lived up to the hype? A systematic review of impact on students' achievement, motivation, participation and attitude. In *Proceedings of LAK '24* (p. 295-304). ACM. [DOI](https://doi.org/10.1145/3636555.3636884)

**En une phrase.** Sur 38 études, les tableaux de bord d'apprentissage n'ont pas d'effet démontré sur la réussite (77 % des effets négligeables ou petits), un effet plus net sur la participation, et les rares grands effets viennent de comparaisons utilisateurs contre non-utilisateurs ou d'interventions mélangées.

## La source

| | |
| --- | --- |
| **Équipe** | Universités d'Oslo, de Bergen et de Finlande orientale ; chercheurs en analytique d'apprentissage. |
| **Nature** | Académique ; financements norvégien, finlandais et européens (p. 303). Les auteurs n'évaluent pas d'outil à eux. |
| **Support** | Actes de la conférence LAK (ACM), relecture par les pairs, libre accès. |
| **Audience** | 130 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : requête, bases, date (15/06/2023) et diagramme PRISMA donnés (p. 297-298) ; grille de codage et calcul des d non détaillés. |

## Ce que fait l'étude

- **Recherche** (p. 297) : Scopus, Web of Science, ACM, ERIC ; 527 articles après doublons, 57 retenus au tri, 38 inclus (études empiriques, données quantitatives suffisantes, plan avec groupe de comparaison annoncé, revues relues).
- **Corpus** (p. 298) : 68,4 % dans le supérieur ; 57,9 % quasi expérimentaux, 23,7 % (9) essais randomisés, 15,8 % sans groupe de comparaison ; 50 % en sciences et ingénierie.
- **Synthèse** (p. 297) : méta-analyse prévue puis abandonnée faute d'études comparables ; effets convertis en d de Cohen et classés (négligeable, petit, moyen, grand).

## Résultats

- **Réussite** (p. 298-299, tableau 1) : sur 34 études, 14 effets négligeables (41,2 %), 12 petits (35,3 %), 3 moyens (8,8 %), 5 grands (14,7 %). Les effets moyens et grands viennent surtout de comparaisons utilisateurs contre non-utilisateurs, d'un tableau de bord qui alerte l'enseignant, ou d'un tableau de bord comparé au papier.
- **Participation** (p. 299-300, tableau 2) : 9 études ; 5 avec effet moyen ou grand (accès à la plateforme, messages, jours de lecture).
- **Motivation** (p. 301, tableau 3) : 6 études, effets de négligeables à grands ; le grand effet (d = 0,81 sur la motivation extrinsèque) est l'article de congrès de Fleur et al. (2020), version courte de [fleur2023](fleur2023.md).
- **Attitudes** (p. 301-302, tableau 4) : 8 études, surtout effets nuls ou petits.
- **Constat méthodologique** (p. 302-303) : aucun essai randomisé de grande taille ; les grands effets viennent d'études petites ; l'accès est pris pour l'usage ; mesures hétérogènes et peu validées.

## Avis critique

**Apport.** Bilan sobre et récent : il interdit de promettre un gain de réussite à partir d'un tableau de bord et donne la liste des erreurs de méthode à éviter pour évaluer DiagForge.

**Points forts**
- Recherche systématique décrite, quatre bases.
- Tailles d'effet ramenées à une même unité et lues avec le plan d'étude.
- Distinction explicite entre accès, usage et effet.

**Réserves**
1. **Importante** — Pas de méta-analyse, pas d'évaluation formelle du risque de biais ni du biais de publication ; les classes « petit » ou « grand » mélangent plans randomisés et non randomisés.
2. **Importante** — Le critère « groupe de comparaison » n'est pas tenu : 6 études sans groupe de comparaison sont incluses (p. 298).
3. **Mineure** — Quelques incohérences de saisie : Fleur et al. (2020) apparaît avec n = 26 dans le tableau 3 et 34 contre 38 dans le texte (p. 301).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Pas d'effet établi des tableaux de bord sur la réussite | B | Revue systématique concordante avec les revues antérieures ; absence de preuve plutôt que preuve d'absence |
| Effet plus net sur la participation | C | 9 études, plans souvent non randomisés |
| Comparer utilisateurs et non-utilisateurs surestime l'effet | B | Argument de sélection, illustré par les études du corpus |

**Transférabilité** : forte pour les constats de méthode ; moyenne pour les effets, car les tableaux de bord étudiés sont variés (activité, prédiction, collaboration) et rarement des rapports de quiz.

**Pour conclure, il faudrait** un essai randomisé en intention de traiter dans nos cours : rapport DiagForge individuel contre rapport collectif seul, avec le score au quiz suivant et l'ouverture du rapport enregistrée.

## Pour Forge

- **DiagForge** : ne pas annoncer aux étudiants ni à l'équipe que le rapport fait progresser les notes (niveau B).
- **DiagForge** : toute évaluation de l'effet du rapport compare des groupes tirés au sort en gardant tous les étudiants ; jamais « ceux qui l'ont ouvert » contre « ceux qui ne l'ont pas ouvert » (niveau B).
- **DiagForge** : journaliser l'ouverture du rapport (qui, quand) pour distinguer accès et usage (niveau C). Voir [fleur2023](fleur2023.md), où l'exclusion des non-utilisateurs illustre ce piège.
