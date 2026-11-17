---
cle: moreno2009
reference: "Moreno, R., Reisslein, M. et Ozogul, G. (2009). Optimizing worked-example instruction in electrical engineering: The role of fading and feedback during problem-solving practice. Journal of Engineering Education, 98(1), 83-92."
doi: 10.1002/j.2168-9830.2009.tb01007.x
axe: [D1]
type_etude: essai randomisé, 5 groupes, une séance sur ordinateur
public: 232 étudiants de 1re année d'ingénierie (États-Unis)
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "après une erreur à une étape, montrer la même étape résolue dans un exemple d'habillage différent, puis redonner un essai"
    niveau: B
    transferabilite: forte
    note: "effet du paquet « comparer + réessayer » ; la part de chaque ingrédient n'est pas isolée"
  - outil: ExoForge
    regle: "retour immédiat après chaque étape plutôt qu'en fin d'exercice"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "pour des exercices faciles, ne pas estomper en commençant par la dernière étape ; préférer l'estompage par la première étape ou la résolution complète"
    niveau: C
    transferabilite: moyenne
---

# Estompage et retour en électricité (Moreno et al., 2009)

Moreno, R., Reisslein, M. et Ozogul, G. (2009). Optimizing worked-example instruction in electrical engineering: The role of fading and feedback during problem-solving practice. *Journal of Engineering Education*, 98(1), 83-92. [DOI](https://doi.org/10.1002/j.2168-9830.2009.tb01007.x)

**En une phrase.** Sur un exercice de circuits en trois étapes, montrer après une erreur l'étape correspondante d'un exemple résolu puis laisser réessayer améliore nettement le transfert proche et éloigné ; le retour après chaque étape fait un peu mieux que le retour global, et l'estompage par la dernière étape fait moins bien que les autres méthodes sur ce contenu facile.

## La source

| | |
| --- | --- |
| **Équipe** | Psychologie de l'éducation (University of New Mexico) et département de génie électrique (Arizona State University) : une spécialiste des exemples résolus associée à des enseignants d'électricité. |
| **Nature** | Académique ; financement National Science Foundation (p. 90). |
| **Support** | *Journal of Engineering Education* (Wiley), revue de référence en pédagogie de l'ingénieur. |
| **Audience** | 74 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : les cinq conditions sont décrites précisément (Fig. 1, p. 88) et les problèmes sont illustrés (p. 84), mais le logiciel, les tests complets et les données ne sont pas publiés. La démarche se refait ; les chiffres ne se vérifient pas. |

## Ce que fait l'étude

- **Public** : 232 étudiants d'un cours d'introduction à la conception en ingénierie, tirés au sort individuellement entre 5 groupes de 45 à 48 (p. 86).
- **Séance** (une seule, sur ordinateur) : rappel des notions (courant, tension, résistance), prétest de 6 questions, puis un exemple résolu et trois problèmes de calcul de la résistance équivalente d'un circuit parallèle en trois étapes (loi d'Ohm par branche, somme des courants, loi d'Ohm globale), puis un questionnaire de charge cognitive (p. 86-87).
- **Conditions** (Fig. 1, p. 88) :
  - résolution complète avec retour après chaque étape (PS-S) ;
  - résolution complète avec retour en fin de problème (PS-T) ;
  - estompage par la dernière étape avec retour par étape (BF-S) ;
  - estompage par la première étape avec retour par étape (FF-S) ;
  - estompage par la dernière étape avec retour « méta » (BF-M) : après une erreur, l'exemple résolu s'affiche avec l'étape concernée surlignée, puis l'étudiant a un second essai (p. 87).
- **Mesures** : test papier immédiat de transfert proche (4 problèmes de même structure) et de transfert éloigné (4 problèmes de structure différente : on donne un courant de branche et on cherche le courant total), notés sur 12 par deux enseignants (p. 87).

## Résultats

Moyennes sur 12 (tableau 1, p. 89) :

| Groupe | Transfert proche | Transfert éloigné |
| --- | --- | --- |
| PS-S (complet, retour par étape) | 10,98 | 4,82 |
| PS-T (complet, retour global) | 9,81 | 4,92 |
| BF-S (estompage arrière) | 8,29 | 3,45 |
| FF-S (estompage avant) | 11,13 | 4,54 |
| BF-M (estompage arrière, retour méta) | 10,99 | 6,34 |

- **Estompage** : FF-S et PS-S font mieux que BF-S en transfert proche (η²p = 0,16) ; aucune différence en transfert éloigné ni en charge perçue (p. 88). Écart FF-S − BF-S : d ≈ 0,87 [calcul, tableau 1].
- **Moment du retour** : PS-S fait mieux que PS-T en transfert proche (η²p = 0,05, p < 0,05), pas en transfert éloigné ; le test multivarié n'est que marginal (p = 0,09) (p. 88). d ≈ 0,44 [calcul].
- **Retour méta** : BF-M fait mieux que BF-S en transfert proche (η²p = 0,15) et éloigné (η²p = 0,13) (p. 88). d ≈ 0,85 et 0,77 [calcul].
- **Charge cognitive** : faible partout (1,6 sur 4 environ), sans différence entre groupes (p. 88-89).

## Avis critique

**Apport.** Une des rares études d'ingénierie qui compare dans le même essai l'estompage, le moment du retour et le contenu du retour sur un calcul en plusieurs étapes, exactement la forme des exercices ExoForge.

**Points forts**
- Tirage au sort individuel, effectifs corrects (45 à 48 par groupe), correction en double par des enseignants (accord ≥ 98,5 %).
- Transfert éloigné mesuré, et pas seulement des exercices identiques à ceux de l'entraînement.
- Les auteurs discutent eux-mêmes la facilité du contenu et la brièveté de la séance (p. 89-90).

**Réserves**
1. **Majeure** — Le groupe BF-M diffère de BF-S par deux choses : il voit l'étape correspondante de l'exemple résolu **et** il a un second essai (p. 87). Le gain ne peut pas être attribué à la seule comparaison avec l'exemple ; le second essai peut y contribuer.
2. **Importante** — Effet plafond en transfert proche : plus de 60 % des étudiants ont la note maximale (p. 89). Le contenu est facile ; les auteurs le reconnaissent et attribuent à cette facilité le mauvais résultat de l'estompage arrière, ce qui limite la portée de ce résultat.
3. **Importante** — Une seule séance courte (un exemple, trois problèmes) et un test immédiat : rien ne dit que les écarts tiennent dans la durée.
4. **Importante** — L'avantage du retour par étape est fragile : test multivarié non significatif (p = 0,09) et effet seulement en transfert proche.
5. **Mineure** — Les groupes avec estompage résolvent 6 étapes au lieu de 9 (p. 87) : à temps de pratique différent, la comparaison avec la résolution complète mêle estompage et quantité d'entraînement.
6. **Mineure** — En transfert éloigné, les écarts-types sont du même ordre que les moyennes (tableau 1) : distribution probablement très asymétrique, ce que l'analyse de covariance gère mal.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Montrer l'étape résolue d'un exemple puis redonner un essai améliore le transfert | B | Essai randomisé, effet grand, deux ingrédients confondus |
| Le retour par étape vaut mieux que le retour global | C | Effet petit, marginal en multivarié, plafond |
| L'estompage arrière fait moins bien sur un contenu facile | C | Un seul contenu, contraire à d'autres études |

**Transférabilité** : forte pour le mécanisme (étudiants d'ingénierie, calcul en étapes enchaînées, travail sur ordinateur) ; faible pour les valeurs, le contenu étant bien plus simple qu'un exercice de mécanique en L3–M2.

**Pour conclure, il faudrait** séparer les deux ingrédients du retour méta : après une erreur, (a) correction expliquée, (b) étape d'un exemple analogue puis second essai, (c) second essai seul, avec un test différé de deux à trois semaines. ExoForge peut faire cette comparaison directement.

## Pour Forge

- **ExoForge** : après une erreur à une étape, afficher la même étape résolue dans un exemple d'habillage différent, puis redonner un essai (niveau B, à tester avec la comparaison ci-dessus).
- **ExoForge** : garder le retour immédiat à chaque étape (niveau C).
- **ExoForge** : pour les exercices faciles, ne pas estomper en commençant par la dernière étape ; d'après les auteurs (p. 85), Renkl et al. (2004) ne trouvaient pas d'effet de l'ordre d'estompage, ce qui reste à confronter à la fiche de Renkl et al. (2004) quand elle sera écrite (axe D1).
