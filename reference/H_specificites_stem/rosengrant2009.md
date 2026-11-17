---
cle: rosengrant2009
reference: "Rosengrant, D., Van Heuvelen, A. et Etkina, E. (2009). Do students use and understand free-body diagrams? Physical Review Special Topics - Physics Education Research, 5, 010108."
doi: 10.1103/PhysRevSTPER.5.010108
axe: [H2]
type_etude: étude corrélationnelle sur copies d'examen (1 465 solutions de 245 étudiants, deux années) et entretiens de verbalisation (6 étudiants) ; groupe de comparaison d'un autre enseignant sur 2 problèmes
public: cours de physique algébrique de 1re année pour étudiants en sciences (environ 500 par an), même enseignant, pédagogie centrée sur les représentations (ISLE), États-Unis
lecture: texte complet, 10/11/2026
regles:
  - outil: ExoForge
    regle: "dans un exercice de statique ou de dynamique, faire construire le diagramme du corps isolé comme étape vérifiée avant les équations : liste des forces (objet qui l'exerce, objet qui la subit), sens ; signaler force manquante, force en trop et sens faux"
    niveau: C
    transferabilite: forte
    note: "corrélation, pas causalité : 85 % de réussite avec un diagramme correct contre 38 % avec un diagramme faux"
  - outil: DiagForge
    regle: "quand le diagramme du corps isolé est saisi, l'utiliser comme premier diagnostic d'une réponse fausse : un diagramme faux annonce l'échec plus qu'une absence de diagramme"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "pour une question numérique sur la 2e loi de Newton, leurres issus des erreurs de diagramme et de signe : poids seul (mg), mg + ma au lieu de mg - ma, ma seul"
    niveau: D
    transferabilite: forte
    note: "leurres visibles dans les questions d'examen publiées (annexe B) ; leur choix n'est pas analysé"
  - outil: ExoForge
    regle: "après la réponse, retour qui fait comparer le résultat au diagramme (ordre de grandeur et sens des forces) plutôt que de seulement donner la valeur attendue"
    niveau: D
    transferabilite: forte
---

# Les étudiants utilisent-ils le diagramme du corps isolé ? (Rosengrant et al., 2009)

Rosengrant, D., Van Heuvelen, A. et Etkina, E. (2009). Do students use and understand free-body diagrams? *Physical Review Special Topics - Physics Education Research*, 5, 010108. [DOI](https://doi.org/10.1103/PhysRevSTPER.5.010108)

Article numéroté 010108 : la fiche cite les pages 010108-N sous la forme p. N.

**En une phrase.** Dans un cours qui enseigne explicitement le diagramme du corps isolé, 58 % des étudiants en tracent un spontanément sur des QCM d'examen non notés sur la démarche, et ceux dont le diagramme est correct trouvent la bonne réponse dans 85 % des cas contre 38 % quand le diagramme est faux (49 % sans trace de diagramme) : un diagramme faux est un signal d'échec plus fort que l'absence de diagramme.

## La source

| | |
| --- | --- |
| **Équipe** | Physique, Kennesaw State University (Rosengrant) ; physique et sciences de l'éducation, Rutgers (Van Heuvelen, Etkina) (p. 1). Van Heuvelen et Etkina sont auteurs de la méthode et du guide d'activités utilisés dans le cours (p. 3). |
| **Nature** | Académique ; financement de la National Science Foundation (DUE 0241078 et DUE 0336713) (p. 11). Les auteurs évaluent un cursus qu'ils ont conçu. |
| **Support** | *Physical Review Special Topics - Physics Education Research*, revue à comité de lecture, libre accès. |
| **Audience** | 187 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Moyenne : grille de codage publiée (tableau II) avec un accord de 90 % entre deux codeurs sur un sous-ensemble (p. 4) ; 4 des 12 problèmes en annexe, les autres dans une thèse ; copies non publiques. La démarche se refait sur toute copie de mécanique. |

## Ce que fait l'étude

- **Public et contexte** (p. 3-4) : cours de physique algébrique en deux semestres, environ 500 étudiants par an, même enseignant, deux années ; travail en groupes, système de vote en amphithéâtre ; 40 % des séances de résolution consacrées à des tâches de représentation.
- **Échantillon** (p. 4) : 125 puis 120 étudiants tirés au hasard (environ 25 % de chaque promotion), représentatifs des notes (test de Kruskal-Wallis). Groupe de comparaison : 479 étudiants d'un autre enseignant, sans enseignement explicite du diagramme, sur 2 problèmes seulement.
- **Mesure** (p. 4-5) : 12 QCM d'examen (5 la 1re année, 7 la 2e ; mécanique et électrostatique), choisis parce que difficiles sans diagramme ; ni consigne ni crédit pour le diagramme. Codage du diagramme : 0 pas de trace, 1 inadéquat (forces manquantes ou en trop, sens faux), 2 à améliorer (forces justes mais étiquettes, axes ou longueurs fautifs), 3 correct (tableau II).
- **Entretiens** (p. 7-10) : 6 étudiants (2 forts, 2 faibles, 2 venant d'un cours traditionnel), un problème de deux boules chargées suspendues, verbalisation à voix haute, puis entretien de fin de semestre.

## Résultats

- **Usage** (tableau III, p. 5) : 58 % des solutions avec diagramme en moyenne (de 33,6 à 80,8 % selon le problème) ; groupe de comparaison 22,5 % et 10,9 % sur les deux problèmes communs, contre 80,8 % et 56,0 % dans le cours étudié.
- **Réussite selon le diagramme** (tableaux IV et V, p. 6) :

| Code du diagramme | Réussite | Solutions |
| --- | --- | --- |
| 3 correct | 85 % | 251/295 |
| 2 à améliorer | 71 % | 261/370 |
| 0 pas de trace | 49 % | 304/619 |
| 1 inadéquat | 38 % | 69/181 |
| Ensemble | 60 % | 885/1 465 |

- **Test** (p. 7) : khi-deux sur les 1 465 solutions, p < 0,001.
- **Erreurs relevées dans les entretiens** (p. 8-10) : orientation des fils fausse reprise telle quelle dans le diagramme, somme des forces non nulle à l'équilibre, 2e loi écrite sans composantes, conversion d'unités (microcoulombs), signe de la charge ; tension prise égale au poids (30 N) corrigée par le diagramme.
- **Usage selon le niveau** (tableaux VI et VII, p. 10) : les deux étudiants forts utilisent le diagramme pour vérifier leur résultat et la cohérence entre représentations ; les faibles le tracent comme une étape de procédure sans y revenir ; une étudiante venant du cours traditionnel refuse d'en tracer.
- **Leurres des QCM publiés** (annexe B, p. 12) : pompier de 100 kg descendant avec une accélération de 4 m/s² : 1 000 N (mg), 1 400 N (mg + ma), 400 N (ma), bonne réponse 600 N ; ascenseur de 1 000 kg freinant en descente : 10 000 N (mg), 6 000 N (mg - ma), 4 000 N (ma), bonne réponse 14 000 N.

## Avis critique

**Apport.** Relie la qualité du diagramme du corps isolé à la réussite sur près de 1 500 solutions réelles, avec une grille de codage simple (forces manquantes ou en trop, sens, étiquettes) directement transposable en contrôle automatique d'une étape d'ExoForge.

**Points forts**
- Copies réelles d'examen, sans consigne de tracer : l'usage observé est spontané.
- Grille publiée et accord entre codeurs mesuré.
- Volet qualitatif qui explique le chiffre : le diagramme sert d'outil de vérification aux meilleurs.

**Réserves**
1. **Majeure** — Corrélation, pas causalité : les étudiants qui tracent un diagramme correct sont probablement aussi les plus forts ; aucune covariable de niveau. On ne peut pas conclure que faire tracer le diagramme fait réussir.
2. **Importante** — Le khi-deux traite 1 465 solutions comme indépendantes alors qu'elles viennent de 245 étudiants (5 à 7 chacune) (p. 7) : la valeur de p est trop optimiste.
3. **Importante** — Code 0 = pas de trace sur la copie, pas absence de diagramme (diagramme mental ou sur brouillon non ramassé, p. 4 et 11) : le groupe 0 est hétérogène.
4. **Mineure** — Comparaison avec un autre enseignant sur 2 problèmes seulement (17 % contre 68 % en moyenne, p. 5, soit la moyenne des valeurs du tableau III [calcul]), dont l'un choisi parce que le cours étudié y trace le plus de diagrammes (80,8 %, p. 5). Cours de physique de 1re année, non de mécanique de l'ingénieur.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Un diagramme correct va avec une réponse juste, un diagramme faux avec une réponse fausse | C | Grand nombre de solutions, mais corrélation et non-indépendance |
| Un enseignement explicite du diagramme en fait tracer davantage | C | Comparaison avec un autre enseignant sur 2 problèmes |
| Les étudiants forts se servent du diagramme pour vérifier | D | 6 entretiens |

**Transférabilité** : forte pour le mécanisme et la grille de codage (statique et dynamique en L3) ; moyenne pour les pourcentages (physique de 1re année, QCM).

**Pour conclure, il faudrait** tirer au sort, dans ExoForge, une version avec étape « diagramme du corps isolé » vérifiée et une version sans, et comparer la réussite aux mêmes problèmes posés ensuite sans étape.

## Pour Forge

- **ExoForge** : étape « diagramme du corps isolé » vérifiée (forces, objet qui l'exerce, sens) avant les équations (niveau C).
- **DiagForge** : diagnostic d'abord sur le diagramme quand il est saisi (niveau C).
- **QuizForge** : leurres de la 2e loi de Newton (mg, mg + ma, ma) (niveau D).
- **ExoForge** : retour qui fait confronter le résultat au diagramme (niveau D).
- Catalogue d'erreurs : « force manquante », « force en trop », « sens faux » (code 1) ; « étiquette ou axe absent, longueur fausse » (code 2). Renvois : [steif2005](steif2005.md) (la force manquante échappe au QCM), [gross2012](gross2012.md) (erreurs de diagramme dans les copies de statique), [bruhl2022](bruhl2022.md).
