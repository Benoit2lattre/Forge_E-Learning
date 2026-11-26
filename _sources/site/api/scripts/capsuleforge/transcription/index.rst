scripts.capsuleforge.transcription
==================================

.. py:module:: scripts.capsuleforge.transcription

.. autoapi-nested-parse::

   CapsuleForge — transcription de la narration enregistrée (Whisper, sur cet ordinateur).

   Sert à reprendre un cours déjà enregistré sans scénario écrit : chaque audio de pas est transcrit, le texte
   devient un premier jet de narration À RELIRE, et le minutage mot par mot est gardé dans ``transcriptions/`` pour
   les sous-titres et le calage des apparitions. Rien ne quitte cet ordinateur (le modèle est téléchargé une fois).

   Dépendance facultative : faster-whisper (``uv pip install faster-whisper``).
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.transcription.FREQ


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.transcription.charger_modele
   scripts.capsuleforge.transcription.vocabulaire
   scripts.capsuleforge.transcription.charger_audio
   scripts.capsuleforge.transcription.transcrire_fichier
   scripts.capsuleforge.transcription.transcrire_chapitre
   scripts.capsuleforge.transcription.decouper_phrases
   scripts.capsuleforge.transcription.mots_du_fichier
   scripts.capsuleforge.transcription.phrases_des_segments
   scripts.capsuleforge.transcription.phrases_alignees
   scripts.capsuleforge.transcription.phrases_du_pas


Module Contents
---------------

.. py:function:: charger_modele(nom: str = 'small')

   Charge et renvoie le modèle Whisper ``nom`` (faster-whisper, sur processeur, en int8).


.. py:function:: vocabulaire(chap: dict) -> str

   Renvoie les titres du chapitre (900 caractères au plus), donnés au modèle comme amorce.

   Les termes techniques sont ainsi mieux reconnus.


.. py:data:: FREQ
   :value: 16000


.. py:function:: charger_audio(chemin: pathlib.Path)

   Lit un fichier audio et renvoie un signal mono à 16 kHz (float32, entre -1 et 1).

   Les WAV sont lus sans bibliothèque externe ; les autres formats (mp3, m4a) passent par PyAV.
   On ne dépend pas du décodeur de faster-whisper, dont une version s'est révélée incompatible avec PyAV.


.. py:function:: transcrire_fichier(modele, audio: pathlib.Path, langue: str, amorce: str) -> dict

   Transcrit un fichier audio et renvoie la transcription (segments horodatés, avec leurs mots).

   Le dictionnaire renvoyé contient ``audio``, ``langue``, ``duree_s`` et ``segments`` ; chaque segment a
   ``debut``, ``fin``, ``texte`` et ``mots``.


.. py:function:: transcrire_chapitre(chap: dict, dossier: pathlib.Path, modele, refaire: bool = False, sections: set | None = None, journal=print) -> int

   Transcrit l'audio des pas sans narration (ou de tous avec ``refaire=True``) et renvoie le nombre de pas traités.

   Chaque transcription est écrite dans ``transcriptions/<pas>.json`` ; les phrases du pas sont remplacées
   par les segments reconnus, marqués à relire. Le chapitre (dictionnaire) est modifié sur place, pas écrit.


.. py:function:: decouper_phrases(texte: str) -> list[str]

   Découpe un texte en phrases (règle commune : :func:`format_chapitre.decouper_phrases`).


.. py:function:: mots_du_fichier(transcription: dict) -> list[dict]

   Renvoie tous les mots horodatés d'une transcription, dans l'ordre.


.. py:function:: phrases_des_segments(transcription: dict) -> list[dict]

   Renvoie une phrase horodatée par segment reconnu (texte tel qu'il est dans la transcription).


.. py:function:: phrases_alignees(texte: str, transcription: dict) -> list[dict]

   Découpe un texte corrigé en phrases et donne à chacune son début et sa fin.

   Les mots de chaque phrase sont retrouvés parmi les mots horodatés de la transcription ; une phrase dont
   aucun mot n'est retrouvé est placée entre ses voisines.


.. py:function:: phrases_du_pas(pas: dict, dossier: pathlib.Path) -> list[dict] | None

   Renvoie les phrases d'un pas qui n'en a pas encore (``None`` s'il n'y a rien).

   Par ordre de préférence : sa narration alignée sur sa transcription, sinon les segments de la
   transcription, sinon la narration découpée sans horodatage.


