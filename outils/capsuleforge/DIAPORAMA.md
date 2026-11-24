# Préparer son diaporama pour CapsuleForge

CapsuleForge part d'un diaporama PowerPoint qui existe déjà. Plus le diaporama est préparé, moins il reste à faire dans l'éditeur de la Forge : un diaporama bien construit donne une capsule presque finie dès sa reprise. Ce guide décrit ce qu'un diaporama peut porter, degré par degré, et la façon de l'écrire pour que la reprise le comprenne.

```{admonition} État
:class: note
Les degrés, les niveaux et les balises sont fixés pour la version 0.3. La lecture des balises, le plan proposé d'après le diaporama et le diagnostic à la reprise arrivent avec cette version. Partir d'une intention (plan, fiche de cours, squelette de leçon), c'est-à-dire des degrés 0 et 1, relève de la version 0.4.
```

## Les six degrés d'un diaporama

Chaque degré contient le précédent. Le degré 2 est l'état de presque tous les diaporamas de cours, faits pour être projetés en direct, l'enseignant aux commandes : c'est le point d'entrée habituel d'une capsule.

| Degré | Le diaporama contient | La reprise produit | Il reste à faire dans la Forge |
|---|---|---|---|
| 0. Brut | Des diapositives, sans structure ni animation | Un pas par diapositive | Tout : plan, texte dit, voix, calage |
| 1. Structuré | Un plan : diapositive de titre, diapositives de partie, sections, titres provisoires | Le plan de la capsule | Le contenu, puis tout le reste |
| 2. Animé | Le contenu et ses animations | Un pas par diapositive, une action par clic | Le texte dit, la voix, le calage |
| 3. Commenté | Le texte à dire, dans les notes | Le texte dit, découpé en phrases ; les actions accrochées aux phrases dans l'ordre | Vérifier le calage, générer la voix |
| 4. Balisé | Des balises dans les notes : où tombe chaque clic, où marquer une pause | Le calage complet | Relire, générer la voix |
| 5. Enregistré | La voix réelle et le minutage, enregistrés dans PowerPoint | La voix et la durée de chaque diapositive | Transcrire, caler les clics (sans balises) |

Deux remarques sur le degré 5 :

- **PowerPoint n'enregistre pas l'instant des clics** pendant une narration, seulement la durée de la diapositive. Sans balises, les clics sont répartis sur cette durée, puis calés à la relecture. Avec un texte balisé (degré 4) lu à voix haute, ils sont calés d'emblée.
- **On peut sauter des degrés** : beaucoup d'anciennes capsules sont passées du degré 2 au degré 5, voix enregistrée sans texte préparé. La reprise les accepte ; c'est la relecture qui fait le travail des degrés 3 et 4.

## Les niveaux d'une capsule dans PowerPoint

| Niveau de la capsule | Porté dans PowerPoint par |
|---|---|
| Chapitre | Le fichier : titre (propriétés du document), modèle, diapositive de titre |
| Partie | Une diapositive dont la disposition est déclarée « partie » (par défaut « En-tête de section ») |
| Section | Une section PowerPoint (volet des miniatures, clic droit, « Ajouter une section ») |
| Pas | Une diapositive |
| Action | Un clic d'animation ; la transition de la diapositive est l'action 0 |
| Élément | Une forme, un groupe ou un paragraphe animé |

Quelques règles en découlent :

- **Les effets « Avec la précédente » et « Après la précédente »** appartiennent au même clic : ils forment une seule action.
- **Nommer les formes** dans le volet Sélection (Accueil, Sélectionner, Volet Sélection) rend le journal de reprise et l'éditeur lisibles : « Force gauche » plutôt que « Connecteur droit 12 ».
- **Les formes « cf … »** (spot, cadre, pointeur, cache, édition) restent valables ; elles sont décrites dans la présentation de CapsuleForge (« Annoter dans PowerPoint »).

## Parties et sections

PowerPoint n'a qu'un niveau de sections. La reprise combine donc deux indices :

- **Avec des sections PowerPoint**, chaque section devient une section de la capsule. Une diapositive « partie » ouvre une nouvelle partie ; elle se range dans la première section de cette partie.
- **Sans sections PowerPoint**, une diapositive dont la disposition est déclarée « section » ouvre une section ; à défaut, chaque partie n'a qu'une section.
- **Sans diapositive « partie »**, la capsule n'a qu'une partie.

### Déclarer le niveau des dispositions

Un modèle d'école peut avoir plusieurs dispositions de titre : titre de section, chapitre, ouverture, diapositive de titre… Le niveau de chacune se déclare dans le profil de l'école, à côté du modèle `.potx` :

```yaml
powerpoint:
  dispositions:                     # nom de la disposition → niveau
    "Diapositive de titre": chapitre
    "Chapitre": partie
    "Titre de section": partie
    "Ouverture": section
```

Sans déclaration, les noms standard de PowerPoint s'appliquent : « Diapositive de titre » (« Title Slide ») pour le chapitre, « En-tête de section » (« Section Header ») pour la partie. Un chapitre peut remplacer la correspondance de son école, sous la même clé de son `chapitre.yaml`.

### Adapter son modèle `.potx`

Deux façons de faire, au choix :

- **Renommer les dispositions** du modèle avec les noms standard (Affichage, Masque des diapositives, clic droit sur la disposition, « Renommer la disposition »). Rien à déclarer.
- **Garder les noms** du modèle et les déclarer dans le profil, comme ci-dessus.

## Le texte dit : les notes

Les notes de la diapositive sont le texte dit du pas, celui que lira la voix de synthèse, que montreront les sous-titres et le volet « Texte » du lecteur, et qu'imprimera le PDF. Elles s'écrivent pour l'oreille :

- **une idée par phrase** : chaque phrase devient une phrase de la voix et un sous-titre ;
- **les formules en toutes lettres** : « sigma égale F sur S » plutôt que « σ = F/S » ;
- **pas d'abréviations** que la voix lirait mal.

## Les balises des notes

Les balises s'écrivent entre crochets dans les notes. Elles règlent la capsule et n'apparaissent nulle part ailleurs : ni dans la voix, ni dans les sous-titres, ni dans le volet « Texte », ni dans le PDF.

| Balise | Effet |
|---|---|
| `[clic]` | L'action suivante se joue à cet endroit du texte. |
| `[pause]` | Silence de durée par défaut à cet endroit (0,4 s). |
| `[pause 2 s]` | Silence de la durée donnée. |
| `[note] … [/note]` | Texte pour l'enseignant : ni dit, ni affiché, ni imprimé. |

Une balise inconnue est signalée par le diagnostic de la reprise, et retirée comme les autres.

Exemple, pour la diapositive de l'éprouvette :

```text
Voici l'éprouvette, un barreau de section constante. [clic] On la tire à ses deux
extrémités avec une force F. [pause 1 s] [clic] Sa section, notée S, est supposée
constante pendant l'essai. [note]En salle : faire passer une vraie éprouvette.[/note]
```

Sans balise `[clic]`, les actions sont accrochées aux phrases dans l'ordre : la première action à la première phrase, la deuxième à la deuxième, et ainsi de suite.

Les crochets sont les délimiteurs par défaut. Un profil d'école peut en choisir d'autres, si les crochets servent déjà dans ses notes :

```yaml
powerpoint:
  balises: ["⟦", "⟧"]               # ouvrante, fermante
```

## Accroche, pause et débit par défaut

| Réglage | Par défaut | Sens |
|---|---|---|
| Accroche d'une action | 0,4 s avant le début de sa phrase | L'élément apparaît juste avant d'être nommé. |
| Pause entre deux phrases | 0,4 s | Le silence que laisse la voix de synthèse. |
| Débit sans voix | Par langue | Sert à estimer les instants tant qu'il n'y a pas de voix, et à relire avant de la générer. |

Les trois réglages se changent par chapitre. Le débit se règle aussi pour une voix enregistrée, quand elle n'est pas de synthèse.

## Le diagnostic à la reprise

La reprise indique le degré atteint par le diaporama, ce qu'elle a produit et ce qu'il faudrait ajouter dans PowerPoint pour monter d'un degré. En dessous du degré 2, elle prévient que le diaporama est trop tôt pour une capsule : c'est le moment du plan et du squelette de leçon (version 0.4).

## Les exemples

Le dossier `outils/capsuleforge/exemples/diaporamas/` du dépôt contient un même petit cours, « Essai de traction », à chaque degré :

| Degré | Fichier |
|---|---|
| 0 | `traction_degre0_brut.pptx` |
| 1 | `traction_degre1_structure.pptx` |
| 2 | `traction_degre2_anime.pptx` |
| 3 | `traction_degre3_commente.pptx` |
| 4 | `traction_degre4_balise.pptx` |
| 5 | À enregistrer soi-même à partir du degré 4 (Diaporama, Enregistrer), en lisant les notes |

Ouvrir deux degrés voisins côte à côte montre ce qui change de l'un à l'autre.
