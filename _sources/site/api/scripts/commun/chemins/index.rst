scripts.commun.chemins
======================

.. py:module:: scripts.commun.chemins

.. autoapi-nested-parse::

   Forge E-Learning — chemins communs à tous les outils (un seul endroit à modifier si l'arborescence change).

   Chaque script ajoute scripts/commun au chemin d'import puis fait ``import chemins``.



Attributes
----------

.. autoapisummary::

   scripts.commun.chemins.RACINE
   scripts.commun.chemins.SCRIPTS
   scripts.commun.chemins.OUTILS
   scripts.commun.chemins.PROFILS
   scripts.commun.chemins.STYLE
   scripts.commun.chemins.LATEX
   scripts.commun.chemins.STATIC
   scripts.commun.chemins.DONNEES
   scripts.commun.chemins.DATA
   scripts.commun.chemins.SORTIES


Functions
---------

.. autoapisummary::

   scripts.commun.chemins.dossiers_profils
   scripts.commun.chemins.nom_profil
   scripts.commun.chemins.fichiers_profils
   scripts.commun.chemins.dossiers_latex
   scripts.commun.chemins.media_exoforge
   scripts.commun.chemins.fichier_exoforge


Module Contents
---------------

.. py:data:: RACINE

.. py:data:: SCRIPTS

.. py:data:: OUTILS

.. py:data:: PROFILS

.. py:data:: STYLE

.. py:data:: LATEX

.. py:data:: STATIC

.. py:data:: DONNEES

.. py:data:: DATA

.. py:data:: SORTIES

.. py:function:: dossiers_profils()

   Renvoie les dossiers où chercher les profils, dans l'ordre de priorité.

   Un dossier ``profils/`` du répertoire courant (profil local), puis ``data/profils``
   (profils privés, non publiés), puis ``profils/`` du dépôt ; seuls les dossiers existants
   sont gardés, sans doublon.


.. py:function:: nom_profil(f: pathlib.Path) -> str

   Renvoie le nom d'un profil à partir de son fichier.

   C'est le nom de son dossier (``profils/Ecole1/profil.yaml`` → ``Ecole1``),
   ou celui du fichier pour un profil isolé (``profils/Ecole1.yaml``).


.. py:function:: fichiers_profils(dossier: pathlib.Path | None = None)

   Renvoie la liste des fichiers de profil.

   Un profil est ``<dossier>/<nom>/profil.yaml`` (un dossier par profil, avec son jeu de couleurs)
   ou ``<dossier>/<nom>.yaml`` (ancienne forme). Sans ``dossier`` : tous les dossiers de
   :func:`dossiers_profils`, dans l'ordre.


.. py:function:: dossiers_latex()

   Renvoie les dossiers où chercher un fichier LaTeX nommé sans chemin valide.

   D'abord le style commun (``style/latex``), puis les dossiers des profils.


.. py:function:: media_exoforge(dossier_fiche: pathlib.Path, ident: str) -> pathlib.Path

   Renvoie le dossier des médias d'un exercice ExoForge.

   D'abord ``data/exoforge/media/<id>`` s'il existe (privé : enregistrements de l'auteur),
   sinon ``media/<id>`` à côté de la fiche (exemples publiés, sans audio tant qu'ils ne sont pas prêts).


.. py:function:: fichier_exoforge(dossier_fiche: pathlib.Path, rel: str) -> pathlib.Path

   Renvoie le chemin d'un fichier cité par une fiche (image ``media/<id>/…``).

   Le fichier est cherché d'abord sous ``data/exoforge``, sinon à côté de la fiche.


