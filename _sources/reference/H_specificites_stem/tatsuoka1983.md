---
cle: tatsuoka1983
reference: "Tatsuoka, K. K. (1983). Rule Space: An Approach for Dealing with Misconceptions Based on Item Response Theory. Journal of Educational Measurement, 20(4), 345-354."
doi: 10.1111/j.1745-3984.1983.tb00212.x
axe: [H3]
type_etude: article de méthode psychométrique illustré sur un test (172 élèves, 40 questions ouvertes)
public: élèves de 4e environ (eighth graders) d'un collège américain, soustraction de nombres relatifs
lecture: texte complet (scan JSTOR, texte coupé en marge droite par endroits ; passages chiffrés vérifiés), 08/11/2026
regles:
  - outil: ExoForge
    regle: "à la construction d'un exercice paramétré, exécuter chaque règle erronée connue sur les valeurs tirées et rejeter le tirage si l'une d'elles donne la bonne réponse"
    niveau: C
    transferabilite: forte
    note: "mécanisme démontré par énumération : 27 des 47 règles erronées donnent la bonne réponse à -16 - (-8)"
  - outil: ExoForge
    regle: "quand la réponse se décompose (signe et valeur absolue, valeur et unité, module et direction), noter chaque composante séparément : deux règles erronées différentes peuvent avoir le même profil juste/faux"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "diagnostiquer une règle erronée à partir du profil de réponses sur plusieurs questions (les réponses fausses elles-mêmes, pas seulement juste/faux), et signaler les profils compatibles avec plusieurs règles"
    niveau: C
    transferabilite: moyenne
---

# L'espace des règles : relier les réponses aux erreurs types (Tatsuoka, 1983)

Tatsuoka, K. K. (1983). Rule Space: An Approach for Dealing with Misconceptions Based on Item Response Theory. *Journal of Educational Measurement*, 20(4), 345-354. [DOI](https://doi.org/10.1111/j.1745-3984.1983.tb00212.x)

**En une phrase.** En arithmétique des relatifs, beaucoup de règles fausses donnent la bonne réponse sur certaines questions et deux règles fausses peuvent produire le même profil juste/faux ; l'article propose de noter séparément les composantes de la réponse et de placer chaque élève dans un espace où chaque règle erronée a sa position, ce qui fonde le diagnostic par erreurs types (mal-rules).

## La source

| | |
| --- | --- |
| **Équipe** | Computer-based Education Research Laboratory, université de l'Illinois (système PLATO) ; psychométrie, tests adaptatifs. |
| **Nature** | Académique ; financement de l'Office of Naval Research (contrat N00014-79-C-0752) (p. 345). L'autrice s'appuie surtout sur ses propres rapports. |
| **Support** | *Journal of Educational Measurement* (NCME), revue de référence en mesure. |
| **Audience** | 930 citations (OpenAlex, 08/11/2026) : article fondateur des modèles diagnostiques cognitifs. |
| **Reproductibilité** | Moyenne : formules et paramètres publiés (tableau 3) ; descriptions des 47 règles dans un rapport technique séparé ; données non publiques. |

## Ce que fait l'étude

- **Problème** (p. 345-346) : les programmes qui diagnostiquent les règles fausses (DEBUGGY : 77 règles en soustraction ; SIGNBUG : 89 en relatifs) sont coûteux à construire ; les indices de « réponses atypiques » repèrent les élèves mais pas leur erreur.
- **Composantes** (p. 346-347) : chaque réponse est notée deux fois, pour son signe et pour sa valeur absolue ; plus de 99 % des valeurs absolues sont la somme ou la différence des deux nombres.
- **Données** (p. 348) : 40 questions ouvertes (4 sous-tests parallèles de 10) passées par 172 élèves ; modèle de réponse à l'item à deux paramètres sur chaque composante.
- **Espace des règles** (p. 348-349, figure 1) : chaque règle erronée, simulée par programme, devient un point (score vrai « signe », score vrai « valeur absolue ») ; l'élève est rattaché à la règle la plus proche.

## Résultats

- **Juste pour une mauvaise raison** (p. 346) : la question -16 - (-8) reçoit la bonne réponse par 27 des 47 règles erronées décrites.
- **Profils confondus** (tableau 1, p. 346-347) : deux règles différentes donnent le même profil juste/faux (0000110000) sur 10 questions, avec des réponses différentes ; leurs profils de signe diffèrent.
- **Fréquences** (tableau 2, p. 350) : sur un sous-test, 27,5 % des profils sont tout justes ; le profil 0000110000 (4,9 %) correspond aux règles 16 ou 30, le profil tout faux (2,1 %) à six règles possibles.
- **Départager** (p. 352) : la vraisemblance de la règle 16 (0,0033) est environ double de celle de la règle 30 (0,0015) ; la distinction compte, car la règle 30 traduit une incompréhension grave et la 16 une erreur moins grave (p. 350).
- **Limites énoncées** (p. 352-353) : la décomposition ne marche pas partout (fractions mixtes) ; un même profil peut venir d'une erreur de concept ou d'une étourderie, et l'analyse des profils seule peut ne pas suffire.

## Avis critique

**Apport.** Démontre, chiffres à l'appui, que le score juste/faux jette l'information qui permet de reconnaître l'erreur, et qu'un énoncé mal choisi laisse une majorité de règles fausses passer pour justes. C'est la base théorique des formules fausses nommées et du rejet des tirages ambigus dans ExoForge.

**Points forts**
- Démonstration par énumération des règles, indépendante de l'échantillon.
- Méthode formalisée (scores vrais, vraisemblance) et limites franchement énoncées.
- Distinction entre erreurs graves et moins graves, utile pour le retour.

**Réserves**
1. **Importante** — Article de méthode : aucune validation du diagnostic contre un critère externe (entretien, correction), aucun taux de bons classements.
2. **Importante** — Domaine très étroit et décomposable (signe et valeur absolue) ; l'autrice signale que d'autres domaines ne le sont pas.
3. **Mineure** — Vraisemblances conditionnelles au niveau de l'élève, comparables seulement à niveau égal (p. 352) ; modèle à deux paramètres estimé sur 172 élèves.
4. **Mineure** — Scan JSTOR dont le texte est coupé en marge droite : chiffres relus dans les tableaux.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Des règles erronées peuvent donner la bonne réponse sur certaines valeurs | B | Démonstration par énumération (27 sur 47), indépendante des données |
| Noter les composantes séparément distingue des règles confondues par le juste/faux | C | Montré dans un domaine, généralisation non testée |
| L'espace des règles diagnostique correctement les élèves | D | Non validé dans l'article |

**Transférabilité** : forte pour le principe (en mécanique : signe et module d'une force, valeur et unité, sin et cos), faible pour la méthode statistique telle quelle.

**Pour conclure, il faudrait** coder dans ExoForge 5 à 10 formules fausses pour un exercice de statique paramétré, mesurer la part des tirages où l'une d'elles donne la bonne réponse, et comparer le diagnostic tiré des réponses fausses à une correction manuelle.

## Pour Forge

- **ExoForge** : rejet automatique des tirages où une formule fausse de la banque donne la bonne valeur (niveau C ; le mécanisme lui-même est établi).
- **ExoForge** : notation par composantes (signe, module, unité) quand la réponse s'y prête, avec retour sur la composante fausse (niveau C).
- **DiagForge** : diagnostic à partir du profil des réponses fausses sur plusieurs questions ; signaler les profils ambigus plutôt que trancher (niveau C).
- Renvois : `sikurajapathi2023` et `greenhow2015` (mal-rules en ligne, fiches de l'axe) ; `gross2012` (erreurs d'exécution en statique) ; `klingbeil2024` (diagnostic sur plusieurs questions).
