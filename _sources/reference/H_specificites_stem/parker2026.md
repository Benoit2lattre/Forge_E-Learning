---
cle: parker2026
reference: "Parker, M. J. et Zavala-Cerna, M. G. (2026). What don't you understand? Using large language models to identify and characterize student misconceptions about challenging topics. Education and Information Technologies, 31, 4705-4744."
doi: 10.1007/s10639-026-13902-8
axe: [H3, C]
type_etude: étude d'usage sur traces de quiz formatifs (trois cohortes par cours) et chaîne d'analyse par grand modèle de langage (LLM), évaluée par deux experts et dix entretiens d'enseignants
public: 2 069 étudiants de 1re et 2e année de médecine (3 802 inscriptions) d'une université mexicaine, 5 cours en ligne de sciences biomédicales, 2019-2023
lecture: texte complet, 10/11/2026
regles:
  - outil: DiagForge
    regle: "repérer les notions difficiles au niveau du quiz (moyenne des premières tentatives), et ne retenir que celles qui sont parmi les plus difficiles dans au moins deux cohortes et portent sur au moins deux questions"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "calculer difficulté et leurre le plus choisi sur la première tentative seulement quand le quiz permet plusieurs essais"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "proposer à l'enseignant des hypothèses d'erreur type rédigées par un LLM à partir de l'énoncé, de la clé, de la réponse fausse la plus fréquente et du support de cours, en sortie structurée (JSON), à valider avant tout usage auprès des étudiants"
    niveau: C
    transferabilite: moyenne
    note: "45 des 48 hypothèses jugées excellentes, mais par un seul expert par cours, co-auteur, sans comparaison avec les explications des étudiants"
  - outil: QuizForge
    regle: "brouillon de retour par leurre généré par LLM à partir de l'énoncé et du support de cours, relu par l'enseignant ; ne jamais publier un retour généré sans relecture"
    niveau: D
    transferabilite: moyenne
---

# Notions difficiles et erreurs types repérées par LLM (Parker et Zavala-Cerna, 2026)

Parker, M. J. et Zavala-Cerna, M. G. (2026). What don't you understand? Using large language models to identify and characterize student misconceptions about challenging topics. *Education and Information Technologies*, 31, 4705-4744. [DOI](https://doi.org/10.1007/s10639-026-13902-8)

**En une phrase.** Sur cinq cours en ligne de sciences biomédicales, les auteurs repèrent les notions durablement difficiles par la réussite aux quiz en première tentative, puis font rédiger par un LLM une hypothèse d'erreur type pour chaque question à partir de l'énoncé, de la réponse fausse la plus choisie et de la transcription de la vidéo ; 45 hypothèses sur 48 sont jugées excellentes par deux experts, ce qui en fait un outil d'aide à l'enseignant, pas une mesure validée des erreurs des étudiants.

## La source

| | |
| --- | --- |
| **Équipe** | Harvard Medical School (premier auteur, concepteur des cours en ligne) ; Universidad Autónoma de Guadalajara (Mexique) (p. 4744). |
| **Nature** | Académique ; pas de financement extérieur, pas de conflit déclaré (p. 4740-4741). Les deux experts qui évaluent les sorties du LLM sont les auteurs (p. 4719). |
| **Support** | *Education and Information Technologies* (Springer). |
| **Audience** | 1 citation (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Moyenne : invites (prompts), schéma de sortie et grille d'évaluation publiés en annexe ; modèles et réglages précisés (gpt-4o-2024-08-06, température 0,3) ; questions et données non publiques, sur demande (p. 4740). La chaîne se refait sur nos quiz ; les chiffres ne se vérifient pas. |

## Ce que fait l'étude

- **Données** (p. 4711-4713, tableaux 1-4) : 9 sessions de 5 cours (immunologie, génétique, biochimie, pharmacologie, physiologie), regroupées en trois cohortes d'au moins 200 inscriptions environ ; 39 à 43 quiz de 1 à 7 questions par cours ; 69 % de QCM, 16 % de cases à cocher ; deux essais par question avec explication.
- **Notions difficiles** (p. 4713-4714) : pour chaque cohorte, les 10 quiz de plus faible réussite en première tentative ; notion retenue si elle figure dans au moins 2 cohortes sur 3 et si le quiz compte au moins 2 questions. Classement vérifié par un modèle de Rasch pour l'immunologie : corrélation de Spearman 0,99 avec le classement par moyennes.
- **Hypothèses d'erreur** (p. 4716-4717) : pour chaque question retenue, le LLM reçoit l'énoncé, les options, la clé, l'explication, la réponse fausse la plus choisie en première tentative et la transcription de la vidéo (Whisper) ; il rend des erreurs types et leur justification en JSON.
- **Évaluation** (p. 4717-4719) : grille en trois niveaux (excellent, bon, faible) sur la plausibilité, l'exactitude, le lien avec la réponse fausse et la clarté ; un expert par cours, pour deux cours. Dix enseignants interrogés sur l'utilité de la liste des notions difficiles (p. 4714-4716).

## Résultats

- **Stabilité entre cohortes** (p. 4723) : selon le cours, 53 % à 100 % des notions repérées dans une cohorte le sont aussi dans au moins une autre. En immunologie, 7 notions et 28 questions retenues (tableau 8) ; réussite en première tentative de 47 % à 70 % pour les 10 quiz les plus difficiles de chaque cohorte (tableau 7).
- **Qualité jugée** (tableau 10, p. 4727) : immunologie, 25 sur 28 excellentes, 3 bonnes (manque de spécificité par rapport à la réponse fausse) ; physiologie, 20 sur 20 ; total 45 sur 48 (93,8 %), aucune faible.
- **Coût** (tableaux 5 et 6, p. 4722) : 263 203 jetons et 1,06 dollar pour l'ensemble des hypothèses des cinq cours.
- **Enseignants** (p. 4727-4729) : la liste des notions difficiles recoupe leurs observations en classe et leur paraît utile pour planifier.
- **Limites reconnues** (p. 4733-4734) : la réponse fausse la plus fréquente fournie au LLM l'ancre sur cette réponse et peut masquer des erreurs minoritaires ; une question mal rédigée peut être prise pour une erreur conceptuelle.

## Avis critique

**Apport.** Une chaîne complète et peu coûteuse pour passer des résultats de quiz à des hypothèses d'erreur rédigées, que l'enseignant relit. Le filtre « difficile dans plusieurs cohortes, sur plusieurs questions » est simple à reprendre dans DiagForge.

**Points forts**
- Grand volume de traces sur plusieurs années, avec un filtre de stabilité entre cohortes.
- Invites, réglages et grille publiés.
- Limites du LLM (ancrage, rédaction des questions) discutées par les auteurs.

**Réserves**
1. **Majeure** — Les hypothèses du LLM ne sont jamais comparées à ce que pensent réellement les étudiants (entretiens, explications écrites) : « excellente » veut dire plausible aux yeux d'un expert, pas exacte.
2. **Importante** — Un seul évaluateur par cours, co-auteur, sans accord entre juges ni comparaison avec des hypothèses rédigées par un enseignant ; 48 questions seulement sur deux cours.
3. **Importante** — Une seule réponse fausse par question est fournie : les erreurs types qui se répartissent sur plusieurs leurres ou plusieurs questions échappent à la méthode (comparer à [Segado et al., 2026](segado2026.md)).
4. **Mineure** — Médecine, savoirs déclaratifs et QCM ; pas de questions de calcul. Les entretiens d'enseignants portent sur la liste des notions, pas sur les hypothèses d'erreur.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les notions difficiles sont en partie stables d'une cohorte à l'autre | C | Description sur trois cohortes, cinq cours |
| Le classement par moyennes équivaut au classement de Rasch | C | Un cours |
| Le LLM produit des hypothèses d'erreur plausibles | C | Deux experts co-auteurs, 48 questions |
| Ces hypothèses correspondent aux erreurs réelles des étudiants | D | Non testé |

**Transférabilité** : moyenne. Le filtrage par quiz et la chaîne d'invite se transposent ; la qualité des hypothèses en mécanique, où l'erreur est souvent un calcul ou un schéma, n'est pas connue.

**Pour conclure, il faudrait** comparer, sur une banque QuizForge de mécanique, les hypothèses du LLM à des explications écrites d'étudiants (invite « explique ton choix », voir [Klingbeil et al., 2024](klingbeil2024.md)) et à des hypothèses d'enseignants, avec deux juges indépendants.

## Pour Forge

- **DiagForge** : notions difficiles = quiz de plus faible réussite en première tentative, stables sur au moins deux cohortes et au moins deux questions (niveau C) ; première tentative seule pour la difficulté et le leurre dominant (niveau C).
- **DiagForge** : hypothèses d'erreur type proposées par LLM (énoncé, clé, réponse fausse dominante, support de cours, sortie JSON), validées par l'enseignant (niveau C pour la plausibilité, D pour l'exactitude).
- **QuizForge** : brouillons de retours par leurre générés puis relus (niveau D).
- Complète la règle « part de chaque leurre par question » de [Steif et Hansen (2006)](steif2006.md).
