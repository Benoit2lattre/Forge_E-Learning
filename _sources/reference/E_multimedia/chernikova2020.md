---
cle: chernikova2020
reference: "Chernikova, O., Heitzmann, N., Stadler, M., Holzberger, D., Seidel, T. et Fischer, F. (2020). Simulation-based learning in higher education: A meta-analysis. Review of Educational Research, 90(4), 499-541."
doi: 10.3102/0034654320933544
axe: [E3, D2]
type_etude: méta-analyse (145 études, 409 effets, 10 532 participants), effets aléatoires avec estimation robuste de la variance
public: enseignement supérieur et formation professionnelle ; 126 études sur 145 en médecine, 7 en formation des enseignants, 12 autres
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "proposer des simulations où l'étudiant agit et reçoit un retour sur le résultat de son action, en complément des exercices classiques"
    niveau: C
    transferabilite: faible
    note: "g = 0,85 mais 87 % d'études médicales, savoir-faire cliniques et relationnels ; les auteurs excluent la généralisation à l'ingénierie (p. 525)"
  - outil: ExoForge
    regle: "dans une simulation destinée à des débutants sur le sujet, fournir des indications (invites) et un exemple de démarche consultable, mais les rendre facultatifs pour les étudiants déjà familiers"
    niveau: C
    transferabilite: moyenne
    note: "invites : g = 0,85 contre 0,63 en contexte peu familier, 0,33 contre 0,96 en contexte familier ; comparaisons entre études"
  - outil: ExoForge
    regle: "ne pas imposer de phase de réflexion écrite après une simulation pour des étudiants de licence ou master ; la réserver aux étudiants avancés"
    niveau: D
    transferabilite: moyenne
    note: "réflexion : g = 0,52 avec contre 0,81 sans en licence-master ; sous-groupes non causaux, surtout médicaux"
---

# Apprendre par simulation dans le supérieur (Chernikova et al., 2020)

Chernikova, O., Heitzmann, N., Stadler, M., Holzberger, D., Seidel, T. et Fischer, F. (2020). Simulation-based learning in higher education: A meta-analysis. *Review of Educational Research*, 90(4), 499-541. [DOI](https://doi.org/10.3102/0034654320933544)

**En une phrase.** Sur 145 études, surtout médicales, l'apprentissage par simulation améliore fortement des compétences complexes (g = 0,85), avec une hétérogénéité énorme ; les aides (exemples, invites, réflexion) ajoutent peu en moyenne mais leur effet dépend des connaissances préalables ; pour ExoForge, le mécanisme (agir, voir la conséquence, être guidé si l'on débute) se transpose, la valeur chiffrée non.

## La source

| | |
| --- | --- |
| **Équipe** | Psychologie de l'éducation, Ludwig-Maximilians-Universität de Munich (Fischer) ; TUM School of Education (Seidel, Holzberger). Le cadre de codage vient d'un modèle publié par le même groupe (Heitzmann et al., 2019, p. 508). |
| **Nature** | Académique ; financement de la Deutsche Forschungsgemeinschaft (DFG FOR2385, p. 527). |
| **Support** | *Review of Educational Research* (AERA, SAGE), libre accès. |
| **Audience** | 1360 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Bonne pour la méthode : bases, mots-clés, date (13 avril 2018), critères, diagramme de flux, manuel de codage en annexe, logiciel (R, metafor, robumeta) ; double codage de 50 % des études (accord > 0,80, p. 508). |

## Ce que fait l'étude

- **Corpus** (p. 507-508, 512) : PsycINFO, PsycARTICLES, ERIC, MEDLINE jusqu'en avril 2018 ; 3235 articles, 145 études (128 articles, 1979-2018), 409 effets.
- **Critères** (p. 507) : simulation dans le supérieur, mesure objective d'une compétence complexe ; plan expérimental, quasi-expérimental ou simple avant-après (sans groupe témoin).
- **Modérateurs** (p. 509-511) : type de simulation, technologie, authenticité, durée, aides (exemples, invites, phases de réflexion), connaissances préalables codées par la familiarité du contexte et le niveau d'études (licence et master « bas », post-master et professionnels « haut »).
- **Analyse** (p. 511-512) : g de Hedges corrigé du prétest, effets aléatoires, estimation robuste pour les effets dépendants ; Egger et trim and fill annoncés.

## Résultats

- **Effet global** (p. 513) : g = 0,85, SE = 0,08 ; contre absence d'intervention g = 1,02 (N = 16), contre autre enseignement g = 0,82 (N = 53), contre prétest seul g = 0,88 (N = 76). Hétérogénéité : τ² = 1,2 ; I² = 95,9 %. Intervalle de prédiction ≈ −1,3 à +3,0 [calcul : 0,85 ± 1,96 × √1,2].
- **Biais de publication** (p. 512) : « aucune indication » (entonnoir, relation effet-erreur type) ; valeurs du test d'Egger non rapportées dans le texte.
- **Compétences** (p. 513) : performance technique g = 1,06 ; résolution de problèmes 0,88 ; diagnostic 0,82 ; communication 0,44.
- **Technologie** (p. 518) : simulations sur écran g = 0,68 (N = 43), sans technologie 0,74, simulateurs 1,07, réalité virtuelle 0,85.
- **Aides** (p. 519-520) : avec ou sans exemples 0,88 contre 0,81 (ns) ; avec invites 0,65 contre 0,92 sans ; réflexion 0,78 contre 0,80.
- **Interaction avec les connaissances préalables** (p. 520-521) : contexte peu familier, invites 0,85 contre 0,63 ; contexte familier, invites 0,33 contre 0,96. Licence et master : exemples 0,88 contre 0,80 (ns) ; réflexion 0,52 contre 0,81. Exemples seuls : 1,15 (N = 9) au niveau bas contre 0,56 (N = 18) au niveau haut.

## Avis critique

**Apport.** Synthèse la plus large sur les simulations dans le supérieur, avec une analyse des aides selon le niveau des apprenants, qui rejoint l'inversion d'expertise (p. 524-525).

**Points forts**
- Méthode transparente, correction du prétest, gestion correcte des effets dépendants.
- Financement et manuel de codage déclarés.
- Limites énoncées franchement, y compris sur la généralisation (p. 525-526).

**Réserves**
1. **Majeure** — Public éloigné : 126 études sur 145 en médecine, compétences cliniques, techniques et relationnelles ; les auteurs écrivent que leurs résultats « ne se généralisent pas directement » aux sciences, mathématiques, ingénierie et informatique (p. 525).
2. **Importante** — Comparaisons avant-après sans groupe témoin pour 76 études sur 145 (p. 513) : l'effet global mêle gain de la simulation et gain de toute formation.
3. **Importante** — Hétérogénéité extrême (I² = 95,9 %), dont 4 % seulement est expliquée par les connaissances préalables (p. 526) ; l'intervalle de prédiction inclut des effets négatifs [calcul]. Les écarts entre aides sont des comparaisons entre études, souvent non significatives.
4. **Mineure** — Codage des aides incomplet : 270 effets sur 409 seulement ont des informations complètes (p. 512) ; la rétroaction, présente presque partout, n'est pas codée.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| La simulation améliore des compétences complexes dans le supérieur médical | B | Méta-analyse large, mais près de la moitié des études sans témoin |
| Ce gain vaut pour nos simulations de mécanique | D | Extrapolation exclue par les auteurs |
| Les invites aident les débutants et gênent les avancés | C | Interaction entre études, cohérente avec l'inversion d'expertise |
| Les exemples aident surtout les débutants | C | Tendance non significative en sous-groupes, plus nette dans l'analyse post hoc (N = 9) |

**Transférabilité** : faible pour la valeur de l'effet ; moyenne pour le principe d'adapter les aides au niveau des étudiants.

**Pour conclure, il faudrait** un essai dans ExoForge comparant une simulation de mécanique (par exemple une poutre dont on change les appuis) avec et sans invites, chez des L3 débutants sur le sujet et des M1 qui le connaissent.

## Pour Forge

- **ExoForge** : simulations où l'étudiant agit et voit la conséquence, en complément des exercices (niveau C, transférabilité faible).
- **ExoForge** : invites et exemple de démarche disponibles pour les débutants, facultatifs ensuite (niveau C) ; à rapprocher des fiches de l'axe D sur l'estompage et l'inversion d'expertise.
- **ExoForge** : pas de phase de réflexion écrite imposée en licence-master (niveau D).
- Le résumé de l'axe D (« exemples pour novices ») est à nuancer : la différence avec ou sans exemples n'est pas significative dans les sous-groupes (p. 520-521).
