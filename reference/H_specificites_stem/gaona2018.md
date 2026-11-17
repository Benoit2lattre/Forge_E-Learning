---
cle: gaona2018
reference: "Gaona, J., Reguant, M., Valdivia, I., Vásquez, M. et Sancho-Vinuesa, T. (2018). Feedback by automatic assessment systems used in mathematics homework in the engineering field. Computer Applications in Engineering Education, 26(4), 994-1007."
doi: 10.1002/cae.21950
axe: [H1]
type_etude: quasi-expérimentation à grande échelle, mode de retour (immédiat ou différé) tiré au sort par classe (229 classes, 5 507 étudiants), traces Moodle sur un semestre
public: étudiants de 1re année en ingénierie, cours de mise à niveau Mathématiques I, INACAP (Chili), quatre campus
lecture: texte complet, 10/11/2026
regles:
  - outil: QuizForge
    regle: "quiz d'entraînement à tentatives illimitées notés sur la meilleure tentative : préférer le retour différé (correction après envoi de toute la série) au retour immédiat question par question, ou rendre coûteux l'abandon d'une tentative"
    niveau: C
    transferabilite: moyenne
    note: "avec retour immédiat, les étudiants recommencent la tentative dès la première erreur (p. 1002) ; aucune mesure d'apprentissage hors plateforme"
  - outil: ExoForge
    regle: "comparer la réponse saisie à la clé par équivalence mathématique (0,5 et 1/2 ; x/2 + y/2 et (x + y)/2), en contrôlant à part la forme demandée (simplifiée, factorisée)"
    niveau: D
    transferabilite: forte
  - outil: DiagForge
    regle: "rapporter par quiz le nombre de tentatives, le temps passé, la moyenne de toutes les tentatives et la meilleure note, et la part des tentatives abandonnées avant la fin ; ne pas lire la meilleure note seule"
    niveau: C
    transferabilite: forte
---

# Retour immédiat ou différé dans des devoirs de mathématiques en ligne (Gaona et al., 2018)

Gaona, J., Reguant, M., Valdivia, I., Vásquez, M. et Sancho-Vinuesa, T. (2018). Feedback by automatic assessment systems used in mathematics homework in the engineering field. *Computer Applications in Engineering Education*, 26(4), 994-1007. [DOI](https://doi.org/10.1002/cae.21950)

**En une phrase.** Sur 5 507 étudiants de première année d'ingénierie, des quiz Moodle à paramètres aléatoires (WIRIS) en retour immédiat suscitent plus de tentatives et de temps qu'en retour différé, pour une meilleure note à peine plus haute (+0,6 à +3,7 points sur 100) et une moyenne des tentatives plus basse, parce que les étudiants recommencent dès la première erreur ; aucun effet sur l'apprentissage n'est mesuré.

## La source

| | |
| --- | --- |
| **Équipe** | Université Paris Diderot (LDAR), INACAP (Chili), université de Barcelone, Université ouverte de Catalogne (p. 994). |
| **Nature** | Académique ; financé par le centre d'innovation pédagogique de l'INACAP, projet SEDOL-M (p. 994, 1006). Les auteurs évaluent un dispositif de leur institution. |
| **Support** | *Computer Applications in Engineering Education* (Wiley). |
| **Audience** | 26 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Moyenne : règles du dispositif décrites (p. 998-999), tableaux de moyennes et écarts-types publiés (tableaux 2 à 6) ; questions et données non publiées. Les chiffres se vérifient sur les tableaux. |

## Ce que fait l'étude

- **Dispositif** (p. 995-996) : questions Moodle avec la calculatrice WIRIS, paramètres aléatoires ; plus de 95 % à réponse courte, comparée par calcul formel (équivalences 0,5 et 1/2, 1 + tan²x et sec²x ; contrôle de la forme simplifiée ou factorisée). Après réponse : juste ou faux, puis solution pas à pas calculée avec les paramètres tirés.
- **Conditions** (p. 996) : retour immédiat (bouton « vérifier » après chaque question) ou différé (juste ou faux et solution après envoi de tout le quiz).
- **Population** (p. 999, tableau 1) : 229 classes, 59 enseignants, 5 507 étudiants (2 808 en immédiat, 2 699 en différé) ; mode tiré au sort par classe (115 et 114 classes).
- **Règles communes** (p. 999) : 7 quiz de 6 questions sur quatre thèmes (algèbre, équations et systèmes, polynômes, exponentielles et logarithmes), ouverts trois semaines, tentatives illimitées, note = meilleure tentative, travail hors classe.
- **Mesures** (p. 998-999) : participation par classe, tentatives, temps, moyenne de toutes les tentatives et meilleure note par étudiant ; tests de Mann-Whitney.

## Résultats

| Indicateur (par étudiant et par quiz) | Différé | Immédiat | Page |
| --- | --- | --- | --- |
| Participation (classes) | 56,8 à 81,0 % | 59,0 à 77,7 % | p. 1000, tableau 2, aucune différence significative |
| Tentatives (moyenne) | 2,41 à 4,07 | 2,64 à 4,84 | p. 1002, tableau 3, significatif sur 6 quiz sur 7 |
| Temps (min) | 73,9 à 140,0 | 87,0 à 172,7 | p. 1003, tableau 4, +21 à +39 min [calcul] |
| Moyenne de toutes les tentatives (sur 100) | 42,4 à 68,1 | 36,1 à 64,1 | p. 1004, tableau 5, plus basse de 2,8 à 6,3 points en immédiat [calcul] |
| Meilleure note (sur 100) | 65,1 à 84,8 | 68,8 à 85,4 | p. 1005, tableau 6, +0,6 à +3,7 points en immédiat |

- **Taille des écarts** : sur la meilleure note, d d'environ 0,02 (algèbre Q2 : 85,4 contre 84,8, écarts-types 26,6 et 25,9) à 0,12 (polynômes Q2 : 74,1 contre 70,5, écarts-types 29,8 et 30,9) [calcul] ; sur la moyenne des tentatives, d d'environ 0,12 à 0,23 [calcul, mêmes tableaux].
- **Comportement** (p. 996-997, 1002) : déjà au pilote de 2016, puis selon les enseignants, en retour immédiat les étudiants abandonnent la tentative à la première réponse fausse et recommencent, car une tentative ne coûte rien ; le travail se concentre sur les premières questions.
- **Conclusion des auteurs** (p. 1005) : participation moyenne 68,67 % sans effet du mode ; le retour différé leur paraît plus adapté à un système d'étude.

## Avis critique

**Apport.** Un des rares essais à grande échelle sur un réglage concret de quiz Moodle à paramètres aléatoires en mathématiques d'ingénieur : avec tentatives illimitées et meilleure note retenue, le retour immédiat change la stratégie des étudiants plus que leur note.

**Points forts**
- Tirage au sort du mode par classe, sur 229 classes et un semestre réel.
- Plusieurs indicateurs, dont la moyenne de toutes les tentatives, qui révèle la stratégie de recommencement.
- Tableaux complets (effectifs, moyennes, écarts-types).

**Réserves**
1. **Majeure** — Aucune mesure d'apprentissage hors plateforme (examen, test différé) : on compare des comportements et des notes de quiz, pas des acquis.
2. **Majeure** — Tirage au sort par classe mais tests au niveau de l'étudiant, sans tenir compte du regroupement par classe et par enseignant : les p très petits surestiment la certitude.
3. **Importante** — Le mécanisme (abandon à la première erreur, travail sur les premières questions) vient de témoignages d'enseignants ; la part des tentatives abandonnées n'est pas mesurée dans les traces.
4. **Mineure** — 111 et 113 classes au tableau 2 contre 114 et 115 annoncées (p. 999-1000) ; « groupes équivalents » affirmés sans prétest (p. 998).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Le retour immédiat augmente tentatives et temps sur la plateforme | B | Tirage par classe, grand effectif, écarts concordants sur 6 à 7 quiz ; regroupement ignoré |
| Avec tentatives illimitées, les étudiants recommencent dès la première erreur | C | Témoignages d'enseignants, cohérent avec la moyenne des tentatives plus basse |
| Le retour différé est préférable pour apprendre | D | Interprétation des auteurs, aucune mesure d'apprentissage |

**Transférabilité** : moyenne. Mathématiques de mise à niveau en première année, loin du M2, mais réglages Moodle identiques aux nôtres.

**Pour conclure, il faudrait** tirer au sort, dans QuizForge, le mode de retour d'un quiz d'entraînement entre groupes de TD, journaliser les tentatives abandonnées, et comparer les notes à un examen commun.

## Pour Forge

- **QuizForge** : en entraînement à tentatives illimitées notées sur la meilleure, retour différé par défaut, ou pénalité ou nombre limité de tentatives en mode immédiat (niveau C).
- **ExoForge** : comparaison par équivalence mathématique, avec contrôle séparé de la forme attendue (niveau D, description du dispositif).
- **DiagForge** : tentatives, temps, moyenne des tentatives et meilleure note côte à côte, part des tentatives abandonnées (niveau C).
- Renvois : `gill2007` (réponses au hasard pour voir le retour en formatif) ; `davies2024` (politique de retour incohérente entre modules) ; fiches de l'axe sur le moment du retour.
