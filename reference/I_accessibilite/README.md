# Axe I — Accessibilité

Question pour les outils : quelle typographie, quelles formules et quels sous-titres pour que les pages, les quiz et les capsules soient lisibles par tous, y compris au lecteur d'écran ?

## Vue d'ensemble

Cet axe étudie comment rendre un même support utilisable par tous les étudiants, y compris ceux qui ont un handicap visuel ou auditif, une dyslexie ou un trouble de l'attention. Il couvre trois questions pratiques : comment concevoir un cours qui fonctionne pour tous sans adaptation individuelle (la conception universelle de l'apprentissage, CUA, en anglais *universal design for learning*) ; comment présenter le texte et les vidéos (police, taille, espacement, sous-titres) ; comment écrire des formules mathématiques qu'un lecteur d'écran (logiciel qui lit la page à voix haute ou sur un afficheur braille) sait lire et parcourir.

L'axe touche tous les outils Forge, car il porte sur leurs sorties. QuizForge produit des quiz Moodle depuis des classeurs Excel ; ExoForge produit des exercices HTML/SCORM paramétrés avec retours ; tous deux affichent du texte et des formules. CapsuleForge, futur outil de vidéo interactive (ActivePresenter, H5P), est concerné par les sous-titres et la composition des diapositives. DiagForge, qui analyse les résultats et la qualité des questions, sert à vérifier qu'un aménagement d'accessibilité aide vraiment, au lieu de le supposer.

Le public visé est celui de Forge : étudiants de L3 à M2 en mécanique et mathématiques, qui travaillent en ligne. Les études lues portent rarement sur ce public : beaucoup concernent des enfants (polices pour dyslexiques), des lycéens (formules lues à voix haute) ou des étudiants d'autres disciplines. Il faut aussi distinguer deux sortes de preuve : la **preuve technique** (la page se lit au lecteur d'écran, la formule se parcourt) et la **preuve d'apprentissage** (les étudiants réussissent mieux). Les fiches apportent surtout la première.

## Historique du domaine

**La conception universelle : d'abord un cadre.** La conception universelle vient de l'architecture, avec sept principes (usage équitable, flexibilité, tolérance à l'erreur…), et a été transposée à l'enseignement sous la forme de la CUA, qui demande plusieurs façons de présenter une notion, d'engager les étudiants et de les laisser montrer ce qu'ils savent ([Saenen et al., 2026](saenen2026.md) ; [Almeqdad et al., 2023](almeqdad2023.md)). Pendant longtemps, la CUA a été appliquée plus qu'évaluée. Les synthèses arrivent tard : [Capp (2017)](capp2017.md) recense 18 études de 2013 à 2016, [Schreffler et al. (2019)](schreffler2019.md) ne trouvent que quatre études quantitatives dans l'enseignement scientifique supérieur, [Almeqdad et al. (2023)](almeqdad2023.md) font une méta-analyse de 13 études, et [Saenen et al. (2026)](saenen2026.md) dressent l'inventaire des pratiques dans le supérieur. Toutes concluent au manque de preuves sur les résultats.

**Les polices pour dyslexiques : une promesse testée et écartée.** Des polices ont été conçues pour les lecteurs dyslexiques (Dyslexie, OpenDyslexic). Les essais ont suivi : à l'écran, Rello et Baeza-Yates ont fait varier la présentation du texte ([2015](rello2015.md)) puis la police ([2016](rello2016.md)) ; [Marinus et al. (2016)](marinus2016.md) ont montré que le petit gain de la police Dyslexie venait de son espacement ; [Kuster et al. (2017)](kuster2017.md) n'ont trouvé aucun bénéfice sur de grands groupes d'enfants. La méta-analyse d'[Azzarello et al. (2026)](azzarello2026.md) clôt la question pour la forme des lettres. La taille et l'espacement restent la piste sérieuse (Galliussi et al., 2020, non lu).

**Les sous-titres : de la langue seconde aux cours en ligne.** La recherche sur les sous-titres porte surtout sur l'apprentissage d'une langue. Pour les vidéos de cours, [van der Zee et al. (2017)](vanderzee2017.md) testent des vidéos de cours en ligne ouverts (MOOC) et [Van Hoecke et al. (2026)](vanhoecke2026.md) des cours enregistrés ; la qualité des sous-titres automatiques fait l'objet de travaux plus récents (Matthew, 2024, non lu).

**Les mathématiques accessibles : du braille au MathML.** Les lecteurs d'écran lisent une formule comme une ligne de texte et perdent sa structure. Le langage MathML, qui décrit la formule comme un arbre (fraction, numérateur, dénominateur…), permet à un moteur de parole mathématique de la lire et de la faire parcourir. [Frankel et al. (2017)](frankel2017.md) comparent cette lecture au braille chez des lycéens ; à l'université de technologie de Silésie, [Maćkowski et al. (2017](mackowski2017.md), [2018)](mackowski2018.md) construisent une plateforme d'exercices d'analyse à étapes pour étudiants aveugles ; [Chauhan et al. (2019)](chauhan2019.md) montrent ce qu'entend un étudiant sans moteur mathématique. Deux revues ([Klingenberg et al., 2020](klingenberg2020.md) ; [Shoaib et al., 2023](shoaib2023.md)) constatent des études de très petits groupes. Les travaux récents décrivent des chaînes de production complètes, de LaTeX ou de Markdown vers des pages HTML avec MathML ([Gaggi et al., 2026](gaggi2026.md) ; [McMillan et Boyden, 2026](mcmillan2026.md)).

## I1 — Conception universelle, sous-titres et texte lisible

La conception universelle demande de prévoir dès le départ plusieurs représentations d'une notion (texte, figure décrite, formule lisible, vidéo sous-titrée), plusieurs façons de répondre et plusieurs leviers d'engagement. C'est un cadre de conception utile, mais ses effets sur la réussite ne sont pas démontrés : les chiffres élevés publiés viennent d'études avant-après sans groupe témoin ([Almeqdad et al., 2023](almeqdad2023.md) ; [Capp, 2017](capp2017.md) ; [Schreffler et al., 2019](schreffler2019.md) ; [Saenen et al., 2026](saenen2026.md)). Interrogés, des étudiants en situation de handicap disent surtout manquer de pratiques simples : plan en début de cours, synthèses, retours rapides ([Li et al., 2024](li2024.md)).

Pour le texte, la question est de savoir ce qui aide vraiment les lecteurs en difficulté, sans gêner les autres. Les polices « dyslexie » n'aident pas ([Azzarello et al., 2026](azzarello2026.md) ; [Kuster et al., 2017](kuster2017.md) ; [Marinus et al., 2016](marinus2016.md)). À l'écran, l'italique ralentit ([Rello et Baeza-Yates, 2016](rello2016.md)), un texte trop petit ou trop serré aussi, alors que les couleurs, l'interligne ou la largeur de colonne n'ont pas d'effet mesurable ([Rello et Baeza-Yates, 2015](rello2015.md)).

Pour les vidéos, les sous-titres sont indispensables aux étudiants sourds ou malentendants ; la question est de savoir s'ils gênent les autres. Les deux études lues répondent que non, et montrent que la composition de l'image compte davantage ([van der Zee et al., 2017](vanderzee2017.md) ; [Van Hoecke et al., 2026](vanhoecke2026.md)).

## I2 — Mathématiques accessibles

Une formule en image ou dans un PDF issu de LaTeX est muette pour un lecteur d'écran, ou lue comme une suite de symboles sans structure : « X is equal to b b two four a c two a » pour la formule du second degré ([Chauhan et al., 2019](chauhan2019.md)). La voie technique qui fait consensus est la page HTML avec MathML, rendue par MathJax, qui expose la structure de la formule à la voix et au braille et permet de la parcourir élément par élément ([Gaggi et al., 2026](gaggi2026.md) ; [Frankel et al., 2017](frankel2017.md)). Encore faut-il que la page soit le support principal et non une annexe du PDF ([McMillan et Boyden, 2026](mcmillan2026.md)).

Au-delà de la formule, l'exercice lui-même doit être utilisable sans la vue : découpage en étapes vérifiées une à une, retour pour chaque erreur typique, interaction entière au clavier ([Maćkowski et al., 2017](mackowski2017.md) ; [Maćkowski et al., 2018](mackowski2018.md)). Cette structure est celle des exercices d'ExoForge. Les preuves restent minces : études de prototypes sur 3 à 16 élèves, rarement dans le supérieur ([Klingenberg et al., 2020](klingenberg2020.md) ; [Shoaib et al., 2023](shoaib2023.md)).

## Ce que disent les fiches

Synthèse rédigée à partir des 20 fiches de lecture écrites (6 de priorité 1, 14 de priorité 2). Elle ne dit que ce que ces fiches soutiennent ; le niveau de preuve suit l'échelle de [fiches_methode.md](../fiches_methode.md). Pour chaque point, on indique ce que les fiches de priorité 2 changent.

**1. Pas de police « dyslexie », pas d'italique pour le texte suivi.** Sur 15 études, les polices conçues pour les dyslexiques (OpenDyslexic, Dyslexie) ne font lire ni plus vite ni plus juste qu'Arial ou Times (g = −0,04) ([Azzarello et al., 2026](azzarello2026.md), niveau B chez l'enfant, C pour nos étudiants). À l'écran, sur 12 polices, l'italique ralentit et déplaît, OpenDyslexic n'aide pas ([Rello et Baeza-Yates, 2016](rello2016.md), niveau C). Les fiches P2 **confirment** et expliquent : chez 170 puis 147 enfants, la police Dyslexie n'est lue ni plus vite ni plus juste qu'Arial, et c'est la moins préférée ([Kuster et al., 2017](kuster2017.md), niveau B chez l'enfant) ; chez 39 enfants faibles lecteurs, elle fait lire 7 % plus vite qu'Arial, mais l'avantage disparaît quand on donne à Arial le même espacement entre lettres et entre mots ([Marinus et al., 2016](marinus2016.md), niveau C). Ce n'est donc pas la forme des lettres qui compte, c'est l'espacement.

**2. Taille et espacement : un texte assez grand, jamais serré (point nouveau).** Sur huit paramètres testés à l'écran chez 92 lecteurs, dyslexiques ou non, dont 49 étudiants ou diplômés du supérieur, seuls deux changent la durée des fixations du regard : la taille (14 pt plus lent que 22 à 26 pt, environ 20 % de plus chez les dyslexiques et 17 % chez les autres) et l'interlettrage (resserré de 7 %, plus lent qu'élargi de 7 ou 14 %) ([Rello et Baeza-Yates, 2015](rello2015.md), niveau C). Les couleurs, le gris du texte ou du fond, l'interligne, l'espacement des paragraphes et la largeur de colonne n'ont pas d'effet mesurable ; le texte noir est seulement préféré. Cette étude ne teste pas les polices (c'est l'étude de 2016). La mesure, des fixations sur des fragments très courts, reste loin de la lecture d'un énoncé.

**3. La conception universelle est un cadre, pas un résultat.** Dans l'enseignement scientifique supérieur, seules quatre études quantitatives évaluaient la CUA en 2019, sans gain de notes démontré ([Schreffler et al., 2019](schreffler2019.md), niveau B pour ce constat, D pour l'efficacité). Les fiches P2 **confirment** : la méta-analyse de 13 études annonce un effet de g = 3,56, mais il vient d'études avant-après sans témoin ; les trois études avec groupe témoin donnent 0,69, non significatif ([Almeqdad et al., 2023](almeqdad2023.md), niveau B pour ce constat). La revue de 18 études de [Capp (2017)](capp2017.md), malgré son titre, ne calcule pas d'effet combiné et juge l'effet sur les résultats non démontré ; elle signale, en chimie, un effet positif pour les élèves en situation de handicap (+0,97) et négatif pour les autres (−0,49) dans une même étude (niveau C). La revue de 16 publications de [Saenen et al. (2026)](saenen2026.md) est un catalogue de pratiques sans aucun lien causal établi. Enfin, 160 étudiants en situation de handicap jugent rares le plan en début de cours (2,71 sur 5), les synthèses (2,99) et les retours rapides (2,87) ([Li et al., 2024](li2024.md)) : ce sont des perceptions de fréquence, pas des effets mesurés (niveau D pour les règles qui en découlent). Conséquence nouvelle pour DiagForge : un gain avant-après sans comparaison ne prouve rien (niveau B).

**4. Des formules en MathML, jamais en image.** Une chaîne LaTeX → HTML5 avec MathML et MathJax 4 rend les formules lisibles à la voix et en braille, et navigables élément par élément ; six utilisateurs aveugles ou malvoyants la jugent utilisable (74,6 sur 100), avec des erreurs de lecture sur la portée des racines et la notation f(x) ([Gaggi et al., 2026](gaggi2026.md), niveau C, preuve technique). Les fiches P2 **renforcent** la règle et apportent une première mesure de réussite : avec des formules en MathML lues par un moteur de parole mathématique et parcourues au clavier, 21 lycéens aveugles ou malvoyants réussissent des questions d'algèbre aussi bien qu'en braille ou en gros caractères (0,762 contre 0,756 de réussite par question) ([Frankel et al., 2017](frankel2017.md), niveau C : analyse descriptive, lycéens, conflit d'intérêts signalé). Elles **nuancent** aussi : sans moteur mathématique, un lecteur d'écran lit le MathML aussi mal que le LaTeX ([Chauhan et al., 2019](chauhan2019.md), niveau C, constat technique sur 3 formules) ; il faut donc écouter les formules produites. Des descriptions vocales qui marquent le début et la fin de chaque bloc (« fraction … fin de fraction ») sont mieux comprises qu'une description simple, surtout pour les formules complexes (médianes de 80 à 90 % contre 40 à 80 %) ([Maćkowski et al., 2017](mackowski2017.md), niveau C : compréhension déclarée, 20 participants). Dans cette plateforme, les formules sont des images doublées de descriptions rédigées à la main, qui coûtent 2 à 5 h par exercice ([Maćkowski et al., 2018](mackowski2018.md)) : c'est un argument pour le MathML généré automatiquement (niveau D). Les longues expressions et les fractions imbriquées restent difficiles à l'oral ([Frankel et al., 2017](frankel2017.md) ; [Maćkowski et al., 2017](mackowski2017.md)).

**5. La page web accessible doit être la version principale.** Une chaîne gratuite Markdown + TeX → HTML + MathML se met en place en 1 à 2 heures et se republie en une commande ; produire un PDF principal et une version accessible « annexe » conduit à négliger cette dernière ([McMillan et Boyden, 2026](mcmillan2026.md), niveau D). Le gain de notes rapporté en Calculus II ne peut pas être attribué au site (un seul enseignant, accessibilité non testée). [Maćkowski et al. (2018)](mackowski2018.md) **confirment** l'intérêt d'une source texte unique compilée en page web et en version accessible (niveau D, rapport de conception).

**6. Des exercices à étapes, utilisables au clavier (point nouveau).** Une plateforme d'exercices d'analyse découpés en étapes vérifiées une à une, avec un retour pour chaque erreur typique, est utilisée par des étudiants aveugles et malvoyants ; 23 étudiants en situation de handicap la jugent utilisable (ergonomie et accès complet au clavier jugés bons par 92 %), mais sans groupe témoin ni mesure d'apprentissage ([Maćkowski et al., 2017](mackowski2017.md) ; [Maćkowski et al., 2018](mackowski2018.md), niveau D pour l'efficacité). C'est la structure d'ExoForge. Les deux revues du domaine invitent à la prudence : 13 études de 3 à 16 élèves, une seule dans le supérieur ([Klingenberg et al., 2020](klingenberg2020.md)) ; 72 articles résumés sans évaluation de la qualité ([Shoaib et al., 2023](shoaib2023.md)). Elles recommandent de ne pas faire de la voix le seul accès : la page doit rester lisible en braille et à l'agrandissement (niveau D).

**7. Les sous-titres ne gênent pas ; l'image compte davantage.** Dans des cours enregistrés de 7 minutes, les sous-titres sont très regardés mais ne dégradent ni la compréhension ni la charge ressentie, même avec des diapositives ; le diaporama commenté fait mieux que l'enseignant filmé seul ([Van Hoecke et al., 2026](vanhoecke2026.md), niveau C). La fiche P2 **renforce** ce résultat : dans un essai préenregistré sur 125 spectateurs non anglophones de vidéos de MOOC, des sous-titres identiques à la narration ne changent ni la réussite (0,04 point sur 10) ni l'effort ressenti, et ce nul est démontré, pas seulement « non significatif » ([van der Zee et al., 2017](vanderzee2017.md), niveau B). La règle « sous-titres sur toutes les capsules » passe donc de C à B. Le même essai montre qu'une vidéo visuellement épurée (textes inutiles retirés, étiquettes qui apparaissent quand elles sont dites et placées près de leur objet) fait gagner 0,62 point sur 10 (d = 0,31, niveau B), sans qu'on sache lequel des quatre changements agit. Dans la revue de [Saenen et al. (2026)](saenen2026.md), 99 % des étudiants d'une étude jugent les sous-titres utiles, sans lien causal avec les notes (niveau D).

## Règles pour ExoForge et QuizForge

| Règle | Outil | Niveau | Fiches |
| --- | --- | --- | --- |
| Pas de police « dyslexie » présentée comme aide ; police standard pour tous | ExoForge, QuizForge | B | azzarello2026, kuster2017, marinus2016, rello2016 |
| Texte courant en police sans empattement courante (Arial, Helvetica, Verdana) ; Computer Modern acceptable pour les formules | ExoForge, QuizForge | C | rello2016 |
| Pas de paragraphe ni de consigne en italique | ExoForge, QuizForge | C | rello2016 |
| Texte courant (énoncés, retours) en taille généreuse, jamais réduite, en unités relatives (rem, em) pour que l'agrandissement du navigateur fonctionne | ExoForge, QuizForge | C | rello2015 |
| Jamais d'interlettrage resserré (pas de `letter-spacing` négatif) ; espacement normal ou légèrement augmenté | ExoForge | C | rello2015 |
| Texte foncé sur fond clair uni, pas de gris clair (préférence des lecteurs ; pas d'effet mesuré sur la lecture) | ExoForge | D | rello2015 |
| Laisser l'étudiant régler police, taille et espacement dans son navigateur (pas de taille fixe en pixels, pas de blocage du zoom) ; une éventuelle option d'aide agit sur l'espacement d'une police standard, au choix de l'étudiant, sans promesse d'efficacité | ExoForge | D | kuster2017, marinus2016, azzarello2026 |
| Formules en MathML (ou TeX rendu par MathJax 4 avec l'exploration au lecteur d'écran activée), jamais en image ni en LaTeX brut | ExoForge, QuizForge | C | gaggi2026, frankel2017, chauhan2019, mcmillan2026 |
| Formules lues par un moteur de parole mathématique et parcourables au clavier ; ne pas se contenter d'un texte de remplacement figé | ExoForge, QuizForge | C | frankel2017 |
| Écouter chaque gabarit de formule avec un lecteur d'écran courant (NVDA) avant diffusion | ExoForge | C | chauhan2019 |
| Lecture vocale avec des mots qui ouvrent et ferment chaque bloc (« fraction … fin de fraction ») ; vérifier que MathJax les produit | ExoForge, QuizForge | C | mackowski2017 |
| Éviter les fractions imbriquées et les longues expressions à parenthèses multiples, ou les poser en plusieurs lignes ou étapes | ExoForge, QuizForge | C | mackowski2017, frankel2017 |
| Corriger une lecture incorrecte par les réglages du moteur de lecture, pas en imposant un texte parlé pour toute la formule (qui casse la navigation) | ExoForge | D | frankel2017 |
| Formules générées automatiquement en MathML plutôt que décrites à la main (2 à 5 h par exercice) | ExoForge | D | mackowski2018 |
| Toute l'interaction (choix, champs, listes, bouton suivant) au clavier et annoncée par le lecteur d'écran | QuizForge, ExoForge | C | mackowski2018 |
| Exercice découpé en étapes vérifiées une à une, avec un retour prévu pour chaque erreur typique | ExoForge | D | mackowski2017, mackowski2018 |
| Ne pas faire de la voix le seul accès : formule lisible aussi en braille (via le MathML) et à l'agrandissement | ExoForge | D | klingenberg2020, shoaib2023 |
| Bouton d'aide (indice sur la suite) accessible au lecteur d'écran à chaque étape | ExoForge | D | shoaib2023 |
| Attribut `lang="fr"` sur la page | ExoForge, QuizForge | C | gaggi2026 |
| Pas de tableau de mise en page ; équations centrées par CSS | ExoForge | C | gaggi2026 |
| Page fluide, sans largeur fixe, qui supporte l'agrandissement ; lien d'évitement vers le contenu | ExoForge | C | gaggi2026 |
| Source texte unique (Markdown + TeX) ; la page HTML + MathML est le support principal, le PDF en dérive | ExoForge | D | mcmillan2026, mackowski2018 |
| Republication en une commande, pour que les corrections atteignent la version accessible | ExoForge | D | mcmillan2026 |
| Plusieurs représentations d'une notion (texte, figure décrite, formule lisible, vidéo sous-titrée), sans promesse de gain | ExoForge | D | schreffler2019, almeqdad2023, capp2017, saenen2026 |
| Schémas des énoncés sans texte décoratif, étiquettes placées près de leur objet | ExoForge | C | vanderzee2017 |
| Synthèse des points clés de chaque module, consultable hors séance en page HTML accessible | ExoForge | D | li2024 |
| Quiz d'entraînement à tentatives multiples avec retour, distincts des quiz notés (tolérance à l'erreur) | QuizForge | D | saenen2026 |
| Notice courte des réglages d'accessibilité de MathJax (langue de la voix, braille) | ExoForge | D | gaggi2026 |

## Règles pour CapsuleForge

| Règle | Niveau | Fiches |
| --- | --- | --- |
| Sous-titres identiques à la narration sur toutes les capsules, y compris avec diapositives (était C) | B | vanderzee2017, vanhoecke2026 |
| Épurer l'image : retirer textes et étiquettes inutiles, faire apparaître chaque étiquette quand elle est dite, signaler l'élément commenté, placer les étiquettes près de leur objet | B | vanderzee2017 |
| Diaporama commenté à mots-clés plutôt que l'enseignant filmé seul | C | vanhoecke2026 |
| Sous-titres et texte des diapositives dans la même langue | C | vanhoecke2026 |
| Texte des diapositives en grande taille, sans interlettrage resserré, foncé sur fond clair | C | rello2015 |
| Transcription téléchargeable pour chaque capsule | D | saenen2026 |
| Annoncer le plan au début de chaque capsule et résumer les points clés à la fin | D | li2024 |

## Règles pour DiagForge

| Règle | Niveau | Fiches |
| --- | --- | --- |
| Évaluer un aménagement d'accessibilité par la réussite, avec un groupe témoin ou une comparaison entre versions, jamais par un gain avant-après seul ni par la seule satisfaction | B | almeqdad2023, schreffler2019, klingenberg2020, saenen2026 |
| Quand c'est possible et consenti, restituer l'effet d'un aménagement séparément pour les étudiants qui en bénéficient et pour les autres : il peut être positif pour les uns et négatif pour les autres | C | capp2017 |
| Compter les erreurs par étape pour proposer l'exercice suivant, sans présenter cette progression comme une preuve d'efficacité | D | mackowski2018 |
| Pour repérer les manques d'un cours, interroger les étudiants sur la fréquence de pratiques précises (plan, synthèse, retour, choix de formats) plutôt que sur leur satisfaction | D | li2024 |

Ces règles sont reprises sous forme lisible par un programme dans l'en-tête de chaque fiche (champ `regles`).

## Ce qui reste ouvert

- Aucune fiche ne mesure, avec comparaison, l'apprentissage d'étudiants du supérieur en situation de handicap : Frankel et al. (2017) portent sur des lycéens en algèbre de base, Maćkowski et al. (2017, 2018) sur une compréhension déclarée ou une utilisabilité, et une seule des 13 études revues par Klingenberg et al. (2020) concerne des étudiants.
- La lecture vocale des formules de mécanique (vecteurs, dérivées partielles, intégrales, indices, unités), en français, par MathJax 4 n'a été testée par personne ; Gaggi et al. (2026) signalent déjà des erreurs sur les racines et f(x). Essai proposé : faire recopier ou calculer des formules entendues, avec et sans marqueurs de structure, et noter la réussite plutôt que l'avis (Maćkowski et al., 2017).
- La combinaison voix + afficheur braille, jugée la plus prometteuse, n'a pas été testée (Frankel et al., 2017 ; Klingenberg et al., 2020).
- Taille et espacement : l'effet n'est mesuré que sur la durée des fixations (Rello et Baeza-Yates, 2015) ou chez des enfants sur papier (Marinus et al., 2016). Essai proposé : deux tailles de base tirées au sort dans ExoForge (1 rem et 1,25 rem), sur le temps par énoncé et la réussite. Le rôle de l'espacement des mots reste à lire (`galliussi2020`, priorité 3).
- Sous-titres : van der Zee et al. (2017) portent sur des spectateurs non natifs en anglais ; rien sur des étudiants francophones dans leur langue, ni sur des sous-titres automatiques non relus (`matthew2024`, priorité 3, non lue).
- Épuration des capsules : on ne sait pas lequel des quatre changements (retrait du superflu, apparition progressive, signalement, étiquettes proches) agit (van der Zee et al., 2017).
- CUA : l'effet inverse selon le public observé en chimie (Capp, 2017) n'a pas été recherché ailleurs ; les critiques de mise en œuvre de la CUA restent à lire (`zhang2024b`, priorité 3).
- Figures et schémas de mécanique (descriptions, graphiques tactiles ou sonifiés) : aucune fiche ; les dispositifs tactiles restent des prototypes (Klingenberg et al., 2020).
- Accessibilité des interactions H5P et SCORM (glisser-déposer, zones cliquables) au lecteur d'écran : rien trouvé.
- Une étude plus récente de l'équipe de Silésie (Maćkowski et al., 2022, 30 lycéens), signalée par Shoaib et al. (2023), n'est pas dans la bibliographie.

Chacune de ces questions peut faire l'objet d'un essai avec ExoForge, QuizForge, CapsuleForge ou DiagForge ; les fiches proposent le dispositif (rubrique « Pour conclure, il faudrait »).

## Références

Références complètes : [`../forge.bib`](../forge.bib). La colonne « Fiche » donne le lien quand la fiche est écrite, sinon la raison de son absence.

| Réf. (forge.bib) | Sous-axe | Apport | Priorité | Fiche |
| --- | --- | --- | --- | --- |
| `azzarello2026` — Azzarello et al. (2026) | I1 | méta-analyse de 15 études : polices « dyslexie » sans effet (g = −0,04) | 1 | [fiche](azzarello2026.md) |
| `rello2016` — Rello and Baeza-Yates (2016) | I1 | à l'écran, 12 polices : l'italique ralentit, sans empattement = fixations plus courtes ; OpenDyslexic n'aide pas | 1 | [fiche](rello2016.md) |
| `schreffler2019` — Schreffler et al. (2019) | I1 | revue CUA en STEM : quatre études quantitatives dans le supérieur, aucun gain de notes démontré | 1 | [fiche](schreffler2019.md) |
| `vanhoecke2026` — Van Hoecke et al. (2026) | I1 | sous-titres sans gêne, même avec diapositives ; les diapositives comptent plus que les sous-titres | 1 | [fiche](vanhoecke2026.md) |
| `almeqdad2023` — Almeqdad et al. (2023) | I1 | méta-analyse de 13 études avant-après : g = 3,56 annoncé, mais 0,69 non significatif dans les 3 études avec groupe témoin | 2 | [fiche](almeqdad2023.md) |
| `capp2017` — Capp (2017) | I1 | revue de 18 études (sans effet combiné malgré son titre) : processus amélioré, effet sur les résultats non démontré | 2 | [fiche](capp2017.md) |
| `kuster2017` — Kuster et al. (2017) | I1 | police Dyslexie : aucun bénéfice de lecture chez 170 puis 147 enfants, dyslexiques ou non ; police la moins préférée | 2 | [fiche](kuster2017.md) |
| `li2024` — Li et al. (2024) | I1 | enquête auprès de 160 étudiants en situation de handicap : plan, synthèses, retours et évaluations flexibles jugés rares ; perceptions, aucun effet mesuré | 2 | [fiche](li2024.md) |
| `marinus2016` — Marinus et al. (2016) | I1 | police Dyslexie 7 % plus rapide qu'Arial chez 39 enfants, gain qui disparaît à espacement égal : l'espacement compte, pas la forme des lettres | 2 | [fiche](marinus2016.md) |
| `rello2015` — Rello and Baeza-Yates (2015) | I1 | à l'écran, 8 paramètres (sans les polices) : 14 pt plus lent que 22-26 pt, interlettrage resserré plus lent ; couleurs, interligne, largeur de colonne sans effet | 2 | [fiche](rello2015.md) |
| `saenen2026` — Saenen et al. (2026) | I1 | revue de 16 publications : catalogue de pratiques de conception universelle dans le supérieur, aucun lien causal avec les résultats | 2 | [fiche](saenen2026.md) |
| `vanderzee2017` — van der Zee et al. (2017) | I1 | vidéos de MOOC : sous-titres identiques à la narration sans effet ni coût (0,04 point sur 10) ; image épurée +0,62 point sur 10 (d = 0,31) | 2 | [fiche](vanderzee2017.md) |
| `galliussi2020` — Galliussi et al. (2020) | I1 | espacement des lettres utile seulement avec un espacement des mots ajusté (d'après le résumé) | 3 | sans fiche : priorité 3, non lue |
| `matthew2024` — Matthew (2024) | I1 | format des sous-titres et compréhension : sous-titres automatiques mal synchronisés (d'après le résumé) | 3 | sans fiche : priorité 3, non lue |
| `zhang2024b` — Zhang et al. (2024) | I1 | revue des difficultés de mise en œuvre de la CUA : définitions floues, couverture inégale (d'après le résumé) | 3 | sans fiche : priorité 3, non lue |
| `gaggi2026` — Gaggi et al. (2026) | I2 | conversion de notes LaTeX en HTML + MathML/MathJax lisibles au lecteur d'écran et en braille | 1 | [fiche](gaggi2026.md) |
| `mcmillan2026` — McMillan and Boyden (2026) | I2 | chaîne Markdown → HTML + MathML gratuite, étude sur 31 sections de Calculus II (un seul enseignant, accessibilité non testée) | 1 | [fiche](mcmillan2026.md) |
| `chauhan2019` — Chauhan et al. (2019) | I2 | 3 formules lues par NVDA : lecture linéaire inintelligible en LaTeX comme en MathML ; préférence pour MathML argumentée, non testée | 2 | [fiche](chauhan2019.md) |
| `frankel2017` — Frankel et al. (2017) | I2 | MathML lu par un moteur de parole et parcouru au clavier : 21 lycéens réussissent comme en braille ou gros caractères (0,76 par question) | 2 | [fiche](frankel2017.md) |
| `klingenberg2020` — Klingenberg et al. (2020) | I2 | revue de 13 études : audio et tactile prometteurs, mais 3 à 16 élèves par étude et preuves insuffisantes | 2 | [fiche](klingenberg2020.md) |
| `mackowski2017` — Maćkowski et al. (2017) | I2 | exercices d'analyse en étapes vérifiées une à une ; descriptions vocales à marqueurs de structure mieux comprises (compréhension déclarée, 20 participants) | 2 | [fiche](mackowski2017.md) |
| `mackowski2018` — Maćkowski et al. (2018) | I2 | même plateforme : chaîne TeX → exercices à étapes accessibles ; formules en image + descriptions manuelles (2 à 5 h par exercice) ; environ 40 étudiants en situation de handicap parmi 1 000 utilisateurs | 2 | [fiche](mackowski2018.md) |
| `shoaib2023` — Shoaib et al. (2023) | I2 | revue de 72 articles sans évaluation de la qualité : outils surtout pour enfants, approches multimodales jugées préférables | 2 | [fiche](shoaib2023.md) |
