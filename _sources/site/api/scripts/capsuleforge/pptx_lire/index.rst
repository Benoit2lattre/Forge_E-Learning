scripts.capsuleforge.pptx_lire
==============================

.. py:module:: scripts.capsuleforge.pptx_lire

.. autoapi-nested-parse::

   CapsuleForge — lecture d'un diaporama PowerPoint (.pptx), sans PowerPoint.

   Lit dans l'archive : titre, notes, durée (minutage enregistré), audio de narration et états d'animation de
   chaque diapositive. Un état = ce qui est visible après un clic ; l'état 0 est la diapositive à son ouverture.
   Le fichier n'est jamais modifié. Les images sont produites à part, par PowerPoint lui-même (``pptx_images.py``).
   :func:`reprendre` fait la reprise complète dans un chapitre (commande ``capsuleforge pptx``).

   Formes d'annotation : une forme nommée « cf spot », « cf cadre », « cf pointeur » ou « cf cache » (volet Sélection de
   PowerPoint) n'est jamais sur les images ; elle devient un objet du pas. Un pointeur tracé en ligne brisée
   (forme libre) ou en trait donne une trajectoire.

   Limite connue : PowerPoint n'enregistre pas l'instant des clics pendant une narration, seulement la durée de
   la diapositive ; les apparitions sont donc réparties sur cette durée, à régler ensuite.
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.pptx_lire.NS
   scripts.capsuleforge.pptx_lire.P
   scripts.capsuleforge.pptx_lire.EMU_PAR_POUCE
   scripts.capsuleforge.pptx_lire.PREFIXE
   scripts.capsuleforge.pptx_lire.TYPES_CF
   scripts.capsuleforge.pptx_lire.SOURCE_PPTX
   scripts.capsuleforge.pptx_lire.PAS_PPTX


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.pptx_lire.lire
   scripts.capsuleforge.pptx_lire.extraire_audio
   scripts.capsuleforge.pptx_lire.plage
   scripts.capsuleforge.pptx_lire.reprendre


Module Contents
---------------

.. py:data:: NS

.. py:data:: P
   :value: '{http://schemas.openxmlformats.org/presentationml/2006/main}'


.. py:data:: EMU_PAR_POUCE
   :value: 914400


.. py:data:: PREFIXE
   :value: 'cf'


.. py:data:: TYPES_CF

.. py:function:: lire(fichier: pathlib.Path) -> dict

   Lit un diaporama et renvoie sa structure : taille et, par diapositive, titre, notes, durée, audio, états.

   Chaque diapositive porte aussi les identifiants des formes à cacher à l'export (``medias``) et, s'il y en a,
   ses formes d'annotation (``formes``) et les remarques de lecture (``remarques``).


.. py:function:: extraire_audio(fichier: pathlib.Path, diapos: list[dict], dossier: pathlib.Path) -> dict

   Copie l'audio de narration des diapositives données dans ``<dossier>/audio/dNN.<ext>``.

   Renvoie ``{numéro de diapositive: chemin relatif}``.


.. py:function:: plage(texte: str | None, maxi: int) -> list[int]

   Convertit une plage (« 6-12 », « 6,8,10-12 ») en liste de numéros de diapositives compris entre 1 et ``maxi``.

   Un texte vide donne toutes les diapositives.


.. py:data:: SOURCE_PPTX
   :value: ('type', 'fichier', 'diapo', 'etats', 'titre', 'animation_par_paragraphe')


.. py:data:: PAS_PPTX
   :value: ('id', 'fond', 'source', 'narration', 'phrases', 'audio', 'duree_s', 'objets')


.. py:function:: reprendre(src: pathlib.Path, y: pathlib.Path, diapos: str | None = None, largeur: int | None = None, images: bool = True) -> dict

   Reprend le diaporama ``src`` dans les sections du chapitre ``y`` qui y renvoient ; renvoie le chapitre écrit.

   Les sections visées sont celles dont ``source.fichier`` est le nom du diaporama et dont ``source.diapos``
   contient une des diapositives demandées (``diapos`` : « 6-12 », « 3,5 »… ; toutes si ``None``). Chaque
   diapositive devient un pas (image, audio, durée), chaque clic d'animation une apparition, et les formes
   d'annotation des objets ; le texte déjà relu et les réglages de temps existants sont conservés.

   Écrit les images avec PowerPoint (``pptx_images``, sauf si ``images`` est faux), ``pptx_journal.txt``, une copie
   de l'ancien chapitre dans ``sauvegardes/`` et le nouveau ``chapitre.yaml``. ``largeur`` : largeur des images
   (par défaut celle de l'écran du chapitre, sinon 1440).


