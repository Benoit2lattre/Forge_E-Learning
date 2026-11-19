scripts.forge.capsules
======================

.. py:module:: scripts.forge.capsules

.. autoapi-nested-parse::

   Atelier Forge — écran « Capsules » (CapsuleForge) : liste des capsules, état section par section, actions.

   Une capsule est un dossier de ``data/capsuleforge`` qui contient ``chapitre.yaml`` (lecteur actuel) ou seulement
   ``capsule.yaml`` (didacticiel enregistré pour l'ancien lecteur, à mettre à jour). L'état est lu dans le fichier ;
   les actions sont des commandes ``capsuleforge`` lancées par l'atelier (voir ``forge.Atelier.actions``).

   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.forge.capsules.ICI
   scripts.forge.capsules.DOSSIER
   scripts.forge.capsules.SORTIES
   scripts.forge.capsules.SCRIPT
   scripts.forge.capsules.REGLAGES
   scripts.forge.capsules.GENRES
   scripts.forge.capsules.LANGUES


Functions
---------

.. autoapisummary::

   scripts.forge.capsules.F
   scripts.forge.capsules.reglages
   scripts.forge.capsules.garder_reglage
   scripts.forge.capsules.dossiers_capsules
   scripts.forge.capsules.dossier
   scripts.forge.capsules.texte
   scripts.forge.capsules.liste
   scripts.forge.capsules.detail
   scripts.forge.capsules.paquets
   scripts.forge.capsules.chemins_rel
   scripts.forge.capsules.voix_disponibles
   scripts.forge.capsules.ident_section
   scripts.forge.capsules.sections_valides
   scripts.forge.capsules.langue_valide
   scripts.forge.capsules.nom_propose
   scripts.forge.capsules.argv_base


Module Contents
---------------

.. py:data:: ICI

.. py:data:: DOSSIER

.. py:data:: SORTIES

.. py:data:: SCRIPT

.. py:data:: REGLAGES

.. py:data:: GENRES

.. py:data:: LANGUES

.. py:function:: F()

.. py:function:: reglages() -> dict

.. py:function:: garder_reglage(cle: str, valeur)

.. py:function:: dossiers_capsules() -> list[pathlib.Path]

   Dossiers des capsules : data/capsuleforge, puis ceux que désignent les cours (``capsules/`` d'un cours,
   sources) ; un nom déjà vu masque les suivants (les capsules se désignent par leur nom).


.. py:function:: dossier(nom: str) -> pathlib.Path

   Dossier d'une capsule (nom exact, sans chemin) de data/capsuleforge ou d'un cours ; ``ValueError`` sinon.


.. py:function:: texte(v) -> str

.. py:function:: liste() -> list[dict]

.. py:function:: detail(nom: str) -> dict

.. py:function:: paquets(nom: str) -> list[dict]

.. py:function:: chemins_rel(f: pathlib.Path) -> str

.. py:function:: voix_disponibles() -> dict

   Voix Piper téléchargées, par langue (fr_FR-tom-medium → fr) ; voix Edge proposées par défaut.


.. py:function:: ident_section(titre: str, existants: set) -> str

.. py:function:: sections_valides(d: pathlib.Path, ids) -> list[str]

.. py:function:: langue_valide(l: str) -> str

.. py:function:: nom_propose(titre: str) -> str

   Nom de dossier libre tiré d'un titre (« Traction simple » → traction_simple).


.. py:function:: argv_base(py: str, cmd: str) -> list[str]

