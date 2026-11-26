scripts.capsuleforge.habillage
==============================

.. py:module:: scripts.capsuleforge.habillage

.. autoapi-nested-parse::

   CapsuleForge — habillage d'une capsule pour une édition de cours (option ``construire --cours``).

   La capsule reste nue (aucun établissement nommé) ; l'habillage est lu dans le profil de l'école de l'édition (clés
   ``charte`` et ``habillage``) et dans la déclaration du cours (``cours.yaml`` : titre, codes, promo, année), puis
   appliqué à la construction : couleurs et logo du lecteur, écran d'accueil, pied de page sous l'image, crédits en fin
   de capsule, filigrane sur les images, titre et nom des paquets SCORM.

   Clé ``habillage`` du profil (toutes facultatives) ::

       habillage:
         logo: logo.png                         # dans le dossier du profil ; logo_nuit facultatif
         modele: modele_ecole.potx              # modèle PowerPoint appliqué aux diapositives d'une édition (Windows)
         cadre: principal                       # couleur des bandes autour des images (rôle ou couleur de la charte)
         pied: "{code} · {promo} · {ecole}"     # sous l'image
         filigrane: {texte: "{ecole} · {promo}", position: bas-droite, opacite: 0.35}
         mentions: "Document réservé aux étudiants de {ecole}"
         licence: "CC BY-NC-SA 4.0"

   Champs des textes : ``{cours}`` (titre du cours), ``{code}`` (code de l'enseignement), ``{bloc}``, ``{promo}``,
   ``{annee}`` (2026-2027), ``{ecole}``, ``{declinaison}``, ``{edition}``, ``{enseignant}``, ``{capsule}``.
   Le filigrane n'est posé que pour une édition qui le demande (``filigrane: true`` dans ``cours.yaml``). Les
   variantes de la capsule (``variantes`` de la déclinaison, plus celles de l'édition) choisissent ce qui ne vaut que
   pour ce public : école, parcours, année (``variantes.py``).



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.habillage.ICI
   scripts.capsuleforge.habillage.POSITIONS
   scripts.capsuleforge.habillage.CHAMP


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.habillage.remplir
   scripts.capsuleforge.habillage.pour_cours
   scripts.capsuleforge.habillage.variantes_edition
   scripts.capsuleforge.habillage.resume
   scripts.capsuleforge.habillage.filigraner
   scripts.capsuleforge.habillage.nom_paquet


Module Contents
---------------

.. py:data:: ICI

.. py:data:: POSITIONS
   :value: ('bas-droite', 'bas-gauche', 'haut-droite', 'haut-gauche', 'centre')


.. py:data:: CHAMP

.. py:function:: remplir(texte: str | None, champs: dict) -> str

   Remplace les champs ``{…}`` connus ; un champ inconnu ou vide disparaît (avec un séparateur « · » orphelin).


.. py:function:: pour_cours(spec: str, titre_capsule: str = '') -> dict

   Habillage d'une édition (``--cours cours[:déclinaison[/édition]]``) : champs, couleurs, logo, textes, filigrane.


.. py:function:: variantes_edition(d: dict | None, e: dict | None) -> list[str]

   Variantes actives d'une édition : celles de la déclinaison, puis celles de l'édition (``variantes`` : liste,
   ou ancienne clé ``variante``).


.. py:function:: resume(h: dict) -> dict

   Ce qui fait l'empreinte d'un habillage (pas de chemin absolu, le logo par son contenu).


.. py:function:: filigraner(im, f: dict)

   Pose le filigrane ``f`` ({texte, position, opacite}) sur l'image PIL ``im`` (RGB) et la renvoie.


.. py:function:: nom_paquet(h: dict | None, capsule: str, label: str | None = None) -> str

   Nom de base des paquets : ``traction_ecole1-meca_2026_v1`` (capsule nue : le nom de la capsule).


