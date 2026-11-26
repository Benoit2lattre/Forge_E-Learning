---
cle: menze2026
reference: "Menze, D., Radović, S. et Seidel, N. (2026). AI-assisted MCQ creation increases item-writing flaws through automation bias: Evaluation of a workflow of multiple AI agents with teachers. Frontiers in Computer Science, 8, article 1831250."
doi: 10.3389/fcomp.2026.1831250
axe: [B1]
type_etude: étude comparative de 152 QCM écrits par 19 enseignants, seuls puis avec une IA
public: enseignants d'une université à distance (Allemagne)
lecture: texte complet, 08/11/2026
regles:
  - outil: QuizForge
    regle: "faire passer tout QCM généré par une IA par une vérification automatique des défauts d'écriture avant validation"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "chercher en particulier la reprise de mots de l'énoncé dans la bonne réponse, défaut typique des QCM générés par IA"
    niveau: C
    transferabilite: forte
  - outil: QuizForge
    regle: "imposer une relecture active (modification ou validation critère par critère) plutôt qu'une simple acceptation du brouillon"
    niveau: D
    transferabilite: forte
---

# QCM écrits avec une IA et biais d'automatisation (Menze et al., 2026)

Menze, D., Radović, S. et Seidel, N. (2026). AI-assisted MCQ creation increases item-writing flaws through automation bias: Evaluation of a workflow of multiple AI agents with teachers. *Frontiers in Computer Science*, 8, article 1831250. [DOI](https://doi.org/10.3389/fcomp.2026.1831250)

**En une phrase.** Les QCM produits par une chaîne d'agents d'IA, acceptés tels quels ou retouchés par les enseignants, contiennent plus de défauts d'écriture que les QCM écrits par les enseignants seuls (4,1 et 4,9 défauts par item contre 2,7), alors qu'on ne les distingue pas à la lecture.

## La source

| | |
| --- | --- |
| **Équipe** | Centre CATALPA de la FernUniversität in Hagen (Allemagne), apprentissage assisté par la technologie. |
| **Nature** | Académique ; les auteurs évaluent leur propre outil. |
| **Support** | *Frontiers in Computer Science*, libre accès, noms des relecteurs publiés. |
| **Audience** | 3 citations (OpenAlex, 08/11/2026) ; article de mai 2026. |
| **Reproductibilité** | Bonne : matériel et grille sur l'OSF ; les références renvoient aux sections, la revue numérotant les articles. |

## Ce que fait l'étude

- **Participants** (§ 4.3) : 19 enseignants de l'université, qui écrivent au moins trois QCM par texte, sans consignes détaillées sur les défauts.
- **Ordre** (§ 4) : chaque enseignant écrit d'abord seul sur un premier texte (T), puis avec l'outil d'IA sur un second texte ; un item accepté sans modification est classé « IA », un item modifié « enseignant + IA ».
- **Corpus** : 152 QCM : 63 T, 66 IA, 23 enseignant + IA (11 enseignants seulement ont modifié des brouillons).
- **Mesures** (§ 4.5) : grille de 19 défauts ; tous les items notés par des modèles d'IA, 30 items notés aussi par deux humains ; traces d'interaction (clics, temps) ; perception de l'origine des items.

## Résultats

- **Défauts** (§ 5) : 2,70 par item pour T, 4,09 pour IA, 4,87 pour enseignant + IA ; T contre IA d = 0,75 ; T contre enseignant + IA d = 1,15 ; modèle mixte tenant compte de l'enseignant concordant.
- **Interaction** : temps par item égal, mais trois fois moins de clics avec l'IA (10,8 contre 30,4), ce que les auteurs interprètent comme un biais d'automatisation.
- **Comparaison appariée** : les 23 items retouchés n'ont pas significativement plus de défauts que leurs brouillons IA (+0,35, p = 0,41) : la retouche n'améliore ni n'aggrave.
- **Types de défauts** : les items IA reprennent souvent des mots de l'énoncé dans la bonne réponse, mais évitent les défauts de format des enseignants (questions vrai/faux déguisées, par exemple).
- **Origine** : ni les humains ni les modèles ne distinguent les items IA des items d'enseignants.

## Avis critique

**Apport.** Premier essai, sur des enseignants réels, qui montre qu'une IA qui écrit des QCM « propres en apparence » augmente les défauts d'écriture si l'enseignant valide sans relecture structurée.

**Points forts**
- Grille de défauts explicite et matériel publié.
- Traces d'interaction qui mesurent l'engagement réel des enseignants.
- Les auteurs discutent eux-mêmes plusieurs limites (§ 6.6).

**Réserves**
1. **Majeure** — Ordre et texte confondus avec la condition : chaque enseignant écrit seul sur le premier texte, puis avec l'IA sur le second. L'écart peut venir de la fatigue, de l'ordre ou du texte (les auteurs le signalent, § 6.6).
2. **Importante** — La notation des 152 items repose sur des modèles d'IA dont l'accord entre eux est faible pour plusieurs critères ; seuls 30 items ont été notés par des humains, avec un accord parfois mauvais.
3. **Importante** — Le « biais d'automatisation » est une interprétation : la retouche ne change pas le nombre de défauts, ce qui montre que les enseignants n'ont pas corrigé, pas qu'ils en ont ajouté.
4. **Mineure** — Textes de compréhension écrite, pas de calcul ; 19 enseignants.
5. **Mineure** — Le résumé annonce d = 1,06 pour l'écart entre enseignants seuls et enseignants + IA, la section des résultats d = 1,15.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Des QCM générés par IA et validés sans relecture structurée contiennent plus de défauts | C | Plan non randomisé, ordre confondu, notation par IA |
| Les items IA reprennent les mots de l'énoncé dans la bonne réponse | C | Analyse par critère, une étude |

**Transférabilité** : forte. QuizForge utilise une IA pour proposer des QCM ; le risque décrit est le même.

**Pour conclure, il faudrait** tirer au sort l'ordre des conditions et des textes, et faire noter tous les items par des humains à l'aveugle.

## Pour Forge

- **QuizForge** : contrôle automatique des défauts sur tout item proposé par l'IA avant validation (niveau C).
- **QuizForge** : contrôle prioritaire de la reprise de mots entre énoncé et bonne réponse (niveau C).
- **QuizForge** : validation critère par critère plutôt qu'un bouton « accepter » (niveau D).
