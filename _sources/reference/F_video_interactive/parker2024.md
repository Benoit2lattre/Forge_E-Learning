---
cle: parker2024
reference: "Parker, M. J., Bunch, M. et Pike, A. (2024). Is anybody watching: A multi-factor motivational framework for educational video engagement. Computers & Education, 222, article 105148."
doi: 10.1016/j.compedu.2024.105148
axe: [F2]
type_etude: étude d'usage à grande échelle (3,1 millions de vues, 1 117 vidéos, 16 cours en ligne payants), statistiques descriptives et régressions prédictives
public: apprenants de cours en ligne payants en sciences biomédicales (Harvard Medical School, HMX), 2018-2023 ; effectif d'apprenants donné seulement en annexe en ligne
lecture: texte complet, 09/11/2026
regles:
  - outil: CapsuleForge
    regle: "capsule à voir d'une traite (préparation d'une séance) : rester sous 6 min ; capsule de cours ou de révision : jusqu'à 12-15 min acceptable si elle est découpée en chapitres et reliée à des questions notées"
    niveau: C
    transferabilite: moyenne
    note: "au-delà de 6-9 min, le quart le moins assidu voit moins de 75 % puis moins de 50 % de la vidéo en une session ; le temps total par apprenant augmente pourtant avec la durée ; 3 vidéos seulement entre 12 et 15 min"
  - outil: CapsuleForge
    regle: "associer au moins une question notée à chaque capsule de contenu"
    niveau: C
    transferabilite: forte
    note: "temps total normalisé 1,47 contre 1,24 (avant) et 1,54 contre 1,28 (après) ; effet propre faible (f² = 0,05)"
  - outil: DiagForge
    regle: "mesurer le visionnage par étudiant et par capsule sur toutes les sessions (temps total / durée, part des secondes vues), pas seulement sur la première session"
    niveau: B
    transferabilite: forte
  - outil: DiagForge
    regle: "suivre la baisse de visionnage avec la position de la capsule dans le cours et la signaler à l'enseignant"
    niveau: C
    transferabilite: forte
---

# Le contexte du cours et la durée des vidéos (Parker et al., 2024)

Parker, M. J., Bunch, M. et Pike, A. (2024). Is anybody watching: A multi-factor motivational framework for educational video engagement. *Computers & Education*, 222, article 105148. [DOI](https://doi.org/10.1016/j.compedu.2024.105148)

**En une phrase.** Sur 3,1 millions de vues, les apprenants regardent souvent une même vidéo en plusieurs sessions : une vidéo longue est moins vue d'une traite mais plus vue au total, et le temps total est plus élevé quand la vidéo porte des questions notées et quand elle arrive tôt dans le cours ; la règle des 6 minutes ne vaut que pour la session unique.

## La source

| | |
| --- | --- |
| **Équipe** | Bureau de l'enseignement en ligne (HMX) et bureau de la formation externe, Harvard Medical School ; les auteurs produisent et exploitent les cours étudiés. |
| **Nature** | Académique ; aucun financement spécifique ; pas de conflit d'intérêts déclaré (p. 13). |
| **Support** | *Computers & Education* (Elsevier), libre accès. |
| **Audience** | 13 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Moyenne : indicateurs définis précisément (p. 5-6), logiciels cités ; données « sur demande » (p. 14), effectifs d'apprenants et coefficients des modèles en annexe en ligne. La démarche se refait sur d'autres traces ; les chiffres ne se vérifient pas. Pages citées : numéros imprimés de l'article (1 à 15). |

## Ce que fait l'étude

- **Corpus** (p. 4-6) : 16 cours de 10 semaines, 225 sessions, janvier 2018 à août 2023 ; 1 117 vidéos (concept au tableau blanc 37 %, interviews et tournages 32 %, autres 31 %), toutes de moins de 15 min (22 % de 0-3 min, 42 % de 3-6, 31 % de 6-9, 5 % de 9-12, 3 vidéos de 12-15) ; 53 % des vidéos ont au moins une question notée associée.
- **Changement de règle** (p. 5) : depuis avril 2020, un des deux certificats exige d'avoir vu chaque vidéo en entier en une session ; 74 % des vues sont postérieures.
- **Indicateurs** (p. 5-6) : temps de lecture en une session (SVE) et sur toutes les sessions (TE), rapportés à la durée (SVEN, TEN) ; couverture (secondes distinctes vues).
- **Analyses** (p. 6) : tests de Kruskal-Wallis et Mann-Whitney ; régressions ridge pour prédire, par vidéo, la part de vues très courtes (≤ 10 %) ou complètes (≥ 90 %) et de visionnage total élevé (≥ 150 %), comparées à un modèle « durée seule » ; 60 % apprentissage, 40 % test.

## Résultats

- **Session unique** (p. 7, fig. 4) : SVEN médian = 1,0 pour toutes les durées ; mais le quart le moins assidu voit moins de 75 % des vidéos de 6-9 min et moins de 50 % au-delà.
- **Toutes sessions** (p. 7) : le temps total et le TEN médians augmentent avec la durée ; ce n'est pas un effet de revisionnage d'un même passage (couverture, annexe).
- **Questions notées** (p. 9) : TEN moyen 1,24 sans question contre 1,47 avec (avant 2020) ; 1,28 contre 1,54 (après) ; la session unique est en revanche un peu plus courte.
- **Position** (p. 9, fig. 6) : le TEN baisse du premier au dernier quart des vidéos du cours.
- **Certificat** (p. 10) : part de vues complètes en une session 49,7 % avant, 62,6 % après le changement de règle.
- **Modèles** (p. 11, tableau 5) : erreur absolue moyenne d'environ 1,5 à 8 points, meilleure que la durée seule ; facteur le plus important pour la session unique : la durée ; pour le total : le type « concept » ; questions notées et position : importance moyenne. Effet propre du type f² = 0,36, des questions notées f² = 0,05 ; corrélation durée-questions 0,54.

## Avis critique

**Apport.** Corrige la lecture courante de [Guo et al. (2014)](guo2014.md) : la durée compte pour la session unique, pas pour le visionnage total ; et la présence de questions notées va avec plus de visionnage. Propose des indicateurs par apprenant directement utilisables dans DiagForge.

**Points forts**
- Très grand corpus, traces à la seconde, vidéos de bonne qualité homogène.
- Indicateurs multi-sessions et couverture : distinction claire entre « regarder d'une traite » et « regarder au total ».
- Tendances identiques avant et après le changement de règle de certificat.

**Réserves**
1. **Majeure** — Étude corrélationnelle : durée, type de vidéo et nombre de questions sont liés (r = 0,54 entre durée et questions) et rien n'est tiré au sort ; les auteurs le disent (p. 13). Aucune mesure d'apprentissage.
2. **Importante** — Très peu de vidéos longues : 62 vidéos de plus de 9 min sur 1 117 [calcul : 59 + 3], dont 3 de 12 à 15 min ; la recommandation « jusqu'à 15 min » repose sur peu de vidéos.
3. **Importante** — Public éloigné : adultes qui paient leur formation, 77 % terminent le cours (p. 5) ; la motivation est plus forte que chez des étudiants pour une capsule facultative.
4. **Mineure** — Effectifs d'apprenants et coefficients seulement en annexe ; p = 0,0 partout (millions de vues) ; statistique U de Mann-Whitney incohérente entre avant (1,4 × 10¹⁰) et après (413 202) le changement (p. 9).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les indicateurs en une session sous-estiment le visionnage total | B | Mesure directe sur un très grand corpus |
| Plus une vidéo est longue, moins elle est vue d'une traite par les moins assidus | C | Corrélationnel, concordant avec Guo et al. |
| Les questions notées vont avec plus de visionnage total | C | Corrélationnel, effet propre faible (f² = 0,05) |
| Des vidéos de 12 à 15 min sont aussi bien regardées au total | D | 3 vidéos seulement |

**Transférabilité** : forte pour les indicateurs (DiagForge) ; moyenne pour les seuils de durée (public payant et motivé, biomédical).

**Pour conclure, il faudrait** proposer dans Moodle un même chapitre de mécanique en une capsule de 12 min ou en trois de 4 min, tirées au sort par étudiant, et comparer visionnage total et score au quiz noté associé.

## Pour Forge

- **CapsuleForge** : sous 6 min pour une capsule à voir d'une traite ; jusqu'à 12-15 min possible pour une capsule de cours chapitrée et liée à des questions notées (niveau C, D au-delà de 12 min).
- **CapsuleForge** : au moins une question notée par capsule de contenu (niveau C).
- **DiagForge** : temps total par étudiant rapporté à la durée et couverture, toutes sessions confondues (niveau B) ; baisse avec la position dans le cours (niveau C).
- Renvois : [Guo et al., 2014](guo2014.md) (règle des 6 min, session unique), [Gutiérrez-González et al., 2024](gutierrez2024.md) (calendrier, tâche obligatoire), [Zhu et al., 2022](zhu2022.md) (8 min contre 55 min).
