scripts.capsuleforge.nouvelle
=============================

.. py:module:: scripts.capsuleforge.nouvelle

.. autoapi-nested-parse::

   CapsuleForge — créer une capsule neuve (commande ``capsuleforge nouvelle``).

   Écrit ``data/capsuleforge/<nom>/chapitre.yaml`` : titre, langue, écran, réglages et les trois parcours habituels
   (vue d'ensemble, lecture détaillée, lecture immersive), puis le plan :

   - **à partir d'un diaporama** (``diaporama``) : une partie par section PowerPoint s'il y en a au moins deux, sinon une
     seule partie ; dans chaque partie, des sections de quelques minutes faites de diapositives qui se suivent
     (``decoupe`` : ``auto`` = au plus ``minutes`` min d'après le minutage enregistré, ``diapositive`` = une section
     par diapositive, ``une`` = une seule section par partie). Chaque section renvoie à ses diapositives
     (``source: {fichier, diapos}``) : la reprise du diaporama (``capsuleforge pptx``) remplit ensuite les pas ;
   - **sans diaporama** : une partie vide, que l'import d'une vidéo ou un enregistrement d'écran remplira.

   Le titre d'une section est celui de sa première diapositive (à corriger ensuite si besoin). Une diapositive
   masquée dans PowerPoint est laissée de côté. Rien n'est écrasé : le dossier ne doit pas déjà contenir de capsule.

   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.nouvelle.P14
   scripts.capsuleforge.nouvelle.DUREE_INCONNUE_S
   scripts.capsuleforge.nouvelle.PARCOURS
   scripts.capsuleforge.nouvelle.REGLAGES


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.nouvelle.nom_valide
   scripts.capsuleforge.nouvelle.sections_powerpoint
   scripts.capsuleforge.nouvelle.diapos_masquees
   scripts.capsuleforge.nouvelle.decouper
   scripts.capsuleforge.nouvelle.plan_diaporama
   scripts.capsuleforge.nouvelle.creer


Module Contents
---------------

.. py:data:: P14
   :value: 'http://schemas.microsoft.com/office/powerpoint/2010/main'


.. py:data:: DUREE_INCONNUE_S
   :value: 60.0


.. py:data:: PARCOURS

.. py:data:: REGLAGES

.. py:function:: nom_valide(nom: str) -> str

.. py:function:: sections_powerpoint(fichier: pathlib.Path) -> list[tuple[str, list[int]]]

   Sections PowerPoint d'un diaporama : [(nom, [numéros des diapositives])] ; [] s'il n'y en a pas.


.. py:function:: diapos_masquees(fichier: pathlib.Path) -> set[int]

   Numéros des diapositives masquées dans PowerPoint (``show="0"``).


.. py:function:: decouper(diapos: list[dict], decoupe: str, minutes: float) -> list[list[dict]]

   Groupes de diapositives consécutives formant les sections d'une partie.


.. py:function:: plan_diaporama(fichier: pathlib.Path, decoupe: str = 'auto', minutes: float = 6.0, diapos: str | None = None) -> tuple[list, dict]

   Parties et sections proposées pour un diaporama ; renvoie (parties, infos).


.. py:function:: creer(dossier: pathlib.Path, titre: str, langue: str = 'fr', diaporama: pathlib.Path | None = None, decoupe: str = 'auto', minutes: float = 6.0, diapos: str | None = None) -> dict

   Crée la capsule dans ``dossier`` (qui ne doit pas contenir de capsule) ; renvoie le chapitre écrit.


