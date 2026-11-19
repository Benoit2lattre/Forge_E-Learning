scripts.capsuleforge.construire_chapitre
========================================

.. py:module:: scripts.capsuleforge.construire_chapitre

.. autoapi-nested-parse::

   CapsuleForge — construction du lecteur d'un chapitre (format 2) : de ``chapitre.yaml`` à ``index.html``.

   Sortie : ``<sortie>/index.html`` (lecteur autonome, données incluses : s'ouvre aussi depuis le disque),
   ``<sortie>/images/`` (WebP par défaut) et ``<sortie>/audio/`` (MP3 mono par défaut, WAV recopié si la conversion
   n'est pas possible). Rien n'est supprimé dans la sortie ; un média déjà converti et plus récent que sa source
   est gardé.

   Le lecteur joue les pas d'une section à la suite : image de départ, apparitions, sous-titres tirés des phrases,
   spots, cadres, pointeurs et caches. Les parcours du chapitre filtrent le plan (annexes absentes, à la demande
   ou intégrées). En fin de section, il pose les questions tirées de la banque QuizForge désignée par la section
   (vrai/faux, QCM, numérique), avec leurs rétroactions.

   Une partie peut porter un exercice ExoForge (``exercice: {outil: exoforge, fiche: …yaml}``, ou une liste) : la fiche
   est construite par ``scripts/exoforge/build.py`` si ``dist/exoforge/<id>/`` manque ou est plus ancien qu'elle ou que le
   moteur, ses fichiers sont recopiés dans ``<sortie>/exercices/<id>/``, et l'exercice devient la dernière section de la
   partie. Le lecteur l'affiche dans un cadre et lui fournit une API SCORM 1.2 : score, réussite et réponses sont
   gardés dans le navigateur (jauge « Pratique », journal « exercices »).

   Paquets SCORM 2004 (option ``scorm``) : « chapitre » = un paquet pour tout le chapitre ; « parties » = un paquet par partie
   du tronc, avec les annexes et exercices qu'elle appelle ; « tout » = les deux. Dans une plateforme (Moodle), le lecteur
   y garde l'avancement (``cmi.suspend_data``), renvoie l'achèvement (sections du tronc vues), une note = la pratique en %
   pondérée (question : poids 1, 1 si juste au moins une fois ; exercice : ``poids`` de l'entrée ``exercice``, par défaut sa
   durée en minutes, fois son meilleur score ; poids 0 = hors note) et une interaction par section vue, question
   répondue et réponse d'exercice. Paquets écrits à côté de la sortie : ``<nom>_scorm2004.zip``, ``<nom>_<lettre>_<id>_scorm2004.zip``.
   Option ``scorm_version="1.2"`` : mêmes paquets au format SCORM 1.2 (``…_scorm12.zip``), le seul que Moodle prend
   officiellement en charge ; l'avancement gardé est alors limité à 4 096 caractères (les plus anciennes sections vues
   sont oubliées au-delà) et il n'y a ni mesure de progression ni description des interactions.
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.construire_chapitre.ICI
   scripts.capsuleforge.construire_chapitre.DEBIT_MP3
   scripts.capsuleforge.construire_chapitre.OBJETS
   scripts.capsuleforge.construire_chapitre.MINUTES_PAR_ETAPE
   scripts.capsuleforge.construire_chapitre.TEXTES_FICHE
   scripts.capsuleforge.construire_chapitre.UI_EXOFORGE
   scripts.capsuleforge.construire_chapitre.PREFIXE_EXERCICE
   scripts.capsuleforge.construire_chapitre.TYPES_QUESTION


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.construire_chapitre.textes_fiche
   scripts.capsuleforge.construire_chapitre.page_traduite
   scripts.capsuleforge.construire_chapitre.fiche_exoforge
   scripts.capsuleforge.construire_chapitre.sans_prefixe_exercice
   scripts.capsuleforge.construire_chapitre.exercices_partie
   scripts.capsuleforge.construire_chapitre.textes_question
   scripts.capsuleforge.construire_chapitre.questions_ref
   scripts.capsuleforge.construire_chapitre.questions_section
   scripts.capsuleforge.construire_chapitre.didacticiel
   scripts.capsuleforge.construire_chapitre.construire


Module Contents
---------------

.. py:data:: ICI

.. py:data:: DEBIT_MP3
   :value: 64000


.. py:data:: OBJETS
   :value: ('spot', 'cadre', 'pointeur', 'cache')


.. py:data:: MINUTES_PAR_ETAPE
   :value: 1.5


.. py:data:: TEXTES_FICHE

.. py:data:: UI_EXOFORGE

.. py:function:: textes_fiche(obj, chemin: str = '')

   Produit ``(chemin, texte)`` pour chaque texte affiché d'une fiche ExoForge (clés de :data:`TEXTES_FICHE`).

   Le chemin suit la structure de la fiche (``etapes/2/options/1/retour``) ; il sert de clé de traduction
   (``exercice/<id>/<chemin>``) et retrouve le même texte dans la configuration incluse dans la page construite.


.. py:function:: page_traduite(code: str, ident: str, langue: str, d: dict, perimees: list) -> str | None

   Renvoie la page d'un exercice ExoForge traduite (textes de la fiche, interface du moteur), ou ``None`` sans traduction.

   ``d`` : éléments du fichier de traduction (clé → élément). Les sons du commentaire (langue source) sont retirés.


.. py:function:: fiche_exoforge(nom: str, dossier: pathlib.Path) -> pathlib.Path | None

   Renvoie le chemin d'une fiche ExoForge, cherchée à côté du chapitre puis dans ``data/exoforge`` (``None`` si absente).


.. py:data:: PREFIXE_EXERCICE

.. py:function:: sans_prefixe_exercice(titre: str) -> str

   Titre d'une fiche ExoForge sans « Exercice : » en tête : le lecteur l'ajoute déjà devant le titre.


.. py:function:: exercices_partie(p: dict, dossier: pathlib.Path, sortie: pathlib.Path, journal=print, trad_ext: dict | None = None, perimees: list | None = None) -> list[dict]

   Renvoie les exercices ExoForge d'une partie sous forme de sections « exercice » du lecteur (HTML de l'exercice inclus).

   Chaque fiche est construite si besoin (``scripts/exoforge/build.py``) et ses fichiers sont recopiés dans
   ``<sortie>/exercices/<id>/`` ; une fiche introuvable ou qui ne se construit pas est signalée et ignorée.
   ``trad_ext`` (langue → éléments ``exercice/…`` des fichiers de traduction) ajoute une page traduite par langue
   (``html_tr``) et le titre traduit de la section (``tr``).


.. py:data:: TYPES_QUESTION
   :value: ('vf', 'qcm', 'numerique')


.. py:function:: textes_question(x: dict) -> list[tuple[str, str]]

   Renvoie les textes traduisibles d'une question convertie : ``[(chemin, texte)]``, chemins du type ``choix/1/texte``.

   Ce sont les clés du fichier de traduction du chapitre (``question/<banque>/<titre>/<chemin>``) et de ``tr`` dans le lecteur.


.. py:function:: questions_ref(ref: dict, dossier: pathlib.Path, cache: dict, journal=print, sec_id: str = '') -> list[dict] | None

   Renvoie les questions converties d'un renvoi ``{banque, id | etiquette, nombre}`` (types joués par le lecteur).

   Chaque question porte ``cle_tr`` = ``question/<banque>/<titre>``, préfixe de ses clés de traduction.
   Renvoie ``None`` si la banque est introuvable.


.. py:function:: questions_section(sec: dict, dossier: pathlib.Path, cache: dict, journal=print) -> list[dict]

   Convertit les renvois « questions » d'une section en lots ``[{nombre, questions}]``.

   Le lecteur tire ``nombre`` questions par lot ; seuls les types vrai/faux, QCM et numérique sont gardés.


.. py:function:: didacticiel(q: dict, chap: dict) -> dict | None

   Renvoie, pour un pas de didacticiel (gestes, bulle), ce que le lecteur joue en « Regarder » et attend en « À vous ».

   Renvoie ``None`` si le pas n'a ni geste ni bulle.


.. py:function:: construire(chapitre_yaml: pathlib.Path, sortie: pathlib.Path, largeur: int | None = None, fmt: str = 'webp', audio: str = 'mp3', journal=print, scorm: str | None = None, scorm_version: str = '2004') -> pathlib.Path

   Construit le lecteur d'un chapitre et renvoie le chemin de ``<sortie>/index.html``.

   ``largeur`` : largeur maximale des images (réduction seulement) ; ``fmt`` : ``webp`` ou ``png`` ;
   ``audio`` : ``mp3`` pour convertir les sons (sinon recopiés) ; ``scorm`` : ``chapitre``, ``parties`` ou
   ``tout`` pour écrire aussi les paquets SCORM ; ``scorm_version`` : ``2004`` (défaut) ou ``1.2``. Arrête le programme (``SystemExit``) si le chapitre
   contient des erreurs bloquantes.


