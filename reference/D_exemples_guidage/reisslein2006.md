---
cle: reisslein2006
reference: "Reisslein, J., Atkinson, R. K., Seeling, P. et Reisslein, M. (2006). Encountering the expertise reversal effect with a computer-based environment on electrical circuit analysis. Learning and Instruction, 16(2), 92-103."
doi: 10.1016/j.learninstruc.2006.02.008
axe: [D2, D1]
type_etude: expérience en classe (185 étudiants), 3 séquences × 2 niveaux de connaissances préalables
public: étudiants d'un cours d'introduction à l'ingénierie électrique (Arizona State University, États-Unis)
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "pour un étudiant débutant sur le type de problème, présenter l'exemple résolu avant le problème ; pour un étudiant déjà à l'aise, proposer le problème d'abord, puis l'exemple comme correction"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "ne pas estomper trop vite pour les débutants : garder au moins une paire exemple-problème complète avant de retirer des étapes"
    niveau: D
    transferabilite: forte
    note: "hypothèse des auteurs pour expliquer un résultat inattendu"
---

# Inversion liée à l'expertise en analyse de circuits électriques (Reisslein et al., 2006)

Reisslein, J., Atkinson, R. K., Seeling, P. et Reisslein, M. (2006). Encountering the expertise reversal effect with a computer-based environment on electrical circuit analysis. *Learning and Instruction*, 16(2), 92-103. [DOI](https://doi.org/10.1016/j.learninstruc.2006.02.008)

**En une phrase.** Chez 185 étudiants d'ingénierie apprenant les circuits série et parallèle, aucune des trois séquences (exemple puis problème, problème puis exemple, estompage) ne l'emporte en moyenne ; mais les débutants réussissent mieux avec l'exemple d'abord, et les étudiants plus avancés avec le problème d'abord, en transfert proche seulement.

## La source

| | |
| --- | --- |
| **Équipe** | Psychologie de l'éducation (Atkinson, spécialiste des exemples résolus) et génie électrique, Arizona State University. |
| **Nature** | Académique ; aucun financement déclaré dans le texte. |
| **Support** | *Learning and Instruction* (Elsevier, EARLI). |
| **Audience** | 148 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : environnement repris de Renkl et al. (2002), problèmes et barème décrits (p. 94-97) ; données non publiées. |

## Ce que fait l'étude

- **Participants** (p. 94) : 185 étudiants d'un cours d'introduction (80 % d'hommes), classés en deux niveaux par un prétest une semaine avant, puis répartis au hasard entre trois séquences.
- **Matériel** (p. 94-97) : environnement informatique sur le calcul de résistances en série et en parallèle ; 8 items (4 par type de circuit) ; séquences exemple-problème, problème-exemple, ou estompage progressif depuis la fin.
- **Mesures** (p. 96-97) : post-test immédiat de transfert proche (même structure, autre habillage) et de transfert lointain (autre ordre d'application des lois) ; séance d'environ 60 min en cours.

## Résultats

- **Séquences** (p. 99-100) : pas de différence en moyenne, ni en temps, ni en transfert proche ou lointain ; l'avantage de l'estompage trouvé en probabilités (Renkl et al., 2002) n'est pas répliqué.
- **Interaction** (p. 99) : en transfert proche, interaction niveau × séquence significative (F(2, 179) = 3,24 ; confirmée en contrôlant le prétest) ; avec l'exemple d'abord, les débutants font aussi bien que les avancés ; avec le problème d'abord, les avancés font nettement mieux que les débutants.
- **Estompage** (p. 102) : résultat inattendu, les débutants en estompage font moins bien qu'avec l'exemple d'abord ; les auteurs supposent un estompage trop rapide.
- **Transfert lointain** (p. 100) : seul le niveau préalable compte (effet grand), pas la séquence.

## Avis critique

**Apport.** Une des rares études d'exemples résolus en ingénierie électrique : elle confirme que le meilleur ordre exemple-problème dépend du niveau, et montre que l'estompage n'est pas toujours supérieur.

**Points forts**
- Grand échantillon en cours réel, en ingénierie.
- Répartition au hasard à l'intérieur de chaque niveau.
- Résultats inattendus discutés franchement (p. 102).

**Réserves**
1. **Importante** — Interaction faible, en transfert proche seulement, et comparaisons simples partiellement conformes aux prédictions.
2. **Importante** — Niveaux définis par la médiane du prétest : la frontière entre débutants et avancés est arbitraire.
3. **Mineure** — Module court (8 items, une séance), post-test immédiat.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| L'ordre exemple-problème le plus efficace dépend du niveau | C | Interaction significative mais faible, transfert proche seulement |
| L'estompage n'est pas supérieur dans ce domaine | C | Une étude, contraire à d'autres |

**Transférabilité** : forte. Étudiants en ingénierie, problèmes de calcul à quelques étapes avec lois physiques, comme nos exercices de mécanique.

**Pour conclure, il faudrait** comparer, dans ExoForge, l'ordre exemple-problème et problème-exemple selon le résultat à un test diagnostique, avec un test différé.

## Pour Forge

- **ExoForge** : choisir l'ordre selon le niveau mesuré : exemple d'abord pour les débutants, problème d'abord (suivi de l'exemple) pour les étudiants plus avancés (niveau C ; voir Kalyuga et Sweller, 2004).
- **ExoForge** : estomper plus lentement pour les débutants (niveau D).
