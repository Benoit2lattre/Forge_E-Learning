---
cle: sikurajapathi2023
reference: "Sikurajapathi, I., Henderson, K. L. et Gwynllyw, D. R. (2023). Correct for the wrong reason: why we should know more about Mathematical Common Student Errors in e-Assessment questions. MSOR Connections, 21(1), 43-51."
doi: 10.21100/msor.v21i1.1393
axe: [H3, H1]
type_etude: rapport de pratique (six cas de questions à paramètres aléatoires), sans données sur les étudiants
public: "première année d'ingénierie, module de mathématiques de l'ingénieur, UWE Bristol (examens 2018 et 2019, 298 et 321 étudiants), système Dewis"
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "à la génération, calculer la clé et chaque erreur type pour le tirage, et retirer les paramètres tant que la clé, à la précision demandée, coïncide avec une erreur type ou que deux erreurs types coïncident"
    niveau: B
    transferabilite: forte
  - outil: ExoForge
    regle: "faire la comparaison à la précision d'arrondi demandée à l'étudiant (2 ou 3 décimales), pas en valeur exacte"
    niveau: B
    transferabilite: forte
  - outil: ExoForge
    regle: "exclure d'une liste de valeurs les paramètres qui annulent structurellement une erreur type (exposant 2 quand l'erreur confond (x^b)^2 et x^(b^2) ; intervalle de longueur 1 quand l'erreur oublie de diviser par la longueur)"
    niveau: B
    transferabilite: forte
  - outil: ExoForge
    regle: "n'afficher le retour propre à une erreur type que si la réponse est fausse et correspond à cette erreur"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "ne retenir comme erreur type qu'une réponse fausse donnée par au moins 4 % des réponses fausses à la question (seuil des auteurs)"
    niveau: D
    transferabilite: moyenne
---

# Juste pour une mauvaise raison : paramètres et erreurs types (Sikurajapathi et al., 2023)

Sikurajapathi, I., Henderson, K. L. et Gwynllyw, D. R. (2023). Correct for the wrong reason: why we should know more about Mathematical Common Student Errors in e-Assessment questions. *MSOR Connections*, 21(1), 43-51. [DOI](https://doi.org/10.21100/msor.v21i1.1393)

**En une phrase.** Dans des questions à paramètres aléatoires, certains tirages font coïncider la bonne réponse et une erreur type (à la précision demandée), si bien qu'un étudiant qui se trompe reçoit la note maximale ; les auteurs décrivent six cas et la correction : retirer les paramètres jusqu'à ce que clé et erreurs types diffèrent.

## La source

| | |
| --- | --- |
| **Équipe** | École d'informatique et de technologies créatives, UWE Bristol ; même équipe que [sikurajapathi2020](sikurajapathi2020.md), développeurs de Dewis. |
| **Nature** | Académique ; rapport sur leur propre outil et leur propre module. Financement et conflits d'intérêts non rapportés. |
| **Support** | *MSOR Connections* (revue britannique de pratique en enseignement des mathématiques, statistique et recherche opérationnelle), libre accès. |
| **Audience** | 1 citation (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Bonne pour la démarche : chaque cas donne la forme générique, un tirage fautif et le calcul ; les collisions se vérifient à la main. Code non publié. |

## Ce que fait l'étude

- **Recueil des erreurs** (p. 44-45) : examens en ligne de janvier 2018 et 2019 (298 et 321 étudiants) avec brouillons ; réponses fausses les plus fréquentes examinées dans les brouillons ; une réponse est retenue comme erreur type si elle représente au moins 4 % des réponses fausses à la question.
- **Capture** (p. 45) : un indicateur ajouté à chaque question vaut 1 si l'erreur type est reconnue ; code validé en renotant les examens de 2017-2018, puis renotage des tests hebdomadaires et de révision.
- **Constat** (p. 45-49) : lors du renotage, des tirages où clé et erreur type sont égales.

## Résultats

| Cas (p. 46-49) | Question | Erreur type | Tirage où les deux coïncident |
| --- | --- | --- | --- |
| 1 | f(t) = a u(t+b) - c u(t+d), valeur en p | u traité comme le nombre 1 | a = 2, b = 7, c = 5, d = 1, p = 4 : -3 |
| 2 | somme d'une série géométrique infinie, 3 décimales | somme des quatre premiers termes | a = 2, r = 0,1 |
| 3 | développement limité de e^(ax) à l'ordre 3 en x = c | valeur exacte au lieu de l'approximation | a = 2, c = -0,1 : 0,819 |
| 4 | valeur moyenne de a sin(bt) sur [p, q], 2 décimales | calcul en degrés | -3 sin(5t) sur [3, 7] : -0,02 |
| 5 | volume de révolution de y = a x^b | bornes substituées sans intégrer | a = 6, b = 1, f = 0, g = 3 |
| 6 | même question | (x^b)^2 pris pour x^(b^2) | tout tirage avec b = 2 |

- **Fréquence** : non rapportée (ni part des tirages concernés, ni nombre d'étudiants mal notés). Pour le cas 6, b = 2 est l'une des six valeurs possibles de la liste, soit environ 1 tirage sur 6 [calcul, à partir de la liste p. 49].
- **Correction** (p. 49-50) : à la génération, calcul de la clé et des erreurs types puis nouveau tirage tant qu'elles ne sont pas toutes différentes (cas 1 à 5) ; valeur 2 retirée de la liste de b (cas 6) ; pour le cas 4, q ≠ p + 1 pour séparer l'erreur « oubli de diviser par la longueur de l'intervalle » ; retour propre à l'erreur donné seulement si la réponse est fausse. Toutes les autres questions du module ont été corrigées de même.

## Avis critique

**Apport.** Met en évidence un défaut de construction propre aux questions à paramètres aléatoires avec erreurs types, invisible sans renotage, et donne une correction simple et générale.

**Points forts**
- Cas concrets et vérifiables, dont des collisions dues à l'arrondi demandé.
- Collision structurelle (cas 6) distinguée des collisions ponctuelles.
- Correction appliquée à toutes les questions du module.

**Réserves**
1. **Importante** — Aucune quantification : on ne sait pas si le problème touche 0,1 % ou 15 % des tirages, ni combien d'étudiants ont été notés justes à tort.
2. **Mineure** — Le seuil de 4 % pour retenir une erreur type n'est pas justifié.
3. **Mineure** — Revue de pratique à relecture légère ; article court, sans discussion de la littérature sur les mal-rules au-delà des définitions.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Des tirages peuvent faire coïncider clé et erreur type | B | Démonstration par exemples vérifiables (existence, pas fréquence) |
| Le nouveau tirage jusqu'à séparation règle le problème | B | Correction logiquement suffisante pour les erreurs codées |
| Le problème est fréquent | non établi | Fréquence non rapportée |

Le niveau B porte ici sur une propriété logique vérifiable, pas sur un effet d'apprentissage.

**Transférabilité** : forte. Le mécanisme est général (mécanique : angle de 45° où sin = cos, bras de levier nul, longueur unité, poutre symétrique où deux réactions sont égales).

**Pour conclure, il faudrait** mesurer dans ExoForge, par simulation sur 10 000 tirages par exercice, la part des tirages où une erreur type coïncide avec la clé à la précision demandée, avant et après filtrage.

## Pour Forge

- **ExoForge** : filtre de génération qui retire les tirages où clé et erreurs types coïncident, à la précision d'arrondi demandée (B) ; exclusion des valeurs qui annulent structurellement une erreur type (B) ; retour d'erreur type seulement sur réponse fausse (C) ; seuil de fréquence pour retenir une erreur type, à fixer sur nos données (D).
- **ExoForge, test automatique** : la simulation proposée ci-dessus peut devenir un test du dépôt pour chaque exercice ExoForge.
- Renvois : [sikurajapathi2020](sikurajapathi2020.md) (premier signalement) ; [greenhow2015](greenhow2015.md) et [gill2008](gill2008.md) (unicité des leurres sur les tirages) ; [kinnear2022](kinnear2022.md) (Q3 : détection des erreurs avec paramètres aléatoires).
