---
cle: shoaib2023
reference: "Shoaib, M., Fitzpatrick, D. et Pitt, I. (2023). Assistive technology-based solutions in learning mathematics for visually-impaired people: exploring issues, challenges and opportunities. Multimedia Tools and Applications, 82, 46153-46184."
doi: 10.1007/s11042-023-17409-z
axe: [I2]
type_etude: revue de littérature annoncée systématique (72 articles, 1990-2023), synthèse narrative sans évaluation de qualité rapportée
public: études sur des personnes aveugles ou malvoyantes, surtout enfants et élèves ; applications pour ordinateur et téléphone
lecture: texte complet, 10/11/2026
regles:
  - outil: ExoForge
    regle: "proposer à chaque étape un bouton d'aide (indice sur la suite) accessible au lecteur d'écran, pour l'étudiant qui ne sait plus quoi faire"
    niveau: D
    transferabilite: moyenne
    note: "recommandation des auteurs (p. 46180), non testée"
  - outil: ExoForge
    regle: "offrir plusieurs accès à la même formule (voix, agrandissement, braille via le MathML) plutôt qu'un seul canal"
    niveau: D
    transferabilite: moyenne
    note: "conclusion « multimodal > unimodal » (p. 46179) sans comparaison chiffrée dans la revue"
---

# Technologies d'assistance pour apprendre les mathématiques sans la vue (Shoaib et al., 2023)

Shoaib, M., Fitzpatrick, D. et Pitt, I. (2023). Assistive technology-based solutions in learning mathematics for visually-impaired people: exploring issues, challenges and opportunities. *Multimedia Tools and Applications*, 82, 46153-46184. [DOI](https://doi.org/10.1007/s11042-023-17409-z)

**En une phrase.** Inventaire de 72 articles et d'une dizaine d'applications (lecture vocale, braille, tactile, téléphone) pour apprendre les mathématiques sans la vue, surtout chez l'enfant ; la revue conclut que ces outils aident et que les approches multimodales et sur téléphone sont prometteuses, sans pondérer la qualité des études : peu de règles utilisables pour Forge.

## La source

| | |
| --- | --- |
| **Équipe** | School of Computer Science and IT, University College Cork ; Centre for Excellence in Universal Design, National Disability Authority, Dublin (p. 46153). |
| **Nature** | Académique ; Science Foundation Ireland, subvention 18/CRT/6222 (p. 46181) ; pas de conflit d'intérêts déclaré. |
| **Support** | *Multimedia Tools and Applications* (Springer), libre accès. |
| **Audience** | 53 citations (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Faible : équations de recherche et nombre de résultats par base donnés (tableau 1, p. 46156), mais pas de liste des articles retenus par étape ni de grille de qualité appliquée. Sans objet pour les chiffres (pas de synthèse quantitative). |

## Ce que fait l'étude

- **Méthode** (p. 46155-46158) : guide de Kitchenham et Charters ; trois questions (effet des technologies, difficultés, intérêt du téléphone) ; 8 bases, 1 321 résultats bruts [calcul : somme du tableau 1] ; critères d'inclusion larges ; 72 articles retenus (p. 46158).
- **Classement** (p. 46158-46159) : études théoriques, solutions générales avec études d'usagers (tableau 2), solutions ciblées sans étude d'usagers, applications commerciales, applications sur téléphone.
- **Synthèse** : tableaux descriptifs, décompte des fonctions (voix, braille, agrandissement), modèle conceptuel (fig. 4), recommandations (p. 46179-46181).

## Résultats

- Les études d'usagers du tableau 2 portent sur de petits groupes, souvent d'enfants : par exemple 6 élèves, 2 élèves de 10 et 11 ans, 16 participants de 6 à 22 ans (p. 46162-46163).
- Toutes les applications recensées ont une fonction vocale (p. 46178) ; les difficultés citées : applications non compatibles avec le lecteur d'écran, interfaces très visuelles, navigation complexe (p. 46178-46179).
- Conclusions (p. 46179-46181) : systèmes multimodaux (voix, braille, tactile) préférés aux systèmes à un seul canal ; téléphone moins cher et plus pratique ; recommandations : module « demander de l'aide », niveaux adaptatifs, conception universelle, solutions non limitées à l'anglais.
- [mackowski2018](mackowski2018.md) est résumé comme donnant une meilleure compréhension qu'une notation braille (p. 46162) ; l'article d'origine ne fait pas cette comparaison.

## Avis critique

**Apport.** Carte des outils existants et rappel que la plupart ne fonctionnent qu'en anglais ; signale une étude plus récente de la même équipe polonaise (Maćkowski et al., 2022 : 30 lycéens, amélioration dans 4 catégories sur 11, p. 46161) à lire si l'axe est approfondi.

**Points forts**
- Recherche large sur 8 bases, équations publiées.
- Couvre ordinateur, web et téléphone.

**Réserves**
1. **Majeure** — Pas d'évaluation de la qualité des études appliquée ni de synthèse des effets : les conclusions (« les technologies d'assistance améliorent l'apprentissage », « multimodal plus efficace ») reposent sur des études de quelques participants sans groupe témoin.
2. **Importante** — Public et outils éloignés : surtout enfants, calcul et géométrie élémentaires, applications pour téléphone ; presque rien sur l'analyse, la mécanique ou le supérieur.
3. **Importante** — Résumés parfois inexacts (mackowski2018 présenté comme supérieur au braille, p. 46162).
4. **Mineure** — Diagramme de sélection sans effectifs par étape dans le texte ; recherche Scopus datée d'avril 2022, les autres de 2023 (tableau 1).

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les outils existants sont surtout vocaux et souvent limités à l'anglais | C | Inventaire descriptif |
| Les approches multimodales sont plus efficaces | D | Conclusion des auteurs sans comparaison chiffrée |
| Les technologies d'assistance améliorent l'apprentissage des mathématiques | D | Études petites, non pondérées |

**Transférabilité** : faible. Public et applications éloignés de nos étudiants.

**Pour conclure, il faudrait** une revue limitée au supérieur scientifique, qui retienne les études avec mesure de réussite et compare lecture vocale, braille et combinaison des deux.

## Pour Forge

- **ExoForge** : bouton d'aide accessible à chaque étape (niveau D) ; ExoForge a déjà des indices, à vérifier au lecteur d'écran.
- **ExoForge** : formule accessible par plusieurs canaux via le MathML (voix, agrandissement, braille) (niveau D).
- Renvois : [klingenberg2020](klingenberg2020.md) (revue voisine, mêmes petits échantillons), [frankel2017](frankel2017.md), [mackowski2018](mackowski2018.md).
