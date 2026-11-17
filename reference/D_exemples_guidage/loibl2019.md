---
cle: loibl2019
reference: "Loibl, K. et Leuders, T. (2019). How to make failure productive: Fostering learning from errors through elaboration prompts. Learning and Instruction, 62, 1-10."
doi: 10.1016/j.learninstruc.2019.03.002
axe: [D3]
type_etude: expérience en classe avec répartition individuelle au hasard (200 élèves, 3 groupes)
public: élèves de 10 à 12 ans (5e année, Realschule, Allemagne), comparaison de fractions
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "après une tentative de résolution, montrer des solutions erronées typiques à côté de la solution correcte et demander explicitement de les comparer et de dire où est l'erreur"
    niveau: C
    transferabilite: moyenne
  - outil: ExoForge
    regle: "choisir les solutions erronées montrées parmi les erreurs que l'étudiant a lui-même faites ou risque de faire"
    niveau: C
    transferabilite: moyenne
---

# Rendre l'échec productif par des consignes de comparaison (Loibl et Leuders, 2019)

Loibl, K. et Leuders, T. (2019). How to make failure productive: Fostering learning from errors through elaboration prompts. *Learning and Instruction*, 62, 1-10. [DOI](https://doi.org/10.1016/j.learninstruc.2019.03.002)

**En une phrase.** Après avoir cherché seuls un problème de fractions, les élèves qui reçoivent des solutions erronées typiques avec la consigne de les comparer à la solution correcte apprennent plus que ceux qui reçoivent seulement des solutions correctes, ou des solutions erronées sans consigne ; sans consigne, presque personne ne regarde les erreurs.

## La source

| | |
| --- | --- |
| **Équipe** | École supérieure de pédagogie de Fribourg-en-Brisgau (didactique des mathématiques) ; Loibl travaille sur l'« échec productif » (problème avant le cours). |
| **Nature** | Académique ; financement de la Deutsche Forschungsgemeinschaft (p. 9). |
| **Support** | *Learning and Instruction* (Elsevier, EARLI). |
| **Audience** | 116 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : matériel issu d'un projet public (KOSIMA), procédure et codage décrits (p. 3-5) ; données non publiées. |

## Ce que fait l'étude

- **Participants** (p. 3) : 200 élèves de neuf classes, tirés au sort individuellement entre trois groupes ; effectif calculé a priori.
- **Déroulement** (p. 4) : séance d'introduction commune ; puis 25 min de recherche d'un problème (quelle équipe de lancers a le mieux réussi ?), sans cours préalable ; puis 20 min d'étude selon le groupe.
- **Groupes** (tableau 1, p. 4) : solutions correctes seules ; solutions correctes et tentatives erronées typiques ; même chose avec consignes de comparaison par paires (« Qu'a fait Till de faux ? Qu'a fait Ole de mieux ? »). Les tentatives erronées sont marquées comme fausses dans les deux groupes qui les reçoivent (p. 4).
- **Mesures** : post-test conceptuel et procédural, type de tentative initiale de chaque élève, réponses écrites pendant l'étude.

## Résultats

- **Post-test** (p. 6) : le groupe avec consignes fait mieux que le groupe « solutions correctes » (d = 0,53) et que le groupe « erreurs sans consigne » (d = 0,32) ; ces deux derniers ne diffèrent pas.
- **Selon la tentative initiale** (p. 7) : l'avantage des consignes n'existe que pour les élèves dont la tentative contenait l'erreur typique montrée (d = 0,87) ; ils rejoignent alors ceux qui avaient déjà trouvé l'idée juste.
- **Processus** (p. 7) : sans consigne, 6 élèves sur 64 évoquent les tentatives erronées et 2 identifient une erreur ; avec consigne, 67 sur 68 les évoquent et 56 identifient une erreur. Identifier l'erreur est lié au résultat au post-test.

## Avis critique

**Apport.** Montre que montrer des erreurs ne suffit pas : il faut une consigne qui oblige à les comparer à la solution correcte, et l'effet porte surtout sur les élèves qui ont fait cette erreur.

**Points forts**
- Tirage au sort individuel, effet de classe vérifié et négligeable.
- Mesure des processus qui explique le résultat.
- Analyse selon la tentative initiale, cohérente avec la théorie du changement conceptuel.

**Réserves**
1. **Importante** — Élèves de 10-12 ans et une seule notion (fractions) ; une séance.
2. **Importante** — Comparaisons post-hoc unilatérales ; interaction globale condition × tentative non significative, analyse par sous-groupes.
3. **Mineure** — Limites peu discutées par les auteurs.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Des consignes de comparaison rendent utiles les exemples erronés | B | Essai randomisé, effet modéré, mécanisme mesuré, concordant avec Dieterich et al. (2025) |
| L'effet porte sur les élèves qui ont fait l'erreur | C | Analyse par sous-groupes |

**Transférabilité** : moyenne. Principe général (erreur typique contrastée avec la solution correcte), mais jeunes élèves et notion élémentaire.

**Pour conclure, il faudrait** comparer, dans ExoForge, l'affichage de l'erreur type correspondant à la réponse de l'étudiant, avec et sans consigne de comparaison.

## Pour Forge

- **ExoForge** : après une réponse fausse, afficher la solution erronée typique la plus proche de la réponse de l'étudiant à côté de la solution correcte, avec la consigne « en quoi diffèrent-elles ? où est l'erreur ? » (niveau C).
- **ExoForge** : ne pas afficher d'exemples erronés sans consigne de comparaison (niveau C).
