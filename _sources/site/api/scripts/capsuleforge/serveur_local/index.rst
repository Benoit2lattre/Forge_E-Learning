scripts.capsuleforge.serveur_local
==================================

.. py:module:: scripts.capsuleforge.serveur_local

.. autoapi-nested-parse::

   CapsuleForge — petit serveur local commun aux écrans ouverts dans le navigateur.

   L'éditeur de capsule (``editer``), la relecture d'un chapitre (``relire``) et la relecture d'une traduction
   (``traduire --relire``) passent tous par ce module : un serveur qui n'écoute que sur cet ordinateur (127.0.0.1),
   refuse les requêtes venues d'un autre site ouvert dans le navigateur et sert la page, ses données et ses fichiers.

   Chaque écran définit une sous-classe de :class:`Gestionnaire` avec ses méthodes ``get`` et ``post`` ; ce module
   fournit le reste : envoi des réponses, fichiers, sons avec lecture partielle, choix du port, boucle du serveur.

   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.serveur_local.TYPES
   scripts.capsuleforge.serveur_local.HOTES


Classes
-------

.. autoapisummary::

   scripts.capsuleforge.serveur_local.Gestionnaire


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.serveur_local.type_de
   scripts.capsuleforge.serveur_local.demarrer
   scripts.capsuleforge.serveur_local.servir


Module Contents
---------------

.. py:data:: TYPES

.. py:data:: HOTES
   :value: ('127.0.0.1', 'localhost')


.. py:function:: type_de(f: pathlib.Path) -> str

   Type MIME d'un fichier d'après son extension.


.. py:class:: Gestionnaire(request, client_address, server)



   Gestionnaire HTTP de base des écrans de CapsuleForge.

   Une sous-classe définit ``get(chemin, url)`` et ``post(chemin, corps)`` ; un chemin inconnu reçoit 404.
   Une erreur levée dans ces méthodes est renvoyée à la page en JSON (``{"ok": false, "message": …}``, code 500).


   .. py:attribute:: server_version
      :value: 'CapsuleForge'



   .. py:method:: log_message(*a)

      Log an arbitrary message.

      This is used by all other logging functions.  Override
      it if you have specific logging wishes.

      The first argument, FORMAT, is a format string for the
      message to be logged.  If the format string contains
      any % escapes requiring parameters, they should be
      specified as subsequent arguments (it's just like
      printf!).

      The client ip and current date/time are prefixed to
      every message.

      Unicode control characters are replaced with escaped hex
      before writing the output to stderr.




   .. py:method:: do_GET()


   .. py:method:: do_POST()


   .. py:method:: get(chemin: str, url)

      Répond à ``GET chemin`` (``url`` : adresse analysée, pour les paramètres).



   .. py:method:: post(chemin: str, corps: bytes)

      Répond à ``POST chemin`` ; ``corps`` : octets reçus.



.. py:function:: demarrer(gestionnaire: type[Gestionnaire], port: int, essais: int = 20) -> tuple[http.server.ThreadingHTTPServer, str]

   Crée le serveur sur le premier port libre à partir de ``port`` ; renvoie (serveur, adresse).

   Le serveur n'écoute que sur 127.0.0.1 et n'est pas encore lancé.


.. py:function:: servir(srv: http.server.ThreadingHTTPServer, adresse: str, navigateur: bool = True) -> bool

   Ouvre la page (si ``navigateur``) et fait tourner le serveur jusqu'à son arrêt ou Ctrl+C.

   Renvoie ``True`` si l'arrêt vient de Ctrl+C.


