---
cle: mcmillan2026
reference: "McMillan, M. et Boyden, E. (2026). Tooling for digital accessibility in mathematics: quickly build compliant course websites that benefit all students. In 2026 ASEE Annual Conference & Exposition Proceedings, paper 53256."
doi: 10.18260/1-2--60998
axe: [I2]
type_etude: rapport de conception (taxonomie et chaîne d'outils) avec étude observationnelle non randomisée (31 sections, 6 semestres)
public: étudiants de Calculus II, université de Virginie (environ 197 par semestre) ; pas d'étudiant en situation de handicap étudié en particulier
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "écrire le contenu en source texte (Markdown + TeX) et publier la page HTML avec MathML comme support principal ; le PDF n'est qu'une sortie secondaire"
    niveau: D
    transferabilite: forte
    note: "argument de conception et de conformité, pas preuve d'apprentissage"
  - outil: ExoForge
    regle: "ne pas proposer une version accessible de moindre qualité à côté d'un support principal inaccessible : la version accessible est la version principale"
    niveau: D
    transferabilite: forte
  - outil: QuizForge
    regle: "formules des questions en TeX converti en MathML (ou MathJax), pas en image"
    niveau: D
    transferabilite: forte
  - outil: ExoForge
    regle: "republication en une commande après modification, pour que les corrections en cours de semestre restent dans la version accessible"
    niveau: D
    transferabilite: forte
---

# Sites de cours en HTML + MathML générés depuis Markdown (McMillan et Boyden, 2026)

McMillan, M. et Boyden, E. (2026). Tooling for digital accessibility in mathematics: quickly build compliant course websites that benefit all students. In *2026 ASEE Annual Conference & Exposition Proceedings*. [DOI](https://doi.org/10.18260/1-2--60998)

**En une phrase.** Une chaîne gratuite (Obsidian, Quartz, Git, Cloudflare Pages) publie des pages de cours en HTML avec MathML à partir de Markdown + TeX, en une commande ; les sections de Calculus II qui l'utilisent ont de meilleures notes, mais avec un seul enseignant et sans aucune mesure d'accessibilité : pour Forge, l'argument retenu est la chaîne source texte → HTML + MathML comme support principal, pas le gain de notes.

## La source

| | |
| --- | --- |
| **Équipe** | Centre de mathématiques appliquées, université de Virginie : un enseignant-chercheur et un étudiant de licence en informatique et mathématiques (p. 1). |
| **Nature** | Académique ; soutien du centre pédagogique de l'université pour le second auteur (p. 19). Les auteurs évaluent leur propre système. L'article ne dit pas explicitement qui est l'enseignant des sections « traitement ». |
| **Support** | Actes de la conférence annuelle de l'ASEE (enseignement de l'ingénierie), relecture de conférence. |
| **Audience** | 0 citation (OpenAlex, 08/11/2026) : article de l'année. |
| **Reproductibilité** | Bonne pour la chaîne (tutoriel public, outils libres, p. 9-11) ; faible pour l'étude : données de notes en annexe (tableau 3), mais pas de modèle statistique. La démarche technique se refait ; l'effet sur les notes ne se vérifie pas. |

## Ce que fait l'étude

- **Taxonomie** (p. 5-9, tableau 1) : solutions orientées impression (P1 : PDF → MathML par reconnaissance ; P2 : LaTeX → MathML par LaTeXML, Pandoc, tex4ht) et orientées web (W1 : éditeur d'équations du LMS ; W2 : CMS professionnel ; W3 : Markdown + TeX dans un outil local et générateur de site statique), évaluées sur 7 critères (syntaxe TeX, révision facile, peu d'expertise, coût, contrôle d'accès, gestion de contenu, compatibilité avec l'IA).
- **Chaîne W3** (p. 9-11) : rédaction dans Obsidian ; MathML produit par KaTeX ou par un module Temml ; « commit and sync » déclenche la reconstruction du site dans le nuage (2 à 5 minutes pour six cours) ; installation 1 à 2 heures.
- **Étude** (p. 12-14) : 31 sections de Calculus II sur 6 semestres ; 26 sections témoins (PDF sur Canvas, 6 enseignants), 5 sections « traitement » d'un seul enseignant : F24 en PDF (point de référence), S25 avec site (1 section), F25 avec le système complet (2 sections). Mêmes examens communs (70 à 75 % de la note). Mesures : moyenne de section (GPA), part de A, part d'échecs et abandons ; questionnaire d'expérience en F25.

## Résultats

- **Notes** (p. 14-15, figure 4) : F24 environ un écart-type (entre sections) sous les témoins ; S25 plus d'un écart-type au-dessus ; F25 2,46 écarts-types au-dessus des témoins. Part de A en hausse et part d'échecs plus basse en S25 et F25 (figure 5).
- **Expérience** (p. 15-16, tableau 2) : 55 réponses sur 89 en traitement, 16 sur 87 en témoin ; aucune différence significative (t de Welch unilatéral, p ≥ 0,15).
- **Accessibilité** (p. 12) : non évaluée ; « MathML est pris comme indicateur de conformité ».

## Avis critique

**Apport.** Une taxonomie claire des façons d'obtenir des mathématiques accessibles, et l'argument que la sortie web doit être la version principale (« tentation de la primauté du PDF », p. 6). La chaîne décrite ressemble à ce que fait déjà ExoForge (source texte, génération de pages).

**Points forts**
- Chaîne gratuite, documentée, utilisée sur six cours.
- Limites discutées une à une avec les éléments qui les atténuent (p. 17-18).
- Comparaison du même enseignant avant et après le site.

**Réserves**
1. **Majeure** — Un seul enseignant dans le groupe traitement, nouveau sur le cours, qui change aussi sa façon de faire cours (tableau noir puis notes annotées sur tablette) et ajuste ses supports aux examens entre F24 et S25 (p. 17) : l'effet du site ne peut pas être séparé de l'enseignant. Le changement de prérequis entre S25 et F25 s'ajoute (p. 13).
2. **Majeure** — Aucune preuve d'accessibilité : ni test au lecteur d'écran, ni étudiant concerné (p. 12). C'est une preuve de faisabilité technique, et l'effet sur les notes ne dit rien de l'accessibilité.
3. **Importante** — Effet mesuré en écarts-types entre moyennes de sections (2 sections en F25), sans test ni modèle ; « 2,46 écarts-types » n'est pas une taille d'effet par étudiant.
4. **Mineure** — Questionnaire avec 16 réponses témoins (18 %) et tests unilatéraux.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| La chaîne Markdown + TeX → HTML + MathML est réalisable à faible coût par un enseignant | C | Démonstration sur six cours, tutoriel public |
| Le site de cours améliore les notes en Calculus II | D | Un enseignant, variables confondues, pas de test |
| Le site ne dégrade pas l'expérience des étudiants | D | Absence de différence sur 16 réponses témoins |
| Les pages produites sont accessibles aux lecteurs d'écran | D | Non testé ; repose sur le standard MathML (voir [gaggi2026](gaggi2026.md)) |

**Transférabilité** : forte pour la technique (étudiants scientifiques du supérieur, mathématiques, source TeX) ; nulle pour la preuve d'apprentissage.

**Pour conclure, il faudrait** passer au lecteur d'écran (NVDA, VoiceOver) un échantillon de pages ExoForge et QuizForge et noter, formule par formule, ce qui est lu correctement.

## Pour Forge

- **ExoForge** : garder la source texte (Markdown + TeX) et faire de la page HTML + MathML le support principal ; tout PDF est dérivé (niveau D, argument de conception).
- **ExoForge, QuizForge** : pas de formule en image (niveau D ici ; C avec [gaggi2026](gaggi2026.md)).
- **ExoForge** : republication en une commande, pour que les corrections atteignent la version accessible (niveau D).
- Ne pas citer le gain de notes comme argument pour l'accessibilité.
