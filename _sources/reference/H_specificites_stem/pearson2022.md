---
cle: pearson2022
reference: "Pearson, C. et Penna, N. (2023). Automated marking of longer computational questions in engineering subjects. Assessment & Evaluation in Higher Education, 48(7), 915-925 (en ligne le 12/11/2022)."
doi: 10.1080/02602938.2022.2144801
axe: [H1]
type_etude: étude descriptive de notes réelles (devoirs notés, Numbas) ; une évaluation renotée selon cinq barèmes de report d'erreur (57 étudiants) ; quatre devoirs différents comparés selon le nombre d'étapes intermédiaires ; pas de tirage au sort
public: licence de génie civil et d'ingénierie géospatiale (topographie), université de Newcastle (Royaume-Uni)
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "dans un exercice en plusieurs étapes, recalculer la réponse attendue de chaque étape à partir des saisies précédentes de l'étudiant (report d'erreur) au lieu de la comparer à la seule valeur exacte"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "rendre paramétrable le crédit accordé à une étape juste mais calculée sur une valeur fausse (0 à 100 %) ; valeur par défaut 25 à 50 % quand un contrôle de vraisemblance du résultat est possible"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "découper un long calcul en environ 3 à 4 étapes notées : sans étape, notes en tout ou rien ; avec trop d'étapes, la démarche est donnée et les notes sont gonflées"
    niveau: C
    transferabilite: moyenne
  - outil: DiagForge
    regle: "afficher la distribution des notes par exercice et signaler une distribution bimodale (tout ou rien) ou concentrée vers le maximum"
    niveau: D
    transferabilite: forte
---

# Notation automatique des longs calculs avec report d'erreur (Pearson et Penna, 2022)

Pearson, C. et Penna, N. (2023). Automated marking of longer computational questions in engineering subjects. *Assessment & Evaluation in Higher Education*, 48(7), 915-925 (en ligne le 12/11/2022). [DOI](https://doi.org/10.1080/02602938.2022.2144801)

**En une phrase.** Dans des devoirs de topographie notés automatiquement avec Numbas, les auteurs conseillent d'accorder 25 à 50 % du crédit à une étape juste calculée sur une valeur fausse et de découper un long calcul en environ trois étapes ; ces recommandations reposent sur la forme des distributions de notes, pas sur une mesure d'apprentissage.

## La source

| | |
| --- | --- |
| **Équipe** | École d'ingénieurs de l'université de Newcastle ; enseignants de topographie dont la recherche principale est la géodésie GNSS (p. 924). Numbas est développé dans la même université (p. 917). |
| **Nature** | Académique ; aucun conflit d'intérêts déclaré (p. 923). Financement non rapporté. |
| **Support** | *Assessment & Evaluation in Higher Education* (Taylor & Francis), libre accès. |
| **Audience** | 4 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : barèmes et tableau des notes publiés (tableau 1), questions décrites mais non publiées, données individuelles non publiées. Le renotage se refait facilement sur nos propres données. |

## Ce que fait l'étude

- **Report d'erreur** (p. 917-918) : une évaluation de nivellement (57 étudiants ; deux questions : un tableau de 30 cases dépendantes, un test « deux piquets » en 4 parties) renotée selon cinq barèmes : 0, 25, 50, 75 et 100 % du crédit pour une étape juste calculée sur une valeur fausse.
- **Critère** (p. 918) : une évaluation « juste et efficace » donnerait des notes de distribution normale (test de Shapiro-Wilk) ; justification : 19 des 20 profils de notes de modules de première année sur 10 ans sont normaux.
- **Nombre d'étapes** (p. 920-923) : quatre devoirs différents à valeurs tirées par étudiant, sur plusieurs semaines, sans indice : A trilatération (150 étudiants, aucune étape), B coordonnées polaires (58, aucune étape), C relèvement (28, neuf étapes, report d'erreur à 25 %), D facteurs d'échelle (123, trois étapes).

## Résultats

| Barème de report (tableau 1, p. 919) | 0 % | 25 % | 50 % | 75 % | 100 % |
| --- | --- | --- | --- | --- | --- |
| Moyenne sur 100 | 60,0 | 61,4 | 62,9 | 64,3 | 65,7 |
| Écart-type | 20,1 | 19,7 | 19,3 | 18,9 | 18,6 |
| p de Shapiro-Wilk | 0,13 | 0,10 | 0,06 | 0,03 | 0,01 |

- **Choix du barème** (p. 918) : 75 et 100 % jugés non normaux ; 0 % écarté parce qu'il ne distingue pas une erreur unique d'erreurs multiples ; 25 % retenu ensuite dans tous les devoirs de topographie. L'écart entre 0 et 100 % est de 5,7 points de moyenne [calcul].
- **Sans étape** (p. 921) : A moyenne 72 %, écart-type 35 % ; B moyenne 46 %, écart-type 42 % ; distributions bimodales (fig. 3-4).
- **Neuf étapes** (p. 921-922) : C moyenne 87 %, écart-type 25 %, 24 sur 28 au-dessus de 70 %.
- **Trois étapes** (p. 922-923) : D moyenne 64 %, écart-type 30 % ; encore des grappes près de 0 et de 100, mais plus de notes entre 30 et 80 %.
- **Avis des étudiants** (p. 923) : plus de 60 % préfèrent Numbas, 19 % le papier ; questionnaire non décrit (effectif et questions non rapportés).

## Avis critique

**Apport.** Un des rares articles qui chiffrent l'effet du barème de report d'erreur sur des notes réelles d'ingénierie, et qui posent la question du nombre d'étapes à afficher dans un calcul long noté automatiquement.

**Points forts**
- Renotage des mêmes copies sous cinq barèmes : seule la règle de notation change.
- Problème concret et fréquent en ingénierie (calculs enchaînés, vérification possible du résultat).
- Limite reconnue : le nombre d'étapes dépend de l'application et doit être fixé empiriquement (p. 923).

**Réserves**
1. **Majeure** — La normalité des notes est prise comme critère de justesse d'une évaluation ; ce critère n'est pas un critère de validité (une évaluation de maîtrise peut légitimement donner des notes concentrées vers le haut), et avec 57 étudiants le test de Shapiro-Wilk sépare mal des p de 0,06 et 0,03.
2. **Majeure** — Nombre d'étapes : quatre devoirs sur des sujets, promotions et effectifs différents ; la difficulté propre de chaque sujet est confondue avec le nombre d'étapes, et une seule évaluation a trois étapes. La règle « 3 à 4 étapes » est une observation, pas une comparaison.
3. **Importante** — Aucune mesure d'apprentissage ni de validité (corrélation avec un examen, avis de correcteurs) ; l'effet du découpage sur ce que l'étudiant apprend à faire seul n'est pas mesuré.
4. **Mineure** — Devoir sur plusieurs semaines : la collaboration entre étudiants n'est pas contrôlée (reconnu p. 920, 923).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Le report d'erreur se calcule automatiquement et change peu la moyenne | C | Renotage d'une seule évaluation, 57 étudiants |
| 25 à 50 % de crédit en report d'erreur | C | Critère de normalité discutable ; argument de vraisemblance du résultat recevable |
| Sans étape, notes en tout ou rien ; trop d'étapes, notes gonflées | C | Observations concordantes mais sujets confondus |
| Environ 3 étapes est le bon découpage | D | Une seule évaluation |

**Transférabilité** : forte pour le mécanisme (calculs enchaînés en mécanique : réactions puis efforts internes puis contraintes) ; moyenne pour les valeurs de barème et de nombre d'étapes.

**Pour conclure, il faudrait** dans ExoForge, sur un même exercice de mécanique, tirer au sort 0, 3 ou 6 étapes affichées et mesurer la réussite à un exercice analogue sans étape une semaine plus tard ; renoter aussi nos propres exercices sous plusieurs barèmes de report.

## Pour Forge

- **ExoForge** : report d'erreur dans les exercices en plusieurs étapes (C), avec crédit paramétrable, 25 à 50 % par défaut (C) ; découpage en 3 à 4 étapes notées, à ajuster (C).
- **DiagForge** : signaler les distributions bimodales ou plafonnées par exercice (D).
- Renvois : [greenhow2015](greenhow2015.md) (questions en parties avec report de la saisie), [kinnear2022](kinnear2022.md) (question ouverte sur la notation partielle), `borchers2025` (axe D : faire saisir les étapes porteuses de sens).
