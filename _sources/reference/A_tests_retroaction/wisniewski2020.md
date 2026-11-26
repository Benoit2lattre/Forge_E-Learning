---
cle: wisniewski2020
reference: "Wisniewski, B., Zierer, K. et Hattie, J. (2020). The power of feedback revisited: A meta-analysis of educational feedback research. Frontiers in Psychology, 10, article 3087."
doi: 10.3389/fpsyg.2019.03087
axe: [A2]
type_etude: méta-analyse (435 études, 994 effets, plus de 61 000 participants) à partir des 32 méta-analyses de Visible Learning
public: tous niveaux, de la maternelle à l'université ; part du supérieur non rapportée
lecture: texte complet, 09/11/2026
regles:
  - outil: QuizForge
    regle: "rétroaction riche en information (ce qui est faux, pourquoi, comment faire la prochaine fois) plutôt que juste/faux, note seule ou message d'encouragement"
    niveau: C
    transferabilite: moyenne
    note: "rétroaction riche d = 0,99, corrective d = 0,46, renforcement ou punition d = 0,24 (comparaison entre études)"
  - outil: ExoForge
    regle: "rétroaction riche en information (ce qui est faux, pourquoi, comment faire la prochaine fois) plutôt que juste/faux, note seule ou message d'encouragement"
    niveau: C
    transferabilite: moyenne
  - outil: DiagForge
    regle: "restitution aux étudiants : éviter les retours sans information (récompense, classement, note seule) ; associer toute note à une information sur la tâche"
    niveau: C
    transferabilite: moyenne
    note: "21 % des effets sur la motivation sont négatifs, dont 86 % avec un retour non informatif"
---

# L'effet de la rétroaction revisité (Wisniewski et al., 2020)

Wisniewski, B., Zierer, K. et Hattie, J. (2020). The power of feedback revisited: A meta-analysis of educational feedback research. *Frontiers in Psychology*, 10, article 3087. [DOI](https://doi.org/10.3389/fpsyg.2019.03087)

**En une phrase.** En reprenant une à une les études des méta-analyses de Visible Learning, l'effet moyen de la rétroaction tombe à d = 0,48 (contre 0,79 dans la synthèse de Hattie et Timperley), avec une très forte hétérogénéité ; il dépend surtout de la quantité d'information du retour (d = 0,99 pour une rétroaction riche, 0,24 pour récompense ou punition). Pour Forge : un argument général pour une rétroaction informative, pas un réglage précis.

## La source

| | |
| --- | --- |
| **Équipe** | Pédagogie scolaire, université d'Augsbourg ; école supérieure d'éducation de Melbourne. J. Hattie est l'auteur de la synthèse que l'article réexamine. |
| **Nature** | Académique ; financement non rapporté ; pas de conflit d'intérêts déclaré (p. 14). Synthèse méta-analytique ; les auteurs revoient leurs propres travaux antérieurs. |
| **Support** | *Frontiers in Psychology* (section psychologie de l'éducation), libre accès. |
| **Audience** | 1723 citations (OpenAlex, 09/11/2026). |
| **Reproductibilité** | Moyenne : liste des études en annexe en ligne, méthode décrite (p. 3-7), paquets R cités ; codage fait sur les résumés des études (p. 7), données de codage non publiées. Les pages citées sont celles de l'article (1 à 14). |

## Ce que fait l'étude

- **Sélection** (p. 3-5, tableau 1) : études primaires tirées de 32 méta-analyses ; critères : comparaison expérimentale ou avant-après, données suffisantes pour un d, mesure d'apprentissage (connaissances, motivation, comportement), contexte éducatif. Pas d'exigence de tirage au sort.
- **Analyse** (p. 5-7) : modèle à effets aléatoires, estimation robuste de la variance pour les effets d'un même échantillon, Q, I², graphique en entonnoir et test d'Egger, exclusion des valeurs extrêmes (résidus > 2).
- **Modérateurs** (p. 7) : plan d'étude, type de publication, type de mesure, type de rétroaction (renforcement ou punition ; corrective : juste/faux et bonne réponse ; riche en information : corrective plus information sur la stratégie ou l'autorégulation), canal (oral, écrit, vidéo, audio ou ordinateur), sens (enseignant vers élève, etc.).

## Résultats

- **Corpus** (p. 7) : 732 études repérées, 435 retenues, 994 effets ; année médiane de publication 1985 ; 15 % des effets publiés dans les 15 dernières années.
- **Effet global** (p. 7, 9) : d = 0,55 [0,48 ; 0,62], 17 % d'effets négatifs, I² = 86 % ; après exclusion de 35 valeurs extrêmes, d = 0,48 [0,44 ; 0,51], I² = 83 %. Modèle à effet fixe : 0,41 (p. 11).
- **Biais de publication** (p. 9) : entonnoir asymétrique (Egger z = 9,52, p < 0,001), asymétrie limitée aux articles de revue ; pas d'estimation corrigée.
- **Modérateurs** (tableaux 2 et 3, p. 11) :

| Sous-groupe | k | d [IC 95 %] |
| --- | --- | --- |
| Études avec groupe témoin | 713 | 0,42 [0,37 ; 0,46] |
| Études avant-après | 244 | 0,63 [0,56 ; 0,69] |
| Mesure cognitive | 597 | 0,51 [0,46 ; 0,55] |
| Mesure de motivation | 109 | 0,33 [0,23 ; 0,42] |
| Renforcement ou punition | 39 | 0,24 [0,06 ; 0,43] |
| Rétroaction corrective | 238 | 0,46 [0,39 ; 0,55] |
| Rétroaction riche en information | 42 | 0,99 [0,82 ; 1,15] |

- **Canal** (p. 10, 12) : non significatif ; valeurs par canal non données dans le texte, donc rien sur la rétroaction par ordinateur en particulier.
- **Motivation** (p. 12) : 21 % des effets sur la motivation sont négatifs, et 86 % des interventions concernées donnent un retour non informatif (récompense ou punition).

## Avis critique

**Apport.** Corrige à la baisse le chiffre de 0,7-0,8 souvent cité pour la rétroaction, et fait de la quantité d'information du retour le modérateur principal. Utile comme cadre général ; ne dit rien du moment, du nombre d'essais ni du support numérique.

**Points forts**
- Retour aux études primaires, doublons retirés, effets pondérés par leur précision.
- Hétérogénéité et asymétrie rapportées sans les cacher.
- Distinction utile entre mesures cognitives et de motivation.

**Réserves**
1. **Majeure** — Biais de publication détecté (Egger) mais non corrigé : d = 0,48 est probablement surestimé. Le d des études avec groupe témoin (0,42) est plus prudent.
2. **Importante** — Le type de rétroaction n'est codé que pour 319 effets sur 959 [calcul : 39 + 238 + 42] et à partir des seuls résumés ; la comparaison des types est une comparaison entre études, pas causale.
3. **Importante** — Corpus ancien (médiane 1985), tous niveaux et domaines confondus (musique, sport, langues) ; pas de modérateur niveau d'enseignement ni moment du retour.
4. **Mineure** — τ² non rapporté : intervalle de prédiction impossible à calculer ; avec I² = 83 %, l'effet d'une rétroaction donnée peut être nul ou très fort.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| La rétroaction a en moyenne un effet positif moyen sur l'apprentissage | B | Méta-analyse large mais biais de publication non corrigé |
| Plus le retour contient d'information, plus il est efficace | C | Modérateur entre études, codage sur résumés |
| Un retour non informatif peut nuire à la motivation | C | Décompte descriptif des effets négatifs |

**Transférabilité** : moyenne. Le principe (informer sur la tâche et la façon de faire) se transpose ; les valeurs chiffrées, issues surtout du scolaire et d'études anciennes, non.

**Pour conclure, il faudrait** une méta-analyse limitée au supérieur et aux retours automatiques, avec correction du biais de publication ; la fiche [vanderkleij2015](vanderkleij2015.md) répond en partie pour les environnements numériques.

## Pour Forge

- **QuizForge, ExoForge** : rétroaction qui dit ce qui est faux, pourquoi et comment faire (niveau C) ; elle confirme, sans les préciser, les règles déjà tirées de [vanderkleij2015](vanderkleij2015.md) et [heckler2016](heckler2016.md).
- **DiagForge** : dans la restitution, ne pas envoyer de note ou de classement sans information sur la tâche (niveau C).
- Ne pas citer d = 0,48 comme l'effet attendu d'un quiz Moodle : la valeur dépend du type de retour et du contexte.
