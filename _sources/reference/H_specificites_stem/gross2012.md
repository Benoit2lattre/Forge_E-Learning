---
cle: gross2012
reference: "Gross, S. P. et Dinehart, D. W. (2012). Identification of Common Student Errors in Solving Fundamental Mechanics Problems. 2012 ASEE Annual Conference & Exposition, article AC 2012-4442."
doi: 10.18260/1-2--21466
axe: [H2, H3]
type_etude: étude descriptive d'erreurs relevées en correction (1 493 copies de 28 problèmes, 1 011 erreurs codées), une université, cinq ans
public: étudiants de 2e année (cours de mécanique combinant statique et résistance des matériaux), Villanova University, États-Unis
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "classer chaque erreur prévue d'un exercice en trois familles (conceptuelle majeure, exécution, hors mécanique : calcul, unités, trigonométrie) et donner un retour de nature différente à chacune"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "prévoir des contrôles automatiques pour les erreurs hors mécanique (unité manquante ou fausse, sin et cos permutés, coordonnées x et y inversées) avant de conclure à une erreur de concept"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "dans les questions à réponse numérique de statique, générer les leurres à partir des erreurs d'exécution fréquentes : x et y permutés, mauvais bras de levier, sin et cos permutés, charge répartie mal réduite"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "restituer à chaque étudiant la répartition de ses erreurs par famille et lui proposer un exercice ciblé sur sa famille dominante"
    niveau: D
    transferabilite: forte
    note: "proposé par les auteurs, non testé ; annoncer la liste des erreurs types en classe n'a pas amélioré les quiz (p. 17)"
---

# Les erreurs des étudiants dans les problèmes de statique (Gross et Dinehart, 2012)

Gross, S. P. et Dinehart, D. W. (2012). Identification of Common Student Errors in Solving Fundamental Mechanics Problems. *2012 ASEE Annual Conference & Exposition*, article AC 2012-4442. [DOI](https://doi.org/10.18260/1-2--21466)

**En une phrase.** Sur près de 1 500 copies de quatre problèmes types de statique, la moitié des erreurs sont des erreurs d'exécution (bras de levier, x et y permutés), 38 % sont hors mécanique (calcul, unités, trigonométrie) et seulement 13 % sont conceptuelles ; un outil d'exercices doit donc distinguer ces familles avant de diagnostiquer une conception erronée.

## La source

| | |
| --- | --- |
| **Équipe** | Génie civil et environnement, Villanova University ; deux enseignants du cours étudié. |
| **Nature** | Académique ; aucun financement mentionné. Les auteurs analysent leur propre cours et leur propre grille de correction. |
| **Support** | Actes de la conférence annuelle de l'ASEE (relecture d'actes). Pages citées : numéros 25.709.N imprimés en bas de page, notés « p. N ». |
| **Audience** | 6 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : problèmes types, grilles et listes d'erreurs publiés (tableaux 1-8) ; codage par les seuls auteurs, sans accord inter-correcteurs ; données brutes non publiques. |

## Ce que fait l'étude

- **Contexte** (p. 4) : cours de 2e année, quiz de 10-15 min sur un acquis d'apprentissage, examens de 20-25 min par problème ; notation sur 10 avec une grille qui consigne chaque erreur de chaque étudiant (p. 4-5).
- **Barème** (p. 4-5) : 1 point (parfois 2) pour une erreur hors mécanique, 2-3 pour une erreur d'exécution, 3 ou plus pour une erreur conceptuelle majeure.
- **Corpus analysé** (p. 6) : 28 problèmes de 2007 à 2011 sur quatre thèmes (système de forces parallèles, centre de gravité d'une surface composée, treillis, équilibre d'un solide plan), 1 493 copies, 1 011 erreurs. Plus de 8 000 copies ont été codées au total (p. 5).

## Résultats

| Problème | Copies | Erreurs | Erreur la plus fréquente (n) |
| --- | --- | --- | --- |
| Forces parallèles (p. 6-7) | 500 | 263 | x et y permutés (53), mauvais bras de levier (51) |
| Centre de gravité (p. 8-10) | 415 | 209 | une valeur fausse pour une sous-surface (112) |
| Treillis (p. 11-12) | 279 | 263 | traction et compression inversées sur une barre (62) |
| Équilibre d'un solide (p. 13-15) | 299 | 276 | erreur de trigonométrie (73), diagramme du corps libre faux (42) |

- **Bilan** (p. 16-17, figure 11) : 49 % d'erreurs d'exécution, 38 % hors mécanique, 13 % conceptuelles majeures ; 758 copies sur 1 493 parfaites ; 12 % des copies à 6 sur 10 ou moins.
- **Variations** : les erreurs conceptuelles pèsent 6 % pour le centre de gravité (p. 8) et 19 % pour l'équilibre d'un solide, où 55 % des erreurs sont hors mécanique (figure 9, p. 16).
- **Usage pédagogique** (p. 17-18) : une fiche classant les erreurs passées est revue avant chaque quiz et les erreurs types sont signalées en cours ; les auteurs ne voient « pas encore d'amélioration significative » des quiz. Projet non réalisé : bilan individuel par famille d'erreurs et exercices de remédiation ciblés.

## Avis critique

**Apport.** Donne, pour quatre problèmes standard de statique, la liste chiffrée des erreurs réelles et leur répartition : c'est un catalogue directement utilisable pour écrire des leurres numériques et des retours ciblés.

**Points forts**
- Grand nombre de copies, sur cinq ans, avec une grille stable.
- Erreurs décrites concrètement et comptées par problème.
- Observation honnête : prévenir les étudiants des erreurs types ne suffit pas.

**Réserves**
1. **Importante** — La famille d'une erreur est fixée par les correcteurs, en lien avec le barème ; pas de définition opérationnelle ni d'accord entre correcteurs. La trigonométrie est classée hors mécanique, le diagramme du corps libre faux tantôt en exécution, tantôt en conceptuel.
2. **Importante** — Une seule université, deux enseignants ; 28 problèmes sur 150 analysés (p. 6, 16).
3. **Mineure** — Absence d'effet de la fiche d'erreurs : simple impression des auteurs, sans comparaison.
4. **Mineure** — Copies de quiz et d'examens mêlées, avec des enjeux et des préparations différents.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les erreurs conceptuelles sont minoritaires dans les problèmes de statique standard | C | Description d'un grand corpus, une seule université, codage non validé |
| Liste des erreurs d'exécution les plus fréquentes (bras de levier, x/y, trigonométrie, traction/compression) | C | Comptages précis, un seul contexte |
| Annoncer les erreurs types ne suffit pas à les éviter | D | Impression des auteurs, non mesurée |

**Transférabilité** : forte pour le catalogue (mêmes problèmes en L3), moyenne pour les proportions, qui dépendent du barème et des énoncés.

**Pour conclure, il faudrait** coder avec la même grille les réponses à un exercice de statique dans ExoForge, puis comparer un retour par famille d'erreur à un retour générique.

## Pour Forge

- **ExoForge** : trois familles d'erreurs avec des retours différents ; les contrôles hors mécanique (unités, x/y, sin/cos) passent avant le diagnostic conceptuel (niveau C).
- **QuizForge** : leurres numériques de statique tirés des tableaux 2, 4, 6 et 8 de l'article (niveau C).
- **DiagForge** : bilan individuel par famille d'erreurs, avec exercice ciblé ; à tester, car l'annonce des erreurs seule n'a pas suffi (niveau D).
- Renvois : `steif2005`, `steif2006` (erreurs conceptuelles en QCM) ; `tatsuoka1983` (des règles fausses qui donnent la bonne réponse) ; pistes de l'axe H (formules fausses nommées dans ExoForge).
