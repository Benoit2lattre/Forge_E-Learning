---
cle: segado2026
reference: "Segado, M., Adair, A., Stewart, J. et Pritchard, D. (2026). Discovering Misconceptions and Misunderstandings From Administrations of Research-Designed Multiple Choice Instruments. Prépublication arXiv:2606.08986."
doi: 10.48550/arxiv.2606.08986
axe: [H2, C]
type_etude: analyse psychométrique (modèle multidimensionnel de réponse nominale, inférence bayésienne) de passations d'un inventaire de concepts, avant et après enseignement ; prépublication non relue
public: environ 17 000 élèves et étudiants (dont environ 10 000 lycéens) en mécanique newtonienne d'introduction, États-Unis et Canada, Force Concept Inventory (30 QCM)
lecture: texte complet (corps de l'article p. 1-35 ; annexes de poids des leurres non lues en détail), 10/11/2026
regles:
  - outil: DiagForge
    regle: "score d'erreur type par étudiant = somme des poids des leurres choisis rattachés à cette erreur, divisée par la somme des poids maximaux par question (0 = aucune trace, 1 = tous les leurres les plus typiques) ; calculé sur ces seuls leurres et moyenné par classe"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "afficher pour chaque erreur type le niveau attendu si les réponses fausses étaient données au hasard parmi les leurres, à score égal, pour juger si l'erreur est fréquente ou rare"
    niveau: C
    transferabilite: forte
  - outil: DiagForge
    regle: "mesurer l'effet d'un enseignement par erreur type avec le gain normalisé 1 - m_post / m_pre, par tranche de score initial, plutôt que par le score global"
    niveau: C
    transferabilite: moyenne
  - outil: QuizForge
    regle: "en dynamique, viser chaque erreur type par plusieurs questions de contextes différents, avec des leurres codés : force dans le sens du mouvement (impetus), force motrice supérieure à la résistance à vitesse constante, réaction normale oubliée, l'objet actif ou lourd exerce la plus grande force, force centripète absente"
    niveau: C
    transferabilite: moyenne
---

# Erreurs types extraites des leurres d'un inventaire de concepts (Segado et al., 2026)

Segado, M., Adair, A., Stewart, J. et Pritchard, D. (2026). Discovering Misconceptions and Misunderstandings From Administrations of Research-Designed Multiple Choice Instruments. Prépublication arXiv:2606.08986. [DOI](https://doi.org/10.48550/arxiv.2606.08986)

Prépublication de 65 pages numérotées : les pages citées sont celles du PDF.

**En une phrase.** Sur environ 34 000 passations du Force Concept Inventory, un modèle qui donne à chaque leurre sa propre direction fait apparaître 22 erreurs types stables, chacune portée par quelques leurres de plusieurs questions ; les auteurs en tirent un score d'erreur type par étudiant et par classe, et montrent que l'enseignement réduit peu la plupart d'entre elles chez les étudiants moyens ou faibles.

## La source

| | |
| --- | --- |
| **Équipe** | Département de génie mécanique et département de physique du MIT ; département de physique et d'astronomie de West Virginia University ; recherche en didactique de la physique et psychométrie, suite d'un article de méthode du même groupe (Segado et al., 2025). |
| **Nature** | Académique ; remerciements au MIT, à son département de physique et au Center for Ultracold Atoms (p. 35) ; pas de déclaration de financement plus précise. |
| **Support** | Prépublication arXiv (physics.ed-ph), non relue. |
| **Audience** | 0 citation (OpenAlex, 10/11/2026). |
| **Reproductibilité** | Faible à moyenne : méthode et formule du score décrites (§ 5.1), poids des leurres en annexe (p. 38 et suivantes) ; données non publiques, code non publié, outil web annoncé (p. 34). La démarche se refait sur une banque assez grande ; les chiffres ne se vérifient pas. |

## Ce que fait l'étude

- **Données** (§ 3.1, p. 5) : FCI version 1995, passations avant et après enseignement d'environ 17 000 élèves ; environ 10 000 lycéens de classes « Modeling Instruction », le reste de sept établissements d'enseignement supérieur nord-américains. Exclusion de toute copie avec une question sans réponse et des doublons.
- **Modèle** (§ 2-3) : modèle multidimensionnel de réponse nominale estimé par inférence bayésienne hiérarchique, qui choisit lui-même le nombre de dimensions ; rotations comparées pour obtenir des vecteurs « creux », chacun chargé sur quelques leurres. Stabilité vérifiée entre établissements (§ 3.2.1), par rééchantillonnage (seuil de corrélation 0,85, p. 16) et sur les données avant et après enseignement séparément.
- **Score d'erreur type** (§ 5.1, p. 27) : poids des leurres (charges du modèle, avec une zone morte de ±0,2) ; somme des poids des leurres choisis divisée par la somme, sur toutes les questions, du poids le plus fort de chaque question. Score moyen par tranche de score initial (30 quantiles, groupes de 456 à 1 659 étudiants, p. 28), gain normalisé ⟨g⟩ = 1 - ⟨m_post⟩ / ⟨m_pre⟩ et niveau de référence « réponses au hasard » (p. 28).

## Résultats

- **Dimensions** (résumé, p. 1 ; tableau 4, p. 20) : 21 dimensions extraites ; 22 vecteurs stables nommés, rangés par époque historique (antique, médiévale, post-newtonienne). Exemples : force appliquée supérieure à la résistance pour une vitesse constante ; force d'impetus le long d'une trajectoire rectiligne ou circulaire ; la dernière force reçue fixe le mouvement ; la bille deux fois plus lourde tombe deux fois plus vite ; réaction normale oubliée, souvent avec la pesanteur ; l'agent actif ou massif exerce la plus grande force (3e loi) ; force centripète absente ; vitesse et accélération confondues sur un diagramme de mouvement.
- **Stabilité** (tableau 4 ; § 4.5, p. 26) : 4 des 44 corrélations médianes avant et après enseignement sont sous 0,85 ; « force centripète absente » n'est bien définie qu'après enseignement.
- **Fréquence avant enseignement** (§ 5.3.1, p. 29) : score initial médian 9,0 et moyen 9,8 sur 30 ; les erreurs « fortes » (force supérieure à la résistance, les quatre formes d'impetus, force centripète absente) dépassent souvent 0,5 chez les étudiants faibles et ne décroissent qu'au-delà d'un score initial d'environ 13.
- **Effet de l'enseignement** (§ 5.3.2, p. 29) : hors erreurs « naïves », le gain normalisé moyen part de 0,17 pour les scores initiaux les plus bas et culmine à 0,70 vers un score initial de 20 ; pour plus de la moitié des vecteurs, l'écart entre ce pic et les plus faibles dépasse 0,3. Les erreurs « naïves » ont un gain d'environ 0,5 quel que soit le niveau (0,52 à score nul, 0,51 à 15). Le texte annonce huit erreurs naïves ; le tableau 4 en marque neuf « NM » [décompte].

## Avis critique

**Apport.** Une méthode pour passer des leurres d'un QCM à des erreurs types nommées, chacune portée par plusieurs questions, et un score simple par erreur et par classe : c'est le diagnostic par erreur type que DiagForge vise, ici sur un très grand échantillon.

**Points forts**
- Très grand échantillon, avant et après enseignement, plusieurs établissements.
- Stabilité vérifiée de trois façons (établissements, rééchantillonnage, avant et après).
- Score par erreur type défini sur les seuls leurres concernés, comparé à un niveau de hasard.

**Réserves**
1. **Importante** — Prépublication non relue, avec des choix de rotation et de nommage en partie subjectifs (les auteurs le disent, § 3.5.3) ; légère incohérence entre le texte et le tableau 4 sur le nombre d'erreurs naïves.
2. **Importante** — Le score d'erreur type n'est validé contre aucun critère externe (entretiens, explications écrites) ; il ne peut trouver que les erreurs prévues par les leurres du FCI (p. 33).
3. **Importante** — Les comparaisons avant et après enseignement mêlent des établissements et des pédagogies différents, sans groupe témoin : le gain par erreur décrit, il n'évalue pas un enseignement.
4. **Mineure** — Public d'introduction (surtout lycée) ; nos étudiants de L3 à M2 ont dépassé ce niveau, sauf en remédiation.

**Niveau de preuve**

| Affirmation | Niveau | Raison |
| --- | --- | --- |
| Les leurres du FCI se regroupent en une vingtaine d'erreurs types stables | C | Grand échantillon, stabilité vérifiée, prépublication |
| Score par erreur type utilisable par classe | C | Méthode décrite, non validée contre un critère externe |
| L'enseignement réduit peu les erreurs « fortes » chez les étudiants moyens et faibles | C | Description sur données agrégées, sans témoin |
| Utilité pour orienter une remédiation | D | Proposition des auteurs, non testée |

**Transférabilité** : moyenne. La méthode de score se transpose à toute banque où chaque leurre code une erreur type ; le modèle bayésien demande des milliers de passations, que nos promotions n'atteignent pas : on reprendra un rattachement des leurres fixé par l'enseignant.

**Pour conclure, il faudrait** calculer dans DiagForge le score par erreur type (poids fixés par l'enseignant) sur un quiz de dynamique passé en début et fin de semestre, et vérifier sur un échantillon d'étudiants, par une explication écrite, que le score élevé correspond bien à l'erreur annoncée.

## Pour Forge

- **DiagForge** : score par erreur type sur les seuls leurres rattachés, normalisé de 0 à 1, par étudiant et par classe, avec le niveau attendu au hasard (niveau C) ; gain normalisé par erreur type et par tranche de score initial (niveau C). Prolonge les sous-scores par concept de [Steif et Hansen (2006)](steif2006.md).
- **QuizForge** : en dynamique, chaque erreur type visée par plusieurs questions de contextes différents, leurres codés sur les erreurs de la liste ci-dessus (niveau C). Rejoint [Martín-Blas et al. (2010)](martinblas2010.md) et [Poutot et Blandin (2015)](poutot2015.md) pour le FCI en école d'ingénieur.
