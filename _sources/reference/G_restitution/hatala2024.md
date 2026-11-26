---
cle: hatala2024
reference: "Hatala, M. et Nazeri, S. (2024). Associations between students' standing seen in learning analytics dashboards and their following learning behaviours: A study of three reference frames. Journal of Learning Analytics, 11(3), 41-61."
doi: 10.18608/jla.2024.8547
axe: [G1, G2]
type_etude: étude de traces ; type de tableau de bord tiré au sort (moyenne de classe, classement des 5 premiers, qualité des messages), état affiché non tiré au sort ; 896 étudiants, 21 forums de discussion notés, 11 cours
public: étudiants de 2e et 3e année d'une université canadienne (informatique, interaction humain-machine, médias, psychologie de l'éducation), cours hybrides
lecture: "texte complet, 09/11/2026"
regles:
  - outil: DiagForge
    regle: "quand le rapport montre un étudiant au-dessus de la référence, lui proposer un objectif suivant (notion suivante, exercice plus exigeant) plutôt qu'un simple constat : se voir au-dessus est suivi de moins d'activité"
    niveau: C
    transferabilite: moyenne
  - outil: DiagForge
    regle: "journaliser chaque consultation du rapport avec l'état affiché (position, notions signalées), pour relier ce que l'étudiant a vu à ce qu'il fait ensuite"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "n'afficher que des indicateurs directement actionnables : l'étudiant doit voir quelle action change sa situation (notions à revoir, exercices à refaire)"
    niveau: D
    transferabilite: forte
    note: "condition posée par les auteurs pour que leurs résultats s'appliquent ; non testée"
---

# Ce que l'étudiant fait après avoir vu sa position (Hatala et Nazeri, 2024)

Hatala, M. et Nazeri, S. (2024). Associations between students' standing seen in learning analytics dashboards and their following learning behaviours: A study of three reference frames. *Journal of Learning Analytics*, 11(3), 41-61. [DOI](https://doi.org/10.18608/jla.2024.8547)

**En une phrase.** Dans des forums de discussion notés, 567 étudiants consultent l'un des trois tableaux de bord tirés au sort ; quand l'écran les montre sans message ou sous la moyenne de la classe, ils publient plus souvent à la séance suivante, et quand il les montre au-dessus, ils publient moins mais reviennent surveiller leur position : la position affichée oriente l'action qui suit, ce qui est une association et non un effet démontré.

## La source

| | |
| --- | --- |
| **Équipe** | École des arts et technologies interactives, université Simon Fraser (Colombie-Britannique) ; même groupe que [zheng2026](zheng2026.md) ; les données viennent d'une étude antérieure du premier auteur sur la personnalisation des tableaux de bord selon les buts d'accomplissement (p. 45). |
| **Nature** | Académique ; financement des conseils de recherche canadiens CRSNG et CRSH ; aucun conflit déclaré (p. 57-58). Les auteurs ont conçu les tableaux de bord. |
| **Support** | *Journal of Learning Analytics* (SoLAR), libre accès. |
| **Audience** | 4 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Moyenne : codage des états et des séances détaillé (tableau 1, p. 47-48), tableaux complets ; données de traces non publiées. La démarche se refait sur des journaux Moodle ; les chiffres ne se vérifient pas. |

## Ce que fait l'étude

- **Activité** (p. 45) : discussion en petits groupes de 6 à 12 pendant 10 à 14 jours pour rédiger une réponse commune ; 4 messages minimum pour la note complète ; 5 % de la note du cours.
- **Trois tableaux de bord** (p. 45-46, figure 1), tirés au sort par étudiant pour la première discussion (p. 47) : nombre de messages de l'étudiant contre la moyenne de la classe ; liste nominative des 5 étudiants ayant le plus publié ; couverture des thèmes clés par les messages de l'étudiant contre celle de la classe (analyse sémantique). Chaque tableau ne montre qu'un indicateur.
- **Données** (p. 47, 50) : 1 119 affectations, 896 participants, 28 290 actions (19 749 lectures, 4 484 messages, 4 057 consultations du tableau de bord) ; 567 consultent au moins une fois, 329 jamais.
- **Analyse** (p. 48-50) : découpage en séances (30 min sans action) ; pour chaque séance où l'étudiant consulte le tableau, état affiché (aucun message, sous, à, au-dessus de la référence) et action de la séance suivante ; probabilité de publier et Q de Yule (−1 à +1, 0 = pas de lien) par étudiant et par état ; modèles mixtes.

## Résultats

- **Consultants contre non-consultants** (p. 50) : 34,6 séances contre 18,2 ; 4,4 messages contre 3,5 ; messages 15 % plus longs (p. 51). Les auteurs rappellent que cette comparaison confond le tableau de bord et la motivation (note 5, p. 49).
- **Entre types de tableau de bord** (p. 50-51) : pas de différence de séances, de messages ou de longueur.
- **Moyenne de classe, par état** (tableau 6, p. 52) :

| État affiché | Probabilité de publier ensuite (cote moyenne) | Q de Yule moyen (n) |
| --- | --- | --- |
| Aucun message | 0,47 | +0,13 (30) |
| Sous la moyenne | 0,65 | +0,65 (15) |
| À la moyenne | 0,47 | +0,05 (13) |
| Au-dessus | 0,24 | −0,45 (36) |

  L'écart entre états est significatif (F(3, 94) = 10,49, p < 0,001) ; « au-dessus » est moins souvent suivi d'une publication que « sous » ou « aucun message » (p. 52).
- **Classement des 5 premiers** (tableau 10, p. 55) : être à plus d'un message du classement est suivi de publications (Q = +0,66) ; être à un seul message (Q = −0,77) ou dans le classement (Q = −0,60) ne l'est pas ; les étudiants du classement reviennent le consulter dans 69 % des séances suivantes (p. 54).
- **Qualité des messages** (tableau 8, p. 54) : seul l'état « aucun thème couvert » est suivi de publications (Q = +0,33).
- **Lecture des auteurs** (p. 56-57) : leurs résultats ne valent que pour des indicateurs directement liés à une action (publier un message, couvrir un thème) ; ils appellent à personnaliser l'affichage selon la position de l'étudiant.

## Avis critique

**Apport.** Première étude qui relie, étudiant par étudiant, l'état exact affiché par le tableau de bord à l'action qui suit, dans un vrai cours. Elle donne un mécanisme concret à la règle « la moyenne sert d'ancre » ([zheng2026](zheng2026.md)) : sous la référence on agit, au-dessus on s'arrête et on surveille.

**Points forts**
- Grand nombre de traces, dans 11 cours, avec reconstitution de l'écran vu.
- Trois cadres de référence comparés dans la même activité.
- Analyse jusqu'au 4e message pour séparer l'effet de l'exigence minimale (p. 50).

**Réserves**
1. **Majeure** — L'état affiché n'est pas tiré au sort : il dépend de ce que l'étudiant a déjà fait. Un étudiant au-dessus de la moyenne a souvent atteint les 4 messages exigés ; un étudiant en dessous doit encore publier. L'analyse limitée aux séances avant le 4e message réduit ce biais sans l'éliminer. Il n'y a pas de groupe sans tableau de bord.
2. **Importante** — Les Q de Yule par état reposent sur de petits effectifs (13 à 36 étudiants pour la moyenne de classe) et sur des cotes très dispersées (écarts-types 0,4 à 0,8, tableau 6).
3. **Mineure** — La mesure est la participation (publier), pas l'apprentissage ; une perte d'enregistrement a réduit le groupe « moyenne de classe » à 112 étudiants (note 6, p. 50) ; plan croisé pour les discussions suivantes, non analysé.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Se voir sous la référence est suivi de plus de participation, au-dessus de moins | C | Association dans de nombreuses traces ; état non tiré au sort, confondu avec le travail déjà fait |
| Être juste derrière un classement ne pousse pas à agir | C | Petits effectifs par état |
| Ces résultats valent pour des indicateurs directement actionnables | D | Condition posée par les auteurs, non testée |

**Transférabilité** : moyenne. Étudiants de 2e et 3e année, mais forums notés et indicateur de participation ; pour un quiz de diagnostic, le mécanisme « au-dessus = arrêt » est plausible, la valeur chiffrée non.

**Pour conclure, il faudrait** tirer au sort, pour les étudiants au-dessus du critère dans DiagForge, un rapport « vous maîtrisez » contre « vous maîtrisez ; prochain objectif : … », et comparer l'activité sur les exercices proposés dans la semaine suivante.

## Pour Forge

- **DiagForge** : au-dessus de la référence, proposer un objectif suivant (niveau C).
- **DiagForge** : journaliser l'état affiché à chaque consultation (niveau C) ; cela **précise** la règle existante « journaliser l'ouverture du rapport » ([kaliisa2024](kaliisa2024.md)).
- **DiagForge** : des indicateurs actionnables (notions, exercices), pas des compteurs d'activité (niveau D) ; voir [matcha2020](matcha2020.md).
- **Confirme** et étend [zheng2026](zheng2026.md) (la moyenne de classe sert d'ancre) ; le classement nominatif ne doit pas figurer dans DiagForge (cohérent avec la règle « pas de rang »).
