scripts.quizforge.schema.wohler_schema
======================================

.. py:module:: scripts.quizforge.schema.wohler_schema

.. autoapi-nested-parse::

   Prototype « Schéma » : courbe de Wöhler schématique + 3 questions glisser-déposer Moodle.

   Usage ::

       python wohler_schema.py

   Produit dans le dossier courant ::

       wohler_niveaux.png, wohler_transitions.png, wohler_domaines.png   (images de fond)
       wohler_schema_moodle.xml                                         (3 questions à importer)
       apercu_*.png                                                     (images avec les zones, pour contrôle)

   Principe : la figure est tracée par le script, donc la position de chaque zone est calculée
   à partir de coordonnées physiques (N, σ) et non mesurée à la main en pixels.



Attributes
----------

.. autoapisummary::

   scripts.quizforge.schema.wohler_schema.L_ZONE
   scripts.quizforge.schema.wohler_schema.TAILLE_ZONE
   scripts.quizforge.schema.wohler_schema.COUL
   scripts.quizforge.schema.wohler_schema.RE
   scripts.quizforge.schema.wohler_schema.BANDES
   scripts.quizforge.schema.wohler_schema.DELTA
   scripts.quizforge.schema.wohler_schema.DECADES
   scripts.quizforge.schema.wohler_schema.COUL_DECADES


Functions
---------

.. autoapisummary::

   scripts.quizforge.schema.wohler_schema.borne
   scripts.quizforge.schema.wohler_schema.sigma
   scripts.quizforge.schema.wohler_schema.figure
   scripts.quizforge.schema.wohler_schema.dessiner_bandes
   scripts.quizforge.schema.wohler_schema.contour_decade
   scripts.quizforge.schema.wohler_schema.dessiner_dispersion
   scripts.quizforge.schema.wohler_schema.vers_pixels
   scripts.quizforge.schema.wohler_schema.png
   scripts.quizforge.schema.wohler_schema.q_niveaux
   scripts.quizforge.schema.wohler_schema.q_transitions
   scripts.quizforge.schema.wohler_schema.q_domaines
   scripts.quizforge.schema.wohler_schema.xml_question
   scripts.quizforge.schema.wohler_schema.apercu
   scripts.quizforge.schema.wohler_schema.main


Module Contents
---------------

.. py:data:: L_ZONE
   :value: 170


.. py:data:: TAILLE_ZONE

.. py:function:: borne(x, l=L_ZONE)

   Arrondit l'abscisse ``x`` (pixels) d'une zone de largeur ``l`` pour qu'elle reste dans l'image (marge de 4 px).


.. py:data:: COUL

.. py:function:: sigma(logn)

   Renvoie l'amplitude de contrainte de la courbe schématique pour ``logn`` = log10 N (scalaire ou tableau).

   Courbe arrondie à 3 pentes : plateau Rm, pente de Basquin, plateau σD.


.. py:data:: RE

.. py:function:: figure(variante)

   Trace la courbe de Wöhler schématique et renvoie ``(fig, ax)``.

   ``variante`` : ``"niveaux"`` (pointillés aux trois niveaux), ``"transitions"`` (bande de dispersion
   découpée par décade) ou ``"domaines"`` (bandes de couleur).


.. py:data:: BANDES
   :value: [(330, 700, (3, 4), '#E0B989', '#748CAB'), (0, 215, (6, 7), '#6F8F78', '#BD7A5C')]


.. py:function:: dessiner_bandes(ax, alpha=0.45)

   Dessine les bandes de ``BANDES`` : couleur différente de part et d'autre, dégradé dans la transition.


.. py:data:: DELTA
   :value: 48


.. py:data:: DECADES

.. py:data:: COUL_DECADES
   :value: ['#D3DDEC', '#ECD2A8']


.. py:function:: contour_decade(a, b, n=12)

   Renvoie le contour ``[(log N, σ)…]`` de la bande de dispersion entre les décades ``a`` et ``b``.


.. py:function:: dessiner_dispersion(ax)

   Dessine la bande de dispersion découpée par décade et les courbes 5 %, 50 % et 95 %.


.. py:function:: vers_pixels(ax, logn, s)

   Convertit des coordonnées physiques (log N, σ) en pixels de l'image (origine en haut à gauche).


.. py:function:: png(fig)

   Renvoie l'image PNG de la figure, en octets.


.. py:function:: q_niveaux()

   Construit la question glisser-déposer sur image « nommer les trois niveaux de contrainte ».

   Renvoie ``(fig, question)``.


.. py:function:: q_transitions()

   Construit la question à marqueurs « pointer les deux zones de transition ».

   Les marqueurs se déposent dans la bande de dispersion découpée par décade ; les sept autres
   décades sont des leurres portés par la figure. Renvoie ``(fig, question)``.


.. py:function:: q_domaines()

   Construit la question glisser-déposer sur image « nommer les quatre domaines » (bandes de couleur, une étiquette en trop).

   Renvoie ``(fig, question)``.


.. py:function:: xml_question(q, image, nom_image)

   Renvoie le XML Moodle d'une question glisser-déposer (``ddimageortext`` ou ``ddmarker``).

   ``image`` : octets PNG de l'image de fond, intégrée en base64 sous le nom ``nom_image``.


.. py:function:: apercu(fig, q, chemin)

   Enregistre dans ``chemin`` une image de contrôle : zones et étiquettes dessinées par-dessus la figure.


.. py:function:: main()

   Écrit dans le dossier courant les trois images, leurs aperçus et ``wohler_schema_moodle.xml``.


