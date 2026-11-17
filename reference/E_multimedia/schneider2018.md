---
cle: schneider2018
reference: "Schneider, S., Beege, M., Nebel, S. et Rey, G. D. (2018). A meta-analysis of how signaling affects learning with media. Educational Research Review, 23, 1-24."
doi: 10.1016/j.edurev.2017.11.001
axe: [E1]
type_etude: méta-analyse à effets aléatoires (103 études, 145 comparaisons, N = 12 201, 1970-2016)
public: 78,5 % d'étudiants du supérieur, 13,9 % de collégiens et lycéens, 4,9 % d'écoliers, 2,8 % d'adultes ; sciences de la nature surreprésentées
lecture: texte complet, 08/11/2026
regles:
  - outil: CapsuleForge
    regle: "signaler explicitement l'organisation et les éléments pertinents : titres et marqueurs de structure, mots-clés mis en évidence, partie de figure colorée ou pointée au moment où la voix en parle"
    niveau: B
    transferabilite: forte
    note: "rétention g = 0,53, transfert g = 0,33 ; pas de biais de publication détecté ; hétérogénéité très forte"
  - outil: CapsuleForge
    regle: "préférer la couleur (surbrillance, code couleur texte-figure) au clignotement : ne jamais faire clignoter un élément pour attirer l'attention"
    niveau: C
    transferabilite: forte
    note: "clignotement : 3 comparaisons, effet négatif ; couleur : transfert g = 0,39 sur 16 comparaisons"
  - outil: ExoForge
    regle: "dans les énoncés et corrections, mettre en évidence la structure (étapes titrées, grandeur cherchée, données utiles) ; ne pas attendre de ce signalement un gain de compréhension en mathématiques abstraites"
    niveau: C
    transferabilite: moyenne
    note: "domaine mathématiques et logique : aucun effet (9 comparaisons)"
---

# Méta-analyse du signalement (Schneider et al., 2018)

Schneider, S., Beege, M., Nebel, S. et Rey, G. D. (2018). A meta-analysis of how signaling affects learning with media. *Educational Research Review*, 23, 1-24. [DOI](https://doi.org/10.1016/j.edurev.2017.11.001)

**En une phrase.** Sur 145 comparaisons, surtout chez des étudiants, ajouter des repères qui montrent l'organisation et les éléments pertinents (titres, surlignage, couleur, flèches) améliore la rétention (g = 0,53) et le transfert (g = 0,33) et réduit un peu la charge perçue ; le gain est nul en mathématiques et le clignotement nuit : pour CapsuleForge, signaler en couleur et au bon moment, jamais par clignotement.

## La source

| | |
| --- | --- |
| **Équipe** | Psychologie de l'apprentissage avec les médias numériques, université technique de Chemnitz ; même équipe que [rey2019](rey2019.md). |
| **Nature** | Académique ; financement non rapporté ; remerciements à quatre collaborateurs (p. 21). |
| **Support** | *Educational Research Review* (Elsevier). |
| **Audience** | 311 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : mots-clés, bases, date de fin (23/11/2016), critères et codage par deux juges (κ de 0,63 à 0,81) publiés ; tailles d'effet par étude et entonnoirs en annexes en ligne (non consultées) ; pas de τ². La démarche se refait. |

## Ce que fait l'étude

- **Corpus** (p. 5-6) : recherche dans Google Scholar, ERIC, PsycINFO, PsycARTICLES, ScienceDirect et littérature grise (thèses, actes, posters) ; anglais ou allemand. 150 études examinées, 103 retenues. Critère clé : groupe témoin identique sauf le signalement.
- **Codage** (p. 6) : niveau d'études, connaissances préalables, rythme (imposé ou libre), domaine, mode de signalement (texte : organisation, couleur, intonation... ; image : flèches et gestes, couleur, étiquettes, clignotement, projecteur, organisateurs graphiques), permanence (texte et image fixes ou vidéo et animation).
- **Analyse** (p. 15) : g de Hedges, effets aléatoires, une taille d'effet par expérience et par mesure ; une étude rapportant seulement « pas de différence » est codée g = 0 avec une erreur type de 0,60 ; biais de publication par entonnoir et corrélation de rang de Begg.
- **Public** (p. 15-16) : 145 comparaisons, N de 8 à 300 (moyenne 84) ; 131 articles, 6 thèses, 6 actes ; 78,5 % d'étudiants du supérieur.

## Résultats

| Mesure (tableau 2, p. 16) | k | g [IC 95 %] | Q (ddl), p. 16 | I² [calcul] |
| --- | --- | --- | --- | --- |
| Rétention | 139 | 0,53 [0,42 ; 0,64] | 12 462 (138) | ≈ 99 % |
| Transfert | 70 | 0,33 [0,22 ; 0,43] | 685 (69) | ≈ 90 % |
| Charge cognitive (baisse) | 27 | 0,25 [0,04 ; 0,45] | 1 273 (26) | ≈ 98 % |
| Motivation | 13 | 0,13 [0,04 ; 0,22] | 27,5 (12) | ≈ 56 % |
| Temps d'étude | 27 | −0,30 (plus long) | 282 (26) | ≈ 91 % |

- **Biais de publication** (p. 16) : entonnoir de la rétention un peu asymétrique (effets négatifs sous-représentés) mais test de Begg non significatif (p = 0,67) ; transfert p = 0,22 après exclusion d'une valeur aberrante (g = 2,28).
- **Niveau d'études** (tableaux 3-4, p. 17-18) : supérieur, rétention 0,60 (k = 108), transfert 0,31 (k = 52) ; pas de modération significative.
- **Domaine** (tableaux 3-4) : physique et mécanique, rétention 0,43 (k = 36), transfert 0,44 (k = 23) ; mathématiques et logique, rétention 0,08, transfert −0,03 (k = 9), non significatifs.
- **Mode** (tableaux 3-4) : signalement dans le texte plus efficace en rétention (0,68 contre 0,38 pour l'image) ; en transfert, couleur dans l'image 0,39 (k = 16), flèches et gestes 0,21 (n.s., k = 12), clignotement −0,47 (k = 3, p < 0,10) ; en rétention, clignotement −0,56 (k = 3).
- **Rythme et permanence** (p. 18) : ni le rythme imposé ou libre, ni le support fixe ou animé ne modèrent l'effet.
- **Connaissances préalables** (p. 18-19) : pas de modération ; descriptivement, effet un peu plus grand chez les plus avancés (contraire à l'inversion d'expertise).

## Avis critique

**Apport.** La plus grande synthèse sur le signalement, avec une majorité d'étudiants du supérieur et un tiers des comparaisons en sciences physiques : l'effet moyen tient, y compris en transfert.

**Points forts**
- Grand corpus, littérature grise recherchée, deux juges.
- Groupe témoin strictement identique exigé.
- Public proche du nôtre (78,5 % d'étudiants).

**Réserves**
1. **Importante** — Hétérogénéité extrême (I² ≈ 90 à 99 % [calcul]) sans τ² ni intervalle de prédiction ; la catégorie « signalement » mêle titres de texte, couleurs, flèches et intonation.
2. **Importante** — Tests de biais faibles (entonnoir à l'œil, Begg) ; l'asymétrie notée pour la rétention n'est pas corrigée (pas de « trim and fill »).
3. **Importante** — Les modérateurs (mathématiques, clignotement, couleur) reposent souvent sur moins de 20 comparaisons, parfois 2 ou 3, et comparent des études entre elles ; les auteurs le reconnaissent (p. 20-21).
4. **Mineure** — Incohérences : 103 études annoncées, 95 dans les limites et la conclusion (p. 20-21) ; certains intervalles de confiance ne sont pas centrés sur l'effet (supérieur en transfert 0,31 [0,23 ; 0,50], clignotement −0,56 [−1,38 ; −0,25]).
5. **Mineure** — Codage « g = 0, erreur type 0,60 » pour les résultats non détaillés : choix conservateur, mais arbitraire.
6. **Mineure** — Études de laboratoire à séance unique pour la plupart (p. 20).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Le signalement améliore rétention et transfert | B | Méta-analyse large, public proche, pas de biais détecté, mais hétérogénéité extrême ; concordance avec noetel2021 |
| L'effet vaut en physique et mécanique | B | 23 à 36 comparaisons du domaine |
| Le clignotement nuit, la couleur aide | C | Peu de comparaisons, comparaison entre études |
| Pas de gain en mathématiques | C | 9 comparaisons, comparaison entre études |

**Transférabilité** : forte pour les capsules de mécanique (public et domaine représentés) ; moyenne pour les mathématiques, où aucun gain n'est démontré.

**Pour conclure, il faudrait** comparer deux versions d'une capsule de mécanique : sans repère, et avec surbrillance colorée synchronisée de la partie de figure commentée, avec un quiz de transfert ; faire de même sur une capsule de mathématiques.

## Pour Forge

- **CapsuleForge** : à chaque phrase de narration qui désigne une partie de figure, colorer ou entourer cette partie (niveau B) ; signaler la structure (plan, titres d'étapes) (niveau B).
- **CapsuleForge** : bannir le clignotement ; préférer la couleur (niveau C).
- **ExoForge** : mise en évidence de la structure des corrections, sans en attendre de gain en mathématiques abstraites (niveau C).
- Renvois : [liu2022](liu2022.md) (apparition synchronisée comme forme de signalement), [noetel2021](noetel2021.md), [mayer2017](mayer2017.md).
