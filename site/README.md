# site

Configuration et pages propres du site de documentation de Forge E-Learning (Jupyter Book 1.x, moteur Sphinx).

La racine du livre est la racine du dépôt : les modes d'emploi (`outils/`), la bibliographie (`reference/`), le style, les profils et les skills sont lus là où ils vivent, sans copie. Ce dossier contient la configuration (`_config.yml`), le sommaire (`_toc.yml`), les pages propres au site (accueil, pourquoi, état des outils, prochaines étapes, état de rédaction, référence API), la feuille de style (`_static_site/forge.css`) et les dépendances de construction (`requirements.txt`).

Construction, depuis la racine du dépôt :

```bash
uv pip install -r site/requirements.txt
jupyter-book build . --config site/_config.yml --toc site/_toc.yml --path-output site
```

Sortie : `site/_build/html/` (non suivi). La référence API est générée pendant la construction (`site/api/`, effacé ensuite).
