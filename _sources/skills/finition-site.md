# Finition du dépôt et du site

**État : existe.** Adapté d'un skill de finition de documentation technique ; la version adaptée à Forge est dans `skills/finition-site/SKILL.md`.

## Utilité

Préparer le dépôt et le site avant une version publique : rien de spécifique en ligne (établissement, personne, chemin local), ton éditorial sans notes de chantier, arborescence propre, README et page d'accueil à jour, état des outils, construction du site sans avertissement, contrôle des modes jour et nuit, branche `gh-pages` qui ne contient que le site construit.

## Entrées et sorties

| Entrées | Sorties |
| --- | --- |
| le dépôt (fichiers suivis et historique), les notes d'état des outils | fichiers corrigés en place (sans commit), pages du site, rapport de préparation (fait, pas fait, décisions à prendre, fichiers modifiés), commandes de construction |

## Limites

- Le skill ne commite rien, ne pousse rien et ne réécrit pas l'historique : il liste ce qui s'y trouve et les options.
- Il ne retouche pas une image : une capture qui montre une information spécifique est listée pour être refaite.
- Il ne change aucun comportement du code : seules les docstrings et les commentaires sont mis au propre, contrôle de l'arbre syntaxique à l'appui.
