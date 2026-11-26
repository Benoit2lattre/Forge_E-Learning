scripts.capsuleforge.filmer
===========================

.. py:module:: scripts.capsuleforge.filmer

.. autoapi-nested-parse::

   CapsuleForge — enregistreur intégré : écran, micro et webcam en même temps (Windows), puis import dans un chapitre.

   Commande : ::

       capsuleforge filmer <chapitre> --section partie/section [--titre "…"] [--ecran 1] [--webcam [NOM]] [--micro NOM | --sans-micro]
                           [--ips 20] [--duree s] [--sans-import] [--appareils]

   Raccourcis (comme l'enregistreur de didacticiel) : Ctrl+Maj+P pause / reprise (2 bips), Ctrl+Maj+F fin (3 bips) ;
   dans la fenêtre de commande, Entrée termine aussi ; une ligne « pause » met en pause ou reprend (boutons de l'Atelier Forge). Un compte à rebours de 3 s précède l'enregistrement.

   Chaque source a son fil ; chaque image et chaque morceau de son reçoit l'instant de l'horloge commune (pauses
   retirées) : l'écran, la webcam et la voix restent calés, même si une source démarre en retard (le micro met environ
   une seconde à s'ouvrir : le début du son est complété par du silence). Fichiers bruts dans
   ``<chapitre>/enregistrements/<date>/`` (``ecran_<date>.mp4``, ``micro_<date>.wav``, ``camera_<date>.mp4``, ``journal.txt``), puis import
   comme ``capsuleforge video … --son micro.wav`` : pas vidéo découpés aux silences ; la webcam devient le caméo de ces
   pas. Appareils : DirectShow (noms lus dans le journal de ffmpeg) ; écrans : mss. ``--appareils`` les liste.
   Essai sans appareils (toutes plateformes) : ``--essai`` (mire et son synthétiques).
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.filmer.TAUX


Classes
-------

.. autoapisummary::

   scripts.capsuleforge.filmer.Horloge
   scripts.capsuleforge.filmer.Video
   scripts.capsuleforge.filmer.Micro


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.filmer.appareils
   scripts.capsuleforge.filmer.ecrans
   scripts.capsuleforge.filmer.tester_micro
   scripts.capsuleforge.filmer.enregistrer
   scripts.capsuleforge.filmer.filmer


Module Contents
---------------

.. py:data:: TAUX
   :value: 48000


.. py:function:: appareils() -> tuple[list[str], list[str]]

   Renvoie les listes (caméras, micros) des appareils DirectShow.

   ffmpeg écrit la liste dans son journal, par morceaux : on les recolle. La caméra virtuelle d'OBS est
   écartée et les caméras infrarouges sont placées en dernier.


.. py:function:: ecrans() -> list[dict]

   Renvoie les écrans vus par ``mss`` (``left``, ``top``, ``width``, ``height``), ou une liste vide.


.. py:function:: tester_micro(micro=None, duree: float = 4.0, essai: bool = False, journal=print) -> dict

   Écoute le micro ``duree`` secondes et dit si le niveau de la voix convient (``filmer --tester-micro``).

   Renvoie ``{micro, voix, crete, avis, conseil}`` (niveaux en dBFS) et l'écrit en une ligne « Micro … ».


.. py:class:: Horloge

   Temps utile de l'enregistrement : depuis le départ, pauses retirées.


   .. py:attribute:: t0
      :value: None



   .. py:attribute:: pause_debut
      :value: None



   .. py:attribute:: pauses
      :value: 0.0



   .. py:attribute:: fin


   .. py:method:: demarrer()

      Fixe l'instant de départ de l'horloge.



   .. py:method:: en_pause() -> bool

      Indique si l'enregistrement est en pause.



   .. py:method:: basculer() -> bool

      Met en pause ou reprend ; renvoie ``True`` si l'enregistrement vient d'entrer en pause.



   .. py:method:: maintenant(t: float | None = None) -> float

      Renvoie le temps utile (s) à l'instant ``t`` de ``time.monotonic()``, ou maintenant par défaut.



.. py:class:: Video(nom: str, entree: str, fmt: str, options: dict, dst: pathlib.Path, horloge: Horloge, ips: int = 20, largeur_max: int | None = None, crf: int = 23)



   Une source d'images (écran ou webcam) -> MP4 H.264, chaque image à son instant (cadence variable).


   .. py:attribute:: file
      :type:  queue.Queue


   .. py:attribute:: erreur
      :value: None



   .. py:attribute:: pret


   .. py:method:: run()

      Lit la source et met en file les images horodatées (hors pause) ; un second fil les encode.



.. py:class:: Micro(entree: str, fmt: str, options: dict, dst: pathlib.Path, horloge: Horloge)



   Le micro -> WAV mono 48 kHz ; le début est complété par du silence pour être calé sur l'horloge commune.


   .. py:attribute:: ecrits
      :value: 0



   .. py:attribute:: combles
      :value: 0



   .. py:attribute:: retard
      :value: None



   .. py:attribute:: erreur
      :value: None



   .. py:attribute:: pret


   .. py:attribute:: niveaux
      :type:  list[float]
      :value: []



   .. py:method:: run()

      Écrit le son du micro dans le WAV, calé sur l'horloge commune.

      Le retard d'ouverture et les trous de plus de 0,15 s sont comblés par du silence ; le niveau de chaque
      morceau est noté dans ``niveaux``.



.. py:function:: enregistrer(dossier: pathlib.Path, ecran: int | None = 1, webcam: str | bool | None = None, micro: str | bool | None = True, ips: int = 20, duree: float | None = None, essai: bool = False, journal=print) -> dict

   Filme l'écran, le micro et la webcam demandés dans ``dossier`` jusqu'à la fin demandée.

   La fin vient du raccourci Ctrl+Maj+F, de la touche Entrée ou de ``duree`` (secondes utiles). Écrit les
   fichiers des sources et ``journal.txt`` ; renvoie le dictionnaire des chemins écrits (clés ``ecran``,
   ``micro``, ``camera`` selon les sources). ``essai=True`` remplace les appareils par des sources synthétiques.


.. py:function:: filmer(yaml_chap: pathlib.Path, section: str, titre: str | None = None, ecran: int | None = 1, webcam=None, micro=True, ips: int = 20, duree: float | None = None, importer: bool = True, essai: bool = False, journal=print) -> pathlib.Path

   Filme dans ``enregistrements/<date_heure>/`` du chapitre puis importe la vidéo dans la section.

   ``section`` est de la forme ``partie/section`` ; ``titre`` sert si la section est à créer. La section est
   vérifiée avant de filmer. Avec ``importer=False``, la section peut manquer : les fichiers sont gardés et la
   commande d'import est affichée. Renvoie le dossier de
   l'enregistrement.


