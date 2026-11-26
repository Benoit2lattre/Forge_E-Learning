# Axe H — Spécificités STEM

Question pour les outils : que change le contenu (mathématiques de l'ingénieur, mécanique) pour les questions paramétrées, les erreurs types et le retour ?

## Vue d'ensemble

Une question de mécanique ou de mathématiques de l'ingénieur ne s'écrit pas comme une question de culture générale. La réponse se calcule, souvent en plusieurs étapes ; les valeurs de l'énoncé peuvent être tirées au hasard pour donner à chaque étudiant sa propre version ; et les réponses fausses ne sont pas quelconques : elles viennent d'erreurs types (oublier une force, permuter sinus et cosinus, partager une charge également entre deux appuis) que l'on peut reconnaître et commenter. Cet axe étudie ces trois points : l'évaluation en ligne à paramètres aléatoires (H1), les conceptions erronées propres à la mécanique et les inventaires de concepts qui les mesurent (H2), le diagnostic des erreurs types et le retour ciblé (H3).

L'idée qui relie les trois sous-axes est simple : une réponse fausse est une information. Un leurre de QCM qui code une erreur réelle devient, dans une question paramétrée, une formule fausse (en anglais *mal-rule*) dont on calcule la valeur avec les paramètres tirés ; si l'étudiant saisit cette valeur, on sait quelle erreur il a probablement faite et on peut lui répondre sur cette erreur. Pour les outils Forge, cela touche ExoForge (exercices HTML/SCORM paramétrés avec retours : formules fausses, report d'erreur entre étapes, contrôle des tirages), QuizForge (quiz Moodle construits depuis des classeurs Excel : leurres issus d'erreurs nommées, réglage du retour) et DiagForge (analyse des résultats et restitution : part de chaque leurre, score par concept ou par erreur type). CapsuleForge, qui pose des questions QuizForge et des exercices ExoForge dans ses chapitres de cours interactifs, reprend ces leurres et ces formules fausses.

Le public visé est celui de Forge : étudiants de L3 à M2 en mécanique et mathématiques, qui travaillent en ligne. Les études lues portent surtout sur la première et la deuxième année (statique, dynamique, mécanique newtonienne, algèbre), parfois sur des collégiens ou des lycéens. Les règles qui suivent sont donc transposées vers nos niveaux ; elles sont surtout des règles de conception, rarement des effets démontrés sur l'apprentissage.

## Historique du domaine

**Années 1980-1990 : l'erreur comme règle.** La psychologie cognitive et la psychométrie cessent de voir les erreurs comme du bruit. [Tatsuoka (1983)](tatsuoka1983.md) relie les profils de réponses à des règles erronées dans la théorie des réponses aux items (méthode de l'espace des règles, *rule space*). [Payne et Squibb (1990)](payne1990.md) décrivent les erreurs d'algèbre de collégiens par des règles fausses exécutables : elles sont nombreuses, la plupart rares, et un même élève ne les applique pas à chaque occasion.

**2005-2012 : la mécanique de l'ingénieur s'outille.** Sur le modèle du Force Concept Inventory (FCI), test de 30 QCM de mécanique newtonienne venu de l'enseignement de la physique, des enseignants d'ingénierie construisent des inventaires de concepts dont chaque leurre code une erreur type : statique ([Steif et Dantzler, 2005](steif2005.md)), dynamique ([Gray et al., 2005](gray2005.md)). Des entretiens explorent la résistance des matériaux ([Brown et al., 2007](brown2007.md)) et le diagramme du corps isolé ([Rosengrant et al., 2009](rosengrant2009.md)) ; le FCI entre dans les écoles d'ingénieurs ([Martín-Blas et al., 2010](martinblas2010.md)). À Brunel, [Gill et Greenhow (2007)](gill2007.md) combinent paramètres aléatoires, erreurs types tirées des copies et retour ciblé en mécanique. [Gross et Dinehart (2012)](gross2012.md) classent des milliers de copies de statique en erreurs conceptuelles, d'exécution et hors mécanique.

**2013-2020 : le passage à l'échelle.** Les systèmes de calcul formel intégrés à Moodle (WIRIS, STACK, Numbas) servent à des milliers d'étudiants ([Gaona et al., 2018](gaona2018.md)) ; [Greenhow (2015)](greenhow2015.md) fait le bilan de quinze ans de questions paramétrées. Le projet UWE recense les erreurs types de première année en mathématiques d'ingénieur ([Sikurajapathi et al., 2020](sikurajapathi2020.md)). Les premières mesures d'effet d'un retour sur les erreurs apparaissent, en statique ([Steele et al., 2014](steele2014.md)) et en programmation ([Qian et Lehman, 2019](qian2019.md)). Une école d'ingénieurs française publie ses résultats au FCI ([Poutot et Blandin, 2015](poutot2015.md)).

**2021-2026 : bilans et modèles de langage.** Un programme de recherche de 55 questions ouvertes sur l'évaluation en ligne en mathématiques paraît ([Kinnear et al., 2022](kinnear2022.md)) ; une revue fait le point sur les inventaires de concepts en ingénierie ([Fakiyesi et al., 2024](fakiyesi2024.md)). Les grands modèles de langage (LLM) servent désormais à formuler des hypothèses d'erreur à partir des résultats de quiz ([Parker et Zavala-Cerna, 2026](parker2026.md)) et à exécuter des catalogues de formules fausses (Chen et al., 2026, prépublication). Les travaux récents sur les conceptions erronées en mécanique au niveau L3-M2 restent rares.

## H1 — Évaluation paramétrée en mathématiques et mécanique de l'ingénieur

Tirer les valeurs de l'énoncé au hasard donne une question par étudiant, mais oblige l'auteur à écrire toute la structure algébrique du problème, y compris les méthodes fausses qu'il veut reconnaître. [Gill et Greenhow (2007)](gill2007.md) et [Greenhow (2015)](greenhow2015.md) le font pour la mécanique : leurres et valeurs fausses reconnues viennent des copies d'examen. Le piège est qu'avec certains tirages une formule fausse donne la bonne valeur ([Sikurajapathi et al., 2023](sikurajapathi2023.md)) : il faut contrôler chaque tirage contre chaque erreur codée.

Pour les calculs longs, le report d'erreur (recalculer l'étape suivante à partir de la valeur saisie par l'étudiant) évite de noter en tout ou rien ([Pearson et Penna, 2022](pearson2022.md) ; [Orthaber et al., 2020](orthaber2020.md), en mécanique, sans données). Le passage à l'échelle révèle des problèmes plus terre à terre : réponses justes refusées parce qu'écrites autrement, saisies mal interprétées ([Davies et al., 2024](davies2024.md)), et stratégie des étudiants qui recommencent un quiz dès la première erreur quand le retour est immédiat ([Gaona et al., 2018](gaona2018.md)). Les grandes questions encore ouvertes sont recensées par [Kinnear et al. (2022)](kinnear2022.md).

## H2 — Conceptions erronées en mécanique et inventaires de concepts

La statique est le cas de référence : l'inventaire de statique (27 QCM, 9 concepts de 3 questions) a des leurres qui codent chacun une erreur relevée chez les étudiants, et quelques leurres y dominent ([Steif et Dantzler, 2005](steif2005.md) ; [Steif et Hansen, 2006](steif2006.md)). Ses résultats se restituent par concept ([Steif et Hansen, 2006b](steif2006b.md)), et des QCM courts suivis d'une discussion des erreurs s'accompagnent de meilleurs scores sur les thèmes travaillés ([Steele et al., 2014](steele2014.md)).

Au-delà de la statique, la couverture s'amincit : inventaire de dynamique ([Gray et al., 2005](gray2005.md)), entretiens en résistance des matériaux ([Brown et al., 2007](brown2007.md)), copies classées en statique ([Gross et Dinehart, 2012](gross2012.md)) et en hyperstatique de 3e et 4e année ([Bruhl et al., 2022](bruhl2022.md)), lien entre diagramme du corps isolé et réussite ([Rosengrant et al., 2009](rosengrant2009.md)), QCM de 3e année ([Ford et al., 2020](ford2020.md)). Pour la mécanique du point, le FCI montre les mêmes erreurs dominantes d'un groupe à l'autre, y compris dans une école française ([Martín-Blas et al., 2010](martinblas2010.md) ; [Poutot et Blandin, 2015](poutot2015.md) ; [Segado et al., 2026](segado2026.md), prépublication). La psychométrie de ces inventaires est rarement vérifiée par leurs utilisateurs ([Fakiyesi et al., 2024](fakiyesi2024.md)).

## H3 — Diagnostic des erreurs types et retour ciblé

La méthode est la même partout : relever les erreurs dans les copies ou les brouillons, coder chacune comme une formule fausse qui fonctionne avec les paramètres tirés, lui associer un retour ([Gill et Greenhow, 2008](gill2008.md) ; [Sikurajapathi et al., 2020](sikurajapathi2020.md)). Ses limites sont connues depuis [Payne et Squibb (1990)](payne1990.md) : le catalogue est long, local et jamais complet, et un étudiant n'applique pas son erreur à chaque occasion. Le retour doit donc nommer l'erreur de cette réponse, pas étiqueter l'étudiant, et le diagnostic se faire sur plusieurs questions ([Tatsuoka, 1983](tatsuoka1983.md) ; [Klingbeil et al., 2024](klingbeil2024.md)).

Les mesures d'effet restent minces : un message par erreur fréquente est suivi de plus de corrections à l'essai suivant, en programmation ([Qian et Lehman, 2019](qian2019.md)). Les modèles de langage peuvent proposer des hypothèses d'erreur à partir des réponses fausses les plus choisies, que l'enseignant doit valider ([Parker et Zavala-Cerna, 2026](parker2026.md)).

## Ce que disent les fiches

Synthèse rédigée à partir des 29 fiches de lecture écrites (14 de priorité 1, 15 de priorité 2). Elle ne dit que ce que ces fiches soutiennent ; le niveau de preuve suit l'échelle de [fiches_methode.md](../fiches_methode.md). Aucune étude de l'axe ne compare, par tirage au sort des étudiants, un retour ciblé sur l'erreur à un retour général : les règles sont surtout de conception (niveaux B à D). Les fiches de priorité 2 apportent les premières mesures d'effet, toutes quasi expérimentales (point 6).

**1. Les erreurs types se recueillent dans les copies et se codent en formules.** Les leurres et les réponses fausses reconnues se construisent à partir des erreurs relevées dans des copies ou des brouillons ([Gill et Greenhow, 2007](gill2007.md) ; [Gill et Greenhow, 2008](gill2008.md) ; [Greenhow, 2015](greenhow2015.md) ; niveau C). Sur un examen en ligne de première année, 40 erreurs types couvrent 17 des 19 questions, l'erreur principale expliquant souvent 30 à 70 % des réponses fausses ([Sikurajapathi et al., 2020](sikurajapathi2020.md), niveau C). En statique, la moitié des erreurs relevées dans 1 493 copies sont des erreurs d'exécution, 38 % sont hors mécanique et 13 % seulement conceptuelles ([Gross et Dinehart, 2012](gross2012.md), niveau C). *Apport des P2 : règle confirmée et nuancée.* Le catalogue s'étend à l'hyperstatique de 3e et 4e année, résolue par 11 à 12 % des élèves : l'erreur dominante est de ne pas reconnaître le type de problème (équilibre seul, charge partagée également), à côté du moment d'encastrement oublié ; il faut une famille « aucune piste » pour les copies abandonnées ([Bruhl et al., 2022](bruhl2022.md), niveau C). En algèbre, 99 règles fausses sont nécessaires, quelques-unes dominent et elles changent d'une école à l'autre : le catalogue doit être local, ouvert, écrit sous forme condition -> action et garder une catégorie « non diagnostiquée » ([Payne et Squibb, 1990](payne1990.md), niveau C). Sans catalogue, des concepteurs débutants se rabattent sur une solution rédigée générale ([Davies et al., 2024](davies2024.md), niveau C).

**2. Une bonne réponse peut cacher une erreur type ; une réponse juste peut être refusée.** Avec certains paramètres, une règle fausse donne la bonne valeur : 27 des 47 règles erronées décrites réussissent -16 - (-8) ([Tatsuoka, 1983](tatsuoka1983.md)) ; des tirages font coïncider la clé et une erreur type à la précision demandée ([Sikurajapathi et al., 2023](sikurajapathi2023.md)). Le problème existe (niveau B, propriété logique) ; sa fréquence n'est pas mesurée. En QCM, des options mal découpées laissent un raisonnement faux mener à la bonne réponse ([Ford et al., 2020](ford2020.md), niveau C), et 35 % des explications de la bonne option d'une question d'algèbre montrent le raisonnement erroné ([Klingbeil et al., 2024](klingbeil2024.md), niveau C). *Apport des P2 : nouveau risque, symétrique.* La correction automatique se trompe aussi dans l'autre sens : des réponses justes écrites sous une autre forme (4/2 pour 2) sont refusées, ce qui fait perdre confiance aux étudiants ; il faut tester ces faux négatifs avant diffusion et soigner la saisie (aperçu de l'expression interprétée, saisies conservées) ([Davies et al., 2024](davies2024.md), niveau C ; [Gaona et al., 2018](gaona2018.md), niveau D pour la comparaison par équivalence). En RDM, de bons étudiants donnent des réponses justes par pure procédure ([Brown et al., 2007](brown2007.md), 3 étudiants, niveau D).

**3. En mécanique, les leurres issus d'erreurs types sont fiables et quelques-uns dominent.** L'inventaire de statique a un alpha de 0,89 et suit les notes du cours ([Steif et Dantzler, 2005](steif2005.md)) ; sur 1 331 passations, quatre leurres dominent : force interne dans le diagramme du corps isolé, couple remplacé par une force, force de liaison parallèle à la barre, frottement égal à µN ([Steif et Hansen, 2006](steif2006.md)) (niveau B). Les leurres bien construits sont choisis pour la raison prévue dans plus de 90 % des explications exploitables ([Klingbeil et al., 2024](klingbeil2024.md), niveau B). *Apport des P2 : règle confirmée et étendue hors de la statique (niveau C).* Au FCI, 24 questions sur 30 ont une réponse fausse dominante, la même dans deux groupes de niveaux très différents (53 % et 32 % de réussite) ([Martín-Blas et al., 2010](martinblas2010.md)) ; quatre familles reviennent sur 1 807 passations dans une école d'ingénieurs française : force dans le sens du mouvement, rôle de la masse, confusion vitesse-accélération, trajectoire dictée par la dernière impulsion ([Poutot et Blandin, 2015](poutot2015.md)) ; sur environ 34 000 passations, 22 erreurs types stables se dégagent, chacune portée par des leurres de plusieurs questions ([Segado et al., 2026](segado2026.md), prépublication). En dynamique, des leurres comme « tension du câble égale au poids » attirent la majorité avant le cours, parfois encore après ([Gray et al., 2005](gray2005.md)). En RDM, les pistes de leurres (« cisaillement uniforme, tau = V/A », « contrainte = force ») viennent de 3 étudiants ([Brown et al., 2007](brown2007.md), niveau D). Limite inchangée : une erreur repérable en comparant les options (force manquante) échappe au QCM ([Steif et Dantzler, 2005](steif2005.md), niveau C).

**4. Diagnostiquer sur plusieurs questions, par concept.** Un même étudiant ne choisit pas toujours le leurre de son erreur ; un diagnostic gradué sur 6 questions repère 418 des 420 élèves qui montrent l'erreur par écrit ([Klingbeil et al., 2024](klingbeil2024.md), niveau C). Le sous-score d'un concept annonce l'erreur correspondante à l'examen mieux que le score global ([Steif et Hansen, 2006](steif2006.md), niveau C). *Apport des P2 : règle confirmée, mieux étayée (niveau C).* Les questions d'un même concept de l'inventaire de statique sont plus corrélées entre elles qu'avec les autres (0,50 contre 0,24), ce qui justifie le sous-score par concept ; il faut aussi écarter les passations trop rapides ([Steif et Hansen, 2006b](steif2006b.md)). En algèbre, presque tous les élèves appliquent leur règle fausse dans moins de la moitié des occasions : une erreur se rapporte en fréquence d'usage (usages / occasions) ([Payne et Squibb, 1990](payne1990.md)). Un quiz de 2 à 3 questions a un alpha de 0,16 à 0,73 selon le thème : pas de diagnostic individuel à ce grain ([Steele et al., 2014](steele2014.md)). [Segado et al. (2026)](segado2026.md) proposent un score par erreur type, pondéré par leurre et comparé au niveau attendu au hasard (prépublication).

**5. Exercices en plusieurs étapes : report d'erreur, découpage et corps isolé.** Recalculer chaque étape à partir des saisies précédentes évite le tout ou rien ; 25 à 50 % du crédit pour une étape juste sur une valeur fausse et environ 3 à 4 étapes par calcul long ([Pearson et Penna, 2022](pearson2022.md), niveau C). *Apport des P2 : règle confirmée sans nouvelle mesure.* [Orthaber et al. (2020)](orthaber2020.md) décrivent en mécanique le report par recalcul, préférable à l'affichage des valeurs intermédiaires justes, et un diagramme du corps isolé en glisser-déposer (niveau D, aucune donnée d'étudiants) ; [Davies et al. (2024)](davies2024.md) demandent un retour après chaque partie (niveau D). Le diagramme lui-même compte : la réussite est de 85 % avec un diagramme correct, 49 % sans diagramme et 38 % avec un diagramme faux ([Rosengrant et al., 2009](rosengrant2009.md), niveau C, corrélation) ; d'où une étape « corps isolé » vérifiée avant les équations, sans pouvoir dire qu'elle fait réussir.

**6. L'effet sur l'apprentissage : premières mesures, toutes fragiles.** Les fiches P1 n'avaient que des comparaisons historiques ([Gill et Greenhow, 2008](gill2008.md), niveau D) et des observations d'usage : retour très lu mais retenue souvent limitée au jour même ([Gill et Greenhow, 2007](gill2007.md), niveau C). *Apport des P2 : le constat « effet non démontré » est nuancé, pas renversé.* Huit fiches de 2 à 3 QCM conceptuels suivies d'une discussion des erreurs s'accompagnent d'un gain plus fort sur les thèmes travaillés (+10 et +8 points à l'inventaire de statique), avec un plan contrebalancé mais un test proche des fiches et des tailles d'effet annoncées invraisemblables ([Steele et al., 2014](steele2014.md), niveau C). Un message par erreur fréquente est suivi d'une correction à l'essai suivant dans 58 % des cas contre 38 % sans message, chez 23 lycéens en programmation, sans tirage au sort ([Qian et Lehman, 2019](qian2019.md), niveau C). Avec des tentatives illimitées notées sur la meilleure, le retour immédiat produit plus de tentatives et de temps, un gain de note négligeable (+0,6 à +3,7 points sur 100) et l'abandon des tentatives dès la première erreur, sans mesure d'apprentissage ([Gaona et al., 2018](gaona2018.md), 5 507 étudiants, niveau C) : retour différé par défaut dans ce réglage.

**7. Les modèles de langage aident à formuler, pas à établir, les erreurs types.** *Nouveau point des P2.* À partir de l'énoncé, de la réponse fausse la plus choisie et du support de cours, un LLM rédige des hypothèses d'erreur jugées excellentes dans 45 cas sur 48 par des experts ; elles sont plausibles, mais jamais comparées à ce que pensent réellement les étudiants ([Parker et Zavala-Cerna, 2026](parker2026.md), niveau C pour la plausibilité, D pour l'exactitude). Une hypothèse générée reste donc une hypothèse tant que l'enseignant ne l'a pas validée.

### Vers un catalogue d'erreurs commun

Les fiches convergent vers un même objet, partagé par ExoForge, QuizForge et DiagForge : un catalogue d'erreurs types où chaque entrée porte les champs suivants.

| Champ | Contenu | Fiches |
| --- | --- | --- |
| Identifiant | nom court et stable, repris dans la banque de questions et les rapports | [gill2008](gill2008.md), [sikurajapathi2020](sikurajapathi2020.md) |
| Motif -> résultat erroné | formule fausse exécutable sur les paramètres tirés (condition -> action), avec son domaine de validité ; sert aussi à rejeter les tirages où elle donne la clé | [payne1990](payne1990.md), [greenhow2015](greenhow2015.md), [sikurajapathi2023](sikurajapathi2023.md) |
| Conception erronée et famille | conception visée (plusieurs motifs peuvent la partager) ; famille conceptuelle, exécution, hors mécanique ou aucune piste | [qian2019](qian2019.md), [martinblas2010](martinblas2010.md), [gross2012](gross2012.md), [bruhl2022](bruhl2022.md) |
| Poids par leurre | force du lien entre chaque leurre de QCM et la conception, pour un score par erreur type comparé au hasard | [segado2026](segado2026.md) |
| Message | retour sur l'étape (règle en jeu, contre-exemple chiffré, piste), un seul par conception, aucun pour un symptôme ambigu | [qian2019](qian2019.md), [payne1990](payne1990.md) |
| Compteurs | occasions où l'erreur pouvait s'appliquer, usages, affichages du message, corrections à l'essai suivant | [payne1990](payne1990.md), [qian2019](qian2019.md) |
| Statut | hypothèse (relevée une fois, proposée par un LLM) ou validée (fréquence suffisante, explications ou brouillons concordants) | [parker2026](parker2026.md), [sikurajapathi2023](sikurajapathi2023.md), [klingbeil2024](klingbeil2024.md) |

Ce format n'a été évalué en bloc par aucune étude ; chaque champ s'appuie sur la fiche citée (niveaux C à D).

## Règles pour ExoForge

Mention entre crochets : ce que les fiches de priorité 2 changent à la règle.

| Règle | Niveau | Fiches |
| --- | --- | --- |
| Recueillir les erreurs types dans les réponses fausses fréquentes et les brouillons ou copies (au besoin lors d'une première session sans retour ciblé) ; ne coder que les erreurs confirmées, puis renoter les réponses passées pour mesurer leur fréquence [confirmée] | C | sikurajapathi2020, gill2007, gill2008, qian2019 |
| Coder chaque erreur type comme une formule (mal-rule) condition -> action exécutée avec les paramètres tirés, classée dans un catalogue commun ouvert, avec les catégories « erreur de calcul » et « non diagnostiquée », y compris les erreurs de calculatrice (degrés et radians) [précisée] | C | gill2008, sikurajapathi2020, greenhow2015, payne1990 |
| À la génération, calculer la clé et chaque erreur type, et retirer les paramètres tant que la clé coïncide avec une erreur type ou que deux erreurs types coïncident, à la précision d'arrondi demandée | B | sikurajapathi2023, sikurajapathi2020, greenhow2015, tatsuoka1983 |
| Exclure les valeurs qui annulent structurellement une erreur type (0, 1, exposant 2, intervalle de longueur 1) ; choisir les plages par rétro-conception | B | sikurajapathi2023, greenhow2015 |
| Avant diffusion, tester chaque question sur un jeu de réponses justes écrites autrement (4/2 pour 2, racine rationalisée) et la faire résoudre par un collègue ; comparer par équivalence mathématique, en contrôlant à part la forme demandée [nouvelle] | C | davies2024, gaona2018 |
| Séparer l'erreur de saisie de la réponse fausse : guide de syntaxe, aperçu de l'expression interprétée, autres saisies conservées en cas de faute de frappe [nouvelle] | C | davies2024 |
| Saisie numérique réactive : comparer à la clé puis à chaque erreur type ; retour propre à l'erreur reconnue (seulement si la réponse est fausse), sinon solution rédigée complète | C | gill2008, greenhow2015, gill2007, sikurajapathi2023 |
| Retour ciblé formulé sur l'étape (règle en jeu, contre-exemple chiffré, piste de correction), pas sur l'étudiant ; un seul message par conception erronée, aucun message ciblé pour un symptôme aux causes multiples [nouvelle] | C (D pour le message unique) | payne1990, qian2019 |
| Trois familles d'erreurs (conceptuelle, exécution, hors mécanique) avec des retours différents ; contrôles automatiques hors mécanique (unités, x et y, sin et cos) avant le diagnostic conceptuel | C | gross2012, bruhl2022 |
| Noter séparément les composantes de la réponse : signe, module, unité, et pour une action mécanique sens et point d'application, avec un retour propre au sens faux quand le module est juste [étendue] | C | tatsuoka1983, bruhl2022 |
| Erreurs types de mécanique à coder : hyperstatique (équilibre seul, compatibilité seule, charge partagée également, force totale divisée par chaque aire), dynamique (T = mg pour une masse qui accélère, vitesse calculée depuis le centre de la roue, énergie cinétique sans rotation) [nouvelle] | C | bruhl2022, gray2005 |
| RDM : reconnaître V/A au lieu de 3V/(2A) comme l'erreur « cisaillement uniforme » [nouvelle, à valider par sa fréquence] | D | brown2007 |
| Étape « diagramme du corps isolé » vérifiée avant les équations (forces, objet qui l'exerce, sens) : signaler force manquante, force en trop, sens faux [nouvelle] | C | rosengrant2009 |
| Diagramme du corps isolé en glisser-déposer : plus d'étiquettes que de zones, étiquette vide « aucun effort » ; ne pas le présenter comme équivalent au tracé libre [nouvelle] | D | orthaber2020 |
| Question préalable d'identification du type de problème (isostatique ou hyperstatique, barres à effort nul) ; retour qui renvoie à cette identification [nouvelle] | D | bruhl2022 |
| Faire saisir les étapes intermédiaires quand on veut diagnostiquer une erreur d'algèbre [nouvelle] | C | payne1990 |
| Faire saisir l'unité, ou l'imposer dans l'énoncé et l'annoncer dans la consigne [nuancée : les deux choix existent, il faut en annoncer un] | D | gill2008, gill2007, orthaber2020 |
| Exercices en plusieurs étapes : report d'erreur par recalcul à partir des saisies, de préférence à l'affichage des valeurs intermédiaires justes (sinon les donner aussi en littéral) ; retour après chaque partie ; crédit paramétrable, 25 à 50 % par défaut [confirmée, sans nouvelle mesure] | C | pearson2022, greenhow2015, orthaber2020, davies2024 |
| Découper un long calcul en environ 3 à 4 étapes notées | C | pearson2022 |
| Pendant la mise en place, comparer brouillons et saisies pour repérer ce que l'exercice ne capte pas [nouvelle] | D | orthaber2020 |
| Conserver les réponses brutes, le tirage et l'erreur reconnue pour l'analyse a posteriori ; prévoir des comparaisons tirées au sort (leurres d'erreurs contre aléatoires, retour diagnostique contre général) | D | kinnear2022, gill2007 |
| Seuil d'au moins 4 % des réponses fausses pour retenir une erreur type | D | sikurajapathi2023 |

## Règles pour QuizForge

| Règle | Niveau | Fiches |
| --- | --- | --- |
| Chaque leurre code une erreur type nommée, issue de copies ; garder le lien leurre -> erreur dans la banque | C | steif2005, gill2007, gill2008 |
| Statique : leurres obligatoires « force interne dans le diagramme du corps isolé », « couple remplacé par une force », « force de liaison parallèle à la barre », « frottement = µN » | B | steif2006, steif2005 |
| Statique et RDM : leurres « encastrement sans moment de réaction », « N/A sans terme de flexion », « barre à effort nul non reconnue », « sens de réaction faux » [nouvelle] | C | bruhl2022 |
| Leurres numériques tirés des erreurs d'exécution fréquentes (x et y permutés, bras de levier, sin et cos, charge répartie) | C | gross2012 |
| Mécanique du point : leurres « force dans le sens du mouvement », « le plus lourd exerce la plus grande force », « durée de chute fonction de la masse », « confusion vitesse-accélération », « trajectoire selon la dernière impulsion » ; chaque erreur visée par plusieurs questions de contextes différents [nouvelle] | C | martinblas2010, poutot2015, segado2026 |
| Dynamique : leurres « tension = poids », « vitesse par rotation autour du centre de la roue », « v = 0 donc a = 0 », « énergie de rotation oubliée » [nouvelle] | C | gray2005 |
| RDM et 2e loi de Newton : leurres « cisaillement uniforme tau = V/A », « contrainte = force » ; mg, mg + ma, ma [nouvelle, fréquence inconnue] | D | brown2007, rosengrant2009 |
| Algèbre : leurres Mx + N -> (M + N)x, terme changé de membre sans changer de signe, distribution au seul premier terme, à recaler sur nos réponses [nouvelle] | C | payne1990 |
| Question conceptuelle à calcul trivial : chaque réponse fausse est le résultat exact d'un raisonnement faux | C | steif2005 |
| Options numériques en intervalles : chaque erreur type tombe dans une option distincte de la bonne réponse | C | ford2020 |
| Leurres rédigés avec les mots des étudiants, recueillis d'abord par une question ouverte puis des entretiens [confirmée] | C | ford2020, gray2005 |
| Invite « explique ton choix » sur une partie des passations pour valider les leurres d'une nouvelle question | C | klingbeil2024 |
| Étiqueter chaque question conceptuelle par concept, avec au moins 3 questions par concept [nouvelle] | C | steif2006b |
| Après chaque thème, un quiz conceptuel court (2 à 3 QCM) suivi d'un retour collectif sur le leurre dominant [nouvelle ; testé en classe sur papier, pas en ligne] | C | steele2014 |
| Tentatives illimitées notées sur la meilleure : retour différé par défaut, ou abandon d'une tentative rendu coûteux ; même politique de retour, annoncée, pour tout un parcours [nouvelle] | C (D pour la politique unique) | gaona2018, davies2024 |
| Brouillon de retour par leurre généré par LLM, toujours relu par l'enseignant avant publication [nouvelle] | D | parker2026 |
| Tester l'oubli d'une force et l'action-réaction par une construction, pas par un choix entre diagrammes | C | steif2005 |
| Saisie numérique sans unité : imposer l'unité dans l'énoncé et le dire dans la consigne [nouvelle] | D | orthaber2020 |
| Partir des inventaires existants de mécanique pour les questions conceptuelles | D | fakiyesi2024 |
| Option « je ne sais pas » en quiz sans enjeu ; option « aucune de ces réponses » parfois juste dans les QCM à paramètres | D | ford2020, greenhow2015 |
| Ne pas comparer directement la réussite d'un QCM et d'une saisie numérique sur la même notion | C | gill2007 |
| Programmer les activités sur des créneaux de l'emploi du temps plutôt qu'en ressource libre | C | gill2008 |

## Règles pour DiagForge

| Règle | Niveau | Fiches |
| --- | --- | --- |
| Diagnostiquer une erreur type sur plusieurs questions (au moins 3) qui la visent, avec gradation (absente, intermittente, systématique) ; la rapporter en fréquence d'usage (usages / occasions) et ne la dire systématique qu'au-delà de la moitié des occasions [précisée] | C | klingbeil2024, tatsuoka1983, payne1990 |
| Sous-scores par concept (au moins 3 questions par concept) en plus du score global, restitués à l'étudiant avec le juste/faux par question ; vérifier d'abord que les questions d'un concept sont plus corrélées entre elles qu'avec les autres [confirmée et précisée] | C | steif2006, steif2005, steif2006b |
| Pas de diagnostic individuel sur un quiz de 2 à 3 questions : agréger par concept sur plusieurs quiz [nouvelle] | C | steele2014 |
| Score par erreur type sur les seuls leurres rattachés, pondéré et normalisé de 0 à 1, par étudiant et par classe, avec le niveau attendu au hasard ; gain normalisé par erreur type [nouvelle, prépublication] | C | segado2026 |
| Part de chaque leurre par question, avec alerte quand un leurre égale ou dépasse la bonne réponse, et quand la réponse fausse dominante (leurres d'une même erreur additionnés) dépasse 50 % des réponses fausses ; part des réponses fausses expliquée par l'erreur type principale [étendue] | C | steif2006, sikurajapathi2020, martinblas2010 |
| Répartition des options au pré-test et au post-test, appariés, avec alerte quand un leurre reste majoritaire après le cours [nouvelle] | C (D pour l'appariement) | gray2005, poutot2015 |
| Répartition des réponses et leurre dominant (avec la conception qu'il code) pour préparer le retour collectif ; réponses fausses les plus fréquentes transmises à l'enseignant [nouvelle] | C | steele2014, davies2024 |
| Part des réponses fausses expliquée par le catalogue (toutes règles, 5 et 10 premières) et part non diagnostiquée ; ajouter les règles nouvelles observées localement [nouvelle] | C | payne1990 |
| Taux de correction par message (essais suivants corrigés / affichages), pour les messages assez souvent affichés [nouvelle] | C | qian2019 |
| Classer les réponses fausses en non conceptuelle, exécution, conceptuelle, plus « aucune piste » ; bilan individuel par famille avec exercice ciblé [précisée] | C (D pour le bilan) | bruhl2022, gross2012, kinnear2022 |
| Quand le diagramme du corps isolé est saisi, en faire le premier diagnostic d'une réponse fausse [nouvelle] | C | rosengrant2009 |
| Rapporter à part questions qualitatives et questions de calcul d'une même notion [nouvelle] | D | brown2007 |
| Distinguer question non répondue et réponse fausse ; signaler qu'en formatif sans enjeu une part des réponses est donnée pour voir le retour | C | sikurajapathi2020, gill2007 |
| Exclure ou signaler les passations trop rapides (durée minimale paramétrable) avant les indicateurs [nouvelle] | C | steif2006b |
| Par quiz : tentatives, temps, moyenne de toutes les tentatives, meilleure note et part des tentatives abandonnées ; difficulté et leurre dominant sur la première tentative seulement [nouvelle] | C | gaona2018, parker2026 |
| Notions difficiles : plus faible réussite en première tentative, stable sur au moins deux cohortes et deux questions [nouvelle] | C | parker2026 |
| Hypothèses d'erreur type proposées par LLM (énoncé, clé, réponse fausse dominante, support de cours), avec le statut « hypothèse » jusqu'à validation par l'enseignant [nouvelle] | C (plausibilité), D (exactitude) | parker2026 |
| Confiance déclarée de 0 à 5 par question ; signaler confiance élevée et réussite faible [nouvelle] | D | bruhl2022 |
| Calculer fiabilité, difficulté et discrimination de tout test diagnostique, même publié ; lire la discrimination avec la difficulté et le moment (pré ou post) ; alpha comme repère dans un test à plusieurs objectifs | C | fakiyesi2024, ford2020, greenhow2015 |
| Signaler les profils de réponses compatibles avec plusieurs erreurs types plutôt que trancher | C | tatsuoka1983 |
| Distribution des notes par exercice, avec alerte en cas de tout ou rien ou de concentration au maximum | D | pearson2022 |

Ces règles sont reprises sous forme lisible par un programme dans l'en-tête de chaque fiche (champ `regles`).

## Ce qui reste ouvert

- Aucun essai tiré au sort au niveau de l'étudiant ne compare un retour ciblé sur l'erreur type à une solution rédigée générale, ni des leurres issus d'erreurs à des leurres aléatoires ([Kinnear et al., 2022](kinnear2022.md)). Les mesures des P2 sont quasi expérimentales, sur un test proche de l'intervention ([Steele et al., 2014](steele2014.md)) ou hors de la mécanique ([Qian et Lehman, 2019](qian2019.md)) : c'est toujours le premier essai à mener dans ExoForge.
- Retour immédiat ou différé : on connaît son effet sur les tentatives ([Gaona et al., 2018](gaona2018.md)), pas sur l'apprentissage ; le délai de 48 heures de [Steele et al. (2014)](steele2014.md) n'est comparé à rien.
- La fréquence des tirages où une erreur type donne la bonne réponse, et celle des réponses justes refusées ([Davies et al., 2024](davies2024.md)), ne sont rapportées nulle part ; elles se mesurent directement sur nos banques.
- La part des réponses fausses qu'un catalogue de formules fausses reconnaît en mécanique n'est pas mesurée ; en algèbre, la traîne d'erreurs rares est longue ([Payne et Squibb, 1990](payne1990.md)).
- Le diagnostic par plusieurs leurres est validé en algèbre de collège ([Klingbeil et al., 2024](klingbeil2024.md)) et, pour les sous-scores, en statique ([Steif et Hansen, 2006](steif2006.md) ; [Steif et Hansen, 2006b](steif2006b.md)) ; le score par erreur type de [Segado et al. (2026)](segado2026.md) n'est validé contre aucun critère externe. Les erreurs de l'hyperstatique ([Bruhl et al., 2022](bruhl2022.md)) sont le seul relevé de niveau L3 ; rien en vibrations, mécanique des milieux continus, fatigue ou éléments finis.
- Les catégories d'erreurs (conceptuelle, exécution, hors mécanique) sont fixées par les correcteurs sans accord mesuré ([Gross et Dinehart, 2012](gross2012.md) ; [Gill et Greenhow, 2008](gill2008.md) ; [Bruhl et al., 2022](bruhl2022.md)).
- Le lien entre diagramme du corps isolé et réussite est une corrélation ([Rosengrant et al., 2009](rosengrant2009.md)) ; on ignore si faire construire le diagramme dans ExoForge fait mieux réussir, et le glisser-déposer proposé par [Orthaber et al. (2020)](orthaber2020.md) n'est pas évalué.
- Les hypothèses d'erreur produites par un LLM sont plausibles mais leur exactitude n'est pas mesurée ([Parker et Zavala-Cerna, 2026](parker2026.md)) ; il faudrait les comparer aux explications écrites des étudiants.
- L'effet de la restitution par concept aux étudiants n'est mesuré que par une enquête d'opinion ([Steif et Hansen, 2006b](steif2006b.md)).

Chacune de ces questions peut faire l'objet d'un essai avec ExoForge, QuizForge ou DiagForge ; les fiches proposent le dispositif (rubrique « Pour conclure, il faudrait »).

## Références

Références complètes : [`../forge.bib`](../forge.bib). `ford2020` et `klingbeil2024` figurent aussi dans l'axe B. La colonne « Fiche » donne le lien quand la fiche est écrite.

| Réf. (forge.bib) | Sous-axe | Apport | Priorité | Fiche |
| --- | --- | --- | --- | --- |
| `gill2007` — Gill and Greenhow (2007) | H1, H3 | conception de questions de mécanique à paramètres aléatoires, leurres issus des copies ; observations d'usage sur deux promotions (13 et 21 étudiants), sans groupe témoin | 1 | [fiche](gill2007.md) |
| `greenhow2015` — Greenhow (2015) | H1, H3 | QCM et réponses numériques à paramètres aléatoires codant les erreurs types (mal-rules) ; 272 843 réponses | 1 | [fiche](greenhow2015.md) |
| `kinnear2022` — Kinnear et al. (2022) | H1 | programme de recherche sur l'évaluation en ligne en mathématiques : 55 questions ouvertes | 1 | [fiche](kinnear2022.md) |
| `pearson2022` — Pearson and Penna (2022) | H1 | notation automatique de questions de calcul longues avec report d'erreur (Numbas) | 1 | [fiche](pearson2022.md) |
| `davies2024` — Davies et al. (2024) | H1 | passage de tout un département à STACK : réponses justes refusées, saisie, retour resté général | 2 | [fiche](davies2024.md) |
| `gaona2018` — Gaona et al. (2018) | H1 | WIRIS dans Moodle, 5 507 étudiants, mode de retour tiré au sort par classe : le retour immédiat multiplie les tentatives sans gain net | 2 | [fiche](gaona2018.md) |
| `orthaber2020` — Orthaber et al. (2020) | H1 | conception de questions d'examen de mécanique dans Moodle (report d'erreur, corps isolé en glisser-déposer), sans données d'étudiants | 2 | [fiche](orthaber2020.md) |
| `fakiyesi2024` — Fakiyesi et al. (2024) | H2 | revue des inventaires de concepts en ingénierie : la statique domine, psychométrie rare | 1 | [fiche](fakiyesi2024.md) |
| `ford2020` — Ford et al. (2020) | H2, B2 | QCM pour cours de 3e année (RDM, dynamique) : entretiens, bonnes réponses pour de mauvaises raisons | 1 | [fiche](ford2020.md) |
| `gross2012` — Gross and Dinehart (2012) | H2, H3 | 8 000 copies de mécanique classées : erreurs conceptuelles, d'exécution et hors mécanique | 1 | [fiche](gross2012.md) |
| `steif2005` — Steif and Dantzler (2005) | H2 | Statics Concept Inventory : 27 QCM, leurres = erreurs types, analyse psychométrique | 1 | [fiche](steif2005.md) |
| `steif2006` — Steif and Hansen (2006) | H2 | inventaire de statique et notes d'examen, 1 331 passations ; sous-scores par concept ; leurres les plus choisis | 1 | [fiche](steif2006.md) |
| `brown2007` — Brown et al. (2007) | H2 | états de contrainte en RDM : 3 étudiants interrogés ne relient pas contraintes et chargements (tau = V/A, contrainte = force) | 2 | [fiche](brown2007.md) |
| `bruhl2022` — Bruhl et al. (2022) | H2, H3 | examen diagnostique de mécanique (West Point) : erreurs types en treillis et équilibre | 2 | [fiche](bruhl2022.md) |
| `gray2005` — Gray et al. (2005) | H2 | Dynamics Concept Inventory : version 1.0 (11 concepts, environ 30 QCM), 754 étudiants de deux universités : leurres de dynamique majoritaires avant le cours | 2 | [fiche](gray2005.md) |
| `martinblas2010` — Martín-Blas et al. (2010) | H2 | test FCI en 1re année d'ingénieur : erreurs dominantes partagées par deux groupes | 2 | [fiche](martinblas2010.md) |
| `poutot2015` — Poutot and Blandin (2015) | H2 | FCI au CESI sur trois ans : conceptions erronées les plus fréquentes | 2 | [fiche](poutot2015.md) |
| `rosengrant2009` — Rosengrant et al. (2009) | H2 | diagrammes du corps libre : ceux qui les tracent correctement réussissent mieux | 2 | [fiche](rosengrant2009.md) |
| `segado2026` — Segado et al. (2026) | H2, C | 34 000 passations du FCI : 22 dimensions de leurres, score de conception erronée par classe (prépublication) | 2 | [fiche](segado2026.md) |
| `steele2014` — Steele et al. (2014) | H2 | fiches de QCM en classe et discussion des erreurs : +8 à +10 points à l'inventaire de statique sur les thèmes travaillés (plan contrebalancé) | 2 | [fiche](steele2014.md) |
| `steif2006b` — Steif and Hansen (2006) | H2 | restituer les résultats de l'inventaire de statique aux enseignants et aux étudiants | 2 | [fiche](steif2006b.md) |
| `mccarthy2012` — McCarthy and Goldfinch (2012) | H2 | quiz en ligne sur les diagrammes du corps libre, prédictif des cours suivants | 3 | sans fiche : priorité 3, non lue |
| `gill2008` — Gill and Greenhow (2008) | H3 | erreurs relevées dans 341 copies codées en leurres et en mal-rules ; comparaison historique 1999-2004 / 2004-2006 : meilleures notes sur 2 thèmes sur 4 | 1 | [fiche](gill2008.md) |
| `klingbeil2024` — Klingbeil et al. (2024) | H3, B2 | QCM diagnostiques en algèbre : erreur détectée chez 418 des 420 élèves qui la montrent par écrit ; bonne réponse parfois pour une mauvaise raison | 1 | [fiche](klingbeil2024.md) |
| `sikurajapathi2020` — Sikurajapathi et al. (2020) | H3 | catalogue d'erreurs types en mathématiques d'ingénieur et retour ciblé en ligne | 1 | [fiche](sikurajapathi2020.md) |
| `sikurajapathi2023` — Sikurajapathi et al. (2023) | H3, H1 | juste pour une mauvaise raison : le choix des paramètres peut rendre une erreur type indétectable | 1 | [fiche](sikurajapathi2023.md) |
| `tatsuoka1983` — Tatsuoka (1983) | H3 | rule space : relier les réponses à des règles erronées dans la théorie des réponses aux items | 1 | [fiche](tatsuoka1983.md) |
| `parker2026` — Parker and Zavala-Cerna (2026) | H3, C | repérer les notions difficiles par les résultats de quiz puis caractériser les erreurs avec un LLM | 2 | [fiche](parker2026.md) |
| `payne1990` — Payne and Squibb (1990) | H3 | mal-rules en algèbre : fréquences très inégales, usage instable par un même étudiant | 2 | [fiche](payne1990.md) |
| `qian2019` — Qian and Lehman (2019) | H3 | retour ciblé sur les erreurs types en programmation : correction à l'essai suivant 58 % contre 38 % (23 lycéens, sans tirage au sort) | 2 | [fiche](qian2019.md) |
| `chen2026` — Chen et al. (2026) | H3 | 101 mal-rules exécutables sur 498 gabarits paramétrés (prépublication) | 3 | sans fiche : priorité 3, non lue |

Priorité 1 = à lire d'abord ; priorité 2 = lue ensuite ; priorité 3 = complément, non lu à ce jour.
