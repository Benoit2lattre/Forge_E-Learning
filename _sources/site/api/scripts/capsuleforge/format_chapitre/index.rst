scripts.capsuleforge.format_chapitre
====================================

.. py:module:: scripts.capsuleforge.format_chapitre

.. autoapi-nested-parse::

   CapsuleForge — format capsuleforge/2 : le chapitre (cours interactif ou didacticiel).

   Quatre niveaux : Chapitre > Partie (tronc, annexe, exercice) > Section (5 à 6 min au plus ; l'« étape » d'un
   didacticiel) > Pas (une scène : fond, vue, objets, gestes attendus, retours).
   Spécification complète : ``outils/capsuleforge/FORMAT.md``.

   Ce module ne dépend que de PyYAML : conversion d'une capsule au format 1, noms dynamiques (B-S2-P4),
   déroulé d'un parcours, vérification, écriture.
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.format_chapitre.FORMAT
   scripts.capsuleforge.format_chapitre.FICHIER
   scripts.capsuleforge.format_chapitre.TYPES_PARTIE
   scripts.capsuleforge.format_chapitre.PLACES
   scripts.capsuleforge.format_chapitre.TYPES_GESTE
   scripts.capsuleforge.format_chapitre.TYPES_OBJET
   scripts.capsuleforge.format_chapitre.MODES
   scripts.capsuleforge.format_chapitre.ANNEXES
   scripts.capsuleforge.format_chapitre.QUESTIONS
   scripts.capsuleforge.format_chapitre.MOTS_PAR_MINUTE
   scripts.capsuleforge.format_chapitre.DUREE_MAX_SECTION_S
   scripts.capsuleforge.format_chapitre.ORDRE_CHAPITRE
   scripts.capsuleforge.format_chapitre.ORDRE_PARTIE
   scripts.capsuleforge.format_chapitre.ORDRE_SECTION
   scripts.capsuleforge.format_chapitre.ORDRE_PAS
   scripts.capsuleforge.format_chapitre.ORDRE_GESTE
   scripts.capsuleforge.format_chapitre.ORDRE_OBJET
   scripts.capsuleforge.format_chapitre.FIN_DE_PHRASE
   scripts.capsuleforge.format_chapitre.ENTETE
   scripts.capsuleforge.format_chapitre.ENTETE_CONVERSION


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.format_chapitre.ordonner
   scripts.capsuleforge.format_chapitre.texte
   scripts.capsuleforge.format_chapitre.decouper_phrases
   scripts.capsuleforge.format_chapitre.narration_pas
   scripts.capsuleforge.format_chapitre.convertir_v1
   scripts.capsuleforge.format_chapitre.lettre
   scripts.capsuleforge.format_chapitre.noms
   scripts.capsuleforge.format_chapitre.duree_pas_s
   scripts.capsuleforge.format_chapitre.duree_section_s
   scripts.capsuleforge.format_chapitre.derouler
   scripts.capsuleforge.format_chapitre.plan
   scripts.capsuleforge.format_chapitre.minsec
   scripts.capsuleforge.format_chapitre.verifier
   scripts.capsuleforge.format_chapitre.ecrire
   scripts.capsuleforge.format_chapitre.lire


Module Contents
---------------

.. py:data:: FORMAT
   :value: 'capsuleforge/2'


.. py:data:: FICHIER
   :value: 'chapitre.yaml'


.. py:data:: TYPES_PARTIE
   :value: ('tronc', 'annexe', 'exercice')


.. py:data:: PLACES
   :value: ('debut', 'libre', 'fin')


.. py:data:: TYPES_GESTE
   :value: ('clic', 'double_clic', 'clic_droit', 'clic_milieu', 'glisser', 'molette', 'saisie', 'touche')


.. py:data:: TYPES_OBJET
   :value: ('bulle', 'texte', 'formule', 'cadre', 'spot', 'fleche', 'pointeur', 'image', 'video', 'bouton',...


.. py:data:: MODES
   :value: ('regarder', 'a_vous')


.. py:data:: ANNEXES
   :value: ('aucune', 'a_la_demande', 'integrees')


.. py:data:: QUESTIONS
   :value: ('aucune', 'proposees', 'obligatoires')


.. py:data:: MOTS_PAR_MINUTE
   :value: 150


.. py:data:: DUREE_MAX_SECTION_S
   :value: 360


.. py:data:: ORDRE_CHAPITRE
   :value: ['format', 'titre', 'langues', 'ecran', 'vue', 'source', 'reglages', 'masques', 'parcours',...


.. py:data:: ORDRE_PARTIE
   :value: ['id', 'titre', 'type', 'place', 'prerequis', 'parcours', 'variantes', 'exercice', 'sections']


.. py:data:: ORDRE_SECTION
   :value: ['id', 'titre', 'objectif', 'source', 'narration', 'audio', 'arret', 'ouverture', 'questions',...


.. py:data:: ORDRE_PAS
   :value: ['ecarte', 'raison', 'id', 'fond', 'video', 'camera', 'vue', 'source', 'narration', 'phrases',...


.. py:data:: ORDRE_GESTE
   :value: ['type', 'zone', 'point', 'arrivee', 'crans', 'texte', 'accepte', 'tolerance', 'touches',...


.. py:data:: ORDRE_OBJET
   :value: ['id', 'type', 'forme', 'texte', 'position', 'cadre', 'ouvre', 'trajet', 'fichier', 'couleur',...


.. py:function:: ordonner(d: dict, ordre: list[str]) -> dict

   Renvoie une copie de ``d`` dont les clés suivent ``ordre`` (les autres clés à la suite).


.. py:function:: texte(valeur, langue: str | None = None) -> str

   Renvoie un texte dans la langue demandée.

   Un texte est une chaîne (langue source) ou un dictionnaire par langue ``{fr: …, en: …}`` ; si la langue
   manque, la première valeur non vide est renvoyée.


.. py:data:: FIN_DE_PHRASE

.. py:function:: decouper_phrases(texte: str) -> list[str]

   Découpe un texte en phrases : seule règle de CapsuleForge (relecture, transcription, voix de synthèse).

   Coupure après « . ! ? … » suivis d'un espace puis d'une majuscule ou d'un guillemet ; un chiffre ne commence
   pas une phrase (« fig. 2 », « p. 12 » restent entiers). Les espaces sont normalisés ; le gras ``**…**`` est
   gardé (il est affiché, pas prononcé : la voix de synthèse le retire au moment de dire la phrase).


.. py:function:: narration_pas(pas: dict, langue: str | None = None) -> str

   Renvoie le texte dit pendant un pas : ses phrases horodatées mises bout à bout, sinon son champ ``narration``.


.. py:function:: convertir_v1(cap: dict, nom_fichier: str = 'capsule.yaml') -> dict

   Convertit une capsule au format 1 (étapes, pas à action unique) en chapitre au format 2, sans perte.

   Une seule partie « tronc » ; chaque étape devient une section ; chaque pas devient une scène :
   la bulle devient un objet, l'action devient le premier geste attendu, les variantes (``ou``) les suivants.


.. py:function:: lettre(i: int) -> str

   Renvoie la lettre de rang ``i`` (compté à partir de 0) : 0 → A, 25 → Z, 26 → AA.


.. py:function:: noms(chap: dict) -> dict

   Renvoie les noms dynamiques : partie « B », section « B-S2 », pas « B-S2-P4 ».

   Un pas écarté prend une décimale (B-S2-P4.1). Clés du dictionnaire : ``("partie", id)``,
   ``("section", id partie, id section)``, ``("pas", id du pas)``.


.. py:function:: duree_pas_s(p: dict, depuis, largeur: float) -> tuple[float, list | None]

   Renvoie la durée d'un pas en mode « regarder » et la position du curseur à la sortie.

   Même calcul que le lecteur (``tempsPas``) : déplacement de 0,45 à 1,5 s selon la distance, geste,
   lecture de la bulle de 1,8 à 5 s. ``depuis`` : position du curseur à l'entrée (ou ``None``).


.. py:function:: duree_section_s(sec: dict, langue: str | None = None, largeur: float = 1920) -> float | None

   Renvoie la durée estimée d'une section en secondes (``None`` si rien ne l'indique).

   C'est celle de la source si elle est connue (diaporama minuté) ; sinon la plus longue de la narration
   (150 mots/min, section et pas) et de la somme des pas.


.. py:function:: derouler(chap: dict, parcours: str | None = None, variante: str | None = None) -> dict

   Renvoie ce qu'un étudiant voit sur un parcours.

   Le tronc est rangé dans l'ordre (début, parties libres, fin), les annexes suivent le réglage du parcours.
   Renvoie ``{"tronc": [parties], "annexes": [parties appelables], "regles": parcours}``.


.. py:function:: plan(chap: dict, parcours: str | None = None, variante: str | None = None) -> list[str]

   Renvoie les lignes du plan lisible d'un parcours, avec noms et durées (commande « capsuleforge plan »).


.. py:function:: minsec(s: float | None) -> str

   Écrit une durée en minutes et secondes (« durée inconnue » si elle est nulle ou absente).


.. py:function:: verifier(chap: dict, dossier: pathlib.Path) -> tuple[list[str], list[str]]

   Vérifie un chapitre au format 2 et renvoie ``(erreurs bloquantes, avertissements)``.

   ``dossier`` : dossier du chapitre, où sont cherchés les fichiers cités (fonds, sons, vidéos).


.. py:data:: ENTETE
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """# CapsuleForge — chapitre (format {fmt}).
      # Chapitre > Partie > Section (5 à 6 min au plus) > Pas (une scène : fond, objets, gestes, retours).
      # Coordonnées en pixels de l'écran enregistré ; zone et cadre = [x, y, largeur, hauteur].
      # Description du format : outils/capsuleforge/FORMAT.md
      """

   .. raw:: html

      </details>



.. py:data:: ENTETE_CONVERSION
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """# Fichier produit par « capsuleforge convertir » à partir de {src} : tant que l'éditeur lit {src},
      # c'est {src} qui fait foi et ce fichier se refait par la même commande.
      """

   .. raw:: html

      </details>



.. py:function:: ecrire(chap: dict, chemin: pathlib.Path) -> None

   Écrit le chapitre en YAML dans ``chemin``, précédé d'un en-tête de commentaires.


.. py:function:: lire(chemin: pathlib.Path) -> dict

   Lit un chapitre YAML et le renvoie (dictionnaire vide si le fichier est vide).


