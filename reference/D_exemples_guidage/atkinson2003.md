---
cle: atkinson2003
reference: "Atkinson, R. K., Renkl, A. et Merrill, M. M. (2003). Transitioning from studying examples to solving problems: Effects of self-explanation prompts and fading worked-out steps. Journal of Educational Psychology, 95(4), 774-783."
doi: 10.1037/0022-0663.95.4.774
axe: [D1, D3]
type_etude: deux essais randomisés en laboratoire, une séance (plan 2 × 2, puis 2 groupes)
public: 78 étudiants en psychologie (États-Unis), puis 40 lycéens en algèbre avancée
lecture: texte complet, 08/11/2026
regles:
  - outil: ExoForge
    regle: "à chaque étape résolue d'un exemple, faire choisir dans une liste le principe appliqué, puis afficher la bonne réponse"
    niveau: B
    transferabilite: forte
    note: "choix du principe et retour sur ce choix sont confondus ; Bisra et al. (2018) ne comptent pas ce format comme une auto-explication"
  - outil: ExoForge
    regle: "estomper les étapes résolues d'un exercice à l'autre (exemple complet, puis une étape à faire, puis deux, puis tout) plutôt qu'alterner exemple complet et exercice complet"
    niveau: B
    transferabilite: moyenne
---

# Estompage et choix du principe (Atkinson et al., 2003)

Atkinson, R. K., Renkl, A. et Merrill, M. M. (2003). Transitioning from studying examples to solving problems: Effects of self-explanation prompts and fading worked-out steps. *Journal of Educational Psychology*, 95(4), 774-783. [DOI](https://doi.org/10.1037/0022-0663.95.4.774)

**En une phrase.** Sur des problèmes de probabilités en trois étapes, l'estompage des étapes résolues et le choix du principe appliqué à chaque étape d'exemple améliorent chacun le transfert proche et éloigné, sans allonger le temps de travail.

## La source

| | |
| --- | --- |
| **Équipe** | Arizona State University (Atkinson), Université de Fribourg-en-Brisgau (Renkl), Louisiana State University at Shreveport : l'équipe à l'origine de l'estompage des exemples résolus. |
| **Nature** | Académique ; financement non rapporté. Les auteurs testent leur propre procédure. |
| **Support** | *Journal of Educational Psychology* (APA). |
| **Audience** | 521 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Moyenne : conditions, séquence des tâches (tableau 1, p. 777) et format des invites décrits avec des exemples d'énoncés ; logiciel et données non publiés. La démarche se refait. |

## Ce que fait l'étude

- **Contenu** : probabilités (événement, complémentaire, produit pour des événements indépendants, addition) ; deux séries de quatre tâches de trois étapes, sur ordinateur, avec un texte de cours consultable (p. 776-777).
- **Expérience 1** : 78 étudiants en psychologie, tirés au sort dans un plan 2 × 2 (19 ou 20 par groupe) : paires exemple-exercice ou estompage par la dernière étape ; avec ou sans invite. Après chaque étape à compléter, la bonne étape s'affiche (p. 776-777).
- **Invite** : à chaque étape résolue, l'étudiant choisit dans une liste le principe appliqué ; sa réponse et la bonne réponse s'affichent ensuite (p. 777).
- **Expérience 2** : 40 lycéens volontaires en algèbre avancée, estompage avec ou sans invite (20 par groupe), en salle informatique du lycée (p. 780).
- **Mesures** : test immédiat de 6 problèmes de transfert proche et 6 de transfert éloigné ; temps d'étude enregistré ; séance d'environ 90 minutes (p. 777-778).

## Résultats

- **Expérience 1** (tableau 2, p. 779-780) : l'estompage améliore le transfert proche (f = 0,23) et éloigné (f = 0,27) ; l'invite aussi (f = 0,25 et 0,23) ; pas d'interaction ; temps d'étude identique (environ 31 à 33 minutes). En d, ces effets valent environ 0,46 à 0,54 [calcul : d ≈ 2f].
- **Expérience 2** (tableau 3, p. 781) : avec l'invite, transfert proche 0,52 contre 0,30 (proportions ajustées) et éloigné 0,41 contre 0,23 ; f = 0,42 et 0,37, soit d ≈ 0,8 [calcul] ; temps d'étude identique.
- **Interprétation des auteurs** (p. 781-782) : l'effet de l'invite peut venir du choix du principe ou du retour sur ce choix ; une étude séparant les deux reste à faire.

## Avis critique

**Apport.** Montre qu'une invite très légère, choisir le principe dans une liste, ajoutée à l'estompage, améliore aussi le transfert éloigné, sans coût en temps : c'est la forme d'auto-explication la plus facile à intégrer dans un exercice en ligne.

**Points forts**
- Plan factoriel : l'estompage et l'invite sont testés séparément et ensemble.
- Effet de l'invite reproduit sur un second public (lycéens).
- Temps d'étude mesuré et égal entre conditions.

**Réserves**
1. **Importante** — L'invite associe deux choses : choisir le principe et recevoir la bonne réponse (p. 777). Les auteurs le reconnaissent (p. 781). L'effet ne peut pas être attribué au seul choix.
2. **Importante** — Une seule séance de 90 minutes et un test immédiat : pas de mesure de rétention.
3. **Importante** — Petits groupes (19 à 20) ; les effets de l'expérience 1 sont tout juste significatifs (F entre 4,5 et 6,0).
4. **Mineure** — Public de l'expérience 1 hors sciences (psychologie), contenu simple (quatre principes de probabilités).
5. **Mineure** — Le témoin de l'estompage est la paire exemple-exercice, pas la résolution seule.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Choisir le principe à chaque étape d'exemple, avec retour, améliore le transfert proche et éloigné | B | Deux essais concordants, petits groupes, séance unique |
| L'estompage arrière fait mieux que les paires exemple-exercice | B | Répliqué par l'équipe, petits groupes |

**Transférabilité** : forte pour l'invite (un menu de principes s'ajoute facilement à une étape ExoForge) ; moyenne pour l'estompage, le résultat de Moreno et al. (2009) sur un contenu facile allant dans l'autre sens.

**Pour conclure, il faudrait** séparer, dans ExoForge, le choix du principe sans retour et le choix avec retour, et mesurer à deux ou trois semaines.

## Pour Forge

- **ExoForge** : à chaque étape résolue d'un exemple, faire choisir le principe appliqué dans une liste courte, puis afficher la bonne réponse (niveau B). Même mécanisme que dans Salden et al. (2010), où ce choix sert aussi à piloter l'estompage.
- **ExoForge** : préférer l'estompage progressif aux paires exemple-exercice (niveau B), en gardant en tête la réserve de Moreno et al. (2009) pour les contenus faciles.
- À noter : la méta-analyse de Bisra et al. (2018) exclut ce format (choisir un principe sans l'expliquer) de sa définition de l'auto-explication.
