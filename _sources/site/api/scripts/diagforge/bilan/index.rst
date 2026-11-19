scripts.diagforge.bilan
=======================

.. py:module:: scripts.diagforge.bilan

.. autoapi-nested-parse::

   QuizForge — DiagForge : bilan des résultats d'un test Moodle (exports « Notes » et « Réponses »).

   Usage ::

       python quizforge.py bilan <dossier ou fichiers> [-q questions.xml] [-t toutes|premiere|derniere|meilleure] [-s sortie.xlsx]

   Lit les exports du rapport de test Moodle, en anglais ou en français, en CSV ou en XLSX :

   - « Notes » (Grades) : note de chaque tentative et note de chaque position (Q. 1 /1,00…) ;
   - « Réponses » (Responses), de préférence avec « Texte de la question » et « Bonne réponse » cochés :
     indispensable quand le test tire des questions au hasard (Q. 1 désigne alors une position, pas une question).

   Les deux sont réunis tentative par tentative (courriel, début, fin, durée).
   L'export XML des questions (facultatif) donne le nom de chaque question et ses options (leurres jamais choisis).
   L'export « Statistiques » de Moodle n'est pas utilisé pour les calculs : les indicateurs sont recalculés ici,
   son résumé n'est affiché que pour comparaison.

   Produit un classeur : Synthèse, Questions, Réponses, Éléments, Étudiants, Tentatives, et selon les données
   À revoir, Tirage, Rétention, Par erreur, Groupes, Par tag / type / catégorie ; ainsi qu'une fiche du
   professeur (HTML) et des images pour les étudiants (voir ``bilan_sorties``).



Attributes
----------

.. autoapisummary::

   scripts.diagforge.bilan.SEUILS
   scripts.diagforge.bilan.ALPHA_ATTENDU
   scripts.diagforge.bilan.MOIS
   scripts.diagforge.bilan.TYPES_YAML
   scripts.diagforge.bilan.GREC


Functions
---------

.. autoapisummary::

   scripts.diagforge.bilan.plancher_difficulte
   scripts.diagforge.bilan.lecture_discrimination
   scripts.diagforge.bilan.alpha_cronbach
   scripts.diagforge.bilan.alpha_ramene
   scripts.diagforge.bilan.cle_texte
   scripts.diagforge.bilan.propre
   scripts.diagforge.bilan.nombre
   scripts.diagforge.bilan.duree_s
   scripts.diagforge.bilan.date
   scripts.diagforge.bilan.pearson
   scripts.diagforge.bilan.lire_table
   scripts.diagforge.bilan.colonnes
   scripts.diagforge.bilan.nom_du_test
   scripts.diagforge.bilan.groupe_du_test
   scripts.diagforge.bilan.lire_exports
   scripts.diagforge.bilan.lire_banque_xml
   scripts.diagforge.bilan.completer_banque_yaml
   scripts.diagforge.bilan.codes_erreur
   scripts.diagforge.bilan.par_erreur
   scripts.diagforge.bilan.lisible
   scripts.diagforge.bilan.abrege
   scripts.diagforge.bilan.tronc
   scripts.diagforge.bilan.identifier
   scripts.diagforge.bilan.accolades
   scripts.diagforge.bilan.elements
   scripts.diagforge.bilan.forme
   scripts.diagforge.bilan.cases
   scripts.diagforge.bilan.choisir_tentatives
   scripts.diagforge.bilan.analyser
   scripts.diagforge.bilan.indicateurs
   scripts.diagforge.bilan.alpha_par_tag
   scripts.diagforge.bilan.etudiants
   scripts.diagforge.bilan.ecrire
   scripts.diagforge.bilan.trouver_fichiers
   scripts.diagforge.bilan.bilan


Module Contents
---------------

.. py:data:: SEUILS

.. py:data:: ALPHA_ATTENDU

.. py:function:: plancher_difficulte(k)

   Renvoie la réussite sous laquelle une question à ``k`` options est « très difficile ».

   C'est environ le hasard + 0,10 (slepkov2021 : 0,43 à 3 options, 0,35 à 4, 0,30 à 5 ; 0,60 à 2 options,
   par extension), jamais moins de 0,30 ; 0,30 si le nombre d'options est inconnu.


.. py:function:: lecture_discrimination(r, reussite)

   Renvoie la lecture de la discrimination item-reste ``r`` : « à revoir », « faible », « correcte », « très bonne » ou « peu fiable ».

   « Peu fiable » quand la réussite est hors de l'intervalle ``fiable_min`` – ``fiable_max`` de ``SEUILS`` ;
   chaîne vide si ``r`` est ``None``.


.. py:function:: alpha_cronbach(colonnes)

   Calcule l'alpha de Cronbach, ou ``None`` s'il n'est pas calculable.

   ``colonnes`` : une liste de notes par question, mêmes tentatives dans le même ordre.


.. py:function:: alpha_ramene(alpha, k, cible=50)

   Applique la formule de Spearman-Brown : alpha d'un test de même qualité allongé (ou raccourci) de ``k`` à ``cible`` questions.

   Renvoie ``None`` si ``alpha`` est absent, négatif ou nul, ou si ``k`` < 2.


.. py:function:: cle_texte(t) -> str

   Renvoie une clé de comparaison : sans accents, en minuscules, lettres et chiffres seulement.


.. py:function:: propre(t) -> str

   Renvoie le texte sans balises HTML, entités décodées, espaces insécables et multiples réduits.


.. py:function:: nombre(t)

   Lit un nombre écrit à l'anglaise ou à la française (virgule, espaces, %) ; renvoie ``None`` si ce n'en est pas un.


.. py:function:: duree_s(t)

   Convertit une durée Moodle (« 3 mins 20 secs », « 1 heure 5 min »…) en secondes ; ``None`` si rien n'est reconnu.


.. py:data:: MOIS

.. py:function:: date(t)

   Convertit une date Moodle en ``datetime`` (sinon ``None``).

   Formes reconnues : « 6 November 2026  12:12 AM », « 6 novembre 2026, 00:12 », « 06/11/2026 00:12 ».


.. py:function:: pearson(x, y)

   Renvoie le coefficient de corrélation de Pearson, ou ``None`` (moins de 3 points ou variance nulle).


.. py:function:: lire_table(p: pathlib.Path)

   Lit un export CSV ou XLSX et renvoie ses lignes non vides (listes de chaînes).

   Pour un CSV : encodage UTF-8 ou Windows-1252, séparateur deviné sur la première ligne ; un export
   interrompu par une page d'erreur HTML est coupé avant celle-ci.


.. py:function:: colonnes(entete)

   Repère le rôle de chaque colonne d'un en-tête d'export Moodle.

   Renvoie ``(fixes, slots, total)`` : ``fixes = {"nom": i, ...}`` (identité, état, dates, durée),
   ``slots = {k: {"note": i, "max": m, "question": i, "reponse": i, "bonne": i}}`` par position,
   ``total = (indice, note maximale)`` de la colonne de note globale, ou ``None``.


.. py:function:: nom_du_test(stem: str) -> str

   Extrait le nom du test d'un nom de fichier : « MMC-Quizz1_SMA-grades » → « Quizz1_SMA ».

   Moodle nomme ses exports ``<cours>-<test>-<rapport>``.


.. py:function:: groupe_du_test(test: str) -> str

   Extrait le groupe d'un nom de test : « Quizz1_SMA » → « SMA » (suffixe court après le dernier ``_``), sinon ``""``.


.. py:function:: lire_exports(fichiers, avert, moodle=None)

   Lit les exports « Notes » et « Réponses » et renvoie la liste des tentatives (dictionnaires).

   Les lignes des différents exports sont réunies sur (test, courriel, début, fin, durée) et leur rang
   d'apparition, pour séparer deux tentatives commencées à la même minute.
   ``avert`` reçoit un message par fichier ; ``moodle``, s'il est fourni, reçoit le résumé de l'export
   « Statistiques ».


.. py:function:: lire_banque_xml(xmls)

   Lit les exports XML Moodle des questions et renvoie la banque (liste de dictionnaires).

   Chaque question : ``nom``, ``type``, ``texte``, ``options``, ``single``, ``tags`` et ``categorie``.
   Un fichier illisible est ignoré.


.. py:data:: TYPES_YAML

.. py:function:: completer_banque_yaml(chemins, banque)

   Complète la banque avec les banques YAML de QuizForge (``convertir`` → ``<classeur>_banque.yaml``).

   Ajoute les erreurs types visées par les leurres (Code erreur n) aux questions de même nom ;
   une question absente de l'export XML est ajoutée. Renvoie la banque.


.. py:function:: codes_erreur(rep, q)

   Renvoie les erreurs types (Code erreur n de QuizForge) que trahit une réponse ; ``[]`` si la banque n'en donne pas.


.. py:function:: par_erreur(obs, infos)

   Renvoie une ligne par erreur type, de la plus fréquente à la moins fréquente.

   Chaque ligne donne les questions qui la visent, les réponses, la part des réponses qui la trahissent, les
   étudiants qui la font, et ceux qui la font sur au moins deux questions (un diagnostic sur une seule
   question est fragile : klingbeil2024).


.. py:data:: GREC

.. py:function:: lisible(t) -> str

   Renvoie le texte d'une réponse pour un message : formules ``$…$`` ou ``\(…\)`` rendues en Unicode, numéro d'étiquette « 5. » retiré.


.. py:function:: abrege(t, n: int) -> str

   Renvoie :func:`lisible` de ``t`` coupé à ``n`` caractères au plus, à une fin de mot, avec « … ».


.. py:function:: tronc(resume: str) -> str

   Renvoie le texte de la question sans la liste d'options que Moodle ajoute au résumé (ordre mélangé).


.. py:function:: identifier(resume, banque)

   Renvoie la question de la banque dont le texte commence le résumé Moodle (la plus longue correspondance), sinon ``None``.


.. py:function:: accolades(t)

   Renvoie les groupes entre accolades de premier niveau : ``'{a} {b{c}}'`` → ``['a', 'b{c}']``.


.. py:function:: elements(rep: str)

   Découpe une réponse composée (zones, paires, trous) en ``[(élément, valeur)]`` ; ``None`` si la réponse est simple.


.. py:function:: forme(rep: str) -> str

   Renvoie une forme canonique pour regrouper les réponses identiques (ordre des paires et des cases cochées ignoré).


.. py:function:: cases(rep)

   Renvoie l'ensemble des cases cochées d'une réponse de QCM à plusieurs réponses (séparées par ``;``).


.. py:function:: choisir_tentatives(tent, mode)

   Garde les tentatives terminées et, sauf en mode ``"toutes"``, une seule par étudiant.

   ``mode`` : ``"toutes"``, ``"premiere"``, ``"derniere"`` ; toute autre valeur garde la meilleure note.
   Renvoie les tentatives dans l'ordre de lecture.


.. py:function:: analyser(tent, banque, avert)

   Calcule les statistiques par question à partir des tentatives retenues.

   Identifie chaque question (par la banque, sinon par le début de son texte, sinon par sa position),
   puis calcule réussite, discrimination item-reste, répartition des réponses, alertes et détail des
   réponses composées. Renvoie ``(questions, reponses, elems, obs, infos)`` ; ``obs`` et ``infos`` sont
   les observations et informations par question, reprises par les autres analyses.


.. py:function:: indicateurs(tent)

   Calcule les indicateurs du test comme Moodle, sur les tentatives entièrement notées.

   Moyenne, médiane, écart-type (échantillon), asymétrie, aplatissement, cohérence interne (alpha de
   Cronbach sur les positions), alpha ramené à 50 questions, ratio d'erreur, erreur type, en % de la note
   maximale. Renvoie ``{}`` s'il y a moins de 4 tentatives.


.. py:function:: alpha_par_tag(obs, infos, n_min=10)

   Calcule l'alpha de Cronbach par tag (au moins 3 questions), sur les tentatives notées à toutes les questions du tag.

   Renvoie ``[(tag, alpha, k, n)]`` ; ``alpha`` vaut ``None`` si moins de ``n_min`` tentatives contiennent toutes
   les questions (tirage au hasard). Les tags portés par presque toutes les questions sont ignorés.


.. py:function:: etudiants(tent_toutes)

   Renvoie une ligne par étudiant : notes (première, dernière, meilleure, moyenne), durée médiane et remarques.

   Signale les tentatives très rapides et faibles (réponses au hasard ?) et les tentatives à corriger.
   Les lignes sont triées par nom puis prénom.


.. py:function:: ecrire(sortie: pathlib.Path, synth, questions, reponses, elems, etus, tent, couleur=COULEUR_PRINCIPALE, plus=None)

   Écrit le classeur du bilan (XLSX) dans ``sortie``.

   ``synth`` : ``{"lignes": [(titre, texte)], "histo": [(classe, effectif)]}`` pour la feuille Synthèse ;
   ``plus`` : feuilles facultatives (``revoir``, ``equite``, ``retention``, ``erreurs``, ``groupes``,
   ``regroupements``) ; ``couleur`` : couleur des en-têtes.


.. py:function:: trouver_fichiers(cibles)

   Sépare les fichiers donnés (ou contenus dans les dossiers donnés) en exports et banques.

   Renvoie ``(exports, banques)`` : exports ``.csv`` / ``.xlsx`` (sauf fichiers temporaires et bilans
   déjà produits) ; banques ``.xml`` et ``*_banque.yaml``.


.. py:function:: bilan(cibles, xml=None, mode='toutes', sortie=None, couleur=COULEUR_PRINCIPALE, roster=None, images=True, tirage=None)

   Produit le bilan complet d'un test et renvoie le chemin du classeur.

   - ``cibles`` : dossiers ou fichiers d'exports Moodle ;
   - ``xml`` : banques de questions (XML ou YAML, fichiers ou dossiers), sinon celles trouvées dans ``cibles`` ;
   - ``mode`` : tentatives retenues (voir :func:`choisir_tentatives`) ;
   - ``roster`` : listes d'étudiants avec leur groupe ;
   - ``images`` : produire les graphiques pour les étudiants ;
   - ``tirage`` : mode de tirage déclaré dans le profil.

   Écrit ``bilan_<test>.xlsx`` (ou ``sortie``), la fiche du professeur ``…_fiche_prof.html`` et, si demandé,
   le dossier ``…_images``. Quitte le programme si aucun export ou aucune tentative n'est lu.


