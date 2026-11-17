---
cle: moore2023
reference: "Moore, S., Nguyen, H. A., Chen, T. et Stamper, J. (2023). Assessing the quality of multiple-choice questions using GPT-4 and rule-based methods. Prépublication arXiv:2307.08161 (conférence EC-TEL 2023)."
doi: 10.48550/arxiv.2307.08161
axe: [B1]
type_etude: comparaison de deux méthodes de détection automatique à une évaluation humaine (200 QCM)
public: QCM écrits par des étudiants de premier cycle (chimie, biochimie, statistique, travail en équipe), États-Unis
lecture: texte complet, 08/11/2026
regles:
  - outil: QuizForge
    regle: "détecter par des règles simples (et non par un modèle de langue seul) les défauts de forme : « aucune » ou « toutes les réponses », négation, bonne réponse la plus longue, mots repris, termes absolus, options numériques hors d'ordre"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "présenter le contrôle automatique comme une aide à la relecture, pas comme un verdict : la détection des leurres peu plausibles, des indices logiques et des bonnes réponses multiples reste peu fiable"
    niveau: C
    transferabilite: forte
---

# Détecter automatiquement les défauts des QCM (Moore et al., 2023)

Moore, S., Nguyen, H. A., Chen, T. et Stamper, J. (2023). Assessing the quality of multiple-choice questions using GPT-4 and rule-based methods. Prépublication arXiv:2307.08161 (conférence EC-TEL 2023). [DOI](https://doi.org/10.48550/arxiv.2307.08161)

**En une phrase.** Sur 200 QCM écrits par des étudiants, une méthode à base de règles retrouve 91 % des défauts relevés par deux experts, contre 79 % pour GPT-4 seul ; mais aucune des deux ne reproduit l'avis complet des experts sur une question (accord total sur les 19 critères dans 15 % et 12 % des cas).

## La source

| | |
| --- | --- |
| **Équipe** | Institut d'interaction homme-machine de Carnegie Mellon (Stamper), production de questions par les étudiants. |
| **Nature** | Académique ; les auteurs évaluent leur propre méthode. |
| **Support** | Prépublication arXiv correspondant à une communication de conférence (EC-TEL 2023). |
| **Audience** | 48 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Bonne pour la méthode : code publié sur GitHub ; questions des étudiants sur demande. Les références renvoient aux sections. |

## Ce que fait l'étude

- **Données** (§ 3.1) : 50 QCM tirés au hasard dans chacun de quatre cours (chimie, biochimie, statistique, travail collaboratif), écrits par des étudiants de premier cycle sans aide.
- **Référence humaine** (§ 3.2) : deux experts appliquent une grille de 19 défauts (accord de 87,5 à 100 %, κ de 0,66 à 1) puis s'accordent ; une question est « acceptable » avec 0 ou 1 défaut.
- **Méthodes** : un script par critère (règles sur le texte, outils de traitement du langage, modèles de langue pour les critères difficiles) (§ 3.3) ; GPT-4 interrogé critère par critère (§ 3.4).

## Résultats

- **Défauts retrouvés** : 91 % pour les règles, 79 % pour GPT-4 (résumé).
- **Accord question par question** : les 19 critères identiques à l'avis humain pour 15 % (règles) et 12 % (GPT-4) des questions (§ 4).
- **Acceptable ou non** : accord avec les experts pour 65 % (règles) et 62 % (GPT-4) des questions ; GPT-4 juge plus souvent les questions inacceptables (§ 4).
- **Par critère** : bons résultats pour « aucune des réponses » et la négation ; mauvais pour les indices logiques et les bonnes réponses multiples (§ 4).

## Avis critique

**Apport.** Montre qu'une grande partie des défauts de forme se détecte par des règles simples et transparentes, mieux qu'avec un modèle de langue seul ; c'est le cœur d'un contrôle automatique dans QuizForge.

**Points forts**
- Référence humaine solide (deux experts, accord mesuré).
- Code publié, réutilisable.
- Résultats détaillés par critère.

**Réserves**
1. **Importante** — Le taux de 91 % porte sur les défauts trouvés ; l'accord complet par question est faible et la décision « acceptable ou non » n'est juste qu'aux deux tiers.
2. **Importante** — Questions écrites par des étudiants, souvent factuelles ; les questions de calcul ne sont pas étudiées.
3. **Mineure** — Prépublication d'une communication courte ; prompts de GPT-4 non optimisés (choix assumé, § 3.4).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les défauts de forme se détectent bien par des règles | C | Une étude, 200 questions, référence humaine solide |
| La détection automatique ne remplace pas la relecture | C | Faible accord complet par question |

**Transférabilité** : forte pour les défauts de forme, qui ne dépendent pas de la discipline ; faible pour les critères liés au contenu (plausibilité des leurres en mécanique).

**Pour conclure, il faudrait** mesurer l'accord du contrôle de QuizForge avec la relecture d'un collègue sur nos propres QCM.

## Pour Forge

- **QuizForge** : contrôle par règles des défauts de forme (niveau C), en reprenant au besoin le code publié.
- **QuizForge** : afficher le résultat comme une liste de points à vérifier, la relecture humaine restant indispensable (niveau C ; voir Menze et al., 2026, et Hye et al., 2025).
