---
cle: mertens2025
reference: "Mertens, U. et Lindner, M. A. (2025). Computer-based answer-until-correct and elaborated feedback: Effects on affective-motivational and performance outcomes. Journal of Computer Assisted Learning, 41(2), e13112."
doi: 10.1111/jcal.13112
axe: [A2, A3]
type_etude: expérience intra-sujet (carré latin), une séance en ligne, test différé de quelques minutes
public: 97 étudiants d'une université allemande (questions de biologie, chimie et physique du secondaire)
lecture: texte complet, 09/11/2026
regles:
  - outil: QuizForge
    regle: "pour un quiz d'entraînement, plusieurs essais sans indice ni explication font presque aussi bien qu'une explication immédiate pour corriger les erreurs ; en mode interactif, prévoir au moins une rétroaction générale explicative affichée une fois la question terminée"
    niveau: C
    transferabilite: moyenne
    note: "rappel immédiat : explication 10,2/12, essais multiples 9,34/12, sans retour 4,86/12 ; correction des erreurs équivalente ; la combinaison essais multiples + explication finale n'est pas testée (D)"
  - outil: QuizForge
    regle: "ne jamais laisser une question d'entraînement sans rétroaction : tout retour (explication ou nouvel essai) améliore le rappel et le ressenti par rapport à aucun retour, y compris après une erreur"
    niveau: C
    transferabilite: moyenne
  - outil: ExoForge
    regle: "après des échecs répétés à une étape, passer d'un simple nouvel essai à une explication : les essais répétés sans aide sont un peu plus coûteux et frustrants après une erreur"
    niveau: C
    transferabilite: moyenne
    note: "écarts très faibles (d de 0,06 à 0,10) ; questions factuelles, pas de calcul"
---

# Essais jusqu'à la bonne réponse ou explication (Mertens et Lindner, 2025)

Mertens, U. et Lindner, M. A. (2025). Computer-based answer-until-correct and elaborated feedback: Effects on affective-motivational and performance outcomes. *Journal of Computer Assisted Learning*, 41(2), e13112. [DOI](https://doi.org/10.1111/jcal.13112)

**En une phrase.** Dans un test de 36 QCM difficiles, répondre jusqu'à trouver la bonne réponse (essais multiples avec juste/faux) et recevoir tout de suite une explication améliorent tous deux fortement le rappel par rapport à aucun retour ; l'explication fait un peu mieux au rappel et rend l'erreur moins pénible, mais les deux corrigent autant d'erreurs.

## La source

| | |
| --- | --- |
| **Équipe** | Institut Leibniz pour l'enseignement des sciences et des mathématiques (IPN, Kiel) et université européenne de Flensbourg ; groupe de recherche sur la cognition et la motivation dans les tests. |
| **Nature** | Académique ; financement de l'association Leibniz (p. 1) ; pas de conflit d'intérêts déclaré (p. 13). |
| **Support** | *Journal of Computer Assisted Learning* (Wiley), libre accès. |
| **Audience** | 7 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Moyenne : protocole, items d'exemple et questionnaires en annexe ; la note d'auteur annonce données et code en dépôt en ligne (p. 1), la déclaration finale dit « sur demande » (p. 13). Étude non préenregistrée (p. 12). Les pages citées sont celles de l'article (« N of 16 »). |

## Ce que fait l'étude

- **Public** (p. 5-6) : 104 étudiants recrutés, 97 analysés (4 exclus pour réponses trop rapides sur plus de 25 % des items, 1 pour temps aberrant, 2 hors critères).
- **Matériel** (p. 6) : 36 QCM à 4 options sur des notions du secondaire (biologie 64 %, chimie 19 %, physique 17 %), choisis pour leur difficulté (réussite moyenne 0,38 au test de traitement).
- **Conditions** (p. 5-6) : chaque étudiant voit 12 items dans chaque condition (carré latin, ordre des items tiré au hasard) : sans retour ; explication (EF : bonne réponse en vert, réponse fausse en rouge, une phrase d'explication, un seul essai) ; essais jusqu'à la bonne réponse (AUC : juste/faux, nouvel essai, les options fausses restent en rouge, sans explication).
- **Mesures** (p. 6, 8) : après chaque item, émotions (plaisir, fierté, colère, frustration) et utilité perçue sur échelle de 1 à 5 ; puis test final sur les mêmes 36 items, options remélangées, sans retour, juste après (séance de 51 min au total). Seul le premier essai compte dans la condition AUC.

## Résultats

- **Rappel** (tableau 1, p. 8) : sur 12 items par condition, sans retour 4,86 (ET 1,87), EF 10,2 (1,81), AUC 9,34 (2,19). EF > AUC (z = −4,68, p < 0,001) ; les auteurs donnent d = −0,08 (p. 8) ; à partir des moyennes et écarts-types du tableau, l'écart de 0,86 item correspond à d ≈ 0,43 [calcul : (10,2 − 9,34) / 2,01, sans tenir compte de l'appariement].
- **Correction des erreurs** (tableau 1, p. 8) : items faux au premier essai puis justes au test final : sans retour 0,83, EF 5,94, AUC 5,78 ; EF = AUC (z = −0,61, p = 0,81).
- **Émotions** (p. 10) : après une bonne réponse, forte hausse des émotions positives avec EF et AUC (η² partiel 0,20 et 0,18) ; après une erreur, petite hausse aussi (0,02), contrairement à l'hypothèse d'un effet négatif. Émotions négatives après une erreur : légère baisse avec EF, pas d'effet avec AUC ; EF < AUC (d = 0,10).
- **Utilité perçue** (p. 10-11) : connaissances acquises et utilité plus élevées avec retour qu'en son absence ; EF jugée un peu plus utile qu'AUC après une erreur (d = −0,10) ; coût perçu légèrement plus élevé avec AUC après une erreur (η² partiel 0,005), faible partout.

## Avis critique

**Apport.** Comparaison directe, chez des étudiants, des deux réglages courants dans Moodle (explication immédiate et essais multiples) sur la performance et le ressenti ; elle lève la crainte que les essais multiples découragent : l'effet sur les émotions reste meilleur que sans retour.

**Points forts**
- Plan intra-sujet équilibré (carré latin, ordre aléatoire, livret en covariable), modèles mixtes étudiants x items.
- Mesure du ressenti après chaque item, distinguée selon que la réponse était juste ou fausse.
- Matériel et questionnaires publiés.

**Réserves**
1. **Majeure** — Le test final reprend les mêmes questions quelques minutes après : c'est du rappel immédiat, pas de l'apprentissage durable ni du transfert (les auteurs demandent des études longitudinales, p. 13).
2. **Importante** — EF et AUC diffèrent par deux choses : l'explication et le fait de chercher soi-même. On ne sait pas ce que donnerait AUC suivi d'une explication, réglage pourtant possible dans Moodle.
3. **Importante** — Questions factuelles à 4 options ; avec AUC, la bonne réponse finit toujours par apparaître par élimination. Les auteurs notent que des problèmes à résoudre pourraient donner un autre résultat (p. 13).
4. **Mineure** — Tailles d'effet difficiles à lire : d = −0,08 annoncé pour un écart de 0,86 item sur 12 ; fiabilité modeste des tests (ω = 0,62 et 0,65, p. 6) ; incohérence sur l'accès aux données.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Explication ou essais multiples > aucun retour pour le rappel immédiat | B | Effet très grand, plan contrôlé, mais même séance et mêmes questions |
| Explication > essais multiples pour le rappel | C | Écart faible, rappel immédiat, une seule étude |
| Correction des erreurs équivalente | C | Absence de différence, 97 étudiants |
| Les essais multiples ne nuisent pas au ressenti par rapport à aucun retour | C | Auto-évaluations, une séance |

**Transférabilité** : moyenne. Étudiants d'université et questionnaire en ligne proches de nos quiz ; contenu factuel de niveau secondaire, éloigné de nos problèmes de mécanique.

**Pour conclure, il faudrait** comparer dans QuizForge trois réglages tirés au sort (explication immédiate ; interactif à plusieurs essais sans indice ; interactif avec indices puis explication) sur des questions de calcul, avec un test une semaine plus tard sur des questions nouvelles.

## Pour Forge

- **QuizForge** : en mode Moodle « interactif avec plusieurs essais », les essais multiples sans indice corrigent presque autant d'erreurs qu'une explication ; ajouter une rétroaction générale explicative, affichée une fois la question terminée, réunit les deux (niveau C pour la comparaison, D pour la combinaison).
- **QuizForge** : toujours une rétroaction en entraînement (niveau C ici ; voir [vanderkleij2015](vanderkleij2015.md)).
- **ExoForge** : après deux échecs à une étape, montrer indice ou explication plutôt qu'un nouvel essai nu (niveau C, écarts très faibles).
- Cohérent avec [schwerter2022](schwerter2022.md) : des indices entre les essais font mieux que la bonne réponse donnée tout de suite ; ici, les essais sans indice font un peu moins bien que l'explication. Voir aussi [slepkov2019](slepkov2019.md) pour le crédit partiel des essais multiples.
