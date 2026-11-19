scripts.diagforge.diagforge
===========================

.. py:module:: scripts.diagforge.diagforge

.. autoapi-nested-parse::

   DiagForge — analyse des résultats d'un test Moodle et de la qualité de ses questions.

   Usage : ::

       python scripts/diagforge/diagforge.py <exports Moodle…> [-q questions.xml] [-t toutes|premiere|derniere|meilleure]
                                             [-s bilan.xlsx] [-r roster.csv] [--sans-images] [-p profil]

   Mêmes options que la commande ``bilan`` de QuizForge (``python scripts/quizforge/quizforge.py bilan …``), qui
   reste disponible : le profil d'établissement (couleur principale, mode de tirage) est lu par QuizForge.

   Licence : GPL v3.



Functions
---------

.. autoapisummary::

   scripts.diagforge.diagforge.main


Module Contents
---------------

.. py:function:: main(argv=None)

   Lance le bilan avec les arguments de la ligne de commande (voir l'en-tête du module).


