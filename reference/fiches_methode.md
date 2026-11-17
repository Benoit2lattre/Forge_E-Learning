# Comment les fiches de lecture sont écrites

Une fiche n'est écrite que pour un article qui justifie un choix dans un outil Forge (QuizForge, ExoForge, DiagForge, CapsuleForge). Elle est rédigée à partir du texte complet, pas du résumé : chaque chiffre renvoie à une page ou à un tableau de l'article.

## Plan d'une fiche

1. **En une phrase** : ce que l'article montre et ce qu'on en tire pour Forge.
2. **La source** : équipe, nature (académique, industrielle, financement), support, audience (citations, avec la date et la source), reproductibilité.
3. **Ce que fait l'étude** : public, dispositif, conditions comparées, mesures.
4. **Résultats** : les chiffres utiles, avec leur page.
5. **Avis critique** : apport, points forts, réserves graduées (majeure, importante, mineure), niveau de preuve des affirmations clés, transférabilité à nos étudiants.
6. **Pour Forge** : les règles de conception qu'on en tire, outil par outil, avec leur niveau de preuve.

Un chiffre recalculé à la lecture (taille d'effet, intervalle) est signalé « [calcul] » avec les données sources. Une information absente de l'article est notée « non rapporté ».

## Grille de lecture critique

| Question | Ce qu'on vérifie |
| --- | --- |
| **La bonne mesure ?** | La mesure correspond-elle à l'apprentissage visé : transfert proche ou éloigné, test immédiat ou différé, procédure ou concept ? |
| **Une comparaison équitable ?** | Les groupes ne diffèrent-ils que par la variable étudiée ? Même temps, même nombre d'exercices, même retour ? Tirage au sort individuel ou par classe ? |
| **Généralisable ?** | Public (école, lycée, université, ingénierie), discipline, durée (une séance ou un semestre), laboratoire ou classe réelle. |
| **Quelle incertitude ?** | Effectifs par groupe, tailles d'effet et intervalles, tests unilatéraux, comparaisons multiples, abandons en cours d'étude, effets plafond ou plancher. |
| **Reproductible ?** | Matériel publié, données disponibles, logiciel accessible, protocole assez décrit pour être refait. |

## Niveaux de preuve

| Niveau | Définition |
| --- | --- |
| **A — Établi** | Plusieurs essais randomisés indépendants concordants, ou méta-analyse de qualité dont le résultat résiste aux corrections de biais de publication. |
| **B — Étayé** | Un essai randomisé bien conduit (effectifs suffisants, une seule variable changée, mesure différée ou de transfert). |
| **C — Indicatif** | Un essai petit, court ou en laboratoire ; une variable confondue ; une comparaison entre études plutôt qu'à l'intérieur d'une étude. |
| **D — Conjectural** | Interprétation des auteurs non testée, ou extrapolation hors du domaine étudié. |

On abaisse d'un niveau pour un public éloigné du nôtre, une séance unique, une variable confondue ou de fortes pertes d'effectif. On relève d'un niveau pour un effet grand et répliqué dans des contextes différents.

La **transférabilité** à nos étudiants (L3 à M2, mécanique et mathématiques, travail en ligne en autonomie) est donnée à part : forte, moyenne ou faible. Un mécanisme peut se transposer alors que la valeur chiffrée ne se transpose pas.

## En-tête des fiches

Chaque fiche commence par un en-tête YAML. Le champ `regles` liste les règles de conception tirées de l'article, sous une forme lisible par un programme : il sert à vérifier les outils Forge par rapport à la bibliographie.

```yaml
regles:
  - outil: ExoForge
    regle: "retour immédiat après chaque étape plutôt qu'en fin d'exercice"
    niveau: C
    transferabilite: forte
```
