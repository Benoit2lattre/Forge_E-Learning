scripts.capsuleforge.calage
===========================

.. py:module:: scripts.capsuleforge.calage

.. autoapi-nested-parse::

   CapsuleForge — calage des objets d'un pas sur ses phrases.

   Un objet (apparition, spot, cadre, pointeur…) peut être accroché à une phrase du texte dit au lieu d'un instant
   fixe ::

       objets:
         - id: e2
           type: apparition
           phrase: 3            # numéro de la phrase (à partir de 1)
           ancre: debut         # debut (par défaut) ou fin de la phrase
           decalage_s: -0.4     # facultatif : réglage par défaut du chapitre sinon
           debut_s: 6.5         # recalculé d'après la phrase ; gardé pour les outils qui le lisent

   Son instant suit alors la phrase : une nouvelle voix, une phrase coupée ou une pause ajoutée le déplacent sans
   rien retoucher. Un objet sans ``phrase`` garde son ``debut_s``. Sans voix, les instants des phrases sont estimés
   d'après le débit de la langue. Une phrase peut porter ``pause_s`` : le silence à laisser après elle.

   Réglages par défaut, modifiables dans la clé ``calage`` du chapitre ::

       calage:
         decalage_s: -0.4       # l'objet apparaît juste avant d'être nommé
         pause_s: 0.4           # silence après chaque phrase
         debit_mots_min: {fr: 150, en: 160}

   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.capsuleforge.calage.DEFAUTS
   scripts.capsuleforge.calage.DEBITS
   scripts.capsuleforge.calage.ANCRES
   scripts.capsuleforge.calage.CLES
   scripts.capsuleforge.calage.PROCHE_S
   scripts.capsuleforge.calage.FIN_MARGE_S


Functions
---------

.. autoapisummary::

   scripts.capsuleforge.calage.reglages
   scripts.capsuleforge.calage.debit
   scripts.capsuleforge.calage.mots
   scripts.capsuleforge.calage.estimer
   scripts.capsuleforge.calage.temps
   scripts.capsuleforge.calage.instant
   scripts.capsuleforge.calage.decalage
   scripts.capsuleforge.calage.accrocher_objet
   scripts.capsuleforge.calage.appliquer_pas
   scripts.capsuleforge.calage.appliquer
   scripts.capsuleforge.calage.instants_langue
   scripts.capsuleforge.calage.accrocher_pas
   scripts.capsuleforge.calage.suivre_decoupage
   scripts.capsuleforge.calage.fin_pas


Module Contents
---------------

.. py:data:: DEFAUTS

.. py:data:: DEBITS

.. py:data:: ANCRES
   :value: ('debut', 'fin')


.. py:data:: CLES
   :value: ('phrase', 'ancre', 'decalage_s')


.. py:function:: reglages(chap: dict) -> dict

   Réglages de calage du chapitre, complétés par les valeurs par défaut.


.. py:function:: debit(chap: dict, langue: str | None = None) -> float

   Débit (mots par minute) de la langue : chapitre, sinon table par défaut, sinon ``MOTS_PAR_MINUTE``.


.. py:function:: mots(texte: str) -> int

.. py:function:: estimer(textes: list[str], pauses: list[float | None], debit_mm: float, reg: dict) -> list[list[float]]

   Instants estimés ``[[début, fin], …]`` de phrases dites au débit donné, avec leurs pauses.


.. py:function:: temps(pas: dict, chap: dict, langue: str | None = None) -> list[list[float]]

   Instants des phrases du pas dans la langue : ceux de la voix s'il y en a une complète, sinon estimés.


.. py:function:: instant(objet: dict, t: list[list[float]], reg: dict) -> float | None

   Instant d'un objet accroché (``None`` s'il ne l'est pas ou si le pas n'a pas de phrase).


.. py:function:: decalage(objet: dict, t_objet: float, t: list[list[float]], reg: dict) -> None

   Règle ``decalage_s`` d'un objet accroché pour qu'il tombe à ``t_objet`` (« Poser à cet instant »).


.. py:data:: PROCHE_S
   :value: 1.0


.. py:function:: accrocher_objet(objet: dict, t_objet: float, t: list[list[float]], reg: dict) -> None

   Accroche un objet à une phrase, en gardant son instant ``t_objet``.

   La phrase choisie est celle qui commence dans la seconde qui suit l'objet (il l'annonce) ; sinon celle qui est
   en cours à cet instant (il l'illustre) ; avant la première phrase, la première.


.. py:function:: appliquer_pas(pas: dict, chap: dict) -> int

   Recalcule ``debut_s`` des objets accrochés du pas (langue source) ; renvoie le nombre d'instants changés.


.. py:function:: appliquer(chap: dict) -> int

   Recalcule les instants des objets accrochés de tout le chapitre ; renvoie le nombre d'instants changés.


.. py:function:: instants_langue(pas: dict, chap: dict, langue: str) -> dict

   ``{id: instant}`` des objets accrochés du pas, dans une langue (instants de sa voix ou estimés).


.. py:function:: accrocher_pas(pas: dict, chap: dict, remplacer: bool = False) -> int

   Accroche aux phrases les objets du pas qui ont un instant ; renvoie le nombre d'objets accrochés.

   Chaque objet est rattaché à la phrase qu'il annonce ou qu'il illustre (voir :func:`accrocher_objet`), avec le
   décalage observé. Il faut des
   instants de phrases (voix ou transcription) : sans eux, rien n'est fait. ``remplacer`` refait aussi les accroches
   existantes.


.. py:function:: suivre_decoupage(pas: dict, chap: dict, nouvelles: list[dict]) -> None

   Garde les accroches quand les phrases du pas changent (coupe, fusion, réécriture).

   À appeler avant de remplacer ``pas["phrases"]`` par ``nouvelles``. D'après les mots des phrases :

   - une phrase gardée telle quelle garde ses objets, même déplacée ;
   - une phrase coupée donne ses objets au morceau où ils tombaient (au premier s'ils l'annonçaient) ;
   - une phrase fondue dans une autre lui donne ses objets, décalés de la place qu'elle y occupe ;
   - une phrase réécrite garde son numéro.


.. py:data:: FIN_MARGE_S
   :value: 0.5


.. py:function:: fin_pas(fin: dict | None, base: float, t: list[list[float]], videos: list[dict]) -> float

   Fin d'un pas, en secondes (voir la clé ``fin`` du pas).

   - absente : automatique, la fin de la voix (``base``), prolongée jusqu'à la fin des vidéos insérées qui ne
     bouclent pas, plus ``FIN_MARGE_S`` ;
   - ``{video: v20, decalage_s: 0.5}`` : après la vidéo ;
   - ``{phrase: 3, decalage_s: 0.5}`` : après la fin de la ligne 3 ;
   - ``{instant_s: 24}`` : à un instant fixe.

   ``videos`` : ``[{id, d, du, b}]`` (départ, durée, boucle) dans la langue de la voix ; ``t`` : instants des lignes.


