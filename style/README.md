# style

Style générique, commun à tous les outils de la Forge. Il ne contient aucune couleur d'établissement : chaque élément passe par des **rôles** (à quoi sert la couleur), et un profil ([profils/](../profils/README.md)) donne la couleur de chaque rôle.

| Dossier | Contenu | Utilisé par |
|---|---|---|
| `web/exercice.css` | feuille de style des exercices interactifs, injectée dans chaque page à la construction | ExoForge |
| `latex/couleurs_roles.tex` | commandes LaTeX par rôle (`\TDef`, `\TPro`, `\TRes`, `\TAtt`, `\TMC`, `\TExg`) | ExoForge, IguanaTex / PowerPoint |
| `latex/ppt_commandes.tex` | commandes mathématiques communes (préambule des formules) | ExoForge, IguanaTex / PowerPoint |

## Rôles de couleur des exercices (web)

Dans `profil.yaml`, `charte.roles` associe un rôle à une couleur de `charte.couleurs` (ou à un code hexadécimal). Le rôle `principal_clair` devient la variable CSS `--principal-clair`. Un rôle absent garde la valeur de `web/exercice.css`.

| Rôle (`charte.roles`) | Variable CSS | Usage | Valeur générique |
|---|---|---|---|
| `principal` | `--principal` | bandeau, titres des cartes, boutons, cadre de l'encadré | `#470A68` |
| `principal_clair` | `--principal-clair` | fond doux : option cochée, encadré, message d'information | `#F4EEF8` |
| `succes` / `succes_clair` | `--succes` / `--succes-clair` | réponse juste (bord / fond) | `#2E7D32` / `#E8F5E9` |
| `erreur` / `erreur_clair` | `--erreur` / `--erreur-clair` | réponse fausse (bord / fond) | `#B3161B` / `#FDECEC` |
| `texte` | `--texte` | texte courant | `#1D1D1D` |
| `texte_secondaire` | `--texte-secondaire` | légendes, compteurs d'essais, pied de page | `#5F6368` |
| `fond` / `carte` / `bord` | `--fond` / `--carte` / `--bord` | fond de page, fond des panneaux, filets | `#FAFAFB` / `#FFFFFF` / `#DADCE0` |
| `focus` | `--focus` | élément montré pendant la lecture audio | `#FFCD00` |
| `graphique` | `--graphique` | courbes des graphiques générés | `#470A68` |
| `points` | `--points` | points et repères des graphiques | `#B3161B` |

Le profil choisit aussi les polices : `charte.police_titres`, `charte.police_texte` et `charte.polices_url` (chargement en ligne).

## Rôles de couleur des formules (LaTeX)

Chaque jeu de couleurs d'un profil (ex. `profils/Ecole1/Ecole1_ColorScheme.tex`) définit six couleurs de rôle avec `\colorlet{role…}{…}`, puis se termine par `\input{couleurs_roles}`. Une formule écrite avec ces commandes garde le même sens d'un profil à l'autre ; seule la couleur change.

| Commande | Couleur | Usage |
|---|---|---|
| `\TDef{…}` | `roleDef` | rappel, définition, donnée connue |
| `\TPro{…}` | `rolePro` | proposition, modèle en construction, options d'une question |
| `\TRes{…}` | `roleRes` | résultat, formule à retenir |
| `\TAtt{…}` | `roleAtt` | attention, erreur, piège |
| `\TMC{…}` | `roleMC` | couleur principale (équation en titre) |
| `\TExg{…}` | `roleExg` | mise en exergue : résultat encadré (mode math) |

Les anciennes commandes de couleur (`\TR`, `\TV`, `\TB`…) restent définies dans chaque jeu pour les diapositives existantes, mais leur couleur dépend du jeu : `\TV` est violet dans Ecole1 et vert dans Delattre. Pour un nouveau contenu, préférer les commandes de rôle, ou `\TVi` / `\TVe` (violet / vert dans tous les jeux).
