scripts.capsuleforge.editeur
============================

.. py:module:: scripts.capsuleforge.editeur

.. autoapi-nested-parse::

   CapsuleForge — éditeur visuel d'une capsule (serveur local + page editeur.html).

   « capsuleforge editer tuto1 » démarre un petit serveur sur cet ordinateur seulement (127.0.0.1) et ouvre
   l'éditeur dans le navigateur. La page lit et écrit ``capsule.yaml`` par ce serveur ; rien ne sort de cet ordinateur.

   Ce que fait le serveur (module :mod:`serveur_local`) : ::

     GET  /                      la page de l'éditeur
     GET  /api/capsule           la capsule (JSON) et la liste des images
     POST /api/capsule           enregistre capsule.yaml (copie de l'ancien dans sauvegardes/, une par séance)
     GET  /images/<nom>          une image de la capsule
     GET  /vendor/mathjax.js      MathJax, pour l'aperçu des formules
     GET  /vignette/<nom>?x=&y=  vignette centrée sur le point cliqué (chronologie)
     POST /api/image             ajoute une image (diapositive exportée, capture) ramenée à la taille de l'écran
     POST /api/apercu            construit le lecteur (mode aperçu) ; GET /apercu/… le sert

   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.editeur.ICI
   scripts.capsuleforge.editeur.ORDRE_PAS
   scripts.capsuleforge.editeur.ORDRE_ETAPE
   scripts.capsuleforge.editeur.ORDRE_CAPSULE


Classes
-------

.. autoapisummary::

   scripts.capsuleforge.editeur.SeanceEditeur


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.editeur.normaliser
   scripts.capsuleforge.editeur.demarrer
   scripts.capsuleforge.editeur.editer


Module Contents
---------------

.. py:data:: ICI

.. py:data:: ORDRE_PAS
   :value: ['ignorer', 'raison', 'id', 'action', 'image', 'point', 'arrivee', 'crans', 'texte', 'accepte',...


.. py:data:: ORDRE_ETAPE
   :value: ['titre', 'narration', 'audio', 'arret', 'pas']


.. py:data:: ORDRE_CAPSULE
   :value: ['format', 'titre', 'langue', 'ecran', 'source', 'reglages', 'masques', 'etapes', 'image_finale']


.. py:function:: normaliser(cap: dict) -> dict

   Renvoie la capsule reçue de la page, prête à écrire : clés vides retirées, ordre stable, coordonnées entières.


.. py:class:: SeanceEditeur(capsule_yaml: pathlib.Path, sortie: pathlib.Path)

   État du serveur de l'éditeur pour un ``capsule.yaml`` : lecture, écriture, images, vignettes, aperçu.

   ``sortie`` est le dossier où l'aperçu du lecteur est construit.


   .. py:attribute:: yaml


   .. py:attribute:: dossier


   .. py:attribute:: sortie


   .. py:attribute:: sauvegarde_faite
      :value: False



   .. py:attribute:: verrou


   .. py:attribute:: vignettes
      :type:  dict


   .. py:method:: lire() -> dict

      Renvoie la capsule, la liste des images, les erreurs, les avertissements et les types de contrôle.



   .. py:method:: ecrire(cap: dict) -> dict

      Normalise et enregistre la capsule envoyée par la page ; renvoie erreurs, avertissements et heure.

      Une copie de l'ancien ``capsule.yaml`` est faite dans ``sauvegardes/`` à la première écriture ; le fichier
      est écrit sous un nom temporaire puis renommé. ``ValueError`` si ``etapes`` ou ``ecran`` manque.



   .. py:method:: chemin_image(nom: str) -> pathlib.Path | None

      Renvoie le chemin de l'image ``nom`` dans ``images/`` si elle existe, sinon ``None``.



   .. py:method:: vignette(nom: str, x: float | None, y: float | None, l: int = 176, h: int = 110) -> bytes | None

      Renvoie une vignette JPEG de l'image ``nom`` (``None`` si l'image manque).

      Avec un point (x, y), la vignette montre la zone de 704 × 440 px qui l'entoure (ce que l'on clique) ;
      sinon l'image entière. Les vignettes sont gardées en mémoire.



   .. py:method:: ajouter_image(octets: bytes, ecran: dict) -> str

      Ajoute une image importée dans ``images/ajout_NNN.png`` et renvoie son nom.

      L'image est ramenée à la taille de l'écran de la capsule (bandes noires si les proportions diffèrent).



   .. py:method:: apercu() -> dict

      Construit le lecteur en mode aperçu dans le dossier de sortie ; renvoie l'adresse ou le message d'erreur.



.. py:function:: demarrer(capsule_yaml: pathlib.Path, sortie: pathlib.Path, port: int = 8765) -> tuple[http.server.ThreadingHTTPServer, str]

   Crée le serveur sur le premier port libre à partir de ``port`` ; renvoie (serveur, adresse).

   Le serveur n'écoute que sur 127.0.0.1 et n'est pas encore lancé.


.. py:function:: editer(capsule_yaml: pathlib.Path, sortie: pathlib.Path, port: int = 8765, navigateur: bool = True)

   Lance l'éditeur visuel d'une capsule : serveur local et, si ``navigateur``, ouverture de la page.

   ``sortie`` reçoit l'aperçu du lecteur. Bloque jusqu'à Ctrl+C.


