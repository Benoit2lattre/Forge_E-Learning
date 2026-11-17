# Prochaines étapes

Un plan grossier, outil par outil, de la version 0.2 vers la 0.3 puis au-delà. Les priorités peuvent changer avec les essais en cours.

## Court terme : vers la version 0.3

| Outil | Prochaines étapes |
| --- | --- |
| **CapsuleForge** | essai dans Moodle de l'**export SCORM 1.2** (Moodle ne prend officiellement en charge que SCORM 1.2) ; afficher le **caméo** (vidéo de l'enseignant en médaillon) dans le lecteur, calé sur le pas, puis recaler un caméo filmé à part par comparaison des sons ; jouer une **simulation ActivePresenter** (gestes, mode « À vous ») dans le chapitre ; premier **éditeur d'assemblage** du chapitre (sources mêlées, chronologie, objets) |
| **QuizForge** | rappel des réglages Moodle conseillés selon l'usage (classe ou examen), avec une alerte contre la combinaison tentatives multiples, meilleure note et relecture question par question ; pénalité par essai ; classeurs d'exemple régénérés |
| **ExoForge** | fonction Φ (loi normale) dans les expressions ; rejet des tirages où une erreur type donne la bonne réponse ; retour gradué ; journal SCORM détaillé ; mode d'emploi à jour |
| **DiagForge** | essai sur une vraie promotion ; première **restitution aux étudiants** (repère par notion, pas de classement, stratégie d'étude sous le seuil) ; lecture des traces SCORM d'ExoForge et de CapsuleForge |
| **Ensemble** | site publié (branche `gh-pages`) ; **cours de démonstration** entièrement fictif qui montre la chaîne complète (questions, exercice, chapitre, bilan) ; licences des éléments embarqués vérifiées |

## Au-delà

- **Export H5P** (CapsuleForge, puis questions) : scénario à embranchements et vidéo interactive, après validation du SCORM.
- **Skill de création à partir d'un syllabus** : brouillon de banque de questions et de fiches d'exercices, avec un **catalogue d'erreurs types** par domaine (statique, résistance des matériaux, dynamique, calcul, vibrations, fatigue) partagé par QuizForge, ExoForge et DiagForge. Voir {doc}`../skills/creation-syllabus`.
- **Skill d'aide à la préparation des capsules** (découpage, scénario, questions, traduction, relecture).
- **Thème modifiable** des lecteurs (couleurs et polices du profil) et héritage entre profils.
- **Traduction** de l'interface du moteur ExoForge dans d'autres langues que l'anglais, et des questions dans Moodle (banques bilingues de QuizForge).
- **Import d'un scénario PowerPoint** en fiche ExoForge.
