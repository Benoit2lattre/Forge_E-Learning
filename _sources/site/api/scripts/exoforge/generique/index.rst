scripts.exoforge.generique
==========================

.. py:module:: scripts.exoforge.generique

.. autoapi-nested-parse::

   ExoForge — construction des fiches génériques (étapes info / choix, rappel, audio, LaTeX).

   Appelé par ``build.py`` quand la fiche contient « etapes ».

   Deux temps, comme avec ActivePresenter :

   1. construction initiale, sans média : l'exercice fonctionne, et ``media/<id>/script_enregistrement.md``
      liste chaque emplacement audio avec le texte à dire et les apparitions à marquer ;
   2. reprise : les fichiers déposés dans ``media/<id>/`` sont pris en compte à la construction suivante ::

         <slot>.mp3 (ou .m4a, .wav, .ogg)  enregistrement
         <slot>_a1.mp3, <slot>_a2.mp3 …    ou : enregistrement découpé (dans Audacity) ; le segment k fait
                                           apparaître le k-ième élément, et les segments sont lus à la suite
         <slot>.txt                        transcription affichée sous l'étape (accessibilité)
         <slot>.reperes.json               temps d'apparition (fichier unique), relevés avec le mode auteur
         <id>_explication.mp3              facultatif : commentaire audio de l'explication d'une question
         <id>_retour_<lettre>.mp3          facultatif : commentaire audio du retour de la proposition a, b, c…

      Les noms sont reconnus sans tenir compte des majuscules (``rappel_PPV.mp3`` = ``rappel_ppv.mp3``) ;
      dans le paquet SCORM ils sont écrits en minuscules (Moodle distingue les majuscules).



Attributes
----------

.. autoapisummary::

   scripts.exoforge.generique.RACINE
   scripts.exoforge.generique.MOTEUR
   scripts.exoforge.generique.FEUILLE
   scripts.exoforge.generique.MATHJAX
   scripts.exoforge.generique.EXT_AUDIO
   scripts.exoforge.generique.CONNUES


Functions
---------

.. autoapisummary::

   scripts.exoforge.generique.trouver_profil
   scripts.exoforge.generique.textes_tex
   scripts.exoforge.generique.preparer_latex
   scripts.exoforge.generique.instances
   scripts.exoforge.generique.slots
   scripts.exoforge.generique.slots_facultatifs
   scripts.exoforge.generique.nb_apparitions
   scripts.exoforge.generique.script_enregistrement
   scripts.exoforge.generique.medias_presents
   scripts.exoforge.generique.images
   scripts.exoforge.generique.manifeste
   scripts.exoforge.generique.verifier
   scripts.exoforge.generique.construire_generique


Module Contents
---------------

.. py:data:: RACINE

.. py:data:: MOTEUR

.. py:data:: FEUILLE

.. py:data:: MATHJAX

.. py:data:: EXT_AUDIO
   :value: ('.mp3', '.m4a', '.wav', '.ogg')


.. py:data:: CONNUES

.. py:function:: trouver_profil(nom)

   Renvoie le fichier du profil demandé (``profils/<nom>/profil.yaml``).

   ``nom`` peut être le nom, un alias ou la première lettre (si elle ne désigne qu'un profil) ;
   sans nom, c'est le profil marqué ``defaut`` (ou ``None``). Le premier trouvé l'emporte
   (local, puis privé, puis dépôt). Quitte le programme si le nom n'est pas compris.


.. py:function:: textes_tex(obj)

   Énumère toutes les chaînes de la fiche, à toute profondeur (pour vérifier les macros).


.. py:function:: preparer_latex(cfg, dossier, avert, schema=None)

   Lit les fichiers LaTeX de la fiche et renvoie ``(macros, couleurs)`` pour MathJax.

   Les fichiers de ``latex.fichiers`` sont cherchés à côté de la fiche, puis dans ``style/latex`` et
   les dossiers de profils ; leurs ``\input`` / ``\include`` sont suivis. Les macros de ``latex.macros``
   s'ajoutent ou remplacent. Une couleur mal tapée est remplacée par la plus proche.
   Les avertissements (fichier introuvable, macro inconnue…) sont ajoutés à la liste ``avert``.

   ``schema`` : jeu de couleurs LaTeX du profil (ex. ``Ecole1_ColorScheme.tex``) ; il remplace le
   ``\include{…ColorScheme}`` du préambule, pour que ``\TB``, ``\TV``… prennent les couleurs de l'établissement.


.. py:function:: instances(e)

   Renvoie les instances d'une étape sous forme de couples ``(suffixe, étape)``.

   Une seule, de suffixe vide, pour une étape simple ; suffixes ``"1"`` … ``"n"`` pour « repeter: n ».


.. py:function:: slots(cfg)

   Renvoie les emplacements audio ``(nom, étape)``, dans l'ordre de l'exercice.

   Une étape répétée donne ``bloc1``, ``bloc2``… ; la conclusion vient en dernier si elle a un audio.


.. py:function:: slots_facultatifs(cfg)

   Renvoie les noms des commentaires audio facultatifs des questions.

   Pour une étape ``choix`` : explication et retour de chaque proposition ; pour une étape
   ``numerique`` : explication (si ``solution``) et aide.


.. py:function:: nb_apparitions(e)

   Nombre d'éléments qui apparaissent avec le commentaire de l'étape.


.. py:function:: script_enregistrement(cfg, dossier, presents)

   Écrit ``script_enregistrement.md`` dans ``dossier`` et renvoie son chemin.

   Le script liste chaque emplacement audio (présent ou à enregistrer, selon ``presents``), le texte
   de chaque apparition et les commentaires facultatifs possibles.


.. py:function:: medias_presents(cfg, dossier, avert=None)

   Recense les médias déposés dans ``dossier`` et renvoie ``(audios, transcriptions, reperes)``.

   Audios : fichier unique ou segments ``_a1``, ``_a2``… ; transcriptions ``.txt`` ; repères
   ``.reperes.json``. Les noms sont reconnus sans tenir compte des majuscules. Les incohérences
   (audio manquant, nombre de segments ou de repères) sont ajoutées à ``avert``.


.. py:function:: images(cfg)

   Renvoie les chemins des images citées par la fiche (rappel, contenus des étapes et de la conclusion).


.. py:function:: manifeste(cfg, fichiers)

   Renvoie le texte du manifeste SCORM 1.2 (``imsmanifest.xml``) d'un exercice et de ses fichiers.


.. py:function:: verifier(cfg)

   Vérifie la structure de la fiche (identifiants, types d'étapes, options, renvois ``aller_a``).

   Quitte le programme avec la liste des problèmes s'il y en a.


.. py:function:: construire_generique(fiche: pathlib.Path, cfg: dict, profil=None, auteur=False, style_profil=None) -> pathlib.Path

   Construit l'exercice et renvoie le chemin du paquet SCORM.

   Écrit ``dist/exoforge/<id>/index.html``, ``imsmanifest.xml`` et les médias copiés, puis
   ``dist/exoforge/<id>_scorm12.zip`` ; met à jour le script d'enregistrement dans le dossier des
   médias. ``style_profil`` : fonction qui renvoie le bloc de style du profil (voir ``build.py``).
   Affiche un bilan et les points à vérifier.


