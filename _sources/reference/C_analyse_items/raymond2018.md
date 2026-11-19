---
cle: raymond2018
reference: "Raymond, M. R., Stevens, C. et Bucak, S. D. (2019). The optimal number of options for multiple-choice questions on high-stakes tests: Application of a revised index for detecting nonfunctional distractors. Advances in Health Sciences Education, 24(1), 141-150."
doi: 10.1007/s10459-018-9855-9
axe: [C2]
type_etude: analyse de 840 QCM à 5 options (4 formes d'un examen de licence médicale, environ 1 200 candidats par forme) et simulation de retrait de leurres
public: candidats à l'examen américain de licence de médecin
lecture: texte complet, 08/11/2026
regles:
  - outil: DiagForge
    regle: "déclarer un leurre non fonctionnel avec un seuil qui dépend de la réussite de la question, seuil = 0,1 × (1 − réussite), et non avec un seuil fixe de 5 %"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "ne pas signaler comme défaut les leurres peu choisis d'une question très réussie : peu d'étudiants se trompent, donc peu peuvent choisir chaque leurre"
    niveau: B
    transferabilite: forte
  - outil: QuizForge
    regle: "retirer le leurre le moins choisi ne change presque pas la fiabilité : passer à 3 ou 4 options sans craindre de perte de mesure"
    niveau: C
    transferabilite: moyenne
---

# Un seuil de leurre non fonctionnel qui dépend de la difficulté (Raymond et al., 2018)

Raymond, M. R., Stevens, C. et Bucak, S. D. (2019). The optimal number of options for multiple-choice questions on high-stakes tests: Application of a revised index for detecting nonfunctional distractors. *Advances in Health Sciences Education*, 24(1), 141-150. [DOI](https://doi.org/10.1007/s10459-018-9855-9)

**En une phrase.** La règle « un leurre choisi par moins de 5 % est inutile » pénalise les questions faciles ; avec un seuil qui baisse quand la réussite monte, la part de leurres non fonctionnels passe de 59 % à 35 % sur 840 QCM d'un examen médical, et près de la moitié des questions gardent trois leurres utiles.

## La source

| | |
| --- | --- |
| **Équipe** | National Board of Medical Examiners (Philadelphie), organisme qui conçoit l'examen étudié. |
| **Nature** | Organisme d'examen ; les auteurs analysent leurs propres items. |
| **Support** | *Advances in Health Sciences Education* (Springer) ; en ligne en 2018, volume 2019. |
| **Audience** | 62 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Bonne pour la méthode (formule unique, simulation décrite p. 143-144) ; données non publiques. |

## Ce que fait l'étude

- **Données** (p. 143) : 840 QCM à 5 options, réussite moyenne 0,74, alpha 0,88 par forme.
- **Seuil proposé** (p. 143-144) : un leurre est non fonctionnel s'il est choisi par moins de 0,1 × (1 − réussite) des candidats : 0,09 pour une réussite de 0,10, 0,05 pour 0,50, 0,01 pour 0,90.
- **Simulation** : retrait d'un ou deux leurres (le moins choisi ou au hasard) et effet sur la difficulté et la fiabilité.

## Résultats

- **Leurres non fonctionnels** (tableau 1, p. 145) : 58,9 % avec le seuil de 5 %, 34,7 % avec le seuil proposé ; 5,9 % seulement ont une corrélation positive avec le score.
- **Leurres utiles par question** (tableau 2) : avec 5 %, 13 % des questions ont trois ou quatre leurres utiles ; avec le seuil proposé, 47 %.
- **Explication** (p. 142-143) : si 82 % réussissent et que les erreurs se répartissent également sur 4 leurres, chacun attire 4,5 % et tous seraient déclarés inutiles ; au-dessus de 90 % de réussite, un seul leurre au plus peut être « utile ».
- **Retrait de leurres** (tableau 3, p. 146) : retirer le leurre le moins choisi fait passer l'alpha de 0,884 à 0,880 ; en retirer deux au hasard, à 0,855.

## Avis critique

**Apport.** Corrige un défaut de la règle des 5 % utilisée partout (y compris dans les seuils envisagés pour DiagForge) : le seuil doit tenir compte du nombre d'étudiants qui se trompent.

**Points forts**
- Formule simple, facile à programmer.
- Grand nombre de candidats par question, quatre formes.

**Réserves**
1. **Importante** — Le seuil proposé est un choix raisonné, pas validé par un critère externe (les leurres « utiles » ne sont pas vérifiés autrement).
2. **Importante** — Examen professionnel à questions faciles et très relues, avec plus de 1 000 candidats : avec 30 étudiants, un seuil de 1 à 5 % correspond à moins d'une ou deux personnes.
3. **Mineure** — Simulation du retrait de leurres (réponses réattribuées au hasard), pas expérience réelle.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Le seuil fixe de 5 % dépend mécaniquement de la difficulté | B | Argument arithmétique, confirmé sur les données |
| Seuil 0,1 × (1 − réussite) | C | Proposition raisonnée, une application |
| Retirer le leurre le moins choisi ne nuit pas à la fiabilité | B | Concordant avec Rodriguez (2005) et Sridharan et Sivaramakrishnan (2025) |

**Transférabilité** : forte pour le principe ; à nos effectifs (30 à 100 étudiants), raisonner plutôt en nombre d'étudiants qu'en pourcentage.

**Pour conclure, il faudrait** comparer, sur nos quiz, les leurres signalés par la règle des 5 % et par le seuil proposé.

## Pour Forge

- **DiagForge** : seuil de leurre non fonctionnel 0,1 × (1 − réussite), avec un minimum d'étudiants ayant échoué à la question avant toute alerte (niveau C).
- **DiagForge** : pas d'alerte « leurre peu choisi » pour une question réussie à plus de 90 % (niveau B).
- **QuizForge** : le leurre le moins choisi est le premier candidat à la suppression (niveau C ; voir Sridharan et Sivaramakrishnan, 2025).
