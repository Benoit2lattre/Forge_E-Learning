scripts.commun.cours_options
============================

.. py:module:: scripts.commun.cours_options

.. autoapi-nested-parse::

   Forge E-Learning — option ``--cours`` commune aux outils : réglages d'un cours, d'une déclinaison, d'une édition.

   ``--cours traction``, ``--cours traction:ecole1-meca`` ou ``--cours traction:ecole1-meca/2026`` (déclinaison et édition facultatives :
   la seule déclinaison du cours, puis son édition en cours). Les options données sur la ligne de commande l'emportent ;
   les étiquettes du cours s'ajoutent à celles données.



Functions
---------

.. autoapisummary::

   scripts.commun.cours_options.resoudre
   scripts.commun.cours_options.seance
   scripts.commun.cours_options.prochaine
   scripts.commun.cours_options.decrire_seance


Module Contents
---------------

.. py:function:: resoudre(spec: str) -> dict

   Réglages pour ``spec`` : profil, étiquettes, catégorie Moodle, langues, séances, effectif, dossiers, libellé.


.. py:function:: seance(r: dict, n: int) -> dict | None

.. py:function:: prochaine(r: dict, jour: datetime.date | None = None) -> dict | None

   Première séance datée d'aujourd'hui ou après (sinon None).


.. py:function:: decrire_seance(s: dict | None) -> str

