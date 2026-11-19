scripts.capsuleforge.video
==========================

.. py:module:: scripts.capsuleforge.video

.. autoapi-nested-parse::

   CapsuleForge — import d'une vidéo dans un chapitre (format 2) : pas de type vidéo.

   Utilisation : ::

       capsuleforge video <fichier> --chapitre <ch> --section <partie/section> [--son audio.mp4] [--titre T] [--debut s] [--fin s]
                          [--decoupe silences|aucune] [--pas-min 20] [--pas-max 90] [--qualite 28] [--remplacer]

   Sources : enregistrement d'écran, vidéo exportée d'ActivePresenter, clip quelconque (MP4, MKV, MOV, WEBM…).
   ActivePresenter range le son à part (``audio_NNN.mp4`` à côté de ``Video_NNN.mp4``) : le donner avec ``--son``.

   1. La vidéo est comprimée une fois dans ``<chapitre>/videos/<nom>.mp4`` (H.264 « veryfast », qualité CRF 28 par
      défaut, largeur au plus celle de l'écran du chapitre, 30 images/s au plus, son AAC mono 64 kb/s).
   2. Elle est découpée en pas aux silences de la voix (pas de 20 à 90 s par défaut ; « aucune » = un seul pas).
   3. Chaque pas reçoit : ``video: {fichier, debut_s, fin_s}`` (son extrait de la vidéo), ``duree_s``, une image
      d'affiche ``fond`` (``images/<id>.png``, première image du pas) et son propre son ``audio`` (``audio/<id>.wav``) : la
      relecture, la transcription (``capsuleforge transcrire``), la traduction et les voix fonctionnent comme pour
      une diapositive. Identifiants : v01, v02… (uniques dans le chapitre).

   La section peut être créée : ``--section partie/nouvel_id --titre "Titre"``. ``--remplacer`` retire d'abord de la
   section les pas déjà importés de ce même fichier (``source.fichier``).
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.video.TAUX_SON


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.video.comprimer
   scripts.capsuleforge.video.niveau_voix
   scripts.capsuleforge.video.relever_voix
   scripts.capsuleforge.video.silences
   scripts.capsuleforge.video.coupes
   scripts.capsuleforge.video.affiche
   scripts.capsuleforge.video.trouver_section
   scripts.capsuleforge.video.importer


Module Contents
---------------

.. py:data:: TAUX_SON
   :value: 22050


.. py:function:: comprimer(src: pathlib.Path, dst: pathlib.Path, largeur_max: int = 1440, qualite: int = 28, debut: float = 0.0, fin: float | None = None, ips_max: int = 30, son_src: pathlib.Path | None = None, muet: bool = False, journal=print) -> dict

   Comprime la vidéo ``src`` dans ``dst`` (H.264 + AAC mono), entre ``debut`` et ``fin`` (secondes).

   Le son vient de la vidéo, ou de ``son_src`` (ActivePresenter exporte le son à part : ``audio_NNN.mp4``) ;
   ``muet=True`` n'en met aucun. Renvoie ``{duree_s, largeur, hauteur, son: (échantillons mono float32, taux)}``.


.. py:function:: niveau_voix(son: numpy.ndarray, taux: int) -> tuple[float, float]

   Renvoie (niveau de la voix, crête) en dBFS : la voix est le 90e centile du niveau par tranches de 50 ms.


.. py:function:: relever_voix(son: numpy.ndarray, taux: int, cible: float = -20.0, gain_max: float = 30.0, journal=print) -> numpy.ndarray

   Remonte une voix trop faible (micro loin ou réglé bas) vers ``cible`` dBFS, sans dépasser −1 dBFS en crête
   ni ``gain_max`` dB ; une voix déjà assez forte (au-dessus de cible − 4 dB) est laissée telle quelle.


.. py:function:: silences(son: numpy.ndarray, taux: int, min_s: float = 0.6) -> list[tuple[float, float]]

   Renvoie les intervalles de silence ``(début, fin)`` d'au moins ``min_s`` secondes, seuil adapté au niveau de la voix.


.. py:function:: coupes(duree: float, sil: list[tuple[float, float]], pas_min: float, pas_max: float) -> list[float]

   Renvoie les instants de coupe des pas, au milieu d'un silence.

   Tant que le reste dépasse ``pas_max``, la coupe se fait au premier silence d'au moins 1 s situé entre
   ``pas_min`` et ``pas_max`` après le début du pas, sinon au plus long silence de cet intervalle, sinon à
   ``pas_max`` ; un dernier bout plus court que ``pas_min / 2`` n'est pas créé.


.. py:function:: affiche(video: pathlib.Path, t: float, dst: pathlib.Path) -> None

   Enregistre dans ``dst`` l'image de la vidéo à l'instant ``t`` (première image décodée à partir de ``t``).


.. py:function:: trouver_section(chap: dict, ref: str, titre: str | None)

   Renvoie ``(partie, section)`` désignées par « partie/section » ou « section ».

   Avec « partie/nouvelle » et un titre (``--titre``), la section est créée.


.. py:function:: importer(yaml_chap: pathlib.Path, fichier: pathlib.Path, section: str, titre: str | None = None, debut: float = 0.0, fin: float | None = None, decoupe: str = 'silences', pas_min: float = 20, pas_max: float = 90, qualite: int = 28, remplacer: bool = False, son: pathlib.Path | None = None, camera: pathlib.Path | None = None, journal=print) -> int

   Importe une vidéo dans une section d'un chapitre, découpée en pas vidéo ; renvoie le nombre de pas créés.

   Écrit la vidéo comprimée (``videos/``), une image d'affiche et un son par pas (``images/``, ``audio/``),
   éventuellement la vidéo de la webcam (``camera``), puis sauvegarde et réécrit le chapitre.


