scripts.capsuleforge.approj
===========================

.. py:module:: scripts.capsuleforge.approj

.. autoapi-nested-parse::

   CapsuleForge — reprise d'une simulation enregistrée dans ActivePresenter (.approj) en capsule.yaml.

   Lecture seule : le projet est d'abord copié dans un dossier temporaire (il peut être ouvert dans
   ActivePresenter, avec ses fichiers -wal et -shm), puis lu avec SQLite. Rien n'est écrit à côté du projet.

   Ce qui est repris, diapositive par diapositive : l'image de fond, la trajectoire de la souris,
   la zone de clic (nom du contrôle compris) et le type d'action. L'audio, les bulles mises en forme et les
   objets ajoutés à la main ne sont pas repris (les bulles sont réécrites par assemblage.bulle_auto).

   Unités d'ActivePresenter 10 (constatées sur un projet de simulation) : positions et tailles en
   millièmes de pixel (2560000 = 2560 px).
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.approj.MILLI


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.approj.importer


Module Contents
---------------

.. py:data:: MILLI
   :value: 1000.0


.. py:function:: importer(approj: pathlib.Path, sortie: pathlib.Path, titre: str | None = None) -> dict

   Lit un projet ActivePresenter (.approj) et renvoie la capsule correspondante (dictionnaire).

   Les images de fond sont écrites dans ``<sortie>/images/`` ; le titre par défaut est le nom du projet.
   Le projet lui-même n'est pas modifié (lecture d'une copie temporaire).


