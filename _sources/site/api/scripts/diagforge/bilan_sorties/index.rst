scripts.diagforge.bilan_sorties
===============================

.. py:module:: scripts.diagforge.bilan_sorties

.. autoapi-nested-parse::

   QuizForge — DiagForge, sorties exploitées du bilan :

   1. étudiants : notes de la promotion et par groupe (images PNG anonymes) ;
   2. étudiants + professeur : réussite par tag, par type de question, par catégorie (images + détail) ;
   3. professeur : questions à revoir en priorité (onglet « À revoir » + fiche HTML).

   Groupes : roster (fichier avec une colonne Groupe) en priorité, sinon suffixe du nom du test (``Quizz1_SMA`` → ``SMA``).



Attributes
----------

.. autoapisummary::

   scripts.diagforge.bilan_sorties.TYPES


Functions
---------

.. autoapisummary::

   scripts.diagforge.bilan_sorties.est_roster
   scripts.diagforge.bilan_sorties.lire_roster
   scripts.diagforge.bilan_sorties.affecter_groupes
   scripts.diagforge.bilan_sorties.notes_par_etudiant
   scripts.diagforge.bilan_sorties.stats_groupes
   scripts.diagforge.bilan_sorties.regroupements
   scripts.diagforge.bilan_sorties.a_revoir
   scripts.diagforge.bilan_sorties.images
   scripts.diagforge.bilan_sorties.fiche


Module Contents
---------------

.. py:data:: TYPES

.. py:function:: est_roster(p: pathlib.Path) -> bool

   Indique si le fichier est une liste d'étudiants avec leur groupe (colonne Groupe, sans colonne de début de tentative).


.. py:function:: lire_roster(fichiers, avert)

   Lit les rosters et renvoie ``{clé: groupe}``, avec pour clés le courriel, nom+prénom et prénom+nom.

   Ajoute à ``avert`` un message par fichier (nombre d'étudiants, groupes).


.. py:function:: affecter_groupes(tent, roster, avert)

   Renseigne le groupe de chaque tentative (clé ``groupe``), en modifiant les tentatives sur place.

   Le roster est cherché par courriel puis par nom+prénom ; à défaut, le groupe est le suffixe du nom
   du test. Les étudiants absents du roster sont signalés dans ``avert``.


.. py:function:: notes_par_etudiant(tent, mode)

   Renvoie une note sur 20 par étudiant : ``[{"id", "groupe", "note20"}]``.

   En mode ``toutes`` ou ``meilleure`` : meilleure tentative, comme la méthode par défaut de Moodle ;
   sinon la tentative déjà retenue.


.. py:function:: stats_groupes(notes)

   Calcule les statistiques des notes sur 20 par groupe (et pour la promotion s'il y a plusieurs groupes).

   Renvoie ``(lignes, par_groupe)`` : une ligne par groupe (effectif, moyenne, médiane, écart-type,
   min, max, part ≥ 10/20) et le dictionnaire groupe → notes. Les étudiants sans groupe sont rangés sous « — ».


.. py:function:: regroupements(obs, infos, groupes)

   Calcule la réussite par regroupement de questions (tag, type, catégorie), pour la promotion et par groupe.

   Renvoie ``{"tag": [...], "type": [...], "categorie": [...]}`` ; chaque ligne : ``nom``, ``n_questions``, ``n``,
   ``promo``, ``groupes``, ``detail``, triées de la moins à la plus réussie. Les tags sans information
   (sur presque toutes les questions, ou identiques à un type) sont ignorés.


.. py:function:: a_revoir(questions)

   Classe les questions à revoir par priorité : ce qu'il faut changer dans la question, et ce qu'il faut retravailler en cours.

   Le score additionne les problèmes repérés (discrimination, erreur dominante, difficulté, leurres) ;
   la priorité le pondère par le nombre de réponses. Renvoie les lignes triées, numérotées par ``rang``.


.. py:function:: images(dossier: pathlib.Path, nom_test, notes, par_groupe, regr, couleur, mode='meilleure')

   Produit les images PNG pour les étudiants dans ``dossier`` (notes, comparaison des groupes, réussite par regroupement).

   ``mode`` : tentatives retenues (voir :func:`notes_par_etudiant`), rappelé sous le titre de l'histogramme.
   Renvoie ``(chemins des images, message)`` ; sans matplotlib, aucune image et un message d'explication.


.. py:function:: fiche(sortie: pathlib.Path, nom_test, synth_lignes, stats_g, regr, revoir, imgs, couleur)

   Écrit la fiche du professeur, page HTML autonome (images intégrées), et renvoie son chemin.

   Sections : notes, où se produisent les erreurs, questions à revoir en priorité, indicateurs du test.


