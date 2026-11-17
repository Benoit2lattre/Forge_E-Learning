# scripts/quizforge

Code de QuizForge (Excel vers Moodle) et de DiagForge. Modes d'emploi : [outils/quizforge](../../outils/quizforge/README.md), [outils/diagforge](../../outils/diagforge/README.md).

| Fichier | Rôle |
| --- | --- |
| `quizforge.py` | point d'entrée : commandes, lecture des classeurs, écriture XML / GIFT / YAML, profils, assistant |
| `QuizForge.bat` | lanceur Windows : double-clic = assistant ; classeurs glissés dessus = conversion |
| `bilan.py` | DiagForge : lecture et jonction des exports Moodle, indicateurs, alertes, questions à revoir |
| `bilan_sorties.py` | sorties du bilan : onglets du classeur, fiche du professeur (HTML) |
| `graphiques.py` | images PNG du bilan (matplotlib) |
| `outils/pointeur.html` | pointeur de zones : questions glisser-déposer sur image et marqueurs (à ouvrir dans le navigateur) |
| `outils/promotion_fictive.py` | promotion fictive au format des exports Moodle, pour tester le bilan |
| `schema/` | génération des schémas de Wöhler pour les questions sur image |

Les chemins du dépôt (profils, style, données privées, sorties) sont centralisés dans [`scripts/commun/chemins.py`](../commun/chemins.py).
