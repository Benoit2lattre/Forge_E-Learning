---
cle: salden2010
reference: "Salden, R. J. C. M., Aleven, V., Schwonke, R. et Renkl, A. (2010). The expertise reversal effect and worked examples in tutored problem solving. Instructional Science, 38(3), 289-307."
doi: 10.1007/s11251-009-9107-8
axe: [D2, D1]
type_etude: deux essais randomisés à 3 groupes (laboratoire, puis classe sur 3 semaines)
public: 57 lycéens allemands (laboratoire) ; 51 élèves de lycée professionnel américain (classe)
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "estomper chaque étape selon la maîtrise de l'étudiant, principe par principe : l'étape devient à résoudre après des réussites, redevient un exemple après des erreurs (deux seuils)"
    niveau: C
    transferabilite: moyenne
  - outil: ExoForge
    regle: "faire nommer le principe utilisé à chaque étape (choix dans une liste) : c'est à la fois une auto-explication et la mesure qui pilote l'estompage"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "avec un retour et des indices à chaque étape, un estompage fixe, identique pour tous, n'apporte rien de mesurable"
    niveau: C
    transferabilite: moyenne
---

# Estompage adaptatif dans un tuteur intelligent (Salden et al., 2010)

Salden, R. J. C. M., Aleven, V., Schwonke, R. et Renkl, A. (2010). The expertise reversal effect and worked examples in tutored problem solving. *Instructional Science*, 38(3), 289-307. [DOI](https://doi.org/10.1007/s11251-009-9107-8)

**En une phrase.** Dans un système tutoriel intelligent (STI) de géométrie, qui corrige chaque étape, transformer une étape d'exemple en étape à résoudre seulement quand l'élève sait justifier le principe correspondant donne de meilleurs résultats au test différé qu'un estompage fixe ou que la résolution guidée par le STI sans exemples ; l'estompage fixe, lui, ne fait pas mieux que cette résolution guidée.

## La source

| | |
| --- | --- |
| **Équipe** | Institut d'interaction homme-machine de Carnegie Mellon (Pittsburgh) et Institut de psychologie de Fribourg-en-Brisgau (Renkl, spécialiste de l'estompage). |
| **Nature** | Académique ; financement National Science Foundation via le Pittsburgh Science of Learning Center (p. 306). Le STI évalué (Geometry Cognitive Tutor) vient de l'équipe de Carnegie Mellon. |
| **Support** | *Instructional Science* (Springer). |
| **Audience** | 123 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : la règle d'adaptation est décrite précisément (estimation bayésienne de la maîtrise, seuils 0,7 et 0,5, Fig. 2 p. 296) et la séquence fixe est donnée (tableau 1, p. 294), mais le logiciel et les données ne sont pas fournis. |

## Ce que fait l'étude

- **Contenu** : propriétés des angles en géométrie (angles opposés, supplémentaires, complémentaires, somme) ; problèmes de 1 à 3 étapes, chaque étape étant l'application d'un théorème (p. 293).
- **Trois conditions**, toutes dans le STI, qui corrige chaque étape et donne des indices à la demande (le titre anglais parle de *tutored problem solving*, résolution de problèmes guidée par le STI) :
  - résolution guidée seule, sans exemples ;
  - estompage fixe : les étapes sont d'abord résolues par le logiciel, puis laissées à l'élève selon une séquence identique pour tous (tableau 1, p. 294) ;
  - estompage adaptatif : l'élève justifie chaque étape résolue en nommant le théorème (saisie ou glossaire) ; le STI estime sa maîtrise de chaque théorème ; au-dessus de 0,7 l'étape devient à résoudre, en dessous de 0,5 elle redevient un exemple (p. 295).
- **Expérience 1 (laboratoire)** : 57 lycéens allemands de 15 ans environ, tirés au sort (environ 19 par groupe), 11 problèmes en une séance, test papier immédiat et une semaine plus tard ; élèves payés 20 € (p. 293-297).
- **Expérience 2 (classe)** : 51 élèves de 9e année d'un lycée professionnel rural américain, un seul enseignant, tirage au sort par blocs selon la note antérieure ; 2 h par semaine pendant 3 semaines, 5 sections et 19 théorèmes ; le STI ajoute des problèmes de rattrapage jusqu'à maîtrise ; tests en ligne avant, après et 3 semaines plus tard (p. 299-301).

## Résultats

- **Laboratoire** (p. 297) : moyennes au test immédiat 5,79 (résolution), 5,21 (fixe), 7,13 (adaptatif) ; au test différé 4,66, 4,50 et 6,67. L'adaptatif fait mieux que les deux autres réunis (d = 0,49 immédiat, d = 0,59 différé). Fixe et résolution ne diffèrent pas. Le groupe adaptatif reçoit moins d'étapes résolues (8,4 contre 12,1), en temps égal.
- **Classe** (p. 301-302) : pas de différence au test immédiat. Au test différé : 8,08 (résolution), 9,38 (fixe), 12,80 (adaptatif) ; adaptatif contre les deux autres d = 0,74, contre la résolution seule d = 0,91. Ici le groupe adaptatif reçoit plutôt plus d'exemples que le groupe fixe.

## Avis critique

**Apport.** Montre qu'une règle d'adaptation simple, fondée sur les justifications de l'élève, peut piloter le passage de l'exemple à l'exercice étape par étape, et que l'ajout d'exemples à un STI qui corrige déjà chaque étape n'aide que s'il est adapté à l'élève.

**Points forts**
- Même manipulation testée en laboratoire puis en classe réelle, sur trois semaines.
- La règle d'adaptation est assez décrite pour être reprogrammée.
- Le témoin est exigeant (résolution avec retour et indices à chaque étape), pas une résolution sans aide.

**Réserves**
1. **Majeure** (pour la classe) — Forte perte d'effectif : 20 élèves sur 51 ont passé les trois tests (p. 301). Le résultat de la classe repose sur le seul test différé, sur 35 élèves, soit une douzaine par groupe. Un abandon sélectif ne peut pas être exclu.
2. **Importante** — Tests unilatéraux et contraste « adaptatif contre les deux autres réunis ». Au test immédiat du laboratoire, t(54) = 1,74 donne p ≈ 0,09 en test bilatéral [calcul] : le résultat immédiat ne tient qu'en unilatéral.
3. **Importante** — Le test du laboratoire est annoncé sur 85 points (p. 295) mais les moyennes sont entre 4,5 et 7,1 (p. 297), soit moins de 9 % du maximum [calcul]. Soit l'échelle n'est pas celle annoncée, soit le test est très difficile (effet plancher) ; l'article ne permet pas de trancher.
4. **Importante** — Public éloigné du nôtre : lycéens, théorèmes élémentaires d'une seule ligne de calcul.
5. **Mineure** — Petits groupes dans les deux expériences (environ 19, puis une douzaine).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| L'estompage adaptatif fait mieux au test différé que l'estompage fixe ou la résolution guidée sans exemples | C | Deux contextes concordants, mais petits effectifs, unilatéral, attrition |
| Avec retour et indices à chaque étape, l'estompage fixe n'apporte rien | C | Absence d'effet sur petits échantillons |

**Transférabilité** : moyenne pour le mécanisme (ExoForge corrige déjà chaque étape ; une règle à deux seuils est simple à programmer) ; faible pour les valeurs (lycée, géométrie élémentaire).

**Pour conclure, il faudrait** comparer dans ExoForge, en L3, un estompage adaptatif simple (l'étape devient à résoudre après deux justifications correctes du principe, redevient un exemple après une erreur) à un estompage fixe, avec un test différé de deux à trois semaines.

## Pour Forge

- **ExoForge** : estomper principe par principe selon la maîtrise mesurée, avec un seuil de montée et un seuil de retour (niveau C). C'est la piste « niveau suivant après deux réussites » déjà notée pour l'axe D.
- **ExoForge** : faire nommer le principe de chaque étape par un choix dans une liste ; c'est l'auto-explication la plus légère et c'est elle qui alimente l'adaptation (niveau C).
- **ExoForge** : comme ExoForge corrige déjà chaque étape, un estompage fixe identique pour tous a peu de chances d'apporter quelque chose ; l'effort est à mettre sur l'adaptation (niveau C).
