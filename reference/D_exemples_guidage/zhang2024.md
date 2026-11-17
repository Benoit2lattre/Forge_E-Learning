---
cle: zhang2024
reference: "Zhang, Q. et Fiorella, L. (2024). Effects of self-explaining feedback on learning from problem-solving errors. Contemporary Educational Psychology, 79, article 102326."
doi: 10.1016/j.cedpsych.2024.102326
axe: [D3]
type_etude: deux essais randomisés en ligne, une séance chacun
public: étudiants de premier cycle (États-Unis), presque tous hors sciences ; cinématique à une dimension
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "après une erreur, demander d'expliquer l'erreur avec une phrase à trous qui oriente vers le pourquoi (« J'ai appris que le déplacement est… donc je dois… »)"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "une invite ouverte « expliquez votre erreur » sans guide ne suffit pas"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "ne pas compter sur la seule mise en forme du retour (signalement, segmentation, contiguïté) pour faire apprendre de l'erreur"
    niveau: C
    transferabilite: moyenne
---

# Expliquer ses propres erreurs (Zhang et Fiorella, 2024)

Zhang, Q. et Fiorella, L. (2024). Effects of self-explaining feedback on learning from problem-solving errors. *Contemporary Educational Psychology*, 79, article 102326. [DOI](https://doi.org/10.1016/j.cedpsych.2024.102326)

**En une phrase.** En cinématique, après une erreur, des phrases à compléter qui guident l'explication de l'erreur améliorent la correction des erreurs et le transfert proche ; une invite ouverte ne fait pas mieux que rien, et un retour mieux mis en forme non plus.

## La source

| | |
| --- | --- |
| **Équipe** | Université de Géorgie (États-Unis) ; Fiorella, spécialiste de l'apprentissage génératif. |
| **Nature** | Académique ; financement National Science Foundation ; pas de conflit d'intérêts déclaré. |
| **Support** | *Contemporary Educational Psychology* (Elsevier). |
| **Audience** | 11 citations (OpenAlex, 08/11/2026) ; article récent. |
| **Reproductibilité** | Bonne : données sur l'Open Science Framework, captures du matériel en annexe ; plan non préenregistré (§ 1.4). |

Les références ci-dessous renvoient aux sections de l'article (§), la revue numérotant les articles et non les pages.

## Ce que fait l'étude

- **Contenu** : distance, déplacement, vitesse moyenne et vitesse scalaire moyenne, lecture de graphes position-temps ; leçon, exercices, retour détaillé sous forme de solution résolue, test (§ 2.2). En ligne (Qualtrics) à cause de la pandémie (§ 1.4, § 2.3).
- **Expérience 1** : 131 étudiants (128 retenus), 98 % hors sciences ; plan 2 × 2 : retour standard ou remis en forme selon trois principes multimédia (signalement, segmentation, contiguïté) ; invite ouverte à expliquer ses erreurs ou non (§ 2.1).
- **Expérience 2** : 110 étudiants recrutés ; 21 exclus faute d'erreur, 16 exclus pour ne pas avoir reconnu leur erreur ; 73 analysés : invite ouverte (25), invite guidée par des phrases à compléter (22), témoin sans invite (26) ; environ 60 minutes (§ 4.1, § 4.3).
- **Mesures** : transfert proche et éloigné immédiat, taux d'erreurs corrigées, qualité des explications.

## Résultats

- **Expérience 1** (§ 3.2) : aucun effet de la mise en forme du retour ; l'invite ouverte améliore le transfert proche seulement avec le retour standard (interaction, p = 0,050) ; pas d'effet en transfert éloigné. La qualité des explications est liée aux résultats.
- **Expérience 2** (§ 5.2) : l'invite guidée fait mieux que le témoin en transfert proche (d = 0,73) et en correction des erreurs (d = 0,70), et mieux que l'invite ouverte (d = 0,62 et 0,73) ; l'invite ouverte ne fait pas mieux que le témoin ; aucun effet en transfert éloigné.

## Avis critique

**Apport.** Un essai récent, sur un contenu de mécanique, qui montre qu'apprendre de ses erreurs demande une explication guidée : le retour seul, même bien présenté, et l'invite ouverte ne suffisent pas.

**Points forts**
- Données ouvertes ; matériel visible en annexe.
- Deux expériences, la seconde construite pour répondre aux limites de la première.
- Contenu de mécanique de base, proche de nos sujets.

**Réserves**
1. **Importante** — Exclusions après tirage au sort : 37 étudiants sur 110 (34 %) dans l'expérience 2 [calcul], dont 16 pour ne pas avoir reconnu leur erreur ; l'équilibre entre groupes peut en souffrir.
2. **Importante** — Petits groupes (22 à 26) et une seule séance avec test immédiat ; pas d'effet en transfert éloigné.
3. **Importante** — Les groupes invités passent du temps à écrire pendant que le témoin passe au problème suivant (§ 4.3) : le temps de travail n'est pas égal.
4. **Mineure** — Public non scientifique à faibles connaissances initiales ; les auteurs notent qu'il n'est pas représentatif (§ 6).
5. **Mineure** — Une phrase du § 5.2 compare « témoin et invite guidée » là où le contexte indique « témoin et invite ouverte » (coquille probable).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Une explication guidée de l'erreur améliore la correction et le transfert proche | C | Un essai, petits groupes, exclusions, temps inégal |
| Une invite ouverte sans guide n'aide pas | C | Résultat différent selon les deux expériences |
| La mise en forme multimédia du retour n'aide pas à apprendre de l'erreur | C | Une expérience, trois principes appliqués ensemble |

**Transférabilité** : forte pour le mécanisme (exercices de mécanique avec retour, comme ExoForge) ; moyenne pour l'ampleur, le public étant non scientifique.

**Pour conclure, il faudrait** tester les phrases à compléter dans ExoForge avec des étudiants de L3, à temps égal et avec un test différé.

## Pour Forge

- **ExoForge** : après une erreur, proposer une ou deux phrases à compléter qui orientent vers la cause (« J'ai appris que… donc je dois… ») avant de passer à la suite (niveau C).
- **ExoForge** : éviter l'invite ouverte seule (niveau C).
- **ExoForge** : soigner la présentation du retour reste utile, mais ne remplace pas l'explication demandée à l'étudiant (niveau C). À rapprocher de Moreno et al. (2009) : après une erreur, montrer l'étape analogue d'un exemple puis faire réessayer.
