# AtelierForge — versions et registre (`registre.yaml`, `version.yaml`)

Une conversion de quiz faite pour un cours, ou la construction d'un exercice, devient une **version** : elle est rangée dans l'édition (ou dans le cours pour un extrait commun à plusieurs déclinaisons), sous un nom explicite, et **n'est jamais écrasée**. Le **registre** de l'édition suit chaque version jusqu'au bilan. Ainsi, on sait toujours quel fichier a été déposé dans Moodle et à quel test se rapporte un bilan.

Statut : écrit par `scripts/commun/registre.py`, rempli par QuizForge (`convertir --cours`), ExoForge (`build.py --cours`), DiagForge (bilan) et l'atelier (écran « Registre »). Les capsules suivront, une fois séparés le contenu d'une capsule et la signalétique d'une édition.

## Dossiers

```text
data/cours/<cours>/<déclinaison>/<année>/
├── registre.yaml
├── quiz/<classeur>/S03_v2/          # S03 si un plan de séance est demandé ; v2 : numéro par classeur
│   ├── <classeur>_S03_v2_moodle.xml (et _EN, _FR…), GIFT, _banque.yaml, _plan.md, _rapport.txt
│   └── version.yaml
└── exercices/<id>/v2/
    ├── <id>_v2_scorm12.zip
    └── version.yaml
```

Reconvertir (ou reconstruire) sans changer le classeur ni les réglages (la fiche, ses médias, le profil) ne crée pas de version : le journal indique « identique à la version … ». Sans cours choisi, rien ne change : QuizForge réécrit `<classeur>_QuizForge/`.

## `version.yaml`

| Clé | Contenu |
| --- | --- |
| `id`, `version`, `date` | `modele_QuizForge/v1`, numéro, date de la conversion |
| `classeur` ou `source` | fichier converti (classeur) ou fiche construite (exercice) |
| `empreinte_classeur`, `empreinte` | empreintes du fichier et de l'ensemble fichier + réglages (sert à reconnaître une reconversion identique) |
| `reglages` | profil, catégorie, nom, tags, séance, effectif, formats… tels qu'appliqués |
| `fichiers` | fichiers produits |
| `questions` | nom et catégorie de chaque question (quiz) : sert à DiagForge pour reconnaître la version d'un test |

## `registre.yaml`

Une ligne par version (la plus récente en dernier) :

| Clé | Contenu |
| --- | --- |
| `id`, `genre`, `version`, `dossier` | identifiant, `quiz` ou `exercice`, numéro, dossier de la version |
| `etat` | `convertie` (« construit » pour un exercice), `importee` (dans Moodle), `passee` (par les étudiants), `bilan`, `abandonnee` |
| `dates` | date de chaque état atteint |
| `test_moodle`, `remarques` | nom du test dans Moodle, notes libres |
| `bilans` | bilans DiagForge rattachés (classeur et fiche du professeur) |
| `utilisee_par` | pour un extrait commun (registre du cours) : éditions qui l'utilisent (`epf-msd/2026`) |

L'atelier change l'état, le test Moodle, les remarques et « utilisée par » (bouton **Registre** dans Questions, Exercices et l'écran Cours). DiagForge, au bilan, compare les noms des questions de l'export XML de Moodle aux versions des registres : il écrit la version reconnue dans un onglet « Version » du classeur de bilan (avec les questions absentes ou en plus) et inscrit le bilan au registre, état « bilan fait ».

## Exemple : l'édition de démonstration

```{literalinclude} ../../donnees/cours/traction/ecole1-meca/2026/registre.yaml
:language: yaml
```
