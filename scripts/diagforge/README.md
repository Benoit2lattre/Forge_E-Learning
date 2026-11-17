# scripts/diagforge

Code de DiagForge (analyse des résultats Moodle). Mode d'emploi : [outils/diagforge](../../outils/diagforge/README.md).

| Fichier | Rôle |
| --- | --- |
| `diagforge.py` | point d'entrée (mêmes options que `quizforge.py bilan`) |
| `bilan.py` | lecture et jonction des exports Moodle, indicateurs, alertes, questions à revoir |
| `bilan_sorties.py` | sorties du bilan : onglets du classeur, fiche du professeur (HTML), images par groupe |
| `graphiques.py` | images PNG du bilan (matplotlib) |
| `tirage.py` | analyse du tirage des questions : mode observé, équité entre étudiants, rétention |
| `outils/promotion_fictive.py` | promotion fictive au format des exports Moodle, pour tester le bilan |

Le profil d'établissement (couleur principale, mode de tirage) est lu par QuizForge (`scripts/quizforge/quizforge.py`).
