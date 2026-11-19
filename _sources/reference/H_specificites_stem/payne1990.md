---
cle: payne1990
reference: "Payne, S. J. et Squibb, H. R. (1990). Algebra mal-rules and cognitive accounts of error. Cognitive Science, 14(3), 445-481."
doi: 10.1016/0364-0213(90)90019-s
axe: [H3]
type_etude: étude descriptive d'erreurs (copies avec étapes intermédiaires, trois écoles, deux tests de 28 équations), sans intervention
public: élèves de 13-14 ans de trois collèges anglais (Lancaster), 86 élèves diagnostiqués sur 133 testés (80 après retrait de 6 élèves aux erreurs atypiques), équations du premier degré à une inconnue
lecture: texte complet (scan, OCR imparfait ; tableau 3 lu en image), 10/11/2026
regles:
  - outil: ExoForge
    regle: "catalogue d'erreurs types en algèbre écrit sous forme condition -> action (motif de départ -> résultat erroné, avec M, N, P entiers et pat pour une sous-expression), chaque règle exécutable sur les paramètres tirés ; garder les catégories « erreur de calcul » et « non diagnostiquée » à côté des règles"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "retour ciblé formulé sur l'étape (« cette étape applique a(b + c) = ab + c ») et non sur une croyance supposée de l'étudiant : une même personne applique la règle juste dans la plupart des occasions"
    niveau: C
    transferabilite: moyenne
    note: "presque toutes les proportions d'usage d'une règle erronée par élève sont inférieures à 50 % des occasions (tableau 6, p. 456)"
  - outil: ExoForge
    regle: "faire saisir les étapes intermédiaires (au moins l'équation après chaque transformation) quand on veut diagnostiquer une erreur d'algèbre : la réponse finale seule laisse des erreurs ambiguës ou non diagnosticables"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "leurres numériques des équations linéaires et des développements tirés des erreurs types les plus fréquentes : Mx + N -> (M + N)x, terme changé de membre sans changer de signe, M(pat) -> M + pat, distribution au seul premier terme ; vérifier ensuite leur fréquence sur nos propres réponses"
    niveau: C
    transferabilite: moyenne
  - outil: DiagForge
    regle: "rapporter une erreur type par sa fréquence d'usage sur les occasions où elle pouvait s'appliquer (nombre d'usages / nombre d'occasions), pas par sa simple présence ; ne qualifier une erreur de systématique qu'au-delà de la moitié des occasions"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "suivre la part des réponses fausses que le catalogue explique (toutes règles, 10 premières, 5 premières) et la part non diagnostiquée ; ajouter au catalogue les règles nouvelles observées localement"
    niveau: C
    transferabilite: forte
    note: "les 10 règles les plus fréquentes d'une école diagnostiquent moins de 50 % et moins de 10 % des erreurs des deux autres (p. 455)"
---

# Erreurs types en algèbre : nombreuses, rares et instables (Payne et Squibb, 1990)

Payne, S. J. et Squibb, H. R. (1990). Algebra mal-rules and cognitive accounts of error. *Cognitive Science*, 14(3), 445-481. [DOI](https://doi.org/10.1016/0364-0213(90)90019-s)

**En une phrase.** Dans les équations du premier degré, 99 règles erronées (mal-rules) sont nécessaires pour décrire les erreurs d'élèves de 13-14 ans de trois collèges, mais quelques-unes dominent, elles diffèrent d'une école à l'autre et chaque élève ne les applique que dans une minorité des occasions : un catalogue d'erreurs types est utile pour le retour et le diagnostic, à condition d'être local, ouvert et lu en fréquence d'usage.

## La source

| | |
| --- | --- |
| **Équipe** | Université de Lancaster (psychologie cognitive, interfaces) ; le premier auteur est ensuite à l'IBM T. J. Watson Research Center (adresse de correspondance, p. 445). |
| **Nature** | Académique ; financement Alvey/SERC (subvention GR/D 60355), en collaboration avec British Telecommunications plc (p. 445). |
| **Support** | *Cognitive Science*, revue de référence en sciences cognitives. |
| **Audience** | 119 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Moyenne : les 56 équations sont publiées en annexe (p. 479-481) et les règles sont écrites sous forme de schémas ; copies et codages non publiés, pas d'accord entre codeurs rapporté. La démarche se refait sur nos copies ; les chiffres ne se vérifient pas. |

## Ce que fait l'étude

- **Matériel** (p. 447-448, tableau 1) : 14 types d'équations à une inconnue (de Mx = P à Mx + N = Px + Q), repris en partie de Sleeman (1985) ; deux tests de 28 équations à solution entière, de même forme et de nombres différents.
- **Trois écoles** (p. 448-450) : école 1, 58 élèves, test A « réponds à tout » et test B « réponds seulement si tu es sûr », une semaine d'écart ; 18 exclus pour consignes non suivies et 7 sans étapes écrites, reste 33. École 2 (filles sélectionnées, très bonnes en algèbre), 29 élèves, deux tests le même jour avec note de confiance de 1 à 5. École 3 (classes hétérogènes), 46 élèves, un test de 56 équations en 50 min avec confiance ; 21 n'écrivent aucune étape, reste 24. Après retrait de 6 élèves aux erreurs atypiques (1 et 5), les tableaux portent sur 32, 29 et 19 élèves (p. 452, 455).
- **Codage** (p. 451-452) : chaque erreur est rattachée à une règle erronée, à une erreur de calcul ou à « non diagnosticable » ; en cas d'ambiguïté, préférer une règle unique à une combinaison et pas d'étapes cachées « faire puis défaire ».

## Résultats

- **Taux de réussite** (p. 450) : école 1, 52 % (test A) et 60 % (test B) ; école 2, 91 % et 94 % ; école 3, 56 %.
- **Taille du catalogue** (p. 452) : 99 règles erronées distinctes ; 43 n'apparaissent qu'une fois et 14 autres au plus trois fois.
- **Règles les plus fréquentes, école 1** (tableau 3, p. 453 ; occurrences, puis nombre d'élèves) : Mx +/- N -> (M +/- N)x, 80 (17) ; terme constant changé de membre sans changer de signe, 65 (27) ; terme en x changé de membre sans changer de signe, 52 (24) ; M(pat) -> M + pat, 51 (15) ; Mx +/- N -> M +/- N (x perdu), 37 (17) ; Mx - N = Px + Q -> Mx + Px = N + Q, 35 (22) ; + remplacé par -, 34 (18) ; - remplacé par +, 29 (15) ; M(Nx +/- P) -> MNx +/- P (distribution au premier terme), 24 (12) ; M +/- N(pat) -> (M +/- N)(pat), 19 (15) ; M(NP) -> MNMP, 17 (11) ; A + B -> B - A, 17 (13) ; Mx = N -> x = M + N, 16 (7) ; Mx = N -> x = N, 12 (4). Erreurs de calcul 39 ; non diagnosticables 81.
- **Pouvoir diagnostique** (p. 452-453) : part des erreurs expliquées (règles et erreurs de calcul) : école 1, 87 % avec toutes les règles, 67 % avec les 10 premières, 37 % avec les 5 premières ; école 2, 97 %, 82 %, 72 % ; école 3, 82 %, 52 %, 42 %.
- **Meilleur diagnostic chez les meilleurs élèves** (p. 454-455) : corrélation entre réussite et part des copies diagnostiquées r = 0,47 (n = 32), 0,37 (n = 29), 0,44 (n = 19).
- **Peu de recouvrement** (p. 455) : les 10 règles les plus puissantes de l'école 1 expliquent moins de 50 % des erreurs de l'école 2 et moins de 10 % de celles de l'école 3 ; 6 seulement des 22 règles les plus diagnostiques figuraient chez Sleeman.
- **Instabilité** (tableau 6, p. 455-456) : la grande majorité des élèves appliquent une règle dans moins de 50 % des occasions, estimation volontairement haute ; exceptions M(NP) -> MNMP et -M(Nx - P) -> -MNx - MP, qui ont très peu d'occasions.
- **Contexte** (p. 457-460) : pas de lien entre la complexité de l'équation et la fréquence d'une règle (aucune des 9 corrélations de Spearman significative) ; pas d'effet net des nombres, mais les équations n'ont pas été construites pour le tester.
- **Six élèves « idiosyncrasiques »** (p. 460-462) : erreurs régulières mais non descriptibles par des règles (deux réponses pour deux termes en x, somme des entiers de chaque membre puis division).
- **Confiance** (p. 462-464) : les élèves sont plus confiants dans leurs bonnes réponses (moyennes 4,77 contre 3,54 à l'école 2 ; 4,05 contre 2,23 à l'école 3), mais toutes les règles fréquentes apparaissent dans des réponses notées 4 ou 5 : la confiance ne sépare pas des règles « crues » de règles « au hasard ».

## Avis critique

**Apport.** Premier relevé chiffré d'un catalogue d'erreurs types en algèbre, avec un format de règle directement transposable (motif -> résultat erroné) et trois constats qui pèsent sur la conception : catalogue long et local, quelques règles dominantes, usage instable.

**Points forts**
- Trois écoles et deux protocoles, ce qui montre la dépendance au contexte.
- Les règles sont écrites sous une forme exécutable, avec les conventions de notation (p. 451).
- Mesure de la stabilité rapportée aux occasions et pas seulement aux occurrences.

**Réserves**
1. **Importante** — Fortes pertes : 86 élèves diagnostiqués sur 133 testés ; 18 exclus pour consignes non suivies et 28 faute d'étapes écrites (p. 449-450) ; les élèves qui n'écrivent rien sont probablement aussi les plus faibles, ce qui peut gonfler la part diagnostiquée.
2. **Importante** — Codage par les auteurs, sans second codeur ni accord rapporté ; l'attribution d'une règle dépend des heuristiques retenues (p. 452).
3. **Mineure** — Public de 13-14 ans et équations à solution entière ; les auteurs notent eux-mêmes que ce choix rend certaines règles (division inversée) rares (p. 459).
4. **Mineure** — Texte scanné ; les chiffres cités ont été relus sur la page en image pour le tableau 3.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Distribution très inégale : peu de règles fréquentes, beaucoup de rares | C | Trois écoles concordantes, codage non vérifié |
| Les règles fréquentes diffèrent d'une école à l'autre | C | Trois échantillons, protocoles différents |
| Usage instable par un même élève | C | Estimation par excès, mais constat net |
| Le diagnostic réussit mieux chez les élèves plus forts | C | Corrélations modérées, trois petits échantillons |
| Les erreurs ne se rangent pas en « étourderies » et « conceptions » | D | Discussion théorique (section 6) |

**Transférabilité** : moyenne pour les règles elles-mêmes (collège), forte pour le format et les constats de méthode. Les erreurs d'algèbre restent fréquentes dans les calculs de mécanique (voir [Gross et Dinehart, 2012](gross2012.md)) ; la corrélation avec le niveau laisse penser, sans preuve, que les règles sont plus diagnostiques chez des étudiants avancés (niveau D).

**Pour conclure, il faudrait** coder dans ExoForge 10 à 15 règles d'algèbre de ce catalogue sur des exercices de mise en équation en mécanique, mesurer sur un semestre la part des réponses fausses expliquée et la fréquence d'usage par étudiant, puis comparer au taux de Payne et Squibb.

## Pour Forge

- **ExoForge** : format commun du catalogue d'erreurs types (identifiant, motif -> résultat erroné, domaine de validité, retour associé), exécuté sur les paramètres tirés (niveau C). Rejoint la règle de [Tatsuoka (1983)](tatsuoka1983.md) et de [Sikurajapathi et al. (2023)](sikurajapathi2023.md) : rejeter les tirages où une règle donne la bonne valeur.
- **ExoForge** : retour formulé sur l'étape, pas sur la personne (niveau C) ; saisie des étapes intermédiaires quand le diagnostic compte (niveau C).
- **QuizForge** : leurres d'équations linéaires issus des règles fréquentes (niveau C), à recaler sur nos données.
- **DiagForge** : fréquence d'usage par occasion et part des erreurs expliquée par le catalogue, mise à jour du catalogue par les erreurs non diagnostiquées (niveau C). Confirme la gradation absente, intermittente, systématique de [Klingbeil et al. (2024)](klingbeil2024.md).
