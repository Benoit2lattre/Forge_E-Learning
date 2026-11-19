# Atelier Forge

Mode d'emploi illustré : [outils/atelier](../../outils/atelier/README.md).

Une page dans le navigateur qui lance les outils Forge par boutons et listes, sans ligne de commande.

**Lancer** : double-clic sur `Forge.bat`, à la racine du dépôt. Une fenêtre de commande s'ouvre (la laisser ouverte) et la page s'affiche dans le navigateur. Sans le .bat : `python scripts/forge/forge.py` (`--port`, `--sans-navigateur`).

**Fermer** : bouton « Quitter » de la page, ou fermer l'onglet (l'atelier s'arrête quelques secondes après, sauf si une tâche tourne encore : il attend sa fin).

## Ce que fait l'atelier

- Chaque bouton lance une commande Forge existante (ici `scripts/exoforge/build.py`) dans un sous-processus ; son journal s'affiche en bas de la page, avec la durée, l'état et un bouton « Arrêter ». Les tâches de la séance restent dans la liste ; le journal de toutes les tâches est gardé dans `data/_atelier/journal.jsonl`.
- **Cours** (`cours.py`) : un cours (`data/cours/<nom>/cours.yaml`, format `forge-cours/1`) désigne ses sources sans les déplacer et porte ses déclinaisons (école, campus, parcours, niveau, codes) et leurs éditions (année, promo, groupes). Le sélecteur en haut de la page limite les listes des écrans au cours choisi ; ce qu'on crée lui est ajouté (capsules et classeurs dans son arborescence standard s'il en a une). Écran Cours : fiche, documents, sources, déclinaisons et éditions, objets « à ranger ». En ligne de commande : `python scripts/forge/cours.py liste | montrer | verifier | proposer`.
- **Accueil** : état de l'ordinateur (Python, modules, PowerPoint, voix Piper téléchargées) et ce que chaque élément permet.
- **Exercices (ExoForge)** : fiches des exemples (`outils/exoforge/exemples`) et de `data/exoforge` ; Construire (avec le profil de la fiche ou un autre), Essayer (valeurs fixes) ou Valeurs tirées dans un nouvel onglet, Paquet SCORM (montré dans l'explorateur), Fiche ; « Autre fiche… » choisit une fiche ailleurs avec le dialogue de fichiers de Windows.
- **Capsules (CapsuleForge)** : les capsules de `data/capsuleforge`. Pour la capsule choisie : résumé (parties, sections, durée, langues, remarques de `verifier`), puis cinq étapes — 1. Sources (reprendre chaque diaporama cité, avec ou sans PowerPoint ; le fichier introuvable se retrouve une fois par « Parcourir… » et l'atelier s'en souvient ; importer une vidéo dans une section existante ou nouvelle), 2. Texte dit (transcrire, relire), 3. Traduction (langue, pré-remplissage, relire la traduction, importer), 4. Voix de synthèse (langue, moteur, voix, vitesse), 5. Construire (vérifier, construire avec ou sans paquets SCORM 1.2 ou 2004). Les écrans de relecture s'ouvrent dans un nouvel onglet ; « Enregistrer et quitter » y termine la tâche. Le tableau des sections montre l'état de chacune (diapositives reprises, images, texte dit, relu, texte et voix par langue, questions) ; cocher des sections limite la transcription et la voix à celles-ci. Une capsule écrite pour l'ancien lecteur se met à jour d'un bouton. « Nouvelle capsule… » crée une capsule à partir d'un diaporama (plan proposé : une partie par section PowerPoint, des sections de quelques minutes d'après le minutage, une par diapositive ou une seule ; reprise du diaporama enchaînée si on le souhaite) ou vide, pour y importer ensuite une vidéo.
- **Questions (QuizForge)** : classeurs de `data/quizforge` et du modèle ; Ouvrir dans Excel, Valider (points d'écriture, score au hasard), Convertir pour Moodle (catégorie, nom, tags, XML ou GIFT, réparation, plan du quiz d'une séance avec l'effectif), Sorties ; Nouveau classeur (modèle avec exemples ou vide, ouvert dans Excel), Autre classeur (ajouté à la liste), Réunir un classeur et sa traduction.
- **Bilans (DiagForge)** : dossiers d'exports Moodle de `data/diagforge` et des exemples `donnees/diagforge` ; Faire le bilan (export XML des questions et liste des étudiants repérés dans le dossier ou choisis, autres exports du même test, tentatives, profil, sans images) ; la fiche du professeur s'ouvre à la fin ; Classeur, Dossier.
- **Filmer l'écran** (écran Capsules) : écran, micro, caméra et section choisis dans des listes (`capsuleforge filmer --appareils`), panneau d'enregistrement Pause / Reprendre / Fin (lignes « pause » et « fin » envoyées à la commande) ; raccourcis Ctrl+Maj+P et Ctrl+Maj+F gardés. Nouvelle capsule aussi à partir d'une manipulation enregistrée ou d'un projet ActivePresenter (mise à jour pour le lecteur actuel enchaînée) ; ancien éditeur pour les capsules de l'ancien lecteur.
- **Réglages** : apparence (jour, nuit ou comme Windows ; aussi par le bouton ☾ / ☀ en haut de la page), profil d'établissement proposé d'office, classeurs ajoutés, chemins des diaporamas retrouvés (à oublier), dossier du journal.
- Les écrans suivent l'ordre des outils, du plus simple au plus complet : Questions (QuizForge), Exercices (ExoForge), Capsules (CapsuleForge, qui utilise les deux premiers), Bilans (DiagForge, qui analyse les trois autres).

## Sécurité

Le serveur n'écoute que sur cet ordinateur (127.0.0.1, port 8770 ou le suivant libre), refuse les requêtes venues d'un autre site et demande un jeton tiré au lancement (donné dans l'adresse ouverte par `Forge.bat`). Il ne lance que des actions connues, avec des options vérifiées : jamais une ligne de commande libre.

Licence : GPL v3.
