# scripts/quizforge

Code de QuizForge (Excel vers Moodle). Mode d'emploi : [outils/quizforge](../../outils/quizforge/README.md). Le code de DiagForge (commande `bilan`) est dans [`scripts/diagforge`](../diagforge/README.md).

| Fichier | Rôle |
| --- | --- |
| `quizforge.py` | point d'entrée : commandes, lecture des classeurs, écriture XML / GIFT / YAML, profils, assistant |
| `QuizForge.bat` | lanceur Windows : double-clic = assistant ; classeurs glissés dessus = conversion |
| `qualite.py` | contrôles d'écriture des questions (`valider`), score au hasard |
| `outils/pointeur.html` | pointeur de zones : questions glisser-déposer sur image et marqueurs (à ouvrir dans le navigateur) |
| `schema/` | génération des schémas de Wöhler pour les questions sur image |

Les chemins du dépôt (profils, style, données privées, sorties) sont centralisés dans [`scripts/commun/chemins.py`](../commun/chemins.py).
