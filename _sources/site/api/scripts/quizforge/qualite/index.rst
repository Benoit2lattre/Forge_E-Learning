scripts.quizforge.qualite
=========================

.. py:module:: scripts.quizforge.qualite

.. autoapi-nested-parse::

   QuizForge — contrôle de la qualité d'écriture des questions (appelé par ``quizforge valider``).

   Règles simples, sans modèle de langue, tirées des fiches de lecture (``reference/A_tests_retroaction``, ``B_conception_qcm``) :

   - rétroaction absente (vanderkleij2015, attali2017) ;
   - défauts d'écriture et indices qui trahissent la clé (downing2005, tarrant2008, haladyna2022, moore2023, menze2026) ;
   - QCM à 4 options ou plus (haladyna2022, raymond2018) ; options numériques dans l'ordre (gierl2017).

   Chaque alerte est un point à vérifier, pas un verdict : une clé plus longue ou un « toujours » peuvent être voulus.



Attributes
----------

.. autoapisummary::

   scripts.quizforge.qualite.CLE_LONGUE
   scripts.quizforge.qualite.VF_PLAGE
   scripts.quizforge.qualite.N_MIN_ONGLET
   scripts.quizforge.qualite.ABSOLUS
   scripts.quizforge.qualite.TOUTES_AUCUNE
   scripts.quizforge.qualite.COMBINEE
   scripts.quizforge.qualite.NEGATION
   scripts.quizforge.qualite.CONSIGNE
   scripts.quizforge.qualite.MOTS_VIDES


Functions
---------

.. autoapisummary::

   scripts.quizforge.qualite.controler_question
   scripts.quizforge.qualite.penalite
   scripts.quizforge.qualite.hasard_question
   scripts.quizforge.qualite.rapport_hasard
   scripts.quizforge.qualite.controler


Module Contents
---------------

.. py:data:: CLE_LONGUE
   :value: 1.3


.. py:data:: VF_PLAGE
   :value: (0.35, 0.65)


.. py:data:: N_MIN_ONGLET
   :value: 4


.. py:data:: ABSOLUS

.. py:data:: TOUTES_AUCUNE

.. py:data:: COMBINEE

.. py:data:: NEGATION

.. py:data:: CONSIGNE

.. py:data:: MOTS_VIDES

.. py:function:: controler_question(q) -> list

   Contrôle une question lue par ``lire_excel`` et renvoie la liste des alertes ``[(poids, message)]``.

   Poids : 3 = indice fort ou défaut qui fausse la question ; 2 = à revoir ; 1 = à considérer.


.. py:function:: penalite(t, n, mode)

   Renvoie la pénalité d'une mauvaise case cochée dans un QCM à plusieurs réponses (t bonnes sur n).

   ``mode`` (barème ``mauvaise_option`` du profil) : ``"zero"`` → 0 ; ``"equilibree"`` → -1/(n - t)
   (si n > t) ; sinon (``"negative"``) → -1/t.


.. py:function:: hasard_question(q, mode='negative')

   Renvoie ``(score au hasard, score avec la moitié des connaissances, score en cochant tout)`` en fraction, ou ``None``.

   Le troisième terme ne vaut que pour un QCM à plusieurs réponses (``None`` sinon). Les questions
   numériques, à réponse courte, à trous et ouvertes renvoient ``None``.


.. py:function:: rapport_hasard(qs: list, mode='negative') -> list

   Renvoie les lignes du rapport de ``convertir`` : score au hasard et seuil conseillé, par onglet et pour le classeur.


.. py:function:: controler(qs: list, mode: str = 'negative') -> list

   Contrôle les questions d'un classeur et renvoie des lignes « [poids] source : message », triées par poids décroissant.

   Les régularités d'un onglet (rétroactions absentes, position et longueur des clés, vrai/faux) sont regroupées ;
   le poids est écrit en points d'exclamation (``[!!!]`` pour 3).


