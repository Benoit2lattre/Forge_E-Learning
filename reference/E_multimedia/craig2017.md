---
cle: craig2017
reference: "Craig, S. D. et Schroeder, N. L. (2017). Reconsidering the voice effect when learning from a virtual human. Computers & Education, 114, 193-205."
doi: 10.1016/j.compedu.2017.07.003
axe: [E2]
type_etude: essai randomisé en ligne à trois conditions (140 adultes), une séance
public: adultes recrutés sur Amazon Mechanical Turk (Etats-Unis), âge médian 26-34 ans, niveau licence médian
lecture: texte complet, 08/11/2026
regles:
  - outil: CapsuleForge
    regle: "une voix de synthèse moderne (neuronale ou de qualité équivalente) est acceptable pour la narration ; ne jamais utiliser une voix de synthèse ancienne, robotique"
    niveau: C
    transferabilite: moyenne
  - outil: CapsuleForge
    regle: "faire écouter un extrait de la voix de synthèse retenue avant production et la remplacer si elle est jugée peu naturelle ou difficile à comprendre"
    niveau: C
    transferabilite: forte
    note: "les jugements de crédibilité baissent avec la voix ancienne (d = 0,43 à 0,63)"
---

# Voix de synthèse moderne contre voix humaine (Craig et Schroeder, 2017)

Craig, S. D. et Schroeder, N. L. (2017). Reconsidering the voice effect when learning from a virtual human. *Computers & Education*, 114, 193-205. [DOI](https://doi.org/10.1016/j.compedu.2017.07.003)

**En une phrase.** Dans une vidéo de 16 phrases sur la formation de l'éclair, narrée par un personnage virtuel, une voix de synthèse de 2017 fait au moins aussi bien qu'une voix humaine enregistrée (et mieux en transfert), alors qu'une voix de synthèse ancienne est jugée moins crédible : pour CapsuleForge, une voix de synthèse moderne est acceptable, une voix robotique ne l'est pas.

## La source

| | |
| --- | --- |
| **Équipe** | Ingénierie des systèmes humains, Arizona State University (Craig) ; sciences de l'éducation, Wright State University (Schroeder). Les deux auteurs travaillent de longue date sur les agents pédagogiques (nombreuses auto-citations, p. 194). |
| **Nature** | Académique ; financement non rapporté. |
| **Support** | *Computers & Education* (Elsevier). |
| **Audience** | 172 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : matériel issu de travaux publiés (texte de Moreno et Mayer, 1999 ; questions de Craig et al., 2002 ; tests de transfert de Mayer et Moreno, 1998), voix nommées (Microsoft « Mary », Neospeech « Kate ») ; données non partagées. La démarche se refait facilement ; les chiffres ne se vérifient que par les tableaux 1 à 4. |

## Ce que fait l'étude

- **Participants** (p. 197) : 140 adultes de Mechanical Turk, payés 1 dollar ; tirage au sort par Qualtrics : voix ancienne (n = 50), voix moderne (n = 50), voix humaine (n = 40). Analyse de puissance : 111 participants nécessaires pour f = 0,30.
- **Matériel** (p. 197) : vidéo à rythme imposé, personnage virtuel féminin et 14 images ; texte de 600 mots en 16 phrases ; seule la voix change. Voix humaine : étudiante à l'accent américain standard, enregistrée à vitesse proche des voix de synthèse.
- **Mesures** (p. 197-198) : prétest auto-déclaré (12 points), QCM de 6 questions, rappel libre (19 unités d'idée), 4 questions de transfert ouvertes (accord inter-juges κ = 0,68 et 0,62), effort mental (échelle de Paas, 9 points) après l'étude et après les tests, efficacité, perception de l'agent (questionnaire API, 4 sous-échelles).

## Résultats

| Mesure (tableau 1, p. 199) | Ancienne | Moderne | Humaine |
| --- | --- | --- | --- |
| QCM (proportion) | 0,63 | 0,62 | 0,61 |
| Rappel (sur 19) | 1,88 | 2,84 | 1,83 |
| Transfert (nombre de réponses acceptables) | 1,08 | 1,60 | 0,90 |

- **Apprentissage** (p. 198) : pas de différence au QCM (p = 0,94) ni au rappel (p = 0,12) ; différence en transfert, F(2, 137) = 4,02, p = 0,02, η²p = 0,06 ; voix moderne > ancienne (d = 0,41, p = 0,04) et > humaine (d = 0,54, p = 0,01) ; ancienne et humaine ne diffèrent pas.
- **Effort mental** (p. 199) : aucune différence (p = 0,89 et 0,49). Seule l'efficacité pour le transfert diffère (p = 0,04, p. 200), portée par la performance et non par l'effort (p. 201).
- **Perception** (p. 200-201) : la voix ancienne est jugée moins facilitante (d = 0,51 et 0,53) et moins crédible (d = 0,43 et 0,63) que les deux autres ; moderne et humaine ne diffèrent pas sur ces deux échelles. La voix humaine est jugée plus humaine (d = 1,09 et 0,81) et plus engageante (d = 0,74 et 0,66).

## Avis critique

**Apport.** Premier essai randomisé de taille correcte qui remet en cause l'« effet de voix » établi avec des moteurs de synthèse des années 2000 : avec une voix de synthèse de bonne qualité, l'apprentissage n'est pas moindre.

**Points forts**
- Tirage au sort, une seule variable changée, matériel standard de la littérature.
- Trois niveaux de voix, ce qui sépare « synthèse » et « qualité de la synthèse ».
- Puissance calculée a priori, vérification du son avant la vidéo (p. 198).

**Réserves**
1. **Majeure** — Pertes non expliquées : les mesures d'effort après test et de perception portent sur 99 participants (39, 36 et 24 par groupe, tableaux 3 et 4, p. 199-200), contre 140 au départ ; le groupe voix humaine perd 16 sur 40 [décompte]. L'article ne le commente pas.
2. **Importante** — Effet plancher : 1 à 3 unités d'idée sur 19 au rappel et environ 1 réponse acceptable en transfert (p. 199). La supériorité de la voix moderne repose sur un écart d'environ 0,5 à 0,7 réponse [calcul : 1,60 − 1,08 et 1,60 − 0,90], avec post-tests LSD non corrigés pour comparaisons multiples.
3. **Importante** — Public et contexte éloignés : adultes de Mechanical Turk payés 1 dollar, vidéo de quelques minutes, sans enjeu ; contenu descriptif (météorologie), sans calcul.
4. **Mineure** — Voix personnage virtuel + voix humaine : les auteurs expliquent l'avantage de la voix moderne par une dissonance (« vallée de l'étrange », p. 201), hypothèse non testée ; sans personnage, le résultat peut différer.
5. **Mineure** — Une seule voix humaine (étudiante, non professionnelle) : la qualité de l'enregistrement humain n'est pas contrôlée (voir siegle2024, qui obtient le résultat inverse avec une voix professionnelle).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Une voix de synthèse moderne n'apprend pas moins qu'une voix humaine | C | Un essai, séance unique, plancher, public éloigné ; concordant avec Mayer et DaPra (2012) cité p. 195 |
| La voix moderne fait mieux que la voix humaine en transfert | D | Écart minime, plancher, explication non testée, contredit par siegle2024 |
| Une voix ancienne nuit à la crédibilité perçue | C | Résultat net sur deux échelles, mais 29 % de pertes sur ces mesures |

**Transférabilité** : moyenne. Le mécanisme (une voix intelligible et naturelle suffit) se transpose à des capsules de cours ; les valeurs chiffrées non. Les voix neuronales actuelles sont meilleures que « Kate » (2017), ce qui joue plutôt en faveur de la règle.

**Pour conclure, il faudrait** comparer dans une capsule CapsuleForge de mécanique (sans personnage virtuel) la voix de l'enseignant et une voix neuronale, avec un test de transfert non plancher et un test différé.

## Pour Forge

- **CapsuleForge** : voix de synthèse moderne acceptable pour la narration ; proscrire les voix anciennes au timbre robotique (niveau C).
- **CapsuleForge** : prévoir une étape d'écoute et de validation de la voix avant la génération complète (niveau C).
- À lire avec siegle2024 (voix humaine professionnelle meilleure) et craig2018 (réplication, à lire).
