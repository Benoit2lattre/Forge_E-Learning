# Atelier Forge

Une page dans le navigateur qui lance les outils Forge par boutons et listes, sans ligne de commande.

**Lancer** : double-clic sur `Forge.bat`, à la racine du dépôt. Une fenêtre de commande s'ouvre (la laisser ouverte) et la page s'affiche dans le navigateur. Sans le .bat : `python scripts/forge/forge.py` (`--port`, `--sans-navigateur`).

**Fermer** : bouton « Quitter » de la page, ou fermer l'onglet (l'atelier s'arrête quelques secondes après, sauf si une tâche tourne encore : il attend sa fin).

## Ce que fait l'atelier

- Chaque bouton lance une commande Forge existante (ici `scripts/exoforge/build.py`) dans un sous-processus ; son journal s'affiche en bas de la page, avec la durée, l'état et un bouton « Arrêter ». Les tâches de la séance restent dans la liste ; le journal de toutes les tâches est gardé dans `data/_atelier/journal.jsonl`.
- **Accueil** : état de l'ordinateur (Python, modules, PowerPoint, voix Piper téléchargées) et ce que chaque élément permet.
- **Exercices (ExoForge)** : fiches des exemples (`outils/exoforge/exemples`) et de `data/exoforge` ; Construire (avec le profil de la fiche ou un autre), Essayer (valeurs fixes) ou Valeurs tirées dans un nouvel onglet, Paquet SCORM (montré dans l'explorateur), Fiche ; « Autre fiche… » choisit une fiche ailleurs avec le dialogue de fichiers de Windows.
- **Capsules (CapsuleForge)** : les capsules de `data/capsuleforge`. Pour la capsule choisie : résumé (parties, sections, durée, langues, remarques de `verifier`), puis cinq étapes — 1. Sources (reprendre chaque diaporama cité, avec ou sans PowerPoint ; le fichier introuvable se retrouve une fois par « Parcourir… » et l'atelier s'en souvient ; importer une vidéo dans une section existante ou nouvelle), 2. Texte dit (transcrire, relire), 3. Traduction (langue, pré-remplissage, relire la traduction, importer), 4. Voix de synthèse (langue, moteur, voix, vitesse), 5. Construire (vérifier, construire avec ou sans paquets SCORM 1.2 ou 2004). Les écrans de relecture s'ouvrent dans un nouvel onglet ; « Enregistrer et quitter » y termine la tâche. Le tableau des sections montre l'état de chacune (diapositives reprises, images, texte dit, relu, texte et voix par langue, questions) ; cocher des sections limite la transcription et la voix à celles-ci. Une capsule écrite pour l'ancien lecteur se met à jour d'un bouton. « Nouvelle capsule… » crée une capsule à partir d'un diaporama (plan proposé : une partie par section PowerPoint, des sections de quelques minutes d'après le minutage, une par diapositive ou une seule ; reprise du diaporama enchaînée si on le souhaite) ou vide, pour y importer ensuite une vidéo.
- Les écrans suivent l'ordre des outils, du plus simple au plus complet : Questions (QuizForge), Exercices (ExoForge), Capsules (CapsuleForge, qui utilise les deux premiers), Bilans (DiagForge, qui analyse les trois autres). Questions, Bilans et Réglages arrivent au lot suivant.

## Sécurité

Le serveur n'écoute que sur cet ordinateur (127.0.0.1, port 8770 ou le suivant libre), refuse les requêtes venues d'un autre site et demande un jeton tiré au lancement (donné dans l'adresse ouverte par `Forge.bat`). Il ne lance que des actions connues, avec des options vérifiées : jamais une ligne de commande libre.

Licence : GPL v3.
