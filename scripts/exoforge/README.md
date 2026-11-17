# scripts/exoforge

Code d'ExoForge (exercices interactifs SCORM). Mode d'emploi : [outils/exoforge](../../outils/exoforge/README.md).

| Fichier | Rôle |
| --- | --- |
| `build.py` | point d'entrée : lit la fiche, choisit le profil, applique sa charte |
| `generique.py` | vérifie la fiche, prépare LaTeX et médias, écrit la page et le paquet SCORM 1.2 |
| `latex_macros.py` | lit les macros et couleurs des fichiers LaTeX (IguanaTeX) pour MathJax |
| `moteur/exercice.html` | le moteur de l'exercice (JavaScript), gabarit de la page ; sa feuille de style est [`style/web/exercice.css`](../../style/web/exercice.css) |
| `moteur/vendor/` | MathJax embarqué (fonctionne hors ligne ; licence Apache 2.0) |

Les chemins du dépôt (profils, style, médias privés, sorties) sont centralisés dans [`scripts/commun/chemins.py`](../commun/chemins.py).
