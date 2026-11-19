scripts.capsuleforge.essai_capture
==================================

.. py:module:: scripts.capsuleforge.essai_capture

.. autoapi-nested-parse::

   CapsuleForge — diagnostic de capture sous Windows (écran, webcam, micro) avec PyAV, à lancer si ``capsuleforge filmer`` ne trouve pas un appareil.

   Utilisation : ::

       uv run scripts/capsuleforge/essai_capture.py            # liste les appareils, filme 5 s d'écran
       uv run scripts/capsuleforge/essai_capture.py --tout     # + 5 s de webcam et de micro (premiers appareils trouvés)
       uv run scripts/capsuleforge/essai_capture.py --tout --ecran 2   # écran n° 2 (défaut : l'écran principal)

   Écrit dans data/capsuleforge/_essai_capture/ : ecran.mp4, webcam.mp4, micro.wav et rapport.txt (à joindre à un signalement).
   Rien d'autre n'est modifié.
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.essai_capture.ICI
   scripts.capsuleforge.essai_capture.SORTIE
   scripts.capsuleforge.essai_capture.LIGNES


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.essai_capture.dire
   scripts.capsuleforge.essai_capture.appareils
   scripts.capsuleforge.essai_capture.appareils_windows
   scripts.capsuleforge.essai_capture.ecran
   scripts.capsuleforge.essai_capture.filmer
   scripts.capsuleforge.essai_capture.micro
   scripts.capsuleforge.essai_capture.main


Module Contents
---------------

.. py:data:: ICI

.. py:data:: SORTIE

.. py:data:: LIGNES
   :type:  list[str]
   :value: []


.. py:function:: dire(t: str = '') -> None

   Affiche une ligne et la garde pour le rapport écrit à la fin (``rapport.txt``).


.. py:function:: appareils(av) -> tuple[list[str], list[str]]

   Renvoie les noms des appareils DirectShow (vidéo, audio).

   ffmpeg les écrit dans son journal avec l'option ``list_devices`` ; deux formes de journal sont lues
   (récente : une ligne par appareil suivie de ``(video)`` ou ``(audio)`` ; ancienne : deux sections).


.. py:function:: appareils_windows() -> tuple[list[str], list[str]]

   Renvoie, en secours, les noms des caméras et micros vus par Windows (via PowerShell).

   Ces noms sont souvent les mêmes que ceux de DirectShow ; la caméra infrarouge est placée en dernier.


.. py:function:: ecran(n: int | None) -> dict

   Renvoie les options gdigrab pour filmer un seul écran.

   La géométrie vient de ``mss`` ; ``n`` = 1 (ou ``None``) pour l'écran principal. Renvoie un dictionnaire
   vide (tout le bureau) si la géométrie est inconnue.


.. py:function:: filmer(av, entree: str, fmt: str, options: dict, dst: pathlib.Path, duree: float, ips: int = 15) -> None

   Filme ``duree`` secondes depuis une entrée ffmpeg (écran ou webcam) et les écrit en H.264 dans ``dst``.

   ``ips`` : images par seconde de la vidéo écrite. Le bilan (taille, cadence obtenue) va dans le rapport.


.. py:function:: micro(av, nom: str, dst: pathlib.Path, duree: float) -> None

   Enregistre ``duree`` secondes du micro DirectShow ``nom`` dans le WAV ``dst`` (mono, 48 kHz, 16 bits).

   Le niveau moyen (dBFS) est noté dans le rapport.


.. py:function:: main() -> int

   Lance l'essai (options ``--tout`` et ``--ecran N`` lues dans ``sys.argv``) et renvoie le code de sortie.


