---
cle: chauhan2019
reference: "Chauhan, R., Murray, I. et Koul, R. (2019). Audio rendering of mathematical expressions for blind students: a comparative study between MathML and LaTeX. In 2019 IEEE International Conference on Engineering, Technology and Education (TALE). IEEE."
doi: 10.1109/tale48000.2019.9225961
axe: [I2]
type_etude: note technique de conférence (3 formules lues par un lecteur d'écran, sans participant)
public: aucun participant ; cible annoncée = étudiants aveugles du supérieur
lecture: texte complet, 10/11/2026
regles:
  - outil: ExoForge
    regle: "écouter chaque gabarit de formule avec un lecteur d'écran courant (NVDA) avant diffusion : une lecture linéaire (« X is equal to b b two four a c two a ») est inutilisable, que la source soit LaTeX dans un PDF ou MathML dans une page"
    niveau: C
    transferabilite: forte
    note: "constat technique sur 3 formules, NVDA de 2019 sans moteur de lecture mathématique déclaré"
  - outil: QuizForge
    regle: "formules en MathML (ou TeX rendu par MathJax qui expose la structure), jamais en LaTeX brut ni en image, pour permettre la navigation dans la formule"
    niveau: D
    transferabilite: forte
    note: "argument des auteurs (structure arborescente du MathML), navigation non testée"
---

# Lecture audio des formules : MathML ou LaTeX ? (Chauhan et al., 2019)

Chauhan, R., Murray, I. et Koul, R. (2019). Audio rendering of mathematical expressions for blind students: a comparative study between MathML and LaTeX. In *2019 IEEE International Conference on Engineering, Technology and Education (TALE)*. IEEE. [DOI](https://doi.org/10.1109/tale48000.2019.9225961)

**En une phrase.** Trois formules lues par NVDA, en LaTeX dans un PDF et en MathML dans une page web, donnent dans les deux cas une lecture linéaire incompréhensible ; les auteurs recommandent MathML parce que sa structure permettrait la navigation, sans l'avoir testée : pour Forge, c'est surtout un rappel qu'il faut écouter les formules produites.

## La source

| | |
| --- | --- |
| **Équipe** | Université Curtin (Perth) : école d'éducation, faculté des sciences et de l'ingénierie, faculté des sciences humaines ; première autrice doctorante (p. 1). Travail préparatoire d'un outil à venir (p. 2, 3). |
| **Nature** | Académique ; financement non rapporté. |
| **Support** | Actes de conférence IEEE (TALE 2019), relecture de conférence. Les pages citées sont celles du PDF (1 à 5), la pagination des actes n'apparaissant pas dans le fichier. |
| **Audience** | 5 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Bonne pour la démarche (formules, logiciels et sorties donnés, tableaux I et II, p. 4), mais réglages de NVDA et présence d'un module de lecture mathématique non rapportés. La démarche se refait ; les sorties se vérifient en dix minutes. |

## Ce que fait l'étude

- **Contexte** (p. 1-3) : revue rapide des outils de lecture audio des formules (AsTeR, MathSpeak, i-Math pour LaTeX ; MathPlayer, AudioMath pour MathML) ; deux exigences posées : intelligibilité et navigation dans la formule.
- **Comparaison** (p. 3, § IV) : trois formules « de niveau K-12 » (formule du second degré, longueur d'arc ∫√(1+(dy/dx)²)dx, E = mc²), écrites en LaTeX et rendues en PDF (Acrobat Reader), puis en MathML dans une page HTML (Firefox) ; lecture par NVDA.
- **Mesure** : transcription de la sortie vocale (tableau II, p. 4). Aucun participant, aucune mesure de compréhension.

## Résultats

- **Sorties vocales** (tableau II, p. 4) : formule du second degré lue « X is equal to b b two four a c two a » (PDF) et « X equals b plus or minus b two four a c two a » (MathML) ; intégrale lue « zee b a s one plus dy dx two dx » (PDF) et « Integral zero one one plus dy dx two dx » (MathML) ; E = mc² lu « E equals m c two » dans les deux cas.
- **Constat** (p. 3, § V) : les deux sorties sont « inintelligibles », sans grande différence entre elles ; les lecteurs d'écran lisent la formule comme du texte linéaire.
- **Conclusion** (p. 3-4, § VI) : MathML est préféré parce que sa structure (DOM) permettrait de naviguer élément par élément ; LaTeX n'est qu'une « chaîne ». Argument, non mesuré.

## Avis critique

**Apport.** Montre concrètement ce qu'entend un étudiant aveugle quand une formule est lue sans moteur de parole mathématique : la fraction, la racine et l'exposant disparaissent. Le format source ne suffit pas.

**Points forts**
- Sorties brutes publiées, faciles à refaire.
- Exemples choisis pour les structures difficiles (fraction, racine, puissance, intégrale).

**Réserves**
1. **Majeure** — Le titre annonce une « étude comparative », mais il n'y a ni participant ni mesure : trois formules, un lecteur d'écran, une écoute. La préférence pour MathML repose sur un argument, pas sur un résultat ; le tableau II montre au contraire deux lectures aussi mauvaises.
2. **Importante** — Configuration non décrite : NVDA lit le MathML de façon structurée quand un module de lecture mathématique est installé (MathPlayer, cité p. 3) ; les sorties obtenues suggèrent qu'il ne l'était pas. Le résultat décrit un réglage par défaut, pas les possibilités de MathML.
3. **Mineure** — Erreurs dans le matériel : bornes de l'intégrale a et b en LaTeX mais 0 et 1 en MathML ; balise `<mn>1<mn>` mal fermée et espace de noms MathML erroné (tableau I, p. 4). Le MathML testé n'est pas toujours valide.
4. **Mineure** — Mathématiques de niveau secondaire alors que la cible annoncée est le supérieur.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Un lecteur d'écran sans moteur mathématique lit les formules de façon linéaire et ambiguë | C | Constat technique direct, 3 formules, un seul logiciel |
| MathML est meilleur que LaTeX pour la lecture audio | D | Argument structurel ; aucune différence observée à l'écoute |

**Transférabilité** : forte pour le constat technique (NVDA est gratuit et courant) ; aucune donnée sur des utilisateurs.

**Pour conclure, il faudrait** faire lire les mêmes formules de mécanique par NVDA avec et sans moteur mathématique, et par MathJax 4 avec l'exploration activée, à des étudiants utilisant un lecteur d'écran, et mesurer la reconnaissance de la structure.

## Pour Forge

- **ExoForge** : écouter chaque gabarit de formule avec NVDA avant diffusion ; une lecture linéaire est inutilisable (niveau C, preuve technique).
- **QuizForge** : formules en MathML ou TeX rendu par MathJax, jamais en LaTeX brut ni en image (niveau D pour l'argument propre à cet article ; niveau C par [gaggi2026](gaggi2026.md)).
- Renvois : [gaggi2026](gaggi2026.md) (chaîne MathML + MathJax 4 testée), [frankel2017](frankel2017.md) (lecture vocale avec moteur et navigation, testée avec des élèves).
