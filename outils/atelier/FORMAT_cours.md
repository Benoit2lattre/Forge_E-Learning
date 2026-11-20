# AtelierForge — format d'un cours (`forge-cours/1`)

Un cours est décrit par un seul fichier, `cours.yaml`, rangé dans `data/cours/<nom>/` (cours privés) ou `donnees/cours/<nom>/` (cours de démonstration publiés). L'écran **Cours** de l'atelier l'écrit par formulaire ; le fichier reste lisible et modifiable à la main. Les outils le lisent par l'option `--cours` (QuizForge, ExoForge, DiagForge) ; `python scripts/forge/cours.py verifier` le contrôle.

Statut : format écrit et vérifié par `scripts/forge/cours.py`, lu par `scripts/commun/cours_options.py` et par l'atelier.

## Trois niveaux

| Niveau | Ce qu'il porte | Change |
| --- | --- | --- |
| Cours | le contenu générique : titre, domaine, description, objectifs, compétences, documents, sources | rarement |
| Déclinaison | le cours dans une école : école (profil d'établissement), campus, parcours, niveau, codes de l'enseignement et du bloc, langues, cours et catégorie Moodle | peu d'une année à l'autre |
| Édition | une année de la déclinaison : promo, groupes (campus et langue de chacun), effectif, séances datées, dossiers des exports et des bilans | chaque année |

Un cours désigne ses **sources** (classeurs, fiches, capsules, diaporamas, dossiers d'exports) **sans les déplacer** : tout objet situé dans une source, ou sous le dossier du cours, lui appartient. Un objet peut appartenir à plusieurs cours. Les mots employés ici sont génériques : un **enseignement** est un cours de la maquette, avec son code ; un **bloc** regroupe plusieurs enseignements ; un **parcours** est une filière de l'école. Chaque école garde ses propres mots dans son profil (clé `vocabulaire`, par exemple « Module » et « UE »), avec ses campus, ses parcours, ses formations, les gabarits de ses codes et de ses noms de promotion (voir [Formations, codes et promotions](../../profils/README.md#formations-codes-et-promotions)) ; l'atelier les affiche et les propose à la place des mots génériques.

## Champs du cours

| Clé | Contenu |
| --- | --- |
| `format` | `forge-cours/1` |
| `nom` | nom court, aussi nom du dossier (24 caractères au plus : minuscules sans accent, chiffres, `-`, `_`) |
| `titre`, `domaine`, `langues` | titre affiché, domaine (sert au catalogue d'erreurs), langues du cours (`fr`, `en`…) |
| `description`, `objectifs`, `competences` | texte et listes, lus en premier par le futur skill « questions et exercices à partir d'un syllabus » |
| `documents` | fichiers liés : `syllabus`, `plan`, `fiche_competences`, `autre1`… (PDF, Word, Markdown) |
| `sources` | par type : `questions`, `exercices`, `capsules`, `diaporamas`, `exports` ; chemins relatifs à la racine du dépôt, absolus, ou motifs (`data/capsuleforge/mef_*`) |
| `erreurs` | catalogue d'erreurs types du domaine (`data/reference/erreurs/<domaine>.yaml`), partagé entre cours |
| `etiquettes` | étiquettes Moodle ajoutées aux questions converties |
| `inclut` | cours repris comme séances (leurs sources s'ajoutent, sans copie) |
| `derive_de` | cours d'origine d'une version au plan propre (réduite ou développée) |
| `declinaisons` | liste des déclinaisons (ci-dessous) |
| `comparaisons` | comparaisons choisies pour DiagForge (éditions de plusieurs déclinaisons, années ou campus) |

## Champs d'une déclinaison

| Clé | Contenu |
| --- | --- |
| `nom` | nom court (`ecole1-meca`) : nom du dossier, ne change pas |
| `ecole`, `campus` | profil d'établissement et campus concernés (un ou plusieurs) |
| `parcours` | `Aero`, `Auto`, `Meca`… (liste `parcours` du profil) |
| `formation`, `niveau`, `modalite` | formation du profil (`L`, `M`, `B`, `I` par défaut), un de ses niveaux (`L3`, `I1`…) et, s'il y a lieu, la modalité (`FISE`, `FISA`, `FISEA`, `FC`) |
| `rncp` | numéro au RNCP, quand il diffère de celui de la formation |
| `codes` | `enseignement`, `bloc` : codes de l'enseignement et de son bloc, ajoutés aux étiquettes des questions |
| `abreges` | `bloc`, `cours` : abrégés d'où l'atelier tire les codes quand le profil de l'école donne leurs gabarits |
| `langues` | une ou plusieurs : une déclinaison bilingue garde ses groupes français et anglais ensemble |
| `moodle` | `cours` (nom ou adresse) et `categorie` (racine des catégories de questions) |
| `sources` | sources propres à la déclinaison (version anglaise, TD et TP de l'école) |
| `editions` | liste des éditions ; `en_cours` : nom de l'édition en cours (chaque déclinaison a la sienne) |

## Champs d'une édition

| Clé | Contenu |
| --- | --- |
| `nom` | l'année (`2026`) ou un nom court : nom du dossier, ne change pas |
| `promo`, `effectif` | promotion (proposée d'après le gabarit `promo` du profil) ; nombre d'étudiants (plan du quiz de séance) |
| `enseignant`, `filigrane` | nom affiché sur l'écran d'accueil des capsules ; `true` pour poser le filigrane de l'école sur leurs images |
| `groupes` | `nom`, `campus`, `langue` de chaque groupe |
| `seances` | `n`, `date` (AAAA-MM-JJ), `titre` : la prochaine séance est proposée pour le plan du quiz |
| `exports`, `bilans` | dossiers `data/cours/<cours>/<déclinaison>/<année>/exports` et `bilans` |

À côté du fichier, chaque édition a son dossier `<déclinaison>/<année>/` : `quiz/` et `exercices/` (versions), `exports/`, `bilans/`, `registre.yaml` (voir [le registre des versions](FORMAT_registre.md)).

## Exemple : le cours de démonstration

```{literalinclude} ../../donnees/cours/traction/cours.yaml
:language: yaml
```
