# AtelierForge

<p><img src="../../_static/identite/bandeaux/atelierforge_bandeau_jour.png#gh-light-mode-only" alt="AtelierForge" class="only-light" width="100%"><img src="../../_static/identite/bandeaux/atelierforge_bandeau_nuit.png#gh-dark-mode-only" alt="AtelierForge" class="only-dark" width="100%"></p>

AtelierForge lance toute la suite Forge depuis une page du navigateur, par boutons et listes : rien à taper, ni commande ni chemin. Il ne refait aucun calcul : chaque bouton lance la commande de l'outil (QuizForge, ExoForge, CapsuleForge, DiagForge), et son journal s'affiche en bas de la page.

Statut : version 0.5, essayée sous Windows sur les cours de l'auteur. Les commandes restent utilisables seules (voir le mode d'emploi de chaque outil).

## Lancer et fermer

Double-clic sur `Forge.bat`, à la racine du dépôt : une fenêtre de commande s'ouvre (la laisser ouverte) et la page s'affiche dans le navigateur. Pour fermer : bouton « Quitter », ou fermer l'onglet (l'atelier s'arrête quelques secondes après, sauf si une tâche tourne encore : il attend sa fin).

Sans le fichier `.bat` : `python scripts/forge/forge.py` (options `--port`, `--sans-navigateur`).

![L'accueil de l'atelier : les quatre outils et l'état de l'ordinateur](../../_static/captures/atelier/accueil.png)

L'**accueil** montre l'état de l'ordinateur : Python, les modules utiles (et ce que chacun permet), PowerPoint, les voix de synthèse téléchargées. Un élément facultatif absent n'empêche que ce qu'il sert à faire.

Les écrans suivent l'ordre des outils, du plus simple au plus complet, après l'écran Cours : Questions, Exercices, Capsules (qui utilise les deux premiers), Bilans (qui analyse les trois autres), puis Réglages. Le **panneau des tâches**, en bas, est commun à tous les écrans : chaque tâche lancée y garde son journal, son état, sa durée, un bouton « Arrêter » tant qu'elle tourne et, à la fin, les boutons utiles (essayer l'exercice, ouvrir le lecteur, la fiche du professeur, montrer le paquet SCORM…). Toutes les tâches sont aussi notées dans `data/_atelier/journal.jsonl`.

« Montrer » ouvre l'explorateur sur un fichier ; « Ouvrir » ouvre un fichier avec son programme (Excel, navigateur). La fenêtre est mise au premier plan ; le bouton reste grisé quelques secondes, pour ne pas en ouvrir plusieurs. Les fichiers se choisissent par « Parcourir… », qui ouvre le dialogue de fichiers de Windows (il peut s'ouvrir derrière le navigateur).

## Cours

Un **cours** regroupe ce qui sert pour lui dans les quatre outils (classeurs, fiches d'exercices, capsules, diaporamas, dossiers d'exports) **sans rien déplacer** : il désigne des dossiers et des fichiers. Il a des **déclinaisons** (le cours dans une école : campus, parcours, niveau, codes de l'enseignement et du bloc d'enseignements, langue) et chaque déclinaison des **éditions** (une année : promo, groupes et campus de chacun). Tout tient dans un fichier, `data/cours/<nom>/cours.yaml`, que l'écran Cours remplit par formulaire.

![L'écran Cours : fiche du cours de démonstration, documents et sources](../../_static/captures/atelier/cours.png)

Le sélecteur **Cours**, en haut de la page, choisit un cours (et une édition) : les écrans Questions, Exercices, Capsules et Bilans n'affichent alors que ce qui lui appartient, et ce qu'on y crée (nouvelle capsule, nouveau classeur) lui est ajouté. « Tous les cours » montre tout ; « Sans cours » montre ce qu'aucun cours ne désigne.

L'écran **Cours** montre la fiche du cours choisi (titre, domaine, langues, étiquettes Moodle, description, objectifs, compétences, catalogue d'erreurs types, cours dont il est dérivé, cours qu'il inclut comme séances), ses documents (syllabus, plan, fiche de compétences : ouverts d'un clic), ses sources, ses déclinaisons et leurs éditions.

- **Nouveau cours…** : un titre et un nom court (`mef`, `stat` : il sert de nom de dossier, d'où sa brièveté, à cause de la longueur des chemins sous Windows). « Chercher dans data/ » propose les dossiers et fichiers qui portent ce nom ; on coche ce qui convient. Pour partir de rien, l'arborescence standard crée `documents/` (un syllabus et une fiche de compétences à remplir), `diaporamas/`, `questions/`, `exercices/` et `capsules/` sous `data/cours/<nom>/`.
- **Nouvelle déclinaison…** : l'école (profil d'établissement, ou une autre), ses campus, le parcours, la formation, le niveau, la modalité (FISE, FISA, FISEA, FC pour un diplôme d'ingénieur) et le numéro RNCP, puis les codes de l'enseignement et du bloc, sous les noms de l'école (« Module » et « UE », par exemple) ; quand le profil donne le gabarit des codes, on saisit les abrégés (`MEC`, `TR`) et l'atelier écrit les codes (`MEC-L3`, `MEC-L3-TR`). Les **variantes** des capsules (`ecole1, aero` pour la déclinaison, `2026` en plus pour l'édition) disent pour quel public elles sont construites : ce qui ne vaut que pour lui (un renvoi au reste du cursus, une phrase « chez notre partenaire industriel ») n'apparaît que là. Tout ce que l'atelier propose vient du profil de l'école (voir [Formations, codes et promotions](../../profils/README.md#formations-codes-et-promotions)). Puis les langues d'enseignement (une déclinaison peut être bilingue : ses groupes français et anglais restent ensemble). « Modifier la déclinaison… » change tout sauf le nom court ; une déclinaison sans édition se supprime.
- **Nouvelle édition…** : l'année, la promo (proposée d'après le gabarit du profil : P2029 pour un L3 de 2026-2027 suivi d'un master) et les groupes avec leur campus et, pour une déclinaison bilingue, leur langue (`Aero1:Nord:fr, Aero3:Sud:en`) ; « Modifier » change la promo et les groupes ; une nouvelle édition reprend la précédente (séances décalées d'un an) et reçoit ses propres dossiers `exports/` et `bilans/`. Chaque déclinaison a son édition « en cours » (la dernière créée, ou celle choisie par « En cours ») : deux parcours donnés la même année ont chacun la leur.
- **À ranger…** liste les classeurs, fiches, capsules et dossiers d'exports qu'aucun cours ne désigne ; « Ranger » les ajoute au cours choisi.

**Ce que l'édition choisie apporte aux autres écrans** : le profil de l'école proposé d'office (Questions, Exercices, Bilans) ; dans « Convertir… », les étiquettes du cours et les codes de l'enseignement et du bloc ajoutés aux tags, la catégorie Moodle et l'effectif de l'édition, et la prochaine séance proposée pour le plan du quiz (avec sa date et son titre dans le plan) ; dans Bilans, le dossier des exports de l'édition (un dossier par test : le bilan s'écrit à côté) ; sur l'accueil, le cours choisi et sa prochaine séance. Les séances (« n ; date ; titre », une par ligne) et l'effectif se donnent dans « Modifier » de l'édition.

**Versions et registre.** Avec un cours choisi, chaque « Convertir… » produit une version rangée dans l'édition (`quiz/<classeur>/S03_v2/`, fichiers au nom explicite), chaque « Construire » d'un exercice range son paquet SCORM (`exercices/<id>/v2/`), et chaque « Construire » d'une capsule la range habillée pour l'édition (`capsules/<capsule>/v1/`) ; rien n'est écrasé, et refaire sans rien changer ne crée pas de version. Les écrans Questions et Exercices montrent la dernière version et son état (« Paquet SCORM » montre alors celui de la dernière version) ; « Registre » (dans Questions, ou pour chaque édition dans l'écran Cours) liste les versions : état (convertie, importée dans Moodle, passée, bilan fait, abandonnée), nom du test Moodle, remarques, fiche du bilan, dossier. Une version faite au niveau du cours (extrait commun) se rattache aux éditions qui l'utilisent. Le bilan DiagForge reconnaît la version du test d'après ses questions et s'inscrit au registre. Les commandes reçoivent `--cours cours:déclinaison/édition` ; ce qu'on choisit dans un formulaire l'emporte.

![Le registre d'une édition : la version d'un quiz, son état et le test Moodle](../../_static/captures/atelier/registre.png)

**Cours de démonstration.** `donnees/cours/traction/` est un cours fictif complet, sans aucune donnée réelle : une déclinaison bilingue pour l'école fictive Ecole1 (campus Nord et Sud), une édition 2026 avec trois groupes et trois séances, des sources publiées (classeur modèle, exercice `premier_exercice`, exports `donnees/diagforge/promotion_groupes`) et un registre avec une version de quiz. Choisissez-le en haut de la page pour essayer l'écran Cours et le registre.

En ligne de commande : `python scripts/forge/cours.py liste`, `montrer <nom>`, `verifier [<nom>]`, `proposer <nom>`. Formats : [cours.yaml](FORMAT_cours.md), [registre.yaml et version.yaml](FORMAT_registre.md).

## Questions (QuizForge)

![L'écran Questions : classeurs, validation et conversion pour Moodle](../../_static/captures/atelier/questions.png)

Les classeurs de `data/quizforge`, ceux ajoutés par « Autre classeur… » et les classeurs d'exemple. Pour chacun : Ouvrir dans Excel, Valider (points d'écriture à vérifier, score au hasard ; rien n'est écrit), Convertir… (catégorie Moodle, nom, tags, Moodle XML ou GIFT, réparation des textes, plan du quiz d'une séance avec l'effectif de la promotion), Sorties. « Nouveau classeur… » crée un classeur à partir du modèle (avec exemples ou vide) et l'ouvre dans Excel ; « Réunir un classeur et sa traduction… » écrit un classeur bilingue.

## Exercices (ExoForge)

![L'écran Exercices : fiches, construction, essai](../../_static/captures/atelier/exercices.png)

Les fiches des exemples et de `data/exoforge`. Construire (avec le profil de la fiche ou un autre) produit l'exercice et son paquet SCORM 1.2 ; Essayer l'ouvre avec des valeurs fixes, Valeurs tirées avec de nouvelles valeurs à chaque ouverture ; « fiche modifiée depuis » signale une construction en retard.

## Capsules (CapsuleForge)

![L'écran Capsules : état de la capsule section par section et les cinq étapes de la préparation](../../_static/captures/atelier/capsules.png)

On choisit la capsule ; son résumé (parties, sections, durée, langues, remarques de vérification) et cinq étapes s'affichent :

1. **Sources** : reprendre chaque diaporama cité par les sections (avec PowerPoint pour les images, ou sans) — l'atelier le retrouve dans `data/capsuleforge` ou dans le dossier `e_learning` voisin du dépôt, sinon on le désigne une fois ; importer une vidéo ; filmer l'écran.
2. **Texte dit** : transcrire, puis relire phrase par phrase avec le son et l'image (l'écran de relecture s'ouvre dans un onglet).
3. **Traduction** : langue, pré-remplissage (à la main, Argos hors ligne, DeepL), relire la traduction, l'importer dans la capsule.
4. **Voix de synthèse** : langue, moteur, voix, vitesse.
5. **Construire** : vérifier, construire le lecteur avec ou sans paquets SCORM (une capsule, une par partie, ou les deux ; SCORM 1.2 conseillé pour Moodle). Avec un cours choisi en haut de la page, la capsule est habillée pour l'édition (charte et logo de l'école, écran d'accueil, pied de page, crédits, filigrane si l'édition le demande) et rangée comme version ; « Registre » en donne les versions (voir « Habiller la capsule pour une édition » dans le [mode d'emploi de CapsuleForge](../capsuleforge/README.md)). Les PDF cochés dans la carte 6 sont refaits et joints aux paquets.
6. **PDF** : à partir du lecteur construit, sans le reconstruire, un document à imprimer (diapositives seules, avec le texte dit, le texte des diapositives ou les deux ; place pour les notes en marge ou dessous ; langue au choix). Chaque réglage donne sa version, au nom explicite, que « Montrer » ouvre ; la case « dans le paquet » la joint aux paquets SCORM à la prochaine construction (une par langue), et le bouton « PDF » du lecteur ouvre celle de la langue des sous-titres.

Le tableau des sections, sous les étapes, donne l'état de chacune : diapositives reprises, images, texte dit, relu, texte et voix par langue, questions. Cocher des sections limite la transcription et la voix à celles-ci.

**Nouvelle capsule…** part d'un diaporama (plan proposé : une partie par section PowerPoint, des sections de quelques minutes d'après le minutage, titrées par leur première diapositive ; la reprise du diaporama peut s'enchaîner), d'une manipulation enregistrée dans un logiciel (chaque clic et chaque saisie deviennent un pas, avec une image ; pas de son : la voix se met ensuite sur les pas, ou on filme l'écran), d'un projet ActivePresenter, ou de rien (pour une vidéo ou un film d'écran ensuite). Une capsule écrite pour l'ancien lecteur se met à jour d'un bouton ; elle garde l'accès à l'ancien éditeur.

![Filmer l'écran : le panneau d'enregistrement](../../_static/captures/atelier/filmer.png)

**Filmer l'écran…** demande l'écran, le micro, la caméra (médaillon) et la section, puis filme après un compte à rebours de 3 s. Le panneau d'enregistrement donne Pause ou Reprendre et Fin ; dans n'importe quelle fenêtre, Ctrl+Maj+P et Ctrl+Maj+F font de même. À la fin, la vidéo est importée dans la section, découpée en pas aux silences. Le bouton **Tester** à côté du micro l'écoute 4 s et dit si la voix est assez forte (sinon : rapprocher le micro ou monter son volume dans Windows ; une voix faible est de toute façon relevée à l'import). Pendant un enregistrement (film ou manipulation), un panneau donne les boutons Pause ou Reprendre, Fin et, pour une manipulation, Nouvelle étape (les clics faits pour revenir à l'atelier ne deviennent pas des pas) ; « Arrêter » termine aussi l'enregistrement en le gardant, un second « Arrêter » abandonne tout. Si une caméra a été filmée, la carte « 5. Construire » propose la place (ou « pas de caméo »), la taille et la forme du médaillon (caméo) ; l'élève peut le masquer dans le lecteur.

## Bilans (DiagForge)

![L'écran Bilans : dossiers d'exports Moodle et bilan](../../_static/captures/atelier/bilans.png)

Les dossiers d'exports Moodle de `data/diagforge` et les exemples. « Faire le bilan… » reprend l'export XML des questions et la liste des étudiants trouvés dans le dossier (ou choisis), et accepte d'autres exports du même test ; la tentative retenue, le profil et « sans images » se règlent dans la barre de l'écran. À la fin, la fiche du professeur s'ouvre ; le classeur d'analyse est à côté.

## Réglages et apparence

L'écran Réglages garde dans `data/_atelier/reglages.json` : l'apparence (jour, nuit ou comme Windows ; aussi par le bouton ☾ / ☀ en haut de la page), le profil d'établissement proposé d'office, les classeurs ajoutés et les chemins des diaporamas retrouvés. Chaque classeur et chaque diaporama a son bouton « Oublier », et un chemin qui n'existe plus sur cet ordinateur est marqué « introuvable ».

![L'apparence nuit](../../_static/captures/atelier/capsules_nuit.png)

## Sécurité

Le serveur n'écoute que sur cet ordinateur (127.0.0.1, port 8770 ou le suivant libre), refuse les requêtes venues d'un autre site et demande un jeton tiré au lancement. Il ne lance que des actions connues, avec des options vérifiées : jamais une ligne de commande libre. Code : [`scripts/forge/`](https://github.com/Benoit2lattre/Forge_E-Learning/tree/main/scripts/forge).
