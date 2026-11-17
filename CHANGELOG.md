# Journal des versions

Chaque outil a son propre numéro de version (voir la page « État des outils » du site).

## Forge E-Learning 0.3 — en préparation

### CapsuleForge 0.9

- Paquets SCORM 1.2 en plus de SCORM 2004 (`construire --scorm … --scorm-version 1.2`) ; le lecteur reconnaît seul la version de la plateforme.
- Traduction des questions QuizForge et des exercices ExoForge d'un chapitre (`traduire`, même fichier et même écran de relecture que les sous-titres) ; exercice traduit avec les boutons du moteur en anglais.
- Remarques de `verifier` affichées dans l'écran de relecture (encadré « À vérifier sur ce pas », « ⚠ » dans la liste des pas).
- Un seul serveur local (`serveur_local.py`) pour l'éditeur, la relecture et la relecture des traductions (sans changement visible).
- La reprise d'un diaporama (`pptx`) est dans `pptx_lire.reprendre` (sans changement visible).
- Raccourcis clavier et bips communs à `enregistrer` et `filmer` (`raccourcis.py`) ; bips joués par la sortie son de Windows (ils étaient muets sur beaucoup de portables).
- Une seule règle de découpage en phrases (`format_chapitre.decouper_phrases`) pour la relecture, la transcription et la voix de synthèse ; une diapositive sans enregistrement garde son gras dans les sous-titres.
- `filmer` vérifie la section avant de filmer (et non après) ; `--section` facultatif avec `--sans-import` ; message d'erreur avec la liste des parties.
- Réponses numériques des exercices arrondies dans les traces (0,66 au lieu de 0.6599999999999999) ; écran de départ d'une section mis à jour quand on change de langue.
- Correction : réponse numérique d'une question de fin de section écrite comme un calcul (« 5000/100 ») lue comme dans ExoForge (fractions, opérations, virgule, unité finale ignorée) ; elle n'était lue que jusqu'au premier signe (5000/100 était compté faux, 50/1 juste).
- Correction : le plan du lecteur n'affiche plus « Exercice : Exercice : … » quand le titre de la fiche ExoForge commence déjà par « Exercice : ».
- Mode d'emploi : captures du lecteur de chapitre (section, questions, exercice) et de l'écran de relecture, faites sur un chapitre de démonstration fictif.
- Correction : relancer `pptx` sur un chapitre effaçait les voix de synthèse des autres langues (champ `voix` des pas) ; elles sont gardées, comme la caméra, les gestes et les autres champs que la reprise ne produit pas.
- Code réorganisé sans changement de comportement : `format_chapitre.py`, `construire_chapitre.py` et `lecteur_chapitre.html` (anciennement `format2.py`, `construire2.py`, `lecteur2.html`) ; fonctions partagées rendues publiques (`ordonner`, `minsec`, `masquer`, `fiche_exoforge`, `trouver_section`) ; sons (`sons.py` : rééchantillonnage, écriture WAV) mis en commun.

### ExoForge 0.8 (correction)

- Bouton « Écouter » : lecture dans la langue de la page (un exercice traduit est lu en anglais, et non plus avec une voix française) ; voix « naturelles » du navigateur choisies d'abord quand il en a (Edge, Chrome).

### DiagForge 0.6

- Code dans son propre dossier, `scripts/diagforge/` (`bilan.py`, `bilan_sorties.py`, `graphiques.py`, `tirage.py`, `outils/promotion_fictive.py`) ; nouvelle commande `python scripts/diagforge/diagforge.py <exports…>`, équivalente à `quizforge.py bilan` (toujours disponible, mêmes options).
- Noms explicites : `lire_banque_xml` (export XML Moodle), `completer_banque_yaml` (banques QuizForge), `cle_texte`.

### Code commun aux outils (sans changement de comportement)

- Couleur principale par défaut écrite une seule fois (`scripts/commun/charte.py`) pour QuizForge et DiagForge.
- QuizForge : `cle_question`, `lire_banque_yaml` (noms distincts de ceux de DiagForge) ; schéma de Wöhler sans code mort.
- ExoForge : lecture des `\input` / `\include` des fichiers LaTeX écrite une seule fois (`generique._fichiers_inclus`).
- CapsuleForge : `SeanceEditeur`, `SeanceRelecture`, `SeanceTraduction` (trois classes `Seance` auparavant).

## Forge E-Learning 0.2.1 — novembre 2026

Corrections sans changement de format :

- ExoForge : `build.py --help` affiche l'aide.
- DiagForge : le sous-titre de l'histogramme des notes indique la tentative retenue (première, dernière ou meilleure) ; aide de `bilan -t` précisée.
- CapsuleForge : aide de la commande et de `voix --moteur` à jour ; message de `verifier` sans renvoi bibliographique interne ; journal de compression vidéo corrigé quand le son vient d'un autre fichier ; aide de `filmer` exacte (noms des fichiers, `--micro NOM`).

## Forge E-Learning 0.2 — novembre 2026

Forge E-Learning 0.2 réunit quatre outils libres pour passer d'un cours existant à des activités Moodle : QuizForge (questions à partir d'un classeur Excel, avec contrôle de leur écriture), ExoForge (exercices guidés à données tirées, en HTML5 et SCORM), DiagForge (analyse des résultats et de la qualité des questions) et CapsuleForge, nouveau dans cette version : un diaporama narré devient un chapitre de cours interactif, sous-titré, traduit, avec questions et exercices, déposé dans Moodle en paquet SCORM. Les réglages s'appuient sur une bibliographie de 250 références et 197 fiches de lecture.

### QuizForge 0.9

- `valider` contrôle l'écriture des questions : rétroaction absente, clé nettement plus longue que les leurres, position de la clé, « toutes / aucune des réponses », termes absolus, négation non mise en évidence, vrai/faux déséquilibrés, options numériques hors ordre, énoncé sans consigne.
- Barème des QCM à réponses multiples : `negative`, `equilibree` (cocher toutes les cases rapporte 0), `zero` interdit en réponses multiples notées ; score au hasard et seuil de réussite par onglet.
- Questions numériques : erreurs types avec leur rétroaction, rétroaction générale fausse, indices (mode interactif à plusieurs essais).
- Codes d'erreur sur les leurres et les erreurs numériques, enregistrés dans la banque YAML.
- Colonne `Séance` et plan de quiz de séance (questions tirées, rappels des séances précédentes) ; bloc `quiz` des profils.
- Exemple « matrice rainflow » : signal et matrice redessinés.

### ExoForge 0.8

- Moteur générique : un même moteur joue toutes les fiches (étapes d'information, de choix et de valeur numérique, encadré permanent, données tirées et valeurs calculées).
- Graphiques dans l'encadré et dans les étapes (courbes, couleurs, épaisseurs, séries de points révélées), formules avec les couleurs de rôle.
- Nouveaux exercices d'exemple ; graphiques dans les questions.
- La licence de MathJax (`MATHJAX_LICENSE`) est copiée avec `mathjax.js` dans chaque exercice et chaque paquet SCORM.

### DiagForge 0.5

- Nouveau nom de l'analyse des résultats (anciennement « bilan »).
- Lecture des banques QuizForge : erreur type par réponse, onglet « Par erreur ».
- Analyse du tirage des questions : mode observé, équité entre étudiants, rétention.
- Seuils de lecture des indicateurs (discrimination, fiabilité, leurres non fonctionnels) tirés de la bibliographie.

### CapsuleForge 0.8 (0.2 à 0.7.1 dans l'historique de développement)

- Éditeur visuel et lecteurs des capsules de simulation logicielle (format 1).
- Format de chapitre (format 2) : parties, sections, pas, parcours ; reprise d'un diaporama PowerPoint narré ; transcription ; relecture du texte dit ; annotations dessinées dans PowerPoint.
- Lecteur de chapitre : parcours, jauges, badges, questions QuizForge en fin de section, exercices ExoForge.
- Paquets SCORM 2004 (chapitre ou partie) : avancement repris, note pondérée, interactions.
- Traduction (écran de relecture), sous-titres, voix de synthèse ; interface du lecteur traduite.
- Fusion des sources : import de vidéos (dont exports ActivePresenter), didacticiel dans le lecteur de chapitre, enregistrement d'écran, de micro et de webcam.

### Bibliographie

- Neuf axes (tests et rétroaction, QCM, analyse d'items, exemples guidés, multimédia, vidéo interactive, restitution, spécificités STEM, accessibilité) : 250 références, 197 fiches de lecture, 602 règles adressées aux outils avec leur niveau de preuve.

### Dépôt et site

- Site de documentation (Jupyter Book) : accueil, page « Pourquoi de tels outils ? », état des outils, modes d'emploi, bibliographie, skills, prochaines étapes, référence API ; modes jour et nuit.
- Docstrings du code mises au propre pour la référence API.
- Dossier `skills/` : description des skills d'aide autour de Forge.

## Forge E-Learning 0.1 — 7 novembre 2026 (étiquette `v0.1`)

- Dépôt Forge_E-Learning : migration du code de QuizForge, ExoForge et de l'analyse des résultats ; chemins communs ; identité visuelle (logos, icônes et bandeaux jour / nuit).
- Exemples QuizForge et ExoForge ; données d'exemple entièrement fictives (bac à sable Moodle, promotions générées).
- Style générique par rôles de couleur ; profils `Delattre` et `Ecole1`.
- Premiers modes d'emploi ; contrôle du dépôt avant commit (`scripts/commun/verifier_depot.py`).
