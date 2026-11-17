---
cle: kalyuga2004
reference: "Kalyuga, S. et Sweller, J. (2004). Measuring knowledge to optimize cognitive load factors during instruction. Journal of Educational Psychology, 96(3), 558-568."
doi: 10.1037/0022-0663.96.3.558
axe: [D2]
type_etude: quatre expériences (validation d'un test rapide, puis adaptation de l'enseignement), 20 à 45 élèves chacune
public: élèves des années 9 à 11 du secondaire (environ 15 à 17 ans) en algèbre et géométrie analytique (Sydney, Australie)
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "estimer le niveau de l'étudiant par un test rapide « quelle est la prochaine étape ? » sur des états intermédiaires de solution, plutôt que par un problème complet"
    niveau: C
    transferabilite: moyenne
  - outil: ExoForge
    regle: "repasser le test rapide pendant l'entraînement et faire avancer l'étudiant dans l'estompage (exemple complet, exemple partiel, problème) selon son score"
    niveau: C
    transferabilite: moyenne
---

# Un test rapide pour adapter le guidage (Kalyuga et Sweller, 2004)

Kalyuga, S. et Sweller, J. (2004). Measuring knowledge to optimize cognitive load factors during instruction. *Journal of Educational Psychology*, 96(3), 558-568. [DOI](https://doi.org/10.1037/0022-0663.96.3.558)

**En une phrase.** Demander seulement « quelle est la prochaine étape ? » sur des états intermédiaires de solution mesure le niveau en algèbre et en géométrie presque aussi bien qu'un test complet (r = 0,92 et 0,85) en 2,5 à 5 fois moins de temps ; utilisé pour choisir le degré d'estompage des exemples, il améliore l'apprentissage par rapport à un parcours non adapté.

## La source

| | |
| --- | --- |
| **Équipe** | Université de Nouvelle-Galles du Sud (Sydney) ; Sweller est le fondateur de la théorie de la charge cognitive, Kalyuga a décrit l'effet d'inversion lié à l'expertise. |
| **Nature** | Académique ; financement du conseil australien de la recherche (p. 558). |
| **Support** | *Journal of Educational Psychology* (APA). |
| **Audience** | 235 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Bonne pour la méthode : tâches, barèmes et organigramme du parcours adaptatif décrits (p. 564-566) ; données non publiées. |

## Ce que fait l'étude

- **Test rapide** (p. 559-560) : présenter une série d'équations ou de figures à divers stades de résolution et demander d'écrire en quelques secondes l'étape suivante ; sauter des étapes rapporte plus de points (signe de schémas automatisés).
- **Expériences 1 et 2** (p. 560-562) : 45 élèves en équations du premier degré, puis 20 en géométrie analytique ; comparaison avec un test classique de résolution complète.
- **Expérience 3** (p. 562-563) : 42 élèves classés en deux niveaux par le test rapide, puis exemples résolus alternés avec des problèmes, ou problèmes seuls ; test rapide après une séance de 12 min.
- **Expérience 4** (p. 564-566) : 26 élèves sur ordinateur ; parcours d'exemples estompés où le test rapide, répété, décide de l'étape suivante, comparé à un parcours de même durée attribué sans tenir compte du niveau (élèves appariés).

## Résultats

- **Validité** (p. 561-562) : corrélations de 0,92 (algèbre) et 0,85 (géométrie) avec le test complet ; temps divisé par 4,9 et 2,5 ; fiabilité interne faible (α de 0,57 à 0,63) pour le test rapide.
- **Inversion liée à l'expertise** (p. 563-564) : chez les élèves faibles, les exemples font nettement mieux que les problèmes (24 % contre 6 % de réussite) ; chez les plus forts, tendance inverse non significative (54 % contre 36 %).
- **Adaptation** (p. 566) : gains plus élevés pour le parcours adapté (3,23 contre 0,77 point), à durée égale.

## Avis critique

**Apport.** Donne une méthode concrète, rapide et automatisable pour estimer le niveau d'un étudiant sur un type de problème, et montre qu'elle peut piloter l'estompage des exemples.

**Points forts**
- Méthode fondée sur une théorie explicite des schémas.
- Validation, puis usage pour adapter l'enseignement, dans le même article.
- Limites discutées (domaines étroits, fiabilité ; p. 566-567).

**Réserves**
1. **Importante** — Très petits effectifs (10 à 13 élèves par groupe aux expériences 3 et 4).
2. **Importante** — Tâches très structurées (équations linéaires, projections de segments) ; les auteurs reconnaissent que la méthode est moins simple pour des problèmes à plusieurs démarches possibles.
3. **Importante** — Le test rapide sert à la fois à adapter et à mesurer le résultat ; pas de test classique final.
4. **Mineure** — Élèves du secondaire, séances courtes.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Le test « étape suivante » mesure bien le niveau sur des tâches structurées | B | Deux validations concordantes, fortes corrélations |
| Adapter l'estompage avec ce test améliore l'apprentissage | C | Une expérience, 26 élèves |

**Transférabilité** : moyenne. Bonne pour les étapes de calcul bien définies (dérivées, intégrales, équilibre d'un solide) ; plus délicate pour les problèmes de mécanique à démarches multiples.

**Pour conclure, il faudrait** construire, pour un type d'exercice ExoForge, un test « étape suivante » et vérifier sa corrélation avec la réussite à l'exercice complet.

## Pour Forge

- **ExoForge** : test diagnostique rapide (états intermédiaires d'une solution, « que faites-vous ensuite ? ») pour choisir le point de départ dans l'estompage (niveau C).
- **ExoForge** : test rapide répété en cours de parcours pour passer d'un exemple complet à un exemple partiel puis au problème (niveau C ; voir Salden et al., 2010).
