scripts.capsuleforge.assemblage
===============================

.. py:module:: scripts.capsuleforge.assemblage

.. autoapi-nested-parse::

   CapsuleForge — du journal d'enregistrement au fichier source de la capsule (capsule.yaml).

   Partie sans dépendance à Windows : elle se teste partout. L'enregistreur (``enregistreur.py``) écrit
   un journal JSON Lines (un événement par ligne) et les images ; ce module en fait les pas, les
   regroupe en étapes (Ctrl+Maj+E pendant l'enregistrement) et rédige les bulles.

   Format du fichier source : voir ``outils/capsuleforge/README.md`` (section « Le fichier capsule.yaml »).
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.assemblage.FORMAT
   scripts.capsuleforge.assemblage.TYPES_CONTROLE
   scripts.capsuleforge.assemblage.VERBES
   scripts.capsuleforge.assemblage.NOMS_VIDES
   scripts.capsuleforge.assemblage.CONTENEURS
   scripts.capsuleforge.assemblage.CLASSES_SYSTEME
   scripts.capsuleforge.assemblage.PROCESSUS_SYSTEME
   scripts.capsuleforge.assemblage.ENTETE_YAML
   scripts.capsuleforge.assemblage.ACTIONS


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.assemblage.type_court
   scripts.capsuleforge.assemblage.bulle_auto
   scripts.capsuleforge.assemblage.simplifier_trajet
   scripts.capsuleforge.assemblage.cadre_par_defaut
   scripts.capsuleforge.assemblage.cadre_valide
   scripts.capsuleforge.assemblage.lire_journal
   scripts.capsuleforge.assemblage.appliquer_modifs
   scripts.capsuleforge.assemblage.assembler
   scripts.capsuleforge.assemblage.construire_pas
   scripts.capsuleforge.assemblage.nettoyer_nom
   scripts.capsuleforge.assemblage.nettoyer_cible
   scripts.capsuleforge.assemblage.hors_application
   scripts.capsuleforge.assemblage.ecrire_yaml
   scripts.capsuleforge.assemblage.lire_yaml
   scripts.capsuleforge.assemblage.verifier


Module Contents
---------------

.. py:data:: FORMAT
   :value: 'capsuleforge/1'


.. py:data:: TYPES_CONTROLE

.. py:data:: VERBES

.. py:data:: NOMS_VIDES

.. py:function:: type_court(t: str | None) -> str

   Renvoie le type de contrôle sans le suffixe « Control » (``ButtonControl`` -> ``Button``).


.. py:function:: bulle_auto(action: str, cible: dict | None, texte: str | None = None, touches: str | None = None) -> str

   Renvoie le texte de bulle proposé à partir de l'action et de la cible.

   Le texte est en Markdown (nom du contrôle en gras) ; l'auteur le réécrit dans le YAML au besoin.


.. py:function:: simplifier_trajet(points: list[list[float]], tolerance: float = 6.0, max_points: int = 40) -> list[list[int]]

   Allège un trajet de souris par l'algorithme de Ramer-Douglas-Peucker sur (x, y).

   ``points`` est une liste de ``[x, y, t_ms]`` ; le temps de chaque point retenu est gardé. La tolérance est
   augmentée tant qu'il reste plus de ``max_points`` points. Renvoie une liste allégée d'entiers.


.. py:function:: cadre_par_defaut(point, ecran, l=120, h=48)

   Renvoie une zone de clic de secours ``[x, y, l, h]`` centrée sur le clic, gardée dans l'écran.

   Sert quand l'accessibilité n'a pas donné de cadre.


.. py:function:: cadre_valide(cadre, point, ecran, max_part=0.6) -> bool

   Indique si un cadre d'accessibilité est utile : il contient le clic et ne couvre pas tout l'écran.

   ActivePresenter garde parfois le bureau entier (zone 2560 × 1600 pour « Bureau »). Le cadre est refusé si
   son aire dépasse ``max_part`` au carré de celle de l'écran.


.. py:function:: lire_journal(chemin: pathlib.Path) -> list[dict]

   Lit un journal JSON Lines et renvoie la liste des événements ; les lignes illisibles sont ignorées.


.. py:function:: appliquer_modifs(evts: list[dict]) -> list[dict]

   Applique les événements « modif » aux pas du journal et renvoie les événements sans eux.

   Ces événements complètent un pas après coup (double-clic reconnu, cible lue plus tard).


.. py:function:: assembler(evts: list[dict], titre: str | None = None) -> dict

   Construit le dictionnaire de la capsule (prêt à écrire en YAML) à partir des événements du journal.

   Les pas sont regroupés en étapes, ceux faits dans un autre programme que le principal sont signalés
   (``autre_programme``), et une saisie sans cible reprend celle du clic qui l'a précédée au même endroit.

   Événements reconnus (champ ``e``) : ::

     debut   {ecran:{largeur,hauteur,echelle}, application?, date}
     pas     {id, action, image, point, trajet, cible?, texte?, touches?, t, crans?, arrivee?}
     etape   {t, titre?}         raccourci « nouvelle étape » : une nouvelle étape commence au pas suivant
     fin     {t, image?}


.. py:function:: construire_pas(e: dict, ecran: dict, t_prec) -> dict

   Construit un pas de la capsule à partir d'un événement « pas » du journal.

   Nettoie la cible, propose la bulle, simplifie le trajet et calcule ``duree_ms`` depuis l'instant ``t_prec``
   du pas précédent ; un pas hors de l'application enregistrée est marqué ``ignorer`` avec sa ``raison``.


.. py:data:: CONTENEURS

.. py:data:: CLASSES_SYSTEME

.. py:data:: PROCESSUS_SYSTEME

.. py:function:: nettoyer_nom(nom: str | None) -> str

   Renvoie le nom d'un contrôle sans espaces insécables ni deux-points finaux.


.. py:function:: nettoyer_cible(cible: dict, point, ecran, action: str = 'clic') -> dict

   Renvoie une cible utilisable à partir de celle lue par l'accessibilité.

   Le nom est nettoyé, les conteneurs et les cadres douteux sont écartés ; à défaut de cadre, une zone de
   secours est centrée sur le clic.


.. py:function:: hors_application(action, point, cible: dict, ecran: dict, touches=None) -> str | None

   Renvoie la raison d'écarter un pas étranger à la manipulation (barre des tâches, raccourci Windows…), ou ``None``.


.. py:data:: ENTETE_YAML
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """# CapsuleForge — fichier source de la capsule (format {fmt}).
      # À modifier à la main : titres et narration des étapes, bulles, regroupement des pas.
      # Pour fusionner deux étapes, supprimer les lignes titre/narration/arret/pas de la seconde.
      # Coordonnées en pixels de l'écran enregistré ; cadre = [x, y, largeur, hauteur].
      # Mode d'emploi : outils/capsuleforge/README.md
      """

   .. raw:: html

      </details>



.. py:function:: ecrire_yaml(cap: dict, chemin: pathlib.Path) -> None

   Écrit la capsule dans ``chemin`` en YAML lisible, précédée d'un en-tête de commentaires.


.. py:function:: lire_yaml(chemin: pathlib.Path) -> dict

   Lit un fichier YAML et renvoie son contenu (dictionnaire vide si le fichier est vide).


.. py:data:: ACTIONS

.. py:function:: verifier(cap: dict, dossier: pathlib.Path) -> tuple[list[str], list[str]]

   Contrôle une capsule et renvoie le couple (erreurs bloquantes, avertissements).

   ``dossier`` est celui de la capsule : les images et sons y sont cherchés.


