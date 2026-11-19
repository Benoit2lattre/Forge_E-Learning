---
cle: shultz2024
reference: "Shultz, B., Kopale, M. S., Benken, S. et Mucksavage, J. (2024). Evaluating the quality of examination items from the Pathophysiology, Drug Action, and Therapeutics course series. American Journal of Pharmaceutical Education, 88, article 100757."
doi: 10.1016/j.ajpe.2024.100757
axe: [B1]
type_etude: étude descriptive et corrélationnelle sur les items d'examen de deux semestres (relecture par consensus avec une grille de 14 critères, tests de Mann-Whitney et du khi-deux)
public: étudiants en pharmacie (522 étudiants, 27 examens, cours intégrés de physiopathologie, pharmacologie et thérapeutique)
lecture: texte complet, 10/11/2026
regles:
  - outil: QuizForge
    regle: "signaler un écart de longueur marqué entre les options (critère des auteurs : 10 mots ou plus) ; garder l'alerte comme point à vérifier"
    niveau: D
    transferabilite: forte
    note: "critère opérationnel des auteurs, non validé ; QuizForge utilise un rapport de longueur de la clé aux leurres"
  - outil: QuizForge
    regle: "traiter en premier l'énoncé sans question précise du type « laquelle de ces affirmations est vraie ? » suivi de quatre affirmations"
    niveau: D
    transferabilite: forte
  - outil: DiagForge
    regle: "ne pas conclure qu'un item est « trop facile à cause de leurres non fonctionnels » quand les leurres sont définis par leur taux de choix : les deux mesures dépendent l'une de l'autre ; regarder d'abord les leurres choisis par moins de 5 % comme pistes de révision"
    niveau: C
    transferabilite: forte
---

# Défauts d'écriture dans une banque d'examens de pharmacie (Shultz et al., 2024)

Shultz, B., Kopale, M. S., Benken, S. et Mucksavage, J. (2024). Evaluating the quality of examination items from the Pathophysiology, Drug Action, and Therapeutics course series. *American Journal of Pharmaceutical Education*, 88, article 100757. [DOI](https://doi.org/10.1016/j.ajpe.2024.100757)

**En une phrase.** Sur 928 QCM d'examens de pharmacie, 80 % ont au moins un défaut ; les items dont seules les options sont défectueuses (surtout des leurres choisis par moins de 5 %) sont nettement plus faciles et un peu moins discriminants, alors que les items dont seul l'énoncé est défectueux ne diffèrent pas des items sans défaut ; mais le défaut principal est défini à partir des réponses des étudiants, ce qui rend le lien en partie automatique.

## La source

| | |
| --- | --- |
| **Équipe** | College of Pharmacy, université de l'Illinois à Chicago ; deux enseignants et deux personnels formés à l'évaluation ; deux des relecteurs écrivaient aussi des items, mais n'ont pas relu les leurs (p. 2). |
| **Nature** | Académique ; financement : « None declared » (p. 5). |
| **Support** | *American Journal of Pharmaceutical Education* (Elsevier) ; article numéroté, pages 1 à 5 citées. |
| **Audience** | 3 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Moyenne : grille publiée (tableau 1) et critères automatiques décrits ; ni items ni données publiés ; accord entre relecteurs non mesuré (p. 2). La démarche se refait ; les chiffres ne se vérifient que dans le tableau 2. |

## Ce que fait l'étude

- **Corpus** (p. 3) : 928 QCM de 27 examens (printemps et automne 2022), 8 cours sur 10 de la série, 75 auteurs d'items ; 908 items analysés (20 annulés après l'examen). 93 % des items ont 4 leurres ; 171 étudiants par examen en moyenne.
- **Relecture** (p. 2) : grille de 14 critères (options, énoncé, général ; tableau 1, d'après Haladyna et Downing), étalonnée sur 40 items communs puis items répartis au hasard entre les 4 relecteurs ; 33 items discutés en groupe. Même démarche pour le niveau de Bloom (I-II = bas, III-V = haut).
- **Critères automatiques** (macros Excel, p. 2) : au moins 2 options choisies par moins de 5 % des étudiants = « leurres non plausibles » ; options dont le nombre de mots diffère de 10 ou plus = « longueurs différentes » ; présence de « all/none of the above » ; plusieurs bonnes réponses.
- **Indices** (p. 2) : réussite, point-bisériale, score des 27 % meilleurs et des 27 % moins bons ; tests de Mann-Whitney ; khi-deux pour le lien niveau cognitif-défaut.

## Résultats

- **Fréquence** (p. 3) : 742 items (80 %) avec au moins un défaut, 1 466 défauts en tout. Leurres non plausibles : 438 items (47 %) ; énoncé qui ne contient pas toute l'information nécessaire, souvent « laquelle de ces affirmations est vraie/fausse ? » : 354 (38 %). Négation, questions multiples, blanc mal placé : environ 10 % chacun ; longueurs différentes : 92 items ; « toutes/aucune des réponses » et ordre non logique : rares.

| Items (tableau 2 et figure, p. 3) | n | Réussite | 27 % meilleurs | 27 % moins bons | Point-bisériale |
| --- | --- | --- | --- | --- | --- |
| Sans défaut | 184 | 0,68 | 0,85 | 0,50 | 0,34 |
| Avec défaut(s) | 724 | 0,79 | 0,91 | 0,66 | 0,28 |
| Défaut d'énoncé seul | 233 | 0,68 | 0,85 | 0,51 | non rapporté dans le texte |
| Défaut d'options seul | 185 | 0,84 | 0,93 | 0,73 | 0,27 |

- Différences avec les items sans défaut : p < 0,001 pour les items défectueux et pour les défauts d'options ; pas de différence pour les défauts d'énoncé (p. 3-4).
- Les 27 % moins bons gagnent 16 points sur les items défectueux (+32 % relatif), 22 points sur les items à options défectueuses (p. 4).
- **Niveau cognitif** (p. 4) : deux tiers d'items de bas niveau ; même réussite moyenne (0,77) aux deux niveaux. Les items de haut niveau ont un peu moins de défauts d'énoncé (Φ = −0,079) et un peu plus de défauts d'options (Φ = 0,089).

## Avis critique

**Apport.** Inventaire récent et détaillé, avec séparation des défauts d'énoncé et d'options ; décrit des critères automatiques simples (taux de choix < 5 %, écart de 10 mots) proches de ce que font QuizForge et DiagForge.

**Points forts**
- Corpus complet de deux semestres, 75 auteurs, relecteurs qui ne relisent pas leurs propres items.
- Analyse séparée des items à un seul type de défaut.
- Limites détaillées (p. 4-5).

**Réserves**
1. **Majeure** — Le défaut d'options le plus fréquent est défini par le fait qu'au moins deux leurres sont choisis par moins de 5 % des étudiants. Un item réussi à plus de 90 % ne laisse au plus que 10 % de réponses aux leurres : il est presque toujours classé « défectueux ». Le résultat « les options défectueuses rendent l'item facile » est donc en partie circulaire.
2. **Importante** — La conclusion et le résumé disent que les énoncés sans question précise « gênent probablement la réussite » (p. 1), alors que les items à énoncé défectueux ont la même réussite que les items sans défaut (p. 4).
3. **Importante** — Accord entre relecteurs non mesuré (p. 2) ; les relecteurs sans expertise du contenu ont pu manquer des indices logiques (p. 5).
4. **Mineure** — Décomptes non concordants : 59 + 163 = 222 items à défaut d'énoncé seul et 76 + 107 = 183 à défaut d'options seul (p. 4) [décompte], contre 233 et 185 dans la comparaison des indices.
5. **Mineure** — Public éloigné (pharmacie) ; pas de distinction items neufs et réutilisés (p. 4).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| 80 % des items d'examen d'enseignants ont un défaut | C | Un établissement, accord non mesuré ; concordant avec les autres fiches de l'axe |
| Les défauts d'énoncé ne changent pas la difficulté | C | Comparaison corrélationnelle |
| Les leurres non plausibles rendent l'item plus facile | D | Mesure en partie circulaire |

**Transférabilité** : forte pour les critères de repérage ; faible pour les chiffres (pharmacie, items cliniques).

**Pour conclure, il faudrait** coder les leurres comme plausibles ou non avant l'examen, à l'aveugle des résultats, puis comparer la réussite et la discrimination.

## Pour Forge

- **QuizForge** : signaler un écart de longueur marqué entre options (les auteurs : 10 mots ou plus) comme point à vérifier (niveau D).
- **QuizForge** : repérer l'énoncé « laquelle de ces affirmations est vraie ? » suivi d'affirmations indépendantes et proposer un vrai/faux multiple (niveau D ; voir [couch2018](couch2018.md)).
- **DiagForge** : lister après usage les leurres choisis par moins de 5 % comme pistes de révision, sans en tirer de preuve sur la qualité de l'item (niveau C).
- Renvois : [ali2015](ali2015.md) (cité par les auteurs), [rush2016](rush2016.md), [tarrant2008](tarrant2008.md), [moore2023](moore2023.md).
