---
cle: burton2005
reference: "Burton, R. F. (2005). Multiple-choice and true/false tests: myths and misapprehensions. Assessment & Evaluation in Higher Education, 30(1), 65-72."
doi: 10.1080/0260293042003243904
axe: [B3]
type_etude: essai argumentatif (douze idées reçues discutées), appuyé sur des calculs de probabilité et les travaux antérieurs de l'auteur ; pas de données nouvelles
public: sans objet ; examens QCM et vrai/faux de l'enseignement supérieur (physiologie, médecine)
lecture: texte complet, 10/11/2026
regles:
  - outil: DiagForge
    regle: "pour un quiz court, afficher la marge due au hasard autour de la note (écart-type binomial des réponses devinées) et ne pas trancher réussite ou échec près du seuil sur un seul quiz"
    niveau: B
    transferabilite: forte
    note: "calcul exact sous le modèle « sait ou devine au hasard » ; vérifié ici (p. 67) [calcul]"
  - outil: QuizForge
    regle: "afficher aux étudiants une consigne cohérente avec le barème : sans pénalité, répondre à toutes les questions ; avec pénalité, une réponse fondée sur une connaissance partielle vaut en moyenne d'être donnée"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "vrai/faux noté sans pénalité : à éviter dans un quiz court (une chance sur deux de deviner) ; prévoir une pénalité ou un seuil relevé"
    niveau: C
    transferabilite: forte
    note: "convergent avec schmidt2021 (niveau B) pour le vrai/faux multiple"
  - outil: DiagForge
    regle: "ne pas comparer l'alpha de Cronbach de deux quiz passés par des groupes différents sans regarder la dispersion des notes : l'alpha dépend du groupe autant que du test"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "s'en tenir aux indicateurs de la théorie classique (réussite, discrimination, fiabilité) pour des quiz de cours ; pas de modèle de réponse à l'item"
    niveau: D
    transferabilite: forte
---

# Idées reçues sur le hasard et les barèmes des QCM et vrai/faux (Burton, 2005)

Burton, R. F. (2005). Multiple-choice and true/false tests: myths and misapprehensions. *Assessment & Evaluation in Higher Education*, 30(1), 65-72. [DOI](https://doi.org/10.1080/0260293042003243904)

**En une phrase.** Douze idées reçues sur les QCM et les vrai/faux, discutées par un examinateur de physiologie : le hasard pèse lourd sur la note d'un étudiant proche du seuil, les points négatifs dissuadent de deviner sans « corriger » le hasard, et un coefficient de fiabilité dépend du groupe autant que du test ; argumentation solide en probabilités, mais sans données nouvelles.

## La source

| | |
| --- | --- |
| **Équipe** | Un auteur, Institute of Biomedical and Life Sciences, université de Glasgow ; chercheur honoraire en physiologie, longue pratique d'examinateur (p. 65, 71). |
| **Nature** | Académique ; financement non rapporté. Article d'opinion fondé en partie sur les travaux de l'auteur : 5 des 23 références sont de lui [décompte]. |
| **Support** | *Assessment & Evaluation in Higher Education* (Taylor & Francis). |
| **Audience** | 95 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Sans objet (essai) ; pas de méthode de sélection de la littérature. Le seul calcul chiffré (p. 67) se refait et se vérifie [calcul]. Les pages citées sont celles de la revue (65 à 72). |

## Ce que fait l'étude

- **Cadre** (p. 65-66) : fiabilité des tests sans contrainte de temps ; format, longueur et barème (une bonne réponse = 1 point, ou points négatifs) ; « QCM » = au moins trois options.
- **Douze idées reçues** (p. 66), discutées une à une (p. 67-71) : effet du hasard sur la fiabilité (1-4), points négatifs (5-8), portée du vrai/faux (9), longueur des tests (10), coefficients de fiabilité (11), modèles de réponse à l'item (12).

## Résultats

- **Le hasard près du seuil** (p. 67) : obtenir 60 sur 70 au hasard à un vrai/faux est très improbable (3 × 10⁻¹⁰), mais ce n'est pas la question ; un étudiant qui connaît 35 réponses sur 70 et devine le reste a 9 % de risque d'avoir moins de 49 et 9 % d'avoir plus de 56, pour un seuil à 53. Vérifié : 8,8 % de chaque côté [calcul : 35 + loi binomiale (35 ; 0,5)].
- **Leurres peu plausibles** (p. 67) : ils réduisent le nombre effectif d'options, rendent la réponse moins aléatoire, élèvent les notes et réduisent la fiabilité.
- **Questions bien écrites ou complexes** (p. 67) : elles ne réduisent pas le hasard « à l'aveugle » ; quand on ne sait rien, on devine.
- **Points négatifs** (p. 67-69) : leur but est de dissuader de deviner à l'aveugle, pas de « corriger » le hasard ; ils pénalisent aussi les erreurs commises avec assurance, ce qui peut améliorer la fiabilité. Les étudiants diffèrent par le goût du risque ; pour des vrai/faux de 300 items, cet effet pèse moins que celui du hasard sans pénalité (Burton, 2002, cité par l'auteur) ; aucune donnée équivalente pour les QCM. Les consignes doivent dire qu'une réponse fondée sur une intuition ou une connaissance partielle vaut en moyenne d'être donnée.
- **Vrai/faux** (p. 69) : avec une chance sur deux de deviner, les points négatifs sont « presque une nécessité » sauf test très long ; un vrai/faux peut poser des problèmes difficiles (Ebel, 1979).
- **Longueur** (p. 70) : 60 items ne suffisent pas à échantillonner un vaste domaine (modèle idéalisé, Posey, 1932 ; Ebel, 1979) ; des items plus longs à lire (leurres élaborés) obligent à réduire leur nombre.
- **Fiabilité** (p. 70-71) : un coefficient de fiabilité dépend de la dispersion des connaissances dans le groupe ; ajouter des étudiants qui ne savent rien l'augmente ; il ne voit pas l'effet du goût du risque.
- **Modèles de réponse à l'item** (p. 71) : pas mieux que la théorie classique pour des examens universitaires, d'après les comparaisons citées.

## Avis critique

**Apport.** Rappelle, chiffres à l'appui, que le hasard rend incertaine la note individuelle d'un étudiant proche du seuil, même quand le seuil moyen est bien corrigé : complément utile aux fiches sur les barèmes ([kanzow2023](kanzow2023.md), [schmidt2021](schmidt2021.md)), qui raisonnent sur des moyennes.

**Points forts**
- Arguments de probabilité vérifiables (vérifié ici pour l'exemple de la p. 67).
- Distinction nette entre dissuader de deviner et corriger le hasard.
- Mise en garde utile sur la lecture des coefficients de fiabilité.

**Réserves**
1. **Majeure** — Essai sans méthode ni données nouvelles ; les affirmations sur les points négatifs reposent surtout sur les travaux de l'auteur (Burton, 2002 ; 2004b) et sur des vrai/faux de 300 items, loin de nos quiz.
2. **Importante** — Aucune donnée pour les QCM sur l'arbitrage entre goût du risque et hasard (l'auteur le dit, p. 68) : la préférence pour les points négatifs n'est étayée que pour le vrai/faux.
3. **Mineure** — Ne traite pas le vrai/faux multiple, ni les questions à plusieurs bonnes réponses ; contexte médical britannique de 2005.

**Calcul pour QuizForge** [calcul] (modèle « sait ou devine au hasard », barème 1/0) : un quiz de 20 QCM à 3 options, étudiant qui connaît 10 réponses et devine les 10 autres : 3,3 bonnes réponses de plus en moyenne, écart-type 1,5 question, soit 7,5 points de pourcentage ; avec le seuil de 66,7 % (14 sur 20, [kanzow2023](kanzow2023.md)), il réussit dans 44 % des cas ; s'il connaît 12 réponses, dans 80 % des cas.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Le hasard rend la note individuelle incertaine, surtout dans un test court | B | Calcul exact sous un modèle simple, vérifié |
| Les points négatifs dissuadent de deviner sans corriger le hasard | C | Argument logique et données de l'auteur sur le vrai/faux |
| Points négatifs préférables pour le vrai/faux court | C | Données de l'auteur, tests de 300 items |
| Un coefficient de fiabilité dépend du groupe | C | Propriété connue, illustrée sans données ici |
| Théorie classique suffisante pour des examens de cours | D | Opinion appuyée sur une seule comparaison citée |

**Transférabilité** : forte pour les calculs et les mises en garde (quiz Moodle courts, à seuil) ; faible pour les valeurs issues de tests de 300 items.

**Pour conclure, il faudrait** estimer, sur une année de quiz QuizForge, la part d'étudiants dont la décision réussite / échec change selon la marge due au hasard, avec et sans pénalité, et la comparer à l'effet du goût du risque (part de non-réponses).

## Pour Forge

- **DiagForge** : pour un quiz court, afficher la marge due au hasard autour de la note et ne pas trancher près du seuil sur un seul quiz (niveau B).
- **QuizForge** : consigne au début du quiz cohérente avec le barème (répondre à tout sans pénalité ; avec pénalité, répondre quand on a une connaissance partielle) (niveau C).
- **QuizForge** : pas de vrai/faux sans pénalité dans un quiz court (niveau C ; voir [schmidt2021](schmidt2021.md), niveau B).
- **DiagForge** : lire l'alpha avec la dispersion des notes du groupe ; ne pas comparer deux alphas de groupes différents sans précaution (niveau C ; voir [slepkov2021](../C_analyse_items/slepkov2021.md)).
- **DiagForge** : théorie classique des tests suffisante pour des quiz de cours (niveau D).
- Renvois : [lesage2013](lesage2013.md) (barèmes et goût du risque), [kanzow2023](kanzow2023.md) (seuil du QCM à réponse unique), [schmidt2021](schmidt2021.md) (vrai/faux multiples).
