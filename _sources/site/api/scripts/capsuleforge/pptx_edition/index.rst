scripts.capsuleforge.pptx_edition
=================================

.. py:module:: scripts.capsuleforge.pptx_edition

.. autoapi-nested-parse::

   CapsuleForge — images des diapositives PowerPoint d'une édition (``construire --cours``).

   Les images d'un chapitre repris d'un diaporama sont celles de la capsule nue. Une diapositive qui porte des formes
   d'édition (« cf édition », « cf édition ecole1 », « cf nu ») ou des champs (``{cours}``, ``{promo}``…) est
   réexportée par PowerPoint pour l'édition : formes montrées pour son public (école du profil et variantes),
   champs remplis. Les autres diapositives gardent les images nues. Si le profil de l'école donne un modèle
   PowerPoint (``habillage: {modele: modele_ecole.potx}``), toutes les diapositives sont réexportées avec ce modèle
   appliqué (thème, polices, couleurs et masque de l'école ; dispositions appariées par leur nom).

   Diapositives traduites : pour chaque autre langue du chapitre, les diapositives dont le texte (``texte_diapo``) a des
   traductions sont réexportées avec ces textes à la place des textes d'origine (capsule nue ou édition), et gardées
   en cache de la même façon (:func:`plan_langues`, :func:`produire_langues`).

   Le diaporama est cherché là où il a été repris (``source.chemin`` de la section), à côté du chapitre, dans
   ``sources/``, puis parmi les diaporamas retenus par l'atelier. Les images d'une édition sont gardées en cache dans ``<chapitre>/_editions/<clé>/`` : elles ne sont refaites que
   si le diaporama, la liste des diapositives, l'habillage ou la largeur change. Sans PowerPoint (hors Windows), le
   cache sert s'il est à jour ; sinon la construction s'arrête plutôt que de ranger une édition mal habillée.
   Licence : GPL v3.



Functions
---------

.. autoapisummary::

   scripts.capsuleforge.pptx_edition.publics
   scripts.capsuleforge.pptx_edition.trouver
   scripts.capsuleforge.pptx_edition.a_habiller
   scripts.capsuleforge.pptx_edition.controler_modele
   scripts.capsuleforge.pptx_edition.plan
   scripts.capsuleforge.pptx_edition.resume
   scripts.capsuleforge.pptx_edition.produire
   scripts.capsuleforge.pptx_edition.plan_langues
   scripts.capsuleforge.pptx_edition.resume_langues
   scripts.capsuleforge.pptx_edition.produire_langues


Module Contents
---------------

.. py:function:: publics(h: dict) -> list[str]

   Publics d'une édition, pour les formes « cf édition … » : l'école du profil, puis les variantes actives.


.. py:function:: trouver(dossier: pathlib.Path, fichier: str, chemin: str | None = None) -> pathlib.Path | None

   Cherche le diaporama d'une section : chemin noté à la reprise (``source.chemin``, relatif au chapitre), à côté
   du chapitre, dans ``sources/`` (et plus bas), puis celui que l'atelier a retenu (réglages de l'atelier).


.. py:function:: a_habiller(d: dict, masque: str, champs_masque: list, modele: bool = False) -> bool

   Vrai si l'image d'une diapositive change d'une édition à l'autre (toutes, avec un modèle d'école).


.. py:function:: controler_modele(chemin: pathlib.Path, modele: pathlib.Path, diapos: list[int], journal=print) -> list[int]

   Compare le diaporama et le modèle de l'école avant de l'appliquer ; renvoie les diapositives dont la
   disposition n'existe pas dans le modèle (PowerPoint en choisirait une autre).


.. py:function:: plan(y: pathlib.Path, chap: dict, h: dict, journal=print) -> dict | None

   Prépare l'habillage PowerPoint d'une édition, sans PowerPoint : diapositives à refaire par diaporama.

   Renvoie ``None`` si aucune diapositive du chapitre n'en a besoin. Sinon ``{publics, champs, masque, largeur,
   diaporamas: [{fichier, chemin, md5, diapos, rels}], cle}``, où ``rels`` sont les images du chapitre remplacées.


.. py:function:: resume(pl: dict | None) -> dict | None

   Ce qui fait l'empreinte de l'habillage PowerPoint (sans chemin) : diaporamas, diapositives, habillage, code.


.. py:function:: produire(pl: dict | None, dossier: pathlib.Path, journal=print) -> dict

   Produit (ou reprend du cache) les images de l'édition et renvoie ``{image du chapitre: image de l'édition}``.

   Arrête le programme si PowerPoint manque et que le cache n'est pas à jour.


.. py:function:: plan_langues(y: pathlib.Path, chap: dict, h: dict | None, journal=print) -> list[dict]

   Prépare les diapositives traduites (H14), sans PowerPoint : pour chaque autre langue du chapitre et chaque
   diaporama, les diapositives qui ont des textes traduits et leur table de traduction.

   Les images sont celles de la capsule nue (``h`` vide) ou de l'édition (formes d'édition, champs, modèle de
   l'école), textes remplacés. Renvoie une liste de travaux ``{langue, cle, fichier, chemin, md5, diapos,
   traductions: {n: {source: cible}}, rels, publics, champs, masque, modele, modele_md5, largeur}``.


.. py:function:: resume_langues(travaux: list[dict]) -> list[dict] | None

   Empreinte des diapositives traduites (sans chemin) : langue, diaporama, diapositives, textes, habillage, code.


.. py:function:: produire_langues(travaux: list[dict], dossier: pathlib.Path, journal=print, exiger: bool = False) -> dict

   Produit (ou reprend du cache) les diapositives traduites ; renvoie ``{langue: {image du chapitre: image}}``.

   Sans PowerPoint et sans cache à jour : arrêt si ``exiger`` (édition rangée comme version), sinon les images de la
   langue source restent, avec un avertissement.


