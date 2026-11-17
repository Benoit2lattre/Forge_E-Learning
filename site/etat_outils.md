# État des outils et version 0.2

Cette page dit, pour chaque outil, ce qui marche et a été essayé en conditions réelles (dans Moodle, sur un vrai cours), ce qui est livré mais pas encore essayé, ce qui manque et les limites connues. Elle est mise à jour à chaque version de Forge.

:::{important}
**Numéros de version.** Forge porte un numéro d'ensemble (cette page annonce la **v0.2**). Chaque outil porte en plus son propre numéro, fixé d'après son état : en dessous de 1.0, un outil peut encore changer de format ou de commandes.
:::

## Vue d'ensemble

| Outil | Version | Essayé en conditions réelles | Livré, pas encore essayé | Manque |
| --- | --- | --- | --- | --- |
| QuizForge | 0.9 | tous les types de questions importés et joués dans Moodle ; contrôle `valider` ; barème « équilibré » ; quiz de séance | rappel des réglages Moodle conseillés | catalogue d'erreurs types par domaine ; export H5P |
| ExoForge | 0.8 | quatre exercices construits et validés (fatigue, cumul de dommage, mécanique des milieux continus, fiabilité) ; paquet SCORM 1.2 dans Moodle | graphiques dans les étapes (moteur récent) sur les exercices anciens | fonction de répartition normale Φ dans les expressions ; reprise d'un exercice interrompu ; import d'un scénario PowerPoint |
| DiagForge | 0.5 | bilan sur le bac à sable Moodle et sur des promotions fictives | analyse du tirage, de l'équité et de la rétention ; lecture des erreurs types | essai sur une vraie promotion ; restitution aux étudiants selon les règles de l'axe G ; lecture des traces SCORM d'ExoForge et de CapsuleForge |
| CapsuleForge | 0.8 | chapitre pilote : diaporama narré repris, transcrit, relu, lecteur, questions, exercice, paquet SCORM 2004 reçu par Moodle, traduction anglaise et voix de synthèse ; import de vidéo ; enregistrement d'écran, micro et webcam | dernière version de l'enregistreur (raccourcis corrigés) | caméo dans le lecteur ; simulation ActivePresenter dans le chapitre ; éditeur d'assemblage ; export H5P |
| Style et profils | 0.2 (avec Forge) | profils `Delattre` et `Ecole1` utilisés par QuizForge et ExoForge | — | thème modifiable dans CapsuleForge ; héritage entre profils |
| Bibliographie | 0.2 (avec Forge) | 9 axes, 250 références, 197 fiches, 602 règles | — | règles de restitution (axe G) non encore appliquées dans DiagForge ; quelques articles inaccessibles en texte complet |

## QuizForge — version 0.9

**Justification.** L'outil couvre tout ce dont un quiz Moodle a besoin et sert en cours ; ce qui reste à faire ajoute des contrôles sans changer le format du classeur. Le passage à 1.0 peut suivre l'essai du catalogue d'erreurs types.

- **Essayé** : les huit types d'onglet (vrai/faux, QCM, appariement, numérique, réponse courte, essai, schéma sur image avec le pointeur de zones, texte à trous) importés dans Moodle et joués ; tags, catégories, questions bilingues ; l'assistant `QuizForge.bat` ; `valider` et ses contrôles d'écriture ; barème `equilibree` (une mauvaise option retire 1/(n − t)) adopté dans le profil de l'auteur et vérifié dans Moodle.
- **Livré** : erreurs types et indices sur les questions numériques ; codes d'erreur sur les leurres (banque YAML lue par DiagForge) ; colonne `Séance` et plan de quiz de séance avec rappels ; score au hasard et seuil de réussite.
- **Limites connues** : les classeurs d'exemple ne sont pas régénérés avec les dernières colonnes ; certaines règles d'écriture sont des indices faibles (la clé la plus longue n'a pas d'effet démontré sur les indices, {cite}`rush2016`) et sont signalées comme telles.

## ExoForge — version 0.8

**Justification.** Le moteur générique joue tous les exercices écrits jusqu'ici, mais la syntaxe des fiches s'enrichit encore (graphiques, séries de points) et le mode d'emploi ne décrit pas les derniers ajouts.

- **Essayé** : exercices guidés en étapes (informations, choix, valeur numérique), données tirées au hasard, formules LaTeX avec les couleurs de rôle, graphiques, audio par étape, diagnostic de l'erreur commise, paquet SCORM 1.2 déposé dans Moodle ; quatre exercices validés.
- **Livré** : graphiques dans les étapes, couleurs et épaisseurs par courbe, séries de points (non encore retestés sur les exercices plus anciens).
- **Manque** : la fonction Φ (loi normale) dans les expressions ; la reprise d'un exercice en cours ; le rejet des tirages où une erreur type donne la bonne réponse ; un journal SCORM détaillé lisible par DiagForge.
- **Limites connues** : la notation `-(a)**2` est une erreur en JavaScript (écrire `-((a)**2)`) ; `build.py --help` n'affiche pas l'aide mais cherche un fichier nommé `--help`.

## DiagForge — version 0.5

**Justification.** Les analyses sont écrites et testées sur des données fictives ou de démonstration ; la validation sur une vraie promotion et la restitution aux étudiants restent à faire.

- **Essayé** : bilan à partir des exports Moodle (notes, réponses, XML des questions) du bac à sable ; classeur, fiche du professeur, images par groupe et par thème ; indicateurs de difficulté, de discrimination et de fiabilité avec leur lecture.
- **Livré** : colonne « Erreur type » et onglet « Par erreur » à partir de la banque QuizForge ; analyse du tirage des questions (mode observé, équité entre étudiants, rétention).
- **Manque** : restitution aux étudiants (pas de rang ni de classement, un repère par notion, une stratégie d'étude sous le seuil : règles de l'axe G) ; lecture des traces SCORM d'ExoForge et de CapsuleForge.
- **Limites connues** : sur de petits effectifs, les indicateurs sont instables ; la fiche le dit (« à confirmer »). La légende des images indique toujours « meilleure tentative », même quand une autre tentative est retenue.

## CapsuleForge — version 0.8

**Justification.** L'historique du dépôt porte déjà les versions 0.5 à 0.7.1 (questions, exercices, retour Moodle, traduction) ; la fusion des sources (vidéo, enregistreur intégré, didacticiel dans le lecteur de chapitre) justifie 0.8 (`capsuleforge --version`).

- **Essayé** : reprise d'un diaporama narré (images des états d'animation, sons), transcription automatique, relecture phrase par phrase, annotations dessinées dans PowerPoint, lecteur de chapitre avec parcours, jauges et badges, questions QuizForge en fin de section, exercice ExoForge dans une annexe, paquet SCORM 2004 reçu par Moodle (note pondérée, avancement, interactions), traduction anglaise relue et voix de synthèse, import d'une vidéo ActivePresenter, enregistrement d'écran, de micro et de webcam.
- **Livré, pas encore essayé** : la dernière version de l'enregistreur (raccourcis interceptés, son perdu comblé) ; les paquets SCORM 1.2 (`--scorm-version 1.2`), essayés sur une plateforme simulée seulement.
- **Manque** : affichage du caméo ; simulation ActivePresenter dans le chapitre ; éditeur d'assemblage ; export H5P ; thème modifiable.
- **Limites connues** : Moodle ne prend pas officiellement en charge SCORM 2004 ([FAQ SCORM de Moodle](https://docs.moodle.org/en/SCORM_FAQ)) ; les fonctions utilisées (données de suspension, note, achèvement, interactions) ont fonctionné dans l'essai, et l'export SCORM 1.2, plus sûr pour Moodle et d'autres plateformes, reste à essayer dans Moodle. Le lecteur ne joue pas encore les formules LaTeX dans les questions.

## Annonce de la version 0.2

:::{admonition} Forge E-Learning 0.2
:class: tip

Forge E-Learning 0.2 réunit quatre outils libres pour passer d'un cours existant à des activités Moodle : **QuizForge** (questions à partir d'un classeur Excel, avec contrôle de leur écriture), **ExoForge** (exercices guidés à données tirées, en HTML5 et SCORM), **DiagForge** (analyse des résultats et de la qualité des questions) et **CapsuleForge**, nouveau dans cette version : un diaporama narré devient un chapitre de cours interactif, sous-titré, traduit, avec questions et exercices, déposé dans Moodle en paquet SCORM. Les réglages s'appuient sur une bibliographie de 250 références et 197 fiches de lecture. Code sous GPL v3, documentation sous CC BY-NC-SA 4.0.
:::

Le détail des changements est dans le {doc}`journal des versions <../CHANGELOG>`.
