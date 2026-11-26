# Axe D — Exemples guidés et guidage

Question pour l'outil : combien d'aide donner dans un exercice pas à pas, à qui, et comment la retirer ?

## Vue d'ensemble

Cet axe étudie le guidage pendant la résolution d'un problème : montrer une solution complète avant de faire chercher (exemple résolu, en anglais worked example), retirer peu à peu les étapes données (estompage, fading), proposer des indices et des aides, et demander à l'étudiant d'expliquer une étape ou de trouver l'erreur dans une solution fausse. La théorie qui relie ces travaux est la théorie de la charge cognitive : un débutant qui cherche une solution à tâtons occupe sa mémoire de travail et apprend peu de la méthode. Son résultat le plus utile pour nous est l'effet d'inversion d'expertise : une aide qui soutient le débutant devient inutile, voire gênante, pour l'étudiant qui maîtrise déjà l'étape.

L'axe sert surtout à ExoForge, qui produit des exercices HTML/SCORM paramétrés, découpés en étapes, avec indices, essais multiples et retours après chaque erreur : combien d'étapes données, dans quel ordre les retirer, que montrer après une erreur, quelles questions d'explication poser. Il renseigne aussi CapsuleForge (chapitres de cours interactifs tirés de diaporamas narrés, avec questions et exercices ExoForge), pour les questions posées en cours de chapitre, et DiagForge, qui peut repérer les étudiants à qui une aide sera utile ou superflue.

Le public visé est celui de Forge : étudiants de L3 à M2 en mécanique et en mathématiques, qui travaillent seuls en ligne. La plupart des études lues portent sur des élèves du secondaire ou des étudiants de première année (probabilités, algèbre, géométrie, circuits électriques) ; aucune ne porte sur des problèmes de mécanique à plusieurs étapes du niveau master. Nos étudiants sont avancés sur les bases et débutants sur chaque notion nouvelle : c'est précisément le cas où l'inversion d'expertise compte.

## Historique du domaine

**Années 1980-1990 : les exemples résolus.** L'équipe de John Sweller, à l'université de Nouvelle-Galles du Sud (Sydney), montre qu'étudier des exemples résolus guide mieux les débutants que la résolution libre (Tarmizi et Sweller, 1988). La théorie de la charge cognitive, développée par la même équipe, en donne l'explication : chercher seul consomme la mémoire de travail dont l'apprentissage aurait besoin.

**Années 2000 : estompage et inversion d'expertise.** Renkl, Atkinson et leurs collègues transforment l'exemple résolu en transition progressive vers le problème, en retirant les étapes une à une ([Renkl et al., 2002](renkl2002.md) ; [Renkl et Atkinson, 2003](renkl2003.md) ; [Atkinson et al., 2003](atkinson2003.md) ; [Renkl et al., 2004](renkl2004.md)). Kalyuga montre avec des apprentis que l'exemple aide au début et devient inutile ensuite ([Kalyuga et al., 2001](kalyuga2001.md)), puis décrit l'effet d'inversion d'expertise ([Kalyuga et al., 2003](kalyuga2003.md) ; [Kalyuga, 2007](kalyuga2007.md)), propose un test de niveau rapide ([Kalyuga et Sweller, 2004](kalyuga2004.md)) et l'étend au choix entre animation et images fixes ([Kalyuga, 2008](../E_multimedia/kalyuga2008.md)). Suivent des études en ingénierie sur les circuits électriques ([Reisslein et al., 2006](reisslein2006.md) ; [Moreno et al., 2009](moreno2009.md)), les premiers travaux sur les exemples erronés ([Große et Renkl, 2007](grosse2007.md)) et l'intégration de l'estompage dans des systèmes tutoriels intelligents (STI), qui le rendent adaptatif ([Schwonke et al., 2009](schwonke2009.md) ; [Salden et al., 2009](salden2009.md) ; [Salden et al., 2010](salden2010.md)).

**Années 2010 : méta-analyses et essais en classe.** Les grandes synthèses arrivent : étayage numérique en STEM ([Belland et al., 2017](belland2016.md)), auto-explication ([Bisra et al., 2018](bisra2018.md)) et auto-explication en mathématiques ([Rittle-Johnson et al., 2017](rittlejohnson2017.md)). Les essais quittent le laboratoire : exemples erronés dans un STI d'algèbre en classe ([Booth et al., 2013](booth2013.md)), exemples choisis librement par les étudiants ([Foster et al., 2018](foster2018.md)), comparaison guidée entre sa tentative et la solution ([Loibl et Leuders, 2019](loibl2019.md)), et un premier résultat décevant : l'estompage ne fait pas mieux dans des devoirs en ligne ([Miller-Cotto et Auxter, 2019](millercotto2019.md)).

**2020-2026 : nuances et IA générative.** La méta-analyse sur les exemples résolus en mathématiques confirme l'effet, avec une forte variabilité ([Barbieri et al., 2023](barbieri2023.md)). Les travaux récents précisent les conditions : les exemples erronés aident quand ils sont contrastés avec la solution correcte ([Dieterich et al., 2025](dieterich2025.md) ; méta-analyse d'Alemdag et al., 2025, inaccessible), les invites d'explication doivent être guidées ([Zhang et Fiorella, 2024](zhang2024.md) ; [Beege et Ploetzner, 2024](beege2024.md)), et un guidage plus contraignant peut être moins apprécié mais plus efficace ([Borchers et al., 2025](borchers2025.md)). L'IA générative arrive comme aide à la résolution, avec le risque de devenir une machine à réponses ([Huang et al., 2026](huang2026.md)).

## D1 — Exemples résolus et estompage

Étudier une solution complète avant de résoudre améliore l'apprentissage des débutants en mathématiques ([Barbieri et al., 2023](barbieri2023.md)) ; l'effet tient même face à un STI qui corrige chaque étape ([Schwonke et al., 2009](schwonke2009.md)). Laissés libres, les étudiants consultent peu les exemples et préfèrent chercher seuls d'abord ([Foster et al., 2018](foster2018.md)) : l'exemple doit donc être imposé.

L'estompage remplace l'alternance exemple-exercice par une suite progressive : exemple complet, puis une étape à faire, puis deux, jusqu'à l'exercice entier ([Renkl et al., 2002](renkl2002.md) ; [Renkl et Atkinson, 2003](renkl2003.md)). On apprend surtout les principes dont l'étape a été laissée à faire ([Renkl et al., 2004](renkl2004.md)) ; associé au choix du principe appliqué, il améliore aussi le transfert éloigné ([Atkinson et al., 2003](atkinson2003.md)). L'ordre de retrait (première ou dernière étape d'abord) donne des résultats opposés selon les contenus ; sur un exercice de circuits facile, retirer la dernière étape d'abord échoue ([Moreno et al., 2009](moreno2009.md)). Surtout, le gain de laboratoire ne se retrouve pas toujours en conditions réelles : dans des devoirs d'algèbre en ligne ([Miller-Cotto et Auxter, 2019](millercotto2019.md)) et dans un cours d'introduction à l'ingénierie ([Reisslein et al., 2006](reisslein2006.md)), l'estompage ne fait pas mieux en moyenne.

## D2 — Indices, étayage et inversion d'expertise

L'étayage (scaffolding) désigne toute aide apportée pendant la résolution : indice, étape donnée, question qui oriente, retour après erreur. Fourni par un logiciel, il améliore les résultats en STEM, à l'université aussi, quelle que soit sa forme ([Belland et al., 2017](belland2016.md)). Après une erreur, montrer l'étape correspondante d'un exemple analogue puis laisser réessayer est particulièrement efficace ([Moreno et al., 2009](moreno2009.md)). Un guidage contraignant (saisir unités et grandeurs à chaque étape) fait mieux comprendre, même s'il est moins apprécié ([Borchers et al., 2025](borchers2025.md)).

Mais l'aide utile au débutant gêne l'étudiant avancé : c'est l'inversion d'expertise ([Kalyuga et al., 2001](kalyuga2001.md) ; [Kalyuga et al., 2003](kalyuga2003.md) ; [Kalyuga, 2007](kalyuga2007.md)). En ingénierie électrique, les débutants réussissent mieux avec l'exemple d'abord, les plus avancés avec le problème d'abord ([Reisslein et al., 2006](reisslein2006.md)). Sur des graphes de fonctions, les débutants apprennent mieux une procédure avec des images fixes numérotées qu'avec une animation ; chez les avancés, la différence n'est pas significative ([Kalyuga, 2008](../E_multimedia/kalyuga2008.md), fiche dans l'axe E). Dans les simulations du supérieur, l'effet des aides (exemples, invites) dépend lui aussi des connaissances préalables ([Chernikova et al., 2020](../E_multimedia/chernikova2020.md), fiche dans l'axe E).

Adapter l'aide suppose de connaître le niveau. Un test rapide « quelle est l'étape suivante ? » le mesure presque aussi bien qu'un test complet ([Kalyuga et Sweller, 2004](kalyuga2004.md)). Dans un STI, retirer une étape seulement quand l'élève maîtrise le principe correspondant fait mieux qu'un estompage fixe ([Salden et al., 2010](salden2010.md) ; [Salden et al., 2009](salden2009.md)). Enfin, l'aide d'une IA générative doit elle-même être cadrée : sans méthode de vérification, les étudiants changent des réponses justes en fausses ([Huang et al., 2026](huang2026.md)).

## D3 — Auto-explication et exemples erronés

Demander à l'étudiant d'expliquer lui-même une étape (auto-explication, self-explanation) améliore l'apprentissage ([Bisra et al., 2018](bisra2018.md)) ; en mathématiques, l'effet est plus net quand l'explication est guidée, par exemple en choisissant le principe dans une liste ([Rittle-Johnson et al., 2017](rittlejohnson2017.md) ; [Atkinson et al., 2003](atkinson2003.md)). Les invites ouvertes, elles, coûtent du temps et de l'attention : elles n'aident pas dans des devoirs en ligne ([Miller-Cotto et Auxter, 2019](millercotto2019.md)) ni dans une vidéo ([Beege et Ploetzner, 2024](beege2024.md)), alors qu'une phrase à compléter qui oriente vers la cause d'une erreur aide ([Zhang et Fiorella, 2024](zhang2024.md)).

Un exemple erroné est une solution qui contient une erreur type, à repérer et à expliquer. Il aide surtout quand il est placé à côté de la solution correcte et accompagné d'une consigne de comparaison ([Dieterich et al., 2025](dieterich2025.md) ; [Loibl et Leuders, 2019](loibl2019.md)) ; il améliore la compréhension conceptuelle sans nuire à la résolution ([Booth et al., 2013](booth2013.md)). Il demande toutefois des bases : il gêne les débutants si l'erreur n'est pas signalée ([Große et Renkl, 2007](grosse2007.md)). Les erreurs à montrer sont les mêmes que celles codées comme leurres dans QuizForge et comme règles erronées dans ExoForge (axes B et H).

## Ce que disent les fiches

Synthèse rédigée à partir des 28 fiches de lecture écrites (11 de priorité 1 et 17 de priorité 2, dont [Kalyuga, 2008](../E_multimedia/kalyuga2008.md), fiche de l'axe E ajoutée le 10/11/2026) ; toutes les références de priorité 1 et 2 ont une fiche, sauf la méta-analyse d'Alemdag et al. (2025), inaccessible. Elle ne dit que ce que ces fiches soutiennent ; le niveau de preuve suit l'échelle de [fiches_methode.md](../fiches_methode.md).

**1. Commencer par des exemples résolus.** Étudier une solution complète avant de résoudre améliore les performances en mathématiques ([Barbieri et al., 2023](barbieri2023.md) : g = 0,48, niveau A au collège et au lycée, B dans le supérieur, peu représenté). Plus largement, toute aide apportée par le logiciel pendant la résolution améliore les résultats en STEM, à l'université aussi ([Belland et al., 2017](belland2016.md) : g = 0,46 ; 0,49 dans le supérieur). Il faut imposer l'exemple : libres de choisir, les étudiants commencent par chercher seuls et ne choisissent un exemple que dans 27 % des essais (première expérience), surtout après un échec ([Foster et al., 2018](foster2018.md), niveau B).

**2. Retirer l'aide progressivement, sans en attendre de miracle.** L'estompage (exemple complet, puis une étape à faire, puis deux, puis l'exercice entier) fait mieux que l'alternance exemple-exercice en laboratoire ([Renkl et al., 2002](renkl2002.md) ; [Renkl et Atkinson, 2003](renkl2003.md) ; [Atkinson et al., 2003](atkinson2003.md) ; niveau B, études de la même équipe). Ce qui compte est le principe de l'étape retirée, plus que sa position : on apprend surtout les principes dont l'étape a été laissée à faire ([Renkl et al., 2004](renkl2004.md), niveau C). Ajouté à un système tutoriel intelligent (STI) qui corrige déjà chaque étape, l'estompage donne les mêmes résultats en moins de temps ([Schwonke et al., 2009](schwonke2009.md), niveau C). Mais le gain n'apparaît pas toujours en conditions ordinaires : pas d'avantage dans des devoirs d'algèbre en ligne à l'université ([Miller-Cotto et Auxter, 2019](millercotto2019.md)), ni en moyenne pour des circuits électriques dans un cours d'introduction à l'ingénierie ([Reisslein et al., 2006](reisslein2006.md)), et l'estompage par la dernière étape échoue sur un contenu facile ([Moreno et al., 2009](moreno2009.md)) (niveau C). En moyenne, un étayage qui s'estompe ne donne pas de meilleures notes qu'un étayage fixe ([Belland et al., 2017](belland2016.md), comparaison entre études, niveau C).

**3. Adapter l'aide au niveau.** Un exemple qui aide le débutant devient inutile, puis gênant, pour l'étudiant avancé ([Kalyuga et al., 2001](kalyuga2001.md) ; [Kalyuga et al., 2003](kalyuga2003.md) ; niveau B pour le principe, C pour l'inversion complète). En ingénierie électrique, les débutants réussissent mieux avec l'exemple avant le problème, les plus avancés avec le problème avant l'exemple ([Reisslein et al., 2006](reisslein2006.md), niveau C). **Confirmé et étendu au format de présentation** : pour apprendre à transformer un graphe de fonction, les étudiants les plus faibles progressent davantage avec une suite d'images fixes numérotées qu'avec la même démonstration animée (gain moyen 2,56 contre 0,50 points sur 16) ; chez les plus avancés, l'animation fait un peu mieux mais la différence n'est pas significative ([Kalyuga, 2008](../E_multimedia/kalyuga2008.md), niveau C pour l'interaction niveau × format, D pour un avantage de l'animation chez les avancés ; 8 ou 9 étudiants par groupe, 2 minutes d'enseignement). Ce qui est établi est donc l'inconvénient de l'animation pour le débutant, pas son intérêt pour l'avancé. Un test rapide « quelle est l'étape suivante ? » mesure le niveau presque aussi bien qu'un test complet (r = 0,85 à 0,92) en 2,5 à 5 fois moins de temps, et peut piloter l'estompage ([Kalyuga et Sweller, 2004](kalyuga2004.md), niveau B pour la mesure, C pour le pilotage ; [Kalyuga, 2007](kalyuga2007.md)). Un estompage piloté par la maîtrise de chaque principe fait mieux au test différé qu'un estompage fixe ([Salden et al., 2010](salden2010.md), niveau C ; [Salden et al., 2009](salden2009.md) rapporte les mêmes expériences). Enfin, un guidage plus contraignant peut mieux faire apprendre tout en étant moins apprécié : faire saisir unités et grandeurs à chaque étape améliore la compréhension en chimie, alors que les étudiants préfèrent le système qui ne vérifie que le résultat ([Borchers et al., 2025](borchers2025.md), niveau C).

**4. Faire expliquer, de façon guidée.** Demander à l'étudiant d'expliquer lui-même améliore l'apprentissage, à l'université aussi ([Bisra et al., 2018](bisra2018.md) : g = 0,55, niveau A). En mathématiques, l'effet immédiat est petit à moyen (0,28 à 0,46), plus fort sur les concepts quand l'explication est guidée par une formation ou une réponse structurée, mais peu d'études mesurent l'effet différé ou en classe ([Rittle-Johnson et al., 2017](rittlejohnson2017.md), niveau B). Choisir le principe dans une liste, avec retour, est efficace ([Atkinson et al., 2003](atkinson2003.md), niveau B). À l'inverse, des invites génériques (« pourquoi cette étape ? ») font moins bien que des exercices ordinaires dans des devoirs en ligne ([Miller-Cotto et Auxter, 2019](millercotto2019.md), niveau C) ; dans une vidéo, à temps égal, des questions ouvertes sans retour n'apportent rien et augmentent la charge ([Beege et Ploetzner, 2024](beege2024.md), niveau C) ; une invite ouverte sur une erreur n'aide pas, une phrase à compléter qui oriente vers le pourquoi aide ([Zhang et Fiorella, 2024](zhang2024.md), niveau C).

**5. Exemples erronés : contrastés et avec consigne.** Montrer des solutions fausses aide surtout quand elles sont placées à côté de la solution correcte : 9 comparaisons sur 12 en faveur de l'exemple erroné contrasté contre l'exemple correct seul ([Dieterich et al., 2025](dieterich2025.md), revue de 40 études, niveau C). La consigne est décisive : sans elle, presque personne ne regarde les erreurs ; avec « qu'a-t-il fait de faux ? qu'a fait l'autre de mieux ? », les élèves apprennent plus, surtout ceux qui avaient fait l'erreur ([Loibl et Leuders, 2019](loibl2019.md), niveau B). Remplacer quelques exercices guidés par des exemples corrects et erronés à expliquer améliore la compréhension sans perte en résolution ([Booth et al., 2013](booth2013.md), niveau B pour les exemples, C pour les exemples erronés). Mais les exemples erronés aident les étudiants qui ont des bases et gênent les débutants, sauf si l'erreur est signalée ([Große et Renkl, 2007](grosse2007.md), niveau C).

**6. Après une erreur.** Le retour immédiat à chaque étape fait un peu mieux que le retour en fin d'exercice ([Moreno et al., 2009](moreno2009.md), niveau C). Montrer l'étape correspondante d'un exemple analogue puis laisser réessayer améliore nettement le transfert, sans qu'on sache quel ingrédient agit (même fiche, niveau B). Après un échec, les étudiants choisissent volontiers un exemple partiel (dernière étape à faire) plutôt qu'une solution complète ([Foster et al., 2018](foster2018.md), niveau C). Mieux présenter le retour ne suffit pas ; c'est l'explication demandée à l'étudiant qui compte ([Zhang et Fiorella, 2024](zhang2024.md), niveau C).

**7. L'aide d'une IA générative.** Sans préparation, des étudiants de physique qui révisent leurs réponses avec une IA changent souvent des réponses justes en fausses ; 45 minutes de formation (planifier, vérifier, repérer les erreurs de l'IA) améliorent nettement la révision, mesurée le jour même ([Huang et al., 2026](huang2026.md), niveau C).

## Règles pour ExoForge

| Règle | Niveau | Fiches |
| --- | --- | --- |
| Introduire chaque type d'exercice par un exemple entièrement résolu, imposé et non optionnel | B | barbieri2023, belland2016, foster2018 |
| Proposer l'exercice en séquence estompée plutôt qu'en paires exemple-exercice | B | renkl2002, renkl2003, atkinson2003 |
| Choisir les étapes à estomper selon le principe visé, pas selon leur position | C | renkl2004 |
| À chaque étape résolue, faire choisir le principe appliqué dans une liste (ou compléter une phrase), puis afficher la bonne réponse | B | atkinson2003, salden2010, rittlejohnson2017 |
| Pas d'invite générique « pourquoi ? » ni de question ouverte sans retour | C | millercotto2019, beege2024, zhang2024 |
| Faire saisir unités et grandeurs intermédiaires, pas seulement le résultat final | C | borchers2025 |
| Retour immédiat après chaque étape | C | moreno2009, belland2016 |
| Après une erreur : exemple partiel ou étape analogue d'un exemple résolu, puis second essai | B | moreno2009, foster2018 |
| Après une erreur : phrase à compléter qui oriente vers la cause, pas d'invite ouverte seule | C | zhang2024, bisra2018 |
| Mesurer le niveau par un test rapide « étape suivante » et régler le guidage | C | kalyuga2004, kalyuga2007, kalyuga2003 |
| Ordre selon le niveau : exemple d'abord pour les débutants, problème d'abord pour les avancés | C | reisslein2006, kalyuga2001 |
| Estomper principe par principe selon la maîtrise (seuil de montée, seuil de retour) | C | salden2010, salden2009, renkl2003 |
| Réduire les exemples pour les étudiants avancés ; exercices directs sur un contenu connu | C | kalyuga2001, kalyuga2003 |
| Procédure graphique (graphe, diagramme) montrée à un débutant : suite numérotée d'images fixes annotées plutôt qu'une animation continue sans contrôle ; l'animation reste une simple option pour l'étudiant qui réussit le diagnostic | C | kalyuga2008 (axe E) |
| Ne pas estomper par la dernière étape sur un contenu facile | C | moreno2009 |
| Exemples erronés construits sur les erreurs types, présentés à côté de la solution correcte, avec consigne de comparaison | C | dieterich2025, loibl2019, booth2013 |
| Signaler l'étape fausse pour les débutants ; erreur à trouver seul pour les avancés | C | grosse2007, dieterich2025 |
| Si une IA est autorisée, fournir une méthode de vérification de ses réponses | C | huang2026 |
| Ne pas juger un exercice sur la satisfaction des étudiants seule | C | borchers2025 |

Ces règles sont reprises sous forme lisible par un programme dans l'en-tête de chaque fiche (champ `regles`).

## Ce qui reste ouvert

- Presque toutes les études durent une séance et mesurent le transfert immédiatement ; les effets à plusieurs semaines sont peu connus ([Rittle-Johnson et al., 2017](rittlejohnson2017.md) le confirme pour l'auto-explication).
- L'estompage, robuste en laboratoire, ne fait pas mieux dans deux études en conditions réelles proches des nôtres (devoirs en ligne, cours d'ingénierie électrique) : c'est le premier point à tester dans ExoForge.
- Le public universitaire scientifique reste minoritaire ; aucune étude lue ne porte sur la mécanique au-delà de la première année.
- Le choix du principe dans une liste et l'explication rédigée n'ont pas été comparés directement sur des problèmes de mécanique.
- La méta-analyse sur les exemples erronés (Alemdag et al., 2025) n'est pas accessible ; le sous-axe D3 s'appuie sur la revue de Dieterich et al. (2025) et quatre études.
- L'inversion d'expertise sur le format (images fixes ou animation) repose sur une seule très petite étude, avec une animation sans pause ni retour ([Kalyuga, 2008](../E_multimedia/kalyuga2008.md)) : reste à tester, sur une notion nouvelle pour nos étudiants (cercle de Mohr, diagramme de Bode), des images fixes numérotées contre une animation contrôlable, avec un diagnostic initial et un test différé.
- L'ordre de retrait des étapes (première ou dernière d'abord) donne des résultats opposés selon les contenus ; aucune étude ne dit lequel convient à un problème de mécanique à une dizaine d'étapes.
- L'estompage adaptatif n'a été testé que dans des STI dotés d'un modèle détaillé de l'élève ; des règles simples (passer à l'étape suivante après deux réussites) n'ont pas été évaluées.

Chacune de ces questions peut faire l'objet d'un essai dans ExoForge ; les fiches proposent le dispositif (rubrique « Pour conclure, il faudrait »).

## Références

Références complètes : [`../forge.bib`](../forge.bib). La colonne « Fiche » donne le lien quand la fiche est écrite ; `chernikova2020` et `kalyuga2008` ont leur fiche dans l'axe E.

| Réf. (forge.bib) | Sous-axe | Apport | Priorité | Fiche |
| --- | --- | --- | --- | --- |
| `atkinson2003` — Atkinson et al. (2003) | D1, D3 | estompage + invite « quel principe ? » : transfert proche et lointain, sans temps en plus | 1 | [fiche](atkinson2003.md) |
| `barbieri2023` — Barbieri et al. (2023) | D1, D3 | méta-analyse en maths : exemples résolus g = 0,48 ; les invites d'auto-explication réduisent l'effet | 1 | [fiche](barbieri2023.md) |
| `moreno2009` — Moreno et al. (2009) | D1 | circuits électriques, 1re année : estompage avant et retour après chaque étape plus efficaces | 1 | [fiche](moreno2009.md) |
| `renkl2003` — Renkl and Atkinson (2003) | D1 | procédure d'estompage : exemple complet, puis étapes retirées une à une, puis problème | 1 | [fiche](renkl2003.md) |
| `millercotto2019` — Miller-Cotto and Auxter (2019) | D1 | devoirs Canvas à l'université : l'estompage ne bat pas les exercices classiques | 2 | [fiche](millercotto2019.md) |
| `renkl2002` — Renkl et al. (2002) | D1 | estompage meilleur que les paires exemple-problème ; retirer d'abord les dernières étapes | 2 | [fiche](renkl2002.md) |
| `renkl2004` — Renkl et al. (2004) | D1 | on apprend surtout les principes dont l'étape a été retirée ; moins d'erreurs improductives | 2 | [fiche](renkl2004.md) |
| `schwonke2009` — Schwonke et al. (2009) | D1 | exemples estompés dans un STI : mêmes résultats en moins de temps | 2 | [fiche](schwonke2009.md) |
| `grosse2015` — Große (2015) | D1 | modélisation : paires exemple-problème pour la mise en équation, estompage arrière pour le calcul | 3 | à lire |
| `moreno2006` — Moreno et al. (2006) | D1 | même équipe : estompage avant et adaptatif meilleurs que l'estompage arrière | 3 | à lire |
| `shin2023` — Shin et al. (2023) | D1 | programmation : estomper par concept plutôt que par position | 3 | à lire |
| `tarmizi1988` — Tarmizi and Sweller (1988) | D1 | article fondateur : les exemples résolus guident mieux que la résolution libre | 3 | à lire |
| `belland2016` — Belland et al. (2017) | D2 | méta-analyse de 144 études STEM : étayage numérique g = 0,46 | 1 | [fiche](belland2016.md) |
| `chernikova2020` — Chernikova et al. (2020) | E3, D2 | méta-analyse des simulations dans le supérieur : g = 0,85 ; exemples pour novices | 1 | [fiche](../E_multimedia/chernikova2020.md) |
| `kalyuga2001` — Kalyuga et al. (2001) | D2, D1 | apprentis (automates) : exemples utiles aux débutants, exercices meilleurs ensuite | 1 | [fiche](kalyuga2001.md) |
| `kalyuga2003` — Kalyuga et al. (2003) | D2 | revue de l'effet d'inversion d'expertise : l'aide des novices gêne les avancés | 1 | [fiche](kalyuga2003.md) |
| `kalyuga2007` — Kalyuga (2007) | D2 | mise à jour : conséquences pour un enseignement adapté au niveau | 1 | [fiche](kalyuga2007.md) |
| `salden2010` — Salden et al. (2010) | D2, D1 | labo puis classe : estompage adaptatif meilleur au test différé ; fixe ≈ résolution guidée par le STI | 1 | [fiche](salden2010.md) |
| `borchers2025` — Borchers et al. (2025) | D2 | STI de chimie très guidé : gains conceptuels que le STI peu guidé n'obtient pas ; moins apprécié | 2 | [fiche](borchers2025.md) |
| `foster2018` — Foster et al. (2018) | D2 | libres de choisir, les étudiants prennent peu d'exemples mais utilisent bien les exemples partiels | 2 | [fiche](foster2018.md) |
| `huang2026` — Huang et al. (2026) | D2 | IA sans consigne = machine à réponses ; une formation courte porte les corrections de 41 à 69 % | 2 | [fiche](huang2026.md) |
| `kalyuga2004` — Kalyuga and Sweller (2004) | D2 | test rapide « quelle est l'étape suivante ? » : corrélation 0,92 avec un test complet | 2 | [fiche](kalyuga2004.md) |
| `kalyuga2008` — Kalyuga (2008) | E3, D2 | graphes de fonctions : images fixes numérotées meilleures que l'animation pour les novices (gain 2,56 contre 0,50) ; chez les avancés, avantage de l'animation non significatif | 2 | [fiche](../E_multimedia/kalyuga2008.md) |
| `reisslein2006` — Reisslein et al. (2006) | D2, D1 | circuits : paires exemple-problème pour les faibles, problème-exemple pour les forts | 2 | [fiche](reisslein2006.md) |
| `salden2009` — Salden et al. (2009) | D2 | version courte de salden2010 : estompage adaptatif meilleur que fixe en transfert différé | 2 | [fiche](salden2009.md) |
| `kim2017` — Kim et al. (2017) | D2 | méta-analyse bayésienne : étayage g = 0,39 en apprentissage par problèmes | 3 | à lire |
| `leppink2011` — Leppink et al. (2011) | D2 | statistiques : exemples pour les novices, argumentation pour les avancés | 3 | à lire |
| `vo2025` — Vo et al. (2025) | D2 | revue en chimie : quand et comment retirer l'étayage reste peu étudié | 3 | à lire |
| `wang2026` — Wang et al. (2026) | D2 | tuteur IA qui guide le plan sans donner la solution, bien reçu | 3 | à lire |
| `alemdag2025` — Alemdag et al. (2025) | D3 | méta-analyse des exemples erronés : g = 0,14, utile si l'erreur est expliquée | 1 | sans fiche : inaccessible |
| `bisra2018` — Bisra et al. (2018) | D3 | méta-analyse : invites d'auto-explication g = 0,55 | 1 | [fiche](bisra2018.md) |
| `zhang2024` — Zhang and Fiorella (2024) | D3 | physique : expliquer ses propres erreurs avec des invites structurées améliore la correction | 1 | [fiche](zhang2024.md) |
| `beege2024` — Beege and Ploetzner (2024) | D3, E1 | vidéo interactive : invites = plus de charge sans gain ; réponses de faible qualité | 2 | [fiche](beege2024.md) |
| `booth2013` — Booth et al. (2013) | D3 | algèbre : exemples erronés utiles à la compréhension conceptuelle | 2 | [fiche](booth2013.md) |
| `dieterich2025` — Dieterich et al. (2025) | D3 | revue : erreur + solution correcte en contraste plus efficace que l'erreur seule | 2 | [fiche](dieterich2025.md) |
| `grosse2007` — Große and Renkl (2007) | D3 | exemples corrects et erronés : utiles seulement aux étudiants déjà solides | 2 | [fiche](grosse2007.md) |
| `loibl2019` — Loibl and Leuders (2019) | D3 | comparer sa tentative ratée à la solution correcte, surtout utile à qui a fait l'erreur | 2 | [fiche](loibl2019.md) |
| `rittlejohnson2017` — Rittle-Johnson et al. (2017) | D3 | maths : effet faible à moyen, plus fort si l'explication est guidée | 2 | [fiche](rittlejohnson2017.md) |
