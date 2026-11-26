scripts.forge.forge
===================

.. py:module:: scripts.forge.forge

.. autoapi-nested-parse::

   Forge E-Learning — Atelier : une page dans le navigateur qui lance les outils Forge sans ligne de commande.

   Double-clic sur ``Forge.bat`` (racine du dépôt), ou ``python scripts/forge/forge.py [--port 8770] [--sans-navigateur]``.

   L'atelier ne refait aucun calcul : chaque bouton lance une commande Forge existante (``build.py``, ``capsuleforge``,
   ``quizforge``, ``diagforge``) dans un sous-processus et affiche son journal. Il ne lance que des actions connues, avec des
   options vérifiées (jamais une ligne de commande libre). Le serveur n'écoute que sur cet ordinateur (127.0.0.1), refuse
   les requêtes venues d'un autre site (``serveur_local``) et demande un jeton, tiré au lancement, pour toute action.

   Routes :
     GET  /                      la page (``atelier.html``)
     GET  /api/etat              état du poste, profils, version
     GET  /api/exoforge/fiches   fiches ExoForge trouvées (exemples et data/exoforge)
     GET  /api/capsules          capsules de data/capsuleforge
     GET  /api/capsule/<nom>     état d'une capsule, section par section (``capsules.detail``)
     GET  /api/quizforge/classeurs, /api/diagforge/dossiers   listes des écrans Questions et Bilans
     GET  /api/reglages          réglages de l'atelier (data/_atelier/reglages.json)
     GET  /api/taches            résumé des tâches de la séance
     GET  /api/tache/<id>?depuis=n   lignes du journal d'une tâche à partir de la n-ième
     GET  /dist/<chemin>         fichiers construits (essayer un exercice, ouvrir un lecteur)
     POST /api/lancer            {action, params} : lance une tâche
     POST /api/envoyer           {id, ligne: pause|fin} : commande envoyée à une tâche qui l'accepte (filmer)
     GET  /api/appareils         écrans, caméras et micros (filmer)
     POST /api/arreter           {id} : arrête une tâche
     POST /api/parcourir         {dossier?, types?} : dialogue de fichiers de Windows, renvoie le chemin choisi
     POST /api/montrer           {chemin} : ouvre l'explorateur sur un fichier ou un dossier du dépôt
     POST /api/ouvrir            {chemin} : ouvre un fichier du dépôt avec son programme (Excel, navigateur…)
     POST /api/reglages          {reglages: {profil?, diaporamas?: {}, oublier_diaporama?, retirer_classeur?}} : enregistre les réglages
     (GET et POST /api/reglages donnent aussi ``absents`` : les chemins retenus introuvables)
     POST /api/quitter           arrête l'atelier (refusé si une tâche tourne, sauf {forcer: true})
     POST /api/depart            la page se ferme : arrêt dans 4 s si elle ne revient pas et qu'aucune tâche ne tourne

   Licence : GPL v3.



Attributes
----------

.. autoapisummary::

   scripts.forge.forge.ICI
   scripts.forge.forge.VERSION
   scripts.forge.forge.RACINE
   scripts.forge.forge.PY
   scripts.forge.forge.PORT
   scripts.forge.forge.MAX_LIGNES
   scripts.forge.forge.TYPES
   scripts.forge.forge.WINDOWS
   scripts.forge.forge.ADRESSE


Classes
-------

.. autoapisummary::

   scripts.forge.forge.Tache
   scripts.forge.forge.Atelier


Functions
---------

.. autoapisummary::

   scripts.forge.forge.rel
   scripts.forge.forge.dans_depot
   scripts.forge.forge.fenetres
   scripts.forge.forge.fenetres_explorateur
   scripts.forge.forge.premier_plan
   scripts.forge.forge.lire_fiche
   scripts.forge.forge.profils_campus
   scripts.forge.forge.reglages_absents
   scripts.forge.forge.noms_profils
   scripts.forge.forge.gestionnaire
   scripts.forge.forge.main


Module Contents
---------------

.. py:data:: ICI

.. py:data:: VERSION
   :value: '0.5'


.. py:data:: RACINE

.. py:data:: PY
   :value: '/opt/hostedtoolcache/Python/3.12.16/x64/bin/python'


.. py:data:: PORT
   :value: 8770


.. py:data:: MAX_LIGNES
   :value: 5000


.. py:data:: TYPES

.. py:data:: WINDOWS

.. py:data:: ADRESSE

.. py:function:: rel(p: pathlib.Path) -> str

   Chemin relatif au dépôt, avec des « / » (sinon le chemin absolu).


.. py:function:: dans_depot(chemin: str) -> pathlib.Path

   Chemin absolu d'un fichier du dépôt (ou d'un classeur ajouté, et de son dossier de sortie) ; refuse le reste.


.. py:class:: Tache(ident: str, titre: str, outil: str, argv: list[str], verrou: str | None = None, apres=None, entree: bool = False, genre: str = '')

   Une commande Forge lancée par l'atelier : sous-processus, journal, état.


   .. py:attribute:: apres
      :value: None



   .. py:attribute:: entree
      :value: False



   .. py:attribute:: genre
      :value: ''



   .. py:attribute:: rec
      :value: 'pret'



   .. py:attribute:: lignes
      :type:  list[str]
      :value: []



   .. py:attribute:: retirees
      :value: 0



   .. py:attribute:: debut


   .. py:attribute:: fin
      :type:  float | None
      :value: None



   .. py:attribute:: code
      :type:  int | None
      :value: None



   .. py:attribute:: arretee
      :value: False



   .. py:attribute:: liens
      :type:  dict


   .. py:attribute:: proc
      :type:  subprocess.Popen | None
      :value: None



   .. py:method:: lancer(quand_fini)


   .. py:method:: ajouter(ligne: str)


   .. py:method:: envoyer(ligne: str) -> bool

      Envoie une ligne à la commande (entrée ouverte seulement).



   .. py:method:: arreter()


   .. py:property:: etat
      :type: str



   .. py:method:: resume() -> dict


   .. py:method:: depuis(n: int) -> dict


.. py:class:: Atelier

   État de la séance : tâches, jeton, arrêt.


   .. py:attribute:: jeton


   .. py:attribute:: taches
      :type:  dict[str, Tache]


   .. py:attribute:: ordre
      :type:  list[str]
      :value: []



   .. py:attribute:: verrou


   .. py:attribute:: dialogue


   .. py:attribute:: minuterie
      :type:  threading.Timer | None
      :value: None



   .. py:attribute:: montres
      :type:  dict[str, float]


   .. py:attribute:: page_partie_le
      :type:  float | None
      :value: None



   .. py:attribute:: arreter


   .. py:attribute:: journal


   .. py:attribute:: actions


   .. py:method:: lancer(action: str, params: dict) -> dict


   .. py:method:: nouvel_id() -> str


   .. py:method:: tache_finie(t: Tache)


   .. py:method:: en_cours() -> int


   .. py:method:: cours_actif() -> dict

      Choix du sélecteur : {cours, declinaison?, edition?}, {cours: "_sans"} ou {} (tous les cours).



   .. py:method:: filtre(objets: list[dict], cle: str, chemin=None) -> list[dict]


   .. py:method:: cours_liste() -> dict


   .. py:method:: cours_detail(nom: str) -> dict


   .. py:method:: cours_sans() -> dict


   .. py:method:: cours_action(p: dict) -> dict

      Modifications d'un cours venues de l'écran Cours (un formulaire, jamais le YAML).



   .. py:method:: cours_spec() -> str | None

      Valeur de ``--cours`` pour le choix du sélecteur (rien pour « tous » ou « sans cours »).



   .. py:method:: option_cours() -> list[str]


   .. py:method:: cours_reglages() -> dict

      Réglages de l'édition choisie (profil, étiquettes, catégorie, séances, effectif, dossiers), pour les formulaires.



   .. py:method:: registres(q: dict) -> dict

      Registres des versions de quiz : de l'édition et du cours demandés (ou choisis en haut), sinon tous.



   .. py:method:: registre_modifier(p: dict) -> dict


   .. py:method:: versions_classeurs(classeurs: list[dict]) -> list[dict]

      Dernière version de chaque classeur dans les registres du choix (ou tous) : {id, etat, nombre}.



   .. py:method:: rattacher(type_: str, chemin: pathlib.Path)

      Ajoute un objet créé par l'atelier au cours actif s'il n'y est pas déjà (sources du cours).



   .. py:method:: dossier_du_cours(type_: str, defaut: pathlib.Path) -> pathlib.Path

      Dossier standard du cours actif pour un type (``capsules/``, ``questions/``…), sinon ``defaut``.



   .. py:method:: fiches_exoforge() -> list[dict]

      Fiches ExoForge du dépôt : exemples publiés et data/exoforge (fiches privées).



   .. py:method:: a_exo_construire(p: dict) -> Tache


   .. py:method:: a_cap_simple(cmd: str, libelle: str)


   .. py:method:: a_cap_cameo(p: dict) -> Tache


   .. py:method:: tester_micro(p: dict) -> dict

      Écoute le micro 4 s (``capsuleforge filmer --tester-micro``) ; renvoie voix, crête (dBFS), avis, conseil.



   .. py:method:: a_cap_pptx(p: dict) -> Tache


   .. py:method:: a_cap_transcrire(p: dict) -> Tache


   .. py:method:: a_cap_relire(p: dict) -> Tache


   .. py:method:: a_cap_pdf(p: dict) -> Tache

      Une version du PDF à partir du lecteur construit (carte « 6. PDF ») ; ou seulement la case « dans le paquet ».



   .. py:method:: a_cap_accrocher(p: dict) -> Tache


   .. py:method:: a_cap_traduire(p: dict) -> Tache


   .. py:method:: a_cap_voix(p: dict) -> Tache


   .. py:method:: a_cap_construire(p: dict) -> Tache


   .. py:method:: a_cap_nouvelle(p: dict) -> Tache


   .. py:method:: a_cap_filmer(p: dict) -> Tache


   .. py:method:: a_cap_editer(p: dict) -> Tache


   .. py:method:: a_cap_enregistrer(p: dict) -> Tache


   .. py:method:: a_cap_approj(p: dict) -> Tache


   .. py:method:: appareils() -> dict

      Écrans, caméras et micros (``capsuleforge filmer --appareils``), gardés une minute.



   .. py:method:: a_cap_video(p: dict) -> Tache


   .. py:method:: a_quiz_valider(p: dict) -> Tache


   .. py:method:: a_quiz_convertir(p: dict) -> Tache


   .. py:method:: a_quiz_modele(p: dict) -> Tache


   .. py:method:: a_quiz_fusionner(p: dict) -> Tache


   .. py:method:: a_diag_bilan(p: dict) -> Tache


   .. py:method:: ouvrir(p: dict) -> dict

      Ouvre un fichier du dépôt avec son programme habituel (Excel, navigateur…).



   .. py:method:: etat_poste() -> list[dict]


   .. py:method:: parcourir(p: dict) -> dict

      Dialogue de fichiers du système (tkinter), au premier plan ; un seul à la fois.



   .. py:method:: montrer(p: dict) -> dict

      Ouvre l'explorateur sur un fichier (sélectionné) ou un dossier du dépôt, au premier plan.

      Une même demande répétée dans les 8 s est ignorée (l'explorateur met parfois du temps à s'ouvrir : sans cela,
      chaque clic en ouvrirait un de plus).



   .. py:method:: page_partie()


   .. py:method:: page_revenue()


   .. py:method:: arret_si_parti()

      Arrête l'atelier si la page est partie depuis plus de 4 s et qu'aucune tâche ne tourne.



.. py:function:: fenetres() -> dict

   Fenêtres visibles de premier niveau : {hwnd: (classe, titre)}.


.. py:function:: fenetres_explorateur() -> set

   Fenêtres de l'explorateur Windows ouvertes (classe CabinetWClass).


.. py:function:: premier_plan(avant, titre: str, delai: float = 6.0, explorateur: bool = True)

   Met au premier plan la fenêtre qui vient de s'ouvrir.

   ``explorateur`` : une fenêtre d'explorateur nouvelle, ou déjà ouverte sur le dossier ``titre`` ; sinon : une fenêtre
   dont le titre contient ``titre`` (nom du fichier ouvert dans Excel, le navigateur…), nouvelle de préférence.
   Windows refuse le premier plan à un programme qui n'a pas la main (l'icône clignote dans la barre des tâches) :
   l'atelier emprunte la file d'entrée de la fenêtre active et simule un appui sur Alt, ce qui lève ce refus.


.. py:function:: lire_fiche(f: pathlib.Path, yaml) -> dict | None

   Résumé d'une fiche ExoForge (id, titre, profil, construction) ; ``None`` si ce n'en est pas une.


.. py:function:: profils_campus() -> dict

   Profils d'établissement et ce qu'ils disent des cours (``profil_cours`` : structure, vocabulaire, campus,
   parcours, formations, gabarits des codes et de la promo), complétés par les valeurs génériques.


.. py:function:: reglages_absents(r: dict) -> list[str]

   Chemins retenus par l'atelier (diaporamas, classeurs) qui n'existent plus sur cet ordinateur.


.. py:function:: noms_profils() -> list[str]

.. py:function:: gestionnaire(at: Atelier)

.. py:function:: main(argv=None)

