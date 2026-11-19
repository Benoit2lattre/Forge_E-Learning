scripts.capsuleforge.relecture
==============================

.. py:module:: scripts.capsuleforge.relecture

.. autoapi-nested-parse::

   CapsuleForge — relecture d'un chapitre (serveur local + page relecture.html).

   « capsuleforge relire fiabilite » démarre un petit serveur sur cet ordinateur seulement (127.0.0.1) et ouvre la
   page de relecture : la diapositive, le son, et le texte dit, phrase par phrase. On y corrige le texte en
   l'écoutant, on coupe ou on fusionne les phrases, et on pose les apparitions à l'instant voulu.

   Les phrases horodatées d'un pas (``phrases``) sont la seule source du texte dit : la narration et, plus tard, les
   sous-titres en sont tirés. À la première ouverture, elles sont préparées à partir de la narration et de la
   transcription (``transcriptions/<id>.json``), sans rien écrire tant que l'on n'enregistre pas.

   Routes du serveur (module :mod:`serveur_local`) : ::

     GET  /                  la page
     GET  /api/chapitre      le chapitre : pas, phrases, apparitions, mots horodatés de la transcription
     POST /api/pas           enregistre les pas modifiés dans chapitre.yaml (copie de l'ancien dans sauvegardes/)
     POST /api/fin           arrête le serveur (bouton « Quitter ») ; il s'arrête aussi seul quand la page est fermée
     POST /api/depart        la page se ferme ou se recharge : arrêt dans 4 s, sauf si elle revient
     POST /api/<action>      autres écrans (traduction…) : transmis à la méthode action de la séance
     GET  /media/<chemin>    une image ou un son du chapitre (lecture partielle acceptée, pour se déplacer dans le son)

   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.relecture.ICI
   scripts.capsuleforge.relecture.TYPES
   scripts.capsuleforge.relecture.AJOUTS


Classes
-------

.. autoapisummary::

   scripts.capsuleforge.relecture.SeanceRelecture


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.relecture.demarrer
   scripts.capsuleforge.relecture.relire


Module Contents
---------------

.. py:data:: ICI

.. py:data:: TYPES

.. py:data:: AJOUTS
   :value: ('spot', 'cadre', 'pointeur', 'cache')


.. py:class:: SeanceRelecture(chemin: pathlib.Path)

   État du serveur de relecture pour un ``chapitre.yaml`` : lecture, écriture des pas, arrêt automatique.

   Une sous-classe peut définir ``PAGE`` (page HTML servie à la place de ``relecture.html``) et une méthode
   ``action(nom, donnees)`` appelée pour les autres requêtes ``POST /api/<nom>``.


   .. py:attribute:: arreter


   .. py:attribute:: minuterie
      :value: None



   .. py:attribute:: yaml


   .. py:attribute:: dossier


   .. py:attribute:: sauvegarde_faite
      :value: False



   .. py:attribute:: verrou


   .. py:method:: remarques(chap: dict) -> tuple[dict, list]

      Résultat de :func:`format_chapitre.verifier` rangé pour la page : ``(remarques par pas, remarques générales)``.

      Chaque remarque est ``{"niveau": "erreur" | "avertissement", "texte": …}`` ; un message de la forme
      « D3-2 (d08) : … » est rangé sous le pas ``d08``, les autres (sections, parties, chapitre) sont générales.



   .. py:method:: lire() -> dict

      Renvoie le chapitre tel que la page l'affiche : pas non écartés, phrases, apparitions, objets, mots.

      Un pas sans ``phrases`` reçoit des phrases préparées à partir de la narration et de la transcription
      (marqué ``prepare``) ; rien n'est écrit sur le disque.



   .. py:method:: ecrire(modifs: dict) -> dict

      Enregistre dans ``chapitre.yaml`` les modifications envoyées par la page ; renvoie un compte rendu.

      ``modifs`` associe à l'identifiant d'un pas un dictionnaire pouvant contenir ``phrases`` (liste),
      ``apparitions`` (identifiant -> instant), ``objets`` (spots, cadres, pointeurs, caches) et ``relu``
      (booléen). Le chapitre est relu sur le disque et seuls ces champs sont changés ; une copie de l'ancien
      fichier est faite dans ``sauvegardes/`` à la première écriture.



   .. py:method:: page_partie()

      Programme l'arrêt du serveur dans 4 s : la page se ferme ou se recharge (annulé si elle revient).



   .. py:method:: page_revenue()

      Annule l'arrêt programmé par :meth:`page_partie`.



   .. py:method:: media(rel: str) -> pathlib.Path | None

      Renvoie le fichier du chapitre désigné par ``rel`` s'il est dans le dossier et d'un type servi, sinon ``None``.



.. py:function:: demarrer(chapitre_yaml: pathlib.Path, port: int = 8775, seance=None) -> tuple[http.server.ThreadingHTTPServer, str]

   Crée le serveur sur le premier port libre à partir de ``port`` ; renvoie (serveur, adresse).

   ``seance`` permet de fournir une autre séance que :class:`SeanceRelecture` (écran de traduction, par exemple). Le
   serveur n'écoute que sur 127.0.0.1 et n'est pas encore lancé.


.. py:function:: relire(chapitre_yaml: pathlib.Path, port: int = 8775, navigateur: bool = True)

   Lance la relecture d'un chapitre : serveur local et, si ``navigateur``, ouverture de la page.

   Bloque jusqu'à la fermeture de la page, au bouton « Quitter » ou à Ctrl+C.


