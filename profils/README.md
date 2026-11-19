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
3. Facultatif : ce que l'établissement dit de ses cours, lu par AtelierForge (voir plus bas, « Formations, codes et promotions »).
4. Vérifiez : `python scripts/quizforge/quizforge.py valider profils`.

Un profil que vous ne voulez pas publier se range dans `data/profils/<nom>/` (dossier non suivi par git) : les outils le trouvent de la même façon. Ordre de recherche : `profils/` du répertoire courant, puis `data/profils/`, puis `profils/` du dépôt ; à nom ou alias égal, le premier trouvé l'emporte.

`index_profils.json` est régénéré par QuizForge (valeurs acceptées de chaque réglage) ; il n'est pas suivi.

## Formations, codes et promotions

Chaque école découpe ses formations, nomme ses niveaux, code ses enseignements et nomme ses promotions à sa façon. Le profil le décrit par des clés facultatives, lues par AtelierForge pour les déclinaisons d'un cours (écran Cours). Sans elles, les mots et les listes génériques s'appliquent et les codes restent libres. Le profil `Ecole1` les montre toutes.

| Clé | Contenu | Sans la clé |
| --- | --- | --- |
| `structure` | niveaux d'organisation des enseignements | `[parcours, bloc, enseignement]` |
| `vocabulaire` | mots de l'école pour `enseignement` (un cours de la maquette, avec son code), `bloc` (un bloc d'enseignements) et `parcours` ; par exemple `{enseignement: Module, bloc: UE, parcours: Majeure}` | Enseignement, Bloc, Parcours |
| `campus`, `parcours` | listes de noms, ou de `{nom, code}` ; le code court sert aux gabarits | saisie libre |
| `formations` | `code`, `nom`, `niveaux`, `modalites`, `rncp`, `suite` (voir ci-dessous) | L, M, B, I |
| `codes` | gabarits des codes du bloc et de l'enseignement, et longueur des abrégés | codes libres |
| `promo` | gabarit du nom de promotion | promo de l'édition précédente |

**Formations.** Une formation a un code d'une lettre et ses niveaux. Sans la clé `formations`, quatre sont proposées : licence (L1 à L3), master (M1, M2), bachelor (B1 à B3) et ingénieur (I1 à I3, les trois années du cycle ingénieur que reconnaît la [CTI](https://www.cti-commission.fr/)). Une école qui compte toutes ses années écrit `niveaux: [I1, I2, I3, I4, I5]`. La clé `suite` donne la formation qui en prolonge une autre (une licence suivie d'un master) : elle sert au calcul de l'année de diplomation.

**Modalités et RNCP.** Les modalités sont le statut de l'élève dans une formation. Le diplôme d'ingénieur en connaît quatre : FISE (formation initiale sous statut d'étudiant), FISA (sous statut d'apprenti), FISEA (étudiant en première année du cycle ingénieur, apprenti les deux suivantes) et FC (formation continue) ; voir [la note de la CTI sur la FISEA](https://www.cti-commission.fr/wp-content/uploads/2023/07/Apprentissage-FISEA_nov2022_CTI.pdf). Une même formation peut être déclinée selon ses modalités, avec ou sans numéro différent au Répertoire national des certifications professionnelles (`rncp`) : une école dont le diplôme par apprentissage est enregistré à part déclare deux formations ; une autre garde une seule formation et ses modalités. Deux déclinaisons d'un même cours peuvent ainsi ne différer que par la modalité, avec des enseignements différents : un bloc de mathématiques qui compte deux enseignements en FISE et un seul, renforcé, en FISEA.

**Gabarit des codes.** Comme `AAAA-MM-JJ` décrit une date, un gabarit décrit un code avec des champs nommés entre accolades :

| Champ | Valeur | Exemple |
| --- | --- | --- |
| `{niveau}` | niveau de la déclinaison | L3 |
| `{formation}`, `{annee}` | ses deux parties | L, 3 |
| `{modalite}` | modalité | FISEA |
| `{campus}`, `{parcours}` | code court du campus (s'il n'y en a qu'un) et du parcours | N, AE |
| `{bloc}`, `{cours}` | abrégés saisis dans la déclinaison | MEC, TR |

```yaml
codes:
  longueurs: {bloc: 3, cours: 2}
  bloc: "{bloc}-{niveau}"                  # MEC-L3
  enseignement: "{bloc}-{niveau}-{cours}"  # MEC-L3-TR
```

L'atelier propose les codes dès que les abrégés sont saisis ; ils restent modifiables. `python scripts/forge/cours.py verifier` signale un code qui ne suit pas le gabarit de son école. Le tri alphabétique suit l'ordre du gabarit : avec le bloc en tête, les codes se regroupent par discipline ; avec le niveau en tête, par année.

**Promotions.** `promo: "P{diplomation}"` nomme la promotion d'après son année de diplomation, `promo: "X{entree:aa}"` d'après son année d'entrée sur deux chiffres. L'année se déduit de l'édition et de la place du niveau dans sa formation (et ses suites) : un L3 en 2026-2027, suivi d'un master de deux ans, donne P2029. La promo proposée reste modifiable : certaines ne suivent pas la règle.
