---
cle: schmucker2025
reference: "Schmucker, R. et Moore, S. (2025). The impact of item-writing flaws on difficulty and discrimination in item response theory. Prépublication arXiv:2503.10533."
doi: 10.48550/arxiv.2503.10533
axe: [B1, C]
type_etude: étude corrélationnelle sur 7 126 QCM (réponses de 448 000 élèves), défauts détectés automatiquement
public: QCM de sciences et de mathématiques du collège et du lycée (plateforme CK-12, États-Unis)
lecture: texte complet, 08/11/2026
regles:
  - outil: QuizForge
    regle: "traiter en priorité les défauts les plus liés à une mauvaise discrimination : plusieurs bonnes réponses, bonne réponse la plus longue, « toutes les réponses »"
    niveau: C
    transferabilite: moyenne
  - outil: QuizForge
    regle: "utiliser le nombre de défauts comme filtre avant usage, en particulier pour repérer les questions trop faciles, puis confirmer par l'analyse des réponses"
    niveau: C
    transferabilite: moyenne
---

# Défauts d'écriture et paramètres des items (Schmucker et Moore, 2025)

Schmucker, R. et Moore, S. (2025). The impact of item-writing flaws on difficulty and discrimination in item response theory. Prépublication arXiv:2503.10533. [DOI](https://doi.org/10.48550/arxiv.2503.10533)

**En une phrase.** Sur 7 126 QCM de sciences et de mathématiques passés par 448 000 élèves, plus une question a de défauts d'écriture (détectés automatiquement), moins elle discrimine et plus elle tend à être facile ; les liens sont faibles mais nets, et varient selon la discipline.

## La source

| | |
| --- | --- |
| **Équipe** | Département d'apprentissage automatique et institut d'interaction homme-machine de Carnegie Mellon ; Moore est l'auteur de l'outil de détection utilisé. |
| **Nature** | Académique ; données d'une fondation éducative à but non lucratif (CK-12). |
| **Support** | Prépublication arXiv (version 3, août 2025), non relue. |
| **Audience** | 18 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : outil de détection en libre accès (SAQUET) ; données de la plateforme non publiques. Les références renvoient aux sections. |

## Ce que fait l'étude

- **Données** (§ 3.1-3.2) : questions des sections d'entraînement de la plateforme CK-12 (collège et lycée), en sciences physiques, sciences de la vie et de la Terre, mathématiques ; difficulté et discrimination estimées par un modèle de réponse aux items.
- **Défauts** (§ 3.3-3.4) : 19 critères détectés par l'outil SAQUET (règles, traitement du langage, vérification par GPT-4o) ; pas de validation humaine sur ces données (limite reconnue).
- **Analyses** (§ 3.5) : corrélations, régressions par critère, et modèles de prédiction des paramètres à partir des défauts.

## Résultats

- **Nombre de défauts et discrimination** (§ 4.1) : corrélation r = −0,17 sur l'ensemble ; −0,20 en sciences de la vie et de la Terre ; −0,28 en sciences physiques.
- **Nombre de défauts et difficulté** : faible lien (r = −0,08) : les questions faciles contiennent un peu plus de défauts.
- **Défauts les plus liés à une mauvaise qualité** (§ 4.2) : « plusieurs bonnes réponses », « bonne réponse la plus longue », « toutes les réponses » ; en mathématiques, « toutes les réponses », négation et termes absolus.
- **Filtre** (§ 4.3) : un modèle fondé sur les défauts repère les questions trop faciles avec une précision de 0,80 pour un rappel de 0,47.

## Avis critique

**Apport.** Relie, à très grande échelle, les défauts d'écriture à la qualité mesurée des items : c'est l'argument pour utiliser le contrôle des défauts comme premier filtre avant toute donnée d'étudiants.

**Points forts**
- Très grand corpus, réponses réelles.
- Analyses par discipline et par critère.
- Limites énoncées par les auteurs.

**Réserves**
1. **Importante** — Prépublication non relue.
2. **Importante** — Défauts détectés automatiquement sans contrôle humain sur ce corpus ; l'outil avait un accord de 75 % avec des experts sur l'acceptabilité dans sa validation antérieure (§ 3.4).
3. **Importante** — Étude corrélationnelle : les questions avec défauts peuvent différer par leur contenu ou leur auteur.
4. **Mineure** — Public de collège et de lycée.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les défauts d'écriture vont avec une moins bonne discrimination | C | Grand corpus, lien faible, corrélationnel, prépublication |
| Certains défauts (plusieurs bonnes réponses, bonne réponse la plus longue) pèsent plus | C | Coefficients par critère, détection automatique |

**Transférabilité** : moyenne. Questions de sciences et de mathématiques, mais d'un niveau scolaire.

**Pour conclure, il faudrait** croiser, sur nos propres quiz, le nombre de défauts signalés par QuizForge et la discrimination calculée par DiagForge.

## Pour Forge

- **QuizForge** : ordonner les alertes du contrôle selon leur poids (plusieurs bonnes réponses, bonne réponse la plus longue, « toutes les réponses » d'abord) (niveau C).
- **QuizForge** et **DiagForge** : contrôle des défauts avant usage, puis confirmation par la discrimination après usage (niveau C).
