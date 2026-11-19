scripts.commun.verifier_depot
=============================

.. py:module:: scripts.commun.verifier_depot

.. autoapi-nested-parse::

   Forge E-Learning — contrôle du dépôt avant commit.

   Usage ::

       python scripts/commun/verifier_depot.py           # fichiers qui partiraient en ligne (suivis + nouveaux non ignorés)
       python scripts/commun/verifier_depot.py --index   # fichiers préparés pour le prochain commit (utilisé par .githooks/pre-commit)

   Refuse :

   - tout fichier sous un dossier local (``data/``, ``_legacy/``, ``_brouillons/``, ``_pilotage/``, ``.venv/``…, voir ``LOCAUX``) ;
   - tout fichier de plus de 5 Mo ;
   - les types lourds ou personnels (``.pptx``, ``.mp4``, ``.mov``, ``.aup3``, ``.approj``, ``.wav``, ``.m4a``) ;
   - toute adresse de courriel qui n'est pas fictive (domaines autorisés dans ``DOMAINES_FICTIFS``).

   Code de sortie 1 s'il y a un problème : le commit est alors annulé.



Attributes
----------

.. autoapisummary::

   scripts.commun.verifier_depot.RACINE
   scripts.commun.verifier_depot.LOCAUX
   scripts.commun.verifier_depot.TYPES_INTERDITS
   scripts.commun.verifier_depot.TAILLE_MAX
   scripts.commun.verifier_depot.DOMAINES_FICTIFS
   scripts.commun.verifier_depot.COURRIEL
   scripts.commun.verifier_depot.IMAGE_DENSITE
   scripts.commun.verifier_depot.TEXTE


Functions
---------

.. autoapisummary::

   scripts.commun.verifier_depot.fichiers
   scripts.commun.verifier_depot.controler
   scripts.commun.verifier_depot.main


Module Contents
---------------

.. py:data:: RACINE

.. py:data:: LOCAUX
   :value: ('data/', '_legacy/', '_brouillons/', '_pilotage/', 'Claude outputs/', '.venv/')


.. py:data:: TYPES_INTERDITS
   :value: ('.pptx', '.mp4', '.mov', '.aup3', '.approj', '.wav', '.m4a')


.. py:data:: TAILLE_MAX
   :value: 5242880


.. py:data:: DOMAINES_FICTIFS
   :value: ('exemple.fr', 'exemple.com', 'example.com', 'example.org', 'moodle.a',...


.. py:data:: COURRIEL

.. py:data:: IMAGE_DENSITE

.. py:data:: TEXTE
   :value: ('.py', '.md', '.txt', '.csv', '.yaml', '.yml', '.json', '.xml', '.html', '.tex', '.bib',...


.. py:function:: fichiers(index: bool)

   Renvoie la liste des fichiers à contrôler (chemins relatifs à la racine du dépôt).

   Avec ``index`` vrai : fichiers ajoutés, copiés, modifiés ou renommés dans l'index git
   (prochain commit) ; sinon : fichiers suivis et nouveaux fichiers non ignorés.
   Quitte le programme si git échoue.


.. py:function:: controler(chemins)

   Contrôle une liste de fichiers et renvoie la liste des problèmes (messages), vide si tout va bien.

   Signale les fichiers sous un dossier local, les types exclus, les fichiers trop gros et,
   dans les fichiers texte, la première adresse de courriel dont le domaine n'est pas fictif.


.. py:function:: main()

   Point d'entrée : contrôle les fichiers et quitte avec le code 1 en cas de problème.


