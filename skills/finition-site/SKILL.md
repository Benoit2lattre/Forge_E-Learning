---
name: finition-site
description: Prépare le dépôt Forge E-Learning et son site (Jupyter Book) avant une version publique — rien de spécifique en ligne, ton éditorial, état des outils, docstrings pour la référence API, construction du site en modes jour et nuit, branche gh-pages préparée, rapport. À utiliser quand l'auteur parle de « remettre au propre », publier, annoncer une version ou vérifier le site de Forge.
---

# Finition du dépôt et du site Forge E-Learning

Destinataire final : un collègue enseignant qui découvre Forge par son dépôt ou son site, sans avoir suivi le travail. Il doit comprendre ce que fait chaque outil, l'essayer et savoir ce qui est mûr ou non.

Principe : **auditer, corriger ce qui est sûr, lister le reste**. Rien n'est commité, poussé ni supprimé : l'auteur relit et commite lui-même.

## Règles

- Seules les commandes git de lecture (`status`, `diff`, `log`, `grep`, `ls-files`, `show`).
- Aucune suppression : un fichier à retirer est déplacé dans `_pilotage/_a_supprimer/` (non suivi) et listé.
- Ne pas toucher aux données personnelles (`data/`), aux anciens fichiers, aux sorties construites (`dist/`), ni aux fiches, classeurs et diaporamas de l'auteur.
- Ne change aucun comportement du code : pour chaque fichier Python modifié, l'arbre syntaxique sans docstrings doit rester identique, puis `python -m py_compile` et les commandes de vérification du README.
- Terminologie : DiagForge, CapsuleForge… ; « système tutoriel intelligent » ; abréviations françaises.
- Typographie française (espace insécable avant ; : ! ? et à l'intérieur des guillemets).

## Déroulé

1. **Cadrage** : lire les notes d'état des outils, le README, les modes d'emploi d'`outils/`, `reference/README.md`, `style/`, `profils/`, l'historique (`git log --oneline`). Écrire le rapport au fil de l'eau dans `_pilotage/`.
2. **Rien de spécifique en ligne** : chercher dans tous les fichiers suivis (noms de fichiers, commentaires, docstrings, exemples, métadonnées, texte visible dans les images) les noms d'établissement, de client, de personne autre que l'auteur, de vrais fichiers de cours, les chemins locaux, le nom de la machine, les adresses de courriel, les noms d'étudiants. Remplacer par des termes neutres (« diaporama source », « École 1 »). Les correspondances dans des fichiers binaires ou minifiés sont souvent fortuites : vérifier sans modifier. Une image qui montre une information spécifique est listée pour être refaite. Auditer aussi l'historique (`git log --all -G…`, messages de commit) et présenter les options (publier tel quel, historique neuf, réécriture ciblée) sans rien réécrire.
3. **État des outils** : pour chaque outil, ce qui est essayé en conditions réelles, livré sans essai, manquant, et ses limites ; numéros de version proposés et justifiés ; journal des versions et texte d'annonce.
4. **Site** : Jupyter Book 1.x (moteur Sphinx), configuration dans `site/`, racine du livre = racine du dépôt (les modes d'emploi et la bibliographie sont lus en place, sans copie). Logo jour / nuit du thème, classes `only-light` / `only-dark` pour icônes et bandeaux, bandeau d'annonce aux couleurs Forge, bouton de téléchargement des pages. Dans les README affichés par GitHub : `<picture>` avec `prefers-color-scheme`. Construire, corriger les avertissements, contrôler visuellement les deux modes.
5. **Référence API** : docstrings et commentaires du code mis au propre (français, forme homogène, sans notes de chantier), référence générée par `sphinx-autoapi`.
6. **Pages de suivi** : état de rédaction des pages (rédigé, à compléter, à écrire, dépassé par le code, en vérifiant les modes d'emploi contre `--help`), prochaines étapes lisibles par un collègue.
7. **Branche `gh-pages`** : préparer `.github/workflows/` et `.github/README_site.md` sans les activer ; expliquer que l'action réécrit la branche à chaque push et ce qu'il faut régler sur GitHub (Pages, droits de l'action).
8. **Fin** : rapport complet (résumé, fait, pas fait, décisions à prendre par l'auteur, fichiers modifiés, ordre de relecture conseillé) et message court à l'auteur.

## Construction du site

```bash
uv pip install -r site/requirements.txt
jupyter-book build . --config site/_config.yml --toc site/_toc.yml --path-output site
```

Sortie : `site/_build/html/index.html`. Le build ne doit dépendre ni de `data/` ni d'aucun fichier privé.
