scripts.commun.registre
=======================

.. py:module:: scripts.commun.registre

.. autoapi-nested-parse::

   Forge E-Learning — versions des conversions QuizForge et registre d'une édition (ou d'un cours).

   Une conversion faite pour un cours devient une **version** : un dossier ``quiz/<classeur>/S03_v2/`` (séance si un
   plan est demandé, numéro qui s'incrémente par classeur) sous l'édition, ou sous le cours pour un extrait commun à
   plusieurs déclinaisons, avec des fichiers au nom explicite et une fiche ``version.yaml`` (date, classeur et son
   empreinte, réglages, noms des questions). Rien n'est écrasé ; une reconversion sans changement du classeur ni des
   réglages ne crée pas de version (« identique à v2 »).

   Le **registre** (``registre.yaml`` du même dossier) a une ligne par version, que l'atelier et DiagForge complètent :
   convertie → importée dans Moodle → passée → bilan fait (ou abandonnée), avec dates, test Moodle, bilans, remarques.
   DiagForge reconnaît la version d'un bilan d'après les noms des questions de l'export XML de Moodle.



Attributes
----------

.. autoapisummary::

   scripts.commun.registre.FICHIER
   scripts.commun.registre.ETATS
   scripts.commun.registre.LIBELLES
   scripts.commun.registre.DOSSIERS


Functions
---------

.. autoapisummary::

   scripts.commun.registre.rel
   scripts.commun.registre.absolu
   scripts.commun.registre.maintenant
   scripts.commun.registre.base
   scripts.commun.registre.lire
   scripts.commun.registre.ecrire
   scripts.commun.registre.tous
   scripts.commun.registre.empreinte_fichier
   scripts.commun.registre.empreinte
   scripts.commun.registre.genre
   scripts.commun.registre.nom_source
   scripts.commun.registre.preparer
   scripts.commun.registre.enregistrer_exercice
   scripts.commun.registre.enregistrer
   scripts.commun.registre.modifier
   scripts.commun.registre.noms_xml
   scripts.commun.registre.reconnaitre
   scripts.commun.registre.public
   scripts.commun.registre.noter_bilan


Module Contents
---------------

.. py:data:: FICHIER
   :value: 'registre.yaml'


.. py:data:: ETATS
   :value: ('convertie', 'importee', 'passee', 'bilan', 'abandonnee')


.. py:data:: LIBELLES

.. py:function:: rel(p) -> str

.. py:function:: absolu(chemin) -> pathlib.Path

.. py:function:: maintenant() -> str

.. py:function:: base(r: dict) -> pathlib.Path

   Dossier du registre pour des réglages de cours (``cours_options.resoudre``) : l'édition, sinon le cours.


.. py:function:: lire(b: pathlib.Path) -> dict

.. py:function:: ecrire(b: pathlib.Path, reg: dict)

.. py:function:: tous() -> list[pathlib.Path]

   Dossiers qui ont un registre, dans data/cours et donnees/cours.


.. py:function:: empreinte_fichier(f: pathlib.Path) -> str

.. py:function:: empreinte(f: pathlib.Path, reglages: dict) -> str

.. py:data:: DOSSIERS

.. py:function:: genre(v: dict) -> str

.. py:function:: nom_source(v: dict) -> str

   Nom de ce qui est versionné : classeur (quiz) ou identifiant de la fiche (exercice).


.. py:function:: preparer(b: pathlib.Path, classeur: pathlib.Path, seance, emp: str, genre_: str = 'quiz', nom: str | None = None) -> dict

   Prochaine version d'un classeur ou d'une fiche (dossier, numéro, libellé) ; ``identique`` si une version a déjà
   cette empreinte.


.. py:function:: enregistrer_exercice(b: pathlib.Path, v: dict, fiche: pathlib.Path, reglages: dict, emp: str, cours: str)

   Fiche ``version.yaml`` et ligne du registre pour un paquet ExoForge copié dans le dossier de la version.


.. py:function:: enregistrer(b: pathlib.Path, v: dict, classeur: pathlib.Path, reglages: dict, questions: list, seance, emp: str, cours: str)

   Écrit ``version.yaml`` dans le dossier de la version et ajoute sa ligne au registre.


.. py:function:: modifier(b: pathlib.Path, ident: str, champs: dict) -> dict

   Change l'état (daté du jour si aucune date n'est donnée), le test Moodle, les remarques, « utilisée par ».


.. py:function:: noms_xml(fichiers) -> set[str]

   Noms des questions d'exports Moodle XML (les questions « category » ne comptent pas).


.. py:function:: reconnaitre(noms: set, bases) -> dict | None

   Version dont les questions ressemblent le plus à ``noms`` : {base, version, score, manquantes, en_trop}.


.. py:function:: public(b: pathlib.Path) -> bool

   Registre d'un cours de démonstration publié (donnees/cours) : lu, mais jamais réécrit par un bilan.


.. py:function:: noter_bilan(b: pathlib.Path, ident: str, bilan: pathlib.Path | None, fiche: pathlib.Path | None)

