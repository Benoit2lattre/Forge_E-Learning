# Atelier Forge

Une page dans le navigateur qui lance les outils Forge par boutons et listes, sans ligne de commande.

**Lancer** : double-clic sur `Forge.bat`, à la racine du dépôt. Une fenêtre de commande s'ouvre (la laisser ouverte) et la page s'affiche dans le navigateur. Sans le .bat : `python scripts/forge/forge.py` (`--port`, `--sans-navigateur`).

**Fermer** : bouton « Quitter » de la page, ou fermer l'onglet (l'atelier s'arrête quelques secondes après, sauf si une tâche tourne encore : il attend sa fin).

## Ce que fait l'atelier

- Chaque bouton lance une commande Forge existante (ici `scripts/exoforge/build.py`) dans un sous-processus ; son journal s'affiche en bas de la page, avec la durée, l'état et un bouton « Arrêter ». Les tâches de la séance restent dans la liste ; le journal de toutes les tâches est gardé dans `data/_atelier/journal.jsonl`.
- **Accueil** : état de l'ordinateur (Python, modules, PowerPoint, voix Piper téléchargées) et ce que chaque élément permet.
- **Exercices (ExoForge)** : fiches des exemples (`outils/exoforge/exemples`) et de `data/exoforge` ; Construire (avec le profil de la fiche ou un autre), Essayer (valeurs fixes) ou Valeurs tirées dans un nouvel onglet, Paquet SCORM (montré dans l'explorateur), Fiche ; « Autre fiche… » choisit une fiche ailleurs avec le dialogue de fichiers de Windows.
- Les écrans suivent l'ordre des outils, du plus simple au plus complet : Questions (QuizForge), Exercices (ExoForge), Capsules (CapsuleForge, qui utilise les deux premiers), Bilans (DiagForge, qui analyse les trois autres). Questions, Capsules, Bilans et Réglages arrivent aux lots suivants.

## Sécurité

Le serveur n'écoute que sur cet ordinateur (127.0.0.1, port 8770 ou le suivant libre), refuse les requêtes venues d'un autre site et demande un jeton tiré au lancement (donné dans l'adresse ouverte par `Forge.bat`). Il ne lance que des actions connues, avec des options vérifiées : jamais une ligne de commande libre.

Licence : GPL v3.
