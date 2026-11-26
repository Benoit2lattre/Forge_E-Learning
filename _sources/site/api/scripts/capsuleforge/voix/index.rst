scripts.capsuleforge.voix
=========================

.. py:module:: scripts.capsuleforge.voix

.. autoapi-nested-parse::

   CapsuleForge — voix de synthèse d'un chapitre (format 2).

   Utilisation : ::

       capsuleforge voix <chapitre> --langue en [--moteur piper|edge] [--voix NOM] [--vitesse 1.0] [--sections a,b] [--refaire]

   La voix est fabriquée phrase par phrase, à partir des phrases du pas (texte dans la langue demandée), puis mise
   bout à bout avec des silences proches de ceux de l'original. On connaît donc exactement l'instant de chaque phrase
   dans le nouveau son : sous-titres, apparitions et objets (spots, pointeurs…) sont recalés phrase à phrase.

   Deux usages :

   - une autre langue que la langue source : le son est rangé dans ``pas.voix.<langue>`` (audio, duree_s, phrases =
     instants [début, fin] de chaque phrase) ; le son d'origine n'est pas touché ;
   - la langue source, pour un pas sans enregistrement (diapositive neuve) ou déjà synthétisé : le son devient le son
     du pas (``audio``, ``duree_s``, instants des phrases), marqué ``source.voix: synthese`` ; une narration sans phrases est
     d'abord découpée en phrases. Un pas qui a un enregistrement n'est jamais remplacé.

   Un pas déjà synthétisé n'est refait que si son texte a changé (ou avec --refaire).

   Moteurs (gratuits) : « piper » (voix neuronale sur cet ordinateur, ``pip install piper-tts`` ; modèle téléchargé à la première
   utilisation dans ``data/capsuleforge/_voix/``), « edge » (voix neuronales de Microsoft Edge, en ligne, sans clé :
   ``pip install edge-tts`` ; le texte part chez Microsoft). Moteur ``essai`` : voix factice pour les tests (durée selon le nombre de mots). Autres moteurs (payants) : à brancher dans ``MOTEURS``.
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.voix.VOIX_DEFAUT
   scripts.capsuleforge.voix.TAUX
   scripts.capsuleforge.voix.MOTEURS


Classes
-------

.. autoapisummary::

   scripts.capsuleforge.voix.Piper
   scripts.capsuleforge.voix.Edge
   scripts.capsuleforge.voix.Essai


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.voix.silences_pas
   scripts.capsuleforge.voix.synthetiser
   scripts.capsuleforge.voix.voix_chapitre
   scripts.capsuleforge.voix.recaler


Module Contents
---------------

.. py:data:: VOIX_DEFAUT

.. py:data:: TAUX
   :value: 22050


.. py:class:: Piper(nom: str, dossier: pathlib.Path, vitesse: float = 1.0)

   Moteur Piper (voix neuronale locale) ; le modèle ``<nom>.onnx`` est téléchargé dans ``dossier`` s'il manque.


   .. py:attribute:: voix


   .. py:attribute:: config


   .. py:method:: dire(texte: str)

      Synthétise ``texte`` et renvoie ``(échantillons float32, taux d'échantillonnage)``.



.. py:class:: Edge(nom: str, dossier: pathlib.Path, vitesse: float = 1.0)

   Moteur Edge (voix neuronales en ligne de Microsoft, via ``edge-tts``).


   .. py:method:: dire(texte: str)

      Synthétise ``texte`` (MP3 temporaire décodé) et renvoie ``(échantillons float32, taux)``.



.. py:class:: Essai(nom: str, dossier: pathlib.Path, vitesse: float = 1.0)

   Moteur factice (essais sans voix installée) : un son dont la durée suit le nombre de mots.


   .. py:attribute:: vitesse
      :value: 1.0



   .. py:method:: dire(texte: str)

      Renvoie un son sinusoïdal de 220 Hz, d'environ 160 mots par minute (au moins 0,6 s).



.. py:data:: MOTEURS

.. py:function:: silences_pas(pas: dict, chap: dict, n: int, langue: str, src: str) -> tuple[float, list[float], float]

   Silences de la voix d'un pas : la pause de chaque phrase (``pause_s``, sinon celle du chapitre).

   Langue source : avant la première phrase et entre les phrases, les réglages de calage ; après la dernière, sa
   pause si elle est plus longue que la fin habituelle. Autre langue : les silences de la voix d'origine, sauf
   là où une pause est donnée (elle est rendue telle quelle).


.. py:function:: synthetiser(textes: list[str], moteur, silences) -> tuple[numpy.ndarray, int, list[list[float]]]

   Synthétise les phrases une à une et les met bout à bout, séparées par les silences donnés.

   ``silences`` : ``(avant, [entre…], après)`` en secondes. Renvoie le son, son taux d'échantillonnage et,
   pour chaque phrase, ses instants ``[début, fin]`` en secondes.


.. py:function:: voix_chapitre(yaml_chap: pathlib.Path, langue: str, moteur: str = 'piper', nom: str | None = None, vitesse: float = 1.0, sections: set | None = None, refaire: bool = False, journal=print) -> int

   Synthétise la voix des pas d'un chapitre dans une langue et renvoie le nombre de pas synthétisés.

   ``nom`` : voix du moteur (défaut : ``VOIX_DEFAUT``) ; ``sections`` : identifiants de parties ou de sections
   à traiter (toutes par défaut). Les sons sont écrits dans ``audio/voix/<pas>.<langue>.wav`` ; si au moins un pas
   a été fait, le chapitre est sauvegardé dans ``sauvegardes/`` puis réécrit.


.. py:function:: recaler(t: float, src: list[list[float]], cible: list[list[float]], d_src: float, d_cible: float) -> float

   Convertit un instant du son d'origine en instant du son traduit (linéaire par morceaux entre les bornes des phrases).


