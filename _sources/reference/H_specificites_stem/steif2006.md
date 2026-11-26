---
cle: steif2006
reference: "Steif, P. S. et Hansen, M. A. (2006). Comparisons Between Performances in a Statics Concept Inventory and Course Examinations. International Journal of Engineering Education (volume et pages non rapportés dans forge.bib)."
doi: non attribué (voir forge.bib)
axe: [H2]
type_etude: étude corrélationnelle (1 331 passations d'un inventaire de concepts, 10 classes, 7 universités) et comparaison avec les erreurs d'examen dans deux classes
public: étudiants d'ingénierie en fin de statique ou en résistance des matériaux, États-Unis
lecture: texte complet (version auteur sans pagination de revue ; pages du PDF), 08/11/2026
regles:
  - outil: DiagForge
    regle: "rapporter un sous-score par concept : il annonce l'erreur correspondante à l'examen mieux que le score global"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "pour chaque question, afficher la part de chaque leurre et signaler quand un leurre est choisi autant ou plus que la bonne réponse"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "en statique, prévoir systématiquement les leurres : force interne dans le diagramme du corps libre, couple remplacé par une force de même moment, force de liaison parallèle à la barre, frottement égal à µN sans glissement"
    niveau: B
    transferabilite: forte
---

# Inventaire de statique et examens (Steif et Hansen, 2006)

Steif, P. S. et Hansen, M. A. (2006). Comparisons Between Performances in a Statics Concept Inventory and Course Examinations. *International Journal of Engineering Education*. Volume, pages et DOI absents de `forge.bib` ; le PDF lu est une version auteur sans pagination de revue : les pages citées sont celles du PDF.

**En une phrase.** Sur 1 331 passations de l'inventaire de statique, le score est corrélé aux examens autant que les examens entre eux, les sous-scores par concept repèrent les étudiants qui commettent l'erreur correspondante à l'examen, et quatre leurres dominent ; c'est l'argument pour un diagnostic par concept et par leurre dans DiagForge.

## La source

| | |
| --- | --- |
| **Équipe** | Génie mécanique, Carnegie Mellon (Steif, concepteur de l'inventaire) ; sciences de l'éducation, Robert Morris University (Hansen). |
| **Nature** | Académique ; financement de la National Science Foundation (REC-0440295) et du département (p. 8). Le premier auteur enseigne la classe 1, celle des analyses fines (p. 2, 5). |
| **Support** | *International Journal of Engineering Education* ; version auteur. |
| **Audience** | Voir forge.bib (pas de DOI, citations non relevées). |
| **Reproductibilité** | Moyenne : inventaire accessible aux enseignants (p. 7) ; données non publiques ; analyse factorielle des sous-scores « présentée ailleurs » (p. 4). |

## Ce que fait l'étude

- **Passations** (tableau 1, p. 2) : 10 classes de 7 universités en 2004-2005, 1 331 passations (35 à 419 par classe), en fin de statique (7 classes) ou en résistance des matériaux (3 classes) ; papier ou en ligne, sans enjeu de note.
- **Mesures** : score à 27 questions ; 8 sous-scores par concept ; examens des cours ; part de chaque option par question.
- **Analyses fines** : classe 1 (n = 97) : sous-scores des étudiants qui ont ou non commis trois erreurs précises à l'examen ; classe 2 (n = 38) : sous-scores selon la note d'un problème d'efforts tranchants et moments fléchissants.

## Résultats

- **Scores** (tableau 2, p. 2) : moyenne en fin de cours de 11,6 à 14,4 sur 27 hors classe 1, 20,5 dans la classe 1 ; gain normalisé de 0,24 à 0,35 hors classe 1, 0,61 dans la classe 1, celle du concepteur.
- **Qualité** (p. 2-3) : alpha 0,82 ; la plupart des questions ont une discrimination (27 % supérieurs moins 27 % inférieurs) au-dessus de 0,3 (figure 1).
- **Lien avec les examens** (tableaux 3-5, p. 3) : r de 0,24 à 0,62 avec l'examen final de statique ; de 0,19 à 0,65 avec les examens de résistance des matériaux ; du même ordre que les corrélations entre examens d'une même classe (0,13 à 0,73).
- **Sous-scores et erreurs d'examen** (tableau 6, p. 5) : pour chacune des trois erreurs (direction de la force d'un galet, d'un axe dans une rainure, frottement), le sous-score du concept correspondant sépare le plus nettement ceux qui se trompent (p = 0,002 ; 0,001 ; 0,001), les autres sous-scores rarement (une exception, p = 0,023).
- **Problème de RDM** (tableau 7, p. 5) : les sous-scores pertinents (diagramme du corps libre, équilibre, équivalence) séparent les groupes (écart de 0,78 à 0,90 écart-type, p ≤ 0,015), les non pertinents ne sont pas significatifs (p de 0,087 à 0,278), sauf « galet » (p = 0,045).
- **Leurres dominants** (p. 5-7) : force interne dans le diagramme du corps libre (15 % contre 66 % pour la bonne réponse ; 26 % sur d'autres questions) ; couple remplacé par une force de même moment (26 % contre 32 %) ; force du galet parallèle au bras (20 % contre 58 %) ; frottement pris égal à µN (39 % contre 32 % : le leurre l'emporte) ; force et couple qui « s'équilibrent » (25 % contre 58 %) ; seulement 11 % voient qu'aucun des deux chargements de la figure 12 ne peut être en équilibre.

## Avis critique

**Apport.** Montre qu'un score par concept, tiré de 3 questions environ, annonce l'erreur précise que l'étudiant commettra dans un problème rédigé, et chiffre les leurres de statique qui attirent le plus.

**Points forts**
- Grand nombre de passations dans des établissements variés.
- Comparaison concept par concept avec des erreurs d'examen relevées indépendamment (classe 2 notée par son enseignant avant l'analyse).
- Bonne réponse et leurre dominant rapportés en pourcentages.

**Réserves**
1. **Importante** — Les analyses par concept portent sur deux classes, dont celle du concepteur (n = 97) et une de 38 étudiants ; nombreux tests t sans correction pour comparaisons multiples.
2. **Importante** — Corrélations seulement : un sous-score bas accompagne l'erreur d'examen, rien ne dit qu'un retour par concept la corrige.
3. **Mineure** — Les 1 331 passations ne sont pas 1 331 étudiants : les classes de RDM 6 et 8 reprennent en grande partie les étudiants de statique 5 et 7 (p. 2).
4. **Mineure** — Analyse factorielle des sous-scores renvoyée à une autre publication (p. 4) ; fiabilité de chaque sous-score non rapportée.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Le score à l'inventaire est lié aux examens | B | 10 classes, 7 universités, corrélations comparables à celles entre examens |
| Le sous-score d'un concept annonce l'erreur correspondante | C | Deux classes, dont celle du concepteur ; corrélation |
| Leurres dominants (force interne, couple = force, µN) | B | Grand échantillon ; mêmes leurres dans `steif2005` |

**Transférabilité** : forte. Statique et RDM de l'ingénieur ; ces erreurs sont attendues chez nos L3.

**Pour conclure, il faudrait** comparer dans DiagForge, sur une promotion, les sous-scores par concept d'un quiz de statique aux erreurs codées dans le partiel, puis tester un retour ciblé par concept contre un retour global.

## Pour Forge

- **DiagForge** : rapport par concept (sous-scores) et par leurre (part de chaque option), avec alerte quand un leurre égale ou dépasse la bonne réponse (niveau C).
- **QuizForge** : leurres obligatoires pour la statique : force interne, couple remplacé par une force, force de liaison alignée sur la barre, frottement = µN (niveau B).
- **QuizForge** : au moins 3 questions par concept pour qu'un sous-score ait un sens (niveau C).
- Renvois : `steif2005` (construction de l'inventaire) ; `gross2012` (erreurs dans les problèmes rédigés) ; `klingbeil2024` (diagnostic sur plusieurs questions) ; `steif2006b` (restitution des résultats, fiche de l'axe).
