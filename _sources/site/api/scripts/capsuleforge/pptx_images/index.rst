scripts.capsuleforge.pptx_images
================================

.. py:module:: scripts.capsuleforge.pptx_images

.. autoapi-nested-parse::

   CapsuleForge — images d'un diaporama, une par état d'animation, produites par PowerPoint (Windows).

   PowerPoint est piloté par COM : le fichier est ouvert en lecture seule, sans fenêtre ; pour chaque état, les
   formes et paragraphes qui ne sont pas encore apparus sont cachés en mémoire, puis la diapositive est exportée
   en PNG. Rien n'est enregistré dans le diaporama. Si PowerPoint était déjà ouvert, il le reste.

   Habillage (paramètre ``edition`` de :func:`exporter`) : les formes « cf édition … » et « cf nu » sont montrées ou
   cachées selon le public, les champs ``{cours}``, ``{promo}``… sont remplis (vides pour la capsule nue ; une forme
   qui n'a plus que des séparateurs est cachée), et, masque nu, les formes du masque (« Masquer les graphiques
   d'arrière-plan ») et les pieds de page sans champ sont cachés ; le fond et les couleurs du thème restent. Avec
   le modèle d'une école (``edition["modele"]``), ce modèle est appliqué au diaporama ouvert (jamais enregistré) et
   son masque est montré ; les pieds de page de l'auteur restent cachés.

   Dépendance : ``comtypes`` (déjà installé avec ``uiautomation``).
   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.pptx_images.CHAMPS
   scripts.capsuleforge.pptx_images.TOLERANCE_PT
   scripts.capsuleforge.pptx_images.SEPARATEURS
   scripts.capsuleforge.pptx_images.FINS


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.pptx_images.chevauchements
   scripts.capsuleforge.pptx_images.remplir
   scripts.capsuleforge.pptx_images.appliquer_modele
   scripts.capsuleforge.pptx_images.traduire
   scripts.capsuleforge.pptx_images.montree
   scripts.capsuleforge.pptx_images.exporter


Module Contents
---------------

.. py:data:: CHAMPS
   :value: ('cours', 'code', 'bloc', 'promo', 'annee', 'ecole', 'declinaison', 'edition', 'enseignant', 'capsule')


.. py:data:: TOLERANCE_PT
   :value: 3.0


.. py:function:: chevauchements(diapo, n: int, largeur_pt: float, hauteur_pt: float, masque: bool = True) -> list[str]

   Textes qui se chevauchent ou débordent sur une diapositive, après l'application du modèle de l'école (ou la
   traduction) : texte plus grand que sa zone, texte hors de la diapositive, deux textes l'un sur l'autre, texte
   qui passe en partie sur une autre forme (fond, contour, image, tableau), texte sur une forme du masque ou de la
   disposition (logo, pied de page). Un texte posé tout entier sur une forme n'est pas signalé. Renvoie une phrase par
   problème.


.. py:data:: SEPARATEURS
   :value: ' \t·•|,;:/—–-'


.. py:data:: FINS
   :value: Multiline-String

   .. raw:: html

      <details><summary>Show Value</summary>

   .. code-block:: python

      """
      
      
      """

   .. raw:: html

      </details>



.. py:function:: remplir(forme, valeurs: dict) -> str

   Remplace les champs ``{…}`` du texte d'une forme par ``valeurs``, mise en forme gardée ; un champ vide est
   effacé avec un séparateur voisin. Renvoie le texte obtenu.


.. py:function:: appliquer_modele(pres, modele: pathlib.Path, numeros: list[int], journal) -> None

   Applique le modèle de l'école au diaporama ouvert (en mémoire, jamais enregistré) et vérifie que chaque
   diapositive garde sa disposition (appariée par son nom) ; sinon, la remet d'après son nom si le modèle l'a.


.. py:function:: traduire(forme, table: dict) -> int

   Remplace dans une forme chaque paragraphe (ou cellule de tableau) dont le texte est dans ``table``
   (``{texte source: traduction}``, textes réduits à des espaces simples) ; renvoie le nombre de remplacements.

   Le remplacement garde la mise en forme du début du paragraphe ; un texte lié (valeur ``[traduction, [textes
   liés]]``) que l'on retrouve dans la traduction reste en place, avec son lien et son style, et seul ce qui
   l'entoure est remplacé. Les paragraphes sont parcourus du dernier au premier, pour que les positions restent justes.


.. py:function:: montree(f: dict, publics) -> bool

   Dit si une forme d'édition (``pptx_lire``) est montrée pour ces publics (``None`` : capsule nue).


.. py:function:: exporter(fichier: pathlib.Path, diapos: list[dict], dossier: pathlib.Path, largeur: int, journal=print, edition: dict | None = None) -> list[str]

   Écrit ``<dossier>/images/dNN_eK.png`` pour chaque état des diapositives données et renvoie les chemins relatifs écrits.

   ``diapos`` : diapositives issues de ``pptx_lire.lire`` ; ``largeur`` : largeur des images en pixels.
   ``edition`` : ``{publics, champs, masque, modele}`` — ``publics`` : écoles et variantes de l'édition, ``None``
   pour la capsule nue ; ``champs`` : valeurs des champs ; ``masque`` : ``nu`` (défaut) ou ``garder`` ;
   ``modele`` : modèle PowerPoint de l'école, appliqué avant l'export (son masque est alors montré) ;
   ``traductions`` : ``{diapositive: {texte source: traduction}}``, textes remplacés avant les champs. Sans ``edition``,
   tout est montré tel quel. Ne fonctionne que sous Windows, avec PowerPoint installé.


