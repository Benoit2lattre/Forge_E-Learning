---
cle: rello2016
reference: "Rello, L. et Baeza-Yates, R. (2016). The effect of font type on screen readability by people with dyslexia. ACM Transactions on Accessible Computing, 8(4), article 15, 1-33."
doi: 10.1145/2897736
axe: [I1]
type_etude: expérience intra-sujets en laboratoire (oculométrie), 12 polices, groupe dyslexique et groupe témoin
public: 97 lecteurs hispanophones de 11 à 54 ans (48 dyslexiques diagnostiqués, 49 témoins), collégiens, lycéens et étudiants
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "pas d'énoncé ni de consigne en italique ; l'italique réservé à quelques mots (et aux variables mathématiques rendues par MathJax)"
    niveau: C
    transferabilite: moyenne
  - outil: QuizForge
    regle: "pas d'énoncé ni de consigne en italique ; l'italique réservé à quelques mots"
    niveau: C
    transferabilite: moyenne
  - outil: ExoForge
    regle: "texte courant en police sans empattement et romaine courante (Arial, Helvetica, Verdana) ; Computer Modern acceptable pour les formules"
    niveau: C
    transferabilite: moyenne
    note: "effet seulement sur la durée des fixations, pas sur le temps de lecture"
  - outil: QuizForge
    regle: "texte courant en police sans empattement et romaine courante (Arial, Helvetica, Verdana)"
    niveau: C
    transferabilite: moyenne
  - outil: ExoForge
    regle: "les mêmes réglages typographiques pour tous les étudiants : ce qui aide les dyslexiques n'a pas gêné les autres"
    niveau: C
    transferabilite: moyenne
---

# Choix de police à l'écran et dyslexie (Rello et Baeza-Yates, 2016)

Rello, L. et Baeza-Yates, R. (2016). The effect of font type on screen readability by people with dyslexia. *ACM Transactions on Accessible Computing*, 8(4), article 15, 1-33. [DOI](https://doi.org/10.1145/2897736)

**En une phrase.** Sur 12 polices lues à l'écran par 97 personnes, l'italique ralentit la lecture et les polices sans empattement, romaines ou à chasse fixe raccourcissent les fixations, mais sans différence de temps de lecture ; OpenDyslexic n'aide pas et déplaît : pour Forge, une police courante sans empattement et pas d'italique pour le texte suivi.

## La source

| | |
| --- | --- |
| **Équipe** | Groupe de recherche Web, université Pompeu Fabra (Barcelone) ; la première autrice était ensuite à Carnegie Mellon (p. 1). Informatique et interaction humain-machine. |
| **Nature** | Académique ; bourse catalane et financement du ministère espagnol de la Science (p. 1). Version longue d'un article de 2013 (ASSETS) auquel elle ajoute le groupe témoin (p. 2). Les auteurs ont intégré leurs recommandations dans des lecteurs qu'ils ont contribué à développer (p. 29). |
| **Support** | *ACM Transactions on Accessible Computing*, revue à comité de lecture. |
| **Audience** | 109 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : protocole, matériel et analyses décrits (p. 5-10) ; textes tirés d'un livre publié ; données non publiées. La démarche se refait ; les chiffres ne se vérifient pas. |

## Ce que fait l'étude

- **Participants** (p. 8-9, tableau I p. 6) : 48 dyslexiques diagnostiqués (11 à 50 ans, moyenne 21,0) et 49 témoins (11 à 54 ans, moyenne 29,2) ; scolaires, lycéens et étudiants.
- **Dispositif** (p. 5-10) : chacun lit 12 textes de 60 mots en espagnol, chacun dans une police (Arial, Arial italique, Computer Modern Unicode, Courier, Garamond, Helvetica, Myriad, OpenDyslexic et son italique, Times et son italique, Verdana), ordre contrebalancé ; corps 14 points, au plus 70 caractères par ligne, noir sur blanc ; séance d'environ 20 minutes.
- **Mesures** (p. 7-8) : temps de lecture, durée moyenne et nombre de fixations (oculomètre), préférence sur 5 points ; une question de compréhension littérale par texte, utilisée seulement pour écarter les lectures non comprises (10 sur 1 164, p. 11).
- **Analyse** (p. 10) : Friedman puis Wilcoxon avec correction de Bonferroni.

## Résultats

- **Polices une à une** (p. 12-14) : chez les dyslexiques, 3 comparaisons de temps de lecture sur 66 sont significatives, toutes contre Arial italique (plus lente qu'Arial, CMU et Helvetica) ; 16 sur 66 pour la durée des fixations (Courier, Helvetica, Arial plus courtes).
- **Italique** (p. 19-20) : chez les dyslexiques, fixations plus longues en italique (p = 0,040), temps de lecture non différent (p = 0,120) ; chez les témoins, temps de lecture plus long (p = 0,001). Les deux groupes préfèrent le romain (3,21 contre 2,73 chez les dyslexiques).
- **Avec ou sans empattement** (p. 20-21) : pas d'effet sur le temps de lecture (p = 0,199) ; fixations un peu plus courtes sans empattement (0,24 s contre 0,26 s chez les dyslexiques) ; seuls les dyslexiques préfèrent le sans empattement.
- **OpenDyslexic** (p. 22-23, 25) : aucun gain de temps de lecture (p = 0,197) ; fixations plus longues chez les témoins ; nettement moins appréciée (2,57 contre 3,60 sur 5 chez les dyslexiques).
- **Synthèse des auteurs** (tableau XI, p. 29) : recommandations « faibles » pour sans empattement et chasse fixe, car un seul indicateur sur trois (durée des fixations) est significatif.

## Avis critique

**Apport.** Mesure objective à l'écran d'un choix que tout générateur de page fait : la police. Montre qu'aucune police courante ne gêne vraiment, sauf l'italique, et que la police « dyslexie » n'apporte rien.

**Points forts**
- Douze polices réelles, plan intra-sujets contrebalancé, groupe témoin.
- Correction des comparaisons multiples (Bonferroni).
- Les auteurs qualifient eux-mêmes leurs recommandations de faibles (p. 24, 29).

**Réserves**
1. **Importante** — La mesure est la vitesse de lecture d'un paragraphe narratif de 60 mots ; la compréhension n'est qu'un filtre (une question littérale non validée, p. 28). Rien sur l'apprentissage ni sur un texte scientifique avec formules.
2. **Importante** — L'essentiel des différences porte sur la durée des fixations, pas sur le temps de lecture ; l'intérêt pratique d'une fixation plus courte de 0,02 s n'est pas établi.
3. **Mineure** — Chiffres difficiles à rapprocher : pour les témoins, moyennes du tableau II (11,8 à 17,2 s) inférieures aux médianes et à la moyenne globale annoncée (17,7 s, p. 11) ; un sens inversé dans le texte pour OpenDyslexic italique (p. 22).
4. **Mineure** — Groupes d'âges différents (21 contre 29 ans en moyenne, p. 27), texte en espagnol, écran de 1024 × 768 de 2005.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Un texte suivi en italique se lit moins bien et déplaît | C | Une expérience, effet sur une mesure par groupe, préférence nette |
| Sans empattement ou chasse fixe raccourcissent les fixations | C | Effet faible sur un seul indicateur |
| Aucune police courante en romain ne change le temps de lecture | C | Absence de différence dans une expérience de taille moyenne |
| OpenDyslexic n'aide pas et déplaît | C | Une expérience ; cohérent avec la méta-analyse [azzarello2026](azzarello2026.md) |

**Transférabilité** : moyenne. Lecteurs en partie étudiants et à l'écran ; mais textes narratifs courts, sans contenu scientifique.

**Pour conclure, il faudrait** mesurer dans ExoForge le temps passé sur l'énoncé et la réussite à la première étape selon deux polices (sans empattement contre CMU) tirées au hasard, chez des étudiants qui déclarent ou non une dyslexie.

## Pour Forge

- **ExoForge, QuizForge** : pas de paragraphe entier en italique (niveau C).
- **ExoForge, QuizForge** : police courante sans empattement pour le texte (Arial, Helvetica, Verdana) ; CMU, police par défaut de LaTeX et de MathJax, reste acceptable (niveau C).
- **ExoForge, QuizForge** : un seul réglage pour tous ; pas de police « dyslexie » (voir [azzarello2026](azzarello2026.md)).
- Cette étude ne fait varier ni la taille ni l'espacement (corps 14 fixe) : ces réglages relèvent de `rello2015` et `marinus2016` (priorité 2, non lus).
