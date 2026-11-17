---
cle: kinnear2022
reference: "Kinnear, G., Jones, I., Sangwin, C., Alarfaj, M., Davies, B., Fearn, S., Foster, C., Heck, A., Henderson, K., Hunt, T., Iannone, P., Kontorovich, I., Larson, N., Lowe, T., Meyer, J. C., O'Shea, A., Rowlett, P., Sikurajapathi, I. et Wong, T. (2024). A collaboratively-derived research agenda for e-assessment in undergraduate mathematics. International Journal of Research in Undergraduate Mathematics Education, 10, 201-231 (en ligne le 12/09/2022)."
doi: 10.1007/s40753-022-00189-6
axe: [H1]
type_etude: programme de recherche établi par consensus d'experts (méthode inspirée de Delphi, 22 participants), sans données sur les étudiants
public: sans objet (enseignants, chercheurs et développeurs d'outils d'évaluation en ligne en mathématiques du supérieur, surtout au Royaume-Uni)
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "conserver toutes les réponses brutes et l'erreur type reconnue avec le tirage de paramètres, pour pouvoir étudier les erreurs a posteriori (y compris celles propres à la saisie : syntaxe, mauvais bouton)"
    niveau: D
    transferabilite: forte
  - outil: ExoForge
    regle: "prévoir de pouvoir comparer, par tirage au sort, des leurres issus des erreurs types et des leurres générés au hasard, et un retour diagnostique contre une solution rédigée générale : ces choix ne sont pas tranchés"
    niveau: D
    transferabilite: forte
  - outil: DiagForge
    regle: "résumer les données de réponses pour l'enseignant sous une forme qui appelle une action (notions et erreurs à reprendre), plutôt que livrer des données brutes"
    niveau: D
    transferabilite: forte
---

# Programme de recherche sur l'évaluation en ligne en mathématiques (Kinnear et al., 2022)

Kinnear, G., Jones, I., Sangwin, C. et al. (2024). A collaboratively-derived research agenda for e-assessment in undergraduate mathematics. *International Journal of Research in Undergraduate Mathematics Education*, 10, 201-231 (en ligne le 12/09/2022). [DOI](https://doi.org/10.1007/s40753-022-00189-6)

**En une phrase.** Vingt-deux chercheurs, enseignants et développeurs d'outils (STACK, Numbas, Dewis) listent 55 questions de recherche ouvertes sur l'évaluation en ligne en mathématiques du supérieur, en cinq thèmes ; pour Forge, c'est une carte des choix de conception qui restent sans preuve (erreurs types ou leurres aléatoires, report d'erreur, effet des paramètres aléatoires), pas une source de règles établies.

## La source

| | |
| --- | --- |
| **Équipe** | Pilotée par Kinnear, Jones et Sangwin (Édimbourg, Loughborough) ; participants surtout britanniques, dont des développeurs d'outils et des auteurs d'autres fiches de l'axe (Sikurajapathi, Henderson) (tableau 1, p. 204). |
| **Nature** | Académique ; pas de conflit d'intérêts déclaré ; financement non rapporté. Les participants proposent les questions qu'ils souhaitent étudier. |
| **Support** | *International Journal of Research in Undergraduate Mathematics Education* (Springer), libre accès. |
| **Audience** | 28 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Sans objet pour des résultats ; démarche décrite (p. 202-206) et site public du programme (cité p. 206). |

## Ce que fait l'étude

- **Démarche** (p. 202-206) : 61 questions proposées en ligne par 22 participants ; réunion en ligne de deux heures (21 présents) ; 52 questions après fusion ; retours de trois conférences en ligne (2020), 3 questions ajoutées ; 55 questions sans hiérarchie, la priorisation prévue ayant été abandonnée.
- **Cinq thèmes** : erreurs et retour (Q1-12) ; interactions des étudiants (Q13-20) ; choix de conception (Q21-34) ; possibilités des outils (Q35-48) ; compétences mathématiques (preuve, génération d'exemples, Q49-55).

## Résultats (questions utiles à Forge)

- **Erreurs** (p. 207-208) : quelles erreurs fréquentes (Q1) ; diffèrent-elles du papier (Q2, erreurs de syntaxe ou de clic) ; comment les détecter (Q3), en notant que c'est plus difficile quand les paramètres sont tirés au hasard.
- **Coût du diagnostic** (p. 209-210) : quand le diagnostic des erreurs vaut-il l'effort par rapport à une solution type (Q10) ; traiter les erreurs en amont dans l'enseignement ou après coup par le retour (Q11) ; résultats contradictoires dans la littérature citée.
- **Paramètres aléatoires** (p. 213-214) : réduisent-ils le plagiat (Q24) ; quel effet sur les résultats et le coût de conception (Q25) ; leurres issus des erreurs ou leurres aléatoires (Q26), ces derniers pouvant agir comme un retour immédiat quand l'étudiant ne voit pas sa réponse.
- **Pratique répétée** (p. 210-211) : la répétition de variantes fait-elle découvrir la structure ou seulement repérer des motifs (Q14).
- **Données pour l'enseignant** (p. 215) : comment rendre les données de réponses utilisables (Q34), les données brutes étant « écrasantes ».
- **Notation** (p. 218) : comment reproduire le report d'erreur et le crédit partiel d'un correcteur humain (Q43).
- **Limites reconnues** (p. 223) : groupe surtout britannique, partageant les mêmes outils ; peu de questions sur l'équité.

## Avis critique

**Apport.** Recense les décisions de conception d'ExoForge et QuizForge que la recherche n'a pas tranchées : utile pour ne pas présenter comme établies des règles de pratique, et pour choisir les essais à mener nous-mêmes.

**Points forts**
- Participants qui conçoivent et utilisent réellement ces outils.
- Chaque question motivée et reliée à la littérature.
- Limites de représentativité énoncées.

**Réserves**
1. **Importante** — Pas de priorisation : les 55 questions ont le même poids, ce qui n'aide pas à choisir.
2. **Mineure** — Consensus d'un réseau restreint (surtout Royaume-Uni, outils STACK et Numbas).

**Niveau de preuve** : sans objet pour les résultats (questions, pas réponses) ; les règles tirées sont de niveau D.

**Transférabilité** : forte (mathématiques du supérieur, outils de même nature qu'ExoForge).

**Pour conclure, il faudrait** retenir deux ou trois questions testables dans nos outils, par exemple Q26 (leurres issus des erreurs contre leurres aléatoires) dans QuizForge et Q10 (retour diagnostique contre solution type) dans ExoForge, par tirage au sort entre étudiants.

## Pour Forge

- **ExoForge** : conserver les réponses brutes, le tirage et l'erreur reconnue (D) ; rendre possibles les comparaisons tirées au sort sur les leurres et le type de retour (D).
- **DiagForge** : restitution à l'enseignant orientée vers l'action (D).
- Renvois : réponses partielles à Q1-Q3 dans [sikurajapathi2020](sikurajapathi2020.md) et [sikurajapathi2023](sikurajapathi2023.md) ; à Q43 dans [pearson2022](pearson2022.md) ; principes de conception (Q21) dans [greenhow2015](greenhow2015.md).
