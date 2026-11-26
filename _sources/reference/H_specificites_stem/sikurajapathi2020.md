---
cle: sikurajapathi2020
reference: "Sikurajapathi, I., Henderson, K. et Gwynllyw, R. (2020). Using e-assessment to address mathematical misconceptions in engineering students. International Journal of Information and Education Technology, 10(5), 356-361."
doi: 10.18178/ijiet.2020.10.5.1389
axe: [H3]
type_etude: étude descriptive d'erreurs (réponses saisies et brouillons papier d'un examen en ligne, 298 étudiants), puis renotage des tests hebdomadaires ; pas de mesure d'effet
public: première année d'ingénierie, module de mathématiques de l'ingénieur, université de l'Ouest de l'Angleterre (Bristol), système Dewis
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "repérer les erreurs types à partir des réponses fausses les plus fréquentes, puis les expliquer par les brouillons des étudiants qui ont donné cette réponse ; ne coder que les erreurs ainsi confirmées"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "après ajout d'une erreur type, renoter les réponses passées avec le nouveau code pour mesurer sa fréquence avant de rédiger le retour"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "coder comme erreurs types les erreurs de calculatrice (mode degrés au lieu de radians) au même titre que les erreurs de concept"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "choisir les paramètres pour que la clé diffère de chaque erreur type et que deux erreurs types ne donnent pas la même valeur ; sinon, rédiger un retour qui couvre les deux erreurs possibles"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "distinguer dans les résultats une question non répondue d'une réponse fausse, et compter par question la part des réponses fausses expliquée par l'erreur type principale"
    niveau: C
    transferabilite: forte
---

# Erreurs types en mathématiques de l'ingénieur et évaluation en ligne (Sikurajapathi et al., 2020)

Sikurajapathi, I., Henderson, K. et Gwynllyw, R. (2020). Using e-assessment to address mathematical misconceptions in engineering students. *International Journal of Information and Education Technology*, 10(5), 356-361. [DOI](https://doi.org/10.18178/ijiet.2020.10.5.1389)

**En une phrase.** En croisant les réponses fausses d'un examen en ligne et les brouillons papier de 298 étudiants d'ingénierie de première année, les auteurs cataloguent 40 erreurs types sur 17 des 19 questions, l'erreur principale expliquant souvent 30 à 70 % des réponses fausses ; ils constatent aussi que certains tirages de paramètres rendent une erreur type indiscernable de la bonne réponse.

## La source

| | |
| --- | --- |
| **Équipe** | Département de conception en ingénierie et de mathématiques, UWE Bristol ; doctorante (Sikurajapathi) et deux enseignants-chercheurs, dont le développeur principal de Dewis (Gwynllyw) (p. 361). |
| **Nature** | Académique ; les auteurs travaillent sur leur propre module et leur propre outil ; pas de conflit d'intérêts déclaré (p. 360). Financement non rapporté. |
| **Support** | *International Journal of Information and Education Technology*, libre accès ; revue à relecture probablement légère. |
| **Audience** | 28 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : procédure de repérage décrite (p. 358), trois exemples détaillés ; catalogue complet des 40 erreurs et données non publiés ; Dewis est libre (p. 357). |

## Ce que fait l'étude

- **Contexte** (p. 357-358) : module de mathématiques de l'ingénieur (30 crédits) ; 22 tests hebdomadaires Dewis à paramètres aléatoires, tentatives illimitées ; examen en ligne de deux heures en janvier 2018, 19 questions, deux sessions (148 et 150 étudiants) avec paramètres fixés par session ; brouillons papier ramassés.
- **Repérage** (p. 358) : pour chaque question, les réponses fausses les plus fréquentes sont extraites, puis les brouillons des étudiants qui les ont données sont examinés pour comprendre l'erreur.
- **Renotage** (p. 359) : les questions des tests hebdomadaires sont modifiées pour reconnaître chaque erreur type (indicateurs de performance), et les tests de l'année sont renotés.

## Résultats

- **Catalogue** (p. 358) : 40 erreurs types sur 17 des 19 questions ; aucune pour les questions 1 et 4. Erreur principale : 34 % des 197 réponses fausses à la question la moins réussie (Q14) ; 70 % à la question 12 (valeur la plus haute).
- **Exemples** (p. 358-359) :
  - fonction échelon u(t) traitée comme le nombre 1 : 35 réponses fausses sur 86 (41 %) ;
  - intégrale d'un cosinus calculée en mode degrés : 52 sur 183. Les auteurs écrivent 41 % ; 52/183 = 28 % [calcul] (22/86 et 30/97 par session) ;
  - dérivée de ln(ax) donnée comme 1/(ax) (3/(5x) au lieu de 3/x) : 30 sur 59 (51 %).
- **Tests hebdomadaires** (tableau I, p. 359) : erreur principale dans 25 % (85 sur 335), 20 % (25 sur 123) et 23 % (73 sur 324) des réponses fausses, moins qu'à l'examen.
- **Collisions** (p. 360) : pour f(t) = 2u(t-7) + 5u(t-1) et f(4), la clé et l'erreur type valent toutes deux -3 ; à la question d'intégrale, deux erreurs types donnent la même valeur fausse (3,80), impossible à départager sans brouillon.

## Avis critique

**Apport.** Procédure simple et reproductible pour constituer un catalogue d'erreurs types fondé sur des données (réponses fréquentes puis brouillons), et premier signalement chiffré du problème des tirages où l'erreur type donne la bonne réponse.

**Points forts**
- Erreurs confirmées par les brouillons, pas seulement devinées à partir de la valeur.
- Deux sessions avec paramètres différents, résultats rapportés séparément.
- Problème pratique de conception identifié (collisions) et règle proposée.

**Réserves**
1. **Importante** — Étude descriptive : l'effet du retour ciblé sur l'apprentissage n'est pas mesuré (annoncé pour 2019/20, p. 360).
2. **Importante** — Erreur de calcul dans le texte (41 % au lieu de 28 % pour l'intégrale) ; le catalogue des 40 erreurs n'est pas publié.
3. **Mineure** — Comparaison examen-tests hebdomadaires sur des bases différentes (réponses fausses de l'examen contre tentatives illimitées des tests) ; l'écart ne s'interprète pas directement.
4. **Mineure** — Analyse par une partie de l'équipe sans double codage rapporté.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Une erreur type explique souvent une grande part des réponses fausses | C | Un examen, une promotion, une université |
| La procédure réponses fréquentes puis brouillons identifie les erreurs | C | Décrite et illustrée, pas d'accord entre codeurs |
| Certains tirages rendent l'erreur type indiscernable | B | Constat logique vérifiable sur exemples |

Le dernier niveau porte sur l'existence du problème, pas sur sa fréquence, qui n'est rapportée ni ici ni dans [sikurajapathi2023](sikurajapathi2023.md).

**Transférabilité** : forte (première année d'ingénierie, mathématiques de l'ingénieur, outil de même nature qu'ExoForge).

**Pour conclure, il faudrait** appliquer la même procédure aux réponses d'un examen de mécanique (efforts, moments, RDM) avec brouillons, et comparer la part expliquée par l'erreur principale.

## Pour Forge

- **ExoForge** : catalogue d'erreurs types construit à partir des réponses fréquentes et des brouillons (C) ; renotage du passé avec chaque nouvelle erreur codée (C) ; erreurs de calculatrice codées (C) ; paramètres qui séparent clé et erreurs types (C).
- **DiagForge** : séparer non-réponse et réponse fausse ; part des réponses fausses expliquée par l'erreur principale (C).
- Renvois : [sikurajapathi2023](sikurajapathi2023.md) (suite : six cas de collision et correction du code) ; [gill2008](gill2008.md) (même démarche en mécanique) ; [kinnear2022](kinnear2022.md) (Q1-Q3).
