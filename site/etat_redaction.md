# État de rédaction

Point sur la documentation à la version 0.2 : chaque page ou mode d'emploi est **rédigé**, **à compléter**, **à écrire** ou **dépassé par le code**. Les modes d'emploi ont été comparés aux commandes réelles (`--help` de chaque outil).

## Modes d'emploi des outils

| Page | État | Ce qui manque |
| --- | --- | --- |
| {doc}`QuizForge <../outils/quizforge/README>` | rédigé | les neuf commandes de `quizforge.py --help` sont décrites (`bilan` renvoie à DiagForge) ; classeurs d'exemple à régénérer avec les dernières colonnes (`Code erreur n`, `Séance`, `Indice n`) ; capture du classeur modèle à refaire ensuite |
| {doc}`ExoForge <../outils/exoforge/README>` | à compléter | syntaxe récente du moteur non décrite : bloc `graphique` dans les étapes, `couleur` et `epaisseur` des courbes, `points` en liste de séries, `marque` ; `build.py --help` ne donne pas l'aide (il cherche un fichier nommé `--help`) |
| {doc}`DiagForge <../outils/diagforge/README>` | rédigé | décrit tout ce que fait la commande `bilan` ; la restitution aux étudiants n'existe pas encore ; captures sur données fictives, à jour |
| {doc}`CapsuleForge <../outils/capsuleforge/README>` | à compléter (en partie dépassé, introduction et statut mis à jour pour la 0.2) | la page mêle le format 1 (capsules de simulation) et le format 2 (chapitres) dans l'ordre où ils ont été écrits : à réorganiser autour du chapitre ; pas d'exemple pour `transcrire` ni pour l'assistant `CapsuleForge.bat` ; aucune capture d'écran du lecteur ou de la relecture ; la description de l'aide (`--help`) parle encore seulement de « capsules de simulation logicielle » |
| {doc}`Format du chapitre <../outils/capsuleforge/FORMAT>` | rédigé | exemple neutralisé (variante « École 1 », diaporama source) |

## Éléments communs

| Page | État | Ce qui manque |
| --- | --- | --- |
| {doc}`Style <../style/README>` | rédigé | — |
| {doc}`Profils <../profils/README>` | rédigé | héritage entre profils (`base:`) non décrit, car non codé |
| `donnees/README.md` (hors site) | rédigé | — |
| `_static/README.md` (hors site) | rédigé | — |
| `scripts/quizforge/README.md`, `scripts/exoforge/README.md` (hors site) | rédigés | notes pour développeur, non relues pour la 0.2 ; pas de README dans `scripts/capsuleforge/` |

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
| {doc}`Accueil <index>` | rédigé | à relire par l'auteur |
| {doc}`pourquoi` | rédigé | à relire par l'auteur ; faits datés (versions, licences) vérifiés en novembre 2026, à revoir à chaque version |
| {doc}`etat_outils` | rédigé | numéros de version validés pour la 0.2 |
| {doc}`Journal des versions <../CHANGELOG>` | rédigé | — |
| {doc}`Skills <../skills/README>` | rédigé | — |
| {doc}`prochaines_etapes` | rédigé | — |
| {doc}`api` | générée | docstrings mises au propre pour la 0.2 ; les moteurs HTML (exercice, lecteurs, éditeurs) ne sont pas documentés |
| Cours de démonstration | à écrire | un cours entièrement fictif qui montre la chaîne complète (questions, exercice, chapitre, bilan) |
