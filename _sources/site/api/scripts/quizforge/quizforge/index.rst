scripts.quizforge.quizforge
===========================

.. py:module:: scripts.quizforge.quizforge

.. autoapi-nested-parse::

   QuizForge — banques de questions Moodle à partir d'Excel ou de GIFT.

   Commandes principales ::

       python quizforge.py convertir Quizz.xlsx [autres fichiers…] [--categorie MMC/TP3] [--sortie dossier]
           Excel, GIFT (.txt) ou banque (.yaml) -> GIFT par catégorie + Moodle XML + banque YAML + rapport.
       python quizforge.py importer dossier_ou_fichiers… --banque banque.yaml
           Reprend des fichiers GIFT / Excel existants dans une banque YAML unique, dédoublonnée.
       python quizforge.py modele [--sortie modele_QuizForge.xlsx]
           Crée un classeur modèle avec un onglet par type de question.
       python quizforge.py profils [Ecole1]
           Liste les profils d'établissement, ou affiche les réglages de l'un d'eux.

   Autres commandes : ``valider`` (vérifier classeurs, projets du pointeur et profils), ``bilan``
   (DiagForge : analyse des résultats d'un test Moodle), ``reparer``, ``fusionner`` et ``assistant``
   (menu pas à pas) ; ``python quizforge.py --help`` les décrit toutes.

   Option ``--profil Ecole1`` (convertir, importer) : barème, types autorisés, formats, langues et charte
   lus dans ``profils/Ecole1/profil.yaml`` ; les options de la ligne de commande l'emportent.

   Types gérés : vf (vrai/faux), qcm (une ou plusieurs bonnes réponses), appariement,
   courte (réponse courte), numerique (avec tolérance), essai (réponse libre), et en Moodle XML
   seulement schema (glisser-déposer sur image) et trous (texte à trous).



Attributes
----------

.. autoapisummary::

   scripts.quizforge.quizforge.VERSION
   scripts.quizforge.quizforge.TYPES
   scripts.quizforge.quizforge.XML_SEUL
   scripts.quizforge.quizforge.NUMEROTATIONS
   scripts.quizforge.quizforge.PROFIL_DEFAUT
   scripts.quizforge.quizforge.P
   scripts.quizforge.quizforge.EXT_CLASSEURS
   scripts.quizforge.quizforge.VRAI
   scripts.quizforge.quizforge.FAUX
   scripts.quizforge.quizforge.FRACTIONS
   scripts.quizforge.quizforge.NOMS_TYPES
   scripts.quizforge.quizforge.ENTETES_FIXES
   scripts.quizforge.quizforge.ENTETES_NUMEROTES
   scripts.quizforge.quizforge.LANGUES
   scripts.quizforge.quizforge.SPECIAUX
   scripts.quizforge.quizforge.CHAMPS_TEXTE
   scripts.quizforge.quizforge.MODELE
   scripts.quizforge.quizforge.LISEZMOI
   scripts.quizforge.quizforge.TEXTES_TRADUISIBLES
   scripts.quizforge.quizforge.CLES_PROFIL
   scripts.quizforge.quizforge.COMMANDES


Functions
---------

.. autoapisummary::

   scripts.quizforge.quizforge.comprendre
   scripts.quizforge.quizforge.trouver_fichier
   scripts.quizforge.quizforge.nom_sortie
   scripts.quizforge.quizforge.dossiers_profils
   scripts.quizforge.quizforge.lister_profils
   scripts.quizforge.quizforge.chemin_profil
   scripts.quizforge.quizforge.profil_par_defaut
   scripts.quizforge.quizforge.ecrire_index_profils
   scripts.quizforge.quizforge.charger_profil
   scripts.quizforge.quizforge.couleur
   scripts.quizforge.quizforge.habiller_retroaction
   scripts.quizforge.quizforge.filtrer_types
   scripts.quizforge.quizforge.txt
   scripts.quizforge.quizforge.norm
   scripts.quizforge.quizforge.lire_booleen
   scripts.quizforge.quizforge.fraction_mauvaise
   scripts.quizforge.quizforge.fraction_moodle
   scripts.quizforge.quizforge.cle_question
   scripts.quizforge.quizforge.texte_abime
   scripts.quizforge.quizforge.reparer_texte
   scripts.quizforge.quizforge.reparer_classeur
   scripts.quizforge.quizforge.detecter_type
   scripts.quizforge.quizforge.decouper_tags
   scripts.quizforge.quizforge.ajouter_tags
   scripts.quizforge.quizforge.entete_connu
   scripts.quizforge.quizforge.corriger_entete
   scripts.quizforge.quizforge.lire_excel
   scripts.quizforge.quizforge.separer_langues
   scripts.quizforge.quizforge.lire_projet_pointeur
   scripts.quizforge.quizforge.lire_gift
   scripts.quizforge.quizforge.versions
   scripts.quizforge.quizforge.g_esc
   scripts.quizforge.quizforge.gift_question
   scripts.quizforge.quizforge.ecrire_gift
   scripts.quizforge.quizforge.xml_schema
   scripts.quizforge.quizforge.xml_trous
   scripts.quizforge.quizforge.xml_question
   scripts.quizforge.quizforge.ecrire_xml
   scripts.quizforge.quizforge.ecrire_banque
   scripts.quizforge.quizforge.lire_banque_yaml
   scripts.quizforge.quizforge.dedoublonner
   scripts.quizforge.quizforge.creer_modele
   scripts.quizforge.quizforge.lire_fichiers
   scripts.quizforge.quizforge.chemin_court
   scripts.quizforge.quizforge.appliquer_cours
   scripts.quizforge.quizforge.appliquer_profil
   scripts.quizforge.quizforge.cmd_convertir
   scripts.quizforge.quizforge.ecrire_quiz_seance
   scripts.quizforge.quizforge.cmd_importer
   scripts.quizforge.quizforge.fusionner_classeurs
   scripts.quizforge.quizforge.cmd_fusionner
   scripts.quizforge.quizforge.cmd_reparer
   scripts.quizforge.quizforge.cmd_modele
   scripts.quizforge.quizforge.valider_profil
   scripts.quizforge.quizforge.valider_projet
   scripts.quizforge.quizforge.cmd_valider
   scripts.quizforge.quizforge.cmd_bilan
   scripts.quizforge.quizforge.noter_version_bilan
   scripts.quizforge.quizforge.cmd_profils
   scripts.quizforge.quizforge.assistant
   scripts.quizforge.quizforge.preparer_arguments
   scripts.quizforge.quizforge.main


Module Contents
---------------

.. py:data:: VERSION
   :value: '0.2'


.. py:data:: TYPES
   :value: ['vf', 'qcm', 'appariement', 'courte', 'numerique', 'essai', 'schema', 'trous']


.. py:data:: XML_SEUL
   :value: ('schema', 'trous')


.. py:data:: NUMEROTATIONS
   :value: ['abc', 'ABCD', '123', 'iii', 'IIII', 'none']


.. py:data:: PROFIL_DEFAUT

.. py:data:: P

.. py:function:: comprendre(saisie, choix, quoi: str, annoncer: bool = True)

   Interprète une saisie tolérante et renvoie l'élément de ``choix`` correspondant.

   ``choix`` : liste, ou dictionnaire alias → nom. La saisie est reconnue en entier, sinon par ses 1 à 3
   premières lettres si elles ne désignent qu'un élément. Ce qui a été compris est affiché si ``annoncer``
   est vrai. Quitte le programme avec la liste des possibles si rien ne correspond.


.. py:data:: EXT_CLASSEURS
   :value: ('.xlsx', '.txt', '.gift', '.yaml', '.yml')


.. py:function:: trouver_fichier(nom: str, exts=EXT_CLASSEURS, quoi='fichier') -> pathlib.Path

   Renvoie le fichier ou dossier existant désigné par ``nom``, avec tolérance : extension absente ou mal tapée, nom proche.

   Ce qui a été compris est affiché ; quitte le programme si rien ne convient (avec des suggestions).


.. py:function:: nom_sortie(nom: str, ext: str) -> pathlib.Path

   Renvoie le nom de fichier de sortie avec l'extension ``ext`` : ajoutée si elle manque, corrigée si elle est mal tapée (« Test » → ``Test.xlsx``).


.. py:function:: dossiers_profils()

   Renvoie les dossiers de profils, dans l'ordre de priorité (voir :func:`chemins.dossiers_profils`).


.. py:function:: lister_profils() -> dict

   Renvoie ``{nom: {fichier, alias, description, defaut}}`` pour tous les profils trouvés (``profils/<nom>/profil.yaml``).

   Pour un même nom, le premier trouvé l'emporte (local, puis privé, puis dépôt) ; un profil illisible est signalé et ignoré.


.. py:function:: chemin_profil(nom: str) -> pathlib.Path

   Renvoie le fichier d'un profil désigné par un chemin ``.yaml``, son nom, un alias ou ses premières lettres.

   Quitte le programme si aucun profil n'est trouvé ou si le nom n'est pas compris.


.. py:function:: profil_par_defaut() -> str | None

   Renvoie le nom du premier profil marqué ``defaut``, ou ``None``.


.. py:function:: ecrire_index_profils(force: bool = False)

   Écrit ``index_profils.json`` dans chaque dossier de profils : profils, alias et valeurs acceptées de chaque réglage.

   L'index donne aussi la valeur par défaut de chaque réglage, les commandes et les onglets du modèle.
   Il n'est régénéré que si un profil ``.yaml`` est plus récent que lui, sauf avec ``force``.


.. py:function:: charger_profil(nom: str | None) -> dict

   Charge un profil (réglages par défaut d'un établissement) dans la variable globale ``P`` et le renvoie.

   Sans ``nom`` : réglages par défaut de QuizForge. Les valeurs du profil sont fusionnées avec ``PROFIL_DEFAUT``
   et les noms courts (types, modes) sont interprétés ; les options de la ligne de commande l'emportent ensuite
   (voir :func:`appliquer_profil`). Quitte le programme si une valeur n'est pas comprise.


.. py:function:: couleur(nom_ou_hex: str) -> str

   Renvoie une couleur ``#RRGGBB`` à partir d'un rôle ou d'un nom de couleur de la charte du profil, ou d'un code hexadécimal.


.. py:function:: habiller_retroaction(html: str) -> str

   Encadre la rétroaction générale aux couleurs du profil (Moodle XML).


.. py:function:: filtrer_types(qs: list, rapport: list) -> list

   Renvoie les questions dont le type est autorisé par le profil ; les autres sont signalées dans ``rapport``.


.. py:function:: txt(v) -> str

   Convertit une valeur de cellule en texte sans espaces autour (``None`` → ``""``, ``3.0`` → ``"3"``).


.. py:function:: norm(s) -> str

   Normalise un texte pour la comparaison : sans accents, en minuscules, espaces réduits.


.. py:data:: VRAI

.. py:data:: FAUX

.. py:function:: lire_booleen(v)

   Lit une réponse vrai/faux (T/F, V/F, Vrai/Faux, oui/non, 1/0…) ; renvoie ``True``, ``False`` ou ``None``.


.. py:data:: FRACTIONS
   :value: [100, 90, 83.33333, 80, 75, 70, 66.66667, 60, 50, 40, 33.33333, 30, 25, 20, 16.66667, 14.28571,...


.. py:function:: fraction_mauvaise(nb_bons: int, n_options: int, mode: str | None = None) -> float

   Renvoie la fraction (en %) d'une mauvaise case cochée dans un QCM à plusieurs réponses, avant arrondi Moodle.

   Selon ``mode`` (par défaut ``bareme.qcm.mauvaise_option`` du profil) :

   - ``negative`` : -100/t (t bonnes réponses) ;
   - ``equilibree`` : -100/(n - t), cocher toutes les cases vaut alors 0
     (voir ``reference/B_conception_qcm/schmidt2021.md`` et ``schmidt2022.md``) ;
   - ``zero`` : 0 (cocher tout donne 100 %).


.. py:function:: fraction_moodle(x: float) -> float

   Arrondit une fraction (en %, signe conservé) à la valeur autorisée par Moodle la plus proche (``FRACTIONS``).


.. py:function:: cle_question(q: dict) -> str

   Renvoie la clé de dédoublonnage d'une question : type + énoncé normalisé.


.. py:function:: texte_abime(s: str) -> bool

   Indique si le texte porte la trace d'un Rechercher/Remplacer « V » → « T » sans casse ni mot entier (« plusFin », « deTon »).


.. py:function:: reparer_texte(s: str) -> str

   Répare un texte abîmé par un remplacement « V » → « T » : « plusFin » → « plus fin », « deTon » → « de von ».


.. py:function:: reparer_classeur(chemin: pathlib.Path) -> tuple

   Écrit une copie réparée ``<classeur>_corrige.xlsx`` ; renvoie ``(chemin, liste des corrections)``.

   Le classeur d'origine n'est pas modifié.


.. py:function:: detecter_type(H)

   Reconnaît le type de question d'un onglet d'après ses en-têtes normalisés ; ``None`` si aucun type ne correspond.


.. py:data:: NOMS_TYPES

.. py:function:: decouper_tags(t: str) -> list

   Découpe une liste de tags séparés par ``;`` ou ``,`` (espaces retirés, éléments vides ignorés).


.. py:function:: ajouter_tags(qs: list, extra: list, rapport: list)

   Complète les tags de chaque question, sur place.

   Tags = tags du profil + ``--tags`` + ligne ``$TAGS`` de l'onglet + automatiques + colonne Tags,
   sans doublon (sans tenir compte des majuscules, comme Moodle).


.. py:data:: ENTETES_FIXES
   :value: ['num', 'numero', 'no', 'n', 'titre', 'title', 'question', 'retroaction', 'feedback', 'feedback...


.. py:data:: ENTETES_NUMEROTES
   :value: ['option', 'feedback', 'choix', 'rep', 'mot', 'leurre', 'erreur', 'feedback erreur', 'code...


.. py:function:: entete_connu(h: str) -> bool

   Indique si un en-tête normalisé est reconnu (en-tête fixe ou numéroté, avec ou sans suffixe de langue).


.. py:function:: corriger_entete(h: str)

   Corrige un en-tête mal tapé proche d'un en-tête connu : renvoie ``(en-tête corrigé, True)``, sinon ``(h, False)``.


.. py:function:: lire_excel(chemin: pathlib.Path, racine: str = '', rapport: list | None = None, reparer: bool = False, nom: str = '') -> list

   Lit un classeur Excel QuizForge et renvoie la liste de ses questions (dictionnaires).

   Chaque onglet est un lot de questions d'un même type, reconnu d'après ses en-têtes ; les lignes
   ``$CATEGORY``, ``$SEANCE`` et ``$TAGS`` au-dessus des en-têtes sont prises en compte, ainsi que les
   colonnes de traduction (« Question EN »…).

   - ``racine`` : début de la catégorie Moodle ; ``nom`` : nom de catégorie à la place du nom du classeur ;
   - ``reparer`` : réparer les textes abîmés (sinon ils sont seulement signalés) ;
   - ``rapport`` : reçoit les remarques de lecture.


.. py:data:: LANGUES
   :value: ('en', 'fr', 'es', 'de', 'it')


.. py:function:: separer_langues(H)

   Sépare les colonnes de traduction (« Question EN », « Option 1 (EN) »…).

   Renvoie ``(en-têtes de base, avec None à la place des colonnes de traduction, {langue: {col_base: col_trad}})``.


.. py:function:: lire_projet_pointeur(chemin: pathlib.Path) -> dict

   Lit un projet enregistré par ``scripts/quizforge/outils/pointeur.html`` et renvoie les données utiles à l'export Moodle.

   Lève ``ValueError`` si le projet n'a pas d'image de fond ou si son type est inconnu.


.. py:data:: SPECIAUX
   :value: '~=#{}:'


.. py:function:: lire_gift(chemin: pathlib.Path, racine: str = '', rapport: list | None = None) -> list

   Lit un fichier GIFT et renvoie la liste de ses questions (dictionnaires).

   Les blocs sont séparés par une ligne vide ; ``$CATEGORY:`` change la catégorie, sinon elle est
   construite à partir de ``racine`` et du nom du fichier. Un bloc illisible est signalé dans ``rapport``.


.. py:data:: CHAMPS_TEXTE
   :value: ('question', 'feedback', 'feedback_juste', 'feedback_faux', 'reponse_attendue')


.. py:function:: versions(qs: list, mode: str = 'separe', base: str = 'fr') -> list

   Renvoie les versions linguistiques à écrire, ``[(suffixe, questions)]``.

   Une version par langue (``separe``) ou une version bilingue (``multilang``) ; une seule version, de suffixe vide,
   si aucune question n'a de traduction.


.. py:function:: g_esc(s: str) -> str

   Échappe un texte pour GIFT (caractères spéciaux ``~=#{}:``, barre oblique inverse, sauts de ligne).


.. py:function:: gift_question(q: dict) -> str

   Renvoie le texte GIFT d'une question (un commentaire pour les types décrits seulement en Moodle XML).


.. py:function:: ecrire_gift(questions: list, chemin: pathlib.Path)

   Écrit les questions au format GIFT dans ``chemin``, avec une ligne ``$CATEGORY`` à chaque changement de catégorie.


.. py:function:: xml_schema(q: dict) -> str

   Renvoie le XML Moodle d'une question glisser-déposer sur image (``ddimageortext``) ou à marqueurs (``ddmarker``), depuis un projet du pointeur.


.. py:function:: xml_trous(q: dict) -> str

   Renvoie le XML Moodle d'un texte à trous : glisser-déposer dans le texte (``ddwtos``) ou listes déroulantes (``gapselect``).


.. py:function:: xml_question(q: dict) -> str

   Renvoie le XML Moodle d'une question, avec le barème du profil actif.


.. py:function:: ecrire_xml(questions: list, chemin: pathlib.Path)

   Écrit les questions au format Moodle XML dans ``chemin``, avec une question « category » à chaque changement de catégorie.


.. py:function:: ecrire_banque(questions: list, chemin: pathlib.Path)

   Écrit la banque YAML de QuizForge (version et liste des questions) dans ``chemin``.


.. py:function:: lire_banque_yaml(chemin: pathlib.Path, rapport: list | None = None) -> list

   Lit une banque YAML de QuizForge et renvoie ses questions.


.. py:function:: dedoublonner(questions: list, rapport: list) -> list

   Garde une question par énoncé ; une version avec réponse l'emporte sur un « essai » vide.

   Les doublons écartés, et ceux qui divergent, sont signalés dans ``rapport``.


.. py:data:: MODELE

.. py:data:: LISEZMOI
   :value: ['QuizForge — classeur modèle', '', "Un onglet = un lot de questions d'un même type. Le type est...


.. py:function:: creer_modele(chemin: pathlib.Path, vide: bool = False, onglets=None)

   Écrit le classeur modèle dans ``chemin`` : un onglet « Lisez-moi » puis un onglet par type de question.

   ``vide`` : en-têtes seulement, sans exemples ; ``onglets`` : onglets à garder (tous par défaut).


.. py:function:: lire_fichiers(fichiers, racine, rapport, reparer=False, nom='')

   Lit des classeurs Excel, fichiers GIFT et banques YAML (ou les dossiers qui les contiennent) et renvoie leurs questions.

   Dans un dossier, les sous-dossiers prolongent la catégorie ; les sorties de QuizForge et les rapports sont ignorés.


.. py:function:: chemin_court(p) -> str

   Chemin relatif au dépôt quand il y est (rapports sans chemin personnel), sinon tel quel.


.. py:function:: appliquer_cours(a) -> list

   Option ``--cours`` : complète profil, catégorie, effectif et étiquettes avec ceux du cours, de sa déclinaison
   et de son édition (les options données l'emportent ; les étiquettes s'ajoutent). Renvoie les lignes du rapport.


.. py:function:: appliquer_profil(a)

   Charge le profil puis complète les options laissées vides sur la ligne de commande.


.. py:function:: cmd_convertir(a)

   Commande ``convertir`` : écrit pour chaque fichier, selon les formats retenus, la banque YAML, le Moodle XML,
   les GIFT par catégorie, et ``rapport.txt``.

   Les sorties vont dans ``<fichier>_QuizForge`` (ou ``--sortie``) ; avec ``--seance``, le plan du quiz de séance est écrit aussi.


.. py:function:: ecrire_quiz_seance(qs: list, a, f: pathlib.Path, sortie: pathlib.Path) -> list

   Écrit le plan du quiz de la séance n (``<classeur>_plan_Snn.md``) et renvoie les lignes à ajouter au rapport.

   Rien n'est recopié dans la banque. Le plan donne une section par catégorie de la séance, puis une section
   de rappels par séance précédente, avec le nombre de questions à tirer selon ``quiz.tirage`` du profil.
   Il donne aussi le score au hasard et le seuil du quiz tel qu'il sera tiré, et le nombre de réponses attendu
   par question (DiagForge calcule la discrimination à partir de 20 réponses et la juge solide à partir de 50).
   Rappels : pratique de récupération espacée (``reference/A_tests_retroaction/yang2021.md``, ``murray2025.md``).


.. py:function:: cmd_importer(a)

   Commande ``importer`` : réunit des fichiers existants dans une banque YAML unique, dédoublonnée.

   Écrit aussi ``<banque>_rapport.txt`` et, avec ``--xml`` (ou un profil qui le prévoit), la banque en Moodle XML.


.. py:data:: TEXTES_TRADUISIBLES

.. py:function:: fusionner_classeurs(fr: pathlib.Path, autre: pathlib.Path, lang: str = 'en') -> tuple

   Ajoute à une copie du classeur FR les colonnes « … EN » lues dans le classeur traduit (même structure).

   Écrit ``<classeur>_bilingue.xlsx`` et renvoie ``(chemin, rapport)`` ; les réponses qui diffèrent entre les deux
   classeurs sont signalées.


.. py:function:: cmd_fusionner(a)

   Commande ``fusionner`` : réunit un classeur FR et sa traduction en un classeur bilingue.


.. py:function:: cmd_reparer(a)

   Commande ``reparer`` : écrit une copie corrigée d'un classeur abîmé par un remplacement « V » → « T ».


.. py:function:: cmd_modele(a)

   Commande ``modele`` : crée le classeur modèle (ou un classeur vide), sans écraser un fichier existant sauf avec ``--ecraser``.


.. py:data:: CLES_PROFIL

.. py:function:: valider_profil(f: pathlib.Path) -> list

   Vérifie un fichier de profil (YAML lisible, clés connues, valeurs comprises) et renvoie la liste des problèmes.


.. py:function:: valider_projet(f: pathlib.Path) -> list

   Vérifie un projet du pointeur (JSON) et renvoie la liste des problèmes : type, image, zones, énoncé, leurres.


.. py:function:: cmd_valider(a)

   Commande ``valider`` : vérifie classeurs, projets du pointeur et profils, sans rien écrire.

   Signale aussi les points d'écriture à vérifier dans les questions (rétroaction absente, indices qui
   trahissent la clé, défauts d'écriture : voir ``qualite``).


.. py:function:: cmd_bilan(a)

   Commande ``bilan`` (DiagForge) : bilan des résultats d'un test Moodle (exports Notes + Réponses) → classeur d'analyse.

   La couleur principale et le mode de tirage sont pris dans le profil s'il y en a un (voir :func:`bilan.bilan`).


.. py:function:: noter_version_bilan(a)

   Reconnaît la version QuizForge du test d'après les noms des questions de l'export XML (registres des cours),
   l'écrit dans le bilan (onglet « Version ») et inscrit le bilan au registre.


.. py:function:: cmd_profils(a)

   Commande ``profils`` : liste les profils, ou affiche les réglages complets de l'un d'eux ; régénère les index.


.. py:data:: COMMANDES
   :value: ['convertir', 'importer', 'reparer', 'fusionner', 'profils', 'modele', 'valider', 'bilan', 'assistant']


.. py:function:: assistant()

   Lance l'assistant : menu pas à pas où chaque choix se fait par un numéro.

   La commande équivalente est affichée avant d'être lancée ; Ctrl+C ou fin de saisie quitte l'assistant.


.. py:function:: preparer_arguments(argv)

   Prépare les arguments de la ligne de commande avec une saisie tolérante de la commande.

   « con », « -c », « C », « Convertir »… sont compris ; un fichier seul (glissé sur ``QuizForge.bat``) vaut
   ``convertir``. Sans argument, renvoie ``["--help"]``.


.. py:function:: main(argv=None)

   Point d'entrée : interprète les arguments (``sys.argv`` par défaut) et lance la commande demandée.


