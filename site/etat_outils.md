# État des outils

Cette page dit, pour chaque outil, ce qui marche et a été essayé en conditions réelles (dans Moodle, sur un vrai cours), ce qui est livré mais pas encore essayé, ce qui manque et les limites connues. Elle est mise à jour au fil du travail : elle décrit la version 0.3, publiée (son annonce est en bas de page, avec celle de la v0.2).

:::{important}
**Numéros de version.** Forge porte un numéro d'ensemble (**v0.3** publiée, **v0.4** en préparation). Chaque outil porte en plus son propre numéro, fixé d'après son état : en dessous de 1.0, un outil peut encore changer de format ou de commandes.
:::

## Vue d'ensemble

| Outil | Version | Essayé en conditions réelles | Livré, pas encore essayé | Manque |
| --- | --- | --- | --- | --- |
| AtelierForge | 0.5 | les quatre outils lancés par boutons sous Windows, sur les cours de l'auteur : questions, exercices, capsules (préparation complète, filmer l'écran), bilans ; cours, déclinaisons et éditions ; versions des conversions QuizForge et registre ; versions des capsules habillées ; carte « 6. PDF » ; « Oublier » ligne à ligne dans Réglages | versions des paquets ExoForge ; cours de démonstration | ouverture des fichiers sans messages dans la fenêtre de commande ; essai hors Windows |
| QuizForge | 0.9 | tous les types de questions importés et joués dans Moodle ; contrôle `valider` ; barème « équilibré » ; quiz de séance ; option `--cours` (profil, catégorie Moodle, plan de séance) et versions rangées dans l'édition | rappel des réglages Moodle conseillés | catalogue d'erreurs types par domaine ; export H5P |
| ExoForge | 0.8 | quatre exercices construits et validés (fatigue, cumul de dommage, mécanique des milieux continus, fiabilité) ; paquet SCORM 1.2 dans Moodle ; exercice joué dans un chapitre CapsuleForge, aussi en anglais | graphiques dans les étapes (moteur récent) sur les exercices anciens ; paquet SCORM rangé en version de l'édition (`--cours`) | fonction de répartition normale Φ dans les expressions ; reprise d'un exercice interrompu ; import d'un scénario PowerPoint |
| CapsuleForge | 0.9 | chapitre pilote : diaporama narré repris, transcrit, relu, lecteur, questions, exercice, paquets SCORM 2004 et 1.2 reçus par Moodle, chapitre bilingue (sous-titres, questions, exercice, interface) et voix de synthèse ; import de vidéo ; enregistrement d'écran, micro et webcam avec raccourcis et bips ; capsule habillée pour une édition (charte, modèle PowerPoint de l'école, formes d'édition et champs, variantes, texte et diapositives traduits, PDF, versions rangées) ; relecture d'un diaporama sans voix (scénario des notes, accroches aux phrases, pauses, horloge muette) ; vidéo insérée dans le diaporama (lecteur, relecture, PDF, Moodle) ; fin du pas réglable ; PDF fait à part, en versions | contrôle des chevauchements après le modèle de l'école ou la traduction ; remarques de vérification dans la relecture ; caméo dans le lecteur ; test du micro ; vidéos d'écran allégées | partir d'une intention (plan, squelette du diaporama) ; simulation ActivePresenter dans le chapitre ; éditeur d'assemblage ; export H5P |
| DiagForge | 0.6 | bilan sur le bac à sable Moodle et sur des promotions fictives | commande `diagforge.py` ; analyse du tirage, de l'équité et de la rétention ; lecture des erreurs types ; reconnaissance de la version du test (`--cours`) | essai sur une vraie promotion ; restitution aux étudiants selon les règles de l'axe G ; lecture des traces SCORM d'ExoForge et de CapsuleForge |
| Style et profils | 0.3 (avec Forge) | profils `Delattre` et `Ecole1` utilisés par QuizForge, ExoForge et CapsuleForge (charte, logo, modèle PowerPoint, jeu de couleurs LaTeX, formations et codes) | niveaux des dispositions et balises des notes déclarés dans le profil | héritage entre profils |
| Bibliographie | 0.3 (avec Forge) | 9 axes, 250 références, 197 fiches, 602 règles | — | règles de restitution (axe G) non encore appliquées dans DiagForge ; quelques articles inaccessibles en texte complet |

## AtelierForge — version 0.5

**Justification.** L'atelier lance déjà toute la suite et range le travail par cours ; le modèle des cours (déclinaisons, éditions, registre des versions) vient d'être posé et peut encore changer avec les versions des capsules. Il ne fait aucun calcul lui-même : sa maturité suit celle des outils qu'il lance.

- **Essayé** : sous Windows, sur les cours de l'auteur : écrans Questions (valider, convertir pour Moodle avec plan de séance, réunir un classeur et sa traduction), Exercices, Capsules (de la reprise du diaporama au paquet SCORM, filmer l'écran avec micro, caméra et caméo, manipulation enregistrée), Bilans et Réglages ; apparence jour et nuit ; écran Cours (déclinaisons bilingues, campus, éditions, séances) ; conversions QuizForge rangées en versions de l'édition et écran Registre ; carte « 6. PDF » de l'écran Capsules ; dans Réglages, « Oublier » pour chaque classeur et chaque diaporama, chemin « introuvable » signalé.
- **Livré** : paquets ExoForge rangés en versions ; inscription des bilans DiagForge au registre ; cours de démonstration `donnees/cours/traction/`.
- **Manque** : ouverture des fichiers détachée de la fenêtre de commande (une application comme un lecteur Markdown y écrit ses messages) ; essai sous macOS et Linux.
- **Limites connues** : l'atelier n'écoute que l'ordinateur où il tourne (127.0.0.1) : il ne se partage pas sur le réseau.

## QuizForge — version 0.9

**Justification.** L'outil couvre tout ce dont un quiz Moodle a besoin et sert en cours ; ce qui reste à faire ajoute des contrôles sans changer le format du classeur. Le passage à 1.0 peut suivre l'essai du catalogue d'erreurs types.

- **Essayé** : les huit types d'onglet (vrai/faux, QCM, appariement, numérique, réponse courte, essai, schéma sur image avec le pointeur de zones, texte à trous) importés dans Moodle et joués ; tags, catégories, questions bilingues ; l'assistant `QuizForge.bat` ; `valider` et ses contrôles d'écriture ; barème `equilibree` (une mauvaise option retire 1/(n − t)) adopté dans le profil de l'auteur et vérifié dans Moodle.
- **Livré** : erreurs types et indices sur les questions numériques ; codes d'erreur sur les leurres (banque YAML lue par DiagForge) ; colonne `Séance` et plan de quiz de séance avec rappels ; score au hasard et seuil de réussite ; option `--cours` (profil de l'école, catégorie Moodle, effectif, date et titre de la séance) et conversions rangées en versions de l'édition, jamais écrasées, avec leur fiche `version.yaml` et le registre (essayé par l'auteur).
- **Limites connues** : certaines règles d'écriture sont des indices faibles (la clé la plus longue n'a pas d'effet démontré sur les indices, {cite}`rush2016`) et sont signalées comme telles.

## ExoForge — version 0.8

**Justification.** Le moteur générique joue tous les exercices écrits jusqu'ici, mais la syntaxe des fiches s'enrichit encore (graphiques, séries de points) : elle n'est pas encore figée.

- **Essayé** : exercices guidés en étapes (informations, choix, valeur numérique), données tirées au hasard, formules LaTeX avec les couleurs de rôle, graphiques, audio par étape, diagnostic de l'erreur commise, paquet SCORM 1.2 déposé dans Moodle ; quatre exercices validés ; exercice joué dans le lecteur de chapitre de CapsuleForge, en français et traduit en anglais.
- **Livré** : graphiques dans les étapes, couleurs et épaisseurs par courbe, séries de points (non encore retestés sur les exercices plus anciens) ; avec `--cours`, paquet SCORM rangé comme version de l'édition (`exercices/<id>/v2/`) et inscrit au registre.
- **Manque** : la fonction Φ (loi normale) dans les expressions ; la reprise d'un exercice en cours ; le rejet des tirages où une erreur type donne la bonne réponse ; un journal SCORM détaillé lisible par DiagForge.
- **Limites connues** : la notation `-(a)**2` est une erreur en JavaScript (écrire `-((a)**2)`) ; l'interface du moteur n'est traduite qu'en anglais.

## CapsuleForge — version 0.9

**Justification.** La 0.8 (v0.2 de Forge) réunissait les sources du chapitre (diaporama, vidéo, enregistreur, didacticiel). La 0.9 ajoute les paquets SCORM 1.2, la traduction des questions et des exercices, les remarques de vérification dans la relecture et un code réorganisé (`capsuleforge --version`), puis l'habillage par édition (lot 6 de la v0.3), la relecture d'un diaporama sans voix, les vidéos insérées dans le diaporama et le PDF fait à part. Le format du chapitre peut encore changer avec l'éditeur d'assemblage ; le numéro reste 0.9 jusqu'à ce choix.

- **Essayé** : reprise d'un diaporama narré (images des états d'animation, sons), transcription automatique, relecture phrase par phrase, annotations dessinées dans PowerPoint, lecteur de chapitre avec parcours, jauges et badges, questions QuizForge en fin de section, exercice ExoForge dans une annexe, paquets SCORM 2004 et 1.2 reçus par Moodle (note pondérée, avancement, interactions), chapitre bilingue relu (sous-titres, questions, exercice, interface du lecteur) et voix de synthèse anglaise, import d'une vidéo ActivePresenter, enregistrement d'écran, de micro et de webcam (raccourcis interceptés, bips, section vérifiée avant de filmer) ; une capsule construite pour une édition d'école fictive : charte et logo, écran d'accueil, pied de page, filigrane, modèle PowerPoint de l'école appliqué aux diapositives, formes « cf édition » et champs, variantes de phrases par public, texte des diapositives dans le volet « Texte » (formules, liens), diapositives traduites, voix et sous-titres dans les deux langues, PDF imprimé par Edge, version rangée au registre ; reprise d'un diaporama sans voix d'après son scénario (degrés de préparation, balises `[clic]`, `[pause]`, `[note]` des notes, équations natives lues), apparitions accrochées aux phrases et suivant la voix, pauses, relecture à l'horloge muette ; vidéo insérée dans une diapositive extraite, recadrée, jouée à sa place dans le lecteur (aussi dans Moodle, SCORM 1.2 et 2004), réglée dans la relecture et posée dans le PDF ; fin du pas comme action (après la voix et les vidéos par défaut, réglable dans la relecture, balise `[fin]`) ; PDF fait à part à partir du lecteur construit (commande `pdf`, carte « 6. PDF », une version par réglage, case « dans le paquet », bouton du lecteur selon la langue des sous-titres).
- **Livré, à corriger** : le contrôle des textes qui se chevauchent ou débordent après le modèle de l'école ou la traduction (au journal de la construction) ne voit pas encore un texte traduit plus long qui passe sous une forme voisine.
- **Livré, pas encore essayé** : les remarques de `verifier` affichées dans la relecture sur un pas qui en a (essayé sur une copie modifiée) ; le caméo en médaillon dans le lecteur (commande `cameo` : place, taille, forme) ; le test du micro avant de filmer et le relèvement d'une voix trop faible ; les vidéos d'écran allégées (dix à quarante fois plus légères).
- **Manque** : partir d'une intention (concepteur de leçon, squelette du chapitre et du diaporama de degré 1, prévus en 0.4) ; simulation ActivePresenter dans le chapitre ; éditeur d'assemblage ; export H5P.
- **Limites connues** : Moodle ne prend pas officiellement en charge SCORM 2004 ([FAQ SCORM de Moodle](https://docs.moodle.org/en/SCORM_FAQ)) ; les fonctions utilisées (données de suspension, note, achèvement, interactions) y ont fonctionné, et les paquets SCORM 1.2 (`--scorm-version 1.2`), plus sûrs pour Moodle et d'autres plateformes, y ont donné la même note. Les textes calculés par des expressions dans une fiche ExoForge restent dans la langue source. Le lecteur ne joue pas encore les formules LaTeX dans les questions. Un modèle d'école change polices et couleurs : un texte élargi peut toucher une équation ou un schéma restés en place ; un texte traduit plus long peut déborder de sa zone. La construction signale les textes qui se chevauchent ou débordent, mais pas un texte qui touche une image (schéma, équation en image). PowerPoint n'enregistre pas l'instant des clics : dans un diaporama enregistré sans balises, les clics sont répartis et se calent dans la relecture. Le diaporama doit avoir des dispositions de même nom que le modèle de l'école.

## DiagForge — version 0.6

**Justification.** Les analyses sont écrites et testées sur des données fictives ou de démonstration ; la validation sur une vraie promotion et la restitution aux étudiants restent à faire. Le passage de 0.5 à 0.6 tient au nouvel emplacement du code (`scripts/diagforge/`) et à la commande `diagforge.py` : les chemins des commandes ont changé (`quizforge.py bilan` reste disponible).

- **Essayé** : bilan à partir des exports Moodle (notes, réponses, XML des questions) du bac à sable ; classeur, fiche du professeur, images par groupe et par thème ; indicateurs de difficulté, de discrimination et de fiabilité avec leur lecture.
- **Livré** : commande `python scripts/diagforge/diagforge.py` ; colonne « Erreur type » et onglet « Par erreur » à partir de la banque QuizForge ; analyse du tirage des questions (mode observé, équité entre étudiants, rétention) ; avec `--cours`, reconnaissance de la version du test d'après ses questions (onglet « Version » du bilan, bilan inscrit au registre), essayée sur des exports fictifs seulement.
- **Manque** : restitution aux étudiants (pas de rang ni de classement, un repère par notion, une stratégie d'étude sous le seuil : règles de l'axe G) ; lecture des traces SCORM d'ExoForge et de CapsuleForge.
- **Limites connues** : sur de petits effectifs, les indicateurs sont instables ; la fiche le dit (« à confirmer »). Le générateur de promotions fictives demande un export d'essai d'au moins quatre questions.

## Annonce de la version 0.3

:::{admonition} Forge E-Learning 0.3
:class: tip

Forge E-Learning 0.3 ajoute **AtelierForge**, une page dans le navigateur qui lance toute la suite par boutons et range le travail par **cours** : déclinaisons (école, langue, campus) et éditions (année, promo), chaque conversion de questions, chaque exercice et chaque capsule rangés en versions, avec un registre. **CapsuleForge** habille une même capsule pour plusieurs écoles (charte, modèle PowerPoint, variantes de phrases, diapositives traduites), part d'un diaporama **sans voix** (son scénario de lecture, des apparitions accrochées aux phrases, des pauses), joue les **vidéos insérées** dans le diaporama et fait le **PDF** à imprimer à part, en versions. Un guide aide à préparer son diaporama, avec un exemple pour chaque degré de préparation. Code sous GPL v3, documentation sous CC BY-NC-SA 4.0.
:::

## Annonce de la version 0.2

:::{admonition} Forge E-Learning 0.2
:class: tip

Forge E-Learning 0.2 réunit quatre outils libres pour passer d'un cours existant à des activités Moodle : **QuizForge** (questions à partir d'un classeur Excel, avec contrôle de leur écriture), **ExoForge** (exercices guidés à données tirées, en HTML5 et SCORM), **DiagForge** (analyse des résultats et de la qualité des questions) et **CapsuleForge**, nouveau dans cette version : un diaporama narré devient un chapitre de cours interactif, sous-titré, traduit, avec questions et exercices, déposé dans Moodle en paquet SCORM. Les réglages s'appuient sur une bibliographie de 250 références et 197 fiches de lecture. Code sous GPL v3, documentation sous CC BY-NC-SA 4.0.
:::

Le détail des changements est dans le {doc}`journal des versions <../CHANGELOG>`.
