scripts.diagforge.graphiques
============================

.. py:module:: scripts.diagforge.graphiques

.. autoapi-nested-parse::

   QuizForge — graphiques du bilan (DiagForge) : images PNG pour les étudiants et la fiche du professeur.

   Nécessite matplotlib (dans l'environnement : ``uv pip install matplotlib``). Sans matplotlib, le bilan
   est produit sans images et le signale.



Functions
---------

.. autoapisummary::

   scripts.diagforge.graphiques.disponible
   scripts.diagforge.graphiques.palette
   scripts.diagforge.graphiques.histogramme
   scripts.diagforge.graphiques.comparaison_groupes
   scripts.diagforge.graphiques.reussite


Module Contents
---------------

.. py:function:: disponible()

   Indique si matplotlib est installé (``True`` / ``False``).


.. py:function:: palette(principal=COULEUR_PRINCIPALE)

   Renvoie la couleur principale du profil et une liste de teintes distinctes pour les groupes.

   Renvoie ``(principale, couleurs)`` ; ``couleurs`` commence par la couleur principale.


.. py:function:: histogramme(notes20, titre, sortie: pathlib.Path, couleur='#' + COULEUR_PRINCIPALE, sous_titre='')

   Trace l'histogramme des notes sur 20 (classes de 2 points), avec moyenne et médiane.

   Enregistre l'image dans ``sortie`` et renvoie ce chemin.


.. py:function:: comparaison_groupes(par_groupe: dict, titre, sortie: pathlib.Path, couleurs)

   Trace les boîtes à moustaches des notes sur 20 par groupe, avec points individuels (anonymes) et effectifs.

   ``par_groupe`` : groupe → liste de notes. Enregistre l'image dans ``sortie`` et renvoie ce chemin.


.. py:function:: reussite(lignes, titre, sortie: pathlib.Path, couleur, groupes=(), couleurs=())

   Trace en barres horizontales la réussite moyenne (%) par regroupement (tag, type…), promotion et groupes.

   ``lignes`` : ``[{"nom", "promo": fraction, "groupes": {g: fraction}, "n_questions"}]``, triées du plus
   faible au plus fort. Enregistre l'image dans ``sortie`` et renvoie ce chemin.


