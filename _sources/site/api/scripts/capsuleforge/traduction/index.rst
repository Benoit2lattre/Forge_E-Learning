scripts.capsuleforge.traduction
===============================

.. py:module:: scripts.capsuleforge.traduction

.. autoapi-nested-parse::

   CapsuleForge — traduction d'un chapitre (format 2), en deux temps, quel que soit le moteur.

   1. ``capsuleforge traduire <chapitre> --langue en [--moteur aucun|argos|deepl]``
      écrit ou complète ``<chapitre>/traductions/<langue>.yaml`` : un élément par texte à traduire (clé, source, cible,
      relu). Le moteur pré-remplit les cibles vides ; « aucun » les laisse vides (traduction à la main, par un
      collègue ou par un assistant d'IA). Une cible déjà écrite n'est jamais remplacée.
   2. ``capsuleforge traduire <chapitre> --langue en --importer``
      recopie les cibles dans ``chapitre.yaml`` : le texte devient ``{fr: …, en: …}``. Une cible dont la source a changé
      depuis (phrase corrigée dans la relecture) est signalée et laissée de côté.

   Textes traduits : titre du chapitre, titres des parties, titre / objectif / ouverture des sections, phrases dites
   (sous-titres et voix de synthèse), narration d'un pas sans phrases, texte des bulles et textes posés sur l'image ;
   textes des questions QuizForge posées en fin de section (énoncé, options, rétroactions, indices, unité) et textes
   affichés des exercices ExoForge du chapitre. Ces deux dernières traductions restent dans ``traductions/<langue>.yaml``
   (la banque et la fiche ne sont pas modifiées) et sont prises à la construction du lecteur ; « importer » ne les
   recopie pas dans ``chapitre.yaml``.
   Moteurs : « aucun » (gratuit), « argos » (Argos Translate, gratuit, hors ligne : ``pip install argostranslate``, modèle
   téléchargé à la première utilisation), « deepl » (API DeepL ; clé dans la variable ``DEEPL_AUTH_KEY`` ; l'offre
   « API Free » a un quota gratuit).
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.traduction.MOTEURS


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.traduction.elements
   scripts.capsuleforge.traduction.elements_questions
   scripts.capsuleforge.traduction.elements_exercices
   scripts.capsuleforge.traduction.preparer
   scripts.capsuleforge.traduction.importer
   scripts.capsuleforge.traduction.relire_traduction


Module Contents
---------------

.. py:data:: MOTEURS
   :value: ('aucun', 'argos', 'deepl')


.. py:function:: elements(chap: dict)

   Produit le triplet ``(clé, objet parent, champ)`` de chaque texte traduisible du chapitre, dans l'ordre du fichier.


.. py:function:: elements_questions(chap: dict, dossier: pathlib.Path)

   Produit ``(clé, texte, contexte)`` pour chaque texte des questions QuizForge posées par le chapitre.

   Clés ``question/<banque>/<titre>/<chemin>`` ; une question posée par plusieurs sections n'apparaît qu'une fois.
   La banque n'est pas modifiée : la traduction reste dans le fichier du chapitre et sert à la construction.


.. py:function:: elements_exercices(chap: dict, dossier: pathlib.Path)

   Produit ``(clé, texte, contexte)`` pour chaque texte affiché des fiches ExoForge appelées par le chapitre.

   Clés ``exercice/<id>/<chemin>`` (chemins de :func:`construire_chapitre.textes_fiche`). La fiche n'est pas modifiée :
   à la construction, une page traduite de l'exercice est produite à côté de l'originale.


.. py:function:: preparer(yaml_chap: pathlib.Path, langue: str, moteur: str = 'aucun', journal=print) -> pathlib.Path

   Écrit ou complète ``traductions/<langue>.yaml`` et renvoie son chemin.

   Les cibles existantes sont gardées (retrouvées par clé, ou par texte source si la phrase a été découpée) ;
   le moteur ne remplit que les cibles vides. L'ancien fichier est d'abord copié en ``.yaml.bak`` horodaté.


.. py:function:: importer(yaml_chap: pathlib.Path, langue: str, journal=print) -> int

   Recopie les cibles de ``traductions/<langue>.yaml`` dans ``chapitre.yaml`` et renvoie le nombre de textes posés.

   Une cible dont la source a changé depuis la traduction est signalée et laissée de côté. Si un texte est posé,
   le chapitre est sauvegardé dans ``sauvegardes/`` et la langue ajoutée à ``langues.autres``.


.. py:function:: relire_traduction(yaml_chap: pathlib.Path, langue: str, port: int = 8776, navigateur: bool = True)

   Prépare (ou met à jour) ``traductions/<langue>.yaml`` puis ouvre l'écran de relecture des traductions.

   Le serveur local tourne jusqu'à la fermeture de la page (ou Ctrl+C).


