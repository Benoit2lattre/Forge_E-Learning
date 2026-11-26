scripts.capsuleforge.variantes
==============================

.. py:module:: scripts.capsuleforge.variantes

.. autoapi-nested-parse::

   CapsuleForge — variantes d'une capsule : ce qui ne vaut que pour certains publics (une école, un client).

   La capsule source reste unique et nue ; les **variantes** actives (``variantes`` du chapitre, choisies par la
   déclinaison et l'édition du cours ou ``construire --variante a,b``) ajoutent, retirent ou remplacent des morceaux à
   la construction. Plusieurs variantes peuvent être actives ensemble (école, parcours, année) :

   - partie, section, pas ou phrase avec ``variantes: [psa]`` : seulement si l'une de ces variantes est active (absent de
     la capsule nue) ; avec ``sauf: [psa]`` : retiré si l'une d'elles est active ;
   - phrase avec ``pour: {psa: "…"}`` : autre texte pour cette variante (la première active qui en a un) ; avec
     ``audio_pour: {psa: audio/….wav}``, le son de la phrase est remplacé aussi ;
   - pas avec ``fond_pour: {psa: images/….png}`` : autre image ;
   - masque ``{zone: [x, y, l, h], variantes: […]}`` ou ``{zone: …, sauf: […]}`` : zone floutée selon la variante.

   Une phrase retirée coupe son extrait de narration (du début de la phrase au début de la suivante) dans le son du
   pas et dans les voix de synthèse des autres langues ; les phrases et objets qui suivent sont recalés. Un pas vidéo
   garde son film : seuls les sous-titres changent (signalé).



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.variantes.ICI


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.variantes.actives
   scripts.capsuleforge.variantes.retenu
   scripts.capsuleforge.variantes.masques
   scripts.capsuleforge.variantes.appliquer
   scripts.capsuleforge.variantes.noms_a_eviter


Module Contents
---------------

.. py:data:: ICI

.. py:function:: actives(v) -> tuple

   Variantes actives : None, « psa », « ecole1, aero » ou une liste → tuple ordonné sans doublon.


.. py:function:: retenu(e: dict, variante) -> bool

   Un élément (partie, section, pas, phrase, masque) est-il gardé pour ces variantes (aucune : capsule nue) ?


.. py:function:: masques(liste: list, variante: str | None) -> list

   Masques retenus, sous la forme ``[x, y, l, h]``.


.. py:function:: appliquer(chap: dict, variante: str | None, dossier: pathlib.Path, travail: pathlib.Path, journal=print) -> dict

   Copie du chapitre pour une variante (None : capsule nue), sons recoupés écrits dans ``travail``.


.. py:function:: noms_a_eviter(chap: dict, fichier: pathlib.Path | None = None) -> list[str]

   Noms d'établissements trouvés dans la capsule nue (liste privée ``data/capsuleforge/noms_a_eviter.txt`` :
   un nom par ligne, ``#`` pour un commentaire). Seul ce qui reste dans la capsule nue est cherché : un pas ou une
   phrase réservé à une variante peut nommer son client.


