---
cle: heckler2016
reference: "Heckler, A. F. et Mikula, B. D. (2016). Factors affecting learning of vector math from computer-based practice: Feedback complexity and prior knowledge. Physical Review Physics Education Research, 12(1), 010134."
doi: 10.1103/PhysRevPhysEducRes.12.010134
axe: [A2]
type_etude: deux essais randomisés individuels (plan factoriel complet KCR x EF dans l'expérience 2), une séance d'entraînement sur ordinateur
public: 456 étudiants de physique générale à l'université (mécanique et électromagnétisme), université publique des États-Unis
lecture: texte complet, 09/11/2026
regles:
  - outil: QuizForge
    regle: "rétroaction de chaque question d'entraînement = juste/faux + courte explication de la règle en jeu (mots, équation ou schéma), pas seulement la bonne réponse"
    niveau: B
    transferabilite: forte
    note: "l'explication profite surtout aux étudiants qui ont peu de prérequis ; ajouter la bonne réponse à l'explication n'apporte ni gain ni perte significatifs"
  - outil: ExoForge
    regle: "une explication générale par type d'étape (règle de calcul, valable quelles que soient les valeurs tirées) suffit ; inutile de rédiger une explication propre à chaque jeu de paramètres"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "analyser l'effet d'un entraînement séparément selon le niveau de départ (score aux premières questions de la série ou note du cours) : un effet moyen nul peut cacher un gain chez les plus faibles"
    niveau: C
    transferabilite: forte
---

# Rétroaction et prérequis en calcul vectoriel (Heckler et Mikula, 2016)

Heckler, A. F. et Mikula, B. D. (2016). Factors affecting learning of vector math from computer-based practice: Feedback complexity and prior knowledge. *Physical Review Physics Education Research*, 12(1), 010134. [DOI](https://doi.org/10.1103/PhysRevPhysEducRes.12.010134)

**En une phrase.** Sur 24 questions d'entraînement aux produits scalaire et vectoriel, une explication générale de la règle après chaque réponse fait mieux que le seul juste/faux ou que la bonne réponse, surtout pour les étudiants qui partent de bas ; pour QuizForge, cela justifie une rétroaction explicative courte, écrite une fois par type de question.

## La source

| | |
| --- | --- |
| **Équipe** | Département de physique de l'université d'État de l'Ohio (recherche en didactique de la physique) ; les deux auteurs ont construit le test d'évaluation (p. 6). |
| **Nature** | Académique ; financement par un centre de recherche sur les matériaux de la NSF (MRSEC, p. 13). Les auteurs évaluent un module qu'ils ont conçu. |
| **Support** | *Physical Review Physics Education Research* (American Physical Society), libre accès. |
| **Audience** | 36 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Bonne : test d'évaluation complet et exemples de questions et d'explications en matériel supplémentaire (p. 4-5) ; données non publiées. La démarche se refait ; les chiffres ne se vérifient que sur les résumés publiés. Les pages citées sont celles de l'article (010134-1 à -15). |

## Ce que fait l'étude

- **Public** (p. 3-4) : 456 étudiants tirés au sort parmi plus de 1000 inscrits par cours ; expérience 1 en mécanique, premier semestre (n = 206, produits vectoriels peu enseignés) ; expérience 2 en électromagnétisme, second semestre (n = 250, produits enseignés en cours). Participation créditée quelle que soit la performance ; 444 sur 456 ont tout fait.
- **Entraînement** (p. 4) : 24 questions en 4 blocs de 6 types (signe, norme, comparaison, pour chaque produit), en salle d'expérience, logiciel E-Prime, 10 à 15 min ; rétroaction immédiate après chaque réponse.
- **Conditions** (tableau II, p. 4) : témoin sans entraînement ; KR (juste/faux) ; KR + KCR (bonne réponse) ; KR + EF (explication générale de la règle, propre au type de question et non aux valeurs) ; KR + KCR + EF (expérience 2 seulement). Mêmes questions dans toutes les conditions.
- **Mesure** (p. 4-6) : test papier DotCross de 14 questions, environ 20 min après l'entraînement, sans rétroaction ; questions proches mais non identiques (transfert proche) ; alpha = 0,88.
- **Prérequis** (p. 6) : deux mesures, la note du cours (médiane) et le score aux 6 premières questions d'entraînement (« pré-score »).

## Résultats

- **Effet de l'entraînement** (p. 6, 8) : toutes les conditions font mieux que le témoin ; d = 0,5 (KR) à 1,0 (KR + EF) dans l'expérience 1, d = 0,46 (KR) à 1,1 (KR + KCR + EF) dans l'expérience 2.
- **Expérience 1, faibles prérequis** (p. 6-7) : sous la médiane de la note, KR + EF > KR (p = 0,02) et > KR + KCR (p = 0,03) ; même résultat avec le pré-score (p = 0,037 et 0,022). Au-dessus de la médiane, pas de différence (p = 0,34 et 0,14).
- **Expérience 2** (p. 8, tableau V p. 11) : scores moyens témoin 61 %, KR 74 %, KR + KCR 81 %, KR + EF 82 %, KR + KCR + EF 87 % ; seule la différence KR + KCR + EF contre KR est significative deux à deux (Tukey, p = 0,016). Dans l'analyse à deux facteurs (tableau III, p. 8), effet de EF significatif (F = 13,8, p < 0,001, η² partiel = 0,07), effet de KCR non significatif (p = 0,14), pas d'interaction KCR x EF ; interaction EF x pré-score (p = 0,002) : l'explication aide les faibles pré-scores.
- **Temps** (tableau IV, p. 9) : l'explication allonge l'entraînement de 10 à 20 % (1 à 2 min) ; efficacité (gain par unité de temps) plus élevée avec EF mais non significative (p = 0,076 et 0,22).
- **Lecture des explications** (p. 10-11) : temps de lecture plus long après une erreur qu'après une réussite ; il chute après une ou deux lectures par type de question ; au 4e essai d'un même type, environ 10 % des étudiants se trompent encore et ne lisent presque plus l'explication.
- **Perception** (p. 11-12) : proficience déclarée la plus haute avec KR + KCR + EF ; chez les faibles pré-scores, l'effet de l'entraînement est plus fort quand l'étudiant juge le sujet important pour le cours (corrélationnel).

## Avis critique

**Apport.** Essai randomisé en physique universitaire, sur une compétence de calcul de base de nos cours, qui sépare les effets de la bonne réponse et de l'explication dans un plan factoriel complet ; il montre que l'avantage de l'explication tient aux étudiants faibles.

**Points forts**
- Tirage au sort individuel dans de grands cours réels ; groupes comparables sur la note (p = 0,25, p. 4).
- Seule la rétroaction change ; mêmes questions et même ordre.
- Deux mesures de prérequis concordantes ; données de temps qui montrent l'usage de l'explication.

**Réserves**
1. **Importante** — Séance unique en salle d'expérience, test 20 min après : rien sur la rétention ni sur des problèmes plus complexes (les auteurs le disent, p. 13).
2. **Importante** — L'effet « faibles prérequis » vient de partages à la médiane et de tests post hoc ; dans l'expérience 2, les trois conditions à une seule information ne diffèrent pas (p = 0,21, p. 8).
3. **Mineure** — Les scores de l'expérience 1 ne sont donnés qu'en figure ; pas d'intervalles de confiance.
4. **Mineure** — Compétence procédurale simple (règles de produit) ; l'explication générale suffit peut-être parce que la règle est courte.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Un entraînement court avec rétroaction améliore le calcul vectoriel par rapport à rien | B | Deux essais randomisés concordants, mais une séance |
| L'explication générale fait mieux que juste/faux | B | Effet principal de EF dans un plan factoriel randomisé |
| L'explication profite surtout aux étudiants faibles | C | Interactions et partages à la médiane, post hoc |
| La bonne réponse ajoutée à l'explication n'apporte rien | C | Absence d'effet significatif, effectifs d'environ 50 par groupe |

**Transférabilité** : forte. Étudiants d'université en physique, calcul vectoriel utilisé en mécanique ; rétroaction automatique à questions fermées, comme dans Moodle.

**Pour conclure, il faudrait** refaire la comparaison dans un quiz Moodle de mécanique en comparant, par tirage au sort, « juste/faux + bonne réponse » et « juste/faux + explication », avec un test à une semaine.

## Pour Forge

- **QuizForge** : remplir la colonne `Rétroaction` (rétroaction générale) avec une explication courte de la règle ; ne pas se contenter du juste/faux ni de la bonne réponse (niveau B). Dans Moodle, le comportement « rétroaction immédiate » ou « interactif » affiche cette explication question par question ; en mode « différé », elle n'apparaît qu'à la relecture.
- **ExoForge** : une explication par type d'étape, indépendante des valeurs tirées, suffit (niveau C).
- **DiagForge** : analyser les résultats par niveau de départ (niveau C).
- Concorde avec [vanderkleij2015](vanderkleij2015.md) (explication > bonne réponse > juste/faux) et avec [attali2017](attali2017.md) (l'explication sert après une erreur : ici, temps de lecture plus long après erreur). La chute du temps de lecture après une ou deux lectures pose une question ouverte : faut-il varier l'explication, ou placer les questions difficiles en début de série (p. 13) ?
