scripts.capsuleforge.scenario
=============================

.. py:module:: scripts.capsuleforge.scenario

.. autoapi-nested-parse::

   CapsuleForge — scénario de lecture d'un diaporama : niveaux des dispositions, balises des notes, diagnostic.

   Voir le guide « Préparer son diaporama pour CapsuleForge » (``outils/capsuleforge/DIAPORAMA.md``).

   - **Niveaux des dispositions** (:func:`niveaux`) : une diapositive dont la disposition est déclarée ``chapitre``
     est la page de titre, ``partie`` ouvre une partie, ``section`` ouvre une section (quand le diaporama n'a pas de
     sections PowerPoint). Noms standard de PowerPoint par défaut, complétés par le profil de l'école puis par le
     chapitre (clé ``powerpoint: {dispositions: {nom: niveau}}``).
   - **Balises des notes** (:func:`lire_notes`) : ``[clic]``, ``[pause]``, ``[pause 2 s]``, ``[fin]``, ``[note] … [/note]``,
     retirées du texte dit ; délimiteurs ``[`` ``]`` par défaut (clé ``powerpoint: {balises: ["⟦", "⟧"]}``).
   - **Diagnostic** (:func:`diagnostiquer`) : degré atteint (0 brut à 5 enregistré) et ce qu'il faudrait ajouter.

   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.scenario.NIVEAUX
   scripts.capsuleforge.scenario.DISPOSITIONS
   scripts.capsuleforge.scenario.DELIMITEURS
   scripts.capsuleforge.scenario.PAUSE_MARQUEE_S
   scripts.capsuleforge.scenario.NOMS_DEGRES


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.scenario.niveaux
   scripts.capsuleforge.scenario.delimiteurs
   scripts.capsuleforge.scenario.profil_nomme
   scripts.capsuleforge.scenario.a_des_balises
   scripts.capsuleforge.scenario.lire_notes
   scripts.capsuleforge.scenario.accroches
   scripts.capsuleforge.scenario.structure
   scripts.capsuleforge.scenario.diagnostiquer
   scripts.capsuleforge.scenario.resume_diagnostic


Module Contents
---------------

.. py:data:: NIVEAUX
   :value: ('chapitre', 'partie', 'section')


.. py:data:: DISPOSITIONS

.. py:data:: DELIMITEURS
   :value: ('[', ']')


.. py:data:: PAUSE_MARQUEE_S
   :value: 1.0


.. py:data:: NOMS_DEGRES
   :value: ['brut', 'structuré', 'animé', 'commenté', 'balisé', 'enregistré']


.. py:function:: niveaux(profil: dict | None = None, chap: dict | None = None) -> dict

   Niveau de chaque disposition (nom en minuscules → ``chapitre`` | ``partie`` | ``section``).


.. py:function:: delimiteurs(profil: dict | None = None, chap: dict | None = None) -> tuple[str, str]

   Délimiteurs des balises : chapitre, sinon profil, sinon crochets.


.. py:function:: profil_nomme(nom: str | None) -> dict | None

   Contenu du profil d'école ``nom`` (``None`` s'il n'est pas donné ou introuvable).


.. py:function:: a_des_balises(texte: str, d: tuple[str, str] = DELIMITEURS) -> bool

.. py:function:: lire_notes(texte: str, d: tuple[str, str] = DELIMITEURS, debit_mm: float = 150.0) -> dict

   Lit les notes d'une diapositive et leurs balises.

   Renvoie ``{texte, phrases, clics, pauses, notes, inconnues}`` :

   - ``texte`` : le texte dit, sans balises ni notes pour l'enseignant ;
   - ``phrases`` : ses phrases (découpe de CapsuleForge) ;
   - ``clics`` : un ``(phrase, decalage_s)`` par balise ``[clic]``, dans l'ordre : la phrase où tombe la balise
     (numérotée à partir de 1) et, si elle est au milieu de la phrase, le temps estimé des mots qui précèdent ;
   - ``pauses`` : ``{phrase: secondes}``, silence après la phrase ;
   - ``fin`` : ``{phrase, decalage_s?}`` si la balise ``[fin]`` (ou ``[fin 3 s]``) fixe la fin du pas après une phrase ;
   - ``notes`` : les textes ``[note] … [/note]`` ; ``inconnues`` : les balises non reconnues.


.. py:function:: accroches(n_actions: int, lu: dict, reg_decalage: float) -> tuple[list[dict], list[str]]

   Accroche des actions (apparitions e1…eK) aux phrases ; renvoie ``([{phrase, decalage_s?}…], remarques)``.

   Avec des balises ``[clic]`` : chaque action à la place de sa balise. Sans balise : la première action à la
   première phrase, la deuxième à la deuxième, et ainsi de suite (la dernière phrase reçoit le reste).


.. py:function:: structure(fichier: pathlib.Path, niv: dict) -> dict

   Structure lue : sections PowerPoint, niveau de chaque diapositive d'après sa disposition.


.. py:function:: diagnostiquer(fichier: pathlib.Path, profil: dict | None = None, chap: dict | None = None, lu: dict | None = None) -> dict

   Degré du diaporama et conseils pour monter d'un degré.

   Renvoie ``{degre, nom, criteres: {structure, animations, notes, balises, enregistrement}, details, conseils}``.


.. py:function:: resume_diagnostic(diag: dict) -> list[str]

   Lignes du diagnostic, pour le journal.


