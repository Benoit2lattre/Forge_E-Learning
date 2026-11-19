scripts.capsuleforge.sons
=========================

.. py:module:: scripts.capsuleforge.sons

.. autoapi-nested-parse::

   CapsuleForge — petites fonctions sur les sons (signal mono en flottants entre -1 et 1).

   Communes à la transcription, à la voix de synthèse et à l'import de vidéo.

   Licence : GPL v3.



Functions
---------

.. autoapisummary::

   scripts.capsuleforge.sons.reechantillonner
   scripts.capsuleforge.sons.ecrire_wav


Module Contents
---------------

.. py:function:: reechantillonner(a: numpy.ndarray, de: int, vers: int) -> numpy.ndarray

   Ramène un signal mono de la fréquence ``de`` à la fréquence ``vers`` (Hz) ; renvoie du float32.

   Pour réduire la fréquence, un filtre passe-bas (sinus cardinal fenêtré) évite le repliement ; puis
   interpolation linéaire.


.. py:function:: ecrire_wav(chemin: pathlib.Path, a: numpy.ndarray, taux: int) -> None

   Écrit un son mono en WAV 16 bits (dossier créé au besoin ; valeurs hors de [-1, 1] écrêtées).


