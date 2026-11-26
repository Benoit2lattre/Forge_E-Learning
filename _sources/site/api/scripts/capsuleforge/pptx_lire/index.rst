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

   Habillage (lot 6) : une forme « cf édition » n'est montrée que dans une capsule habillée pour une édition,
   « cf édition ecole1 » seulement pour ce public (école ou variante), « cf nu » seulement dans la capsule nue ;
   un texte ``{cours}``, ``{code}``, ``{promo}``… est un champ, rempli à l'export d'une édition (vide dans la
   capsule nue). La lecture les repère (``edition``, ``champs``, ``pieds``) ; l'export est fait par ``pptx_images``.

   Limite connue : PowerPoint n'enregistre pas l'instant des clics pendant une narration, seulement la durée de
   la diapositive ; les apparitions sont donc réparties sur cette durée, à régler ensuite.
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.pptx_lire.NS
   scripts.capsuleforge.pptx_lire.P
   scripts.capsuleforge.pptx_lire.EMU_PAR_POUCE
   scripts.capsuleforge.pptx_lire.MC
   scripts.capsuleforge.pptx_lire.A14_M
   scripts.capsuleforge.pptx_lire.PREFIXE
   scripts.capsuleforge.pptx_lire.TYPES_CF
   scripts.capsuleforge.pptx_lire.CHAMPS
   scripts.capsuleforge.pptx_lire.CHAMP
   scripts.capsuleforge.pptx_lire.EDITION
   scripts.capsuleforge.pptx_lire.SEPARATEURS
   scripts.capsuleforge.pptx_lire.P14
   scripts.capsuleforge.pptx_lire.SOURCE_PPTX
   scripts.capsuleforge.pptx_lire.PAS_PPTX


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.pptx_lire.remplir_texte
   scripts.capsuleforge.pptx_lire.vide
   scripts.capsuleforge.pptx_lire.texte_diapo
   scripts.capsuleforge.pptx_lire.lire
   scripts.capsuleforge.pptx_lire.extraire_audio
   scripts.capsuleforge.pptx_lire.plage
   scripts.capsuleforge.pptx_lire.garder_traductions
   scripts.capsuleforge.pptx_lire.dispositions
   scripts.capsuleforge.pptx_lire.masque_chapitre
   scripts.capsuleforge.pptx_lire.reprendre


Module Contents
---------------

.. py:data:: NS

.. py:data:: P
   :value: '{http://schemas.openxmlformats.org/presentationml/2006/main}'


.. py:data:: EMU_PAR_POUCE
   :value: 914400


.. py:data:: MC
   :value: '{http://schemas.openxmlformats.org/markup-compatibility/2006}'


.. py:data:: A14_M
   :value: '{http://schemas.microsoft.com/office/drawing/2010/main}m'


.. py:data:: PREFIXE
   :value: 'cf'


.. py:data:: TYPES_CF

.. py:data:: CHAMPS
   :value: ('cours', 'code', 'bloc', 'promo', 'annee', 'ecole', 'declinaison', 'edition', 'enseignant', 'capsule')


.. py:data:: CHAMP

.. py:data:: EDITION

.. py:data:: SEPARATEURS
   :value: ' \t·•|,;:/—–-'


.. py:function:: remplir_texte(texte: str, valeurs: dict) -> str

   Remplit les champs ``{cours}``… d'un texte ; un champ vide part avec un séparateur voisin, comme à l'export
   PowerPoint (« Benoit Delattre - {code} » → « Benoit Delattre » dans la capsule nue).


.. py:function:: vide(texte: str) -> bool

   Vrai si un texte n'a plus que des espaces et des séparateurs.


.. py:function:: texte_diapo(z: zipfile.ZipFile, chemin: str, racine, etats: list) -> list[dict]

   Texte d'une diapositive, dans l'ordre de lecture (titre d'abord, puis de haut en bas et de gauche à droite).

   Blocs : ``{texte, titre: true}``, ``{texte, niveau}`` (un paragraphe, niveau de puce à partir de 0),
   ``{formule}`` (LaTeX d'une équation IguanaTeX), ``{cellules: [[{texte}…]…]}`` (tableau). Chaque bloc porte, s'il
   y a lieu, ``etat`` (premier état où il est visible) et, pour une forme d'édition, ``cas`` et ``publics``. Les
   annotations « cf … », les médias, les images et les pieds de page n'y sont pas ; les champs ``{cours}``… restent
   écrits tels quels (remplis à la construction).


.. py:data:: P14
   :value: '{http://schemas.microsoft.com/office/powerpoint/2010/main}'


.. py:function:: lire(fichier: pathlib.Path) -> dict

   Lit un diaporama et renvoie sa structure : taille et, par diapositive, titre, notes, durée, audio, états.

   Chaque diapositive porte aussi les identifiants des formes à cacher à l'export (``medias``) et, s'il y en a,
   ses formes d'annotation (``formes``), ses formes d'édition (``edition``), ses champs (``champs`` :
   ``{spid: [noms]}``), ses pieds de page (``pieds``) et les remarques de lecture (``remarques``). Le diaporama porte
   ``champs_masque`` : les champs écrits dans les masques et les dispositions.


.. py:function:: extraire_audio(fichier: pathlib.Path, diapos: list[dict], dossier: pathlib.Path) -> dict

   Copie l'audio de narration des diapositives données dans ``<dossier>/audio/dNN.<ext>``.

   Renvoie ``{numéro de diapositive: chemin relatif}``.


.. py:function:: plage(texte: str | None, maxi: int) -> list[int]

   Convertit une plage (« 6-12 », « 6,8,10-12 ») en liste de numéros de diapositives compris entre 1 et ``maxi``.

   Un texte vide donne toutes les diapositives.


.. py:data:: SOURCE_PPTX
   :value: ('type', 'fichier', 'diapo', 'etats', 'titre', 'animation_par_paragraphe', 'phrases_notes',...


.. py:data:: PAS_PPTX
   :value: ('id', 'fond', 'source', 'narration', 'phrases', 'audio', 'duree_s', 'objets', 'texte_diapo')


.. py:function:: garder_traductions(neuf: list[dict], vieux: list[dict] | None, src: str) -> list[dict]

   Reporte sur le texte de diapositive relu ``neuf`` les traductions de ``vieux`` dont le texte source n'a pas
   changé (textes ``{fr: …, en: …}`` du chapitre).


.. py:function:: dispositions(fichier: pathlib.Path) -> dict

   Lit sans PowerPoint ce qui compte pour appliquer un modèle : taille des diapositives (EMU), noms des
   dispositions du fichier et de chaque diapositive, champs des masques. Marche pour un .pptx ou un .potx.


.. py:function:: masque_chapitre(chap: dict) -> str

   Masque des diapositives PowerPoint du chapitre (clé ``powerpoint: {masque: …}``) : ``nu`` (défaut, formes du
   masque et pieds de page cachés) ou ``garder`` (masque neutre, montré partout).


.. py:function:: reprendre(src: pathlib.Path, y: pathlib.Path, diapos: str | None = None, largeur: int | None = None, images: bool = True, profil: dict | None = None, video: str | None = None) -> dict

   Reprend le diaporama ``src`` dans les sections du chapitre ``y`` qui y renvoient ; renvoie le chapitre écrit.

   Les sections visées sont celles dont ``source.fichier`` est le nom du diaporama et dont ``source.diapos``
   contient une des diapositives demandées (``diapos`` : « 6-12 », « 3,5 »… ; toutes si ``None``). Chaque
   diapositive devient un pas (image, audio, durée), chaque clic d'animation une apparition, et les formes
   d'annotation des objets ; le texte déjà relu et les réglages de temps existants sont conservés. Les images sont
   celles de la capsule nue : formes « cf édition » cachées, champs vides, masque caché sauf ``powerpoint: {masque:
   garder}`` dans le chapitre (``pptx_edition`` refait celles d'une édition).

   Notes et balises (guide « Préparer son diaporama ») : sans enregistrement, les notes deviennent les phrases du
   texte dit, sans leurs balises ; chaque clic est accroché à sa balise ``[clic]`` ou, sans balise, à la phrase de
   même rang ; ``[pause]`` donne la pause après une phrase. Avec un enregistrement, les balises sont seulement
   retirées (les clics restent répartis sur la durée, à caler après la transcription). Le diagnostic du diaporama
   est écrit au journal.

   Vidéo insérée : extraite, recadrée et mise à la taille ``video`` (``standard``, ``fine``, ``source`` ; réglage
   ``powerpoint: {video: …}`` du chapitre, ``fine`` par défaut) par ``pptx_video`` ; elle devient un objet ``video``
   du pas (place, état où elle apparaît, départ, durée, première et dernière images, options de lecture). Le clic
   qui la lance est une action comme les autres (balise ``[clic]``, accroche).

   Écrit les images avec PowerPoint (``pptx_images``, sauf si ``images`` est faux), ``pptx_journal.txt``, une copie
   de l'ancien chapitre dans ``sauvegardes/`` et le nouveau ``chapitre.yaml``. ``largeur`` : largeur des images
   (par défaut celle de l'écran du chapitre, sinon 1440).


