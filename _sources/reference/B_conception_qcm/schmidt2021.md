---
cle: schmidt2021
reference: "Schmidt, D., Raupach, T., Wiegand, A., Herrmann, M. et Kanzow, P. (2021). Relation between examinees' true knowledge and examination scores: Systematic review and exemplary calculations on Multiple-True-False items. Educational Research Review, 34, article 100409."
doi: 10.1016/j.edurev.2021.100409
axe: [B3]
type_etude: revue systématique des barèmes de vrai/faux multiples et calculs des scores attendus
public: sans objet (calculs) ; contexte des examens de médecine
lecture: texte complet, 08/11/2026
regles:
  - outil: QuizForge
    regle: "vrai/faux multiples sans pénalité (1/n par affirmation juste) : fixer le seuil de réussite à 75 % pour exiger la moitié des connaissances"
    niveau: B
    transferabilite: forte
  - outil: QuizForge
    regle: "vrai/faux multiples avec +1/n par affirmation juste et −1/n par affirmation fausse : le hasard est déjà corrigé, seuil à 50 %"
    niveau: B
    transferabilite: forte
  - outil: QuizForge
    regle: "afficher pour chaque barème le score moyen obtenu au hasard"
    niveau: B
    transferabilite: forte
---

# Barèmes des vrai/faux multiples (Schmidt et al., 2021)

Schmidt, D., Raupach, T., Wiegand, A., Herrmann, M. et Kanzow, P. (2021). Relation between examinees' true knowledge and examination scores: Systematic review and exemplary calculations on Multiple-True-False items. *Educational Research Review*, 34, article 100409. [DOI](https://doi.org/10.1016/j.edurev.2021.100409)

**En une phrase.** 27 barèmes existent pour les vrai/faux multiples ; selon le barème, le score obtenu au hasard va de 0 à 50 %, et le seuil de réussite qui correspond à la moitié des connaissances varie de moins de 0 % à plus de 80 % : le barème et le seuil doivent être choisis ensemble.

## La source

| | |
| --- | --- |
| **Équipe** | Centre médical universitaire de Göttingen et hôpital universitaire de Bonn ; recherche en pédagogie médicale. |
| **Nature** | Académique ; pas de conflit d'intérêts déclaré. |
| **Support** | *Educational Research Review* (Elsevier). |
| **Audience** | 14 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Bonne : équations publiées pour chaque barème, calculs refaisables. Les références renvoient aux sections, la revue numérotant les articles. |

## Ce que fait l'étude

- **Revue** (§ 2) : recherche systématique (mars 2020) des barèmes de vrai/faux multiples dans la littérature, sans restriction de langue ni de date ; double extraction.
- **Calculs** : pour chaque barème, information conservée, score moyen au hasard, et score attendu selon la part de connaissances réelles de l'étudiant (modèle où l'étudiant connaît une partie des affirmations et devine les autres).
- **Seuils** : seuil de réussite correspondant à 50 % de connaissances réelles.

## Résultats

- **27 barèmes** identifiés (§ 3.1), dont ceux de Moodle (« Kprime » à demi-point, « Kprime 1/0 ») et d'ILIAS.
- **Score au hasard** : par exemple 6,25 % pour le « tout ou rien » sur 4 affirmations, 50 % pour 1/n par affirmation juste sans pénalité (§ 2).
- **Seuils** : de −0,8 % à 82,9 % selon le barème pour exiger 50 % de connaissances (§ 3, fig. 4).
- **Recommandations** (§ 4-5) : si les points négatifs par item sont admis, barème +1/n par affirmation juste, −1/n par affirmation fausse, avec un seuil à 50 % ; sinon, 1/n par affirmation juste sans pénalité, avec un seuil à 75 %. En Allemagne, la jurisprudence interdit de reporter des points négatifs sur les autres questions.

## Avis critique

**Apport.** Donne, pour chaque barème, le score au hasard et le seuil de réussite cohérent ; c'est exactement l'information dont un générateur de QCM a besoin pour proposer un barème.

**Points forts**
- Revue systématique et équations explicites.
- Correspondance avec les barèmes de Moodle et d'ILIAS.
- Recommandations conditionnelles (selon les règles locales), pas un barème unique.

**Réserves**
1. **Importante** — Les calculs reposent sur un modèle simple (l'étudiant sait ou devine au hasard) ; la connaissance partielle et le goût du risque des vrais étudiants ne sont pas pris en compte.
2. **Mineure** — Pas de données réelles d'examen pour vérifier les seuils proposés.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Score au hasard et seuil cohérent pour chaque barème | B | Calcul exact sous un modèle simple |
| Barèmes recommandés selon les contraintes locales | C | Raisonnement, pas de validation empirique |

**Transférabilité** : forte. Les barèmes sont ceux de Moodle ; les règles françaises sur les points négatifs sont à vérifier localement.

**Pour conclure, il faudrait** comparer les seuils calculés aux résultats d'un examen réel, par exemple avec les réponses déjà disponibles dans DiagForge.

## Pour Forge

- **QuizForge** : pour les vrai/faux multiples, proposer soit 1/n sans pénalité avec un seuil à 75 %, soit +1/n et −1/n avec un seuil à 50 % (niveau B).
- **QuizForge** : afficher dans l'export le score moyen au hasard de chaque barème (niveau B).
- **DiagForge** : corriger la lecture des taux de réussite par le score au hasard du barème utilisé.
