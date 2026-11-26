scripts.capsuleforge.pdf_capsule
================================

.. py:module:: scripts.capsuleforge.pdf_capsule

.. autoapi-nested-parse::

   CapsuleForge — PDF d'une capsule (construire --pdf).

   Le PDF est fait à partir du lecteur construit : mêmes images (habillage de l'édition, variantes, filigrane,
   diapositives traduites), mêmes textes, même langue. Une page imprimable (``<sortie>/imprimer.html``) est écrite à côté
   du lecteur, puis imprimée en PDF par Edge ou Chrome sans fenêtre (Edge est présent sur tout Windows). Sans navigateur,
   la page reste : l'ouvrir et l'imprimer en PDF à la main.

   Contenu : une couverture (logo, titre, cours, code, école, année, promo, enseignant, mentions, licence), puis, partie
   par partie et section par section, chaque diapositive dans son dernier état (toutes ses apparitions) ; à la demande,
   le texte dit, le texte de la diapositive (formules comprises) et de la place pour les notes, en marge ou dessous.
   Pied de page et numéros de page sur chaque page sauf la couverture. Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.pdf_capsule.CONTENUS
   scripts.capsuleforge.pdf_capsule.NOTES
   scripts.capsuleforge.pdf_capsule.CONTENU_PDF
   scripts.capsuleforge.pdf_capsule.NOMS_CONTENU


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.pdf_capsule.page
   scripts.capsuleforge.pdf_capsule.navigateur
   scripts.capsuleforge.pdf_capsule.imprimer
   scripts.capsuleforge.pdf_capsule.ecrire
   scripts.capsuleforge.pdf_capsule.norme
   scripts.capsuleforge.pdf_capsule.cle
   scripts.capsuleforge.pdf_capsule.fichier
   scripts.capsuleforge.pdf_capsule.lire_versions
   scripts.capsuleforge.pdf_capsule.ecrire_versions
   scripts.capsuleforge.pdf_capsule.noter_version
   scripts.capsuleforge.pdf_capsule.faire


Module Contents
---------------

.. py:data:: CONTENUS
   :value: ('texte', 'diapo')


.. py:data:: NOTES
   :value: ('aucune', 'marge', 'dessous')


.. py:function:: page(donnees: dict, langue: str | None = None, contenu=('texte', ), notes: str = 'aucune') -> tuple[str, bool]

   Écrit la page imprimable (HTML) d'une capsule à partir des données du lecteur ; renvoie ``(html, formules)``.


.. py:function:: navigateur() -> str | None

   Edge ou Chrome (ou Chromium) installé, pour imprimer sans fenêtre ; variable ``FORGE_NAVIGATEUR`` d'abord.


.. py:function:: imprimer(page_html: pathlib.Path, pdf: pathlib.Path, journal=print, attente_ms: int = 20000) -> bool

   Imprime la page en PDF avec Edge ou Chrome sans fenêtre ; renvoie vrai si le PDF est écrit.


.. py:function:: ecrire(donnees: dict, sortie: pathlib.Path, nom: str, langue: str | None = None, contenu=('texte', ), notes: str = 'aucune', journal=print, dossier: str = '') -> pathlib.Path | None

   Écrit ``<sortie>/imprimer.html`` puis ``<sortie>/<dossier>/<nom>.pdf`` ; renvoie le chemin du PDF, ou ``None``.


.. py:data:: CONTENU_PDF

.. py:data:: NOMS_CONTENU

.. py:function:: norme(v: dict, src: str) -> dict

   Version complétée et contrôlée : ``{langue, contenu, notes, paquet}``.


.. py:function:: cle(v: dict) -> str

.. py:function:: fichier(v: dict, nom: str) -> str

   Chemin de la version, relatif au dossier du lecteur construit.


.. py:function:: lire_versions(dossier: pathlib.Path, src: str) -> list[dict]

.. py:function:: ecrire_versions(dossier: pathlib.Path, versions: list[dict]) -> None

.. py:function:: noter_version(dossier: pathlib.Path, v: dict, src: str, paquet: bool | None = None) -> list[dict]

   Ajoute ou met à jour une version ; ``paquet`` vrai la met dans le paquet (et en retire l'autre de sa langue).


.. py:function:: faire(donnees: dict, sortie: pathlib.Path, nom: str, v: dict, journal=print) -> pathlib.Path | None

   Fait la version ``v`` du PDF à partir des données du lecteur ; renvoie son chemin, ou ``None``.


