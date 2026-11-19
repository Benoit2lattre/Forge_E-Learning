---
cle: kalyuga2001
reference: "Kalyuga, S., Chandler, P., Tuovinen, J. et Sweller, J. (2001). When problem solving is superior to studying worked examples. Journal of Educational Psychology, 93(3), 579-588."
doi: 10.1037/0022-0663.93.3.579
axe: [D2, D1]
type_etude: deux expériences randomisées répétées sur trois semaines, mêmes participants
public: 24 apprentis de l'industrie (Australie), programmation d'automates
lecture: texte complet (PDF scanné, lu en image), 08/11/2026
regles:
  - outil: ExoForge
    regle: "réduire la part d'exemples résolus quand l'étudiant devient plus avancé ; pour un contenu déjà connu, préférer les exercices"
    niveau: C
    transferabilite: forte
---

# Quand les exercices valent mieux que les exemples (Kalyuga et al., 2001)

Kalyuga, S., Chandler, P., Tuovinen, J. et Sweller, J. (2001). When problem solving is superior to studying worked examples. *Journal of Educational Psychology*, 93(3), 579-588. [DOI](https://doi.org/10.1037/0022-0663.93.3.579)

**En une phrase.** Chez des apprentis qui apprennent à programmer des automates, les exemples résolus aident au début ; leur avantage disparaît avec l'entraînement, et sur un contenu déjà mieux maîtrisé les exercices finissent par faire mieux.

## La source

| | |
| --- | --- |
| **Équipe** | Université de Nouvelle-Galles du Sud (Sydney), équipe de John Sweller, à l'origine de la théorie de la charge cognitive ; Monash University. |
| **Nature** | Académique et industrielle : financement de l'Australian Research Council, avec deux entreprises partenaires (Email Ltd et BHP) qui ont fourni les apprentis (p. 579). |
| **Support** | *Journal of Educational Psychology* (APA). |
| **Audience** | 584 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Faible à moyenne : procédure et séquence décrites (Fig. 1, p. 582), logiciel maison (Authorware) et données non publiés. |

## Ce que fait l'étude

- **Participants** : 24 apprentis de deux entreprises australiennes, en première année de formation, sans connaissance préalable de la programmation d'automates (p. 581).
- **Expérience 1** (programmes d'automates pour circuits à relais) : 12 apprentis par groupe. Groupe « exercices » : il programme chaque circuit, avec trois essais, la solution s'affiche après trois échecs. Groupe « exemples » : un exemple résolu puis un exercice, en alternance. Trois étapes à une semaine d'intervalle, avec des séances d'entraînement communes entre les étapes ; test de 12 questions à chaque étape (p. 581-583).
- **Expérience 2** (équations booléennes des mêmes circuits) : mêmes apprentis, de nouveau tirés au sort, deux étapes (p. 585-586).
- **Mesures** : score au test sur 12, nombre d'essais ratés, temps, difficulté perçue (échelle de 1 à 9), efficacité (score et difficulté combinés).

## Résultats

| Expérience 1 (tableau 1, p. 583) | Étape 1 | Étape 2 | Étape 3 |
| --- | --- | --- | --- |
| Exemples, score sur 12 | 5,9 | 7,3 | 6,3 |
| Exercices, score sur 12 | 3,8 | 3,7 | 5,4 |

- **Expérience 1** (p. 583-584) : interaction groupe × étape significative sur le score ; avantage des exemples significatif à l'étape 2 seulement (pas à l'étape 1, F = 2,41) ; aucune différence à l'étape 3. Le groupe « exemples » étudie moins longtemps.

| Expérience 2 (tableau 2, p. 586) | Étape 1 | Étape 2 |
| --- | --- | --- |
| Exemples, score sur 12 | 9,4 | 8,2 |
| Exercices, score sur 12 | 10,2 | 10,6 |

- **Expérience 2** (p. 586-587) : interaction significative ; à l'étape 2, le groupe « exercices » fait mieux (p < 0,05) et avec moins d'essais ratés.

## Avis critique

**Apport.** L'étude qui a montré l'inversion d'expertise pour les exemples résolus : un même support aide le débutant et devient inutile, puis gênant, quand l'apprenant progresse. C'est l'argument central pour adapter la part d'exemples au niveau de l'étudiant.

**Points forts**
- Suivi des mêmes apprentis pendant plusieurs semaines, dans leur centre de formation.
- Contenu technique proche de l'ingénierie (automates, logique booléenne).
- Le groupe « exercices » reçoit la solution après trois échecs : le témoin n'est pas une résolution sans aide.

**Réserves**
1. **Importante** — 12 apprentis par groupe : effectifs très faibles, et la plupart des effets simples sont à la limite de la significativité.
2. **Importante** — Dans l'expérience 1, l'inversion n'est pas obtenue : l'avantage des exemples disparaît sans s'inverser (les auteurs le reconnaissent, p. 584). L'inversion ne vient que de l'expérience 2, sur un contenu plus facile.
3. **Importante** — Les mêmes participants servent aux deux expériences ; l'expertise est construite par les séances d'entraînement entre étapes, pas mesurée par un test indépendant.
4. **Mineure** — Le groupe « exercices » passe plus de temps à étudier ; les auteurs discutent ce point (p. 587).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les exemples résolus aident les débutants plus que les exercices | C | Significatif à une étape sur trois, 12 par groupe |
| Pour des apprenants plus avancés, les exercices font mieux | C | Une expérience, 12 par groupe, mêmes participants |

**Transférabilité** : forte pour le mécanisme (contenu technique, adultes en formation) ; faible pour les valeurs, compte tenu des effectifs.

**Pour conclure, il faudrait** un essai plus grand où le niveau est mesuré avant chaque séance : voir Kalyuga et Sweller (2004) pour le test rapide « quelle est l'étape suivante ? » (fiche à écrire) et Salden et al. (2010) pour l'adaptation.

## Pour Forge

- **ExoForge** : diminuer la part d'exemples résolus quand l'étudiant progresse, et proposer directement des exercices sur un contenu déjà connu (niveau C). En L3–M2, une partie des étudiants maîtrise déjà certaines étapes : un exemple complet systématique peut leur coûter du temps sans bénéfice.
