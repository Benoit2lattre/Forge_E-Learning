---
cle: salden2009
reference: "Salden, R. J. C. M., Aleven, V., Renkl, A. et Schwonke, R. (2009). Worked examples and tutored problem solving: Redundant or synergistic forms of support? Topics in Cognitive Science, 1(1), 203-213."
doi: 10.1111/j.1756-8765.2008.01011.x
axe: [D2, D1]
type_etude: deux expériences à 3 groupes (laboratoire, 57 élèves ; classe, 51 élèves), version courte de Salden et al. (2010)
public: élèves de 9e et 10e année en géométrie (Allemagne ; lycée professionnel près de Pittsburgh)
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "dans un exercice qui corrige chaque étape, ajouter des étapes d'exemple et les retirer selon la maîtrise de l'étudiant plutôt que selon un calendrier fixe"
    niveau: C
    transferabilite: moyenne
    note: "mêmes données que salden2010, ne compte pas comme une preuve de plus"
---

# Exemples et résolution guidée par un STI : redondants ou complémentaires ? (Salden et al., 2009)

Salden, R. J. C. M., Aleven, V., Renkl, A. et Schwonke, R. (2009). Worked examples and tutored problem solving: Redundant or synergistic forms of support? *Topics in Cognitive Science*, 1(1), 203-213. [DOI](https://doi.org/10.1111/j.1756-8765.2008.01011.x)

**En une phrase.** Version courte des deux expériences détaillées dans Salden et al. (2010) : dans un système tutoriel intelligent (STI) de géométrie, l'estompage adaptatif des exemples donne un meilleur transfert que l'estompage fixe et que la résolution guidée par le STI sans exemples, nettement en laboratoire, plus faiblement en classe.

## La source

| | |
| --- | --- |
| **Équipe** | Institut d'interaction homme-machine de Carnegie Mellon et Institut de psychologie de Fribourg-en-Brisgau (Renkl). |
| **Nature** | Académique ; financement National Science Foundation (p. 211). Le STI (Geometry Cognitive Tutor) vient de l'équipe de Carnegie Mellon. |
| **Support** | *Topics in Cognitive Science* (Wiley, Cognitive Science Society), article court. |
| **Audience** | 77 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : séquence d'estompage (tableau 1) et règle d'adaptation (seuils de maîtrise 0,7 et 0,5) décrites ; logiciel et données non fournis. |

## Ce que fait l'étude

- **Trois versions du STI** (p. 206-207) : problèmes seuls ; estompage fixe (exemples complets, puis étapes retirées progressivement) ; estompage adaptatif (une étape devient à résoudre quand la maîtrise estimée du théorème dépasse 0,7, redevient un exemple si elle passe sous 0,5). Dans les étapes d'exemple, l'élève doit nommer le théorème utilisé.
- **Expérience 1** (p. 205-208) : 57 élèves allemands, deux séances en laboratoire, post-test immédiat et différé d'une semaine.
- **Expérience 2** (p. 208-209) : 51 élèves de trois classes, 2 h par semaine pendant 3 semaines dans le cadre du cours, post-test différé de 3 semaines.

## Résultats

- **Laboratoire** (p. 208) : meilleur transfert pour l'estompage adaptatif que pour les deux autres groupes, au post-test immédiat (η² = 0,09) et différé (η² = 0,08) ; estompage fixe et problèmes seuls identiques ; même temps de test.
- **Classe** (p. 209) : forte attrition (20 élèves sur 51 ont fait les trois tests) ; pas de différence au post-test immédiat ; au test différé, avantage de l'adaptatif sur les problèmes seuls (d = 0,91), contraste principal non significatif.
- **Temps** : pas de différence de temps passé dans le STI.

## Avis critique

**Apport.** Même message que Salden et al. (2010) : dans un environnement qui corrige déjà chaque étape, ce sont les exemples retirés au bon moment pour chaque élève, et non l'estompage fixe, qui apportent un gain.

**Points forts**
- Même manipulation testée en laboratoire et en classe.
- Règle d'adaptation simple et explicite.

**Réserves**
1. **Majeure** — Mêmes expériences que Salden et al. (2010) : à ne pas compter comme une confirmation indépendante.
2. **Importante** — Attrition massive dans l'étude en classe ; résultats de classe fragiles.
3. **Mineure** — Article court : méthode et analyses résumées.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| L'estompage adaptatif dans un STI améliore le transfert différé | C | Deux expériences d'une même équipe, effets modestes, attrition |

**Transférabilité** : moyenne. Géométrie du secondaire, mais logique d'étapes justifiées par un principe proche des exercices de mécanique.

**Pour conclure, il faudrait** voir la fiche de Salden et al. (2010).

## Pour Forge

- **ExoForge** : estompage piloté par la maîtrise estimée de chaque principe (niveau C ; s'appuyer sur la fiche de Salden et al., 2010).
