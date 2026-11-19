---
cle: davies2024
reference: "Davies, B., Crisan, C., Geraniou, E. et Smart, T. (2024). A Department-Wide Transition to a New Mode of Computer-Aided Assessment Using STACK. International Journal of Research in Undergraduate Mathematics Education, 10, 850-870."
doi: 10.1007/s40753-024-00251-5
axe: [H1]
type_etude: étude de cas qualitative (entretiens de 6 concepteurs débutants, 445 commentaires d'étudiants), passage de tout un département à STACK
public: enseignants et doctorants chargés de TD d'un département de mathématiques britannique ; étudiants de 1re et 2e année de licence de mathématiques
lecture: texte complet, 10/11/2026
regles:
  - outil: ExoForge
    regle: "avant diffusion, tester chaque question sur un jeu de réponses justes écrites autrement (4/2 pour 2, racine rationalisée au dénominateur, autre forme d'une solution d'équation différentielle) et faire relire la question par un collègue qui la résout"
    niveau: C
    transferabilite: forte
    note: "faux négatifs fréquents chez des concepteurs débutants, avec perte de confiance des étudiants (p. 859-861)"
  - outil: ExoForge
    regle: "séparer l'erreur de saisie de la réponse fausse : guide de syntaxe (lettres grecques, indices) avant le premier exercice, aperçu de l'expression interprétée, et pas d'effacement des autres saisies en cas de faute de frappe"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "exercice en plusieurs parties : retour après chaque partie et report d'erreur, pour ne pas pénaliser plusieurs fois la même erreur"
    niveau: D
    transferabilite: forte
  - outil: QuizForge
    regle: "fixer et annoncer une même politique de retour (immédiat, ou solution après la date limite) pour tous les quiz d'un parcours"
    niveau: D
    transferabilite: moyenne
  - outil: DiagForge
    regle: "restituer à l'enseignant, par question, les réponses fausses les plus fréquentes, pour remplacer la synthèse des erreurs que faisaient les correcteurs de copies"
    niveau: D
    transferabilite: forte
    note: "manque relevé par les enseignants (p. 864) ; solution proposée par les auteurs, non testée (p. 867)"
---

# Passage d'un département de mathématiques à STACK (Davies et al., 2024)

Davies, B., Crisan, C., Geraniou, E. et Smart, T. (2024). A Department-Wide Transition to a New Mode of Computer-Aided Assessment Using STACK. *International Journal of Research in Undergraduate Mathematics Education*, 10, 850-870. [DOI](https://doi.org/10.1007/s40753-024-00251-5)

**En une phrase.** Quand plus de 20 modules d'un département passent en même temps à des quiz STACK notés, conçus par des débutants, les problèmes viennent surtout des réponses justes refusées et des saisies mal interprétées, et le retour reste général (solution rédigée) faute de temps pour coder les erreurs types ; les enseignants perdent aussi la synthèse des erreurs fréquentes que leur donnaient les copies.

## La source

| | |
| --- | --- |
| **Équipe** | Université de Southampton (école d'éducation) et IOE, University College London (p. 850). Le premier auteur a codirigé le projet étudié mais n'a pas mené les entretiens (p. 851, 856). |
| **Nature** | Académique ; financement non rapporté ; aucun conflit d'intérêts déclaré (p. 868). Les auteurs étudient un projet de leur département. |
| **Support** | *International Journal of Research in Undergraduate Mathematics Education* (Springer), libre accès. |
| **Audience** | 7 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Faible : guide d'entretien résumé (p. 856), données non publiées pour l'anonymat (p. 868). La démarche se refait ; les observations ne se vérifient pas. |

## Ce que fait l'étude

- **Contexte** (p. 855) : pendant la pandémie, quiz STACK non testés déployés dans plus de 20 modules des deux premières années, notés, en remplacement des feuilles d'exercices manuscrites ; deux enseignants à plein temps et plus de 10 doctorants sur deux ans.
- **Participants** (p. 851, 855-856) : 4 responsables de module et 2 doctorants, tous sans expérience préalable de l'évaluation en ligne.
- **Données** (p. 855-856) : entretiens semi-directifs, dont une réflexion sur la question préférée et la moins aimée ; 445 commentaires libres d'étudiants de 8 modules ; réflexions du codirecteur du projet.
- **Analyse** (p. 856-857) : analyse thématique inductive, lue ensuite à travers les cinq principes de conception de Sangwin (2013).

## Résultats

- **Choix des questions** (p. 857-858) : on garde ce qui se code facilement (réponses numériques ou algébriques) ; randomiser en gardant une difficulté de calcul comparable demande beaucoup de travail et d'essais (p. 858).
- **Réponses justes refusées** (p. 859-860) : 4/2 refusé quand la clé est 2 ; racine au dénominateur rationalisée non reconnue ; formes équivalentes de solutions d'équations différentielles (p. 861). Un étudiant : « mon approche était-elle fausse ? mon calcul ? ma saisie ? » (p. 860) ; dans un module, « les quiz avaient presque toujours des erreurs » (p. 859).
- **Saisie** (p. 861) : une faute de frappe dans une formule efface toutes les réponses ; il faut apprendre aux étudiants à saisir lettres grecques et indices.
- **Contenus** (p. 861-863) : méthodes de calcul faciles à évaluer ; démonstrations remplacées par des textes à trous ou des QCM, que certains enseignants refusent comme mesure de compréhension.
- **Retour** (p. 863-865) : en général solution rédigée complète pour toute réponse, indices propres à certaines réponses fausses ; pas de retour adapté à la saisie faute de moyens ; retour après chaque partie pour ne pas pénaliser une erreur reportée ; trois essais avant la solution, ou nouvelle version de la question à chaque essai. En mode noté, solution seulement après la date limite, parfois deux semaines plus tard (p. 863-864), avec des pratiques différentes selon les modules (p. 864).
- **Perte pour l'enseignant** (p. 864, 867) : plus de synthèse des erreurs fréquentes, autrefois faite par les correcteurs ; les traces Moodle pourraient la remplacer mais ne sont pas utilisées.

## Avis critique

**Apport.** Un retour d'expérience franc sur ce qui casse quand on industrialise des questions à calcul formel : les faux négatifs et la saisie, plus que le contenu. Il montre aussi que coder le retour par erreur type demande un catalogue d'erreurs que les concepteurs n'ont pas.

**Points forts**
- Déploiement à l'échelle d'un département, avec des participants peu enthousiastes, rare dans ce domaine (p. 855).
- Exemples précis de défauts de correction automatique.
- Premier auteur écarté du recueil des données (p. 856).

**Réserves**
1. **Majeure** — Six personnes interrogées et des commentaires libres : aucune fréquence (part de questions défectueuses, part de faux négatifs) ni mesure d'apprentissage.
2. **Importante** — Contexte d'urgence (pandémie, quiz non testés, concepteurs débutants) : une partie des défauts tient au déploiement précipité, comme le disent les auteurs (p. 859-860).
3. **Mineure** — Les principes de Sangwin sont appliqués a posteriori ; leur utilité pour former les concepteurs est une conjecture (p. 867).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Des concepteurs débutants produisent des questions qui refusent des réponses justes équivalentes | C | Exemples répétés dans plusieurs modules, sans fréquence |
| Ces erreurs de correction entament la confiance des étudiants | C | Commentaires d'étudiants concordants |
| Un retour par erreur type est hors de portée sans catalogue d'erreurs | D | Témoignages, non mesuré |
| Les traces peuvent remplacer la synthèse des erreurs faite par les correcteurs | D | Proposition des auteurs |

**Transférabilité** : forte pour les leçons techniques (STACK dans Moodle, mêmes types de saisies) ; moyenne pour le reste, licence de mathématiques pures et appliquées.

**Pour conclure, il faudrait** compter, sur une banque ExoForge, la part de réponses justes refusées avant et après un test systématique sur des formes équivalentes.

## Pour Forge

- **ExoForge** : jeu de formes équivalentes testé sur chaque question et relecture par un collègue (niveau C) ; guide de syntaxe, aperçu de l'expression interprétée, saisies conservées (niveau C) ; retour après chaque partie avec report d'erreur (niveau D).
- **QuizForge** : politique de retour unique et annoncée (niveau D).
- **DiagForge** : réponses fausses les plus fréquentes par question, transmises à l'enseignant (niveau D).
- Renvois : `pearson2022` (report d'erreur) ; `orthaber2020` (STACK en mécanique) ; `sikurajapathi2020` (catalogue d'erreurs types) ; `gaona2018` (retour immédiat ou différé).
