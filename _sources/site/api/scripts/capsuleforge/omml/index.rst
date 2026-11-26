scripts.capsuleforge.omml
=========================

.. py:module:: scripts.capsuleforge.omml

.. autoapi-nested-parse::

   CapsuleForge — équations natives d'Office (OMML) converties en LaTeX.

   Les équations de PowerPoint (Insertion, Équation) sont écrites en OMML dans le diaporama. :func:`latex` en donne
   le LaTeX, pour MathJax (volet « Texte » du lecteur, PDF) : fractions, racines, exposants et indices, parenthèses
   et crochets, fonctions (exp, ln, sin…), sommes et intégrales, accents, matrices, lettres grecques et symboles
   courants. Ce qui n'est pas reconnu garde son texte.

   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.omml.M
   scripts.capsuleforge.omml.GRECS
   scripts.capsuleforge.omml.SYMBOLES
   scripts.capsuleforge.omml.FONCTIONS
   scripts.capsuleforge.omml.GRANDS
   scripts.capsuleforge.omml.ACCENTS
   scripts.capsuleforge.omml.DELIMS


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.omml.latex


Module Contents
---------------

.. py:data:: M
   :value: '{http://schemas.openxmlformats.org/officeDocument/2006/math}'


.. py:data:: GRECS

.. py:data:: SYMBOLES

.. py:data:: FONCTIONS

.. py:data:: GRANDS

.. py:data:: ACCENTS

.. py:data:: DELIMS

.. py:function:: latex(o_math) -> str

   LaTeX d'un élément ``m:oMath`` (ou ``m:oMathPara``), espaces superflus réduits.


