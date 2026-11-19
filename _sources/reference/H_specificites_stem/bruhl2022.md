---
cle: bruhl2022
reference: "Bruhl, J. C., Hanus, J. P., McMullen, K. F. et Rocha, B. (2022). Identifying Sticking Points: Common Mechanics Errors Made by Civil Engineering Students. 2022 ASEE Annual Conference & Exposition Proceedings, papier 36646."
doi: 10.18260/1-2--40565
axe: [H2, H3]
type_etude: étude descriptive d'erreurs sur un examen diagnostique sans enjeu (10 problèmes à réponse numérique), 4 promotions, en 3e et 4e année ; classement des erreurs des 4 problèmes les moins réussis
public: élèves ingénieurs en génie civil de West Point (académie militaire, États-Unis), 3e année (127 copies) et 4e année (139 copies), 2018-2021
lecture: texte complet, 10/11/2026
regles:
  - outil: ExoForge
    regle: "problème hyperstatique (barres, poutre continue, poteau en béton armé) : reconnaître comme erreurs types « équilibre seul sans compatibilité », « compatibilité seule », « charge répartie également entre appuis ou matériaux », « force totale divisée par chaque aire » ; retour qui fait d'abord identifier le degré d'hyperstaticité"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "leurres de statique et RDM issus des erreurs relevées : encastrement sans moment de réaction, contrainte normale sans terme de flexion (N/A seul), mauvaise somme des contraintes, barre à effort nul non reconnue, mauvais sens de réaction"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "vérifier séparément le module, l'unité, le sens et le point d'application d'une réaction (et traction ou compression pour une barre), avec un retour propre au sens faux quand le module est juste"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "classer les réponses fausses d'un problème en non conceptuelle (calcul, trigonométrie, présentation), exécution mineure et conceptuelle majeure, avec une catégorie distincte « aucune piste » (copie abandonnée)"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "recueillir une confiance de 0 à 5 par question et signaler les questions où la confiance moyenne est élevée et la réussite faible"
    niveau: D
    transferabilite: forte
  - outil: ExoForge
    regle: "avant le calcul, une question d'identification du type de problème (isostatique ou hyperstatique, barres à effort nul, sollicitations combinées)"
    niveau: D
    transferabilite: forte
---

# Erreurs types en statique et RDM chez les élèves de génie civil (Bruhl et al., 2022)

Bruhl, J. C., Hanus, J. P., McMullen, K. F. et Rocha, B. (2022). Identifying Sticking Points: Common Mechanics Errors Made by Civil Engineering Students. *2022 ASEE Annual Conference & Exposition Proceedings*. [DOI](https://doi.org/10.18260/1-2--40565)

Actes sans pagination de revue : la fiche cite les pages du PDF (1 à 21).

**En une phrase.** Sur un examen diagnostique sans enjeu passé en 3e et 4e année, les problèmes hyperstatiques sont résolus par 11 à 12 % des élèves, l'erreur dominante étant de ne pas reconnaître l'hyperstaticité (équilibre seul, charge répartie également) ; les autres erreurs fréquentes sont la barre à effort nul non vue, le moment d'encastrement oublié et la flexion omise dans le calcul des contraintes : un catalogue d'erreurs directement utilisable pour des leurres et des retours ciblés.

## La source

| | |
| --- | --- |
| **Équipe** | Département de génie civil et mécanique, académie militaire de West Point (p. 1). Les auteurs enseignent les cours concernés et ont construit l'examen. |
| **Nature** | Académique ; financement non rapporté. |
| **Support** | Actes du congrès annuel de l'ASEE (relecture de congrès). |
| **Audience** | 2 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Faible à moyenne : énoncés non publiés, l'examen étant toujours en usage (p. 9) ; concepts (tableau 1) et barèmes renvoyés à un article antérieur ; tableaux d'erreurs détaillés par promotion (tableaux 3 à 6). La grille de classement se refait ; les chiffres ne se vérifient que dans les tableaux. |

## Ce que fait l'étude

- **Examen** (p. 4-6, tableau 1) : 10 problèmes à réponse numérique (pas de QCM), 55 minutes, une feuille de formules ; versions différentes en 3e et 4e année sur les mêmes concepts (treillis, hyperstatique axial, diagrammes d'effort tranchant et de moment, flèche, poutre hyperstatique, encastrement, sollicitations combinées). Statique et RDM ont été suivies en 2e année : 3 mois avant l'examen de 3e année, 15 mois avant celui de 4e année.
- **Effectifs** (tableau 2, p. 5) : promotions 2019 à 2023 ; 20 à 45 élèves par passation ; 2020 à 2022 passent les deux versions.
- **Mesures** (p. 6) : 2 points par problème, notation globale par barème ; temps estimé et confiance de 0 à 5 par problème.
- **Classement des erreurs** (p. 6, 8) : pour les 4 problèmes les moins réussis, erreurs non conceptuelles, d'exécution mineures et conceptuelles majeures, grille adaptée de [Gross et Dinehart (2012)](gross2012.md) ; un auteur par problème.

## Résultats

Décomptes sur les tableaux 3 à 6 : 127 copies de 3e année et 139 de 4e année, toutes promotions réunies [décompte].

- **Treillis** (tableau 3, p. 9-11) : en 3e année, environ 25 % réussissent, 35 % font des erreurs de calcul ou de trigonométrie, 40 % une erreur conceptuelle majeure, surtout la coupe mal posée, qui fait abandonner (p. 10). Diagramme du corps isolé gravement faux (forces manquantes ou fausses) : 28 copies sur 127 en 3e année, 10 sur 139 en 4e année [décompte]. En 4e année, la barre à effort nul n'est pas reconnue dans 66 copies sur 139 (47 %) [décompte] ; ceux qui la voient finissent en général le problème (p. 11).
- **Hyperstatique axial** (tableau 4, p. 11-12) : 11 % de réussite en 3e année, 12 % en 4e année. Erreurs : « aucune piste » 35 copies sur 127 en 3e année et 109 sur 139 (78 %) en 4e année [décompte] ; équilibre seul ou compatibilité seule 36 copies en 3e année [décompte] ; en 4e année (poteau en béton armé), charge partagée également entre béton et acier, ou force totale divisée par l'aire du béton puis par celle de l'acier : 83 % font une de ces erreurs (p. 12).
- **Poutre hyperstatique** (tableau 5, p. 13-15) : environ 53 % d'erreurs conceptuelles majeures en 3e année ; parmi les copies « aucune piste », 87 % répartissent la charge également entre les trois appuis ; seuls 5 élèves ayant fait une erreur majeure reconnaissent l'hyperstaticité (p. 14). En 4e année, 32 élèves donnent le bon module de la réaction mais pas son sens (p. 14).
- **Sollicitations combinées** (tableau 6, p. 16-17) : moins de 10 % de réussite en 3e année, 18 % en 4e année. Encastrement sans moment de réaction : 59 copies sur 127 en 3e année, 36 sur 139 en 4e année ; contrainte de flexion omise : 50 et 54 copies [décompte]. Autres : mauvaise somme des contraintes normales, mauvais sens d'une réaction, axe neutre mal placé, charge répartie mal convertie.
- **Confiance** (fig. 4, p. 8) : en 4e année, la confiance est plus élevée sur l'hyperstatique axial que sur des problèmes mieux réussis ; les auteurs parlent de confiance mal placée.
- **Évolution** (p. 18) : meilleurs résultats en 4e année sur 3 problèmes sur 4, ceux repris dans les cours suivants ; pas sur l'hyperstatique axial, non repris avant l'examen.

## Avis critique

**Apport.** Prolonge le catalogue de [Gross et Dinehart (2012)](gross2012.md) à des problèmes de niveau L3 (hyperstatique, sollicitations combinées) avec des fréquences par promotion ; conclusion pédagogique nette : l'erreur majeure vient souvent de ce que le type de problème n'est pas reconnu (p. 19).

**Points forts**
- Problèmes ouverts, copies réelles, quatre promotions, deux niveaux d'études.
- Tableaux d'erreurs détaillés et nommés, réutilisables tels quels.
- Recueil de la confiance et du temps par problème.

**Réserves**
1. **Importante** — Les versions de 3e et 4e année posent des problèmes différents (p. 11-12, 18) : les comparaisons entre niveaux ne mesurent pas l'évolution des mêmes élèves ; aucun test statistique, bien que le texte dise « significativement » (p. 17).
2. **Importante** — Classement des erreurs par un seul auteur par problème, sans accord entre codeurs (p. 6) ; frontière entre « exécution mineure » et « conceptuelle majeure » non définie (la barre à effort nul non vue est dite « erreur conceptuelle mineure » p. 11, catégorie absente de la grille à trois familles ; p. 17, « erreur conceptuelle mineure » et « erreur d'exécution mineure » sont employées l'une pour l'autre).
3. **Mineure** — Petites incohérences d'effectifs entre le tableau 2 et les tableaux 3 à 6 (45 contre 47 en 2019, 35 contre 34 et 34 contre 35 en 3e année) ; certains pourcentages du texte ne se retrouvent pas dans les tableaux (« aucune piste » sur la poutre : 33 % en 4e année contre 24 % en 3e année [décompte], alors que le texte annonce 14 % d'erreurs majeures en moins en 4e année, p. 14).
4. **Mineure** — Un seul établissement, très particulier (académie militaire), examen sans enjeu : une part des copies « aucune piste » peut traduire un manque d'effort.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Liste et fréquence relative des erreurs sur ces problèmes | C | Copies réelles, quatre promotions, codage sans accord mesuré |
| Ne pas reconnaître l'hyperstaticité est l'erreur dominante | C | Concordant sur deux problèmes et deux niveaux |
| S'exercer à identifier le type de problème réduirait les erreurs | D | Proposition des auteurs, non testée |
| La confiance est mal placée sur l'hyperstatique axial | D | Lecture de figures, sans test |

**Transférabilité** : forte pour le catalogue (problèmes de RDM et de calcul des structures de L3) ; moyenne pour les fréquences.

**Pour conclure, il faudrait** coder dans ExoForge les erreurs « équilibre seul » et « charge répartie également » sur un problème hyperstatique paramétré, et comparer par tirage au sort un retour qui fait identifier le degré d'hyperstaticité à la seule solution rédigée.

## Pour Forge

- **ExoForge** : erreurs types de l'hyperstatique codées comme formules fausses, avec retour sur l'identification du problème (niveau C).
- **QuizForge** : leurres « encastrement sans moment », « N/A sans flexion », « barre à effort nul ignorée », « sens de réaction faux » (niveau C).
- **ExoForge** : contrôle séparé module, unité, sens, point d'application (niveau C).
- **DiagForge** : trois familles d'erreurs plus « aucune piste » (niveau C) ; confiance déclarée contre réussite (niveau D).
- **ExoForge** : question préalable d'identification du type de problème (niveau D).
- Catalogue d'erreurs (statique et RDM) : diagramme du corps isolé avec forces manquantes ou fausses ; coupe de treillis mal posée ; barre à effort nul non reconnue ; traction et compression inversées ; équilibre seul en hyperstatique ; compatibilité seule ; charge partagée également entre appuis ou matériaux ; force divisée par chaque aire ; équation de déformation axiale au lieu de la flèche ; mauvaise inconnue hyperstatique ; moment d'encastrement oublié ; terme de flexion omis ; mauvaise somme des contraintes ; axe neutre mal placé ; charge répartie mal convertie ; bras de levier faux ; sens de réaction faux ; erreurs de calcul, de trigonométrie et de présentation (unités, sens).
- Renvois : [gross2012](gross2012.md) (même grille), [steif2006](steif2006.md) (erreurs conceptuelles de statique), [rosengrant2009](rosengrant2009.md) (diagramme du corps isolé).
