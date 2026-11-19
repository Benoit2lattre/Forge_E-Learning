---
cle: frankel2017
reference: "Frankel, L., Brownstein, B. et Soiffer, N. (2017). Expanding audio access to mathematics expressions by students with visual impairments via MathML. ETS Research Report Series, 2017(1), rapport RR-17-13. Educational Testing Service."
doi: 10.1002/ets2.12132
axe: [I2]
type_etude: étude pilote intra-sujet (lecture vocale contre braille ou imprimé, ordre tiré au sort) et pilote d'utilisabilité de l'outil auteur
public: 21 lycéens aveugles ou malvoyants (15-19 ans, niveau Algèbre 1) ; 12 enseignants (10 de mathématiques, 2 spécialisés)
lecture: texte complet, 10/11/2026
regles:
  - outil: ExoForge
    regle: "formules en MathML lues par un moteur de parole mathématique avec navigation au clavier dans la formule (flèches pour avancer, zoom pour changer la taille des morceaux) ; ne pas se contenter d'un texte de remplacement figé"
    niveau: C
    transferabilite: moyenne
    note: "réussite équivalente au braille ou à l'imprimé (0,762 contre 0,756 par question), 21 lycéens, tâches d'algèbre de base"
  - outil: QuizForge
    regle: "formules en MathML lisibles et navigables au lecteur d'écran dans les questions, la lecture vocale navigable pouvant remplacer une version braille ou agrandie pour des calculs d'algèbre"
    niveau: C
    transferabilite: moyenne
  - outil: ExoForge
    regle: "corriger une lecture vocale incorrecte par les réglages de lecture du moteur (préférences) plutôt qu'en imposant un texte parlé pour toute la formule, qui casse la navigation"
    niveau: D
    transferabilite: forte
    note: "recommandation des auteurs (p. 13, 18), non mesurée"
  - outil: ExoForge
    regle: "éviter de faire lire à l'oral une longue expression à nombreux termes : la découper ou la poser en plusieurs étapes"
    niveau: D
    transferabilite: moyenne
    note: "une seule paire de questions (simplification à 9 termes) : 9 bonnes réponses sur 21 à l'oral contre 15 sur 21 en braille ou imprimé (tableau 4)"
---

# Lecture vocale navigable des formules en MathML (Frankel et al., 2017)

Frankel, L., Brownstein, B. et Soiffer, N. (2017). Expanding audio access to mathematics expressions by students with visual impairments via MathML. *ETS Research Report Series*, rapport RR-17-13. [DOI](https://doi.org/10.1002/ets2.12132)

**En une phrase.** Avec des formules en MathML lues par un moteur de parole mathématique (ClearSpeak dans MathPlayer, avec NVDA) et navigables au clavier, 21 lycéens aveugles ou malvoyants réussissent des questions d'algèbre aussi bien qu'en braille ou en gros caractères (0,76 de réussite par question dans les deux cas), et 12 enseignants apprennent en un tutoriel à produire des formules qui se lisent correctement : pour ExoForge et QuizForge, la lecture vocale navigable est une voie d'accès crédible, à condition d'un vrai moteur de lecture.

## La source

| | |
| --- | --- |
| **Équipe** | Educational Testing Service (Princeton) pour les deux premières autrices ; Design Science (Long Beach), éditeur de MathType et MathPlayer, pour le troisième auteur (p. 1). Suite de rapports antérieurs de la même équipe sur le style ClearSpeak (p. 2). |
| **Nature** | Financement public : Institute of Education Sciences, ministère américain de l'Éducation, subvention R324A110355 (p. 2, 22). Les auteurs évaluent leurs propres outils ; l'un d'eux appartient à l'entreprise qui les commercialise (déclaration de conflit d'intérêts non rapportée). Participants rémunérés (125 dollars en bons d'achat, p. 4, 15). |
| **Support** | Série de rapports de recherche d'ETS, relecture interne par ETS (page de garde) ; pas une revue externe. |
| **Audience** | 13 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Bonne pour le matériel : instruments de mathématiques, questionnaires et tâches des enseignants en annexes A à D ; données individuelles par élève et par question publiées (tableaux 4 et 5, p. 9-10). Les logiciels de 2015 ont évolué. La démarche se refait ; les chiffres se vérifient (moyennes recalculées ci-dessous). |

## Ce que fait l'étude

- **Outil** (p. 3, 12-14) : formules saisies dans Word avec MathType (MathML sous-jacent), lues par MathPlayer avec le style ClearSpeak et NVDA ; navigation au clavier : flèches pour avancer par morceaux, zoom avant ou arrière pour changer la taille des morceaux, trois modes (caractère, simple, enrichi), signets, « où suis-je », mode « décrire » (« fraction plus fraction »).
- **Élèves** (p. 3-8) : 21 lycéens (tableau 1 : 7 aveugles, 14 malvoyants ; 15-19 ans), 17 avaient déjà participé à l'étude de mise au point de la navigation (p. 4). Chacun fait deux versions parallèles de 16 questions (clones), l'une à l'oral, l'autre dans son format habituel (13 imprimé ou agrandi, 8 braille) ; ordre tiré au sort (groupes de 10 et 11, tableau 2, p. 6) ; tutoriel de navigation avant la partie orale.
- **Tâches** (p. 7, annexe A) : compter les zéros après la virgule, identifier termes et degré d'un polynôme, réduire une expression, calculer une expression avec parenthèses, simplifier une fraction rationnelle, simplifier des puissances. Questionnaires de préférence et de facilité.
- **Enseignants** (p. 12-19) : 12 enseignants saisissent 11 formules et doivent obtenir une lecture imposée, à l'aide des préférences de lecture ou, en dernier recours, d'un texte parlé imposé (« exact speech »).

## Résultats

- **Réussite** (tableaux 4 à 6, p. 8-10) : moyenne par question 0,762 à l'oral contre 0,756 dans le format habituel ; aveugles 0,741 à l'oral contre 0,750 en braille ; malvoyants 0,772 contre 0,760 en imprimé. Soit 256 contre 254 bonnes réponses sur 336 [calcul : somme des colonnes du tableau 4]. Pour chaque élève, l'écart entre les deux versions est d'au plus 2 questions sur 16 (tableau 5).
- **Par question** (tableau 4, p. 9) : score net moyen 0,125 (écart-type 2,73) ; deux écarts nets de 6 élèves : réduction d'une expression à 9 termes (3.2) moins bien réussie à l'oral (9 contre 15 sur 21) ; expression à parenthèses imbriquées (4.3) mieux réussie à l'oral (13 contre 7).
- **Préférences** (tableau 7, p. 11) : 2 élèves (10 %) préfèrent toujours leur format habituel ; 8 (38 %) le préfèrent mais acceptent l'oral ; 7 (33 %) indifférents ; 1 (5 %) préfère toujours l'oral ; 3 (14 %) veulent combiner les deux.
- **Facilité** (tableau 8, p. 11) : oral « très facile » pour 9 sur 21 et « plutôt facile » pour 12 ; imprimé « très facile » pour 11 sur 13 ; braille « très facile » pour 6 sur 8.
- **Navigation** (tableau 10, p. 12, n = 20) : flèches et zoom rendent l'oral « beaucoup plus facile » pour 14 élèves, changement de mode pour 13 ; « où suis-je » et « décrire » jugés sans effet par 9 et 12 élèves.
- **Enseignants** (tableaux 18 et 19, p. 20) : 7 sur 12 obtiennent la bonne lecture pour les 11 formules, le plus faible 7 sur 11 ; 3 sur 12 saisissent les 11 formules de la façon recommandée ; 11 sur 12 jugent la tâche facile ; 12 sur 12 jugent le tutoriel « très utile » (p. 19). Erreur la plus fréquente : texte parlé imposé pour toute la formule (p. 19).

## Avis critique

**Apport.** Seule étude de l'axe qui compare, chez les mêmes élèves et sur des questions parallèles, la lecture vocale navigable des formules au braille et à l'imprimé, avec les données par élève. Elle donne aussi le mode d'emploi côté auteur : rédiger en MathML, corriger par préférences, écouter.

**Points forts**
- Plan intra-sujet avec ordre tiré au sort et formes parallèles relues par des experts.
- Données brutes publiées, cohérentes avec les moyennes annoncées [calcul].
- Volet enseignants : la production par des non-spécialistes est testée, pas seulement la lecture.
- Limites reconnues par les auteurs (p. 21).

**Réserves**
1. **Majeure** — L'équivalence n'est pas démontrée : 21 élèves, analyse descriptive seulement (p. 8), pas d'intervalle de confiance ; plusieurs questions sont réussies par 19 à 21 élèves dans les deux formats (effet plafond, tableau 4). « Pas de différence visible » ne veut pas dire « équivalent ».
2. **Importante** — Conflit d'intérêts : un auteur travaille pour l'éditeur des logiciels évalués (p. 1) ; 17 élèves sur 21 connaissaient déjà l'outil (p. 4).
3. **Importante** — Public éloigné : lycéens, algèbre de base, une seule séance ; rien sur les dérivées, intégrales, vecteurs ou matrices. Les auteurs renvoient le calcul différentiel à des travaux futurs (p. 22).
4. **Mineure** — Répartition aveugles / malvoyants différente entre le tableau 1 (7 et 14, p. 4) et le tableau 6 (8 et 13, p. 10).
5. **Mineure** — Les élèves braille n'avaient pas d'afficheur braille couplé à la voix (p. 21) : la combinaison voix + braille, la plus prometteuse, n'est pas testée.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| La lecture vocale navigable d'un MathML donne une réussite proche du braille ou de l'imprimé sur l'algèbre de base | C | Plan intra-sujet randomisé mais 21 élèves, descriptif, plafond, auteurs liés à l'éditeur |
| Flèches et zoom sont les fonctions de navigation utiles ; « où suis-je » et « décrire » peu utiles | C | Avis déclarés de 20 élèves après usage |
| Des enseignants non spécialistes produisent des formules qui se lisent correctement après un tutoriel | C | 12 enseignants, tâche imposée, matériel du concepteur |
| La lecture orale gêne pour les longues expressions | D | Une seule paire de questions |

**Transférabilité** : moyenne. Le mécanisme (MathML + moteur de parole + navigation) est celui de MathJax aujourd'hui ; la valeur chiffrée vient de lycéens sur de l'algèbre simple, en anglais.

**Pour conclure, il faudrait** refaire la comparaison avec des formules de mécanique (dérivées partielles, vecteurs, intégrales) rendues par MathJax 4 dans ExoForge, en français, auprès d'étudiants utilisant un lecteur d'écran, avec un nombre de questions suffisant pour estimer un intervalle autour de l'écart.

## Pour Forge

- **ExoForge, QuizForge** : MathML lu par un moteur de parole mathématique avec navigation au clavier (flèches, zoom) ; c'est ce que fournit l'exploration de MathJax (niveau C).
- **ExoForge** : corriger une lecture fautive par les réglages du moteur, pas par un texte parlé imposé sur toute la formule (niveau D).
- **ExoForge** : découper les longues expressions à lire à l'oral (niveau D).
- Renvois : [gaggi2026](gaggi2026.md) (même principe avec MathJax 4, adultes), [chauhan2019](chauhan2019.md) (lecture sans moteur mathématique : inutilisable), [mackowski2017](mackowski2017.md) (descriptions structurées).
