# État de rédaction

Point sur la documentation de la version 0.3 en préparation : chaque page ou mode d'emploi est **rédigé**, **à compléter**, **à écrire** ou **dépassé par le code**. Les modes d'emploi ont été comparés aux commandes réelles (`--help` de chaque outil).

## Modes d'emploi des outils

| Page | État | Ce qui manque |
| --- | --- | --- |
| {doc}`AtelierForge <../outils/atelier/README>` | rédigé | mode d'emploi écran par écran, avec captures de la version 0.5 (cours de démonstration) ; à compléter quand les capsules auront leurs versions |
| {doc}`Format d'un cours <../outils/atelier/FORMAT_cours>` | rédigé | — |
| {doc}`Versions et registre <../outils/atelier/FORMAT_registre>` | rédigé | versions des capsules à ajouter quand elles existeront |
| {doc}`QuizForge <../outils/quizforge/README>` | rédigé | les neuf commandes de `quizforge.py --help` sont décrites (`bilan` renvoie à DiagForge) ; classeurs d'exemple à régénérer avec les dernières colonnes (`Code erreur n`, `Séance`, `Indice n`) ; capture du classeur modèle à refaire ensuite |
| {doc}`ExoForge <../outils/exoforge/README>` | à compléter | syntaxe récente du moteur pas entièrement décrite : `couleur` et `epaisseur` des courbes, `points` en liste de séries, `marque` |
| {doc}`DiagForge <../outils/diagforge/README>` | rédigé | décrit tout ce que fait la commande `bilan` ; la restitution aux étudiants n'existe pas encore ; captures sur données fictives, à jour |
| {doc}`CapsuleForge <../outils/capsuleforge/README>` | rédigé | réorganisé autour des capsules (cours et didacticiels) et de l'ancien lecteur, avec captures du lecteur et de la relecture sur un chapitre fictif ; aide de la commande à jour |
| {doc}`Format du chapitre <../outils/capsuleforge/FORMAT>` | rédigé | exemple neutralisé (variante « École 1 », diaporama source) |

## Éléments communs

| Page | État | Ce qui manque |
| --- | --- | --- |
| {doc}`Style <../style/README>` | rédigé | — |
| {doc}`Profils <../profils/README>` | rédigé | héritage entre profils (`base:`) non décrit, car non codé |
| `donnees/README.md` (hors site) | rédigé | — |
| `_static/README.md` (hors site) | rédigé | — |
| `scripts/quizforge/README.md`, `scripts/diagforge/README.md`, `scripts/exoforge/README.md` (hors site) | rédigés | notes pour développeur, non relues pour la 0.2 ; pas de README dans `scripts/capsuleforge/` |

## Bibliographie

| Page | État | Ce qui manque |
| --- | --- | --- |
| {doc}`Index de la bibliographie <../reference/README>` | rédigé | la colonne « État » emploie les priorités de lecture P1 / P2, à expliciter pour un lecteur extérieur |
| {doc}`Méthode des fiches <../reference/fiches_methode>` | rédigé | — |
| Axes A à I (9 pages) | rédigés | synthèses à jour des fiches écrites ; quelques articles inaccessibles en texte complet sont signalés sans fiche |
| 197 fiches de lecture | rédigées | — |
| {doc}`Liste des références <bibliographie_complete>` | générée | produite à partir de `forge.bib` |

## Pages du site

| Page | État | Ce qui manque |
| --- | --- | --- |
| {doc}`Accueil <index>` | rédigé | relu par l'auteur ; AtelierForge et la famille v0.3 ajoutés depuis |
| {doc}`pourquoi` | rédigé | relu par l'auteur ; faits datés (versions, licences) vérifiés en novembre 2026, à revoir à chaque version |
| {doc}`etat_outils` | rédigé | numéros de version validés pour la 0.2 ; AtelierForge 0.5 ajouté pour la 0.3 |
| {doc}`Journal des versions <../CHANGELOG>` | rédigé | — |
| {doc}`Skills <../skills/README>` | rédigé | — |
| {doc}`prochaines_etapes` | rédigé | — |
| {doc}`api` | générée | docstrings mises au propre pour la 0.2 ; les moteurs HTML (exercice, lecteurs, éditeurs) ne sont pas documentés |
| Cours de démonstration | à compléter | `donnees/cours/traction/` (hors site, décrit dans {doc}`Format d'un cours <../outils/atelier/FORMAT_cours>`) : fiche du cours, déclinaison bilingue Ecole1, édition 2026 et registre avec une version de quiz ; la chaîne complète (exercice, capsule, bilan rattachés au cours) reste à montrer |
