scripts.capsuleforge.capsuleforge
=================================

.. py:module:: scripts.capsuleforge.capsuleforge

.. autoapi-nested-parse::

   CapsuleForge — chapitres de cours interactifs et capsules de simulation logicielle, décrits par un fichier YAML.

   Commandes (abréviations acceptées : « en », « ed », « cons », « conv », « v »…) : ::

       python capsuleforge.py enregistrer freecad_pad [--titre "FreeCAD : premier corps"] [--ecran 1]
           Enregistre une manipulation (Windows). Ctrl+Maj+E = nouvelle étape, Ctrl+Maj+P = pause, Ctrl+Maj+F = fin.
           Sortie : data/capsuleforge/freecad_pad/ (journal.jsonl, images/, capsule.yaml).
       python capsuleforge.py editer freecad_pad
           Ouvre l'éditeur visuel dans le navigateur (image, zone, bulle, chronologie, ajout d'éléments).
       python capsuleforge.py construire freecad_pad [--largeur 1920] [--format webp]
           capsule.yaml -> dist/capsuleforge/freecad_pad/index.html (lecteur « Regarder » / « À vous »).
       python capsuleforge.py construire fiabilite
           Un dossier sans capsule.yaml mais avec chapitre.yaml (cours) : lecteur du chapitre (plan, parcours, sous-titres,
           apparitions, spots, pointeurs), images en WebP et sons en MP3.
       python capsuleforge.py construire fiabilite --scorm chapitre|parties|tout [--scorm-version 1.2]
           En plus : paquets SCORM 2004 pour Moodle (un pour le chapitre, un par partie du tronc, ou les deux).
       python capsuleforge.py traduire fiabilite --langue en [--moteur aucun|argos|deepl]
           Écrit ou complète data/capsuleforge/fiabilite/traductions/en.yaml (source, cible, relu) ; le moteur pré-remplit.
       python capsuleforge.py traduire fiabilite --langue en --importer
           Recopie les traductions dans chapitre.yaml (textes {fr: …, en: …}) : sous-titres et voix dans cette langue.
       python capsuleforge.py traduire fiabilite --langue en --relire
           Écran de relecture dans le navigateur : original, diapositive et son à côté ; « Fait » valide et passe au
           suivant, « Zap » passe sans changer le statut ; enregistrement continu ; bouton « Importer dans le chapitre ».
       python capsuleforge.py video capture.mp4 --chapitre fiabilite --section partie/section [--son audio.mp4] [--titre "…"]
           Importe une vidéo (enregistrement d'écran, export ActivePresenter, clip) : compressée dans videos/, découpée
           en pas aux silences, chaque pas avec son image d'affiche et son son (transcription et relecture comme une diapo).
       python capsuleforge.py filmer tuto1 --section principale/demo --titre "Démo" [--webcam] [--ecran 1] [--micro NOM]
           Filme l'écran, le micro (et la webcam) en même temps, puis importe la vidéo en pas (webcam = caméo).
           Ctrl+Maj+P pause, Ctrl+Maj+F (ou Entrée) fin. « filmer --appareils » liste écrans, caméras et micros ;
           « filmer --tester-micro [NOM] » écoute le micro 4 s et dit si le niveau de la voix convient.
       python capsuleforge.py cameo tuto1 [--position bas-droite] [--taille 0.22] [--forme rond|rectangle]
           Place le médaillon de la webcam (caméo) dans le lecteur ; sans option, affiche le réglage actuel.
       python capsuleforge.py voix fiabilite --langue en [--moteur piper|edge] [--voix en_GB-alan-medium] [--vitesse 1.0]
           Voix de synthèse phrase par phrase (autre langue : à côté du son d'origine ; langue source : pas sans
           enregistrement seulement). Sous-titres, apparitions et objets recalés dans le lecteur.
       python capsuleforge.py convertir freecad_pad
           capsule.yaml (format 1) -> chapitre.yaml (format 2 : parties, sections, pas en scènes), sans toucher à l'original.
       python capsuleforge.py plan fiabilite [--parcours immersive] [--variante ecole1]
           Plan d'un chapitre au format 2, parcours par parcours : noms (B-S2-P4), durées, annexes, questions.
       python capsuleforge.py pptx cours.pptx --chapitre fiabilite [--diapos 6-12] [--largeur 1440]
           Remplit les sections du chapitre qui renvoient à ce diaporama : un pas par diapositive (image de départ,
           audio de narration, durée) et une apparition par clic d'animation. Les images sont produites par PowerPoint.
       python capsuleforge.py transcrire fiabilite [--modele small|medium] [--refaire] [--sections dimensionnement]
           Transcrit l'audio des pas sans narration (Whisper, sur cet ordinateur) : premier jet de scénario à relire.
       python capsuleforge.py relire fiabilite
           Ouvre la relecture dans le navigateur : diapositive, son et texte dit phrase par phrase (corriger, couper,
           fusionner, poser les apparitions). Les phrases horodatées sont la source de la narration et des sous-titres.
       python capsuleforge.py verifier freecad_pad
           Erreurs et avertissements (images manquantes, bulles génériques, étapes sans narration).
       python capsuleforge.py assembler freecad_pad
           Refait le YAML depuis le journal (écrit capsule_reassemblee.yaml si capsule.yaml existe déjà).
       python capsuleforge.py approj projet.approj [--nom nom]
           Reprend une simulation ActivePresenter (lecture seule) en capsule.yaml.

   Un nom sans chemin désigne data/capsuleforge/<nom>/ ; on peut aussi donner un dossier ou un capsule.yaml.
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.capsuleforge.ICI
   scripts.capsuleforge.capsuleforge.VERSION
   scripts.capsuleforge.capsuleforge.DOSSIER
   scripts.capsuleforge.capsuleforge.COMMANDES
   scripts.capsuleforge.capsuleforge.POSITIONS_CAMEO


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.capsuleforge.commande_tolerante
   scripts.capsuleforge.capsuleforge.trouver_capsule
   scripts.capsuleforge.capsuleforge.cmd_enregistrer
   scripts.capsuleforge.capsuleforge.cmd_construire
   scripts.capsuleforge.capsuleforge.cmd_editer
   scripts.capsuleforge.capsuleforge.trouver_chapitre
   scripts.capsuleforge.capsuleforge.cmd_verifier
   scripts.capsuleforge.capsuleforge.cmd_convertir
   scripts.capsuleforge.capsuleforge.cmd_pptx
   scripts.capsuleforge.capsuleforge.cmd_transcrire
   scripts.capsuleforge.capsuleforge.cmd_traduire
   scripts.capsuleforge.capsuleforge.cmd_video
   scripts.capsuleforge.capsuleforge.cmd_filmer
   scripts.capsuleforge.capsuleforge.cmd_cameo
   scripts.capsuleforge.capsuleforge.cmd_voix
   scripts.capsuleforge.capsuleforge.cmd_relire
   scripts.capsuleforge.capsuleforge.cmd_nouvelle
   scripts.capsuleforge.capsuleforge.cmd_plan
   scripts.capsuleforge.capsuleforge.cmd_assembler
   scripts.capsuleforge.capsuleforge.cmd_approj
   scripts.capsuleforge.capsuleforge.cmd_assistant
   scripts.capsuleforge.capsuleforge.main


Module Contents
---------------

.. py:data:: ICI

.. py:data:: VERSION
   :value: '0.9'


.. py:data:: DOSSIER

.. py:data:: COMMANDES
   :value: ['enregistrer', 'editer', 'construire', 'traduire', 'voix', 'video', 'filmer', 'convertir',...


.. py:function:: commande_tolerante(argv: list[str]) -> list[str]

   Remplace le premier argument par le nom exact de la commande qu'il abrège.

   « con », « Vérifier » ou « verif » sont reconnus par leurs premières lettres, sans tenir compte des accents
   ni de la casse ; « v » désigne « verifier ». Renvoie ``argv`` inchangé si rien ne correspond ; arrête le
   programme (``SystemExit``) si l'abréviation est ambiguë.


.. py:function:: trouver_capsule(nom: str) -> pathlib.Path

   Renvoie le chemin du ``capsule.yaml`` désigné par ``nom``.

   ``nom`` peut être un fichier, un dossier ou un nom court cherché dans ``data/capsuleforge`` (sans tenir compte
   des accents ni de la casse ; un début de nom suffit s'il est unique). Le fichier renvoyé n'existe pas
   forcément (dossier d'un chapitre au format 2) ; ``SystemExit`` si rien ne correspond.


.. py:function:: cmd_enregistrer(a)

   Enregistre une manipulation (commande ``enregistrer``, Windows) puis affiche le contrôle de la capsule.

   Le dossier de sortie est ``data/capsuleforge/<nom>`` pour un nom court ; il reçoit ``journal.jsonl``,
   ``images/`` et ``capsule.yaml``.


.. py:function:: cmd_construire(a)

   Construit le lecteur HTML d'une capsule (format 1) ou d'un chapitre (format 2), commande ``construire``.

   Si le dossier contient à la fois ``capsule.yaml`` et ``chapitre.yaml``, l'option ``--lecteur`` choisit le
   format ; à défaut, le fichier modifié en dernier l'emporte. La sortie va par défaut dans
   ``<sorties>/capsuleforge/<nom>/`` ; pour un chapitre, ``--scorm`` produit en plus les paquets SCORM.


.. py:function:: cmd_editer(a)

   Ouvre l'éditeur visuel d'une capsule dans le navigateur (commande ``editer``) ; bloque jusqu'à l'arrêt du serveur.


.. py:function:: trouver_chapitre(nom: str) -> pathlib.Path

   Renvoie le chemin du ``chapitre.yaml`` (format 2) désigné par ``nom``.

   ``nom`` peut être un fichier, un dossier ou un nom court cherché dans ``data/capsuleforge`` comme pour
   :func:`trouver_capsule`. Le fichier renvoyé n'existe pas forcément.


.. py:function:: cmd_verifier(a)

   Contrôle une capsule (format 1) et, s'il existe, le chapitre (format 2) du même dossier.

   Commande ``verifier`` ; renvoie 1 s'il y a au moins une erreur, 0 sinon.


.. py:function:: cmd_convertir(a)

   Convertit ``capsule.yaml`` (format 1) en ``chapitre.yaml`` (format 2) dans le même dossier.

   Commande ``convertir`` ; l'original n'est pas modifié. Un ``chapitre.yaml`` existant n'est remplacé que s'il
   est lui-même issu d'une conversion.


.. py:function:: cmd_pptx(a)

   Reprend un diaporama PowerPoint dans les sections du chapitre qui y renvoient (commande ``pptx``).

   Le travail est fait par :func:`pptx_lire.reprendre` ; cette commande trouve le diaporama et le chapitre,
   puis affiche le rapport du chapitre.


.. py:function:: cmd_transcrire(a)

   Transcrit l'audio des pas d'un chapitre avec Whisper (commande ``transcrire``).

   Écrit ``transcription_journal.txt`` et, si au moins un pas a été transcrit, une copie de l'ancien chapitre
   dans ``sauvegardes/`` puis le ``chapitre.yaml`` mis à jour.


.. py:function:: cmd_traduire(a)

   Prépare, relit (``--relire``) ou importe (``--importer``) la traduction d'un chapitre (commande ``traduire``).


.. py:function:: cmd_video(a)

   Importe une vidéo dans une section du chapitre, découpée en pas (commande ``video``).


.. py:function:: cmd_filmer(a)

   Filme l'écran, le micro et éventuellement la webcam, puis importe la vidéo (commande ``filmer``).

   Avec ``--appareils``, affiche seulement les écrans, caméras et micros disponibles et renvoie 0.


.. py:data:: POSITIONS_CAMEO
   :value: ('bas-droite', 'bas-gauche', 'haut-droite', 'haut-gauche', 'aucune')


.. py:function:: cmd_cameo(a)

   Règle le médaillon de la webcam dans le lecteur (commande ``cameo``) : position, taille, forme.

   Sans option, affiche le réglage actuel. Le chapitre est sauvegardé dans ``sauvegardes/`` avant d'être réécrit.


.. py:function:: cmd_voix(a)

   Produit la voix de synthèse d'un chapitre, phrase par phrase (commande ``voix``).


.. py:function:: cmd_relire(a)

   Ouvre la relecture du texte dit d'un chapitre dans le navigateur (commande ``relire``).


.. py:function:: cmd_nouvelle(a)

   Crée une capsule neuve dans data/capsuleforge/<nom>, ou au chemin donné (vide, ou plan d'après un diaporama).


.. py:function:: cmd_plan(a)

   Affiche le plan d'un chapitre au format 2, parcours par parcours (commande ``plan``).


.. py:function:: cmd_assembler(a)

   Refait le YAML de la capsule à partir de ``journal.jsonl`` (commande ``assembler``).

   Écrit ``capsule.yaml``, ou ``capsule_reassemblee.yaml`` si ``capsule.yaml`` existe déjà.


.. py:function:: cmd_approj(a)

   Reprend un projet ActivePresenter (``.approj``, lu sans être modifié) en capsule (commande ``approj``).

   Écrit ``data/capsuleforge/<nom>/capsule.yaml`` ; refuse de remplacer une capsule existante.


.. py:function:: cmd_assistant(_a)

   Propose un menu pas à pas dans la console, puis lance la commande choisie (commande ``assistant``).


.. py:function:: main(argv=None)

   Point d'entrée en ligne de commande : analyse ``argv`` et lance la commande demandée.

   ``argv`` vaut par défaut ``sys.argv[1:]`` ; les abréviations de commande sont acceptées. Renvoie le code
   de sortie (0 si la commande ne renvoie rien).


