# Axe F — Vidéo interactive

Question pour CapsuleForge (outil de vidéo interactive, en préparation) : quand et comment interrompre une vidéo par une question, et comment concevoir, découper et diffuser une capsule pour qu'elle soit regardée et qu'elle fasse apprendre ?

## Vue d'ensemble

Cet axe étudie la vidéo de cours dans le supérieur et ce qu'on peut y ajouter pour la rendre active. Deux questions le structurent. La première porte sur les questions insérées dans la vidéo : faut-il couper la vidéo par des questions, à quel moment, sous quelle forme, en bloquant la lecture ou non ? La seconde porte sur la conception et la diffusion : quelle durée, quel découpage, faut-il filmer l'enseignant, quelle vitesse de lecture, et comment faire pour que les étudiants ouvrent réellement les vidéos interactives (H5P) déposées dans Moodle ?

Ces questions concernent d'abord CapsuleForge, le futur outil qui produira des capsules interactives à partir de PowerPoint et d'ActivePresenter, puis les déposera dans Moodle en H5P ou en SCORM : où placer les questions, s'il faut arrêter la vidéo, quelle durée viser. Elles concernent aussi DiagForge, qui analyse les résultats et les traces des étudiants : quels indicateurs de visionnage ont un sens, et comment juger qu'une capsule fait apprendre. Elles touchent enfin QuizForge (le quiz noté auquel on relie la capsule) et ExoForge (l'exercice qui suit la capsule et la correction écrite qui l'accompagne).

Le public visé est celui des outils Forge : étudiants de L3 à M2 en mécanique et en mathématiques, qui regardent les capsules seuls, en ligne, souvent pour préparer une séance de TD. Les études lues en sont assez loin. La plupart sont des expériences de laboratoire d'une seule séance, sur des cours filmés de psychologie, de statistique ou de biologie ; les grandes études d'usage portent sur des MOOC ou sur des cours de médecine. La base de preuves sur la vidéo vient à plus de 80 % des études en santé ([Trenholm et Marmolejo-Ramos, 2024](trenholm2024.md)). Un seul essai randomisé porte sur des étudiants en génie mécanique ([Zhu et al., 2022](zhu2022.md)).

## Historique du domaine

**2013-2016 : la vidéo devient un objet d'expérience.** Avec les cours en ligne, des psychologues de la mémoire se demandent comment garder l'attention devant un cours filmé. L'étude fondatrice de [Szpunar, Khan et Schacter (2013)](szpunar2013.md) coupe un cours filmé en segments et fait répondre à de courtes questions entre les segments (questions intercalées, *interpolated tests*) : les étudiants décrochent moins et retiennent mieux. La même équipe montre ensuite que ces rappels aident à relier les segments entre eux ([Jing, Szpunar et Schacter, 2016](jing2016.md)), et Szpunar (2017) en fait une synthèse : mieux vaut questionner pour maintenir l'attention que chercher à détecter les décrochages. Au même moment, l'analyse de 6,9 millions de sessions de visionnage sur la plateforme edX par [Guo, Kim et Rubin (2014)](guo2014.md) donne naissance à la « règle des 6 minutes ». [Brame (2016)](brame2016.md) rassemble ces résultats en principes pratiques pour les enseignants.

**2017-2021 : les synthèses et les premiers essais en cours réel.** La méta-analyse de [Noetel et al. (2021)](noetel2021b.md) rassemble 105 essais randomisés dans le supérieur et établit que la vidéo aide surtout quand elle s'ajoute au cours. Les questions posées avant le contenu (prétests) sont testées en laboratoire et en ligne ([Pan et al., 2020](pan2020.md)), et les questions qui interrompent la vidéo sont évaluées dans un vrai cours de biologie ([Haagsman et al., 2020](haagsman2020.md)). Fyfield et al. (2019) publient des recommandations de conception dans un éditorial.

**2022-2026 : réplications, usage réel et H5P.** Une réplication sur 195 étudiants trouve un effet plus petit des questions sur l'attention et aucun gain au test ([Welhaf et al., 2022](welhaf2022.md)). Les études se déplacent vers les cours réels et la plateforme H5P, qui permet d'insérer des questions dans une vidéo sous Moodle : MOOC ([Thurner et al., 2022](thurner2022.md)), cours d'ingénierie ([Jiang et al., 2022](jiang2022.md) ; [Zhu et al., 2022](zhu2022.md)), cours de psychologie en ligne ([Jacob et Centofanti, 2023](jacob2023.md)), classes inversées ([Deng et Gao, 2023](deng2023.md) ; [Deng et al., 2024](deng2024.md) ; [Gutiérrez-González et al., 2024](gutierrez2024.md)). Elles montrent que le premier obstacle est l'usage. D'autres travaux reviennent sur des idées reçues : l'enseignant à l'écran n'aide pas à apprendre ([Alemdag, 2022](alemdag2022.md)), la règle des 6 minutes ne vaut que pour le visionnage d'une traite ([Parker et al., 2024](parker2024.md)), et la méta-analyse de Noetel et al. repose presque entièrement sur la santé ([Trenholm et Marmolejo-Ramos, 2024](trenholm2024.md)). Les plus récents testent de nouvelles formes de questions : questions préalables combinées à une lecture accélérée ([Liu et Jia, 2024](liu2024.md)), questions laissées visibles pendant toute la vidéo ([Zhou et al., 2026](zhou2026.md)).

## F1 — Questions insérées dans les vidéos

L'idée vient de l'effet de test : se rappeler une information renforce sa mémorisation plus que la relire. Dans une vidéo, on l'applique en coupant le cours en segments de quelques minutes et en faisant répondre à une question après chacun. En laboratoire, l'effet est grand : après chaque segment de 5 min, répondre à des questions ou écrire de mémoire ce qu'on a retenu fait nettement mieux que relire les questions corrigées ou les diapositives ([Szpunar et al., 2013](szpunar2013.md) ; [Jing et al., 2016](jing2016.md)). Mais les études sont petites (16 à 18 étudiants par groupe) et la réplication sur un grand effectif trouve un effet faible sur l'attention et aucun gain au test ([Welhaf et al., 2022](welhaf2022.md)). L'attention est mesurée par des sondes : à des moments imprévus, on demande à l'étudiant « à quoi pensiez-vous à l'instant ? », et on compte les réponses hors sujet (décrochage, *mind wandering*).

La forme et le moment des questions comptent. Des questions posées avant le contenu aident aussi, qu'elles soient regroupées au début ou placées avant chaque segment ([Pan et al., 2020](pan2020.md)) ; elles limitent la perte quand la vidéo est accélérée ([Liu et Jia, 2024](liu2024.md)). Arrêter la vidéo n'est pas nécessaire : des questions affichées avec leur solution font aussi bien que des questions bloquantes ([Deng et al., 2024](deng2024.md)), et des questions laissées visibles dans un panneau à côté de la vidéo soutiennent l'attention mieux qu'un prétest ([Zhou et al., 2026](zhou2026.md)). En classe inversée réelle, l'effet est plus faible : petit gain global avec des questions bloquantes ([Haagsman et al., 2020](haagsman2020.md)), aucun effet avec de simples vrai/faux quand la séance suivante reprend le contenu ([Deng et Gao, 2023](deng2023.md)).

Quatre références de priorité 3 n'ont pas été lues : auto-explications écrites aux pauses (Ebbert et al., 2024), accélération de la vidéo pour gagner le temps des questions (Risko et al., 2024), synthèse de Szpunar (2017), effet des questions préalables selon la motivation (Yang et al., 2021).

## F2 — Conception, durée des vidéos et H5P

La vidéo aide à apprendre, surtout en complément du cours ([Noetel et al., 2021](noetel2021b.md)) ; l'effet d'un remplacement est plus faible dans les disciplines « dures » comme la physique ou les mathématiques ([Trenholm et Marmolejo-Ramos, 2024](trenholm2024.md)). Pour la fabrication, les principes connus sont de maîtriser la charge cognitive (signaler l'essentiel, découper, élaguer), de garder les vidéos courtes et de les associer à une activité ([Brame, 2016](brame2016.md)). Filmer le visage de l'enseignant augmente la motivation déclarée mais pas l'apprentissage ([Alemdag, 2022](alemdag2022.md)).

Sur la durée, la règle des 6 minutes vient du temps passé dans une seule session sur edX, pas de l'apprentissage ([Guo et al., 2014](guo2014.md)). Avec des traces sur plusieurs sessions, on voit qu'une vidéo longue est moins vue d'une traite mais plus vue au total ([Parker et al., 2024](parker2024.md)). Le seul essai qui compare directement une vidéo longue et la même découpée en capsules, chez des étudiants en génie mécanique, est favorable aux capsules ([Zhu et al., 2022](zhu2022.md)).

Sur H5P en pratique, les études sont des essais en cours réel ou des études de traces. Leur message commun : une forte part des étudiants n'ouvre pas les vidéos ou ne fait pas les activités ([Jacob et Centofanti, 2023](jacob2023.md) ; [Gutiérrez-González et al., 2024](gutierrez2024.md)), ce qui va avec le calendrier et le lien à une tâche obligatoire plus qu'avec la présence de questions. Les questions H5P changent surtout la navigation dans la vidéo ([Thurner et al., 2022](thurner2022.md)) ; le retour d'expérience en ingénierie de [Jiang et al. (2022)](jiang2022.md) est utile pour la conception (TP filmés, coût de préparation) plus que pour ses chiffres. Deux références n'ont pas de fiche : l'éditorial de Fyfield et al. (2019) et la revue de 30 études H5P de Ki (2025), de priorité 3.

## Ce que disent les fiches

Synthèse rédigée à partir des 20 fiches de lecture écrites (9 de priorité 1 et 11 de priorité 2 ; 11 fiches ajoutées le 09/11/2026). Elle ne dit que ce que ces fiches soutiennent ; le niveau de preuve suit l'échelle de [fiches_methode.md](../fiches_methode.md).

**1. La vidéo aide, surtout en complément ; moins en remplacement dans nos disciplines.** Sur 105 essais randomisés dans le supérieur, remplacer un enseignement par une vidéo donne un petit gain (g = 0,28) et ajouter des vidéos au cours un gain net (g ≈ 0,8-0,9), ce dernier mêlant l'effet de la vidéo et celui du temps d'étude en plus ([Noetel et al., 2021](noetel2021b.md), niveau B). **Nuancé** par la réanalyse de ces données : plus de 80 % des essais sont en santé, un seul en ingénierie et un seul en physique (niveau B pour ce constat) ; en remplacement, l'effet est plus faible dans les disciplines « dures » (0,15 contre 0,37, comparaison entre études, niveau C), et la différence entre savoir-faire et connaissances n'y est plus significative ([Trenholm et Marmolejo-Ramos, 2024](trenholm2024.md)). L'idée que la vidéo n'aiderait que les apprentissages de bas niveau (faits, procédures) est une hypothèse des auteurs : le niveau cognitif des tests n'est mesuré dans aucune étude (niveau D). La règle « en complément plutôt qu'en remplacement » vaut donc d'autant plus en mécanique et en mathématiques.

**2. Une question après chaque segment aide, surtout si elle fait rappeler activement.** Dans l'étude fondatrice, six questions après chaque segment de 5 min réduisent de moitié les pensées hors sujet et améliorent le test, alors que relire les mêmes questions avec leur réponse n'apporte rien ([Szpunar et al., 2013](szpunar2013.md), 16 étudiants par groupe, niveau C). **Confirmé en laboratoire** : écrire de mémoire ce qu'on a retenu après chaque segment, plutôt que relire les diapositives pendant le même temps, augmente le rappel final de 54 à 68 % et fait davantage relier les segments entre eux, dans deux expériences de 18 étudiants par groupe ([Jing et al., 2016](jing2016.md), niveau C) ; le décrochage déclaré ne baisse pas, mais il pénalise moins. Sur 195 étudiants, la réplication de Szpunar trouve un effet faible sur l'attention (d = 0,29) et aucun gain au test, avec des questions sans retour ([Welhaf et al., 2022](welhaf2022.md), niveau B). **Nuancé en cours réel** : des questions bloquantes améliorent un peu le test sur l'ensemble de la vidéo (79 % contre 75 %), sans améliorer la notion questionnée elle-même ([Haagsman et al., 2020](haagsman2020.md), niveau C) ; 50 vrai/faux intégrés dans des vidéos de préparation de classe inversée ne changent ni la rétention (74 contre 75 sur 100) ni le transfert quand la séance reprend le même contenu ; seul le temps de visionnage baisse d'environ un quart ([Deng et Gao, 2023](deng2023.md), une classe par condition, niveau C). La forme de la question compte : rappel ou application plutôt que vrai/faux ou relecture.

**3. Bloquer la vidéo n'est pas indispensable.** En classe inversée sur six semaines, des questions affichées avec leur solution (l'étudiant met en pause lui-même) donnent le même score que des questions qui arrêtent la vidéo et corrigent, et mieux qu'une vidéo sans questions ([Deng et al., 2024](deng2024.md), une classe par condition, niveau C). **Confirmé pour l'attention, pas pour l'apprentissage** : quatre QCM laissés visibles dans un panneau pendant un cours filmé de 52 min réduisent le décrochage déclaré par rapport aux mêmes QCM montrés seulement avant la vidéo (environ 32 % contre 42 % des sondes, d ≈ 0,35-0,38), surtout sur les passages visés par les questions ; mais aucune condition n'améliore le test final ([Zhou et al., 2026](zhou2026.md), niveau B pour l'attention, D pour l'apprentissage ; consignes différentes entre conditions et pas de groupe sans questions). **Nouveau** : dans un MOOC, les questions H5P servent de repères de navigation : les retours en arrière et les sauts se concentrent autour d'elles ([Thurner et al., 2022](thurner2022.md), niveau C). Avec des essais illimités, près de la moitié des étudiants disent répondre au hasard jusqu'à la bonne réponse ([Haagsman et al., 2020](haagsman2020.md)) ; d'une année à l'autre, la réussite aux questions passe de 64 % avec une tentative à 90 % avec tentatives multiples ([Gutiérrez-González et al., 2024](gutierrez2024.md), niveau C).

**4. Questionner avant le contenu est une option, utile si l'étudiant accélère.** Quelques QCM posés avant la vidéo, même ratés, améliorent le score sur ces questions et, dans une expérience sur deux, sur le reste du cours ; les poser en bloc au début ou avant chaque segment revient au même ([Pan et al., 2020](pan2020.md), niveau C). **Nouveau** : sur une vidéo de 8 min, la lecture à 1,25× ne fait pas baisser les résultats ; à 1,5×, la rétention chute sans questions préalables (3,3 contre 5,0 sur 10), mais pas avec trois questions affichées avant chaque partie (5,3 contre 5,9) ; l'effet propre des questions ne porte que sur la rétention, pas sur le transfert ([Liu et Jia, 2024](liu2024.md), 15 étudiants par groupe, interaction significative de justesse, niveau C). **Nuancé** : des questions montrées seulement avant la vidéo soutiennent moins l'attention que les mêmes questions laissées visibles pendant la lecture ([Zhou et al., 2026](zhou2026.md)).

**5. Le premier obstacle est l'usage ; les questions ne font pas ouvrir les vidéos.** Dans un cours entièrement en ligne, un tiers seulement des étudiants a fait toutes les activités d'une vidéo H5P proposée par un lien, et aucun gain n'a été mesuré ([Jacob et Centofanti, 2023](jacob2023.md), niveau C pour l'usage). **Confirmé par les traces** : dans un cours de médecine en classe inversée, sur deux années, 56 % des inscrits n'ouvrent pas une vidéo donnée (moyenne par vidéo) et 41 % du contenu est vu en moyenne ([Gutiérrez-González et al., 2024](gutierrez2024.md), niveau B pour le constat). Le visionnage est lié au calendrier (vidéos du début de semestre) et au caractère obligatoire de la séance associée (+4,5 et +15 points), et pas à la présence de questions intégrées (niveau C, peu de vidéos sans questions ; l'étude ne mesure pas l'apprentissage). **Précisé** : sur 3,1 millions de vues, le visionnage total est plus élevé quand la vidéo porte des questions notées (1,47 contre 1,24 fois la durée), avec un effet propre faible, et baisse avec la position de la vidéo dans le cours ([Parker et al., 2024](parker2024.md), niveau C). Dans un cours d'ingénierie, les vidéos H5P sont plus ouvertes que les vidéos simples (1,0 contre 0,34 ouverture par étudiant et par vidéo en licence), mais l'écart sur les quiz (environ 0,5 point sur 10) n'est pas testé et les semaines comparées diffèrent ([Jiang et al., 2022](jiang2022.md), niveau C pour l'usage, D pour l'effet). Les gains apparaissent dans les études où la vidéo prépare une séance ou un test noté ([Haagsman et al., 2020](haagsman2020.md) ; [Deng et al., 2024](deng2024.md)).

**6. Satisfaction et motivation ne prouvent rien.** Une forte satisfaction (97 % veulent plus d'interactivité) ne garantit aucun gain ([Jacob et Centofanti, 2023](jacob2023.md)). **Confirmé** : deux tiers des participants d'un MOOC jugent les questions H5P utiles, alors que l'activité totale par utilisateur est voisine avec ou sans questions ([Thurner et al., 2022](thurner2022.md), niveau C) ; l'enseignant à l'écran augmente la motivation déclarée (g = 0,43) sans augmenter l'apprentissage ([Alemdag, 2022](alemdag2022.md), niveau C).

**7. Courte et segmentée, mais la durée ne dit pas tout.** Sur 6,9 millions de sessions edX, la durée médiane de visionnage plafonne vers 6 min et les vidéos de plus de 9 min sont souvent abandonnées avant la moitié ([Guo et al., 2014](guo2014.md), engagement et non apprentissage, niveau C). **Nuancé** : la durée est bien le facteur principal du visionnage d'une traite (au-delà de 6 à 9 min, le quart le moins assidu voit moins de 75 %, puis moins de 50 % de la vidéo), mais le visionnage total par apprenant, sur toutes les sessions, augmente avec la durée et avec les questions notées ([Parker et al., 2024](parker2024.md), niveau B pour le fait que les mesures d'une seule session sous-estiment le visionnage, C pour le reste ; 3 vidéos seulement entre 12 et 15 min). **Nouveau, premier essai direct** : chez 65 étudiants de 1re année de génie mécanique tirés au sort, le même cours en capsules d'environ 8 min plutôt qu'en une vidéo de 55 min est plus regardé (temps médian rapporté à la durée 0,93 contre 0,75) et donne un meilleur examen final (environ 70 contre 64 sur 100) ([Zhu et al., 2022](zhu2022.md), niveau C : petit effectif, incohérences de rapport, le découpage ajoute aussi des titres par notion). Les vidéos de procédure sont rouvertes très souvent pendant la pratique (environ 29 ouvertures par vidéo et par étudiant), d'où l'intérêt de chapitres ([Deng et Gao, 2023](deng2023.md), niveau C). Les principes de conception (signalement, segmentation, élagage, voix sur image, ton conversationnel, activité associée) sont résumés par [Brame (2016)](brame2016.md) (niveaux C à D).

**8. Nouveau : pas d'enseignant à l'écran, mais une capsule pilotable et accessible.** Sur 20 études comparant la même vidéo avec ou sans enseignant à l'écran, la présence de l'enseignant n'améliore ni l'acquisition (g = 0,17, non significatif) ni le transfert, et augmente la charge cognitive déclarée ; le petit avantage n'apparaît qu'en laboratoire, pas en ligne ([Alemdag, 2022](alemdag2022.md), niveau B pour l'absence de gain). Montrer la main qui écrit plutôt que le visage reste une piste (deux études, niveau D). Dans un MOOC, 43 % des répondants lisent la transcription en regardant et plus d'un tiers accélère la vidéo ou active les sous-titres ([Thurner et al., 2022](thurner2022.md), niveau C). Dans un cours d'ingénierie, les corrections écrites sont consultées 3,2 à 3,6 fois par étudiant, les vidéos de démonstration 0,4 à 0,6 fois ; une vidéo H5P demande environ 50 % de préparation en plus (estimation des auteurs) ([Jiang et al., 2022](jiang2022.md), niveaux C et D).

**9. Nouveau : mesurer le visionnage sans se tromper.** Le temps de visionnage n'est pas une mesure d'apprentissage : des questions l'ont réduit d'un quart sans changer les résultats ([Deng et Gao, 2023](deng2023.md), niveau C). Les mesures sur une seule session sous-estiment le visionnage ; il faut cumuler toutes les sessions par étudiant ([Parker et al., 2024](parker2024.md), niveau B) et donner la médiane et la dispersion, car quelques revisionnages multiples tirent la moyenne vers le haut ([Zhu et al., 2022](zhu2022.md), niveau C). Il faut séparer « jamais ouverte », taux de visionnage et part de ceux qui finissent ([Gutiérrez-González et al., 2024](gutierrez2024.md), niveau C), et ne pas juger une capsule H5P en comparant des semaines de cours différentes ([Jiang et al., 2022](jiang2022.md), niveau C).

## Règles pour CapsuleForge, DiagForge et ExoForge

**CapsuleForge — place et forme des questions**

| Règle | Niveau | Fiches |
| --- | --- | --- |
| Proposer les capsules en complément du cours et des TD plutôt qu'en remplacement, a fortiori en mécanique et en mathématiques | B | noetel2021b, trenholm2024 |
| En remplacement d'une séance, garder au moins autant d'activité (questions, exercices) | C | noetel2021b |
| Segments d'environ 5 min, chacun suivi d'au moins une question de compréhension | C | szpunar2013, jing2016, haagsman2020, deng2024 |
| Questions de rappel ou d'application (répondre sans revoir, résumer de mémoire, résoudre), pas un récapitulatif à relire ni de simples vrai/faux | C | szpunar2013, jing2016, deng2023 |
| Dans une capsule longue ou une suite de capsules, prévoir des questions qui relient le segment courant aux précédents | D | jing2016 |
| Après une capsule conceptuelle, une tâche de raisonnement (exercice ExoForge, question ouverte), pas seulement du rappel | D | trenholm2024 |
| Toujours afficher la solution ou une explication après la question | C | deng2024, welhaf2022 |
| L'arrêt automatique n'est pas obligatoire ; prévoir une version « questions affichées » (panneau visible pendant la lecture) en plus de la version bloquante | C | deng2024, zhou2026 |
| Placer les questions aux points clés et sur les passages où l'attention baisse (repérés sur une promotion précédente) ; elles servent aussi de repères de navigation | C | zhou2026, thurner2022 |
| Limiter les essais au hasard : une tentative, puis l'explication ou un renvoi au passage | D | haagsman2020, gutierrez2024 |
| Option : deux à quatre questions avant la vidéo ou avant chaque partie (« la suite répond à : ... »), en bloc ou réparties | C | pan2020, liu2024 |
| Ne pas compter sur les questions seules pour maintenir l'attention (effet faible, sans gain au test) | B | welhaf2022, zhou2026 |
| Ne pas compter sur les questions intégrées pour faire ouvrir ou finir une vidéo | C | gutierrez2024, thurner2022 |

**CapsuleForge — conception et durée**

| Règle | Niveau | Fiches |
| --- | --- | --- |
| Capsule à voir d'une traite (préparation de séance) : moins de 6 min ; capsule de cours ou de révision : jusqu'à 12 min si elle est chapitrée et reliée à des questions notées (au-delà : niveau D) | C | guo2014, parker2024 |
| Découper un cours enregistré en capsules d'une notion complète (7 à 9 min) plutôt que livrer une séance filmée entière | C | zhu2022 |
| Chapitres par étape pour les procédures et les résolutions : les étudiants y reviennent pendant qu'ils pratiquent | C | deng2023, guo2014 |
| Résolutions en écriture pas à pas plutôt qu'en diapositives statiques | C | guo2014 |
| Ne pas incruster le visage de l'enseignant pour améliorer l'apprentissage ; si une présence humaine est souhaitée, la main qui écrit ou pointe (niveau D) | B | alemdag2022 |
| Liste de contrôle : signalement, élagage, voix sur image, texte hors vidéo avec objectif | C | brame2016 |
| Transcription téléchargeable et sous-titres pour chaque capsule ; vitesse de lecture réglable | C | thurner2022 |
| Laisser la vidéo pilotable (pause, retour, notes) | D | deng2024, welhaf2022 |
| Vitesse : 1,25× acceptable ; ne pas proposer 1,5× par défaut pour une capsule sans questions préalables | C | liu2024 |
| TP ou démonstration filmée : menu par étape et questions obligatoires de relevé des valeurs utiles au compte rendu | D | jiang2022 |
| Prévoir environ 50 % de préparation en plus pour une capsule H5P et réutiliser les interactions d'une année sur l'autre | D | jiang2022 |

**CapsuleForge — diffusion dans Moodle**

| Règle | Niveau | Fiches |
| --- | --- | --- |
| Intégrer la capsule dans la page Moodle et la relier à une tâche notée ou obligatoire de la séance ; expliquer à quoi servent les questions | C | jacob2023, haagsman2020, deng2024, gutierrez2024 |
| Associer au moins une question notée à chaque capsule de contenu | C | parker2024 |
| Soigner les capsules du début de semestre et alléger celles des semaines qui précèdent les examens, moins regardées | C | gutierrez2024, parker2024 |
| Relier chaque capsule à une activité de la séance suivante | D | zhu2022 |

**DiagForge**

| Règle | Niveau | Fiches |
| --- | --- | --- |
| Mesurer le visionnage par étudiant et par capsule sur toutes les sessions (temps total rapporté à la durée, part des secondes vues), avec médiane et dispersion | B | parker2024, zhu2022 |
| Par capsule, séparer la part d'inscrits qui ne l'ouvrent jamais, le taux de visionnage et la part de ceux qui la finissent | C | gutierrez2024, jacob2023 |
| Ne pas lire le temps de visionnage comme une mesure d'apprentissage | C | deng2023 |
| Enregistrer la réussite à la première tentative ; ne pas comparer des taux obtenus avec une tentative et avec plusieurs | C | gutierrez2024 |
| Enregistrer les retours en arrière et les sauts autour de chaque question H5P | C | haagsman2020, thurner2022 |
| Repérer dans les traces d'une promotion les passages de décrochage (abandons, sauts, retours) pour y placer des questions l'année suivante | D | zhou2026 |
| Suivre la baisse de visionnage avec la position de la capsule dans le cours et la signaler à l'enseignant | C | parker2024 |
| Séparer les items déjà vus en prétest des items nouveaux | C | pan2020 |
| Analyser l'effet d'une capsule séparément sur les items de rappel ou de procédure et sur les items conceptuels ou de transfert | D | trenholm2024 |
| Juger une capsule sur les résultats, pas sur la satisfaction, l'utilité déclarée, la motivation ou le nombre d'actions | C | jacob2023, noetel2021b, thurner2022, alemdag2022 |
| Ne pas conclure à l'effet d'une capsule à partir d'une comparaison entre semaines de cours ; tirer au sort les versions | C | jiang2022 |

**ExoForge**

| Règle | Niveau | Fiches |
| --- | --- | --- |
| Toujours fournir la correction écrite d'un exercice ; réserver la vidéo de résolution aux exercices difficiles | D | jiang2022 |

Ces règles sont reprises sous forme lisible par un programme dans l'en-tête de chaque fiche (champ `regles`).

## Ce qui reste ouvert

- La taille réelle de l'effet des questions insérées : grande dans les petites études de laboratoire (d de 1,2 à 1,7 chez [Jing et al., 2016](jing2016.md)), faible ou nulle sur le test dans les études plus grandes ([Welhaf et al., 2022](welhaf2022.md) ; [Zhou et al., 2026](zhou2026.md)), petite ou nulle en cours réel ([Haagsman et al., 2020](haagsman2020.md) ; [Deng et Gao, 2023](deng2023.md)). Les essais en classe comparent des classes entières (une classe par condition).
- La forme de la question : l'écart entre rappel actif (effet net en laboratoire) et vrai/faux (aucun effet en classe) n'a jamais été testé dans une même étude.
- L'effet du retour après la question n'a été isolé dans aucune étude lue ; c'est pourtant l'explication avancée de l'absence de gain chez Welhaf et al. (2022).
- Questions visibles, bloquantes ou absentes : aucune étude ne compare les trois dans un cours réel avec une mesure d'apprentissage ([Zhou et al., 2026](zhou2026.md) n'a pas de groupe sans questions).
- Aucune étude lue ne porte sur des démonstrations ou des résolutions de mécanique ; l'essai le plus proche ([Zhu et al., 2022](zhu2022.md)) porte sur du dessin industriel en 1re année, sans questions intégrées. La base de preuves sur la vidéo vient surtout de la santé ([Trenholm et Marmolejo-Ramos, 2024](trenholm2024.md)), et l'hypothèse selon laquelle la vidéo aiderait moins les apprentissages conceptuels reste à tester.
- Presque toutes les mesures sont immédiates ou à une semaine ; seul [Zhu et al. (2022)](zhu2022.md) mesure un examen de fin de semestre, avec un petit effectif.
- Durée : la comparaison « une vidéo longue contre plusieurs capsules » n'a qu'un essai ; les capsules de 12 à 15 min reposent sur 3 vidéos ([Parker et al., 2024](parker2024.md)).
- Vitesse de lecture : elle était imposée dans [Liu et Jia (2024)](liu2024.md) ; on ne sait pas quelle vitesse les étudiants choisissent ni ce qu'elle coûte pour un calcul.
- Usage : les questions intégrées n'augmentent pas le visionnage dans une étude de traces sans tirage au sort ([Gutiérrez-González et al., 2024](gutierrez2024.md)) ; leur effet sur l'apprentissage dans un cours Moodle reste à mesurer, comme le coût réel de préparation d'une capsule H5P ([Jiang et al., 2022](jiang2022.md)).
- Priorité 3 non lue : ebbert2024, risko2024, szpunar2017, yang2021b (F1), ki2025 (F2). fyfield2019 n'a pas de fiche (éditorial sans données).

Chacune de ces questions peut faire l'objet d'un essai avec CapsuleForge ; les fiches proposent le dispositif (rubrique « Pour conclure, il faudrait »).

## Références

Références complètes : [`../forge.bib`](../forge.bib). La colonne « Fiche » donne le lien quand la fiche est écrite.

| Réf. (forge.bib) | Sous-axe | Apport | Priorité | Fiche |
| --- | --- | --- | --- | --- |
| `deng2024` — Deng et al. (2024) | F1, F2 | questions affichées avec solution, sans arrêt imposé, aussi efficaces que des questions bloquantes, et mieux que pas de questions (une classe par condition) | 1 | [fiche](deng2024.md) |
| `haagsman2020` — Haagsman et al. (2020) | F1 | biologie, classe inversée : petit gain global (79 % contre 75 %), aucun gain sur la notion questionnée elle-même | 1 | [fiche](haagsman2020.md) |
| `pan2020` — Pan et al. (2020) | F1 | questions posées avant le contenu : meilleure attention déclarée et meilleur test, réparties ou en bloc ; gain sur les questions nouvelles dans une expérience sur deux | 1 | [fiche](pan2020.md) |
| `szpunar2013` — Szpunar et al. (2013) | F1 | tests courts entre les segments d'un cours filmé : moins de décrochage, plus de notes, meilleur apprentissage (16 par groupe) | 1 | [fiche](szpunar2013.md) |
| `welhaf2022` — Welhaf et al. (2022) | F1 | réplication sur 195 étudiants : moins de pensées hors sujet (d = 0,29), pas de gain au test ; questions sans retour | 1 | [fiche](welhaf2022.md) |
| `deng2023` — Deng and Gao (2023) | F1 | classe inversée, vidéos de procédure : 50 vrai/faux intégrés sans effet sur la rétention (74 contre 75) ni sur le transfert ; seul le temps de visionnage baisse (environ −24 %) ; une classe par condition | 2 | [fiche](deng2023.md) |
| `jing2016` — Jing et al. (2016) | F1 | rappel écrit après chaque segment plutôt que relecture : rappel final +54 à +68 %, plus de liens entre segments ; décrochage déclaré inchangé mais moins pénalisant (laboratoire, 18 par groupe) | 2 | [fiche](jing2016.md) |
| `liu2024` — Liu and Jia (2024) | F1 | vitesse de lecture : 1,25× sans perte ; 1,5× fait chuter les tests sans questions préalables, pas avec trois questions préalables (15 par groupe) | 2 | [fiche](liu2024.md) |
| `zhou2026` — Zhou et al. (2026) | F1 | QCM visibles pendant toute la vidéo : moins de décrochage déclaré qu'avec les mêmes QCM montrés seulement avant (d ≈ 0,35), surtout sur les passages visés ; aucun gain au test final | 2 | [fiche](zhou2026.md) |
| `ebbert2024` — Ebbert et al. (2024) | F1 | auto-explications écrites aux pauses : pas mieux que des QCM | 3 | sans fiche : priorité 3, non lue |
| `risko2024` — Risko et al. (2024) | F1 | accélérer la vidéo pour récupérer le temps pris par les questions | 3 | sans fiche : priorité 3, non lue |
| `szpunar2017` — Szpunar (2017) | F1 | synthèse : questionner pour maintenir l'attention plutôt que détecter les décrochages | 3 | sans fiche : priorité 3, non lue |
| `yang2021b` — Yang et al. (2021) | F1 | pré-questions : transfert amélioré surtout chez les étudiants motivés | 3 | sans fiche : priorité 3, non lue |
| `brame2016` — Brame (2016) | F2 | principes pratiques : charge maîtrisée, vidéos courtes, associées à une activité | 1 | [fiche](brame2016.md) |
| `guo2014` — Guo et al. (2014) | F2 | origine de la règle des 6 minutes : durée de visionnage d'une traite sur edX, pas apprentissage | 1 | [fiche](guo2014.md) |
| `jacob2023` — Jacob and Centofanti (2023) | F2 | vidéos H5P : un tiers seulement termine les activités ; pas de gain mesuré (analyse fragile) | 1 | [fiche](jacob2023.md) |
| `noetel2021b` — Noetel et al. (2021) | F2 | méta-analyse de 105 essais : vidéo en remplacement g = 0,28, en complément g = 0,80-0,88 ; pas d'avantage si l'enseignement remplacé est plus interactif | 1 | [fiche](noetel2021b.md) |
| `alemdag2022` — Alemdag (2022) | F2 | méta-analyse de 20 études : enseignant à l'écran sans gain d'apprentissage (g = 0,17, non significatif), plus de motivation et de charge déclarées ; petit avantage seulement en laboratoire | 2 | [fiche](alemdag2022.md) |
| `fyfield2019` — Fyfield et al. (2019) | F2 | éditorial : recommandations de conception de vidéos pédagogiques, sans données nouvelles | 2 | sans fiche : éditorial de 7 pages sans données |
| `gutierrez2024` — Gutiérrez-González et al. (2024) | F2 | classe inversée en médecine, traces sur deux ans : en moyenne 56 % des inscrits n'ouvrent pas une vidéo donnée ; visionnage lié au calendrier et à la séance obligatoire ; questions intégrées sans effet sur le visionnage (apprentissage non mesuré) | 2 | [fiche](gutierrez2024.md) |
| `jiang2022` — Jiang et al. (2022) | F2 | ingénierie de l'environnement, Moodle : vidéos H5P plus ouvertes que les vidéos simples ; quiz à peine différents (environ 0,5 sur 10), écart non testé, semaines non comparables ; préparation +50 % (estimation) | 2 | [fiche](jiang2022.md) |
| `parker2024` — Parker et al. (2024) | F2 | 3,1 millions de vues : la durée réduit le visionnage d'une traite (au-delà de 6 à 9 min) ; le visionnage total croît avec la durée, les questions notées et une place tôt dans le cours | 2 | [fiche](parker2024.md) |
| `thurner2022` — Thurner et al. (2022) | F2 | MOOC, 1 238 inscrits : les questions H5P ne font pas faire plus d'actions mais concentrent la navigation autour d'elles ; deux tiers les jugent utiles ; la moitié utilise la transcription | 2 | [fiche](thurner2022.md) |
| `trenholm2024` — Trenholm and Marmolejo-Ramos (2024) | F2 | réanalyse de Noetel et al. : plus de 80 % des essais en santé ; remplacement par la vidéo moins utile dans les disciplines « dures » (0,15 contre 0,37) ; la limite aux objectifs de bas niveau est une hypothèse non mesurée | 2 | [fiche](trenholm2024.md) |
| `zhu2022` — Zhu et al. (2022) | F2 | essai randomisé, 65 étudiants de génie mécanique : capsules d'environ 8 min plutôt qu'une vidéo de 55 min, plus regardées et meilleur examen final (environ 70 contre 64 sur 100) | 2 | [fiche](zhu2022.md) |
| `ki2025` — Ki (2025) | F2 | revue de 30 études H5P : avis positifs, peu d'études contrôlées ou longues | 3 | sans fiche : priorité 3, non lue |

Priorité 1 = à lire d'abord. « Fiche » donne le lien vers la fiche de lecture `<clé>.md` de ce dossier, ou la raison de son absence.
