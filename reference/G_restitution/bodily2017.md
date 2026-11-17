---
cle: bodily2017
reference: "Bodily, R. et Verbert, K. (2017). Review of research on student-facing learning analytics dashboards and educational recommender systems. IEEE Transactions on Learning Technologies, 10(4), 405-418."
doi: 10.1109/tlt.2017.2740172
axe: [G2]
type_etude: revue systématique descriptive (93 articles de 2005 à juin 2016), codage binaire des fonctions, sources de données, démarche de conception et effets mesurés ; sans méta-analyse
public: systèmes de restitution aux étudiants (tableaux de bord, systèmes de recommandation, messages automatiques), surtout dans le supérieur
lecture: "texte complet, 09/11/2026"
regles:
  - outil: DiagForge
    regle: "chaque rapport réunit ce qui s'est passé (résultats par notion) et quoi faire (recommandation précise) ; ne pas livrer l'un sans l'autre"
    niveau: D
    transferabilite: forte
    note: "17 % seulement des systèmes recensés font les deux"
  - outil: DiagForge
    regle: "envoyer le rapport à l'étudiant (message Moodle ou courriel) plutôt que d'attendre qu'il aille le consulter"
    niveau: D
    transferabilite: forte
    note: "usage spontané faible (environ 30 % des étudiants en moyenne) ; les systèmes avec notification sont décrits comme plus utilisés, sans chiffre"
---

# Revue des systèmes de restitution aux étudiants (Bodily et Verbert, 2017)

Bodily, R. et Verbert, K. (2017). Review of research on student-facing learning analytics dashboards and educational recommender systems. *IEEE Transactions on Learning Technologies*, 10(4), 405-418. [DOI](https://doi.org/10.1109/tlt.2017.2740172)

**En une phrase.** Sur 93 articles décrivant un système qui renvoie aux étudiants des données sur leur activité, 15 % seulement mesurent un effet sur la réussite et les résultats sont mitigés, l'usage spontané tourne autour de 30 % des étudiants, et 17 % des systèmes disent à la fois ce qui s'est passé et quoi faire : la revue fixe le constat de départ du domaine.

## La source

| | |
| --- | --- |
| **Équipe** | Département de psychologie et technologie de l'enseignement, université Brigham Young (Utah), et groupe interaction humain-machine du département d'informatique de la KU Leuven (Belgique). |
| **Nature** | Académique ; financement du FWO (Flandre) et du conseil de recherche de la KU Leuven (remerciements, p. 417). Les auteurs développent eux-mêmes des tableaux de bord ; pas de déclaration de conflit. |
| **Support** | *IEEE Transactions on Learning Technologies*. Les renvois se font aux sections et tableaux. |
| **Audience** | 358 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Moyenne : requêtes publiées (tableau 1), grille de codage définie (tableaux 2 à 6), liste des articles sur un site personnel ; double codage de 20 % des articles seulement (accord 86 %). Sans objet pour les chiffres d'effet (aucune synthèse quantitative). |

## Ce que fait l'étude

- **Recherche** (§ 3, tableau 1) : ERIC, IEEE Xplore, ACM, actes LAK et EDM, Google Scholar, revues antérieures ; 945 articles après doublons ; critères : le système suit automatiquement l'activité (les seules notes ne suffisent pas) et la renvoie directement aux étudiants ; 93 retenus (§ 3.1).
- **Codage** (§ 4-5) : fonctions (visualisation, recommandation, comparaison à la classe…), sources de données, démarche de conception (analyse des besoins, choix des informations, conception visuelle, test d'utilisabilité), perceptions, effets mesurés.

## Résultats

- **Fonctions et données** (tableau 7) : données d'utilisation des ressources 75 %, visualisations 67 %, recommandations 46 %, comparaison à la classe 38 %, données d'évaluation 37 %.
- **Démarche de conception** (§ 6.2, tableau 7) : analyse des besoins 6 % des articles, justification des données choisies 15 %, conception visuelle 13 %, test d'utilisabilité 11 %, suivi de l'usage réel 13 %.
- **Effets mesurés** (§ 6.3, tableaux 11 à 13) : comportement 15 articles (16 %), réussite 14 (15 %), compétences 2 (2 %) ; résultats « mitigés » : certains bénéfices, certains effets défavorables, souvent sur de petits échantillons ou par simple comparaison descriptive.
- **Usage** (§ 8.1) : les articles qui le suivent rapportent un usage faible, environ 30 % des étudiants en moyenne ; les systèmes qui envoient des notifications par courriel ou SMS sont plus utilisés que ceux que l'étudiant doit aller consulter (sans chiffre).
- **Résultat + recommandation** (§ 8.2.5) : 16 articles (17 %) combinent recommandation et retour ou visualisation ; les auteurs recommandent de faire les deux.

## Avis critique

**Apport.** La revue qui a établi le constat de départ : beaucoup de systèmes, peu d'évaluation, peu d'usage. Pour DiagForge, deux leçons pratiques : un rapport peu consulté ne sert à rien, et un rapport qui ne dit pas quoi faire reste un constat.

**Points forts**
- Recherche large, croisant éducation et informatique.
- Grille explicite, appliquée à tous les articles.
- Recommandations de méthode (essais, suivi de l'usage) restées d'actualité ([kaliisa2024](kaliisa2024.md)).

**Réserves**
1. **Importante** — Pas de méthode de sélection de la qualité ni de synthèse des effets : le « mitigé » est un décompte de conclusions d'auteurs. Les chiffres d'usage (environ 30 %) et l'avantage des notifications ne sont pas rapportés étude par étude.
2. **Mineure** — Codage par un seul auteur pour 80 % des articles ; corpus arrêté en juin 2016 ; les auteurs incluent des systèmes très différents (recommandation de ressources, tableaux de bord, alertes précoces).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Peu de systèmes de restitution ont un effet démontré sur la réussite | C | Décompte d'une revue descriptive, concordant avec [kaliisa2024](kaliisa2024.md) |
| L'usage spontané est faible (environ 30 %) | C | Moyenne d'articles non détaillée |
| Les notifications augmentent l'usage | D | Constat qualitatif |
| Combiner constat et recommandation améliore l'effet | D | Recommandation des auteurs, non testée |

**Transférabilité** : forte pour les constats de méthode ; le public des études est surtout le supérieur, toutes disciplines.

**Pour conclure, il faudrait** comparer, dans DiagForge, le taux d'ouverture du rapport selon qu'il est envoyé par message Moodle ou seulement déposé dans le cours, puis l'effet sur la participation au quiz suivant.

## Pour Forge

- **DiagForge** : constat et recommandation dans chaque rapport (niveau D) ; **confirme** la règle « terminer le rapport par les notions à revoir » ([herodotou2025](herodotou2025.md)).
- **DiagForge** : envoyer le rapport plutôt que le déposer (niveau D) ; **complète** la règle « journaliser l'ouverture du rapport » : sans envoi, une faible ouverture est attendue.
- Suite du domaine : [matcha2020](matcha2020.md), [valle2021](valle2021.md), [paulsen2024](paulsen2024.md), [kaliisa2024](kaliisa2024.md).
