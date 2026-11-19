---
cle: mackowski2017
reference: "Mackowski, M. S., Brzoza, P. F. et Spinczyk, D. R. (2018). Tutoring math platform accessible for visually impaired people. Computers in Biology and Medicine, 95, 298-306 (en ligne 2017)."
doi: 10.1016/j.compbiomed.2017.06.003
axe: [I2]
type_etude: rapport de conception d'une plateforme d'exercices et étude croisée de compréhension déclarée des formules lues à voix haute (deux groupes de 10, rôles inversés)
public: 20 élèves et étudiants aveugles (8) ou malvoyants (12), 16-24 ans, Pologne ; plateforme utilisée à l'université de technologie de Silésie
lecture: texte complet, 10/11/2026
regles:
  - outil: ExoForge
    regle: "lecture vocale des formules avec des mots de structure qui ouvrent et ferment chaque bloc (« fraction, numérateur ... dénominateur ... fin de fraction », « puissance ... fin de puissance ») plutôt qu'une lecture linéaire ; vérifier que le moteur de lecture (MathJax) les produit"
    niveau: C
    transferabilite: moyenne
    note: "compréhension déclarée (bonne / mauvaise), médianes 80-90 % contre 50-80 % selon la complexité (tableau 1, p. 305) ; 20 participants"
  - outil: QuizForge
    regle: "dans les questions, formules lues avec des marqueurs de structure ; éviter les fractions imbriquées et les longues expressions à parenthèses multiples, ou les poser en plusieurs lignes"
    niveau: C
    transferabilite: moyenne
    note: "fractions imbriquées et parenthèses multiples = principales difficultés (p. 303)"
  - outil: ExoForge
    regle: "découper un exercice en étapes élémentaires vérifiées une à une, avec un retour prévu pour chaque erreur typique, pour qu'un étudiant au lecteur d'écran puisse le résoudre seul"
    niveau: D
    transferabilite: forte
    note: "dispositif décrit (p. 299-302), effet sur l'apprentissage non mesuré ; 2 à 10 h de préparation par exercice"
---

# Plateforme d'exercices de mathématiques pour étudiants aveugles (Mackowski et al., 2017)

Mackowski, M. S., Brzoza, P. F. et Spinczyk, D. R. (2018). Tutoring math platform accessible for visually impaired people. *Computers in Biology and Medicine*, 95, 298-306. [DOI](https://doi.org/10.1016/j.compbiomed.2017.06.003)

**En une phrase.** Une plateforme d'exercices d'analyse découpés en étapes vérifiées, avec des formules décrites à la voix par des règles qui marquent la structure (« fraction ... fin de fraction »), est utilisable par des étudiants aveugles ; ces descriptions structurées sont jugées mieux comprises qu'une description simple, surtout pour les formules complexes, mais la mesure est une compréhension déclarée par 20 participants.

## La source

| | |
| --- | --- |
| **Équipe** | Départements d'informatique et de génie biomédical, université de technologie de Silésie (Gliwice, Zabrze) ; travaux antérieurs de la même équipe sur les livres DAISY et le STI ForMath (p. 299). |
| **Nature** | Académique ; les auteurs évaluent leur propre plateforme. Financement non rapporté ; « no conflict of interest » (p. 306). |
| **Support** | *Computers in Biology and Medicine* (Elsevier), revue de génie biomédical, pas d'éducation. |
| **Audience** | 40 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Faible : règles de description et liste des formules en annexe en ligne (non lue), plateforme réservée à l'université (p. 299), données individuelles non publiées. La démarche se refait en partie ; les chiffres ne se vérifient pas. |

## Ce que fait l'étude

- **Plateforme** (p. 299-302) : un mathématicien prévoit les erreurs des étudiants, construit le graphe de résolution et un écran d'explication par erreur ; réponses par liste, champ de texte ou menu déroulant ; indices, rappels de théorie ; choix de l'exercice suivant selon l'historique (domaine, erreurs, temps, difficulté). Dérivées, intégrales, limites, suites. Préparation : 2 à 10 h par exercice, plus 2 à 5 h pour les descriptions vocales (60 exercices) (p. 299).
- **Descriptions** (p. 299-300) : rédigées à la main, faute de moteur automatique en polonais (Speech Rule Engine alors limité à l'anglais et au MathML) ; vocabulaire de structure (« fin de puissance », « fin de fraction »), lu par JAWS, Window-Eyes ou un agrandisseur à voix.
- **Évaluation** (p. 302-303) : 20 participants (8 aveugles, 12 malvoyants), tirés au sort en deux groupes de 10 ; un groupe écoute la description « simple », l'autre la description structurée, puis les rôles s'inversent sur l'autre moitié des formules. Trois séries : 20 formules simples, 20 complexes (fractions, racines, puissances imbriquées), 30 avancées (dérivées, intégrales, limites) ; pour chaque formule, compréhension « bonne » ou « mauvaise » déclarée par le participant. La description « simple » n'est pas définie.

## Résultats

| Médiane de formules comprises (tableau 1, p. 305) | Simples | Complexes | Avancées |
| --- | --- | --- | --- |
| Essai 1 : témoin / structurée | 80 % / 90 % | 55 % / 80 % | 50 % / 80 % |
| Essai 2 : témoin / structurée | 75 % / 90 % | 50 % / 85 % | 40 % / 85 % |

- Écart croissant avec la complexité (p. 304) ; tests de Wilcoxon, p = 0,0238, 0,0034 et 4,1 × 10⁻⁸ au premier essai (p. 303).
- Formules simples comprises à 89 % (fig. 6, p. 303) ; difficultés : longues expressions à parenthèses, fractions dans des fractions, que les étudiants relisent par petits morceaux plusieurs fois (p. 303).
- Formules avancées évaluées par 10 étudiants ayant suivi un cours de mathématiques à l'université ; quatre formules mal comprises, en partie faute de connaissances (p. 303).
- Usage (p. 304) : environ 1 000 étudiants de six facultés ; 300 exercices, dont environ 30 % adaptés.

## Avis critique

**Apport.** Un des rares travaux sur des exercices de niveau universitaire (analyse) rendus utilisables au lecteur d'écran, avec un principe de description vocale qui marque début et fin de chaque structure, et un coût de production chiffré.

**Points forts**
- Exercices d'analyse du supérieur, proches des nôtres.
- Plan croisé : chaque participant voit les deux descriptions.
- Coût de préparation rapporté (2 à 10 h, plus 2 à 5 h).

**Réserves**
1. **Majeure** — La mesure est une compréhension déclarée (« bonne » ou « mauvaise »), pas une tâche vérifiée (recopier, calculer) ; la condition témoin n'est pas décrite.
2. **Importante** — Unité d'analyse incohérente : avec 10 participants par groupe, un test de Wilcoxon ne peut pas descendre sous p ≈ 1,1 × 10⁻⁵ [calcul : 2 / C(20,10) = 2 / 184 756] ; le p de 4,1 × 10⁻⁸ suppose une autre unité (formules ?), non précisée.
3. **Importante** — Les formules avancées ne sont évaluées que par 10 étudiants (p. 303), alors que le tableau 1 donne un témoin et un groupe expérimental ; les colonnes « complexes, structurée » et « avancées, structurée » sont identiques aux deux essais (tableau 1).
4. **Mineure** — Effet sur l'apprentissage non mesuré : l'affirmation d'un meilleur accès aux diplômes (p. 304) n'est pas étayée. Les auteurs évaluent leur propre plateforme.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Une description vocale qui marque la structure est mieux comprise qu'une description simple | C | Plan croisé tiré au sort mais 20 participants, compréhension déclarée, témoin non défini |
| Fractions imbriquées et parenthèses multiples sont les principales difficultés à l'oral | C | Observations concordantes avec frankel2017 et gaggi2026 |
| Le découpage en étapes vérifiées aide les étudiants aveugles à apprendre | D | Dispositif décrit, non évalué |

**Transférabilité** : moyenne. Le principe (marqueurs de structure) est celui des moteurs actuels (MathJax, ClearSpeak) ; les descriptions sont en polonais et rédigées à la main.

**Pour conclure, il faudrait** faire recopier ou calculer des formules de mécanique entendues avec la lecture MathJax (avec et sans marqueurs de structure) par des étudiants au lecteur d'écran, et noter la réussite plutôt que l'avis.

## Pour Forge

- **ExoForge** : vérifier que la lecture vocale MathJax des formules annonce début et fin des fractions, puissances et racines (niveau C).
- **QuizForge** : éviter fractions imbriquées et longues expressions parenthésées dans les énoncés, ou les découper (niveau C).
- **ExoForge** : étapes élémentaires vérifiées une à une, avec retour par erreur prévue (niveau D) ; c'est déjà le principe des exercices à étapes.
- Renvois : [mackowski2018](mackowski2018.md) (même plateforme, architecture), [frankel2017](frankel2017.md) (longues expressions mal réussies à l'oral), [gaggi2026](gaggi2026.md) (erreurs sur la portée des racines).
