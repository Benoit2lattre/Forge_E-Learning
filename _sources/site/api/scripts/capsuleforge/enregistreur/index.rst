scripts.capsuleforge.enregistreur
=================================

.. py:module:: scripts.capsuleforge.enregistreur

.. autoapi-nested-parse::

   CapsuleForge — enregistreur de simulation logicielle (Windows).

   Ce qu'il enregistre, comme ActivePresenter en mode « simulation interactive » :

   - une image de l'écran juste avant chaque action (clic, double-clic, clic droit, glisser, molette,
     saisie au clavier, raccourci) ;
   - la trajectoire de la souris depuis l'action précédente ;
   - le contrôle visé, lu par l'accessibilité de Windows (UI Automation) : nom, type, rectangle.
     Si l'application n'expose rien (vue 3D, OpenGL…), le pas reste valide avec une zone par défaut.

   Raccourcis pendant l'enregistrement (modifiables par options, ex. ``--touche-etape f8``) : ::

     Ctrl+Maj+E : nouvelle étape (le pas suivant ouvre une étape)        1 bip
     Ctrl+Maj+P : pause / reprise (avant de taper un mot de passe)       2 bips
     Ctrl+Maj+F : fin de l'enregistrement                                3 bips

   Ils sont interceptés : l'application enregistrée ne les reçoit pas. Pas de touches F1-F12 par
   défaut : sur les portables et claviers compacts, elles demandent Fn et commandent souvent le
   système (mode avion, émojis…).

   Sortie : ``<dossier>/journal.jsonl`` (écrit au fil de l'eau), ``<dossier>/images/pNNN.png``, puis
   ``<dossier>/capsule.yaml`` (assemblé à la fin ; à refaire avec « capsuleforge assembler » si besoin).

   Dépendances (Windows) : pynput, mss, Pillow ; uiautomation facultatif (sans lui : pas de nom de contrôle).
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.enregistreur.DOUBLE_CLIC_MS
   scripts.capsuleforge.enregistreur.DOUBLE_CLIC_PX
   scripts.capsuleforge.enregistreur.GLISSER_PX
   scripts.capsuleforge.enregistreur.MOLETTE_REGROUPE_MS
   scripts.capsuleforge.enregistreur.IMAGES_PAR_SECONDE
   scripts.capsuleforge.enregistreur.SURVOL_MS
   scripts.capsuleforge.enregistreur.MODIFICATEURS
   scripts.capsuleforge.enregistreur.NOMS_TOUCHES


Classes
-------

.. autoapisummary::

   scripts.capsuleforge.enregistreur.Enregistreur


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.enregistreur.nom_processus
   scripts.capsuleforge.enregistreur.lire_raccourci
   scripts.capsuleforge.enregistreur.libelle_raccourci
   scripts.capsuleforge.enregistreur.nom_vk
   scripts.capsuleforge.enregistreur.enregistrer


Module Contents
---------------

.. py:data:: DOUBLE_CLIC_MS
   :value: 450


.. py:data:: DOUBLE_CLIC_PX
   :value: 6


.. py:data:: GLISSER_PX
   :value: 12


.. py:data:: MOLETTE_REGROUPE_MS
   :value: 700


.. py:data:: IMAGES_PAR_SECONDE
   :value: 8


.. py:data:: SURVOL_MS
   :value: 120


.. py:class:: Enregistreur(dossier: pathlib.Path, ecran: int = 1, titre: str | None = None, application: str | None = None, touche_etape='ctrl+shift+e', touche_pause='ctrl+shift+p', touche_fin='ctrl+shift+f', accessibilite: bool = True)

   Enregistreur d'une manipulation : captures d'écran, souris, clavier et accessibilité de Windows.

   À la création, le dossier ``images/`` est créé et ``journal.jsonl`` ouvert en ajout dans ``dossier``.
   :meth:`lancer` déroule l'enregistrement jusqu'au raccourci de fin. ``ecran`` est le numéro d'écran de
   ``mss`` (1 = principal) ; ``touche_etape``, ``touche_pause`` et ``touche_fin`` sont des raccourcis au
   format de :func:`lire_raccourci` ; ``accessibilite=False`` désactive la lecture des noms de contrôles.


   .. py:attribute:: dossier


   .. py:attribute:: journal


   .. py:attribute:: num_ecran
      :value: 1



   .. py:attribute:: touches


   .. py:attribute:: raccourcis


   .. py:attribute:: kl
      :value: None



   .. py:attribute:: intercepteur


   .. py:attribute:: avec_acc
      :value: True



   .. py:attribute:: t0


   .. py:attribute:: actif
      :value: True



   .. py:attribute:: en_pause
      :value: False



   .. py:attribute:: fini


   .. py:attribute:: verrou


   .. py:attribute:: anneau


   .. py:attribute:: survol
      :value: None



   .. py:attribute:: trajet
      :type:  list[list[float]]
      :value: []



   .. py:attribute:: dernier_point
      :value: None



   .. py:attribute:: n
      :value: 0



   .. py:attribute:: dernier_clic
      :value: None



   .. py:attribute:: appui
      :value: None



   .. py:attribute:: saisie
      :value: None



   .. py:attribute:: molette
      :value: None



   .. py:attribute:: modifs


   .. py:attribute:: a_ecrire
      :type:  queue.Queue


   .. py:attribute:: demandes
      :type:  queue.Queue


   .. py:attribute:: verrou_journal


   .. py:attribute:: moniteur
      :value: None



   .. py:method:: t() -> int

      Renvoie le temps écoulé depuis la création de l'enregistreur, en millisecondes.



   .. py:method:: ecrire(evt: dict)

      Ajoute un événement au journal (une ligne JSON), écrit immédiatement sur le disque.



   .. py:method:: image_avant(t_evt: int)

      Renvoie la dernière image de l'anneau prise avant l'instant ``t_evt`` (en ms).

      Renvoie le couple (octets BGRA, (largeur, hauteur)) ; à défaut la plus ancienne image de l'anneau, ou
      ``None`` si l'anneau est vide.



   .. py:method:: sauver_image(nom: str, img) -> str | None

      Met l'image en file d'écriture sous ``images/<nom>.png`` ; renvoie ce chemin relatif, ou ``None`` sans image.



   .. py:method:: cible_au_point(x, y, t_evt)

      Renvoie une copie de la dernière cible lue sous la souris si elle est récente et proche du point.

      La lecture doit dater de moins de 1,5 s et être à 4 px au plus de (x, y) ; sinon renvoie ``None``.



   .. py:method:: rel(x, y)

      Convertit des coordonnées d'écran absolues en coordonnées relatives à l'écran enregistré.



   .. py:method:: cible_rel(cible)

      Renvoie une copie de la cible avec ``cadre_abs`` remplacé par ``cadre`` en coordonnées relatives.



   .. py:method:: nouveau_pas(action, x, y, t_evt, img, cible, **extra) -> str

      Écrit un pas dans le journal (image, point, trajet, cible) et renvoie son identifiant (``p001``…).

      Les champs de ``extra`` sont ajoutés tels quels à l'événement. Un clic sans cible est mis en file pour
      être relu par l'accessibilité après coup.



   .. py:method:: vider_saisie()

      Termine la saisie au clavier en cours et l'écrit comme pas « saisie » si elle contient du texte.



   .. py:method:: vider_molette()

      Termine la série de crans de molette en cours et l'écrit comme pas « molette ».



   .. py:method:: on_move(x, y)

      Suit la souris (rappel de ``pynput``) : dernier point et trajet depuis l'action précédente.



   .. py:method:: on_click(x, y, bouton, enfonce)

      Traite un appui ou un relâchement de bouton (rappel de ``pynput``).

      Au relâchement, écrit un pas « glisser », « clic », « clic_droit » ou « clic_milieu » ; un second clic
      gauche rapproché transforme le pas précédent en « double_clic ».



   .. py:method:: on_scroll(x, y, dx, dy)

      Regroupe les crans de molette successifs au même endroit en un seul pas (rappel de ``pynput``).



   .. py:method:: on_press(key)

      Traite l'appui d'une touche (rappel de ``pynput``).

      Les caractères s'accumulent dans la saisie en cours ; une touche spéciale ou un raccourci devient un pas
      « touche ». Renvoie ``False`` (arrêt de l'écoute) sur le raccourci de fin.



   .. py:method:: on_release(key)

      Retire un modificateur relâché de l'ensemble suivi (rappel de ``pynput``).



   .. py:method:: terminer()

      Termine l'enregistrement : vide la saisie et la molette en cours, écrit l'événement « fin » et son image.



   .. py:method:: lancer(compte_a_rebours: int = 3)

      Déroule l'enregistrement : fils de capture, compte à rebours, écoute de la souris et du clavier.

      Bloque jusqu'au raccourci de fin, attend l'écriture des images puis ferme le journal.



.. py:function:: nom_processus(pid: int) -> str

   Nom de l'exécutable d'un processus (FreeCAD.exe, explorer.exe…), sans dépendance externe.


.. py:function:: lire_raccourci(texte: str)

   Analyse un raccourci écrit en texte et renvoie le couple (modificateurs, touche).

   Accepte « Ctrl+Maj+E », « ctrl+shift+e », « F8 » et des variantes d'écriture ; les modificateurs sont
   rendus sous la forme ``ctrl``, ``shift``, ``alt`` ou ``cmd`` et la touche en minuscules.


.. py:function:: libelle_raccourci(texte: str) -> str

   Renvoie le libellé affichable d'un raccourci (ex. « Ctrl+Maj+E »).


.. py:function:: nom_vk(vk: int) -> str | None

   Renvoie le nom d'un code de touche virtuelle Windows au format de :func:`lire_raccourci`.

   Seuls les lettres, chiffres et touches F1 à F24 sont reconnus ; renvoie ``None`` pour les autres.


.. py:data:: MODIFICATEURS
   :value: ('ctrl_l', 'ctrl_r', 'ctrl', 'alt_l', 'alt_r', 'alt_gr', 'alt', 'cmd', 'cmd_l', 'cmd_r',...


.. py:data:: NOMS_TOUCHES

.. py:function:: enregistrer(dossier: pathlib.Path, **options) -> pathlib.Path

   Enregistre une manipulation dans ``dossier`` puis assemble la capsule ; renvoie le chemin de ``capsule.yaml``.

   Les ``options`` sont passées à :class:`Enregistreur`. Fonctionne sous Windows seulement et refuse un dossier
   qui contient déjà un enregistrement (``SystemExit``).


