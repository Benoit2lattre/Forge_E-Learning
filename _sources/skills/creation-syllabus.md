# Création de quiz et d'exercices à partir d'un syllabus

**État : en projet.** Le cahier des charges est écrit ; le skill n'est pas encore construit ni essayé.

## Utilité

À partir du syllabus d'un cours (et si possible de ses supports), produire en quelques passages validés par l'enseignant un **brouillon** de banque de questions et d'exercices qui respecte d'emblée les règles des fiches : chaque leurre code une erreur type nommée, chaque question porte une rétroaction explicative, les quiz de séance font revenir les séances précédentes.

## Entrées et sorties

| Entrées | Sorties |
| --- | --- |
| syllabus (notions, séances), supports du cours si disponibles, profil Forge (barème, tirage des questions), usage visé (quiz en classe ou quiz d'examen) | classeur QuizForge (onglets de questions, plus onglets de travail « Notions » et « Erreurs »), fiches ExoForge (une par notion de calcul), rapport de passage (notions, erreurs visées, contrôles faits, points à relire), propositions d'ajout au catalogue d'erreurs types |

Parcours prévu : syllabus → notions → plan de questions → rédaction du classeur → rédaction des fiches → `quizforge valider` → conversion → essai en classe et lecture des résultats dans DiagForge.

## Ce qu'il ne fera pas

- Il ne dépose rien dans Moodle et ne règle pas les tests : il rappelle les réglages conseillés selon l'usage (classe ou examen).
- Il ne range aucune question dans une banque sans relecture : tout ce qu'il écrit a le statut « brouillon ».
- Il ne présente jamais une erreur type proposée par l'IA comme validée : elle reste une « hypothèse » tant que la littérature ou les réponses des étudiants ne la confirment pas.
- Il ne fabrique pas les questions sur image (le projet du pointeur de zones reste fait à la main) ni les questions à données tirées (elles relèvent d'ExoForge).
- Ce n'est pas un système tutoriel intelligent : il produit du contenu, il n'adapte rien à l'étudiant.

## Limites

Les limites des questions écrites par une IA (voir {doc}`README`) s'appliquent pleinement : clé et erreurs numériques recalculées par du code ; relecture active de chaque question par l'enseignant ; relecture par un collègue avant un examen. Le protocole d'essai prévu compare les questions produites à une banque existante et à de nouvelles notions, puis les essaie en classe avec DiagForge.
