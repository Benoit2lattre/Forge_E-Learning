scripts.capsuleforge.construire
===============================

.. py:module:: scripts.capsuleforge.construire

.. autoapi-nested-parse::

   CapsuleForge — construction du lecteur HTML à partir de capsule.yaml.

   Sortie : <sortie>/index.html (lecteur autonome, données incluses : s'ouvre aussi depuis le disque)
   et <sortie>/images/ (copiées, masques floutés, éventuellement réduites ou converties en WebP).
   Les coordonnées restent celles de l'écran enregistré : le lecteur les ramène en pourcentages.
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.construire.ICI
   scripts.capsuleforge.construire.MATHJAX


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.construire.masquer
   scripts.capsuleforge.construire.construire


Module Contents
---------------

.. py:data:: ICI

.. py:data:: MATHJAX

.. py:function:: masquer(img, masques, echelle)

   Pixellise puis floute, dans l'image, les zones ``[x, y, l, h]`` des masques.


.. py:function:: construire(capsule_yaml: pathlib.Path, sortie: pathlib.Path, largeur: int | None = None, fmt: str = 'png', apercu: bool = False) -> pathlib.Path

   Construit le lecteur HTML d'une capsule et renvoie le chemin de ``<sortie>/index.html``.

   ``largeur`` : largeur maximale des images (réduction seulement) ; ``fmt`` : ``png`` ou ``webp``.
   ``apercu=True`` (éditeur) : images non optimisées et non refaites si elles sont à jour.
   Arrête le programme (``SystemExit``) si la capsule ne passe pas la vérification.


