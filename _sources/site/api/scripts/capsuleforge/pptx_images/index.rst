scripts.capsuleforge.pptx_images
================================

.. py:module:: scripts.capsuleforge.pptx_images

.. autoapi-nested-parse::

   CapsuleForge — images d'un diaporama, une par état d'animation, produites par PowerPoint (Windows).

   PowerPoint est piloté par COM : le fichier est ouvert en lecture seule, sans fenêtre ; pour chaque état, les
   formes et paragraphes qui ne sont pas encore apparus sont cachés en mémoire, puis la diapositive est exportée
   en PNG. Rien n'est enregistré dans le diaporama. Si PowerPoint était déjà ouvert, il le reste.

   Dépendance : ``comtypes`` (déjà installé avec ``uiautomation``).
   Licence : GPL v3.



Functions
---------

.. autoapisummary::

   scripts.capsuleforge.pptx_images.exporter


Module Contents
---------------

.. py:function:: exporter(fichier: pathlib.Path, diapos: list[dict], dossier: pathlib.Path, largeur: int, journal=print) -> list[str]

   Écrit ``<dossier>/images/dNN_eK.png`` pour chaque état des diapositives données et renvoie les chemins relatifs écrits.

   ``diapos`` : diapositives issues de ``pptx_lire.lire`` ; ``largeur`` : largeur des images en pixels.
   Ne fonctionne que sous Windows, avec PowerPoint installé.


