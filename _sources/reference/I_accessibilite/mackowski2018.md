---
cle: mackowski2018
reference: "Maćkowski, M., Brzoza, P., Żabka, M. et Spinczyk, D. (2018). Multimedia platform for mathematics' interactive learning accessible to blind people. Multimedia Tools and Applications, 77, 6191-6208."
doi: 10.1007/s11042-017-4526-z
axe: [I2]
type_etude: rapport de conception (chaîne de production d'exercices à étapes depuis une source TeX) avec évaluation d'utilisabilité sans groupe témoin
public: 23 étudiants en situation de handicap (12 malvoyants, 7 aveugles, 4 avec handicap moteur des mains), université de technologie de Silésie
lecture: texte complet, 10/11/2026
regles:
  - outil: ExoForge
    regle: "décrire chaque exercice comme un graphe d'étapes (écrans, conditions de passage, erreur typique associée à chaque mauvaise réponse) dans une source texte unique, compilée en page web et en version accessible"
    niveau: D
    transferabilite: forte
    note: "langage de commandes TeX compilé en XML + JavaScript (p. 6194-6200) ; aucune mesure d'apprentissage"
  - outil: ExoForge
    regle: "ne jamais livrer une formule en image sans couche texte structurée ; préférer le MathML généré automatiquement aux descriptions rédigées à la main (2 à 5 h par exercice)"
    niveau: D
    transferabilite: forte
    note: "les formules y sont des images PNG (latex + dvipng) doublées d'une description écrite à la main (p. 6195, 6204)"
  - outil: QuizForge
    regle: "toute l'interaction (choix, champs, listes déroulantes, bouton suivant) doit se faire au clavier et être annoncée par le lecteur d'écran"
    niveau: C
    transferabilite: forte
    note: "92 % des 23 utilisateurs jugent l'ergonomie et l'accès au clavier bons (p. 6203), avis déclaré"
  - outil: DiagForge
    regle: "compter les erreurs par étape dans les traces et s'en servir pour proposer l'exercice suivant de même niveau ou plus difficile ; ne pas présenter cette progression comme une preuve d'efficacité sans groupe témoin"
    niveau: D
    transferabilite: moyenne
    note: "12 + 6 étudiants sur 23 font moins d'erreurs au fil des exercices, 5 sans progrès (p. 6203-6204), sans comparaison"
---

# Chaîne de production d'exercices de mathématiques accessibles (Maćkowski et al., 2018)

Maćkowski, M., Brzoza, P., Żabka, M. et Spinczyk, D. (2018). Multimedia platform for mathematics' interactive learning accessible to blind people. *Multimedia Tools and Applications*, 77, 6191-6208. [DOI](https://doi.org/10.1007/s11042-017-4526-z)

**En une phrase.** Les auteurs décrivent comment ils produisent, depuis une source TeX enrichie de commandes, des exercices de mathématiques à étapes (écrans, conditions, erreurs typiques) utilisables au lecteur d'écran ; 23 étudiants en situation de handicap jugent la plateforme utilisable, mais aucun effet sur l'apprentissage n'est démontré.

## La source

| | |
| --- | --- |
| **Équipe** | Facultés d'automatique et d'informatique, de mathématiques appliquées et de génie biomédical, université de technologie de Silésie (p. 6191) ; mêmes auteurs que [mackowski2017](mackowski2017.md). |
| **Nature** | Académique ; projet « Mathematics - interactive study of the future », financé par l'Union européenne (p. 6205). Les auteurs évaluent leur propre plateforme. |
| **Support** | *Multimedia Tools and Applications* (Springer), libre accès. |
| **Audience** | 43 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Moyenne pour la chaîne (langage de commandes, format XML et JSON décrits avec exemples, p. 6194-6200) ; faible pour l'évaluation (formulaires non publiés, résultats en pourcentages sans effectifs par question). La démarche se refait ; les chiffres ne se vérifient pas. |

## Ce que fait l'étude

- **Chaîne** (p. 6194-6200) : l'auteur d'un exercice écrit en TeX avec des commandes `\fm...` (écrans, tuiles, boutons, champs, `\fmGoTo` conditionnels) ; un programme C++ découpe les écrans en tuiles rendues en PNG (latex, dvipng), produit un fichier XML de structure (ordre des écrans, conditions de passage), un XML de descriptions textuelles des formules et un état JSON par étudiant (écran courant, nombre d'erreurs). Trois couches dans le navigateur : interaction, image, description alternative (p. 6199).
- **Descriptions** (p. 6200) : rédigées à la main en polonais selon des règles validées avec des mathématiciens et des enseignants d'élèves aveugles ; Speech Rule Engine écarté (anglais seulement, MathML seulement, instable alors).
- **Corpus** (p. 6201-6202) : environ 240 exercices, dont 60 avec la couche de description ; environ 1 000 étudiants et 40 étudiants en situation de handicap de six facultés.
- **Évaluation** (p. 6202-6204) : 23 étudiants ; avis sur la reconnaissance de la structure, la navigation et la compréhension des formules (bon, moyen, mauvais) ; ergonomie au clavier ; puis prétest, exercices sur la plateforme et suivi du nombre d'erreurs dans les traces.

## Résultats

- Reconnaissance de la structure déclarée : 75 % chez les aveugles, 93 % chez les malvoyants (p. 6203) ; difficulté proportionnelle à l'imbrication (fractions dans des fractions, parenthèses).
- Compréhension des formules simples et complexes : 73 à 90 % (p. 6203) ; formules avancées selon le niveau en mathématiques.
- Navigation : par formule et par mot surtout ; par caractère pour les longs nombres (p. 6203).
- Ergonomie et accès complet au clavier jugés bons par 92 % (p. 6203).
- Traces (p. 6203-6204) : 12 étudiants sur 23 font moins d'erreurs ; 6 aussi, mais après beaucoup plus d'exercices ; 5 sans progrès, niveau jugé insuffisant.
- Coût (p. 6204) : 2 à 10 h pour concevoir un exercice à étapes, 2 à 5 h pour ses descriptions vocales.

## Avis critique

**Apport.** Décrit une architecture très proche d'ExoForge (source texte, graphe d'étapes, erreurs typiques, état par étudiant) avec une couche d'accessibilité, et chiffre le coût de la description manuelle, qui plaide pour une génération automatique.

**Points forts**
- Chaîne de production décrite avec exemples de code et de fichiers.
- Exercices d'analyse du supérieur.
- Coûts de production rapportés.

**Réserves**
1. **Majeure** — Pas de groupe témoin ni de mesure d'apprentissage : la baisse des erreurs au fil des exercices (18 sur 23) peut venir de la pratique ou de l'adaptation de la difficulté, pas de l'accessibilité.
2. **Importante** — Pourcentages sans dénominateur (nombre de formules, de réponses) ; « 73-90 % » et « 92 % » sont des avis déclarés.
3. **Importante** — Formules en images doublées d'un texte rédigé à la main : approche datée, coûteuse, sans navigation dans la formule par le moteur ; contraire à la règle MathML de l'axe ([gaggi2026](gaggi2026.md)).
4. **Mineure** — Chiffres différents de [mackowski2017](mackowski2017.md) : 240 + 60 exercices ici, 300 dont environ 30 % adaptés dans mackowski2017 (p. 304).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Une plateforme d'exercices à étapes peut être rendue utilisable au clavier et au lecteur d'écran | C | 23 utilisateurs, avis déclarés, pas de critère objectif |
| L'imbrication des structures est la principale difficulté à l'oral | C | Concordant avec mackowski2017, frankel2017 |
| La plateforme améliore la résolution d'exercices | D | Traces sans comparaison |

**Transférabilité** : forte pour l'architecture, faible pour les chiffres (descriptions en polonais, outils de 2016).

**Pour conclure, il faudrait** comparer, sur les mêmes exercices ExoForge, des formules MathML lues par MathJax et des descriptions rédigées, en mesurant réussite et temps chez des étudiants au lecteur d'écran.

## Pour Forge

- **ExoForge** : source texte unique décrivant le graphe d'étapes et les erreurs typiques, compilée vers la page (niveau D) ; déjà le modèle d'ExoForge.
- **ExoForge** : pas de formule en image ; MathML généré plutôt que descriptions manuelles (niveau D).
- **QuizForge** : interaction complète au clavier, annoncée par le lecteur d'écran (niveau C).
- **DiagForge** : erreurs par étape dans les traces, sans les présenter comme preuve d'efficacité (niveau D).
- Renvois : [mackowski2017](mackowski2017.md), [gaggi2026](gaggi2026.md), [mcmillan2026](mcmillan2026.md).
