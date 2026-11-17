"""DiagForge — analyse des résultats d'un test Moodle et de la qualité de ses questions.

Usage : ::

    python scripts/diagforge/diagforge.py <exports Moodle…> [-q questions.xml] [-t toutes|premiere|derniere|meilleure]
                                          [-s bilan.xlsx] [-r roster.csv] [--sans-images] [-p profil]

Mêmes options que la commande ``bilan`` de QuizForge (``python scripts/quizforge/quizforge.py bilan …``), qui
reste disponible : le profil d'établissement (couleur principale, mode de tirage) est lu par QuizForge.

Licence : GPL v3.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "quizforge"))
import quizforge  # noqa: E402


def main(argv=None):
    """Lance le bilan avec les arguments de la ligne de commande (voir l'en-tête du module)."""
    return quizforge.main(["bilan"] + list(sys.argv[1:] if argv is None else argv))


if __name__ == "__main__":
    main()
