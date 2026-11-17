---
cle: siegle2024
reference: "Siegle, R. F. et Craig, S. D. (2024). The voice quality of pedagogical agent impacts learning and agent perceptions. Journal of Computer Assisted Learning, 40(5), 2278-2291."
doi: 10.1111/jcal.13027
axe: [E2]
type_etude: essai randomisé en ligne, plan factoriel 2 x 2 (type de voix x accent), 81 adultes analysés sur 197, une séance
public: adultes recrutés sur Amazon Mechanical Turk (Etats-Unis), âge moyen 37 ans, majoritairement diplômés de licence
lecture: texte complet, 08/11/2026
regles:
  - outil: CapsuleForge
    regle: "pour les capsules durables et les passages clés, préférer une voix humaine enregistrée avec soin (diction, prise de son) à une voix de synthèse"
    niveau: C
    transferabilite: moyenne
  - outil: CapsuleForge
    regle: "réserver la voix de synthèse aux contenus souvent modifiés ou produits sans budget d'enregistrement, et choisir le moteur le plus naturel disponible"
    niveau: D
    transferabilite: moyenne
    note: "règle proposée par les auteurs (p. 2288), non testée"
  - outil: CapsuleForge
    regle: "un accent non natif clair et bien articulé n'est pas un motif d'écarter une voix"
    niveau: D
    transferabilite: moyenne
    note: "absence d'effet sur 81 participants ; absence de preuve, pas preuve d'absence"
---

# Voix professionnelle contre voix de synthèse (Siegle et Craig, 2024)

Siegle, R. F. et Craig, S. D. (2024). The voice quality of pedagogical agent impacts learning and agent perceptions. *Journal of Computer Assisted Learning*, 40(5), 2278-2291. [DOI](https://doi.org/10.1111/jcal.13027)

**En une phrase.** Avec une vidéo de deux minutes narrée par un personnage virtuel, une voix humaine de comédienne professionnelle fait mieux retenir et transférer qu'une voix de synthèse Neospeech (moteur de 2017), l'accent russe ou américain ne changeant rien ; pour CapsuleForge, c'est un argument pour enregistrer soi-même avec soin les passages importants, à prendre avec prudence vu les pertes d'effectif et les incohérences de l'article.

## La source

| | |
| --- | --- |
| **Équipe** | Ingénierie des systèmes humains, Arizona State University ; Craig est aussi l'auteur de craig2017, dont cette étude prolonge le protocole. |
| **Nature** | Académique ; financement non rapporté. Les auteurs testent les limites de leur propre résultat de 2017. |
| **Support** | *Journal of Computer Assisted Learning* (Wiley). |
| **Audience** | 14 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : matériel standard (vidéo de Mayer et Moreno, 1998), barème détaillé avec accords inter-juges (p. 2282-2283), prétest en annexe ; voix humaines achetées sur Voices.com, non publiées ; données « sur demande » (p. 2288). La démarche se refait ; les chiffres ne se vérifient pas tous (voir réserves). |

## Ce que fait l'étude

- **Plan** (p. 2281) : 2 types de voix (humaine professionnelle ou synthèse Neospeech) x 2 accents (américain du Midwest ou russe) ; personnage virtuel féminin identique dans toutes les conditions ; tirage au sort par Qualtrics.
- **Participants** (p. 2281) : 197 inscrits sur Mechanical Turk (3 dollars) ; 66 retirés pour abandon, 50 pour réponses copiées à l'identique (suspicion de recherche en ligne) ; 81 analysés (22, 22, 19 et 18 par groupe, tableau 1, p. 2282).
- **Mesures** (p. 2282-2283) : prétest de 8 QCM ; rappel libre (8 idées, 4 min) ; 4 questions de transfert (8 points, 2 min chacune) ; perception du locuteur (15 items), questionnaire API-R, 4 questions sur l'apparence et la voix.

## Résultats

| Mesure (tableaux 2 et 3, p. 2284) | Synthèse (n = 44) | Humaine (n = 37) |
| --- | --- | --- |
| Rappel (sur 8) | 2,20 (ET 1,95) | 3,92 (ET 2,24) |
| Transfert (sur 8) | 1,50 (ET 1,23) | 2,59 (ET 1,72) |

- **Type de voix** (p. 2284) : effet sur le rappel, F(1, 77) = 13,49, p < 0,01, η²p = 0,15, soit d ≈ 0,8 [calcul : (3,92 − 2,20) / 2,09] ; effet sur le transfert (η²p = 0,12 ou 0,15, voir réserve 2), soit d ≈ 0,7 [calcul : (2,59 − 1,50) / 1,47].
- **Accent** (p. 2284) : aucun effet sur le rappel (p = 0,39), le transfert (p = 0,97) ni l'interaction.
- **Perceptions** (p. 2284-2287) : la voix humaine est mieux notée sur toutes les échelles ; « voix naturelle » 3,89 contre 2,77 sur 5, « facile à comprendre » 4,16 contre 3,43 (tableau 6, p. 2287).
- **Interprétation des auteurs** (p. 2287-2288) : « effet de qualité de voix » ; une voix moderne égale une voix humaine ordinaire (craig2017), pas une voix professionnelle.

## Avis critique

**Apport.** Nuance utile à craig2017 : ce n'est pas « humaine contre synthèse » qui compte, mais la qualité de la voix ; une voix humaine soignée garde un avantage net sur la synthèse de l'époque.

**Points forts**
- Tirage au sort, plan factoriel, seule la voix change.
- Barème de correction précis, accords inter-juges élevés (κ de 0,77 à 1,00).
- Contrôle de l'écoute (code audio) et item de vigilance.

**Réserves**
1. **Majeure** — Pertes massives : 81 analysés sur 197 (59 % retirés) [calcul : 116 / 197], dont 50 pour plagiat détecté a posteriori ; la répartition des retraits par condition n'est pas rapportée. Si les retraits diffèrent selon la voix, le tirage au sort ne protège plus la comparaison.
2. **Importante** — Incohérences de rapport : deux F différents pour le même effet du type de voix en transfert (10,94 puis 13,49, p. 2284) ; les quatre sous-échelles de l'API-R et l'échelle « supériorité » portent exactement les mêmes statistiques (F = 12,59 ; accent p = 0,16 ; interaction p = 0,49, p. 2284-2285) alors que leurs moyennes diffèrent (tableau 5). Ces chiffres ne sont pas fiables tels qu'imprimés ; les moyennes des tableaux le sont davantage.
3. **Importante** — La voix de synthèse est le moteur Neospeech déjà utilisé en 2017 (p. 2282) : en 2024, ce n'est plus l'état de l'art (voix neuronales). Le résultat compare donc une voix professionnelle à une synthèse datée.
4. **Importante** — Public éloigné (adultes Mechanical Turk payés 3 dollars), vidéo de deux minutes, contenu descriptif, scores bas (2 à 4 sur 8).
5. **Mineure** — Deux comédiennes différentes pour les deux accents humains : voix et accent sont confondus dans la condition humaine.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Une voix humaine professionnelle fait mieux apprendre qu'une voix de synthèse de 2017 | C | Effet net (d ≈ 0,7-0,8) mais un seul essai, 59 % de pertes, incohérences de rapport |
| La qualité de la voix, plus que sa nature, explique les résultats contraires | D | Synthèse des auteurs entre leurs études, non testée dans un même essai |
| L'accent n'a pas d'effet | D | Absence d'effet sur environ 20 participants par groupe |

**Transférabilité** : moyenne. Le mécanisme (une voix peu naturelle coûte à l'apprentissage) est plausible pour nos capsules ; la comparaison avec les voix neuronales actuelles reste à faire.

**Pour conclure, il faudrait** comparer, dans une capsule de mécanique, la voix enregistrée de l'enseignant et une voix neuronale récente, sans personnage virtuel, avec un test différé et un effectif suffisant après exclusions.

## Pour Forge

- **CapsuleForge** : voix humaine soignée pour les capsules durables et les passages clés (niveau C).
- **CapsuleForge** : synthèse de la meilleure qualité disponible pour les contenus révisés souvent (niveau D).
- **CapsuleForge** : un accent clair ne pose pas de problème (niveau D).
- À lire avec craig2017 (synthèse moderne ≈ voix humaine ordinaire) : les deux études ensemble suggèrent que CapsuleForge doit garantir une voix naturelle, quelle que soit sa source.
