scripts.exoforge.build
======================

.. py:module:: scripts.exoforge.build

.. autoapi-nested-parse::

   ExoForge — construit un exercice interactif à partir d'une fiche YAML.

   Usage :
       python build.py exercices/<fiche>.yaml [--profil Ecole1] [--cours traction:ecole1-meca] [--auteur]
       (l'extension .yaml peut être omise)

   --cours : profil de l'école de l'édition (cours[:déclinaison[/édition]]), si --profil n'est pas donné.

   --profil (-p) : applique la charte (couleurs, police, jeu de couleurs LaTeX) de profils/<nom>/profil.yaml
                   (nom, alias ou première lettre) ; sinon le profil de la fiche, ou le profil par défaut.

   --auteur (-a) : affiche les outils auteur (emplacements audio, relevé des temps d'apparition, données tirées).

   La fiche décrit des étapes (info, choix, numerique), l'encadré permanent (rappel), les données
   tirées et calculées, les audios ; generique.py la vérifie et la construit.

   Produit dans dist/exoforge/<id>/ :

       index.html            l'exercice autonome (s'ouvre dans un navigateur)
       imsmanifest.xml       manifeste SCORM 1.2

   et dist/exoforge/<id>_scorm12.zip, prêt à déposer dans Moodle (activité SCORM).



Attributes
----------

.. autoapisummary::

   scripts.exoforge.build.RACINE


Functions
---------

.. autoapisummary::

   scripts.exoforge.build.style_profil
   scripts.exoforge.build.construire
   scripts.exoforge.build.ranger_version


Module Contents
---------------

.. py:data:: RACINE

.. py:function:: style_profil(nom) -> str

   Renvoie un bloc ``<style>`` qui remplace les couleurs et la police du moteur par celles du profil.

   ``nom`` : fichier du profil, ou nom / alias / première lettre (même tolérance que QuizForge).
   Les rôles de couleur de la charte deviennent des variables CSS (``principal_clair`` → ``--principal-clair``).


.. py:function:: construire(fiche: pathlib.Path, profil: str | None = None, auteur: bool = False) -> pathlib.Path

   Construit l'exercice décrit par la fiche YAML ``fiche`` et renvoie le chemin du paquet SCORM.

   ``profil`` : nom du profil à appliquer (sinon celui de la fiche) ; ``auteur`` : active le mode auteur.
   Quitte le programme si la fiche ne contient pas ``etapes``. Le travail est délégué à
   :func:`generique.construire_generique`.


.. py:function:: ranger_version(fiche: pathlib.Path, paquet: pathlib.Path, profil, cours: dict)

   Avec --cours : copie le paquet SCORM dans l'édition comme une version (``exercices/<id>/v2/<id>_v2_scorm12.zip``),
   inscrite au registre ; une construction identique (même fiche, mêmes médias, même profil) n'en crée pas.


