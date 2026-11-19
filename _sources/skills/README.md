# Skills : l'aide d'un assistant d'IA autour de Forge

Un *skill* est un ensemble d'instructions et de fichiers de référence qu'un assistant d'IA (ici [Claude](https://claude.ai), d'Anthropic) charge quand une tâche s'y prête : il décrit une méthode, les fichiers à lire, le format attendu et les contrôles à faire. Les outils Forge sont des programmes ordinaires, qui fonctionnent sans IA ; les skills décrits ici aident l'enseignant **autour** des outils : lire la recherche, préparer des brouillons de questions, préparer une capsule, mettre le site au propre.

| Skill | Utilité | État |
| --- | --- | --- |
| {doc}`critique-pedagogie` | lecture critique d'un article de recherche en éducation et fiche de lecture au format Forge | existe (utilisé pour les 197 fiches) |
| {doc}`creation-syllabus` | brouillon de banque de questions QuizForge et de fiches ExoForge à partir d'un syllabus | en projet (cahier des charges écrit) |
| {doc}`preparation-capsules` | aide à la préparation d'un chapitre CapsuleForge : découpage, scénario, questions, traduction, relecture | en projet |
| {doc}`finition-site` | remise au propre du dépôt et du site avant une version publique | existe (adaptation d'un skill de finition de documentation) ; source dans `skills/finition-site/` |

## Ce qu'un skill ne remplace pas

Tout ce qu'un assistant d'IA écrit est un **brouillon**. La bibliographie de Forge en donne les raisons, chiffres à l'appui :

- des QCM écrits par une IA puis acceptés ou retouchés par l'enseignant comportent plus de défauts d'écriture que ceux écrits par l'enseignant seul, et l'on relit moins un texte proposé par l'IA ({cite}`menze2026`) ;
- les leurres proposés par une IA sont souvent valides mais peu plausibles, et anticipent mal les erreurs réelles des étudiants ({cite}`feng2024`) ;
- un contrôle automatique retrouve une bonne part des défauts d'écriture, mais ce n'est pas un verdict ({cite}`moore2023`) ;
- des hypothèses d'erreur rédigées par une IA sont plausibles, sans que leur exactitude soit vérifiée ({cite}`parker2026`).

D'où trois règles communes à tous les skills Forge : les valeurs numériques (clé, erreurs types) sont **recalculées par du code**, jamais reprises du texte de l'IA ; chaque question est **relue par l'enseignant**, critère par critère, avant d'entrer dans une banque ; une question d'examen est en plus **relue par un collègue** ({cite}`hye2025`).

## Autres pistes

- **Catalogue d'erreurs types par domaine** (statique, résistance des matériaux, dynamique, calcul, vibrations, fatigue…) : prévu avec le skill de création à partir d'un syllabus, pour coder chaque leurre par une erreur nommée et la retrouver dans DiagForge.
- **Lecture d'un bilan DiagForge** : aider à passer des indicateurs à une décision (question à revoir, notion à reprendre en cours), dans le respect des règles de restitution de l'axe G.
- **Écriture d'une fiche ExoForge** à partir d'un scénario PowerPoint (une diapositive par étape).
