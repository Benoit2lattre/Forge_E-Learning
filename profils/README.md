# profils

Un profil adapte le style générique ([style/](../style/README.md)) et les réglages par défaut des outils à un établissement ou à un usage : couleurs par rôle, polices, jeu de couleurs LaTeX, barème Moodle, types de questions, langues. **Un dossier par profil** ; le nom du dossier est le nom du profil.

| Profil | Contenu |
|---|---|
| `Delattre/` | profil de l'auteur (formations professionnelles) : charte navy / sable, Lora + Karla ; profil par défaut |
| `Ecole1/` | établissement d'exemple (école d'ingénieurs fictive), à copier pour créer le profil de votre école |

Chaque dossier contient :

- `profil.yaml` : réglages QuizForge (barème, types, langues, tags) et charte (`charte.couleurs`, `charte.roles`, polices, `latex_couleurs`) ;
- le jeu de couleurs LaTeX nommé par `charte.latex_couleurs` (ex. `Ecole1_ColorScheme.tex`), qui se termine par `\input{couleurs_roles}` ;
- éventuellement les effets sonores nommés par `charte.sons` (chemins relatifs au dossier du profil).

## Choisir un profil

```bash
python scripts/exoforge/build.py outils/exoforge/exemples/fatigue_haigh_goodman -p Ecole1
python scripts/quizforge/quizforge.py profils            # liste des profils
python scripts/quizforge/quizforge.py profils Ecole1     # réglages d'un profil
```

`-p` accepte le nom, un alias (`alias:` dans `profil.yaml`) ou la première lettre quand elle ne désigne qu'un profil. Sans `-p`, ExoForge prend le profil de la fiche (`profil:`), puis le profil marqué `defaut: true`.

## Créer le profil de votre établissement

1. Copiez `Ecole1/` sous le nom de votre établissement (ex. `MonEcole/`), renommez `Ecole1_ColorScheme.tex` et mettez à jour `charte.latex_couleurs`.
2. Modifiez `nom`, `alias`, `description`, puis `charte.couleurs` et `charte.roles` (voir les rôles dans [style/README.md](../style/README.md)).
3. Facultatif : `campus: [Nord, Sud]`, la liste des campus de l'établissement, que l'Atelier Forge propose pour les déclinaisons d'un cours.
4. Vérifiez : `python scripts/quizforge/quizforge.py valider profils`.

Un profil que vous ne voulez pas publier se range dans `data/profils/<nom>/` (dossier non suivi par git) : les outils le trouvent de la même façon. Ordre de recherche : `profils/` du répertoire courant, puis `data/profils/`, puis `profils/` du dépôt ; à nom ou alias égal, le premier trouvé l'emporte.

`index_profils.json` est régénéré par QuizForge (valeurs acceptées de chaque réglage) ; il n'est pas suivi.
