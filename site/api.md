# Référence API

La référence du code est générée à partir des docstrings des modules de `scripts/` par [sphinx-autoapi](https://sphinx-autoapi.readthedocs.io/), sans importer ni exécuter le code. Les moteurs HTML (pages d'exercice, lecteurs, éditeurs) et les bibliothèques embarquées (`vendor/`) n'y figurent pas.

| Dossier | Contenu |
| --- | --- |
| `scripts/quizforge/` | QuizForge (conversion des classeurs, contrôles d'écriture, tirage) et DiagForge (analyse des résultats : `bilan`, `bilan_sorties`, `graphiques`, `tirage`) |
| `scripts/exoforge/` | ExoForge : construction des exercices, moteur générique, macros LaTeX |
| `scripts/capsuleforge/` | CapsuleForge : enregistrement, formats 1 et 2, lecture de PowerPoint, transcription, relecture, traduction, voix, vidéo, construction des lecteurs et des paquets SCORM |
| `scripts/commun/` | chemins communs, contrôle du dépôt avant commit |

Les pages de la référence sont listées dans le menu, sous cette page.
