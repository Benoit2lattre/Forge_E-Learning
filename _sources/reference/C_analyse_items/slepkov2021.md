---
cle: slepkov2021
reference: "Slepkov, A. D., Van Bussel, M. L., Fitze, K. M. et Burr, W. S. (2021). A baseline for multiple-choice testing in the university classroom. SAGE Open, 11(2), 1-12."
doi: 10.1177/21582440211016838
axe: [C1]
type_etude: étude descriptive de 182 tests QCM réels (11 246 items, 24 885 copies)
public: examens de premier cycle d'une université canadienne (Trent), 12 disciplines, 45 enseignants
lecture: texte complet, 08/11/2026
regles:
  - outil: DiagForge
    regle: "mesurer la discrimination par la corrélation entre l'item et le score du reste du test (item exclu), pas par la point-bisériale classique"
    niveau: B
    transferabilite: forte
  - outil: DiagForge
    regle: "lire la discrimination item exclu ainsi : négative = à revoir (clé fausse, énoncé ambigu) ; 0 à 0,15 = faible ; 0,15 à 0,35 = correcte ; au-dessus de 0,35 = très bonne"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "signaler une difficulté hors de la plage utile : réussite entre environ 0,30-0,43 (selon 5 ou 3 options) et 0,90"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "comparer la fiabilité de tests de longueurs différentes avec l'alpha ramené à 50 items (Spearman-Brown) ou avec la discrimination moyenne item exclu"
    niveau: C
    transferabilite: forte
---

# Valeurs de référence pour les QCM d'examen à l'université (Slepkov et al., 2021)

Slepkov, A. D., Van Bussel, M. L., Fitze, K. M. et Burr, W. S. (2021). A baseline for multiple-choice testing in the university classroom. *SAGE Open*, 11(2), 1-12. [DOI](https://doi.org/10.1177/21582440211016838)

**En une phrase.** Sur 182 QCM d'examen écrits par des enseignants d'université, la réussite moyenne par question est de 0,64, un quart des questions discriminent très bien et 8 % ont une discrimination négative ; les auteurs proposent de mesurer la discrimination « item exclu » et donnent des seuils et une fiabilité ramenée à 50 items tirés de ces tests réels.

## La source

| | |
| --- | --- |
| **Équipe** | Département de physique et d'astronomie, université Trent (Ontario) ; outils d'analyse publiés par les auteurs (paquet R et application). |
| **Nature** | Académique ; soutien partiel du centre pédagogique de l'université (p. 11). |
| **Support** | *SAGE Open*, libre accès. |
| **Audience** | 28 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Bonne pour les méthodes (formules, scripts R publiés) ; données des tests non publiques. |

## Ce que fait l'étude

- **Corpus** (p. 2, tableau 1 p. 4) : tous les QCM fournis par 45 enseignants de 2013 à 2019, sans sélection sur la qualité ; 17 à 106 items par test, 11 à 901 étudiants.
- **Indicateurs** (p. 3-4) : réussite par question ; discrimination par point-bisériale et par corrélation item exclu (r′) ; alpha de Cronbach ramené à 50 items par la formule de Spearman-Brown.
- **Recommandations** (p. 9-10) : seuils tirés de la distribution observée.

## Résultats

- **Pourquoi l'item exclu** (p. 3) : la point-bisériale contient l'item dans le total ; sur un test de 20 questions répondues au hasard, elle dépasserait le seuil usuel de 0,20 alors que rien n'est mesuré. L'écart moyen avec r′ est de 0,06 (p. 10).
- **Difficulté** (p. 6, 8-9) : réussite moyenne 0,64 ; près de 15 % des questions réussies par plus de 90 % ; les questions de réussite 0,4 à 0,9 discriminent à peu près autant ; la discrimination s'effondre sous 0,3.
- **Discrimination** (tableau 1) : r′ moyen 0,24 ; 8 % négatives, 20 % faibles (0 à 0,15), 45 % correctes (0,15 à 0,35), 25 % très bonnes (> 0,35).
- **Fiabilité** (p. 8-10) : alpha ramené à 50 items 0,77 en moyenne (0,20 à 0,92) ; 22 % des tests sous 0,7 ; au-dessus de 0,8, un test convient à une note sommative. r′ moyen du test suit étroitement l'alpha ramené à 50 items.
- **Pratiques** (p. 5-6, 10) : 3 options dans moins de 10 % des questions malgré les recommandations ; questions faciles en début de test, sans effet mesurable sur la qualité.

## Avis critique

**Apport.** Donne des seuils réalistes pour des tests d'enseignants, et non pour des examens standardisés, avec un indicateur de discrimination correct pour les tests courts : c'est le cadre de référence de DiagForge.

**Points forts**
- Très grand corpus réel, sans sélection.
- Choix d'indicateurs justifié, outils publiés.
- Seuils reliés à une distribution observée.

**Réserves**
1. **Importante** — Une seule université, surtout des examens sur feuilles optiques ; seuils descriptifs (« où se situent les tests »), pas validés contre un critère externe.
2. **Mineure** — Tests de 17 à 106 items, plus longs que la plupart des quiz Moodle ; avec 10 à 20 questions tirées, r′ est plus instable.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| La discrimination item exclu est préférable pour les tests courts | B | Argument mathématique et données concordantes |
| Seuils r′ (0 ; 0,15 ; 0,35) et plage de difficulté | C | Description d'un grand corpus, pas de validation externe |

**Transférabilité** : forte. Tests d'enseignants à l'université, toutes disciplines dont les sciences.

**Pour conclure, il faudrait** calculer ces indicateurs sur une année de quiz Moodle de mécanique et comparer leur distribution à celle de Slepkov et al.

## Pour Forge

- **DiagForge** : garder la corrélation item-reste (déjà utilisée) ; aligner les seuils sur r′ < 0 (à revoir), < 0,15 (faible), > 0,35 (très bonne) (niveau C).
- **DiagForge** : plage de difficulté utile selon le nombre d'options : 0,43-0,90 (3 options), 0,35-0,90 (4), 0,30-0,90 (5) (niveau C).
- **DiagForge** : afficher l'alpha ramené à 50 items à côté de l'alpha brut (niveau C).
