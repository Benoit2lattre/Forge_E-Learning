# ExoForge

<p><img src="../../_static/identite/bandeaux/exoforge_bandeau_jour.png#gh-light-mode-only" alt="ExoForge" class="only-light" width="100%"><img src="../../_static/identite/bandeaux/exoforge_bandeau_nuit.png#gh-dark-mode-only" alt="ExoForge" class="only-dark" width="100%"></p>

ExoForge construit un exercice interactif à partir d'une fiche texte (YAML) : une page HTML autonome, qui s'ouvre dans n'importe quel navigateur, et un paquet SCORM 1.2 à déposer dans Moodle. L'exercice enchaîne des étapes (explication, question à choix, réponse numérique) à côté d'un encadré permanent (énoncé, tableau, graphique, formules) ; il peut tirer ses données au hasard, diagnostiquer les erreurs prévisibles et être commenté à l'oral.

![Un exercice ExoForge (profil Ecole1) : encadré permanent, graphique généré, question avec retour](../../_static/captures/exoforge/exercice_question.png)

Code : [`scripts/exoforge/`](https://github.com/Benoit2lattre/Forge_E-Learning/tree/main/scripts/exoforge). Installation : [README du dépôt](https://github.com/Benoit2lattre/Forge_E-Learning#installation).

## En 3 minutes

```bash
python scripts/exoforge/build.py outils/exoforge/exemples/premier_exercice
```

| Sortie (dans `dist/exoforge/`, non suivi) | Usage |
| --- | --- |
| `premier_exercice/index.html` | l'exercice : à ouvrir dans le navigateur pour le tester |
| `premier_exercice_scorm12.zip` | à déposer dans Moodle : Ajouter une activité › Paquetage SCORM ; la note est transmise au carnet de notes |

![SCORM : un paquet standard qui transmet la progression et la note](../../_static/identite/formats/bandeaux/scorm_bandeau_jour.png)

### Déposer l'exercice dans Moodle

1. Dans le cours, mode édition : **Ajouter une activité ou une ressource › Paquetage SCORM**.
2. Donnez un nom, une description, puis déposez `…_scorm12.zip` dans « Paquetage ». Enregistrez.
3. L'activité propose **Aperçu** (essai sans note) et **Entrer** ; les réglages (nombre de tentatives, méthode d'évaluation, note reportée au carnet) se trouvent dans « Paramètres ».

| Ajouter l'activité | Déposer le paquet |
| --- | --- |
| ![Ajouter une activité : Paquetage SCORM](../../_static/captures/exoforge/moodle_ajout_activite.png) | ![Formulaire du paquetage SCORM](../../_static/captures/exoforge/moodle_paquet_scorm.png) |
| **L'activité** | **L'exercice dans Moodle (aperçu)** |
| ![Page de l'activité SCORM](../../_static/captures/exoforge/moodle_activite_scorm.png) | ![Aperçu de l'exercice dans Moodle](../../_static/captures/exoforge/moodle_apercu_scorm.png) |

Options de `build.py` (l'extension `.yaml` peut être omise) :

| Option | Rôle |
| --- | --- |
| `-p Ecole1` | profil : couleurs, polices, jeu de couleurs LaTeX (nom, alias ou première lettre) ; sinon le `profil:` de la fiche, sinon le profil par défaut |
| `--cours traction:ecole1-meca` | profil de l'école de l'édition (cours d'AtelierForge), si `-p` n'est pas donné ; le paquet SCORM est aussi rangé comme version de l'édition, jamais écrasée (`…/<édition>/exercices/<id>/v2/<id>_v2_scorm12.zip`, avec `version.yaml`), et inscrit à son registre ; une construction identique (même fiche, mêmes médias, même profil) n'en crée pas |
| `-a` | mode auteur intégré à la page (emplacements audio, relevé des temps, données tirées, avertissements) |

Pour tester la page sans reconstruire : `index.html?auteur` (mode auteur), `?mode=fixe` (données d'origine de la fiche), `?seed=12` (un tirage précis, pour reproduire ce qu'a vu un étudiant).

## Écrire une fiche

Partez de [`exemples/premier_exercice.yaml`](exemples/premier_exercice.yaml), la fiche minimale ci-dessous, puis des trois exemples complets. Rangez vos fiches où vous voulez ; `data/exoforge/` n'est pas publié.

```yaml
id: premier_exercice                    # nom des sorties et du dossier des médias
titre: "Exercice : contrainte dans une barre en traction"
cours: "Résistance des matériaux — Traction simple"
auteur: "Benoit Delattre"
profil: Delattre

donnees:                                # tirées à chaque ouverture
  tirage:
    F: {parmi: [10, 15, 20, 25, 30]}      # kN
    d: {parmi: [10, 12, 16, 20]}          # mm
  calculs:
    S: "pi*d**2/4"
    sigma: "F*1000/S"
  fixe: {F: 20, d: 16}                  # données d'origine (?mode=fixe)

rappel:                                 # encadré permanent, à gauche
  titre: "Énoncé"
  texte: >-
    Une barre cylindrique de diamètre d = {=d} mm est tendue par un effort F = {=F} kN.
    <b>Quelle est la contrainte normale dans la barre ?</b>
  formules:
    - tex: '\sigma = \dfrac{F}{S}'

etapes:
  - id: unite
    type: choix
    titre: "Question 1 : unités"
    enonce: "Avec F en newtons et S en mm², la contrainte F / S s'exprime en :"
    options:
      - {texte: "MPa", correct: true}
      - {texte: "Pa", retour: "1 N/m² = 1 Pa, mais ici la section est en mm²."}
      - {texte: "kPa", retour: "1 N/mm² = 10<sup>6</sup> N/m², soit 1 MPa."}
    explication: "1 N/mm² = 1 MPa."

  - id: contrainte
    type: numerique
    titre: "Question 2 : contrainte"
    enonce: "Calculez la contrainte normale σ (en MPa)."
    attendu: "sigma"
    erreurs:                            # diagnostic des erreurs prévisibles
      - {si: "F/S", message: "F est en kN : convertissez-le en N."}
      - {si: "F*1000/(pi*d**2)", message: "La section d'un disque est πd²/4."}
    indice: "S = π × {=d}² / 4 = {=round(S)} mm²."
    solution: "σ = {=F*1000} N / {=round(S)} mm² = <b>{=round(sigma*10)/10} MPa</b>"

defauts:
  tentatives: 3
  points_par_tentative: [1, 0.75, 0.5]
  tolerance: 0.02                       # écart relatif accepté
```

![Diagnostic d'une erreur prévisible sur une réponse numérique](../../_static/captures/exoforge/exercice_diagnostic.png)

### Étapes (`etapes`)

Chaque étape a un `id` (unique) et un `type`.

| Type | Contenu | Clés utiles |
| --- | --- | --- |
| `info` | blocs de contenu et bouton « Continuer » | `contenu`, `suite_auto: true` (suite à la fin de l'audio), `mises_en_evidence: [{t, fin, cible}]` (cadre lumineux sur un élément), `sous_titres: [{t, texte}]` |
| `choix` | une ou plusieurs bonnes réponses | `options` (`texte`, `correct`, `retour`, `pose: {variable: valeur}`, `aller_a: <id>`), `plusieurs: true`, `correct: <expression>` (bonne réponse calculée), `retour_juste` / `retour_faux`, `explication`, `note: false` (question non notée : estimation, confiance), `options_une_par_une: true` (propositions lues à l'oral) |
| `numerique` | réponse saisie, tolérante (`0,25`, `1/4`, `2.5e-3`) | `attendu` (expression), `tolerance`, `erreurs: [{si, message}]`, `indice`, `solution`, `aide: {texte, graphique}` (rappel de méthode sur demande) |

Pour toutes : `tentatives`, `points_par_tentative`, `repeter: 3` (répète l'étape avec k = 0, 1, 2 et i = k + 1), `si: <expression>` (étape affichée seulement si la condition est vraie), `audio: <emplacement>`, `focus_rappel: <id>` (met en évidence un élément de l'encadré), `ajoute_au_rappel` (complète la zone « modèle » de l'encadré : `remplace`, `apres`, `exergue`), `fin: {graphique: …}` (pilote le graphique à la fin de l'étape).

**Blocs de contenu** : `texte`, `liste`, `formule` (avec `legende`), `image` (avec `alt`), `graphique` (même écriture que le graphique de l'encadré, voir plus bas : un graphique propre à l'étape, piloté comme lui).

**Fin de l'exercice** (`conclusion`) : `titre`, `recommencer: true` (ou le texte du bouton) pour refaire l'exercice avec de nouvelles données.

### Encadré permanent (`rappel`)

Toujours visible à gauche : `texte`, `image`, `tableau` (lignes calculées), `graphique`, `formules`, et une zone `modele` qui se remplit au fil des étapes.

**Graphique** (dans l'encadré ou dans une étape) :

- `id`, `largeur` et `hauteur` (pixels, 540 × 330 par défaut), `alt`, `description` (texte affiché sous le graphique et lu à voix haute, pour l'accessibilité ; `{texte, voix}` si la version lue diffère) ;
- axes `x` et `y` : `titre`, `log`, `min`, `max`, `pas` (bornes et pas calculables, ex. `max: "Rm"`) ;
- `courbes` : `{id, y: <f(x)>, etiquette, position_etiquette, couleur, epaisseur, pointilles, cachee}`. `position_etiquette` place l'étiquette le long de la courbe (de 0 à 1 ; 0,15 par défaut) ; `couleur` accepte un code (`"#748CAB"`) ou une couleur de rôle du profil (`"var(--graphique)"`, `"var(--erreur)"`…) ; `epaisseur` en pixels (3 par défaut, 1,5 en pointillés) ; une courbe `cachee` n'apparaît que quand une étape la montre ; une expression qui vaut `NaN` interrompt la courbe ;
- `points` : une série `{x, y, …}` ou une liste de séries. `x` et `y` sont des expressions qui donnent une valeur ou une liste (`"[muC]"`, `"[0.55*M, 0.58*M]"`) ; chaque série a `id`, `couleur`, `etiquette` (`{j}` : rang du point dans la série), `position_etiquette: gauche`, `marque: false` (étiquette seule, sans losange : utile pour nommer une zone), `apparait: revele` (point caché jusqu'à ce qu'une étape le révèle) et `lecture: {x, etiquette}` (pointillés de lecture vers les axes). Les points sont numérotés à la suite d'une série à l'autre, à partir de 0.

Les étapes pilotent les graphiques : `graphique: {actif, lecture, revele, montre, si}` à l'affichage de l'étape, `fin: {graphique: …}` une fois l'étape réussie. `actif` entoure un point ; `lecture` et `revele` prennent un numéro de point ou une liste ; `montre` prend le nom d'une courbe cachée ; `si` réserve l'action à une condition.

```yaml
contenu:
  - graphique:
      id: plan
      largeur: 420
      x: {titre: "Contrainte C (kN)", min: 0, max: "M"}
      y: {titre: "Résistance R (kN)", min: 0, max: "M"}
      courbes:
        - {id: egal, y: "x", couleur: "var(--erreur)", epaisseur: 2, etiquette: "C = R", position_etiquette: 0.8}
      points:
        - {x: "[muC]", y: "[muR]", etiquette: "moyennes"}                     # point n° 0
        - {x: "[cP]", y: "[cP]", etiquette: "P", apparait: revele}            # point n° 1
        - {x: "[0.6*M]", y: "[0.1*M]", etiquette: "Défaillance", marque: false}
      description: "Plan contrainte-résistance ; la droite C = R sépare la sécurité de la défaillance."
fin: {graphique: {revele: 1}}          # P apparaît quand l'étape est réussie
```

![Profil Delattre : données tirées, graphique en échelle logarithmique, choix du parcours](../../_static/captures/exoforge/exercice_profil_delattre.png)

### Données et valeurs calculées (`donnees`)

- `constantes`, `tirage` (`parmi` : liste ; ou `min`, `max`, `pas`), `calculs` (dans l'ordre), `rejeter_si` (nouveau tirage si la condition est vraie), `fixe` (données d'origine).
- Dans tous les textes, `{=expr}` affiche une valeur calculée : `{=n[k]}`, `{=round(N[k])}`. Fonctions : `sum`, `prod`, `round`, `floor`, `ceil`, `abs`, `min`, `max`, `log10`, `ln`, `exp`, `sqrt`, `pow`, `pi`, `fmt` (nombre à la française). Les accolades LaTeX ne sont pas touchées.

### Formules LaTeX

Les formules (`$…$` dans les textes, `tex:` dans les blocs) sont rendues par MathJax, embarqué dans la page (fonctionne hors ligne). Vos macros IguanaTeX sont reprises telles quelles :

```yaml
latex:
  fichiers: [ppt_commandes.tex]         # cherché à côté de la fiche, puis dans style/latex/ et les profils
  macros:
    hu: '\vect{\hat{U}}'
```

Le profil choisit le jeu de couleurs (`\TR`, `\TB`… et les commandes de rôle `\TDef`, `\TRes`, `\TAtt`… : voir [style/](../../style/README.md)). En YAML, écrivez les textes contenant du LaTeX entre apostrophes ou en bloc (`tex: |-`, `texte: >-`).

### Comportement par défaut (`defauts`)

`tentatives`, `points_par_tentative`, `tolerance`, `ordre_options` (`melange` ou `fixe`), `suite` (`bouton` : « Continuer » ; `auto` : l'étape suivante s'ouvre dès la correction). Chaque étape peut les remplacer.

**Accessibilité** : `accessibilite: {lecture_vocale: true}` ajoute un bouton « Écouter » (synthèse vocale) sur les cartes sans enregistrement ; chaque graphique a une description textuelle.

## Ajouter l'audio : deux temps

1. **Construction sans média.** L'exercice fonctionne tel quel. La construction écrit `script_enregistrement.md` dans le dossier des médias : chaque emplacement audio, le texte de la fiche à lire, les apparitions numérotées et les emplacements facultatifs.
2. **Reprise.** Déposez les fichiers dans le dossier des médias (majuscules indifférentes), puis reconstruisez :
   - `<emplacement>.mp3` (ou `.m4a`, `.wav`, `.ogg`), ou découpé en segments, un par apparition : `<emplacement>_a1.mp3`, `_a2`… ;
   - `<emplacement>.txt` : transcription, affichée sous l'étape ;
   - `<emplacement>.reperes.json` : temps d'apparition relevés en mode auteur ;
   - facultatifs : `<id>_explication`, `<id>_retour_<lettre>`, `<id>_aide`.

Dossier des médias : `data/exoforge/media/<id>/` s'il existe (enregistrements non publiés), sinon `media/<id>/` à côté de la fiche.

**Mode auteur** (`-a` ou `index.html?auteur`) : emplacement audio de chaque étape ; « Pointer les apparitions » pendant l'écoute (Espace : marquer ; Retour arrière : annuler ; ← : reculer de 5 s) ; données tirées ; avertissements de construction.

**Enregistrer avec Audacity** : un projet par exercice, un titre de piste par emplacement (`presentation`, `q1_a1`…), puis export groupé (Fichier › Exporter › Exporter plusieurs) dans le dossier des médias.

**Sons** (facultatif) : `charte.sons: {juste: …, faux: …}` dans le profil ; `sons: false` dans une fiche pour les couper.

## Exemples ([`exemples/`](https://github.com/Benoit2lattre/Forge_E-Learning/tree/main/outils/exoforge/exemples))

| Fiche | Montre |
| --- | --- |
| `premier_exercice.yaml` | fiche minimale : données tirées, question à choix, réponse numérique avec diagnostic |
| `fatigue_haigh_goodman.yaml` | contrainte moyenne : tableau et diagramme de Haigh calculés, droite de Goodman, point qui apparaît, coefficient de sécurité |
| `miner_cumul_generique.yaml` | cumul de Miner : estimation non notée, choix du parcours (seul ou guidé), étapes répétées, graphique logarithmique, audio |

```bash
python scripts/exoforge/build.py outils/exoforge/exemples/fatigue_haigh_goodman -p Ecole1
```
