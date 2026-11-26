---
cle: attali2000
reference: "Attali, Y. et Fraenkel, T. (2000). The point-biserial as a discrimination index for distractors in multiple-choice items: Deficiencies in usage and an alternative. Journal of Educational Measurement, 37(1), 77-86."
doi: 10.1111/j.1745-3984.2000.tb01077.x
axe: [C2]
type_etude: article méthodologique (démonstration et application à 3 620 items d'un test d'admission)
public: items prétestés d'un test d'entrée à l'université (Israël), environ 300 candidats par section
lecture: texte complet, 08/11/2026
regles:
  - outil: DiagForge
    regle: "juger un leurre en comparant le score moyen de ceux qui le choisissent à celui de ceux qui choisissent la bonne réponse, pas à celui de tous les autres étudiants"
    niveau: B
    transferabilite: forte
  - outil: DiagForge
    regle: "signaler comme suspect un leurre choisi par des étudiants dont le score moyen est égal ou supérieur à celui des étudiants qui ont la bonne réponse (clé fausse ou deuxième bonne réponse)"
    niveau: C
    transferabilite: forte
---

# Mesurer la discrimination d'un leurre (Attali et Fraenkel, 2000)

Attali, Y. et Fraenkel, T. (2000). The point-biserial as a discrimination index for distractors in multiple-choice items: Deficiencies in usage and an alternative. *Journal of Educational Measurement*, 37(1), 77-86. [DOI](https://doi.org/10.1111/j.1745-3984.2000.tb01077.x)

**En une phrase.** Calculer la point-bisériale d'un leurre en opposant ceux qui le choisissent à tous les autres est une erreur, qui fait rejeter à tort des leurres de questions difficiles ; il faut opposer ceux qui choisissent le leurre à ceux qui choisissent la bonne réponse, ce qui aurait gardé 78 % des items rejetés dans un test réel.

## La source

| | |
| --- | --- |
| **Équipe** | Institut national de mesure et d'évaluation (NITE, Jérusalem), concepteur du test d'admission étudié. |
| **Nature** | Institut public de mesure ; les auteurs analysent leurs propres items. |
| **Support** | *Journal of Educational Measurement* (NCME), revue de référence en psychométrie. |
| **Audience** | 40 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Bonne pour la méthode : formules et exemples numériques complets (tableaux 1 à 3) ; données d'items non publiques. |

## Ce que fait l'étude

- **Argument** (p. 78-79) : la point-bisériale usuelle d'un leurre compare ceux qui le choisissent à tous les autres, qui mêlent bons et mauvais répondants ; elle n'est négative que si le groupe du leurre est sous la moyenne générale.
- **Alternative** (p. 79) : point-bisériale entre ceux qui choisissent le leurre et ceux qui choisissent la bonne réponse.
- **Démonstrations** (p. 79-82) : valeurs calculées pour des items types ; cas des abstentions avec points négatifs.
- **Application** (p. 84-85) : 3 620 items prétestés ; 523 items à bonne discrimination rejetés à cause d'un leurre selon la règle usuelle (point-bisériale du leurre ≥ −0,05).

## Résultats

- **Biais de la méthode usuelle** (tableau 1, p. 80) : pour une question difficile (30 % de réussite), un leurre peut être rejeté alors que ceux qui le choisissent ont un score inférieur de plus d'un demi-écart-type à ceux qui réussissent.
- **Application** (tableau 4, p. 84) : 78 % des 523 items rejetés auraient été acceptés avec l'indice proposé ; presque tous les items très difficiles.
- **Décision** (p. 83) : l'indice proposé repose sur moins d'étudiants, donc il faut un seuil fondé sur un test statistique et corrigé pour le nombre d'options.

## Avis critique

**Apport.** Indique la bonne comparaison pour juger un leurre : c'est directement applicable au tableau des leurres de DiagForge.

**Points forts**
- Argument mathématique simple, démonstrations chiffrées.
- Vérification sur un grand nombre d'items réels.

**Réserves**
1. **Importante** — Échantillons de prétest d'environ 300 candidats : avec 30 à 60 étudiants, l'indice par leurre est très instable.
2. **Mineure** — Les auteurs n'ont pas vérifié par une autre source que les items repêchés étaient réellement bons.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Comparer le leurre à la bonne réponse, pas à l'ensemble | B | Démonstration mathématique, cohérente avec Gierl et al. (2017) |
| La méthode usuelle rejette à tort beaucoup d'items difficiles | C | Une application, critère de vérité absent |

**Transférabilité** : forte pour le principe ; à petits effectifs, se contenter d'un indicateur descriptif (score moyen des choisisseurs du leurre comparé à celui des choisisseurs de la bonne réponse).

**Pour conclure, il faudrait** comparer, sur nos quiz, les leurres signalés par les deux méthodes et les relire.

## Pour Forge

- **DiagForge** : pour chaque leurre, afficher le score moyen (sur le reste du test) de ceux qui le choisissent à côté de celui des étudiants qui ont la bonne réponse (niveau B).
- **DiagForge** : alerte si ce score dépasse ou égale celui des bonnes réponses, avec au moins quelques étudiants concernés (niveau C ; voir Srisomsak et al., 2025).
