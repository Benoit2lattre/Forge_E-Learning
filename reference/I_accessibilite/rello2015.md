---
cle: rello2015
reference: "Rello, L. et Baeza-Yates, R. (2017). How to present more readable text for people with dyslexia. Universal Access in the Information Society, 16(1), 29-49 (en ligne 2015)."
doi: 10.1007/s10209-015-0438-8
axe: [I1]
type_etude: huit expériences intra-sujets en oculométrie (un paramètre de présentation par expérience, ordre contrebalancé), avec questionnaire de préférences
public: 92 hispanophones de 11 à 45 ans (46 dyslexiques diagnostiqués, 46 témoins), dont 49 étudiants ou diplômés du supérieur, lecture à l'écran
lecture: texte complet, 10/11/2026
regles:
  - outil: ExoForge
    regle: "texte courant (énoncés, retours) en taille généreuse, jamais réduite, et exprimée en unités relatives (rem, em) pour que l'agrandissement du navigateur fonctionne"
    niveau: C
    transferabilite: moyenne
    note: "14 pt allonge les fixations par rapport à 22-26 pt, dyslexiques ou non"
  - outil: QuizForge
    regle: "ne pas réduire la taille de police dans le HTML des questions et des retours (pas de font-size en petits caractères ou en pixels)"
    niveau: C
    transferabilite: moyenne
  - outil: ExoForge
    regle: "ne jamais resserrer l'interlettrage (pas de letter-spacing négatif) ; espacement normal ou légèrement augmenté"
    niveau: C
    transferabilite: moyenne
  - outil: ExoForge
    regle: "texte noir ou très foncé sur fond clair uni ; pas de texte gris clair"
    niveau: C
    transferabilite: moyenne
    note: "préférence déclarée ; aucun effet du gris sur les fixations"
  - outil: CapsuleForge
    regle: "texte des diapositives en grande taille, sans interlettrage resserré, noir sur fond clair"
    niveau: C
    transferabilite: moyenne
---

# Taille et espacement du texte à l'écran pour les lecteurs dyslexiques (Rello et Baeza-Yates, 2015)

Rello, L. et Baeza-Yates, R. (2017). How to present more readable text for people with dyslexia. *Universal Access in the Information Society*, 16(1), 29-49 (publié en ligne en novembre 2015). [DOI](https://doi.org/10.1007/s10209-015-0438-8)

**En une phrase.** Sur huit paramètres de présentation testés à l'écran chez 92 lecteurs, seuls la taille de police (14 pt plus lent que 22-26 pt) et l'interlettrage (−7 % plus lent que +7 % ou +14 %) changent la durée des fixations, pour les dyslexiques comme pour les autres ; couleurs, gris, interligne, espacement des paragraphes et largeur de colonne n'ont pas d'effet mesurable : pour Forge, du texte assez grand, jamais serré.

## La source

| | |
| --- | --- |
| **Équipe** | Institut d'interaction humain-machine, Carnegie Mellon (Pittsburgh) ; Yahoo Labs et groupe de recherche web de l'université Pompeu Fabra (Barcelone) ; travail de thèse de la première autrice (p. 29). |
| **Nature** | Académique et industrielle ; financement non rapporté. Les auteurs ont intégré ces recommandations dans leurs propres outils de lecture (p. 45). |
| **Support** | *Universal Access in the Information Society* (Springer). |
| **Audience** | 122 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Moyenne : paramètres et couleurs détaillés (tableau 1, annexe 1) ; textes en partie publiés ; données non publiées. |

## Ce que fait l'étude

- **Public** (p. 35, tableau 1 p. 34) : 46 dyslexiques diagnostiqués et 46 témoins hispanophones ; 21 dyslexiques et 28 témoins à l'université ou diplômés.
- **Paramètres** (p. 33) : gris du texte, gris du fond, 8 paires de couleurs, taille (14, 18, 22, 26 pt), interlettrage (−7, 0, +7, +14 %), interligne (0,8 à 1,4), espacement des paragraphes, largeur de colonne (22 à 88 caractères). Un paramètre à la fois ; réglage par défaut Arial 20 pt, 66 caractères par ligne (p. 36).
- **Mesures** : durée moyenne des fixations (oculomètre) ; préférence déclarée ; compréhension (3 QCM) utilisée seulement comme filtre (p. 35, 37). Séance de 30 à 40 minutes ; lecture silencieuse de 36 fragments courts (p. 36-37).

## Résultats

- **Groupes** : les dyslexiques fixent plus longtemps dans toutes les expériences (par exemple 0,229 contre 0,202 s pour la taille, p < 0,001 ; p. 39).
- **Taille** (p. 39, tableau 2 p. 38) : effet principal F(3, 372) = 8,80, p < 0,001, sans interaction avec le groupe. Dyslexiques : 0,259 s à 14 pt contre 0,216 s à 22 pt et 0,208 s à 26 pt (p = 0,003) ; témoins : 0,223 contre 0,186 s à 26 pt (p = 0,005), soit environ −20 % et −17 % [calcul]. 26 pt est la taille préférée des deux groupes (p. 39).
- **Interlettrage** (p. 40) : effet principal F(3, 368) = 2,86, p = 0,037 ; −7 % plus lent que +7 % (p = 0,035) et +14 % (p = 0,013) ; aucun effet à l'intérieur de chaque groupe. Les témoins préfèrent l'espacement standard.
- **Sans effet sur les fixations** (p. 37-41) : gris du texte, gris du fond, couleurs, interligne, paragraphes, largeur de colonne. Préférences : texte noir (60 % des dyslexiques, 93,9 % des témoins, p. 41-42) ; 44 caractères par ligne préférés par les seuls témoins (p. 41).
- **Recommandations** (tableau 3, p. 44) : 18 à 26 pt ; interlettrage 0 à +14 % ; noir sur blanc ou blanc sur noir ; polices Arial, Courier, CMU, Helvetica, Verdana, ces dernières reprises d'une autre étude des auteurs ([rello2016](rello2016.md)).

## Avis critique

**Apport.** Seule étude de l'axe qui fait varier la taille et l'espacement à l'écran, avec un groupe témoin et un public en partie universitaire ; montre surtout que beaucoup de recommandations courantes (couleurs, interligne) n'ont pas d'effet mesurable.

**Points forts**
- 92 participants, plan intra-sujets contrebalancé, groupe témoin.
- Huit paramètres testés avec la même méthode ; nombreux résultats nuls rapportés.
- Public adulte en partie étudiant.

**Réserves**
1. **Majeure** — La seule mesure est la durée des fixations sur des fragments très courts (moins de 22 mots pour certains) ; ni temps de lecture, ni compréhension mesurée comme résultat (p. 43). Un effet sur les fixations n'est pas un effet sur l'apprentissage.
2. **Importante** — Plusieurs incohérences : l'interaction interlettrage × groupe est dite « significative » avec F = 0,52, p = 0,665 (p. 40) ; 18 pt est dit « significativement » meilleur que 14 pt avec p = 0,054 (p. 39) ; la conclusion recommande 18 à 24 pt contre 18 à 26 pt ailleurs (p. 45 et 44) ; âges des groupes différents entre le tableau 1 et le texte (p. 34-35) ; oculomètre « Tobii 1750 » puis « T50 » (p. 35-36).
3. **Importante** — Effet de l'interlettrage fragile : p = 0,037 sur l'ensemble, rien dans chaque groupe.
4. **Mineure** — Les points d'écran (17 pouces, 1024 × 768) ne se traduisent pas directement en CSS ; paramètres testés un à un, sans interactions.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Un texte plus grand se lit avec des fixations plus courtes, dyslexiques ou non | C | Un essai intra-sujets, mesure indirecte, textes courts |
| Un interlettrage resserré gêne | C | Effet faible, non retrouvé par groupe |
| Couleurs, gris, interligne, largeur de colonne sans effet | C | Résultats nuls avec 45 participants par groupe : absence de preuve |

**Transférabilité** : moyenne. Adultes et étudiants lisant à l'écran, mais en espagnol, sans formules ni figures.

**Pour conclure, il faudrait** comparer dans ExoForge deux tailles de base (par exemple 1 rem et 1,25 rem) tirées au sort, sur le temps par énoncé et la réussite.

## Pour Forge

- **ExoForge, QuizForge** : taille de texte généreuse, en unités relatives, jamais réduite pour les retours (niveau C).
- **ExoForge** : pas de `letter-spacing` négatif (niveau C).
- **ExoForge, CapsuleForge** : texte noir ou très foncé sur fond clair uni (niveau C, préférence).
- Pas de règle sur l'interligne, les couleurs ou la largeur de colonne : aucun effet mesuré. Pour la police, voir [rello2016](rello2016.md) ; pour l'espacement, [marinus2016](marinus2016.md).
