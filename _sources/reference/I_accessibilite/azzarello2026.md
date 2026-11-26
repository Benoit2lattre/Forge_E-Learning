---
cle: azzarello2026
reference: "Azzarello, C., Paek, S., Hodge, C., Jameson, M. et Lewis, J. (2026). Does font improve reading in dyslexic children?: meta-analysis of dyslexia-friendly fonts and dyslexic children's reading performance. Annals of Dyslexia."
doi: 10.1007/s11881-026-00389-8
axe: [I1]
type_etude: méta-analyse (15 études, 91 tailles d'effet, N = 688)
public: élèves dyslexiques de 8 à 15 ans pour l'essentiel (moyenne 11,4 ans), une étude avec des participants plus âgés
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "ne pas proposer de police « dyslexie » (OpenDyslexic, Dyslexie) comme aménagement ; garder une police standard"
    niveau: B
    transferabilite: moyenne
    note: "études sur enfants et sur papier ; s'applique aussi aux pages HTML de QuizForge"
  - outil: QuizForge
    regle: "ne pas proposer de police « dyslexie » (OpenDyslexic, Dyslexie) comme aménagement ; garder une police standard"
    niveau: B
    transferabilite: moyenne
  - outil: ExoForge
    regle: "si une police de confort est proposée, la laisser au choix de l'étudiant (préférence), sans la présenter comme une aide à la lecture"
    niveau: C
    transferabilite: moyenne
---

# Polices « dyslexie » et lecture (Azzarello et al., 2026)

Azzarello, C., Paek, S., Hodge, C., Jameson, M. et Lewis, J. (2026). Does font improve reading in dyslexic children?: meta-analysis of dyslexia-friendly fonts and dyslexic children's reading performance. *Annals of Dyslexia*. [DOI](https://doi.org/10.1007/s11881-026-00389-8)

**En une phrase.** Sur 15 études, les polices conçues pour les dyslexiques (OpenDyslexic, Dyslexie) ne font lire ni plus vite ni plus juste qu'Arial ou Times New Roman (g = −0,04) ; pour Forge, inutile de proposer ces polices comme aménagement : ce sont la taille et l'espacement qui comptent (voir [rello2016](rello2016.md)).

## La source

| | |
| --- | --- |
| **Équipe** | Université du Northern Colorado (États-Unis) et université de Strathclyde (Royaume-Uni), p. 23 ; psychologie et méthodes quantitatives. |
| **Nature** | Académique ; aucun financement spécifique ; pas de conflit d'intérêts déclaré (p. 20). |
| **Support** | *Annals of Dyslexia* (Springer), revue à comité de lecture. |
| **Audience** | 0 citation (OpenAlex, 08/11/2026) : article de l'année. |
| **Reproductibilité** | Moyenne : équation de recherche, critères et tableau des études publiés (p. 6-12) ; données sur demande seulement (p. 20) ; analyses sous SPSS. La démarche se refait ; les chiffres ne se vérifient pas sans les données codées. |

## Ce que fait l'étude

- **Recherche** (p. 6) : PsycINFO, ProQuest Dissertations, Web of Science jusqu'en avril 2026 ; 89 publications, 15 études retenues (11 articles, 1 mémoire, 3 thèses).
- **Critères** (p. 6-7) : plan expérimental ou quasi expérimental comparant une police « dyslexie » à une police standard ; mesure objective (vitesse ou exactitude de lecture) ; élèves dyslexiques lisant dans leur langue ; articles en anglais.
- **Analyse** (p. 9-10) : g de Hedges, effets aléatoires (DerSimonian-Laird), modérateurs (diagnostic, langue, âge, police comparée, police « dyslexie », type de mesure), biais de publication (entonnoir, Egger, trim and fill).

## Résultats

- **Effet global** (p. 13) : g = −0,04, IC 95 % [−0,15 ; 0,07], p = 0,50.
- **Hétérogénéité** (p. 14) : Q(81) = 269,8, I² = 73,3 % ; intervalle de prédiction −0,87 à 0,79.
- **Modérateurs** (tableau 2, p. 13) : aucun significatif. Vitesse g = 0,00 ; exactitude g = −0,08 ; Dyslexie g = −0,10 ; OpenDyslexic g = 0,07. Seul sous-groupe dont l'intervalle exclut zéro : échantillons d'âges mélangés (14 effets, g = 0,21, p = 0,01).
- **Biais de publication** (p. 15-16) : Egger non significatif (p = 0,67) ; le trim and fill ajoute 33 effets et fait passer l'effet à g = −0,20 (p < 0,001), donc plutôt en défaveur des polices « dyslexie ».
- **Poids** (tableau 1, p. 10-12) : Kuster et al. (2017) fournit 272 participants sur 688, soit 40 % [calcul], et 30 tailles d'effet, avec un effet nul.

## Avis critique

**Apport.** Synthèse récente et directe d'une question que se pose tout concepteur de page : faut-il proposer une police « dyslexie » ? La réponse est non, en lecture objective.

**Points forts**
- Critères explicites, mesures objectives seulement, littérature grise incluse.
- Plusieurs tests de biais de publication, qui vont tous contre un bénéfice caché.
- Intervalle de prédiction rapporté.

**Réserves**
1. **Importante** — Public d'enfants de 8 à 15 ans, sur papier pour l'essentiel (p. 19) ; une seule étude avec des participants plus âgés (p. 7). Le résultat se transpose au principe, pas directement à la lecture de formules à l'écran par des L3-M2.
2. **Importante** — Effets multiples par étude analysés comme indépendants, sans modèle multiniveau (p. 19) : erreurs-types probablement sous-estimées, ce qui ne change pas la conclusion nulle.
3. **Mineure** — Incohérences de comptage : 91 effets annoncés, Q à 81 degrés de liberté, 76 + 14 = 90 effets dans le tableau 2, trim and fill « de 81 à 115 » pour 33 effets ajoutés ; intervalle de Dyslexie différent entre le tableau 2 et le texte (p. 13-14). Le sous-groupe « âges mélangés » est significatif alors que le texte dit qu'aucun modérateur ne l'est.
4. **Mineure** — Pas de mesure de compréhension retenue : vitesse et exactitude seulement.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les polices « dyslexie » n'améliorent pas la vitesse ni l'exactitude de lecture des enfants dyslexiques | B | Méta-analyse, effet nul et biais de publication qui va dans le même sens ; abaissé de A pour dépendance des effets et poids d'une étude |
| Même conclusion pour des étudiants à l'écran | C | Extrapolation hors du public et du support étudiés |
| Le bénéfice ressenti (confort) existe sans gain mesuré | C | Rapporté dans la discussion à partir d'autres études, non analysé ici |

**Transférabilité** : moyenne. Mécanisme (la dyslexie n'est pas d'abord visuelle) transposable ; public et support éloignés.

**Pour conclure, il faudrait** proposer dans ExoForge un réglage de police (standard ou OpenDyslexic) et comparer temps de lecture de l'énoncé et réussite chez les étudiants qui déclarent une dyslexie.

## Pour Forge

- **ExoForge, QuizForge** : pas de police « dyslexie » présentée comme aide ; police standard sans empattement, taille et espacement réglables (niveau B ; voir [rello2016](rello2016.md)).
- **ExoForge** : un réglage de police peut exister comme confort, au choix de l'étudiant, sans promesse d'efficacité (niveau C).
- Renvois : `kuster2017`, `marinus2016` (priorité 2, non lus), déjà dans le tableau de l'axe.
