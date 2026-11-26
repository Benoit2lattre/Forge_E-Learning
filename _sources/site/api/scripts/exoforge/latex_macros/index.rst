scripts.exoforge.latex_macros
=============================

.. py:module:: scripts.exoforge.latex_macros

.. autoapi-nested-parse::

   Lecture des macros LaTeX de l'auteur (préambule IguanaTeX) pour MathJax.

   - ``\newcommand{\nom}[n]{corps}`` → ``{"nom": ["corps", n]}`` (configuration MathJax ``tex.macros``) ;
   - ``\definecolor{Nom}{rgb}{r,g,b}`` → ``{"Nom": "#rrggbb"}`` (couleurs déclarées au chargement) ;
   - ``\colorlet{alias}{Nom}`` → même couleur (couleurs par rôle : ``roleDef``, ``rolePro``…).

   Les ``\usepackage``, ``\include``, environnements et commandes non mathématiques sont ignorés.



Attributes
----------

.. autoapisummary::

   scripts.exoforge.latex_macros.REMPLACEMENTS


Functions
---------

.. autoapisummary::

   scripts.exoforge.latex_macros.lire_macros
   scripts.exoforge.latex_macros.couleurs_inconnues


Module Contents
---------------

.. py:data:: REMPLACEMENTS

.. py:function:: lire_macros(*fichiers)

   Lit les fichiers LaTeX donnés et renvoie ``(macros, couleurs, ignorees)``.

   - ``macros`` : nom (sans barre oblique inverse) → corps, ou ``[corps, nombre d'arguments]`` ;
   - ``couleurs`` : nom → code ``#RRGGBB`` (``\definecolor`` en ``rgb``, ``RGB`` ou ``HTML``, et alias ``\colorlet``) ;
   - ``ignorees`` : extraits des définitions non comprises et des ``\colorlet`` vers une couleur inconnue.

   Les commentaires ``%`` sont retirés avant la lecture ; ``\mathbbm`` est remplacé par ``\mathbb``.


.. py:function:: couleurs_inconnues(macros, couleurs)

   Repère les ``\textcolor{X}`` vers une couleur jamais définie (faute de frappe).

   Renvoie la liste des couples ``(nom de la macro, couleur inconnue)`` ; les couleurs standard
   (``white``, ``black``, ``red``…) sont admises.


