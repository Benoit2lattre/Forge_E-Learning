---
cle: booth2013
reference: "Booth, J. L., Lange, K. E., Koedinger, K. R. et Newton, K. J. (2013). Using example problems to improve student learning in algebra: Differentiating between correct and incorrect examples. Learning and Instruction, 25, 24-34."
doi: 10.1016/j.learninstruc.2012.11.002
axe: [D3]
type_etude: deux expériences en classe avec répartition au hasard (116 et 64 élèves analysés), dans un système tutoriel intelligent
public: élèves de collège et de lycée en algèbre (équations à deux étapes), États-Unis
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "remplacer quelques exercices guidés par des exemples à expliquer (« qu'a-t-on fait ? pourquoi est-ce juste ou faux ? »)"
    niveau: C
    transferabilite: moyenne
  - outil: ExoForge
    regle: "inclure des exemples erronés, construits sur des erreurs types, en plus des exemples corrects, et demander d'expliquer l'erreur"
    niveau: C
    transferabilite: moyenne
---

# Exemples corrects et erronés dans un STI d'algèbre (Booth et al., 2013)

Booth, J. L., Lange, K. E., Koedinger, K. R. et Newton, K. J. (2013). Using example problems to improve student learning in algebra: Differentiating between correct and incorrect examples. *Learning and Instruction*, 25, 24-34. [DOI](https://doi.org/10.1016/j.learninstruc.2012.11.002)

**En une phrase.** Dans un système tutoriel intelligent (STI) d'algèbre utilisé en classe, remplacer quelques exercices guidés par des exemples à expliquer améliore la compréhension conceptuelle sans nuire à la résolution ; les exemples erronés (seuls ou avec des exemples corrects) font mieux que les exemples corrects seuls pour la compréhension, sans différence en résolution.

## La source

| | |
| --- | --- |
| **Équipe** | Université Temple (Booth, Newton) et Carnegie Mellon (Koedinger, premier auteur de l'article de référence sur le STI d'algèbre utilisé, cité p. 26). |
| **Nature** | Académique ; financement National Science Foundation (Pittsburgh Science of Learning Center) et ministère américain de l'Éducation (p. 32). Le STI utilisé est un produit commercial issu de l'équipe de Koedinger. |
| **Support** | *Learning and Instruction* (Elsevier, EARLI). |
| **Audience** | 238 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : interventions et tests décrits avec exemples d'items (p. 26-30) ; logiciel commercial, données non publiées. |

## Ce que fait l'étude

- **Expérience 1** (p. 26-28) : 134 élèves de neuf classes de lycée (116 analysés) travaillant l'unité « équations à deux étapes » du STI ; quatre groupes tirés au sort : STI seul, ou 8 exercices remplacés par des exemples corrects, erronés, ou les deux ; pour chaque exemple, expliquer ce qui a été fait et pourquoi c'est juste ou faux.
- **Expérience 2** (p. 29-30) : 64 élèves de 4e (8th grade), trois groupes d'exemples seulement (pas de groupe STI seul), 12 exemples ; tests plus fins de compréhension (repérer les caractéristiques conceptuelles d'une équation) et de résolution.

## Résultats

- **Exemples contre STI seul** (p. 28) : meilleure compréhension conceptuelle (63 % contre 58 %, η²p = 0,05) ; résolution identique malgré 8 exercices en moins (42 % contre 41 %) ; tendance en transfert (24 % contre 16 %, non significatif).
- **Types d'exemples, expérience 1** : pas de différence entre corrects, erronés et mélange.
- **Types d'exemples, expérience 2** (p. 30-31) : le mélange correct + erroné fait mieux que les corrects seuls sur les caractéristiques conceptuelles (72 % contre 53 %) ; les erronés seuls réduisent les erreurs de lecture des équations ; aucune différence en résolution.
- **Interprétation des auteurs** (p. 32) : les élèves voient de toute façon des solutions correctes (cours, STI) ; les exemples erronés apportent ce qui manque, à condition d'être expliqués.

## Avis critique

**Apport.** Montre, en conditions réelles de classe, que des exemples (y compris erronés) peuvent remplacer une partie de l'entraînement guidé et améliorer la compréhension sans coût en résolution.

**Points forts**
- Deux expériences en classe, tirage au sort individuel.
- Mesures séparées de compréhension et de procédure.
- Discussion nuancée des conditions d'usage des exemples erronés.

**Réserves**
1. **Importante** — Effets petits ou modestes ; résultats sur les types d'exemples non concordants entre les deux expériences.
2. **Importante** — Petits groupes à l'expérience 2 (21-22 élèves) et pas de groupe témoin sans exemples.
3. **Mineure** — Même version du test avant et après à l'expérience 2 ; conflit d'intérêt possible (STI de l'équipe).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Remplacer des exercices guidés par des exemples expliqués améliore la compréhension | B | Essai en classe, concordant avec la littérature |
| Les exemples erronés aident plus que les corrects seuls | C | Une expérience sur deux, petits groupes |

**Transférabilité** : moyenne. Algèbre élémentaire et élèves jeunes, mais le principe (expliquer pourquoi une étape est fausse) s'applique aux erreurs types de mécanique.

**Pour conclure, il faudrait** comparer, dans ExoForge, exemples corrects seuls et paires correct-erroné sur les mêmes notions de mécanique, avec une mesure conceptuelle.

## Pour Forge

- **ExoForge** : remplacer quelques exercices guidés d'une série par des exemples à expliquer (niveau C).
- **ExoForge** : construire des exemples erronés à partir des règles erronées (erreurs types) et demander de localiser et d'expliquer l'erreur (niveau C ; voir Große et Renkl, 2007, et Dieterich et al., 2025).
