scripts.diagforge.tirage
========================

.. py:module:: scripts.diagforge.tirage

.. autoapi-nested-parse::

   DiagForge — tirage des questions d'un quiz : mode observé, équité entre questions tirées, rétention des rappels.

   Modes (bloc ``quiz`` du profil QuizForge, voir ``outils/quizforge/README.md``) :

   - ``commun`` : toutes les tentatives d'un même test contiennent les mêmes questions ;
   - ``partiel`` : chaque tentative tire k questions sur N dans chaque catégorie ;
   - ``mixte`` : questions de la séance communes à tous, rappels des séances précédentes tirés.

   La séance d'une question vient de son tag ``S01``, ``S02``… (QuizForge, colonne Séance) ou du champ ``seance`` de la banque YAML.
   Les seuils d'équité sont des règles d'usage (niveau D) : aucune fiche de la bibliographie ne porte sur l'équité entre
   versions tirées. La rétention compare, pour une même question, la réussite le jour de sa séance et la réussite en rappel
   (pratique de récupération espacée : ``reference/A_tests_retroaction/yang2021.md``, ``murray2025.md``).



Attributes
----------

.. autoapisummary::

   scripts.diagforge.tirage.ECART_EQUITE
   scripts.diagforge.tirage.N_MIN


Functions
---------

.. autoapisummary::

   scripts.diagforge.tirage.seance_question
   scripts.diagforge.tirage.test_de_base
   scripts.diagforge.tirage.analyser_tirage


Module Contents
---------------

.. py:data:: ECART_EQUITE
   :value: 0.3


.. py:data:: N_MIN
   :value: 10


.. py:function:: seance_question(q) -> int | None

   Renvoie le numéro de séance d'une question de la banque, ou ``None``.

   Le champ entier ``seance`` l'emporte ; sinon le premier tag de la forme ``S01``, ``s2``… (1 à 3 chiffres).


.. py:function:: test_de_base(test: str) -> str

   Retire le suffixe de groupe d'un nom de test : « Quizz1_SMA » → « Quizz1 » (même test passé par plusieurs groupes).

   Le suffixe retiré compte 1 à 8 caractères alphanumériques et n'est pas uniquement numérique.


.. py:function:: analyser_tirage(obs, infos, declare=None)

   Analyse le tirage des questions : mode observé par test, équité entre questions tirées, rétention.

   ``obs`` : observations par question ; ``infos`` : informations par question (dont ``banque``) ;
   ``declare`` : mode déclaré dans le profil, comparé au mode observé.

   Renvoie un dictionnaire ``{"tests": [...], "equite": [...], "retention": [...], "lignes": [lignes de synthèse],
   "bloc": {nom: bloc}, "seance": {nom: séance}}``.


