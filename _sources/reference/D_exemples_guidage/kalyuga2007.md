---
cle: kalyuga2007
reference: "Kalyuga, S. (2007). Expertise reversal effect and its implications for learner-tailored instruction. Educational Psychology Review, 19(4), 509-539."
doi: 10.1007/s10648-007-9054-3
axe: [D2]
type_etude: revue narrative et propositions de conception
public: études de l'école primaire à l'université (plus de 2 200 participants au total)
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "mesurer le niveau par un test rapide (choisir ou vérifier l'étape suivante d'une solution) avant et pendant la séance, et régler le guidage en conséquence"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "faire passer au niveau de guidage inférieur quand l'étudiant réussit le test rapide du niveau en cours"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "proposer des questions « étape suivante » comme diagnostic rapide en début de séance"
    niveau: C
    transferabilite: forte
---

# Adapter le guidage au niveau (Kalyuga, 2007)

Kalyuga, S. (2007). Expertise reversal effect and its implications for learner-tailored instruction. *Educational Psychology Review*, 19(4), 509-539. [DOI](https://doi.org/10.1007/s10648-007-9054-3)

**En une phrase.** Mise à jour de la revue de 2003 : l'inversion d'expertise est retrouvée dans de nombreux domaines, et des tests rapides (« quelle est la prochaine étape ? ») permettent de mesurer le niveau en ligne et d'adapter le guidage, avec des gains de l'ordre de d = 0,5.

## La source

| | |
| --- | --- |
| **Équipe** | Université de Nouvelle-Galles du Sud (Sydney) ; auteur principal des travaux sur l'inversion d'expertise. |
| **Nature** | Académique ; financement non rapporté. Revue fondée en grande partie sur les études de l'auteur. |
| **Support** | *Educational Psychology Review* (Springer). |
| **Audience** | 1 165 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Sans objet pour une revue narrative ; tableau récapitulatif des études avec tailles d'effet (tableau 1, p. 516-518). |

## Ce que fait l'article

- **Synthèse** des études d'inversion d'expertise par type de support : exemples résolus, redondance, représentations dynamiques, hypertexte, auto-explication et charge utile (p. 512-530).
- **Tests rapides de niveau** (p. 530-531) :
  - « première étape » : on montre une tâche peu de temps et l'apprenant indique sa première étape ; corrélation jusqu'à 0,92 avec un test classique, durée divisée par 4,9 au mieux ;
  - « vérification rapide » : l'apprenant juge vite si une étape proposée est correcte ; corrélations de 0,71 et 0,75 avec l'observation de la résolution en cinématique (addition de vecteurs) et en mathématiques (transformations de graphes), durée divisée par 3,2 à 3,5.
- **Tutoriels adaptatifs** (p. 531-532) : en algèbre et en cinématique, au lycée, le niveau de guidage est choisi d'après le test rapide puis réajusté ; gains de connaissances supérieurs au groupe non adapté (d = 0,46 ; puis d = 0,55 en combinant test et difficulté perçue).
- **Bilan** (p. 533-534) : plus de 2 200 participants ; inversions le plus souvent partielles ; dans plusieurs études transversales, l'expertise est déduite des années d'études.

## Avis critique

**Apport.** Transforme l'inversion d'expertise en méthode : mesurer vite le niveau, puis choisir le guidage. Les tests « première étape » et « vérification de l'étape » sont directement transposables à un exercice en ligne.

**Points forts**
- Tableau des études avec les tailles d'effet.
- Méthodes de diagnostic décrites avec leurs validations (corrélations, gain de temps).
- L'auteur signale lui-même les limites : inversions souvent partielles, expertise parfois supposée.

**Réserves**
1. **Importante** — La « différence de taille d'effet » de 0,45 à 2,99 (moyenne 1,72, p. 534) additionne l'effet chez les débutants et chez les avancés ; ce n'est pas une taille d'effet comparable à celles des méta-analyses.
2. **Importante** — Revue narrative, surtout fondée sur les travaux de l'auteur ; pas de recherche systématique.
3. **Importante** — Les tutoriels adaptatifs sont testés au lycée, sur des contenus courts ; les groupes témoins n'ont pas toujours le même nombre d'exercices.
4. **Mineure** — Les validations des tests rapides portent sur de petits échantillons (non rapportés dans la revue).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Un test rapide « étape suivante » estime bien le niveau | C | Corrélations élevées, études de l'auteur, petits échantillons |
| Adapter le guidage au niveau mesuré améliore les gains | C | Quelques essais au lycée, d ≈ 0,5 |

**Transférabilité** : forte pour les tests rapides (un exercice ExoForge a déjà des étapes nommées) ; moyenne pour les gains, mesurés au lycée.

**Pour conclure, il faudrait** valider un test « étape suivante » sur des exercices ExoForge de L3 (corrélation avec la note d'examen) avant de s'en servir pour adapter le guidage.

## Pour Forge

- **ExoForge** : avant un bloc d'exercices, deux ou trois questions « quelle est l'étape suivante ? » ou « cette étape est-elle correcte ? » pour choisir entre exemple complet, exercice estompé et exercice libre (niveau C).
- **ExoForge** : faire passer au niveau de guidage inférieur après réussite au test rapide du niveau en cours (niveau C). Même idée que l'estompage adaptatif de Salden et al. (2010), avec un autre indicateur.
- **QuizForge** : des questions « étape suivante » peuvent servir de diagnostic en début de séance.
