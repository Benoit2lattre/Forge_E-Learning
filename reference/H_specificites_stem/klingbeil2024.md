---
cle: klingbeil2024
reference: "Klingbeil, K., Rösken, F., Barzel, B., Schacht, F., Stacey, K., Steinle, V. et Thurm, D. (2024). Validity of multiple-choice digital formative assessment for assessing students' (mis)conceptions: evidence from a mixed-methods study in algebra. ZDM - Mathematics Education, 56, 713-726."
doi: 10.1007/s11858-024-01556-0
axe: [H3, B2]
type_etude: étude de validation à méthodes mixtes (5 entretiens cognitifs, 600 explications écrites comparées au diagnostic automatique)
public: élèves allemands de collège (Year 7 et Year 8) en début de chapitre sur les variables
lecture: texte complet, 08/11/2026
regles:
  - outil: DiagForge
    regle: "diagnostiquer une conception erronée sur plusieurs questions (ici 6, en paires parallèles), jamais sur une seule réponse"
    niveau: C
    transferabilite: moyenne
  - outil: DiagForge
    regle: "graduer le diagnostic selon le nombre de leurres d'une même erreur choisis (absent, intermittent, systématique), car un même étudiant ne choisit pas toujours le leurre de son erreur"
    niveau: C
    transferabilite: moyenne
  - outil: QuizForge
    regle: "pour valider une question diagnostique, ajouter une invite « explique ton choix » à une partie des passations et comparer l'explication au leurre choisi"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "ne pas conclure qu'une notion est maîtrisée sur une seule bonne réponse : la bonne option peut être choisie avec le raisonnement erroné"
    niveau: C
    transferabilite: forte
---

# Un QCM diagnostique en ligne mesure-t-il bien une conception erronée ? (Klingbeil et al., 2024)

Klingbeil, K., Rösken, F., Barzel, B., Schacht, F., Stacey, K., Steinle, V. et Thurm, D. (2024). Validity of multiple-choice digital formative assessment for assessing students' (mis)conceptions: evidence from a mixed-methods study in algebra. *ZDM - Mathematics Education*, 56, 713-726. [DOI](https://doi.org/10.1007/s11858-024-01556-0)

**En une phrase.** Un test en ligne de 6 QCM dont les leurres codent l'erreur « la lettre désigne un objet » repère presque tous les élèves qui montrent cette erreur dans leurs explications écrites (418 sur 420), mais un tiers des bonnes réponses à une question s'accompagnent du raisonnement erroné : le diagnostic tient sur un ensemble de questions, pas sur une seule.

## La source

| | |
| --- | --- |
| **Équipe** | Didactique des mathématiques, universités de Duisburg-Essen et Siegen (Allemagne) ; université de Melbourne (Stacey, Steinle), où le test SMART a été conçu. |
| **Nature** | Académique ; libre accès financé par Projekt DEAL ; pas de conflit d'intérêts déclaré (p. 725). Les conceptrices du test original sont co-autrices. |
| **Support** | *ZDM - Mathematics Education* (Springer), revue de didactique des mathématiques à comité de lecture. |
| **Audience** | 12 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : 6 questions, règles de diagnostic (tableau 1) et grille de codage (tableau 2) publiées ; données non publiques ; codage à deux codeurs par consensus, sans accord chiffré. |

## Ce que fait l'étude

- **Test** (p. 715-717) : version allemande du test SMART « Meaning of Letters » : 6 QCM en trois paires de structures algébriques différentes ; chaque leurre code l'erreur « lettre = objet » ou son sous-type « solution prise comme coefficient » (ex. 30b = 10p).
- **Règle de diagnostic** (tableau 1, p. 716) : stade 0 (0-1 bonne réponse), stade 1 (2-5), stade 2 (6) ; drapeau « solution comme coefficient » dès une réponse de ce type.
- **Entretiens** (p. 719) : 5 élèves de Year 8, une semaine après le test en ligne, sur la version parallèle, dont deux questions sans options.
- **Explications écrites** (p. 719) : deux invites « justifie ton choix » ajoutées au test en ligne ; 600 élèves analysés (228 en Year 7, 372 en Year 8) sur 616 ; explications de la question « Biros » codées par deux autrices.

## Résultats

- **Origine de la gradation** (p. 715-716) : sur 1 433 élèves australiens, pour deux questions quasi identiques, 52 % donnent la même erreur, 22 % une juste et une fausse, 6 % deux erreurs différentes : 28 % ne choisissent pas l'erreur de façon constante.
- **Leurres choisis pour la raison prévue** (p. 721) : explication « lettre = objet » chez 97 % des 305 explications exploitables de l'option p = 3b et 95 % des 21 de l'option p = 3 ; explication « solution comme coefficient » chez 92 % des 60 de l'option 30b = 10p. L'option b + p = 4 reçoit surtout des explications vides.
- **Bonne réponse pour une mauvaise raison** (p. 722) : la bonne option 3p = b (105 élèves) : sur 75 explications exploitables, 32 % justes, 35 % « lettre = objet », 28 % ambiguës.
- **Sensibilité du diagnostic** (tableau 4, p. 722) : 418 des 420 élèves dont l'explication montre l'erreur sont classés aux stades 0 ou 1 [décompte] ; 57 des 58 explications « solution comme coefficient » sont signalées.
- **Spécificité moindre** (p. 722, 724) : 78 % des explications des élèves de stade 0 montrent l'erreur ; seulement 14 % des élèves signalés « solution comme coefficient » la montrent sur cette question, car le drapeau vient surtout d'autres questions (314 et 344 sur 412).
- **Entretiens** (tableau 3, p. 721) : l'erreur est retrouvée chez les 5 élèves, aussi dans les questions ouvertes ; le stade exact diffère dans un cas et le drapeau « coefficient » dans deux.
- **Plafond bas** : 11 élèves sur 600 au stade 2 (p. 722).

## Avis critique

**Apport.** Une des rares études qui confrontent, à grande échelle, le leurre choisi et le raisonnement écrit : elle mesure ce que vaut un diagnostic automatique par leurres et montre pourquoi il faut plusieurs questions par erreur.

**Points forts**
- Triangulation : entretiens, explications écrites, diagnostic automatique.
- Les deux sens de la concordance sont analysés (l'erreur vue est-elle signalée ? le signal correspond-il à l'erreur ?).
- Limites énoncées (p. 724), y compris l'ambiguïté des explications courtes.

**Réserves**
1. **Importante** — Public de collège et notion d'algèbre élémentaire : le mécanisme (diagnostic sur plusieurs leurres) se transpose, pas les taux.
2. **Importante** — Explication écrite pour une seule question sur six ; 128 explications vides ou inexploitables (p. 723), toutes aux stades 0 ou 1.
3. **Mineure** — Codage par consensus sans indice d'accord ; 11 élèves seulement au stade 2, trop peu pour juger les faux négatifs.
4. **Mineure** — Effets sur les décisions des enseignants et l'apprentissage non évalués (p. 724).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les leurres bien construits sont choisis pour la raison prévue | B | 600 élèves, concordance > 90 % pour les leurres principaux, entretiens concordants |
| Un diagnostic sur 6 questions repère presque tous les élèves qui ont l'erreur | C | Un seul test, public éloigné (abaissé d'un niveau) |
| Une bonne réponse isolée ne prouve pas la maîtrise | C | Une question ; rejoint `ford2020` et `tatsuoka1983` |

**Transférabilité** : moyenne pour les règles de diagnostic (collège, algèbre), forte pour la méthode de validation (invite « explique ton choix »), utilisable telle quelle dans un quiz Moodle.

**Pour conclure, il faudrait** ajouter dans QuizForge une invite de justification à une question sur six d'un quiz de statique, coder les réponses d'une promotion et calculer la concordance avec le leurre choisi.

## Pour Forge

- **DiagForge** : diagnostic d'une erreur type sur au moins 3 questions qui la visent, avec gradation (absente, intermittente, systématique) (niveau C).
- **DiagForge** : une bonne réponse isolée ne vaut pas maîtrise ; rapporter « à confirmer » tant que les questions parallèles ne concordent pas (niveau C).
- **QuizForge** : invite « explique ton choix » sur une partie des passations pour valider les leurres d'une nouvelle question (niveau C).
- Renvois : `ford2020` (faux positifs vus en entretien) ; `steif2006` (sous-scores par concept) ; `tatsuoka1983` (règles erronées qui donnent la bonne réponse) ; fiches de l'axe B sur la rédaction des leurres.
