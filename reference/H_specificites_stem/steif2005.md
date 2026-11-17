---
cle: steif2005
reference: "Steif, P. S. et Dantzler, J. A. (2005). A Statics Concept Inventory: Development and Psychometric Analysis. Journal of Engineering Education, 94(4), 363-371."
doi: 10.1002/j.2168-9830.2005.tb00864.x
axe: [H2]
type_etude: développement d'un instrument et analyse psychométrique (245 étudiants, 5 universités ; pré-test et post-test dans l'une d'elles)
public: étudiants d'ingénierie en fin de cours de statique (2e année environ), États-Unis
lecture: texte complet, 08/11/2026
regles:
  - outil: QuizForge
    regle: "construire chaque leurre d'une question conceptuelle à partir d'une erreur type nommée, relevée dans des copies, et garder dans la banque le lien leurre -> erreur"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "pour viser un concept, réduire le calcul à une opération triviale : chaque réponse fausse doit être le résultat exact d'un raisonnement faux, pas d'une erreur de calcul"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "ne pas compter sur un QCM pour détecter une erreur que l'on repère par simple comparaison des options (force manquante, action et réaction non opposées) : la tester par une construction (schéma, saisie) plutôt que par un choix"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "regrouper les questions par concept (au moins 3 par concept) et rapporter un sous-score par concept en plus du score global"
    niveau: C
    transferabilite: forte
---

# Un inventaire de concepts en statique (Steif et Dantzler, 2005)

Steif, P. S. et Dantzler, J. A. (2005). A Statics Concept Inventory: Development and Psychometric Analysis. *Journal of Engineering Education*, 94(4), 363-371. [DOI](https://doi.org/10.1002/j.2168-9830.2005.tb00864.x)

**En une phrase.** Un test de 27 QCM à cinq options, dont chaque leurre correspond à une erreur type de statique relevée dans des copies, se montre fiable (alpha 0,89), lié à la note du cours et sensible à l'enseignement ; c'est le modèle d'une banque de QCM où les mauvaises réponses ont un sens diagnostique.

## La source

| | |
| --- | --- |
| **Équipe** | Génie mécanique, Carnegie Mellon (Steif, enseignant de statique) ; société d'évaluation privée (Dantzler, psychométrie). |
| **Nature** | Académique ; aucun financement mentionné dans l'article. Le premier auteur a conçu l'instrument et enseigne dans l'université où ont lieu le pré-test et la validation par les notes. |
| **Support** | *Journal of Engineering Education* (Wiley), revue de référence en enseignement de l'ingénieur. |
| **Audience** | 347 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : 5 questions publiées en exemple, test complet sur demande à l'auteur (p. 371) ; données non publiques. Les indicateurs (difficulté, discrimination, alpha, analyse factorielle confirmatoire) se refont sur nos propres données. |

## Ce que fait l'étude

- **Cadre** (p. 363-364) : quatre groupes de concepts (forces entre corps, équivalence statique, forces aux liaisons, conditions d'équilibre) et 11 erreurs types tirées de copies (oubli d'une force, force interne dans le diagramme du corps libre, couple confondu avec un moment, frottement pris égal à µN, etc.).
- **Questions** (p. 364) : cinq options ; chaque mauvaise réponse est « un calcul juste fondé sur une conception fausse » ; calculs triviaux pour isoler le concept.
- **Test** (p. 367) : 27 questions en 5 catégories (diagramme du corps libre 5, équivalence 3, liaisons 12, frottement 3, équilibre 4), soit 8 concepts.
- **Passations** (p. 367-368) : Carnegie Mellon sur papier en 50 min, avant et après le cours ; quatre autres universités en fin de cours, à distance, sans surveillance ni limite de temps, sans enjeu de note.

## Résultats

- **Échantillon** (p. 368) : 245 étudiants en fin de cours ; moyenne 15,71 sur 27 (écart-type 6,56) ; pas d'écart selon le genre ou l'origine.
- **Questions** (p. 368-369) : difficulté (part de réussite) de 0,31 à 0,85 ; discrimination (tiers supérieur moins tiers inférieur) de 0,26 à 0,84, une seule question sous 0,3.
- **Fiabilité** (p. 369) : alpha de Cronbach 0,89.
- **Validité** (p. 369-370) : corrélation de Spearman de 0,547 entre score et note du cours à Carnegie Mellon (n = 105) ; modèle à 8 facteurs acceptable (GFI 0,90, CFI 0,91, RMSEA 0,067), « avec de la marge ».
- **Pré-post** (tableau 4, p. 370) : à Carnegie Mellon, 10,6 (n = 127) avant, 20,34 (n = 105) après ; réussite en hausse sur chaque question. Les quatre autres universités ont en moyenne environ 12,2 en fin de cours [calcul : (245 × 15,71 − 105 × 20,34) / 140, en supposant les 105 étudiants de Carnegie Mellon inclus dans les 245].
- **Leurres les plus choisis** (p. 370) : frottement pris égal à µN (le tiers inférieur le choisit plus que la bonne réponse sur 2 des 3 questions de frottement) ; en équivalence statique, trois leurres choisis plus que la bonne réponse sur 2 des 3 questions ; force interne dans le diagramme du corps libre ; force supposée parallèle ou perpendiculaire à une barre, ou opposée à la force appliquée.
- **Ce que le QCM ne détecte pas** (p. 365) : l'option où une force manque, et celles qui violent l'action-réaction, sont rarement choisies, alors que ces erreurs sont fréquentes dans les copies : l'étudiant les élimine par comparaison des options.

## Avis critique

**Apport.** Montre qu'une banque de QCM courte, dont chaque leurre code une erreur type de mécanique, fournit une mesure fiable et un diagnostic par concept ; et, point moins cité, qu'un QCM rate les erreurs qu'une simple comparaison des options rend visibles.

**Points forts**
- Leurres ancrés dans une analyse de copies et un cadre conceptuel explicite.
- Indicateurs classiques complets (difficulté, discrimination, alpha, structure factorielle, lien avec la note).
- Limites signalées par les auteurs eux-mêmes (erreurs non détectables, structure factorielle perfectible).

**Réserves**
1. **Importante** — Validation par la note et pré-post dans le seul cours du concepteur (Carnegie Mellon, n = 105) ; les étudiants y réussissent nettement mieux que dans les quatre autres universités [calcul ci-dessus].
2. **Importante** — Passations à distance non surveillées et sans enjeu dans quatre universités : aide extérieure et temps non contrôlés (p. 368).
3. **Mineure** — Pas d'analyse des leurres par étudiant (régularité d'une même erreur) : annoncée pour plus tard (p. 370).
4. **Mineure** — Alpha élevé sur un test qui vise 8 concepts distincts : il dit que le test mesure un tout cohérent, pas que chaque sous-score est fiable.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Un QCM à leurres issus d'erreurs types mesure de façon fiable la compréhension en statique | B | 245 étudiants, 5 universités, alpha 0,89 ; confirmé sur 1 331 passations (fiche `steif2006`) |
| Le score est lié à la réussite au cours | C | Une seule université, celle du concepteur |
| Certaines erreurs ne se détectent pas en QCM (élimination par comparaison) | C | Constat des auteurs sur des versions antérieures, sans chiffres |

**Transférabilité** : forte. Statique de l'ingénieur, celle que nos étudiants de L3 doivent maîtriser ; les erreurs types sont universelles. Le test se ferait en français après traduction.

**Pour conclure, il faudrait** passer une traduction de l'inventaire en début de L3 dans QuizForge et vérifier que les mêmes leurres dominent et que les sous-scores par concept restent cohérents.

## Pour Forge

- **QuizForge** : chaque leurre porte l'étiquette de l'erreur type qu'il code ; la banque de statique commence par les erreurs de cet inventaire (force interne, couple équivalent à une force, frottement = µN, direction imposée par la liaison) (niveau C).
- **QuizForge** : questions conceptuelles à calcul trivial ; le calcul se travaille ailleurs (ExoForge) (niveau C).
- **QuizForge** : pour l'oubli d'une force ou l'action-réaction, demander une construction (tracé ou saisie du diagramme) plutôt qu'un choix parmi des diagrammes (niveau C).
- **DiagForge** : sous-scores par concept, au moins 3 questions par concept ; voir `steif2006` pour leur lien avec les erreurs d'examen (niveau C).
- Renvois : `steif2006` (leurres les plus choisis, 1 331 passations) ; `fakiyesi2024` (place de cet inventaire parmi les autres) ; `slepkov2021` (seuils de discrimination).
