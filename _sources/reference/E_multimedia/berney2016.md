---
cle: berney2016
reference: "Berney, S. et Bétrancourt, M. (2016). Does animation enhance learning? A meta-analysis. Computers & Education, 101, 150-167."
doi: 10.1016/j.compedu.2016.06.005
axe: [E3]
type_etude: méta-analyse (61 expériences, 140 comparaisons, 7036 participants), modèle à effets aléatoires
public: tous publics, niveau scolaire non codé ; animations expositives sur ordinateur
lecture: texte complet, 08/11/2026
regles:
  - outil: CapsuleForge
    regle: "n'animer que ce qui change dans le temps (mouvement, évolution d'un état) ; ne pas attendre d'une animation un gain important par rapport à une bonne figure fixe"
    niveau: B
    transferabilite: moyenne
    note: "g = 0,23 en moyenne, hétérogénéité forte (I² = 78 %)"
  - outil: CapsuleForge
    regle: "commenter une animation par la voix plutôt que par du texte écrit à l'écran"
    niveau: C
    transferabilite: moyenne
    note: "narration g = 0,32, texte écrit g = 0,11 non significatif : comparaison entre études"
  - outil: CapsuleForge
    regle: "pour un schéma abstrait (diagramme, graphe, notation), ne pas présumer qu'une animation fera mieux qu'une suite d'images fixes annotées"
    niveau: C
    transferabilite: moyenne
    note: "représentations abstraites g = 0,006 ; domaine mécanique g = -0,11 et mathématiques g = -0,07, non significatifs"
---

# Animation contre image fixe : méta-analyse (Berney et Bétrancourt, 2016)

Berney, S. et Bétrancourt, M. (2016). Does animation enhance learning? A meta-analysis. *Computers & Education*, 101, 150-167. [DOI](https://doi.org/10.1016/j.compedu.2016.06.005)

**En une phrase.** Sur 140 comparaisons, une animation fait un peu mieux apprendre qu'une suite d'images fixes (g = 0,23), avec de très fortes variations ; le gain apparaît surtout pour les animations narrées et figuratives, et disparaît pour les représentations abstraites ainsi qu'en mécanique et en mathématiques : pour CapsuleForge, animer ce qui bouge, pas les schémas.

## La source

| | |
| --- | --- |
| **Équipe** | Unité TECFA, Faculté de psychologie et des sciences de l'éducation, Université de Genève. Bétrancourt a publié des travaux de référence sur l'animation, dont plusieurs sont discutés dans l'introduction. |
| **Nature** | Académique ; financement non rapporté. |
| **Support** | *Computers & Education* (Elsevier). |
| **Audience** | 421 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : bases, mots-clés, critères (p. 154-155) et tableau des 140 comparaisons (annexe A1) publiés ; double codage sur 10 articles (CCI = 0,875, p. 155). Les chiffres se vérifient à partir de l'annexe. |

## Ce que fait l'étude

- **Corpus** (p. 154-155) : études de Höffler et Leutner (2007) moins les animations non informatiques et les vidéos, plus une recherche jusqu'en décembre 2013 (PsycInfo, ERIC, Francis, MedLine, Psyndex), thèses comprises ; anglais, français, allemand ; 61 expériences, 140 comparaisons, 7036 participants (p. 157).
- **Critères** (p. 155) : animation expositive sur ordinateur contre image fixe ; mesure d'acquisition de connaissances. Pas d'exigence explicite de tirage au sort.
- **Modérateurs** (p. 155-156) : contrôle du rythme (imposé, lecture seule, lecture-arrêt, complet), signalement, abstraction de la représentation, modalité du commentaire, domaine, type de connaissance (taxonomie de Bloom révisée).
- **Analyse** (p. 156) : g de Hedges, effets aléatoires ; plusieurs résultats d'une même étude traités comme indépendants ; quatre valeurs extrêmes ramenées ; biais de publication évalué par le seul fail-safe N.

## Résultats

- **Effet global** (p. 157) : g = 0,226, IC95 [0,12 ; 0,33] ; I² = 78 % ; fail-safe N = 2999. Comparaisons : 30,7 % en faveur de l'animation, 10 % en faveur de l'image fixe, 59,3 % sans différence significative.
- **Types de connaissances** (tableau 2, p. 158) : factuelles g = 0,34, conceptuelles g = 0,16, procédurales g = 0,39 (non significatif, k = 15) ; aucune différence significative entre niveaux (QB = 2,54, p = 0,28).

| Modérateur (tableau 3, p. 159) | g | k |
| --- | --- | --- |
| Rythme imposé par le système | 0,31 | 96 |
| Contrôle complet (lecture, retour, avance) | −0,12 (ns) | 12 |
| Commentaire oral | 0,32 | 28 |
| Commentaire écrit | 0,11 (ns) | 58 |
| Sans texte | 0,89 | 14 |
| Représentation figurative | 0,25 | 91 |
| Représentation abstraite | 0,006 (ns) | 26 |
| Domaine : mécanique | −0,11 (ns) | 22 |
| Domaine : mathématiques | −0,07 (ns) | 11 |
| Domaine : physique | 0,43 (ns) | 14 |

## Avis critique

**Apport.** Mise à jour de hoffler2007 avec 41 expériences de plus : l'avantage de l'animation est réel mais petit, et dépend fortement de la manière dont elle est construite et de ce qu'elle représente.

**Points forts**
- Corpus large, trois langues, thèses incluses (réduit le biais de publication).
- Modérateurs utiles pour la conception (rythme, modalité, abstraction).
- Annexe détaillée des 140 comparaisons.

**Réserves**
1. **Importante** — Dépendance des données : plusieurs résultats d'une même étude traités comme indépendants (p. 156), ce qui réduit artificiellement les intervalles ; les auteurs l'assument.
2. **Importante** — Biais de publication évalué par le seul fail-safe N (p. 157), insuffisant ; pas d'Egger ni de trim and fill. Intervalle de prédiction non rapporté, τ² non rapporté : avec I² = 78 %, l'effet dans une situation donnée peut être nul ou négatif.
3. **Importante** — Modérateurs = comparaisons entre études, non causales. Le résultat « rythme imposé meilleur » repose sur 96 comparaisons contre 12 à 17 pour les autres niveaux ; il contredit d'autres travaux (hasler2007, à lire) et les auteurs le jugent eux-mêmes « surprenant » (p. 160).
4. **Mineure** — Incohérence au tableau 3 : erreur-type de 0,014 pour la mécanique, incompatible avec l'intervalle [−0,34 ; 0,13] (erreur-type ≈ 0,12 [calcul : 0,466 / 3,92]).
5. **Mineure** — Public non codé : on ne sait pas quelle part concerne le supérieur ; « mécanique » désigne le domaine du contenu (dispositifs mécaniques), pas des étudiants ingénieurs.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Une animation fait un peu mieux qu'une image fixe en moyenne | B | Méta-analyse large, concordante avec hoffler2007, mais biais de publication mal contrôlé et hétérogénéité forte |
| Narration meilleure que texte écrit avec une animation | C | Modérateur entre études ; cohérent avec le principe de modalité |
| Pas de gain pour les représentations abstraites, la mécanique et les mathématiques | C | Sous-groupes de 11 à 26 comparaisons, non causaux |
| Le rythme imposé est préférable | D | Déséquilibre des sous-groupes, contredit par d'autres études |

**Transférabilité** : moyenne. Les contenus de mécanique et de mathématiques sont représentés, mais le niveau des apprenants ne l'est pas.

**Pour conclure, il faudrait** comparer, dans une capsule de mécanique (par exemple un mécanisme bielle-manivelle), une animation narrée et une suite d'images fixes annotées narrées, à durée égale, avec un test de transfert.

## Pour Forge

- **CapsuleForge** : animer ce qui change dans le temps, avec une attente de gain modeste (niveau B).
- **CapsuleForge** : commentaire oral plutôt qu'écrit sur une animation (niveau C).
- **CapsuleForge** : pour un diagramme ou un graphe, des images fixes successives annotées suffisent souvent (niveau C) ; à rapprocher de kalyuga2008 et ploetzner2021 (à lire).
- La question du contrôle du rythme est traitée dans d'autres fiches ([mayer2019](mayer2019.md) ; hasler2007, non encore lu) ; ne pas en tirer de règle ici.
