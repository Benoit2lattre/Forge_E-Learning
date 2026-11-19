---
cle: noetel2021
reference: "Noetel, M., Griffith, S., Delaney, O., Harris, N. R., Sanders, T., Parker, P., del Pozo Cruz, B. et Lonsdale, C. (2021, en ligne ; 2022). Multimedia design for learning: An overview of reviews with meta-meta-analysis. Review of Educational Research, 92(3), 413-454."
doi: 10.3102/00346543211052329
axe: [E1, E2, E3]
type_etude: revue de revues systématiques avec méta-méta-analyse (29 revues, 1 189 études ; 11 revues retenues pour la méta-méta-analyse, 808 tailles d'effet)
public: tous publics (école, université, adultes) ; le niveau d'études ne modère pas les effets
lecture: texte complet (version JSTOR), figure 3 lue en image, 08/11/2026
regles:
  - outil: CapsuleForge
    regle: "appliquer par défaut, dans cet ordre de priorité, la contiguïté (mot et image ensemble dans le temps et l'espace), le signalement, la voix sur image plutôt que le texte lu, la segmentation et la suppression des détails décoratifs"
    niveau: B
    transferabilite: forte
    note: "effets moyens de 0,33 à 0,74 selon le principe ; qualité des revues sources inégale"
  - outil: CapsuleForge
    regle: "soigner davantage la conception des capsules à rythme imposé et des contenus complexes (beaucoup d'éléments en interaction), où les principes comptent le plus"
    niveau: C
    transferabilite: forte
    note: "rythme imposé g = 0,41 contre 0,27 en rythme libre ; contenu complexe 0,70 contre 0,20"
  - outil: CapsuleForge
    regle: "attendre d'un principe multimédia un effet petit à moyen (g de 0,2 à 0,4 en général), pas les effets supérieurs à 1 des premières revues narratives"
    niveau: B
    transferabilite: forte
---

# Revue des revues sur la conception multimédia (Noetel et al., 2021)

Noetel, M., Griffith, S., Delaney, O., Harris, N. R., Sanders, T., Parker, P., del Pozo Cruz, B. et Lonsdale, C. (2021, en ligne ; 2022). Multimedia design for learning: An overview of reviews with meta-meta-analysis. *Review of Educational Research*, 92(3), 413-454. [DOI](https://doi.org/10.3102/00346543211052329)

**En une phrase.** En rassemblant 29 revues systématiques (1 189 études), les auteurs trouvent 11 principes de conception multimédia avec un effet positif sur l'apprentissage, d'environ g = 0,38 en moyenne, les plus forts pour les sous-titres en langue étrangère, la contiguïté et le signalement ; c'est la carte d'ensemble qui fixe les priorités de CapsuleForge, avec la mise en garde que les revues sources sont de qualité inégale.

## La source

| | |
| --- | --- |
| **Équipe** | Institut de psychologie positive et d'éducation, université catholique australienne (Noetel, Lonsdale, Parker) ; université du Queensland ; université du Danemark du Sud. Équipe extérieure aux laboratoires qui ont formulé les principes. |
| **Nature** | Académique ; financement non rapporté dans la version lue. |
| **Support** | *Review of Educational Research* (AERA). |
| **Audience** | 258 citations (OpenAlex, 08/11/2026). |
| **Reproductibilité** | Bonne : protocole PRISMA, termes de recherche et 674 tailles d'effet extraites en double en annexes en ligne (non consultées), analyses en R (metaSEM). Pas d'enregistrement préalable mentionné. La démarche se refait. |

## Ce que fait l'étude

- **Sélection** (p. 421-423) : revues systématiques ou méta-analyses comparant un même support avec et sans un principe de conception ; ERIC, PsycINFO, Scopus, Web of Science (janvier et décembre 2020) ; tri en double.
- **Qualité** (p. 423-424) : grille abrégée tirée d'AMSTAR 2 (recherche complète, tri en double, hétérogénéité, biais de publication...).
- **Analyse** (p. 424-425) : pour chaque principe, la revue la plus grande seule est retenue (éviter de compter deux fois les mêmes études) ; méta-analyse multiniveau à effets aléatoires sur les effets poolés des revues ; modérateurs : type de mesure, rythme, connaissances préalables, complexité (interactivité des éléments), niveau d'études, support, discipline.

## Résultats

| Principe (figure 3, p. 433) | g [IC 95 %] | k | Revue source |
| --- | --- | --- | --- |
| Sous-titres de vidéo en langue étrangère | 0,99 [0,60 ; 1,38] | 15 | Montero Perez et al., 2013 |
| Intégration et contiguïté | 0,74 [0,67 ; 0,82] | 46 | Ginns, 2006 |
| Signalement | 0,43 [0,35 ; 0,50] | 209 | [schneider2018](schneider2018.md) |
| Modalité (voix plutôt que texte écrit) | 0,38 [0,33 ; 0,43] | 86 | Reinwein, 2012 |
| Couleurs agréables, traits humains | 0,35 [0,29 ; 0,42] | 45 | Brom et al., 2018 |
| Segmentation | 0,34 [0,30 ; 0,38] | 123 | [rey2019](rey2019.md) |
| Personnalisation du langage | 0,33 [0,23 ; 0,44] | 55 | Ginns et al., 2013 |
| Suppression des détails séduisants | 0,33 [0,18 ; 0,48] | 68 | Sundararajan et Adesope, 2020 |
| Animation | 0,23 [0,12 ; 0,33] | 61 | Berney et Bétrancourt, 2016 |
| Agent pédagogique | 0,19 [0,12 ; 0,26] | 43 | Schroeder et al., 2013 |
| Redondance verbale | 0,15 [0,08 ; 0,22] | 57 | [adesope2012](adesope2012.md) |
| **Moyenne** | **0,38 [0,27 ; 0,49]** | 808 | 11 revues, 66 553 participants |

- **Rétention et transfert** (p. 425) : effets presque identiques (0,42 et 0,43) ; le type de mesure ne modère pas.
- **Détails** (p. 434-437) : contiguïté temporelle g = 0,78 (k = 13, Ginns 2006), illustrée par « une puce à la fois pendant que l'orateur en parle » ; modalité ramenée à 0,20 après correction du biais de publication ; animation utile seulement si elle montre un mouvement porteur de sens (0,40), décorative nulle (−0,05) ; redondance utile quand on ajoute du texte à une narration (0,29), pas quand on ajoute une narration à un texte (−0,04).
- **Charge cognitive** (p. 426, 434) : petite amélioration moyenne (g = 0,22).
- **Modérateurs** (p. 438) : rythme imposé 0,41 contre rythme libre 0,27 ; contenu complexe 0,70 contre simple 0,20 ; pas de modération par les connaissances préalables, le niveau d'études, le support ni la discipline.
- **Qualité des revues** (p. 438, 445-446) : 2 revues sur 29 rapportent un tri en double, une seule évalue la qualité des études primaires (adesope2012), 20 sur 29 testent le biais de publication, souvent avec des méthodes peu fiables.

## Avis critique

**Apport.** Donne une échelle commune pour hiérarchiser les principes et ramène les attentes à des effets petits à moyens (p. 443). Le niveau d'études et la discipline ne changent pas les effets, ce qui autorise à appliquer ces principes en L3-M2.

**Points forts**
- Méthode de revue systématique complète, travail en double.
- Une seule revue par principe : pas de double comptage.
- Évaluation explicite de la qualité des revues.

**Réserves**
1. **Importante** — La méta-méta-analyse combine les effets moyens des revues sans reprendre leur hétérogénéité interne (I² ≈ 90 % ou plus dans rey2019 et schneider2018 [calcul dans ces fiches]) : les intervalles étroits de la figure 3 sous-estiment l'incertitude pour une capsule donnée.
2. **Importante** — Qualité des revues sources faible sur plusieurs critères (p. 445-446) ; certaines sont anciennes (contiguïté : Ginns 2006 ; modalité : 2012) et l'effet de modalité baisse de moitié après correction du biais.
3. **Mineure** — Le modérateur « complexité » repose sur 4 effets poolés ; les comparaisons de modérateurs restent entre études.
4. **Mineure** — Incohérence d'effectif : 78 177 participants dans le résumé, 79 415 dans les résultats (p. 425).
5. **Mineure** — Recommandations pratiques (p. 443-444) plus larges que les données (traits humains sur des concepts abstraits, par exemple).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Contiguïté, signalement, modalité, segmentation améliorent l'apprentissage | B | Plusieurs méta-analyses concordantes, mais qualité inégale et hétérogénéité non reportée |
| Les principes comptent plus en rythme imposé et pour les contenus complexes | C | Modérateurs entre revues, peu d'effets poolés |
| Le niveau d'études ne modère pas les effets | C | Absence d'effet sur des données agrégées |

**Transférabilité** : forte. Synthèse multidisciplinaire, sans modération par le niveau ni la discipline.

**Pour conclure, il faudrait** tester dans CapsuleForge une capsule « tous principes appliqués » contre une capsule « diaporama lu » sur un même contenu de mécanique, puis retirer les principes un à un.

## Pour Forge

- **CapsuleForge** : liste de contrôle par défaut, par ordre d'effet : texte et figure au même endroit et au même moment ; signalement ; voix sur image ; segmentation ; pas de décor (niveau B).
- **CapsuleForge** : priorité de conception aux capsules à rythme imposé et aux notions complexes (niveau C).
- **CapsuleForge** : annoncer aux enseignants des gains attendus modestes (niveau B).
- Renvois : [mayer2017](mayer2017.md) et [mayer2021](mayer2021.md) (mêmes principes, présentation par le fondateur), [liu2022](liu2022.md), [adesope2012](adesope2012.md).
