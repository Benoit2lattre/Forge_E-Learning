---
cle: grosse2007
reference: "Große, C. S. et Renkl, A. (2007). Finding and fixing errors in worked examples: Can this foster learning outcomes? Learning and Instruction, 17(6), 612-634."
doi: 10.1016/j.learninstruc.2007.09.008
axe: [D3]
type_etude: deux expériences en laboratoire avec répartition au hasard (118 et 39 étudiants), avec pensée à voix haute dans la seconde
public: étudiants de l'université de Fribourg-en-Brisgau (surtout psychologie), problèmes de probabilités
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "réserver les exemples erronés aux étudiants qui ont déjà des bases sur la notion ; donner aux débutants des exemples corrects"
    niveau: C
    transferabilite: moyenne
  - outil: ExoForge
    regle: "si un débutant reçoit un exemple erroné, signaler l'étape fausse"
    niveau: C
    transferabilite: moyenne
  - outil: ExoForge
    regle: "demander d'expliquer l'erreur en citant le principe violé, puis montrer la solution correcte pour comparaison"
    niveau: D
    transferabilite: moyenne
    note: "mesure proposée par les auteurs, non testée"
---

# Trouver et corriger les erreurs d'un exemple (Große et Renkl, 2007)

Große, C. S. et Renkl, A. (2007). Finding and fixing errors in worked examples: Can this foster learning outcomes? *Learning and Instruction*, 17(6), 612-634. [DOI](https://doi.org/10.1016/j.learninstruc.2007.09.008)

**En une phrase.** Mêler des solutions erronées aux exemples résolus améliore le transfert lointain des étudiants qui ont de bonnes bases, mais le dégrade pour les plus faibles ; signaler l'erreur aide les plus faibles en transfert proche ; et les erreurs font produire des explications sur l'erreur au détriment des explications fondées sur le principe.

## La source

| | |
| --- | --- |
| **Équipe** | Psychologie de l'éducation, université de Fribourg-en-Brisgau (Renkl, spécialiste des exemples résolus). |
| **Nature** | Académique ; financement de la Deutsche Forschungsgemeinschaft (p. 612). |
| **Support** | *Learning and Instruction* (Elsevier, EARLI). |
| **Audience** | 342 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Bonne pour le matériel : tous les exemples et problèmes en annexe ; données non publiées. |

## Ce que fait l'étude

- **Matériel** (p. 616-617) : 8 exemples résolus de probabilités, organisés pour distinguer « l'ordre compte » et « l'ordre ne compte pas » ; dans les versions avec erreurs, la moitié des exemples contient une étape fausse à repérer et corriger.
- **Expérience 1** (p. 616-618) : 118 étudiants, plan 3 × 2 : exemples corrects seuls, corrects et erronés avec erreur signalée, ou sans signalement ; avec ou sans consignes d'auto-explication écrite.
- **Expérience 2** (p. 622-623) : 39 étudiants, exemples corrects seuls ou corrects et erronés (erreur non signalée), avec pensée à voix haute codée.
- **Mesures** : transfert proche et lointain ; niveau préalable traité comme variable continue.

## Résultats

- **Effet moyen** : aucun effet global des exemples erronés ni des consignes d'auto-explication (p. 618-619).
- **Interaction avec le niveau** (p. 619, 624) : en transfert lointain, les exemples erronés profitent aux étudiants du quart supérieur et nuisent à ceux du quart inférieur ; même résultat aux deux expériences (η² = 0,05 puis 0,15).
- **Signalement de l'erreur** (p. 619-620) : en transfert proche, il aide les étudiants faibles (interaction η² = 0,06), sans effet pour les forts ni en transfert lointain.
- **Processus** (p. 624-626) : avec erreurs, plus de mots, plus d'impasses et des explications propres à l'erreur (erreur trouvée dans 66 % des cas), mais moins d'explications fondées sur le principe ; charge utile ressentie plus élevée.

## Avis critique

**Apport.** Étude fondatrice sur les exemples erronés : elle montre que leur intérêt dépend du niveau de l'apprenant et qu'ils déplacent l'attention du principe vers l'erreur.

**Points forts**
- Interaction répliquée dans deux expériences.
- Analyse des processus par pensée à voix haute.
- Matériel complet publié.

**Réserves**
1. **Importante** — Interactions établies sur des sous-groupes extrêmes très petits (4 à 19 étudiants) ; tests unilatéraux à l'expérience 2.
2. **Importante** — Étudiants surtout en psychologie, tâche courte en laboratoire.
3. **Mineure** — Pas de solution correcte ni de retour après les exemples erronés, ordre fixe sans retour en arrière (reconnu p. 628) ; consignes d'auto-explication sans effet, contrairement à beaucoup d'autres études.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les exemples erronés aident les avancés et nuisent aux débutants | C | Interaction répliquée, petits sous-groupes |
| Signaler l'erreur aide les débutants | C | Une expérience, transfert proche seulement |
| Les erreurs réduisent les explications fondées sur le principe | C | Une expérience en pensée à voix haute, 39 étudiants |

**Transférabilité** : moyenne. Problèmes de calcul fondés sur un principe ; étudiants non scientifiques et tâche courte.

**Pour conclure, il faudrait** proposer, dans ExoForge, des exemples erronés selon le niveau mesuré et vérifier l'interaction sur un exercice de mécanique.

## Pour Forge

- **ExoForge** : exemples erronés pour les étudiants qui réussissent déjà les exercices de base, exemples corrects pour les autres (niveau C ; voir Dieterich et al., 2025).
- **ExoForge** : pour un débutant, indiquer l'étape fausse (niveau C).
- **ExoForge** : faire expliquer l'erreur par le principe violé, puis afficher la solution correcte (niveau D ; pistes proposées par les auteurs p. 627-628).
