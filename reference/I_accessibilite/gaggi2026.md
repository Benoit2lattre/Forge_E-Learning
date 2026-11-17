---
cle: gaggi2026
reference: "Gaggi, O., Gatto, S. et Noro, M. (2026). Transforming LaTeX lecture notes into accessible multimodal web pages for inclusive STEM learning. In Proceedings of the 2026 International Conference on Information Technology for Social Good (GoodIT '26), Pise, p. 466-474. ACM."
doi: 10.1145/3794786.3830787
axe: [I2]
type_etude: rapport de conception avec évaluation pilote d'utilisabilité (6 utilisateurs)
public: 6 personnes aveugles ou malvoyantes utilisant un lecteur d'écran, sans exigence de niveau en mathématiques
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "formules en MathML (présentation et contenu) rendues par MathJax 4 avec l'exploration au lecteur d'écran activée ; jamais de formule en image"
    niveau: C
    transferabilite: forte
    note: "preuve technique et d'utilisabilité (6 utilisateurs), pas preuve d'apprentissage"
  - outil: QuizForge
    regle: "formules en MathML rendues par MathJax 4 avec l'exploration au lecteur d'écran activée ; jamais de formule en image"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "déclarer la langue de la page (attribut lang='fr') pour que le lecteur d'écran prononce correctement"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "pas de tableau de mise en page (cellules vides annoncées « vide ») ; centrer les équations par CSS"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "page fluide sans largeur fixe pour permettre l'agrandissement sans défilement horizontal ; lien d'évitement vers le contenu principal"
    niveau: C
    transferabilite: forte
  - outil: ExoForge
    regle: "fournir un court mode d'emploi des réglages d'accessibilité de MathJax (langue de la voix, braille)"
    niveau: D
    transferabilite: forte
---

# Notes de cours LaTeX converties en pages web accessibles (Gaggi et al., 2026)

Gaggi, O., Gatto, S. et Noro, M. (2026). Transforming LaTeX lecture notes into accessible multimodal web pages for inclusive STEM learning. In *Proceedings of GoodIT '26*, p. 466-474. ACM. [DOI](https://doi.org/10.1145/3794786.3830787)

**En une phrase.** Une chaîne LaTeX → LaTeXML → HTML5 avec MathML et MathJax 4 rend des notes de cours de mathématiques lisibles et navigables au lecteur d'écran et en braille ; six utilisateurs aveugles ou malvoyants lui donnent une utilisabilité « bonne » (74,6 sur 100) : pour ExoForge et QuizForge, c'est la recette technique à suivre, sans preuve d'effet sur l'apprentissage.

## La source

| | |
| --- | --- |
| **Équipe** | Département de mathématiques « Tullio Levi-Civita », université de Padoue (p. 466) ; travaux antérieurs de l'équipe sur les fonctions rendues par le son et le toucher (réf. 15). |
| **Nature** | Académique ; financé par le département (p. 473) ; les auteurs évaluent leur propre système. |
| **Support** | Actes de conférence ACM (GoodIT '26), relecture de conférence ; libre accès. |
| **Audience** | 0 citation (OpenAlex, 08/11/2026) : article de l'année. |
| **Reproductibilité** | Moyenne : chaîne et règles décrites (tableau 1, p. 469 ; § 3.3, p. 470-471) avec des outils libres (LaTeXML, MathJax, BeautifulSoup) ; code du système non publié dans l'article. La démarche se refait ; les scores se vérifient sur le tableau 2, aux écarts près signalés ci-dessous. |

## Ce que fait l'étude

- **Chaîne** (p. 469-471) : application web Flask ; prétraitement du source LaTeX par expressions régulières (suppression des paquets non pris en charge, Beamer converti en article, liste d'avertissements rendue à l'auteur) ; conversion LaTeXML en HTML5 avec MathML « combiné » (présentation et contenu) ; post-traitement : lien d'évitement, injection de MathJax 4, attribut de langue, remplacement des tableaux de mise en page par des blocs, chemins CSS.
- **Pourquoi MathML combiné** (p. 470) : MathJax 4 construit à partir de la couche « contenu » un arbre sémantique exposé par ARIA ; l'utilisateur entre dans une fraction, passe du numérateur au dénominateur, etc.
- **Évaluation** (p. 471-472) : document test de 11 thèmes (équations du premier degré jusqu'aux limites, dérivée, matrices, fonction par morceaux, figure) ; exploration libre ; questionnaire AUS (version du SUS pour les technologies d'assistance) ; commentaire libre. 6 participants (2 JAWS, 3 VoiceOver, 1 NVDA), tous sur ordinateur.

## Résultats

- **Utilisabilité** (p. 472) : AUS moyen 74,6 (écart-type 19,2), au-dessus de la référence de 55 pour les utilisateurs de lecteur d'écran et de la moyenne de 65 citées par les auteurs.
- **Point le plus faible** (p. 472) : besoin d'apprentissage préalable (Q10).
- **Commentaires** (p. 472-473, 4 participants) : la coexistence voix, braille et agrandissement dans une même page est jugée l'apport principal ; erreurs de lecture vocale sur la portée des racines et la notation f(x) ; réglages avancés de MathJax difficiles à trouver ; un utilisateur expérimenté préfère lire le source LaTeX en braille.
- **Enseignants** (p. 467) : trois enseignants ont accepté les quelques restrictions sur les commandes LaTeX.

## Avis critique

**Apport.** Décrit pas à pas une chaîne reproductible, avec les pièges concrets (tableaux de mise en page, langue non déclarée, paquets non pris en charge) : directement utile à des pages générées par script comme celles d'ExoForge.

**Points forts**
- Choix techniques justifiés (MathML combiné pour la navigation sémantique).
- Test avec de vrais utilisateurs de trois lecteurs d'écran différents.
- Limites reconnues : étude pilote, pas de comparaison (p. 473).

**Réserves**
1. **Majeure** — Preuve technique et d'utilisabilité seulement : six participants, sans tâche de mathématiques, sans mesure de compréhension ni d'apprentissage, sans comparaison avec un PDF balisé ou une autre chaîne. Les participants n'étaient pas tenus d'avoir un niveau en mathématiques (p. 471).
2. **Importante** — Auteurs qui évaluent leur propre système ; participants recrutés en partie par contacts personnels (p. 471).
3. **Mineure** — Moyennes par question différentes entre le texte et le tableau 2 (par exemple Q10 2,3 contre 2,60 ; Q4 1,5 contre 1,60 ; p. 472-473).
4. **Mineure** — Seuils de comparaison (55 et 65) tirés d'une page web d'un prestataire, non d'une publication relue.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| HTML + MathML + MathJax 4 rend les formules navigables au lecteur d'écran et en braille | C | Démonstration technique et pilote cohérents avec les standards (MathML, ARIA) |
| Les utilisateurs aveugles jugent ces pages utilisables | C | 6 participants, auto-évaluation |
| Ces pages améliorent l'apprentissage des mathématiques | D | Non mesuré |

**Transférabilité** : forte pour la technique (MathJax est déjà le moteur de Moodle et d'ExoForge) ; nulle donnée sur nos étudiants.

**Pour conclure, il faudrait** faire passer une page ExoForge et sa version PDF à des étudiants utilisant un lecteur d'écran, avec une tâche de lecture et de résolution, et comparer réussite et temps.

## Pour Forge

- **ExoForge, QuizForge** : formules en MathML ou en TeX rendu par MathJax 4 avec l'exploration activée ; jamais d'image de formule (niveau C, preuve technique).
- **ExoForge** : attribut `lang="fr"` ; pas de tableau de mise en page ; mise en page fluide qui supporte l'agrandissement ; lien d'évitement (niveau C, conformité WCAG).
- **ExoForge** : notice courte des réglages d'accessibilité de MathJax (niveau D).
- Pistes non lues : `chauhan2019` (MathML préféré à LaTeX à l'écoute), `frankel2017` (MathML avec lecture vocale proche du braille).
