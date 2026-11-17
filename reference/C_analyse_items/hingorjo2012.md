---
cle: hingorjo2012
reference: "Hingorjo, M. R. et Jaleel, F. (2012). Analysis of one-best MCQs: The difficulty index, discrimination index and distractor efficiency. Journal of the Pakistan Medical Association, 62(2), 142-147."
doi: ""
pmid: "22755376"
axe: [C1, C2]
type_etude: analyse d'items d'un seul examen (50 QCM à 5 options, 102 étudiants)
public: étudiants de première année d'odontologie (physiologie), Karachi, Pakistan
lecture: texte complet, 08/11/2026
regles:
  - outil: DiagForge
    regle: "classer chaque question selon la réussite et la discrimination, et afficher pour chaque leurre la part d'étudiants qui le choisissent ; un leurre choisi par moins de 5 % est « non fonctionnel »"
    niveau: D
    transferabilite: moyenne
    note: "seuils conventionnels repris par l'étude, non validés par elle ; voir Raymond et al. (2018) pour la limite du seuil de 5 %"
---

# Difficulté, discrimination et efficacité des leurres sur un examen (Hingorjo et Jaleel, 2012)

Hingorjo, M. R. et Jaleel, F. (2012). Analysis of one-best MCQs: The difficulty index, discrimination index and distractor efficiency. *Journal of the Pakistan Medical Association*, 62(2), 142-147. Pas de DOI ; [PubMed 22755376 (Europe PMC)](https://europepmc.org/article/MED/22755376)

**En une phrase.** Sur un examen de physiologie de 50 QCM à 5 options passé par 102 étudiants, 64 % des questions sont « idéales » (réussite de 30 à 70 %, discrimination au-dessus de 0,24) ; 24 % des leurres sont choisis par moins de 5 % des étudiants, surtout dans les questions faciles ; les questions avec un leurre inutile discriminent un peu mieux que celles où les quatre fonctionnent.

## La source

| | |
| --- | --- |
| **Équipe** | Physiologie et biochimie, Fatima Jinnah Dental College (Karachi). |
| **Nature** | Académique, étude d'établissement ; aucun financement déclaré. |
| **Support** | *Journal of the Pakistan Medical Association*, revue médicale nationale. |
| **Audience** | Pas de DOI (PubMed 22755376) ; non retrouvé dans OpenAlex (08/11/2026). Souvent cité comme source des seuils usuels. |
| **Reproductibilité** | Bonne : indicateurs de chaque question publiés (tableau 1, p. 144) ; formules données. |

## Ce que fait l'étude

- **Données** (p. 143) : examen de fin de semestre, 50 QCM à 5 options, sans points négatifs, 102 étudiants.
- **Indicateurs** (p. 143) : réussite (« indice de difficulté ») ; indice de discrimination par groupes extrêmes (27 % supérieurs contre 27 % inférieurs) ; efficacité des leurres = part des leurres choisis par au moins 5 % des étudiants.
- **Seuils** (tableau 2, p. 144) : réussite trop faible sous 30 %, trop élevée au-dessus de 70 % ; discrimination excellente au-dessus de 0,35, bonne de 0,25 à 0,34, faible de 0,15 à 0,24 (à revoir), mauvaise sous 0,15 (à écarter).

## Résultats

- **Questions** (p. 144-145) : réussite moyenne 54 % ; 78 % des questions de difficulté moyenne ; 62 % avec une discrimination excellente ; deux questions à discrimination négative, expliquées par un leurre choisi par les bons étudiants.
- **Leurres** (p. 145) : 47 leurres sur 200 non fonctionnels ; les questions faciles en ont le plus, les difficiles aucun.
- **Nombre de leurres** : discrimination 0,43 avec un leurre inutile contre 0,35 quand les quatre fonctionnent ; les auteurs y voient un argument pour trois leurres.

## Avis critique

**Apport.** Exemple simple et complet d'analyse d'items (réussite, discrimination, leurres) et source fréquente des seuils 30-70 % et 0,25 ; utile surtout comme modèle de présentation.

**Points forts**
- Toutes les valeurs par question publiées.
- Analyse des réponses des groupes forts et faibles sur des questions défectueuses.

**Réserves**
1. **Majeure** — Un seul examen, 50 questions : les seuils sont repris de manuels, pas établis par l'étude.
2. **Importante** — Discrimination par groupes extrêmes, moins précise que la corrélation item-reste ([Slepkov et al., 2021](slepkov2021.md)) ; comparaison des leurres sur de très petits sous-groupes.
3. **Mineure** — Plage de réussite 30-70 % plus étroite que celle observée sur de grands corpus (Slepkov et al. : jusqu'à 90 %).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Seuils 30-70 % et discrimination ≥ 0,25 | D | Conventions reprises, une seule application |
| Les questions faciles ont plus de leurres inutiles | C | Un examen, concordant avec d'autres corpus |

**Transférabilité** : moyenne. Méthode générale ; contexte médical et seuils discutables.

**Pour conclure, il faudrait** appliquer les deux définitions de la discrimination (groupes extrêmes et item-reste) aux mêmes quiz pour voir si elles désignent les mêmes questions.

## Pour Forge

- **DiagForge** : tableau des réponses par leurre, séparé pour les étudiants forts et faibles (niveau D ; voir Gierl et al., 2017).
- **DiagForge** : préférer la plage de réussite de Slepkov et al. (2021) à la plage 30-70 % (niveau C).
