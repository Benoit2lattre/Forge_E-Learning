scripts.capsuleforge.pptx_video
===============================

.. py:module:: scripts.capsuleforge.pptx_video

.. autoapi-nested-parse::

   CapsuleForge — vidéo insérée dans une diapositive : extraction, recadrage, première et dernière images.

   La vidéo est lue dans l'archive du diaporama, recadrée comme dans PowerPoint, mise à la taille voulue et
   réencodée sans son (H.264). Ses première et dernière images sont écrites à part : la première est montrée avant
   le départ, la dernière après la lecture et dans le PDF.

   Taille (``qualite``, réglage ``powerpoint: {video: …}`` du chapitre ou ``capsuleforge pptx --video``) :

   - ``standard`` : la taille de la zone de la vidéo dans le lecteur ;
   - ``fine`` (défaut) : 1,5 fois cette taille (écrans haute densité, zoom) ;
   - ``source`` : toute la définition de la vidéo recadrée.

   Jamais plus grande que la source. Une vidéo déjà faite avec les mêmes réglages n'est pas refaite.

   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.pptx_video.QUALITES
   scripts.capsuleforge.pptx_video.CRF


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.pptx_video.qualite_chapitre
   scripts.capsuleforge.pptx_video.extraire


Module Contents
---------------

.. py:data:: QUALITES

.. py:data:: CRF
   :value: 23


.. py:function:: qualite_chapitre(chap: dict, demandee: str | None = None) -> str

.. py:function:: extraire(pptx: pathlib.Path, membre: str, recadrage: dict, largeur_zone: int, qualite: str, dst: pathlib.Path, premiere: pathlib.Path, derniere: pathlib.Path) -> dict

   Extrait la vidéo ``membre`` du diaporama dans ``dst`` ; renvoie ``{duree_s, largeur, hauteur, refaite}``.


