scripts.capsuleforge.raccourcis
===============================

.. py:module:: scripts.capsuleforge.raccourcis

.. autoapi-nested-parse::

   CapsuleForge — raccourcis clavier et bips des enregistreurs (Windows).

   Commun à l'enregistreur de didacticiel (``enregistrer``) et à l'enregistreur d'écran, de micro et de webcam
   (``filmer``) : les bips de départ, de pause et de fin, la lecture des touches Ctrl, Maj, Alt et Windows
   réellement enfoncées, et l'interception des raccourcis avant l'application enregistrée.

   Les modificateurs sont lus dans l'état réel du clavier au moment de l'appui : une touche « restée enfoncée »
   après un changement de fenêtre ne fausse pas le raccourci. Un raccourci intercepté n'arrive pas à l'application
   enregistrée, et une touche maintenue enfoncée ne le répète pas.

   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.raccourcis.WM_CLAVIER
   scripts.capsuleforge.raccourcis.WM_RELACHE


Classes
-------

.. autoapisummary::

   scripts.capsuleforge.raccourcis.Intercepteur


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.raccourcis.son_bip
   scripts.capsuleforge.raccourcis.bip
   scripts.capsuleforge.raccourcis.modificateurs_enfonces


Module Contents
---------------

.. py:data:: WM_CLAVIER
   :value: (256, 257, 260, 261)


.. py:data:: WM_RELACHE
   :value: (257, 261)


.. py:function:: son_bip(n: int = 1, frequence: int = 1000, duree_ms: int = 90, silence_ms: int = 60, taux: int = 22050) -> bytes

   Renvoie un fichier WAV (octets) de ``n`` bips courts séparés par un silence.


.. py:function:: bip(n: int = 1)

   Signal sonore sans bloquer l'enregistrement : 1 = départ ou nouvelle étape, 2 = pause / reprise, 3 = fin.

   Joué par la sortie son habituelle de Windows (``winsound.PlaySound``) ; ``winsound.Beep``, muet sur
   beaucoup d'ordinateurs portables, ne sert plus qu'en secours.


.. py:function:: modificateurs_enfonces() -> set

   Renvoie les modificateurs réellement enfoncés (Windows) : ``ctrl``, ``shift``, ``alt``, ``cmd``.

   Renvoie un ensemble vide hors de Windows.


.. py:class:: Intercepteur(action_de)

   Filtre Windows du clavier : exécute les raccourcis et les retire du flux.

   ``action_de(vk)`` reçoit le code virtuel d'une touche appuyée ou relâchée et renvoie la fonction à exécuter
   si c'est un raccourci (en lisant au besoin :func:`modificateurs_enfonces`), sinon ``None``. La fonction est
   exécutée une fois à l'appui ; l'appui et le relâchement de la touche ne parviennent pas à l'application.


   .. py:attribute:: action_de


   .. py:attribute:: ecouteur
      :value: None



   .. py:method:: filtre(msg, data)

      Filtre passé à ``pynput`` (``win32_event_filter``).



   .. py:method:: ecouteur_clavier(**rappels)

      Crée l'écouteur ``pynput`` du clavier avec ce filtre (``rappels`` : ``on_press``, ``on_release``…).

      L'écouteur n'est pas démarré.



