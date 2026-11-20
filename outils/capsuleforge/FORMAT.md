# CapsuleForge — le fichier `chapitre.yaml` d'une capsule

Une capsule (un cours interactif ou un didacticiel) est décrite par un seul fichier, `chapitre.yaml`, rangé avec ses médias (`images/`, `audio/`) ; sa première ligne utile est `format: capsuleforge/2`. Il remplace l'ancien `capsule.yaml` (étapes et pas à action unique), que `capsuleforge convertir` (« Mettre à jour pour le lecteur actuel » dans l'Atelier Forge) reprend sans perte.

Statut : format écrit et vérifié par `scripts/capsuleforge/format_chapitre.py` (conversion, noms, plan par parcours, contrôles), lu par le lecteur de chapitre (`lecteur_chapitre.html`, construit par `construire_chapitre.py`). L'éditeur visuel lit encore l'ancien `capsule.yaml`.

## Les quatre niveaux

| Niveau | Rôle | Nom affiché |
| --- | --- | --- |
| Chapitre | le fichier : titre, langues, écran, réglages, parcours | |
| Partie | un bloc cohérent : `tronc`, `annexe` ou `exercice` | `B` |
| Section | 5 à 6 min au plus ; c'est l'« étape » d'un didacticiel | `B-S2` |
| Pas | une scène : un fond et ce qui s'y passe | `B-S2-P4` |

Les noms affichés suivent la place dans le fichier : lettre de la partie, rang de la section, rang du pas joué. Un pas écarté prend une décimale (`B-S2-P4.1`). Chaque partie, section et pas garde par ailleurs un `id` fixe, qui sert aux renvois et ne change jamais.

## Exemple commenté

```yaml
format: capsuleforge/2
titre: "Dimensionnement fiabiliste : la méthode Contrainte-Résistance"
langues: {source: fr, autres: [en]}
ecran: {largeur: 1440, hauteur: 1080}       # pixels des fonds
vue: [0, 40, 1440, 1000]                    # cadrage commun (facultatif) : [x, y, largeur, hauteur]
reglages:
  modes: [regarder, a_vous]                 # ce que le lecteur propose
  essais: 3                                 # essais avant de montrer la zone
  trajectoire: arc                          # ou « enregistree »
  retours: {juste: "Oui.", faux: "Pas tout à fait.", indice_apres: essais}   # messages par défaut
masques: [[0, 1534, 2558, 69]]              # zones floutées sur tous les fonds

parcours:                                   # des filtres sur le même contenu
  - {id: ensemble,  titre: "Vue d'ensemble",    annexes: aucune,       questions: proposees}
  - {id: detaillee, titre: "Lecture détaillée", annexes: a_la_demande, questions: proposees}
  - {id: immersive, titre: "Lecture immersive", annexes: integrees,    questions: obligatoires, exercices: true}
variantes:                                  # publics : même principe que les parcours
  - {id: ecole1, titre: "École 1"}

parties:
  - id: introduction
    titre: Introduction
    type: tronc                             # tronc | annexe | exercice
    place: debut                            # debut (ouvre le chapitre) | libre (ordre au choix) | fin
    sections: [...]
  - id: dimensionnement
    titre: Dimensionnement fiabiliste
    type: tronc
    place: libre
    prerequis: [introduction]
    sections:
      - id: defaillance
        titre: Probabilité de défaillance
        objectif: Relier l'écart entre Contrainte et Résistance à un risque
        source: {fichier: diaporama_source.pptx, diapos: [11], duree_s: 111}
        narration: |                        # le scénario ; ou {fr: "…", en: "…"}
          La défaillance survient quand la Contrainte dépasse la Résistance…
        audio: audio/defaillance.mp3        # facultatif
        arret: true                         # arrêt en fin de section
        ouverture: "À votre avis, que vaut le risque quand les deux moyennes sont égales ?"
        questions:                          # fin de section : renvois à la banque QuizForge
          - {banque: fiabilite_banque.yaml, id: Q12}
          - {banque: fiabilite_banque.yaml, etiquette: defaillance, nombre: 1}
        annexes: [lois_normales]            # annexe annoncée à la fin de cette section, avec retour ici
        pas:
          - id: p011
            fond: images/d11_e3.png         # diapositive, capture, image ; ou une courte vidéo
            vue: [200, 300, 900, 600]       # zoom sur ce pas (facultatif)
            source: {type: pptx, diapo: 11, etat: 3}
            phrases:                        # cours : le texte dit, phrase par phrase, calé sur le son
              - {debut_s: 0.85, fin_s: 11.2, texte: "Pour calculer cette probabilité de défaillance…"}
              - {debut_s: 12.2, fin_s: 20.2, texte: "Nous retenons des distributions gaussiennes."}
            duree_s: 12.5                   # durée en mode « regarder » ; absente = calculée
            objets:                         # chacun avec son début et sa durée dans le pas
              - {id: o1, type: spot, cadre: [620, 410, 240, 120], debut_s: 3.2, duree_s: 4}
              - {id: o2, type: bulle, texte: "L'aire commune mesure le risque : $P_f$", position: [700, 560]}
              - {id: o3, type: bouton, texte: "Voir le calcul", ouvre: lois_normales, parcours: [detaillee]}
  - id: lois_normales
    titre: Lois normales et indice de fiabilité
    type: annexe
    parcours: [detaillee, immersive]        # absent = tous les parcours
    exercice: {outil: exoforge, fiche: fiabilite_indice.yaml}
    sections: [...]
```

Un pas de didacticiel porte en plus les gestes attendus et les retours :

```yaml
          - id: p021
            fond: images/p021.png
            source: {type: captation, duree_ms: 2540, processus: FreeCAD.exe}
            objets:
              - {id: bulle, type: bulle, texte: "Validez avec **Entrée** ou un clic sur **OK**", position: [672, 924]}
            gestes:                         # n'importe lequel valide le pas ; le premier est montré en mode « regarder »
              - {type: touche, touches: Entrée}
              - {type: clic, zone: [1150, 882, 120, 48]}
            a_vous: {observer: false, indice: false}
            retours: {juste: "La cote est enregistrée dans la liste des contraintes.", faux: "Le champ est encore ouvert."}
          - id: p016
            ecarte: true                    # gardé dans le fichier, absent du lecteur
            raison: saisie partie dans la vue
            fond: images/p016.png
```

## Référence des champs

**Chapitre** : `format`, `titre`, `langues` (`source`, `autres`), `ecran` (`largeur`, `hauteur`, `echelle`), `vue`, `source`, `reglages` (`modes`, `essais`, `trajectoire`, `retours`), `masques`, `affichage` (format de la zone d'image du lecteur, `16:9` par défaut ; les fonds y sont calés sans déformation), `parcours`, `variantes`, `parties`, `image_finale`, `cameo` (`position` : `bas-droite` par défaut, `bas-gauche`, `haut-droite`, `haut-gauche`, ou `aucune` : webcam gardée mais non montrée ; `taille` : part de la largeur de l'image, 0,22 par défaut ; `forme` : `rond` ou `rectangle` ; écrit par `capsuleforge cameo`).

**Parcours** : `id`, `titre`, `annexes` (`aucune`, `a_la_demande`, `integrees`), `questions` (`aucune`, `proposees`, `obligatoires`), `exercices`.

**Partie** : `id`, `titre`, `type`, `place`, `prerequis`, `parcours`, `variantes`, `exercice`, `sections`.

**Exercice** (sur une partie, seul ou en liste) : `outil` (`exoforge`, valeur par défaut), `fiche` (fiche ExoForge, cherchée à côté du chapitre puis dans `data/exoforge`), `titre` (sinon celui de la fiche), `objectif`, `duree_min` (sinon 1,5 min par étape de la fiche), `poids` dans la note SCORM (une question pèse 1 ; par défaut la durée en minutes ; 0 = hors note). À la construction, la fiche est construite par ExoForge si besoin et l'exercice devient la dernière section de la partie (nom `B-Ex`). Une annexe peut ainsi porter du cours et un exercice ; une partie de type `exercice` peut n'avoir aucune section. L'exercice n'est proposé que par les parcours `exercices: true` ; il est appelé comme une annexe (`annexes: [id]` sur une section). Le lecteur l'affiche dans un cadre et lui sert d'API SCORM 1.2 : l'exercice compte comme fait quand il est terminé, avec son score (meilleur, dernier, nombre de fois) et ses réponses gardés dans le navigateur.

**Section** : `id`, `titre`, `objectif`, `source`, `narration`, `audio`, `arret`, `ouverture`, `questions`, `annexes`, `variantes`, `sauf`, `pas`.

**Pas** : `id`, `fond`, `fond_pour`, `vue`, `source`, `narration`, `phrases` (`debut_s`, `fin_s`, `texte`, `variantes`, `sauf`, `pour`, `audio_pour`), `variantes`, `sauf`, `audio`, `duree_s`, `voix`, `objets`, `gestes`, `a_vous` (`observer`, `indice`), `retours` (`juste`, `faux`), `ecarte`, `raison`.

**Pas vidéo** : `video` = `{fichier: videos/<nom>.mp4, debut_s, fin_s}` (extrait de la vidéo joué pendant le pas) ; le pas garde `fond` (image d'affiche), `audio` (son de l'extrait, horloge du pas), `duree_s`, `phrases` et `objets` comme une diapositive ; `source: {type: video, fichier, debut_s, fin_s}` (instants dans le fichier d'origine). Écrit par `capsuleforge video`. `camera` = `{fichier: videos/<nom>_camera.mp4, debut_s, fin_s}` : webcam filmée en même temps (caméo), même découpage que `video` (écrit par `capsuleforge filmer --webcam`) ; le lecteur la montre en médaillon, calée sur la vidéo (bouton « Caméo », touche V) ; `position`, `taille` et `forme` sur un pas remplacent ceux du chapitre.

**Langues** : tout texte (titre, objectif, ouverture, texte d'une phrase, narration, texte d'un objet) peut être une chaîne (langue source) ou `{fr: …, en: …}` ; `langues.autres` liste les langues traduites (écrit par `traduire --importer`). `voix.<langue>` d'un pas (écrit par `capsuleforge voix`) : `audio`, `duree_s`, `phrases` (une paire [début, fin] par phrase du pas, dans le son synthétisé), `moteur`, `nom`, `empreinte` (texte + voix : refait si elle change), `date`. Un pas dont le son source est synthétisé porte `source.voix: synthese` (et `voix_moteur`, `voix_nom`, `voix_empreinte`).

**Objet** : `id`, `type`, `forme` (`ellipse` pour un spot ou un cadre ; rectangle sinon), `texte`, `position`, `cadre`, `trajet`, `ouvre`, `fichier`, `couleur`, `debut_s`, `duree_s`, `origine`, `modes`, `parcours`. Types : `bulle`, `texte`, `formule`, `cadre`, `spot`, `fleche`, `pointeur`, `image`, `video`, `bouton`, `apparition`, `cache`.

**Geste** : `type`, `zone`, `point`, `arrivee`, `crans`, `texte`, `accepte`, `tolerance`, `touches`, `cible` (`nom`, `type`, `origine`, `dans`), `trajectoire`, `trajet`. Types : `clic`, `double_clic`, `clic_droit`, `clic_milieu`, `glisser`, `molette`, `saisie`, `touche`.

Un texte (titre, narration, bulle, retour) est une chaîne dans la langue source, ou un dictionnaire par langue.

**Variantes** : une capsule reste nue (aucun établissement nommé) ; ce qui ne vaut que pour un public (une école, un client) le dit, et la construction le retient ou non selon la variante (`construire --variante psa`, ou celle de la déclinaison du cours avec `--cours`) :

| Clé | Sur | Effet |
| --- | --- | --- |
| `variantes: [psa]` | partie, section, pas, phrase | seulement pour ces variantes ; absent de la capsule nue |
| `sauf: [psa]` | partie, section, pas, phrase | retiré pour ces variantes |
| `pour: {psa: "…"}` | phrase | autre texte pour cette variante (sous-titres, texte de la section) |
| `audio_pour: {psa: audio/….wav}` | phrase | son de remplacement de la phrase ; sans lui, le son dit encore l'ancienne phrase (signalé) |
| `fond_pour: {psa: images/….png}` | pas | autre image pour cette variante |
| `{zone: [x, y, l, h], variantes: […]}` ou `sauf` | masque | zone floutée selon la variante |

Une phrase retirée coupe son extrait de narration (de son début au début de la suivante) dans le son du pas et dans les voix de synthèse des autres langues ; les phrases, apparitions et objets qui suivent sont recalés. Un pas vidéo garde son film : seuls ses sous-titres changent. Dans l'écran de relecture, le bouton « Public » de chaque phrase règle `variantes`, `sauf` et `pour`.

## Règles

- L'introduction (`place: debut`) ouvre le chapitre, la conclusion (`place: fin`) le ferme ; les parties `libre` se suivent dans l'ordre choisi par l'étudiant.
- Une annexe est appelée depuis une section (`annexes:`) ou depuis un bouton d'un pas (`ouvre:`). Selon le parcours, elle est absente, ouverte à la demande ou insérée à son premier point d'appel.
- Un pas sans geste se regarde ; un pas avec gestes se refait en mode « à vous ».
- Les retours par défaut sont ceux des réglages ; un pas ne les redéfinit que s'il le mérite.
- Le texte dit pendant un pas est porté par ses `phrases` horodatées : c'est la seule source de la narration et des sous-titres. `narration` ne sert qu'à un pas sans son (scénario écrit avant l'enregistrement) ; `capsuleforge relire` la découpe en phrases et la retire.
- Un `pointeur` qui porte un `trajet` (liste de points) parcourt cette ligne brisée pendant sa durée. `origine: pptx` marque un objet dessiné dans PowerPoint (forme nommée « cf spot », « cf cadre », « cf pointeur ») : `capsuleforge pptx` relit sa forme et garde ses réglages de temps.
- Un `spot` éclaire son `cadre` et assombrit le reste (plusieurs spots au même instant percent le même voile) ; un `pointeur` est un point lumineux à sa `position` ; un `cache` recouvre son `cadre` de sa `couleur` depuis le début du pas et pendant `duree_s` : il sert à faire apparaître plus tard une zone que le diaporama montre d'emblée.
- Les `questions` d'une section renvoient à une banque QuizForge (`…_banque.yaml`), cherchée à côté du chapitre puis dans `data/quizforge` : `id` désigne une question par son titre, `etiquette` toutes celles qui portent ce tag, `nombre` combien en tirer au hasard (toutes par défaut). Le lecteur joue les types vrai/faux, QCM et numérique.
- Durée d'une section : celle de la source si elle est connue, sinon le plus long de la narration (150 mots par minute) et de la somme des pas. Au-delà de 6 min, `verifier` le signale.

## Commandes

```
capsuleforge convertir tuto1                  capsule.yaml -> chapitre.yaml (l'original n'est pas touché)
capsuleforge plan fiabilite                   plan par parcours : noms, durées, annexes, questions
capsuleforge plan fiabilite --parcours immersive --variante ecole1
capsuleforge relire fiabilite                 relecture dans le navigateur : son, texte phrase par phrase, apparitions
capsuleforge verifier fiabilite               contrôles des deux formats
```

## Correspondance avec l'ancien `capsule.yaml`

| `capsule.yaml` | `chapitre.yaml` |
| --- | --- |
| `etapes` | les `sections` d'une partie unique `principale` |
| `pas.image` | `pas.fond` |
| `pas.action` + `cible.cadre` + `point`… | premier élément de `pas.gestes` (`type`, `zone`, `point`…) |
| `pas.ou` | éléments suivants de `pas.gestes` |
| `pas.bulle`, `bulle_position` | objet `bulle` (`texte`, `position`) |
| `action: montrer` | pas sans geste, objet `cadre` |
| `lecture_s` | `duree_s` |
| `ignorer`, `raison` | `ecarte`, `raison` |
| `observer`, `indice` | `a_vous` |
| `retour_juste`, `retour_faux` | `retours` |
| `reglages.mode` | `reglages.modes` |
| `duree_ms`, `processus` | `source` du pas |

Licence : GPL v3 (code), CC BY-NC-SA (contenus).
