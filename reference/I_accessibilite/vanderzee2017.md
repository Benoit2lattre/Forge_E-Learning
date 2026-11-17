---
cle: vanderzee2017
reference: "van der Zee, T., Admiraal, W., Paas, F., Saab, N. et Giesbers, B. (2017). Effects of subtitles, complexity, and language proficiency on learning from online education videos. Journal of Media Psychology, 29(1), 18-30."
doi: 10.1027/1864-1105/a000208
axe: [I1]
type_etude: essai intra-sujets préenregistré en ligne (2 × 2 sous-titres × complexité, listes contrebalancées tirées au sort), analyse bayésienne
public: 125 adultes non anglophones natifs recrutés sur Prolific, 17 à 53 ans, vidéos de MOOC de biologie en anglais
lecture: texte complet, 10/11/2026
regles:
  - outil: CapsuleForge
    regle: "sous-titres identiques à la narration sur toutes les capsules : ils ne dégradent ni la réussite ni l'effort ressenti, et sont indispensables aux étudiants sourds ou malentendants"
    niveau: B
    transferabilite: moyenne
    note: "sous-titres dans la langue de la narration, spectateurs non natifs ; effet estimé 0,04 point sur 10"
  - outil: CapsuleForge
    regle: "réduire la complexité visuelle et textuelle : retirer textes et étiquettes inutiles, faire apparaître chaque étiquette quand elle est dite, signaler l'élément commenté, placer les étiquettes près de leur référent"
    niveau: B
    transferabilite: forte
    note: "quatre principes appliqués ensemble ; leurs effets séparés ne sont pas mesurés"
  - outil: ExoForge
    regle: "schémas des énoncés sans texte décoratif, étiquettes placées près de leur référent"
    niveau: C
    transferabilite: moyenne
    note: "transposé de la vidéo à la page statique"
---

# Sous-titres et complexité des vidéos de MOOC (van der Zee et al., 2017)

van der Zee, T., Admiraal, W., Paas, F., Saab, N. et Giesbers, B. (2017). Effects of subtitles, complexity, and language proficiency on learning from online education videos. *Journal of Media Psychology*, 29(1), 18-30. [DOI](https://doi.org/10.1027/1864-1105/a000208)

**En une phrase.** Chez 125 spectateurs non natifs, des sous-titres anglais identiques à la narration ne changent ni la réussite (0,04 point sur 10) ni l'effort ressenti, quel que soit le niveau d'anglais, alors qu'une vidéo visuellement épurée fait gagner 0,62 point sur 10 (d = 0,31) : pour CapsuleForge, sous-titrer sans crainte et soigner d'abord la complexité de l'image.

## La source

| | |
| --- | --- |
| **Équipe** | ICLON, université de Leyde ; université Érasme de Rotterdam (p. 18) ; thèse du premier auteur sur l'apprentissage par vidéo dans les MOOC (p. 30). |
| **Nature** | Académique ; financement non rapporté ; pas de déclaration de conflit d'intérêts. |
| **Support** | *Journal of Media Psychology* (Hogrefe), format « rapport préenregistré ». |
| **Audience** | 79 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Bonne : plan d'analyse préenregistré ; données et scripts publiés sur l'Open Science Framework (p. 23) ; vidéos modifiées non publiées. |

## Ce que fait l'étude

- **Vidéos** (p. 22) : quatre vidéos de cours Coursera (rein, histoire de la génétique, système visuel, système nerveux périphérique), environ 7 minutes, même narrateur, enseignant jamais à l'image. Chacune en 4 versions : avec ou sans sous-titres (identiques mot pour mot à la narration, en bas d'écran, sans recouvrement), complexité haute ou basse.
- **Complexité** (tableau 1, p. 22) : version simple = informations inutiles retirées, apparition progressive (segmentation), indices d'attention, étiquettes proches de leur référent ; version complexe = l'inverse.
- **Plan** (p. 22) : chaque participant voit une vidéo dans chaque condition (liste tirée au sort parmi 4) ; un seul visionnage, sans pause ; exclusion si connaissance préalable déclarée ≥ 3 sur 5.
- **Mesures** : effort mental (échelle en 9 points) ; 10 QCM factuels juste après chaque vidéo ; test de niveau d'anglais adaptatif (CECR, 15 questions).
- **Échantillon** (p. 23) : arrêt prévu quand un modèle atteint un facteur de Bayes ≥ 10 contre tous les autres, atteint à 125 participants ; 43 % de niveau C1-C2 (tableau 3, p. 24).

## Résultats

- **Modèle retenu** (tableau 5, p. 25) : complexité + niveau d'anglais, 10,3 fois plus soutenu que le même modèle avec sous-titres ; l'interaction triple prévue est 400 000 fois moins soutenue (p. 24).
- **Effets sur la note sur 10** (tableau 6, p. 26 ; p. 24) : sous-titres 0,04 point (d = 0,02, intervalle crédible de part et d'autre de zéro) ; complexité 0,62 point (d = 0,31) ; niveau d'anglais 0,55 point par niveau (d = 0,27 ; intervalle crédible à 95 % de 0,43 à 0,68), soit plus de 2,5 points entre extrêmes (p. 28). Toutes les interactions sont centrées sur zéro.
- **Effort ressenti** (p. 25-26) : sous-titres 0,015 (intervalle crédible −0,16 à 0,19) ; complexité 0,24 (0,06 à 0,41 ; d = 0,12).
- Note moyenne de 4,81 sur 10 (tableau 6) : pas d'effet plafond.

## Avis critique

**Apport.** Un résultat nul solide (préenregistré, bayésien, quantifié) sur les sous-titres dans des vidéos de contenu, et la mesure de ce que rapporte l'épuration visuelle d'une vidéo réelle.

**Points forts**
- Préenregistrement, données et scripts ouverts.
- Plan intra-sujets avec contrebalancement ; vidéos de cours réelles.
- Le nul est démontré (facteur de Bayes), pas seulement « non significatif ».

**Réserves**
1. **Importante** — La « complexité » cumule quatre manipulations (cohérence, segmentation, signalement, contiguïté spatiale) : on ne sait pas laquelle agit. Les auteurs notent que l'effet combiné (d = 0,31) est plus petit que les effets publiés de chacune (0,48 à 1,36) (p. 27).
2. **Importante** — Test immédiat de 10 QCM factuels, fiabilité non rapportée ; pas de mesure différée ni de transfert. Vidéos de biologie, pas de calcul ni de formules.
3. **Importante** — Sous-titres dans la langue de la narration pour des non-natifs ; le cas d'étudiants francophones devant une capsule en français n'est pas testé, ni des sous-titres traduits (p. 27).
4. **Mineure** — Pas de pause ni de retour en arrière, contrairement à une capsule réelle (p. 28) ; participants Prolific dont le statut d'étudiant n'est pas rapporté ; échelle d'effort dite en 9 points puis « 1 à 10 » (p. 22 et 27).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Des sous-titres identiques à la narration ne gênent pas et n'aident pas l'apprentissage factuel immédiat | B | Essai préenregistré, 125 participants, nul quantifié |
| Une vidéo épurée (4 principes ensemble) améliore la réussite immédiate | B | Même essai ; effet moyen |
| Chacun des quatre principes contribue | C | Non séparés ici |

**Transférabilité** : moyenne pour les sous-titres (langue et public différents) ; forte pour l'épuration visuelle, qui ne dépend pas de la langue.

**Pour conclure, il faudrait** produire une capsule CapsuleForge de mécanique en deux versions (schéma complet d'emblée ou étiquettes qui apparaissent au fil de la narration), tirer la version au sort et comparer un quiz différé d'une semaine.

## Pour Forge

- **CapsuleForge** : sous-titres partout, identiques à la narration (niveau B) ; confirme [vanhoecke2026](vanhoecke2026.md).
- **CapsuleForge** : épurer l'image, faire apparaître les étiquettes au fil de la narration, signaler l'élément commenté, étiquettes près du référent (niveau B pour l'ensemble).
- **ExoForge** : mêmes principes pour les schémas des énoncés (niveau C).
