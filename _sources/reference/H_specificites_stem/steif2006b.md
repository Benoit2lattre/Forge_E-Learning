---
cle: steif2006b
reference: "Steif, P. S. et Hansen, M. A. (2006). Feeding Back Results From A Statics Concept Inventory To Improve Instruction. 2006 Annual Conference & Exposition Proceedings, ASEE, papier 2006-204, p. 11.641.1-11.641.9."
doi: 10.18260/1-2--130
axe: [H2]
type_etude: rapport de conception (formats de restitution) avec indicateurs psychométriques sur 1 164 passations et enquête d'opinion dans une classe (41 réponses)
public: étudiants de statique, 16 classes de 14 établissements, États-Unis, automne 2005
lecture: texte complet, 10/11/2026
regles:
  - outil: DiagForge
    regle: "restituer à chaque étudiant son score par concept (moyenne des questions du concept), le juste/faux par question et sa position dans la classe, pas seulement le score total"
    niveau: C
    transferabilite: forte
    note: "sous-scores étayés par des corrélations plus fortes à l'intérieur des concepts qu'entre concepts ; l'effet de la restitution sur l'apprentissage n'est pas mesuré"
  - outil: DiagForge
    regle: "avant d'interpréter des sous-scores par concept, vérifier que les questions d'un même concept sont plus corrélées entre elles qu'avec celles des autres concepts (corrélation tétrachorique) et signaler la question qui ne corrèle pas avec les deux autres"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "exclure ou signaler les passations trop rapides (durée minimale paramétrable, 10 minutes pour 27 questions conceptuelles) avant de calculer les indicateurs"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "étiqueter chaque question conceptuelle par concept dans la banque, avec au moins 3 questions par concept, pour permettre un sous-score par concept"
    niveau: C
    transferabilite: forte
---

# Restituer les résultats de l'inventaire de statique (Steif et Hansen, 2006)

Steif, P. S. et Hansen, M. A. (2006). Feeding Back Results From A Statics Concept Inventory To Improve Instruction. *2006 Annual Conference & Exposition Proceedings*, ASEE. [DOI](https://doi.org/10.18260/1-2--130)

Pagination des actes « 11.641.N » : la fiche cite p. N.

**En une phrase.** Sur 1 164 passations de l'inventaire de statique (27 questions, 9 concepts de 3 questions), les questions d'un même concept sont plus corrélées entre elles qu'avec les autres (0,50 contre 0,24 en moyenne), ce qui justifie de restituer un score par concept aux étudiants et aux enseignants ; les auteurs proposent trois graphiques de restitution, mais n'en mesurent l'effet que par une enquête de satisfaction dans une classe.

## La source

| | |
| --- | --- |
| **Équipe** | Génie mécanique, Carnegie Mellon (Steif, concepteur de l'inventaire) ; sciences de l'éducation, Robert Morris University (Hansen) (p. 1). Suite de [Steif et Dantzler (2005)](steif2005.md) et de [Steif et Hansen (2006)](steif2006.md). |
| **Nature** | Académique ; financement de la National Science Foundation (REC-0440295) et du département de génie mécanique de Carnegie Mellon (p. 9). Les auteurs évaluent leur propre instrument. |
| **Support** | Actes du congrès annuel de l'ASEE (relecture de congrès). |
| **Audience** | 14 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Moyenne : formules des indicateurs données (p. 3-4), inventaire accessible aux enseignants ; données non publiques ; questions de l'enquête publiées (p. 8). Les calculs se refont sur toute banque de QCM étiquetée par concept. |

## Ce que fait l'étude

- **Instrument** (p. 2-3, tableau 1) : 27 QCM, une question par concept élémentaire, calcul négligeable, leurres codant des erreurs types ; 9 concepts de 3 questions (A forces sur des corps séparés, B 3e loi de Newton, C équivalence statique, D appui à rouleau, E axe dans une rainure, F surface sans frottement, G efforts aux liaisons, H limite du frottement, I équilibre).
- **Données** (p. 3) : version en ligne, automne 2005, 16 classes de 14 établissements ; 1 255 passations, dont 91 exclues [calcul : 1 255 - 1 164] pour une durée inférieure à 10 minutes, soit 1 164 retenues.
- **Indicateurs** (p. 3-5) : alpha de Cronbach ; indice de discrimination (27 % meilleurs moins 27 % plus faibles) ; corrélations tétrachoriques entre questions d'un même concept et de concepts différents.
- **Restitution** (p. 6-7) : boîtes à moustaches des scores totaux par classe, profil des scores par concept d'une classe comparé aux autres, histogramme par concept pour la classe ; envoi automatique par courriel à chaque étudiant de son score par question, par concept et total.
- **Usage** (p. 8) : dans une classe, séance de révision avant l'examen final sur les 5 concepts les moins réussis ; enquête en 3 questions sur une échelle de 1 à 5.

## Résultats

- **Erreurs dominantes** (p. 3), reprises d'une étude antérieure : forces internes dessinées dans le diagramme du corps isolé d'un ensemble de corps ; couple remplacé par une force de même moment en un point ; équilibre des forces sans équilibre des moments (ou l'inverse) ; direction de la force de liaison (rouleau, axe dans une rainure) déduite de la charge appliquée ou de la forme du corps ; frottement pris égal à µN alors qu'il n'y a pas glissement.
- **Durée** (p. 3) : sous 5 minutes, scores proches du hasard ; entre 5 et 10 minutes, à peine meilleurs.
- **Fiabilité** (p. 4) : alpha = 0,834 ; une seule question sous 0,3 de discrimination (très peu réussie), trois autres sous 0,4.
- **Sous-scores** (tableau 2, p. 5) : corrélation moyenne à l'intérieur d'un concept 0,500 contre 0,239 entre concepts ; à l'intérieur de 0,258 (G) à 0,672 (A et E), entre concepts de 0,176 à 0,288 ; pour tous les concepts, l'intérieur dépasse l'extérieur. Les valeurs faibles de G et I viennent d'une question qui ne corrèle pas avec les deux autres.
- **Enquête** (tableau 3, p. 8), 41 réponses : la séance a aidé à comprendre 4,15 (écart-type 0,70) ; connaître ses réponses justes et fausses a rendu la séance plus utile 3,65 (1,03) ; aidera à l'examen 3,64 (0,90). Deux étudiants demandent qu'on rappelle d'apporter les résultats reçus.

## Avis critique

**Apport.** Fixe le grain de restitution d'un test diagnostique de mécanique : le concept (3 questions), entre le score total, qui ne dit pas quoi faire, et la question isolée, trop fine (p. 5). C'est la justification directe des sous-scores par concept de DiagForge.

**Points forts**
- Argument psychométrique simple et reproductible pour les sous-scores (corrélations intra contre inter-concepts).
- Gros échantillon multi-établissements ; règle explicite d'exclusion des passations bâclées.
- Formats de restitution concrets, pour l'enseignant et pour l'étudiant.

**Réserves**
1. **Majeure** — L'effet de la restitution n'est pas mesuré : une enquête d'opinion dans une seule classe (41 réponses), sans groupe témoin ni note d'examen. Les auteurs le renvoient à des travaux futurs (p. 9).
2. **Importante** — Avec 3 questions par concept, un sous-score individuel ne prend que 4 valeurs ; aucune fiabilité par concept n'est donnée. Les corrélations intra-concept de G (0,258) et I (0,333) restent faibles.
3. **Mineure** — Les leurres dominants sont rappelés sans chiffres (renvoi à une étude antérieure, voir [steif2006](steif2006.md)).
4. **Mineure** — Le seuil de 10 minutes est fixé à vue, sans distribution des durées publiée.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les sous-scores par concept mesurent des connaissances distinctes | C | Corrélations sur 1 164 passations, sans analyse factorielle ni fiabilité par concept |
| Les passations de moins de 10 minutes ne mesurent rien | C | Constat descriptif, seuil non justifié |
| Restituer les résultats par concept améliore l'apprentissage | D | Opinion d'une classe, pas de mesure de performance |

**Transférabilité** : forte pour le grain par concept et le filtre de durée (quiz Moodle en autonomie) ; l'effet sur l'apprentissage reste à établir.

**Pour conclure, il faudrait** envoyer dans DiagForge le bilan par concept à une moitié tirée au sort d'un groupe et le seul score total à l'autre, puis comparer la réussite aux questions des mêmes concepts à l'examen.

## Pour Forge

- **DiagForge** : bilan individuel par concept, par question et par rapport à la classe ; bilan enseignant par concept avec comparaison entre groupes ou années (niveau C).
- **DiagForge** : test de validité des sous-scores (corrélations intra contre inter-concepts) et repérage de la question isolée d'un concept (niveau C).
- **DiagForge** : filtre de durée minimale avant les indicateurs (niveau C).
- **QuizForge** : étiquette de concept et au moins 3 questions par concept (niveau C).
- Renvois : [steif2005](steif2005.md) (construction de l'inventaire), [steif2006](steif2006.md) (leurres dominants, lien avec l'examen), [steele2014](steele2014.md) (usage en classe des questions par concept).
