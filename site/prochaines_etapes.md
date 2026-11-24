# Prochaines étapes

Un plan grossier, outil par outil, de la version 0.2 vers la 0.3 puis au-delà. Les priorités peuvent changer avec les essais en cours.

## Court terme : vers la version 0.3

| Outil | Prochaines étapes |
| --- | --- |
| **QuizForge** | rappel des réglages Moodle conseillés selon l'usage (classe ou examen), avec une alerte contre la combinaison tentatives multiples, meilleure note et relecture question par question ; pénalité par essai |
| **ExoForge** | fonction Φ (loi normale) dans les expressions ; rejet des tirages où une erreur type donne la bonne réponse ; retour gradué ; journal SCORM détaillé |
| **CapsuleForge** | **relecture d'un diaporama sans voix** (durées estimées, apparitions accrochées aux phrases, pauses) ; afficher le **caméo** (vidéo de l'enseignant en médaillon) dans le lecteur, calé sur le pas, puis recaler un caméo filmé à part par comparaison des sons ; jouer une **simulation ActivePresenter** (gestes, mode « À vous ») dans le chapitre ; premier **éditeur d'assemblage** du chapitre (sources mêlées, chronologie, objets) |
| **DiagForge** | essai sur une vraie promotion ; première **restitution aux étudiants** (repère par notion, pas de classement, stratégie d'étude sous le seuil) ; lecture des traces SCORM d'ExoForge et de CapsuleForge |
| **Ensemble** | **interface graphique** qui lance toute la suite Forge avec des boutons et des listes (chapitres, sections, profils, micros, langues choisis au lieu d'être tapés), sans ligne de commande ; **cours de démonstration** entièrement fictif qui montre la chaîne complète (questions, exercice, chapitre, bilan) ; licences des éléments embarqués vérifiées |

## Au-delà

- **Voix de synthèse pour les exercices et les questions** (Piper, la voix du cours), au lieu de la voix du navigateur, dont la qualité dépend de l'ordinateur : en option pour un exercice seul, et à étudier pour les exercices intégrés à un chapitre (taille des paquets).
- **Export H5P** (CapsuleForge, puis questions) : scénario à embranchements et vidéo interactive, après validation du SCORM.
- **Skill de création à partir d'un syllabus** : brouillon de banque de questions et de fiches d'exercices, avec un **catalogue d'erreurs types** par domaine (statique, résistance des matériaux, dynamique, calcul, vibrations, fatigue) partagé par QuizForge, ExoForge et DiagForge. Voir {doc}`../skills/creation-syllabus`.
- **Skill d'aide à la préparation des capsules** (découpage, scénario, questions, traduction, relecture).
- **Héritage entre profils** (un profil d'école qui reprend un autre et n'en change que quelques réglages).
- **Traduction** de l'interface du moteur ExoForge dans d'autres langues que l'anglais, et des questions dans Moodle (banques bilingues de QuizForge).
- **Import d'un scénario PowerPoint** en fiche ExoForge.
