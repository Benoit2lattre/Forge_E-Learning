scripts.forge.cours
===================

.. py:module:: scripts.forge.cours

.. autoapi-nested-parse::

   Cours, déclinaisons et éditions de Forge (fichier ``cours.yaml``, format ``forge-cours/1``).

   Un **cours** décrit un contenu stable (description, objectifs, compétences, documents, sources) ; une
   **déclinaison** est ce cours dans une école (campus, parcours, niveau, codes, langue, Moodle) ; une **édition** est
   une année de cette déclinaison (promo, groupes et leur campus, séances datées). Un cours désigne ses dossiers et
   fichiers (sources) sans les déplacer ; un cours nouveau reçoit une arborescence standard sous ``data/cours/<nom>/``.

   L'atelier s'en sert pour son sélecteur « Cours » et pour trier ses listes ; la ligne de commande donne la même vue :

       python scripts/forge/cours.py liste
       python scripts/forge/cours.py montrer mef
       python scripts/forge/cours.py verifier [mef]
       python scripts/forge/cours.py proposer mef          # sources trouvées dans data/ pour un nom court



Attributes
----------

.. autoapisummary::

   scripts.forge.cours.FORMAT
   scripts.forge.cours.FICHIER
   scripts.forge.cours.RACINES
   scripts.forge.cours.TYPES
   scripts.forge.cours.DOCUMENTS
   scripts.forge.cours.STANDARD
   scripts.forge.cours.NOM
   scripts.forge.cours.LIMITE_CHEMIN
   scripts.forge.cours.EN_TETE
   scripts.forge.cours.CODES
   scripts.forge.cours.ANCIENS_CODES


Classes
-------

.. autoapisummary::

   scripts.forge.cours.Index


Functions
---------

.. autoapisummary::

   scripts.forge.cours.rel
   scripts.forge.cours.absolu
   scripts.forge.cours.fichiers
   scripts.forge.cours.lire
   scripts.forge.cours.ecrire
   scripts.forge.cours.tous
   scripts.forge.cours.trouver
   scripts.forge.cours.dossier_cours
   scripts.forge.cours.declinaison
   scripts.forge.cours.edition
   scripts.forge.cours.libelle
   scripts.forge.cours.choix_possibles
   scripts.forge.cours.nom_valide
   scripts.forge.cours.texte_valide
   scripts.forge.cours.motifs
   scripts.forge.cours.correspond
   scripts.forge.cours.filtrer
   scripts.forge.cours.proposer
   scripts.forge.cours.creer
   scripts.forge.cours.longueur
   scripts.forge.cours.langues_declinaison
   scripts.forge.cours.ajouter_declinaison
   scripts.forge.cours.modifier_declinaison
   scripts.forge.cours.supprimer_declinaison
   scripts.forge.cours.modifier_edition
   scripts.forge.cours.ajouter_edition
   scripts.forge.cours.en_cours
   scripts.forge.cours.ajouter_source
   scripts.forge.cours.retirer_source
   scripts.forge.cours.verifier
   scripts.forge.cours.main


Module Contents
---------------

.. py:data:: FORMAT
   :value: 'forge-cours/1'


.. py:data:: FICHIER
   :value: 'cours.yaml'


.. py:data:: RACINES

.. py:data:: TYPES

.. py:data:: DOCUMENTS

.. py:data:: STANDARD

.. py:data:: NOM

.. py:data:: LIMITE_CHEMIN
   :value: 200


.. py:data:: EN_TETE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """# Cours Forge (format forge-cours/1) : écrit par l'Atelier Forge ; modifiable à la main.
      # Chemins relatifs à la racine du dépôt. Mode d'emploi : outils/atelier/README.md (Cours).
      """

   .. raw:: html

      </details>



.. py:function:: rel(p: pathlib.Path) -> str

.. py:function:: absolu(chemin: str) -> pathlib.Path

.. py:function:: fichiers() -> list[pathlib.Path]

   Fichiers ``cours.yaml`` de data/cours puis de donnees/cours (un nom déjà vu dans data/ masque la démo).


.. py:data:: CODES
   :value: ('enseignement', 'bloc')


.. py:data:: ANCIENS_CODES

.. py:function:: lire(f: pathlib.Path) -> dict

.. py:function:: ecrire(c: dict) -> pathlib.Path

.. py:function:: tous() -> dict[str, dict]

.. py:function:: trouver(nom: str) -> dict

.. py:function:: dossier_cours(c: dict) -> pathlib.Path

.. py:function:: declinaison(c: dict, nom: str) -> dict

.. py:function:: edition(c: dict, decl: str, ed: str) -> dict

.. py:function:: libelle(c: dict, decl: str | None = None, ed: str | None = None) -> str

.. py:function:: choix_possibles() -> list[dict]

   Ce que propose le sélecteur : chaque cours, et chaque édition de chacune de ses déclinaisons.


.. py:function:: nom_valide(nom: str, quoi: str = 'nom court') -> str

.. py:function:: texte_valide(v, maxi: int = 200, lignes: bool = False) -> str

.. py:function:: motifs(c: dict, cours_par_nom: dict | None = None, deja: set | None = None) -> list[str]

   Chemins et motifs (``*``) désignés par un cours, ses déclinaisons et les cours qu'il inclut, plus son dossier.


.. py:function:: correspond(chemin, motif: str) -> bool

   Vrai si ``chemin`` est le motif, est dedans, ou s'il correspond au motif (``*`` sur un nom).


.. py:class:: Index

   Appartenance des objets aux cours, calculée une fois par requête.


   .. py:attribute:: cours


   .. py:attribute:: motifs


   .. py:method:: de(chemin) -> list[str]


   .. py:method:: dossiers(type_: str) -> list[pathlib.Path]

      Dossiers où chercher les objets d'un type (sources désignées et dossiers standard des cours).



.. py:function:: filtrer(objets: list[dict], cle: str, choix: dict | None, index: Index | None = None, chemin=None) -> list[dict]

   Ajoute à chaque objet la liste ``dans_cours`` de ses cours, puis garde ceux du choix (cours, « sans » ou tous).


.. py:function:: proposer(nom: str) -> list[dict]

   Sources de ``data/`` dont le nom contient le nom court (dossiers, classeurs, fiches, capsules, diaporamas).


.. py:function:: creer(nom: str, titre: str, domaine: str = '', langues=None, sources: list[dict] | None = None, standard: bool = False, base: pathlib.Path | None = None) -> tuple[dict, list[str]]

   Crée un cours : à partir de sources existantes (désignées) et/ou avec l'arborescence standard.

   Renvoie le cours et les avertissements (chemins trop longs).


.. py:function:: longueur(p: pathlib.Path) -> list[str]

.. py:function:: langues_declinaison(d: dict) -> list[str]

   Langues d'une déclinaison (``langues``, ou l'ancien ``langue`` seul).


.. py:function:: ajouter_declinaison(c: dict, d: dict) -> dict

.. py:function:: modifier_declinaison(c: dict, nom: str, d: dict) -> dict

   Change école, campus, parcours, niveau, codes et langues ; le nom court (nom des dossiers) reste.


.. py:function:: supprimer_declinaison(c: dict, nom: str)

.. py:function:: modifier_edition(c: dict, decl: str, ed: str, e: dict) -> dict

.. py:function:: ajouter_edition(c: dict, decl: str, e: dict) -> dict

   Nouvelle édition d'une déclinaison : copie de la précédente (séances décalées d'un an), puis les champs donnés.


.. py:function:: en_cours(d: dict) -> str | None

   Édition en cours d'une déclinaison (chacune la sienne : deux parcours peuvent avoir lieu en même temps).


.. py:function:: ajouter_source(c: dict, type_: str, chemin: str) -> str

.. py:function:: retirer_source(c: dict, type_: str, chemin: str)

.. py:function:: verifier(c: dict, cours_par_nom: dict | None = None) -> list[str]

   Remarques sur un cours : format, sources introuvables, noms en double, choix actif, chemins trop longs.


.. py:function:: main(argv=None) -> int

