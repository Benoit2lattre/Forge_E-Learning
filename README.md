<picture>
  <source media="(prefers-color-scheme: dark)" srcset="_images/forge_e-learning_bandeau_nuit.png">
  <img alt="Forge E-Learning" src="_images/forge_e-learning_bandeau_jour.png">
</picture>

# Forge E-Learning — site de documentation

Cette branche (`gh-pages`) ne contient que le **site construit** de [Forge E-Learning](https://github.com/Benoit2lattre/Forge_E-Learning) : des pages HTML statiques, sans le code des outils. Elle est **régénérée automatiquement** à partir de la branche `main` et réécrite à chaque publication : ne la modifiez pas à la main, vos changements seraient perdus.

Forge E-Learning réunit des outils libres pour passer d'un cours existant à des activités Moodle : QuizForge (questions), ExoForge (exercices guidés), DiagForge (analyse des résultats) et CapsuleForge (chapitres de cours interactifs), avec une bibliographie de 250 références et 197 fiches de lecture. Auteur : Benoit Delattre.

## Récupérer le site

```bash
git clone --branch gh-pages --single-branch --depth 1 https://github.com/Benoit2lattre/Forge_E-Learning.git forge-site
```

Mise à jour : `git -C forge-site pull --depth 1` (ou supprimer le dossier et cloner à nouveau, la branche étant réécrite à chaque publication).

## Consulter ou diffuser le site

- **Consulter** : ouvrir `index.html` dans un navigateur ; le site fonctionne aussi depuis le disque, sans serveur.
- **Diffuser** sur un serveur interne : copier le contenu du dossier, **sans** le sous-dossier `.git/`, à la racine d'un site web statique.
- **Télécharger une page** : le bouton de téléchargement de chaque page donne sa source (`.md`) ; l'impression du navigateur donne un PDF.

## Le code et les modes d'emploi

Le code, les exemples et la façon de construire ce site sont sur la branche `main` : voir son [README](https://github.com/Benoit2lattre/Forge_E-Learning#readme).

Licences : code sous GNU GPL v3 ; documentation et site sous CC BY-NC-SA 4.0.
