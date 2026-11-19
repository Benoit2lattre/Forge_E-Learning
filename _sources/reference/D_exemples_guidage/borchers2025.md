---
cle: borchers2025
reference: "Borchers, C., Fleischer, H., Schanze, S., Scheiter, K. et Aleven, V. (2025). High scaffolding of an unfamiliar strategy improves conceptual learning but reduces enjoyment compared to low scaffolding and strategy freedom. Computers & Education, 236, article 105364."
doi: 10.1016/j.compedu.2025.105364
axe: [D2]
type_etude: expérience en plan croisé (61 étudiants), deux systèmes tutoriels intelligents comparés
public: étudiants de première année en cours de remise à niveau de chimie (stœchiométrie), Allemagne
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "faire saisir explicitement les étapes porteuses de sens (unités, grandeurs, substances) au lieu de ne vérifier que le résultat final"
    niveau: C
    transferabilite: moyenne
  - outil: ExoForge
    regle: "ne pas juger un exercice sur la préférence des étudiants : un guidage plus contraignant peut être moins apprécié et mieux faire apprendre"
    niveau: C
    transferabilite: forte
---

# Guidage fort ou liberté de stratégie ? (Borchers et al., 2025)

Borchers, C., Fleischer, H., Schanze, S., Scheiter, K. et Aleven, V. (2025). High scaffolding of an unfamiliar strategy improves conceptual learning but reduces enjoyment compared to low scaffolding and strategy freedom. *Computers & Education*, 236, article 105364. [DOI](https://doi.org/10.1016/j.compedu.2025.105364)

**En une phrase.** Chez 61 étudiants allemands, un système tutoriel intelligent qui impose une méthode inconnue d'eux et fait saisir chaque unité et chaque substance améliore la compréhension conceptuelle, contrairement à un système qui laisse libre la stratégie et ne vérifie que les valeurs ; les deux font progresser en calcul, et les étudiants préfèrent nettement le second.

## La source

| | |
| --- | --- |
| **Équipe** | Institut d'interaction homme-machine de Carnegie Mellon (Borchers, Aleven), didactique de la chimie à Hanovre, psychologie de l'éducation à Potsdam. |
| **Nature** | Académique ; financement d'une fondation (Joachim Herz Stiftung) via une bourse de la quatrième autrice. |
| **Support** | *Computers & Education* (Elsevier), libre accès. |
| **Audience** | 24 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Faible pour les données (non partageables, règles de protection des données) ; procédure et traduction des systèmes décrites (§ 3, annexe A). Les références renvoient aux sections. |

## Ce que fait l'étude

- **Participants** (§ 3.1) : 61 étudiants de première année (surtout biologie, biotechnologie végétale, chimie) dans un cours facultatif de remise à niveau avant le semestre.
- **Deux systèmes** (§ 3.2) : StoichTutor, guidage fort (méthode des facteurs de conversion, non enseignée en Allemagne ; unité et substance demandées à chaque étape ; rétroaction explicative) ; ORCCA, liberté de stratégie (seul le résultat compte, unités facultatives, rétroaction surtout de correction).
- **Plan** (§ 3.3, 3.5) : plan croisé ; chaque étudiant travaille une unité avec chaque système, dans un ordre tiré au sort ; jusqu'à 60 min et 7 problèmes par unité ; tests de calcul et tests conceptuels avant, entre et après.
- **Mesures** : gains en procédure et en compréhension, sentiment d'efficacité, utilisabilité et goût pour l'exercice.

## Résultats

- **Procédure** (§ 4.1) : progrès avec les deux systèmes, sans différence (d = 0,38 avec StoichTutor, 0,55 avec ORCCA).
- **Compréhension** (§ 4.1) : progrès seulement avec StoichTutor (d = 0,42 contre 0,10 ; F(1, 59) = 6,47, p = 0,014) ; gain moyen modeste (7 points de pourcentage).
- **Ordre** (§ 4.2) : pas d'effet de l'ordre des deux systèmes.
- **Préférences** (§ 4.3) : ORCCA jugé plus utilisable (3,12 contre 2,40 sur 5) et plus agréable ; le sentiment d'efficacité progresse autant avec les deux.
- **Traces** (§ 4.4) : avec ORCCA, les étudiants indiquent une unité 2 fois en moyenne et une substance 0,6 fois, contre environ 22 fois chacune avec StoichTutor ; les écarts de compréhension portent justement sur les unités et les substances.

## Avis critique

**Apport.** Montre qu'un système qui ne vérifie que le résultat numérique laisse les étudiants sauter les étapes qui portent le sens physique, et qu'ils apprennent alors moins de concepts, tout en préférant cette liberté.

**Points forts**
- Plan croisé avec tirage au sort et ordre contrebalancé.
- Explication du résultat par les traces d'usage (étapes réellement saisies).
- Contexte réel de cours, limites énoncées (§ 5.5).

**Réserves**
1. **Importante** — Les deux systèmes diffèrent sur plusieurs points à la fois (méthode, saisie des unités, rétroaction explicative, interface) : on ne sait pas lequel produit l'effet.
2. **Importante** — Petit échantillon de volontaires (61), séances courtes ; gain conceptuel faible en valeur absolue.
3. **Mineure** — Tests construits pour l'étude, données non partagées.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Faire saisir unités et grandeurs améliore la compréhension | C | Une expérience, facteurs confondus, mécanisme appuyé par les traces |
| Les étudiants préfèrent le système qui les fait moins apprendre | B | Écart net et cohérent avec d'autres travaux |

**Transférabilité** : moyenne. La situation (calcul avec unités et grandeurs) est très proche de la mécanique ; le public est en première année.

**Pour conclure, il faudrait** comparer, dans ExoForge, un même exercice avec et sans saisie obligatoire des unités et des grandeurs intermédiaires, à rétroaction identique.

## Pour Forge

- **ExoForge** : demander l'unité et la grandeur physique de chaque résultat intermédiaire, pas seulement la valeur finale (niveau C).
- **ExoForge** et **DiagForge** : ne pas utiliser la satisfaction des étudiants comme critère principal de qualité d'un exercice (niveau C).
