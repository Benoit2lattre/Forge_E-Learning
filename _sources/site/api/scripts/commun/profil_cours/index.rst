scripts.commun.profil_cours
===========================

.. py:module:: scripts.commun.profil_cours

.. autoapi-nested-parse::

   Forge E-Learning — ce que le profil d'établissement dit des cours (clés facultatives, lues par AtelierForge).

   Chaque école découpe ses formations, nomme ses niveaux, code ses enseignements et nomme ses promotions à sa
   façon. Le profil le décrit ; sans ces clés, les mots et les listes génériques ci-dessous s'appliquent et les
   codes restent libres.

   - ``structure`` : niveaux d'organisation, par défaut ``[parcours, bloc, enseignement]`` ;
   - ``vocabulaire`` : mots de l'école pour ``enseignement``, ``bloc`` et ``parcours`` ;
   - ``campus``, ``parcours`` : listes de noms, ou de ``{nom, code}`` (code court utilisé dans les gabarits) ;
   - ``formations`` : ``{code, nom, niveaux, modalites, rncp, suite}`` ; ``suite`` = code de la formation qui la
     prolonge, pour le calcul de l'année de diplomation (une licence suivie d'un master) ;
   - ``codes`` : gabarits des codes, ``{longueurs: {bloc: 3, cours: 2}, bloc: "{bloc}-{niveau}",
     enseignement: "{bloc}-{niveau}-{cours}"}`` ;
   - ``promo`` : gabarit du nom de promotion, ``"P{diplomation}"`` ou ``"X{entree:aa}"``.

   Champs des gabarits : ``{niveau}`` (L3), ``{formation}`` (L), ``{annee}`` (3), ``{modalite}``, ``{campus}``,
   ``{parcours}`` (codes courts), ``{bloc}`` et ``{cours}`` (abrégés saisis) ; pour la promo ``{diplomation}`` et
   ``{entree}`` (quatre chiffres, ou deux avec ``:aa``).



Attributes
----------

.. autoapisummary::

   scripts.commun.profil_cours.STRUCTURE
   scripts.commun.profil_cours.VOCABULAIRE
   scripts.commun.profil_cours.MODALITES_INGENIEUR
   scripts.commun.profil_cours.FORMATIONS
   scripts.commun.profil_cours.CHAMP


Functions
---------

.. autoapisummary::

   scripts.commun.profil_cours.lire
   scripts.commun.profil_cours.generique
   scripts.commun.profil_cours.formation_du_niveau
   scripts.commun.profil_cours.appliquer
   scripts.commun.profil_cours.motif
   scripts.commun.profil_cours.champs_declinaison
   scripts.commun.profil_cours.annees_promo
   scripts.commun.profil_cours.pour_ecole
   scripts.commun.profil_cours.remarques_codes


Module Contents
---------------

.. py:data:: STRUCTURE
   :value: ['parcours', 'bloc', 'enseignement']


.. py:data:: VOCABULAIRE

.. py:data:: MODALITES_INGENIEUR
   :value: ['FISE', 'FISA', 'FISEA', 'FC']


.. py:data:: FORMATIONS

.. py:data:: CHAMP

.. py:function:: lire(d: dict | None) -> dict

   Profil (dict lu du YAML) → réglages des cours, complétés par les valeurs génériques.


.. py:function:: generique() -> dict

.. py:function:: formation_du_niveau(reglages: dict, niveau: str, formation: str | None = None) -> dict | None

.. py:function:: appliquer(gabarit: str, champs: dict) -> str

   Remplit un gabarit ; un champ vide laisse ``?`` (code incomplet, visible).


.. py:function:: motif(gabarit: str, longueurs: dict | None = None) -> re.Pattern

   Expression régulière d'un code conforme au gabarit (pour ``cours.py verifier``).


.. py:function:: champs_declinaison(reglages: dict, d: dict) -> dict

   Champs des gabarits d'une déclinaison (codes courts du campus et du parcours, abrégés saisis).


.. py:function:: annees_promo(reglages: dict, niveau: str, annee_edition: int, formation: str | None = None) -> dict | None

   Années d'entrée et de diplomation d'une édition (année scolaire qui commence en ``annee_edition``),
   d'après la place du niveau dans sa formation et les formations qui la prolongent (``suite``).


.. py:function:: pour_ecole(nom: str | None) -> dict | None

   Réglages des cours du profil d'établissement ``nom`` (None si aucun profil ne porte ce nom).


.. py:function:: remarques_codes(d: dict) -> list[str]

   Codes d'une déclinaison qui ne suivent pas les gabarits du profil de son école.


