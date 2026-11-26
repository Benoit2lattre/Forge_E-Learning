scripts.forge.questions_bilans
==============================

.. py:module:: scripts.forge.questions_bilans

.. autoapi-nested-parse::

   Atelier Forge — écrans « Questions » (QuizForge) et « Bilans » (DiagForge) : listes et commandes.

   Questions : classeurs QuizForge de ``data/quizforge`` et des exemples ; valider, convertir pour Moodle (avec plan de
   séance), créer un classeur modèle, réunir un classeur et sa traduction.
   Bilans : dossiers d'exports Moodle de ``data/diagforge`` et des exemples ``donnees/diagforge`` ; faire le bilan.

   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.forge.questions_bilans.ICI
   scripts.forge.questions_bilans.QUIZFORGE
   scripts.forge.questions_bilans.DIAGFORGE
   scripts.forge.questions_bilans.EXEMPLES_Q
   scripts.forge.questions_bilans.EXEMPLES_D


Functions
---------

.. autoapisummary::

   scripts.forge.questions_bilans.rel
   scripts.forge.questions_bilans.classeurs
   scripts.forge.questions_bilans.classeur_valide
   scripts.forge.questions_bilans.texte_court
   scripts.forge.questions_bilans.dossiers_exports
   scripts.forge.questions_bilans.dossier_valide
   scripts.forge.questions_bilans.fichier_dans
   scripts.forge.questions_bilans.liens_bilan


Module Contents
---------------

.. py:data:: ICI

.. py:data:: QUIZFORGE

.. py:data:: DIAGFORGE

.. py:data:: EXEMPLES_Q

.. py:data:: EXEMPLES_D

.. py:function:: rel(p: pathlib.Path) -> str

.. py:function:: classeurs(ajoutes: list | None = None) -> list[dict]

   Classeurs QuizForge : data/quizforge (privés), classeurs ajoutés par l'atelier, puis exemples.


.. py:function:: classeur_valide(chemin: str) -> pathlib.Path

.. py:function:: texte_court(v: str, maxi: int = 80) -> str

.. py:function:: dossiers_exports() -> list[dict]

   Dossiers qui contiennent un export « notes » de Moodle (CSV ou classeur), avec leur bilan s'il existe.


.. py:function:: dossier_valide(chemin: str) -> pathlib.Path

.. py:function:: fichier_dans(d: pathlib.Path, nom: str, extensions: tuple) -> pathlib.Path

   Fichier ``nom`` du dossier ``d`` (nom simple) ou chemin choisi par Parcourir.


.. py:function:: liens_bilan(d: pathlib.Path, debut: float) -> dict

