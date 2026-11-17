---
cle: schmidt2022
reference: "Schmidt, D., Raupach, T., Wiegand, A., Herrmann, M. et Kanzow, P. (2022). Relation between examinees' true knowledge and examination scores: Systematic review and exemplary calculations on Pick-N items. Educational Research Review, 37, article 100483."
doi: 10.1016/j.edurev.2022.100483
axe: [B3]
type_etude: revue systématique des barèmes des questions à réponses multiples et « choisir N » (Pick-N), calculs des scores attendus
public: sans objet (calculs) ; contexte des examens de médecine
lecture: texte complet, 09/11/2026
regles:
  - outil: QuizForge
    regle: "question à réponses multiples dans Moodle : ne pas annoncer le nombre de bonnes réponses par défaut ; Moodle n'a pas de vrai format « choisir N » et n'empêche pas de cocher plus de cases que le nombre annoncé"
    niveau: C
    transferabilite: forte
    note: "les auteurs proposent eux-mêmes de poser une question « choisir N » comme une question à réponses multiples sans annoncer N (p. 16)"
  - outil: QuizForge
    regle: "interdire mauvaise_option: zero pour une question à réponses multiples notée : un barème qui ne compte que les bonnes options cochées donne la note maximale à qui coche tout"
    niveau: B
    transferabilite: forte
  - outil: QuizForge
    regle: "si le nombre de bonnes réponses est annoncé (« choisir N »), garder une pénalité par mauvaise option cochée et au plus la moitié d'options justes (2 <= t <= n/2) ; afficher le score au hasard et le seuil correspondant à 50 % de connaissances"
    niveau: B
    transferabilite: forte
  - outil: DiagForge
    regle: "ne pas lire la note d'une question « choisir N » comme une part de connaissances : la relation est non linéaire pour tous les barèmes ; comparer les étudiants sur des questions de même format"
    niveau: B
    transferabilite: forte
---

# Barèmes des questions « choisir N » (Schmidt et al., 2022)

Schmidt, D., Raupach, T., Wiegand, A., Herrmann, M. et Kanzow, P. (2022). Relation between examinees' true knowledge and examination scores: Systematic review and exemplary calculations on Pick-N items. *Educational Research Review*, 37, article 100483. [DOI](https://doi.org/10.1016/j.edurev.2022.100483)

**En une phrase.** Quand on annonce aux étudiants le nombre N de bonnes réponses (format « choisir N », Pick-N), aucun des 24 barèmes recensés ne donne une note proportionnelle aux connaissances ; le score au hasard va de −20 % à 80 % selon le barème, le seuil de réussite doit être recalculé pour chacun, et Moodle ne gère pas ce format : les auteurs proposent, à défaut, de poser la même question sans annoncer N.

## La source

| | |
| --- | --- |
| **Équipe** | Centre médical universitaire de Göttingen (pédagogie médicale, odontologie) et hôpital universitaire de Bonn ; mêmes auteurs que [Schmidt et al. (2021)](schmidt2021.md), dont c'est la suite. |
| **Nature** | Académique ; financement de la fondation Kurt Kaltenbach ; pas de conflit d'intérêts déclaré (p. 1). |
| **Support** | *Educational Research Review* (Elsevier). |
| **Audience** | 7 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Bonne : équations de chaque barème (tableau 2), formules des scores attendus (éq. 1-5), tableaux pour n = 5 ; la démarche se refait et les chiffres se vérifient (vérifié ici pour la méthode 12 [calcul]). Les pages citées sont celles de l'article (1 à 16). |

## Ce que fait l'étude

- **Définition** (p. 2) : dans une question à réponses multiples classique, l'étudiant coche les options vraies sans savoir combien il y en a ; dans une question « choisir N », on lui annonce ce nombre t. Usage : 5 à 26 options, avec 2 ≤ t < n (ni zéro, ni une, ni toutes justes).
- **Revue** (p. 2-3) : recherche de mars 2020 dans PubMed, Embase et PsycInfo, double extraction ; 19 sources retenues sur 1 547, plus 16 par recherche manuelle.
- **Calculs** (p. 3-5) : pour chaque barème, part des schémas de réponse distingués (« information conservée »), score moyen au hasard et score attendu selon la part de connaissances k (modèle : l'étudiant connaît une partie des bonnes options et tire les autres au hasard ; il coche exactement t cases). Deux cas : 2 ≤ t < n (A) et 2 ≤ t ≤ n/2 (B, recommandé par Bauer et al., 2011). Examens fictifs de 100 questions à 5, 6 ou 7 options.

## Résultats

- **24 barèmes** (p. 5-12, tableau 2), ramenés entre −1 et +1 point par question.
- **Score au hasard**, n = 5 (tableaux 3 et 4, p. 9 et 12), cas A / cas B :

| Barème (numéro de l'article) | Hasard A | Hasard B | Seuil pour 50 % de connaissances |
| --- | --- | --- | --- |
| Tout ou rien (1) | 13 % | 10 % | non rapporté dans le texte |
| 1/n par option bien traitée, cochée ou non (5) | 57 % | 52 % | 72,5 % (A) ; 73,0 % (B) (p. 15) |
| ±1/n par option bien ou mal traitée (9) | 15 % | 4 % | 45 % (A) ; 46 % (B) (p. 15) |
| 1/t par bonne option cochée, rien d'autre (12) | 60 % | 40 % | 75,0 % (A) ; 66,3 % (B) (p. 13) |
| +1/t par bonne option cochée, −1/(n−t) par mauvaise (19) | 0 % | 0 % | non rapporté dans le texte |
| Méthode 16 (la plus généreuse) | 80 % | 70 % | — |

- **Non-linéarité** (p. 13-14) : pour tous les barèmes, la note n'est pas proportionnelle aux connaissances ; un étudiant qui sait 50 % n'obtient 50 % avec aucun barème.
- **Cocher tout** (p. 10) : un barème qui ne compte que les bonnes options cochées donne la note maximale à qui coche toutes les cases, si le logiciel n'impose pas le nombre t ; les auteurs le déconseillent alors.
- **Recommandations** (p. 14-15) : barème qui traite également bonnes et mauvaises options ; sans points négatifs, méthode 5 avec un seuil à 73 % ; si le seuil est fixé à 50 %, méthode 9. Comparaison avec le QCM à réponse unique à 5 options noté 1/0 : seuil à 60 % pour 50 % de connaissances, contre 73 % pour la méthode 5 (p. 15).
- **Logiciels** (p. 15) : Moodle ne propose pas de question « choisir N » ; on peut écrire N dans l'énoncé d'une question à réponses multiples, mais les étudiants peuvent cocher plus de cases.
- **Conclusion** (p. 16) : utiliser ce format au cas par cas ; ou poser les mêmes questions sans annoncer le nombre de bonnes réponses, ce qui rend la relation linéaire.

## Avis critique

**Apport.** Seule fiche du dépôt qui traite directement la question « annoncer ou non le nombre de bonnes réponses » ; elle donne pour chaque barème le score au hasard et le seuil de réussite, et signale le piège du barème qui ne compte que les cases justes cochées.

**Points forts**
- Revue systématique et formules publiées ; tableaux complets pour n = 5.
- Prise en compte des contraintes réelles : logiciel (Moodle cité), seuil fixé par le règlement, interdiction des points négatifs en Allemagne.
- Recommandation conditionnelle et alternative explicite (ne pas annoncer N).

**Réserves**
1. **Importante** — Tout repose sur un modèle simple (options de même difficulté, connaissance « sait ou devine », t cases toujours cochées) ; aucune donnée d'examen réel (p. 15-16).
2. **Importante** — Le barème réellement produit par QuizForge dans Moodle (+1/t par bonne case cochée, −1/t par mauvaise, note ramenée à 0) n'est pas dans la liste ; ses valeurs sont recalculées ci-dessous avec le modèle de l'article.
3. **Mineure** — Bases de données médicales seulement (pas d'ERIC) ; seuils de 50 % de connaissances propres au contexte allemand.

**Calculs pour QuizForge** [calcul] (modèle de l'article ; marquage libre = chaque case cochée à pile ou face quand l'option est inconnue ; « choisir N » = t cases cochées) :

| Barème Moodle | Cas | Hasard | Seuil pour 50 % de connaissances |
| --- | --- | --- | --- |
| +1/t, mauvaise case 0 (`zero`) | N non annoncé | 50 % ; 100 % en cochant tout | 75 % |
| +1/t, mauvaise case −1/t (`negative`) | N non annoncé, n = 5, t = 2 | 11 % | 44 % |
| idem | N non annoncé, n = 5, t = 3 | 24 % ; 33 % en cochant tout | 59 % |
| idem | N annoncé, n = 5, t = 2 | 10 % | 40 % |
| +1/t, mauvaise case −1/(n−t) | N non annoncé, n de 4 à 6, t de 1 à 3 | 16 à 25 % ; 0 % en cochant tout | 51 à 56 % |

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Score au hasard et seuil de chaque barème | B | Calcul exact sous un modèle simple |
| Note non proportionnelle aux connaissances en « choisir N » | B | Résultat de calcul, vrai pour tous les barèmes |
| Préférer ne pas annoncer N | C | Raisonnement des auteurs, pas de données d'examen |

**Transférabilité** : forte pour les calculs ; le choix du seuil dépend du règlement local.

**Pour conclure, il faudrait** poser les mêmes questions avec et sans annonce de N à deux groupes tirés au sort dans Moodle et comparer difficulté, discrimination et fiabilité (proposé par les auteurs, p. 16).

## Pour Forge

- **QuizForge** : par défaut, ne pas annoncer le nombre de bonnes réponses dans une question à réponses multiples Moodle (niveau C).
- **QuizForge** : refuser `mauvaise_option: zero` pour une question à réponses multiples notée ; cocher toutes les cases donnerait la note maximale (niveau B).
- **QuizForge** : si N est annoncé, garder la pénalité, choisir au plus la moitié d'options justes, afficher score au hasard et seuil (niveau B).
- **QuizForge** : la pénalité −1/t de QuizForge rend le score au hasard dépendant du rapport t/n (de 6 % à 24 %) et donne des points à qui coche tout quand t > n/2 ; une pénalité −1/(n−t) stabilise le seuil autour de 50-55 % [calcul] (niveau C, à valider sur données réelles).
- **DiagForge** : ne pas convertir la note d'une question « choisir N » en part de connaissances ; comparer des questions de même format (niveau B).
- Renvois : [schmidt2021](schmidt2021.md) (vrai/faux multiples), [kanzow2023](kanzow2023.md) (réponse unique), [lesage2013](lesage2013.md) (réponses multiples, Kubinger et al., 2010, cité de seconde main).
