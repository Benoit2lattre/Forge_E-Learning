# Forge E-Learning

```{image} ../_static/identite/bandeaux/forge_e-learning_bandeau_jour.png
:alt: Forge E-Learning — des outils pour créer quiz, exercices guidés et vidéos interactives pour Moodle, H5P et SCORM, puis en diagnostiquer la qualité
:class: only-light
```

```{image} ../_static/identite/bandeaux/forge_e-learning_bandeau_nuit.png
:alt: Forge E-Learning — des outils pour créer quiz, exercices guidés et vidéos interactives pour Moodle, H5P et SCORM, puis en diagnostiquer la qualité
:class: only-dark
```

Forge E-Learning réunit des outils libres pour passer d'un cours existant à des activités en ligne : questions Moodle, exercices guidés autonomes, chapitres de cours interactifs, puis l'analyse des résultats des étudiants. Chaque outil part d'un fichier simple (classeur Excel, fiche YAML, diaporama PowerPoint) que l'enseignant garde sous la main, relit et corrige ; le format de sortie (Moodle XML, page HTML5, paquet SCORM) est reconstruit à chaque fois.

Les outils sont écrits pour l'enseignement de la mécanique et des mathématiques en école d'ingénieurs (de la licence au master), mais rien n'y est propre à ces disciplines.

:::{note}
**Version 0.2** publiée, **0.3** en préparation. Les outils servent déjà en cours ; leur maturité est inégale. La page {doc}`etat_outils` dit, outil par outil, ce qui a été essayé en conditions réelles, ce qui est livré sans avoir encore été essayé et ce qui manque.
:::

## La démarche : de la diapositive à l'étudiant

```{image} ../_static/identite/formats/bandeaux/demarche_bandeau_jour.png
:alt: La démarche en sept étapes — concevoir, décrire, forger, exporter, intégrer, tester, analyser
:class: only-light
```

```{image} ../_static/identite/formats/bandeaux/demarche_bandeau_nuit.png
:alt: La démarche en sept étapes — concevoir, décrire, forger, exporter, intégrer, tester, analyser
:class: only-dark
```

La première étape, **concevoir le cours**, reste celle de l'enseignant : Forge part d'un cours qui existe et ne le fournit pas. Les étapes suivantes sont outillées : décrire les questions et les exercices dans un fichier, les forger, les exporter dans un format que la plateforme accepte, les intégrer, les tester comme un étudiant, puis analyser les résultats. La page {doc}`pourquoi` explique ce que Forge ajoute aux outils sur lesquels il s'appuie (Moodle, PowerPoint, ActivePresenter…).

## Les outils

```{image} ../_static/identite/bandeaux/famille_forge_bandeau_jour.png
:alt: La famille Forge — Forge E-Learning, QuizForge, ExoForge, CapsuleForge, DiagForge
:class: only-light
```

```{image} ../_static/identite/bandeaux/famille_forge_bandeau_nuit.png
:alt: La famille Forge — Forge E-Learning, QuizForge, ExoForge, CapsuleForge, DiagForge
:class: only-dark
```

| Outil | Ce qu'il fait | Mode d'emploi |
| --- | --- | --- |
| **QuizForge** | classeur Excel → questions Moodle (XML, GIFT) : huit types de questions (dont questions sur image et textes à trous), rétroactions, erreurs types visées par les leurres, contrôle de la qualité d'écriture | {doc}`../outils/quizforge/README` |
| **ExoForge** | fiche YAML → exercice guidé autonome (page HTML5 et paquet SCORM 1.2) : données tirées au hasard, formules LaTeX, diagnostic des erreurs, graphiques, audio | {doc}`../outils/exoforge/README` |
| **DiagForge** | exports Moodle → bilan : classeur, fiche du professeur, images pour les étudiants, qualité des questions, erreurs types, tirage et rétention | {doc}`../outils/diagforge/README` |
| **CapsuleForge** | diaporama narré, vidéo ou capture → chapitre de cours interactif (lecteur HTML, paquets SCORM 2004 et 1.2) : parcours, sous-titres, questions, exercices, traduction, voix de synthèse | {doc}`../outils/capsuleforge/README` |

Les outils partagent un style générique et des profils d'établissement (couleurs par rôle, polices, barème Moodle) : voir {doc}`communs`.

```{image} ../_static/identite/formats/formats_jour.png
:alt: Formats produits — SCORM, XML, HTML5, H5P
:class: only-light
:width: 80%
```

```{image} ../_static/identite/formats/formats_nuit.png
:alt: Formats produits — SCORM, XML, HTML5, H5P
:class: only-dark
:width: 80%
```

## Une bibliographie derrière chaque réglage

Les choix des outils ne sont pas des préférences : chacun s'appuie sur une lecture de la recherche en éducation. La {doc}`bibliographie <../reference/README>` est organisée en **9 axes**, compte **250 références** (`reference/forge.bib`, importable dans Zotero) et **197 fiches de lecture** écrites en français, d'où sont tirées **602 règles** adressées aux outils.

Une fiche de lecture résume un article lu en texte complet : question, public, méthode, résultats chiffrés, lecture critique (limites majeures et mineures), puis les **règles** qu'il justifie pour un outil, chacune avec un **niveau de preuve** (de A, preuve solide et répliquée, à D, indice faible ou avis d'expert) et une **transférabilité** au cas de l'enseignement scientifique en école d'ingénieurs. La méthode est décrite dans {doc}`../reference/fiches_methode`.

| Axe | Question pour les outils | Références | Fiches | Règles |
| --- | --- | ---: | ---: | ---: |
| {doc}`A — Tests et rétroaction <../reference/A_tests_retroaction/README>` | quel retour, quand, combien d'essais ? | 28 | 19 | 58 |
| {doc}`B — Conception des QCM <../reference/B_conception_qcm/README>` | comment écrire de bons leurres ? | 30 | 25 | 77 |
| {doc}`C — Analyse d'items <../reference/C_analyse_items/README>` | quels indicateurs, quels seuils ? | 25 | 10 | 25 |
| {doc}`D — Exemples guidés et guidage <../reference/D_exemples_guidage/README>` | combien d'aide, comment la retirer ? | 38 | 27 | 58 |
| {doc}`E — Multimédia <../reference/E_multimedia/README>` | audio, apparitions, découpage | 40 | 31 | 99 |
| {doc}`F — Vidéo interactive <../reference/F_video_interactive/README>` | quand interrompre une vidéo par une question ? | 26 | 20 | 66 |
| {doc}`G — Restitution aux étudiants <../reference/G_restitution/README>` | que montrer à l'étudiant de ses résultats ? | 19 | 16 | 33 |
| {doc}`H — Spécificités STEM <../reference/H_specificites_stem/README>` | paramètres aléatoires, erreurs types en mécanique | 31 | 29 | 121 |
| {doc}`I — Accessibilité <../reference/I_accessibilite/README>` | lisibilité, dyslexie, audio | 23 | 20 | 65 |

Une référence peut relever de plusieurs axes : la somme de la colonne « Références » dépasse donc 250. Les règles se répartissent entre QuizForge (152), ExoForge (178), DiagForge (143) et CapsuleForge (129) ; 2 sont de niveau A, 70 de niveau B, 372 de niveau C et 158 de niveau D. La liste complète est sur la page {doc}`bibliographie_complete`.

## Essayer

```bash
git clone https://github.com/Benoit2lattre/Forge_E-Learning.git
cd Forge_E-Learning
uv venv
uv pip install -r requirements.txt
python scripts/quizforge/quizforge.py profils
python scripts/exoforge/build.py outils/exoforge/exemples/premier_exercice
```

La seconde commande produit `dist/exoforge/premier_exercice/index.html`, à ouvrir dans le navigateur. Le bac à sable public de Moodle ([sandbox.moodledemo.net](https://sandbox.moodledemo.net), remis à zéro toutes les heures) suffit pour importer les questions et déposer les paquets SCORM.

## À propos

Forge E-Learning est un projet personnel de Benoit Delattre, enseignant-chercheur en mécanique. Code sous licence GNU GPL v3 ; documentation, exemples et site sous licence CC BY-NC-SA 4.0. Les exemples ne contiennent que des données fictives.

:::{note}
Ce site et les outils ont été écrits par Benoit Delattre. L'assistant d'IA [Claude](https://claude.ai) (Anthropic) a été utilisé pour l'écriture du code, la lecture et la synthèse de la bibliographie, l'édition et la relecture ; les choix pédagogiques et la validation des outils en cours relèvent de l'auteur.
:::
