#!/usr/bin/env python3
"""CapsuleForge — chapitres de cours interactifs et capsules de simulation logicielle, décrits par un fichier YAML.

Commandes (abréviations acceptées : « en », « ed », « cons », « conv », « v »…) : ::

    python capsuleforge.py enregistrer freecad_pad [--titre "FreeCAD : premier corps"] [--ecran 1]
        Enregistre une manipulation (Windows). Ctrl+Maj+E = nouvelle étape, Ctrl+Maj+P = pause, Ctrl+Maj+F = fin.
        Sortie : data/capsuleforge/freecad_pad/ (journal.jsonl, images/, capsule.yaml).
    python capsuleforge.py editer freecad_pad
        Ouvre l'éditeur visuel dans le navigateur (image, zone, bulle, chronologie, ajout d'éléments).
    python capsuleforge.py construire freecad_pad [--largeur 1920] [--format webp]
        capsule.yaml -> dist/capsuleforge/freecad_pad/index.html (lecteur « Regarder » / « À vous »).
    python capsuleforge.py construire fiabilite
        Un dossier sans capsule.yaml mais avec chapitre.yaml (cours) : lecteur du chapitre (plan, parcours, sous-titres,
        apparitions, spots, pointeurs), images en WebP et sons en MP3.
    python capsuleforge.py construire fiabilite --scorm chapitre|parties|tout [--scorm-version 1.2]
        En plus : paquets SCORM 2004 pour Moodle (un pour le chapitre, un par partie du tronc, ou les deux).
    python capsuleforge.py traduire fiabilite --langue en [--moteur aucun|argos|deepl]
        Écrit ou complète data/capsuleforge/fiabilite/traductions/en.yaml (source, cible, relu) ; le moteur pré-remplit.
    python capsuleforge.py traduire fiabilite --langue en --importer
        Recopie les traductions dans chapitre.yaml (textes {fr: …, en: …}) : sous-titres et voix dans cette langue.
    python capsuleforge.py traduire fiabilite --langue en --relire
        Écran de relecture dans le navigateur : original, diapositive et son à côté ; « Fait » valide et passe au
        suivant, « Zap » passe sans changer le statut ; enregistrement continu ; bouton « Importer dans le chapitre ».
    python capsuleforge.py video capture.mp4 --chapitre fiabilite --section partie/section [--son audio.mp4] [--titre "…"]
        Importe une vidéo (enregistrement d'écran, export ActivePresenter, clip) : compressée dans videos/, découpée
        en pas aux silences, chaque pas avec son image d'affiche et son son (transcription et relecture comme une diapo).
    python capsuleforge.py filmer tuto1 --section principale/demo --titre "Démo" [--webcam] [--ecran 1] [--micro NOM]
        Filme l'écran, le micro (et la webcam) en même temps, puis importe la vidéo en pas (webcam = caméo).
        Ctrl+Maj+P pause, Ctrl+Maj+F (ou Entrée) fin. « filmer --appareils » liste écrans, caméras et micros.
    python capsuleforge.py voix fiabilite --langue en [--moteur piper|edge] [--voix en_GB-alan-medium] [--vitesse 1.0]
        Voix de synthèse phrase par phrase (autre langue : à côté du son d'origine ; langue source : pas sans
        enregistrement seulement). Sous-titres, apparitions et objets recalés dans le lecteur.
    python capsuleforge.py convertir freecad_pad
        capsule.yaml (format 1) -> chapitre.yaml (format 2 : parties, sections, pas en scènes), sans toucher à l'original.
    python capsuleforge.py plan fiabilite [--parcours immersive] [--variante ecole1]
        Plan d'un chapitre au format 2, parcours par parcours : noms (B-S2-P4), durées, annexes, questions.
    python capsuleforge.py pptx cours.pptx --chapitre fiabilite [--diapos 6-12] [--largeur 1440]
        Remplit les sections du chapitre qui renvoient à ce diaporama : un pas par diapositive (image de départ,
        audio de narration, durée) et une apparition par clic d'animation. Les images sont produites par PowerPoint.
    python capsuleforge.py transcrire fiabilite [--modele small|medium] [--refaire] [--sections dimensionnement]
        Transcrit l'audio des pas sans narration (Whisper, sur cet ordinateur) : premier jet de scénario à relire.
    python capsuleforge.py relire fiabilite
        Ouvre la relecture dans le navigateur : diapositive, son et texte dit phrase par phrase (corriger, couper,
        fusionner, poser les apparitions). Les phrases horodatées sont la source de la narration et des sous-titres.
    python capsuleforge.py verifier freecad_pad
        Erreurs et avertissements (images manquantes, bulles génériques, étapes sans narration).
    python capsuleforge.py assembler freecad_pad
        Refait le YAML depuis le journal (écrit capsule_reassemblee.yaml si capsule.yaml existe déjà).
    python capsuleforge.py approj projet.approj [--nom nom]
        Reprend une simulation ActivePresenter (lecture seule) en capsule.yaml.

Un nom sans chemin désigne data/capsuleforge/<nom>/ ; on peut aussi donner un dossier ou un capsule.yaml.
Licence : GPL v3.
"""
from __future__ import annotations

import argparse
import sys
import unicodedata
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
sys.path.insert(0, str(ICI.parent / "commun"))
import chemins  # noqa: E402
import assemblage as A  # noqa: E402

VERSION = "0.9"
DOSSIER = chemins.DATA / "capsuleforge"
COMMANDES = ["enregistrer", "editer", "construire", "traduire", "voix", "video", "filmer", "convertir", "plan", "pptx", "transcrire", "relire", "verifier", "assembler", "approj", "assistant"]


def _sans_accent(s: str) -> str:
    """Renvoie ``s`` en minuscules, sans accents (comparaison tolérante des noms)."""
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def commande_tolerante(argv: list[str]) -> list[str]:
    """Remplace le premier argument par le nom exact de la commande qu'il abrège.

    « con », « Vérifier » ou « verif » sont reconnus par leurs premières lettres, sans tenir compte des accents
    ni de la casse ; « v » désigne « verifier ». Renvoie ``argv`` inchangé si rien ne correspond ; arrête le
    programme (``SystemExit``) si l'abréviation est ambiguë.
    """
    if not argv or argv[0].startswith("-"):
        return argv
    mot = _sans_accent(argv[0])
    if mot == "v":                                   # abréviation historique de « verifier » (avant « voix »)
        return ["verifier"] + argv[1:]
    exacts = [c for c in COMMANDES if c == mot]
    cand = exacts or [c for c in COMMANDES if c.startswith(mot)]
    if len(cand) == 1:
        return [cand[0]] + argv[1:]
    if len(cand) > 1:
        raise SystemExit(f"« {argv[0]} » est ambigu : {', '.join(cand)}")
    return argv


def trouver_capsule(nom: str) -> Path:
    """Renvoie le chemin du ``capsule.yaml`` désigné par ``nom``.

    ``nom`` peut être un fichier, un dossier ou un nom court cherché dans ``data/capsuleforge`` (sans tenir compte
    des accents ni de la casse ; un début de nom suffit s'il est unique). Le fichier renvoyé n'existe pas
    forcément (dossier d'un chapitre au format 2) ; ``SystemExit`` si rien ne correspond.
    """
    p = Path(nom)
    if p.is_file():
        return p
    if p.is_dir():
        return p / "capsule.yaml"
    if p.with_suffix(".yaml").is_file():
        return p.with_suffix(".yaml")
    if DOSSIER.is_dir():
        cible = _sans_accent(p.name)
        for d in sorted(DOSSIER.iterdir()):
            if d.is_dir() and _sans_accent(d.name) == cible:
                return d / "capsule.yaml"
        cands = [d for d in sorted(DOSSIER.iterdir()) if d.is_dir() and _sans_accent(d.name).startswith(cible)]
        if len(cands) == 1:
            return cands[0] / "capsule.yaml"
    raise SystemExit(f"Capsule introuvable : {nom} (ni fichier, ni dossier, ni nom dans {DOSSIER})")


def cmd_enregistrer(a):
    """Enregistre une manipulation (commande ``enregistrer``, Windows) puis affiche le contrôle de la capsule.

    Le dossier de sortie est ``data/capsuleforge/<nom>`` pour un nom court ; il reçoit ``journal.jsonl``,
    ``images/`` et ``capsule.yaml``.
    """
    import enregistreur
    d = Path(a.nom) if (Path(a.nom).parent != Path(".") or a.nom.startswith(".")) else DOSSIER / a.nom
    print(f"CapsuleForge {VERSION} — enregistrement dans {d}")
    print("Pensez à fermer ou masquer ce qui ne doit pas apparaître (messagerie, noms, chemins personnels).")
    y = enregistreur.enregistrer(d, ecran=a.ecran, titre=a.titre, application=a.application,
                                 accessibilite=not a.sans_accessibilite,
                                 touche_etape=a.touche_etape, touche_pause=a.touche_pause, touche_fin=a.touche_fin)
    cap = A.lire_yaml(y)
    n = sum(len(e["pas"]) for e in cap.get("etapes", []))
    print(f"\n{n} pas en {len(cap.get('etapes', []))} étape(s) -> {y}")
    _rapport(cap, y.parent)
    print(f"\nÉtape suivante : relire {y.name}, puis « capsuleforge construire {d.name} ».")


def _rapport(cap, dossier):
    """Affiche les erreurs et avertissements d'une capsule au format 1 ; renvoie la liste des erreurs."""
    err, av = A.verifier(cap, dossier)
    for e in err:
        print("  ERREUR :", e)
    for x in av:
        print("  à revoir :", x)
    pas = [p for e in cap.get("etapes", []) for p in e["pas"]]
    if pas:
        pas = [p for p in pas if not p.get("ignorer")]
        clics = [p for p in pas if p.get("action") not in ("touche", "saisie")]
        acc = sum(1 for p in clics if (p.get("cible") or {}).get("origine") == "accessibilite")
        print(f"  contrôle nommé par l'accessibilité de Windows : {acc} / {len(clics)} actions à la souris")
    return err


def cmd_construire(a):
    """Construit le lecteur HTML d'une capsule (format 1) ou d'un chapitre (format 2), commande ``construire``.

    Si le dossier contient à la fois ``capsule.yaml`` et ``chapitre.yaml``, l'option ``--lecteur`` choisit le
    format ; à défaut, le fichier modifié en dernier l'emporte. La sortie va par défaut dans
    ``<sorties>/capsuleforge/<nom>/`` ; pour un chapitre, ``--scorm`` produit en plus les paquets SCORM.
    """
    y = trouver_capsule(a.capsule)
    y2 = trouver_chapitre(a.capsule)
    chapitre = y.name != "capsule.yaml" or (not y.is_file() and y2.is_file())
    if y.name == "capsule.yaml" and y.is_file() and y2.is_file():            # les deux formats dans le dossier
        choix = getattr(a, "lecteur", None)
        if choix:
            chapitre = choix == "2"
        else:
            chapitre = y2.stat().st_mtime > y.stat().st_mtime                  # le plus récemment modifié fait foi
            print(f"  {y.parent.name} a capsule.yaml (format 1) et chapitre.yaml (format 2) : lecteur au format "
                  f"{2 if chapitre else 1}, celui du fichier modifié en dernier (--lecteur 1 ou 2 pour choisir)")
    if chapitre:                                                               # chapitre au format 2 (cours)
        import construire_chapitre
        y2 = y if y.name != "capsule.yaml" and y.is_file() else y2
        sortie = Path(a.sortie) if a.sortie else chemins.SORTIES / "capsuleforge" / y2.parent.name
        construire_chapitre.construire(y2, sortie, largeur=a.largeur, fmt=a.format or "webp", audio=a.audio,
                                       scorm=getattr(a, "scorm", None), scorm_version=getattr(a, "scorm_version", None) or "2004")
        return 0
    import construire
    sortie = Path(a.sortie) if a.sortie else chemins.SORTIES / "capsuleforge" / y.parent.name
    construire.construire(y, sortie, largeur=a.largeur, fmt=a.format or "png")


def cmd_editer(a):
    """Ouvre l'éditeur visuel d'une capsule dans le navigateur (commande ``editer``) ; bloque jusqu'à l'arrêt du serveur."""
    import editeur
    y = trouver_capsule(a.capsule)
    editeur.editer(y, chemins.SORTIES / "capsuleforge" / y.parent.name, port=a.port, navigateur=not a.sans_navigateur)


def trouver_chapitre(nom: str) -> Path:
    """Renvoie le chemin du ``chapitre.yaml`` (format 2) désigné par ``nom``.

    ``nom`` peut être un fichier, un dossier ou un nom court cherché dans ``data/capsuleforge`` comme pour
    :func:`trouver_capsule`. Le fichier renvoyé n'existe pas forcément.
    """
    import format_chapitre as F
    p = Path(nom)
    if p.is_file():
        return p
    if p.is_dir():
        return p / F.FICHIER
    return trouver_capsule(nom).parent / F.FICHIER


def _rapport2(chap, dossier):
    """Affiche les erreurs et avertissements d'un chapitre au format 2 ; renvoie la liste des erreurs."""
    import format_chapitre as F
    err, av = F.verifier(chap, dossier)
    for e in err:
        print("  ERREUR :", e)
    for x in av:
        print("  à revoir :", x)
    return err


def cmd_verifier(a):
    """Contrôle une capsule (format 1) et, s'il existe, le chapitre (format 2) du même dossier.

    Commande ``verifier`` ; renvoie 1 s'il y a au moins une erreur, 0 sinon.
    """
    import format_chapitre as F
    y = trouver_capsule(a.capsule)
    err = []
    if y.is_file() and y.name != F.FICHIER and (A.lire_yaml(y).get("format") != F.FORMAT):
        print(f"{y.name} (format 1)")
        err += _rapport(A.lire_yaml(y), y.parent)
        y2 = y.parent / F.FICHIER
    else:
        y2 = y if y.is_file() else trouver_chapitre(a.capsule)
    if y2.is_file():
        print(f"{y2.name} (format 2)")
        err += _rapport2(F.lire(y2), y2.parent)
    elif not y.is_file():
        raise SystemExit(f"Ni capsule.yaml ni chapitre.yaml dans {y.parent}")
    print("OK" if not err else f"{len(err)} erreur(s)")
    return 1 if err else 0


def cmd_convertir(a):
    """Convertit ``capsule.yaml`` (format 1) en ``chapitre.yaml`` (format 2) dans le même dossier.

    Commande ``convertir`` ; l'original n'est pas modifié. Un ``chapitre.yaml`` existant n'est remplacé que s'il
    est lui-même issu d'une conversion.
    """
    import format_chapitre as F
    y = trouver_capsule(a.capsule)
    if not y.is_file():
        raise SystemExit(f"Capsule introuvable : {y}")
    dest = y.parent / F.FICHIER
    if dest.is_file() and not (F.lire(dest).get("source") or {}).get("conversion"):
        raise SystemExit(f"{dest} existe et n'est pas issu d'une conversion : il n'est pas remplacé.")
    chap = F.convertir_v1(A.lire_yaml(y), y.name)
    F.ecrire(chap, dest)
    n = F.noms(chap)
    pas = [p for pa in chap["parties"] for s in pa["sections"] for p in s["pas"]]
    print(f"-> {dest}\n  {len(chap['parties'][0]['sections'])} section(s), {len(pas)} pas "
          f"dont {sum(1 for p in pas if p.get('ecarte'))} écartés ; noms de {n[('pas', pas[0]['id'])] if pas else '-'} "
          f"à {n[('pas', pas[-1]['id'])] if pas else '-'}")
    _rapport2(chap, y.parent)


def cmd_pptx(a):
    """Reprend un diaporama PowerPoint dans les sections du chapitre qui y renvoient (commande ``pptx``).

    Le travail est fait par :func:`pptx_lire.reprendre` ; cette commande trouve le diaporama et le chapitre,
    puis affiche le rapport du chapitre.
    """
    import pptx_lire as L
    src = Path(a.fichier)
    if not src.is_file():
        raise SystemExit(f"Diaporama introuvable : {src}")
    y = trouver_chapitre(a.chapitre)
    if not y.is_file():
        raise SystemExit(f"Pas de chapitre : {y}")
    chap = L.reprendre(src, y, a.diapos, largeur=a.largeur, images=not a.sans_images)
    _rapport2(chap, y.parent)


def cmd_transcrire(a):
    """Transcrit l'audio des pas d'un chapitre avec Whisper (commande ``transcrire``).

    Écrit ``transcription_journal.txt`` et, si au moins un pas a été transcrit, une copie de l'ancien chapitre
    dans ``sauvegardes/`` puis le ``chapitre.yaml`` mis à jour.
    """
    import shutil
    import time
    import format_chapitre as F
    import transcription as T
    y = trouver_chapitre(a.chapitre)
    if not y.is_file():
        raise SystemExit(f"Pas de chapitre : {y}")
    chap = F.lire(y)
    journal = y.parent / "transcription_journal.txt"
    journal.write_text(f"{time.strftime('%Y-%m-%d %H:%M:%S')} modèle {a.modele}\n", encoding="utf-8")

    def noter(ligne):
        print(ligne)
        with open(journal, "a", encoding="utf-8") as f:
            f.write(ligne + "\n")

    print(f"Chargement du modèle « {a.modele} » (téléchargé à la première utilisation)…")
    t0 = time.time()
    try:
        modele = T.charger_modele(a.modele)
        n = T.transcrire_chapitre(chap, y.parent, modele, refaire=a.refaire,
                                  sections=set(a.sections.split(",")) if a.sections else None, journal=noter)
    except SystemExit:
        raise
    except BaseException:
        import traceback
        noter(traceback.format_exc())
        raise SystemExit(f"La transcription a échoué : voir {journal}")
    if n:
        (y.parent / "sauvegardes").mkdir(exist_ok=True)
        shutil.copy2(y, y.parent / "sauvegardes" / f"chapitre_{time.strftime('%Y%m%d_%H%M%S')}.yaml")
        F.ecrire(chap, y)
    noter(f"{n} pas transcrit(s) en {round(time.time() - t0)} s -> {y}")


def cmd_traduire(a):
    """Prépare, relit (``--relire``) ou importe (``--importer``) la traduction d'un chapitre (commande ``traduire``)."""
    import traduction
    y = trouver_chapitre(a.chapitre)
    if not y.is_file():
        raise SystemExit(f"Pas de chapitre : {y}")
    if a.relire:
        traduction.relire_traduction(y, a.langue, port=a.port, navigateur=not a.sans_navigateur)
    elif a.importer:
        traduction.importer(y, a.langue)
    else:
        traduction.preparer(y, a.langue, moteur=a.moteur)


def cmd_video(a):
    """Importe une vidéo dans une section du chapitre, découpée en pas (commande ``video``)."""
    import video
    y = trouver_chapitre(a.chapitre)
    if not y.is_file():
        raise SystemExit(f"Pas de chapitre : {y}")
    video.importer(y, Path(a.fichier.strip('"')), a.section, titre=a.titre, debut=a.debut or 0.0, fin=a.fin,
                   decoupe=a.decoupe, pas_min=a.pas_min, pas_max=a.pas_max, qualite=a.qualite, remplacer=a.remplacer,
                   son=Path(a.son.strip('"')) if a.son else None)


def cmd_filmer(a):
    """Filme l'écran, le micro et éventuellement la webcam, puis importe la vidéo (commande ``filmer``).

    Avec ``--appareils``, affiche seulement les écrans, caméras et micros disponibles et renvoie 0.
    """
    import filmer
    if a.appareils:
        v, m = filmer.appareils()
        print("Écrans :", " ; ".join(f"n° {k + 1} {e['width']} × {e['height']}" for k, e in enumerate(filmer.ecrans())) or "?")
        print("Caméras :", v or "aucune")
        print("Micros :", m or "aucun")
        return 0
    if not a.chapitre:
        raise SystemExit("filmer : le nom du chapitre est demandé")
    if not a.section and not a.sans_import:
        raise SystemExit("filmer : --section partie/section est demandé (section où importer la vidéo) ; "
                         "sans import : --sans-import")
    y = trouver_chapitre(a.chapitre)
    if not y.is_file():
        raise SystemExit(f"Pas de chapitre : {y}")
    webcam = True if a.webcam == "" else a.webcam                 # « --webcam » seul : la caméra par défaut
    micro = False if a.sans_micro else (a.micro or True)
    filmer.filmer(y, a.section, titre=a.titre, ecran=a.ecran, webcam=webcam, micro=micro, ips=a.ips, duree=a.duree,
                  importer=not a.sans_import, essai=a.essai)


def cmd_voix(a):
    """Produit la voix de synthèse d'un chapitre, phrase par phrase (commande ``voix``)."""
    import voix
    y = trouver_chapitre(a.chapitre)
    if not y.is_file():
        raise SystemExit(f"Pas de chapitre : {y}")
    voix.voix_chapitre(y, a.langue, moteur=a.moteur, nom=a.voix, vitesse=a.vitesse,
                       sections=set(a.sections.split(",")) if a.sections else None, refaire=a.refaire)


def cmd_relire(a):
    """Ouvre la relecture du texte dit d'un chapitre dans le navigateur (commande ``relire``)."""
    import relecture
    y = trouver_chapitre(a.chapitre)
    if not y.is_file():
        raise SystemExit(f"Pas de chapitre : {y}")
    relecture.relire(y, port=a.port, navigateur=not a.sans_navigateur)


def cmd_plan(a):
    """Affiche le plan d'un chapitre au format 2, parcours par parcours (commande ``plan``)."""
    import format_chapitre as F
    y = trouver_chapitre(a.chapitre)
    if not y.is_file():
        raise SystemExit(f"Pas de {F.FICHIER} : {y} (pour une capsule au format 1 : « capsuleforge convertir »)")
    chap = F.lire(y)
    print(F.texte(chap.get("titre")))
    choisis = [a.parcours] if a.parcours else [p.get("id") for p in chap.get("parcours") or []] or [None]
    for pid in choisis:
        titre = next((p.get("titre") for p in chap.get("parcours") or [] if p.get("id") == pid), None)
        print(f"\n=== Parcours : {titre or pid or 'tout le contenu'}" + (f" · variante {a.variante}" if a.variante else "") + " ===")
        print("\n".join(F.plan(chap, pid, a.variante)))


def cmd_assembler(a):
    """Refait le YAML de la capsule à partir de ``journal.jsonl`` (commande ``assembler``).

    Écrit ``capsule.yaml``, ou ``capsule_reassemblee.yaml`` si ``capsule.yaml`` existe déjà.
    """
    y = trouver_capsule(a.capsule)
    j = y.parent / "journal.jsonl"
    if not j.is_file():
        raise SystemExit(f"Pas de journal dans {y.parent}")
    cap = A.assembler(A.lire_journal(j), titre=a.titre)
    dest = y if not y.exists() else y.with_name("capsule_reassemblee.yaml")
    A.ecrire_yaml(cap, dest)
    print(f"-> {dest}")
    _rapport(cap, y.parent)


def cmd_approj(a):
    """Reprend un projet ActivePresenter (``.approj``, lu sans être modifié) en capsule (commande ``approj``).

    Écrit ``data/capsuleforge/<nom>/capsule.yaml`` ; refuse de remplacer une capsule existante.
    """
    import approj
    src = Path(a.projet)
    if not src.is_file() and src.with_suffix(".approj").is_file():
        src = src.with_suffix(".approj")
    if not src.is_file():
        raise SystemExit(f"Projet introuvable : {a.projet}")
    d = DOSSIER / (a.nom or src.stem)
    if (d / "capsule.yaml").exists():
        raise SystemExit(f"{d / 'capsule.yaml'} existe déjà : choisir --nom")
    cap = approj.importer(src, d, titre=a.titre or src.stem)
    A.ecrire_yaml(cap, d / "capsule.yaml")
    print(f"-> {d / 'capsule.yaml'}")
    _rapport(cap, d)


def cmd_assistant(_a):
    """Propose un menu pas à pas dans la console, puis lance la commande choisie (commande ``assistant``)."""
    print(f"CapsuleForge {VERSION}\n  1. Enregistrer une manipulation\n  2. Construire le lecteur d'une capsule\n"
          "  3. Vérifier une capsule\n  4. Reprendre un projet ActivePresenter (.approj)\n"
          "  5. Modifier une capsule dans l'éditeur visuel\n"
          "  6. Reprendre un diaporama PowerPoint dans un chapitre\n"
          "  7. Relire le texte dit d'un chapitre, avec le son")
    if DOSSIER.is_dir():
        noms = [d.name for d in sorted(DOSSIER.iterdir()) if (d / "capsule.yaml").is_file()]
        if noms:
            print("Capsules existantes :", ", ".join(noms))
    ch = input("Choix : ").strip()
    if ch == "1":
        nom = input("Nom court (sans espace, ex. freecad_pad) : ").strip()
        titre = input("Titre affiché : ").strip() or None
        main(["enregistrer", nom] + (["--titre", titre] if titre else []))
    elif ch in ("2", "3"):
        nom = input("Nom de la capsule : ").strip()
        main(["construire" if ch == "2" else "verifier", nom])
    elif ch == "4":
        main(["approj", input("Chemin du .approj : ").strip().strip('"')])
    elif ch == "5":
        main(["editer", input("Nom de la capsule : ").strip()])
    elif ch == "6":
        f = input("Chemin du .pptx (on peut glisser le fichier dans cette fenêtre) : ").strip().strip('"')
        c = input("Nom du chapitre : ").strip()
        d = input("Diapositives (ex. 6-12 ; vide = toutes) : ").strip()
        main(["pptx", f, "--chapitre", c] + (["--diapos", d] if d else []))
    elif ch == "7":
        main(["relire", input("Nom du chapitre : ").strip()])


def main(argv=None):
    """Point d'entrée en ligne de commande : analyse ``argv`` et lance la commande demandée.

    ``argv`` vaut par défaut ``sys.argv[1:]`` ; les abréviations de commande sont acceptées. Renvoie le code
    de sortie (0 si la commande ne renvoie rien).
    """
    argv = commande_tolerante(list(sys.argv[1:] if argv is None else argv))
    p = argparse.ArgumentParser(prog="capsuleforge", description="CapsuleForge : chapitres de cours interactifs et capsules de simulation logicielle (YAML -> lecteur HTML, paquet SCORM).")
    p.add_argument("--version", action="version", version=VERSION)
    sp = p.add_subparsers(dest="cmd")
    e = sp.add_parser("enregistrer", help="enregistrer une manipulation (Windows)")
    e.add_argument("nom"); e.add_argument("--titre"); e.add_argument("--application")
    e.add_argument("--ecran", type=int, default=1, help="numéro de l'écran (1 = principal)")
    e.add_argument("--sans-accessibilite", action="store_true", help="ne pas lire les noms de contrôles")
    e.add_argument("--touche-etape", default="ctrl+shift+e", help="raccourci « nouvelle étape » (ex. ctrl+maj+e ; f8 = Fn+F8 sur un portable)")
    e.add_argument("--touche-pause", default="ctrl+shift+p")
    e.add_argument("--touche-fin", default="ctrl+shift+f")
    c = sp.add_parser("construire", help="construire le lecteur HTML")
    c.add_argument("capsule"); c.add_argument("--sortie")
    c.add_argument("--largeur", type=int, help="réduire les images à cette largeur (px)")
    c.add_argument("--format", choices=["png", "webp"], help="images : png par défaut pour une capsule, webp pour un chapitre")
    c.add_argument("--audio", default="mp3", choices=["mp3", "origine"], help="chapitre : sons convertis en MP3 mono (défaut) ou recopiés")
    c.add_argument("--scorm", choices=["chapitre", "parties", "tout"], help="chapitre : paquets SCORM (Moodle) en plus du lecteur")
    c.add_argument("--scorm-version", choices=["2004", "1.2"], default="2004", help="format des paquets : 2004 (défaut) ou 1.2 (seul format officiellement pris en charge par Moodle)")
    c.add_argument("--lecteur", choices=["1", "2"], help="dossier qui a capsule.yaml et chapitre.yaml : format à construire (défaut : le plus récent)")
    ed = sp.add_parser("editer", help="ouvrir l'éditeur visuel (navigateur)"); ed.add_argument("capsule")
    ed.add_argument("--port", type=int, default=8765); ed.add_argument("--sans-navigateur", action="store_true")
    cv = sp.add_parser("convertir", help="capsule.yaml (format 1) -> chapitre.yaml (format 2)"); cv.add_argument("capsule")
    pl = sp.add_parser("plan", help="plan d'un chapitre (format 2) par parcours"); pl.add_argument("chapitre")
    pl.add_argument("--parcours"); pl.add_argument("--variante")
    px = sp.add_parser("pptx", help="reprendre un diaporama PowerPoint dans un chapitre"); px.add_argument("fichier")
    px.add_argument("--chapitre", required=True); px.add_argument("--diapos", help="ex. 6-12 (défaut : toutes)")
    px.add_argument("--largeur", type=int, help="largeur des images en pixels (défaut : celle du chapitre)")
    px.add_argument("--sans-images", action="store_true", help="ne pas piloter PowerPoint (structure et audio seulement)")
    tr = sp.add_parser("transcrire", help="transcrire l'audio des pas (premier jet de scénario)"); tr.add_argument("chapitre")
    tr.add_argument("--modele", default="small", help="small (rapide) ou medium (plus juste, plus lent)")
    tr.add_argument("--refaire", action="store_true", help="retranscrire aussi les pas qui ont déjà une narration")
    tr.add_argument("--sections", help="identifiants de parties ou de sections, séparés par des virgules")
    rl = sp.add_parser("relire", help="relire le texte dit, phrase par phrase, avec le son (navigateur)"); rl.add_argument("chapitre")
    rl.add_argument("--port", type=int, default=8775); rl.add_argument("--sans-navigateur", action="store_true")
    tl = sp.add_parser("traduire", help="traduire les textes d'un chapitre (fichier d'échange, puis import)"); tl.add_argument("chapitre")
    tl.add_argument("--langue", required=True, help="code de la langue cible (en, es, de…)")
    tl.add_argument("--moteur", default="aucun", choices=["aucun", "argos", "deepl"], help="pré-remplissage des cibles vides (défaut : aucun)")
    tl.add_argument("--importer", action="store_true", help="recopier les traductions dans chapitre.yaml")
    tl.add_argument("--relire", action="store_true", help="écran de relecture (navigateur) : Fait / Zap, enregistrement continu, import")
    tl.add_argument("--port", type=int, default=8776); tl.add_argument("--sans-navigateur", action="store_true")
    vd = sp.add_parser("video", help="importer une vidéo (écran, ActivePresenter, clip) dans une section"); vd.add_argument("fichier")
    vd.add_argument("--chapitre", required=True); vd.add_argument("--section", required=True, help="partie/section (ou id de section unique)")
    vd.add_argument("--titre", help="titre de la section si elle est à créer")
    vd.add_argument("--son", help="son pris dans un autre fichier (ActivePresenter : audio_NNN.mp4 exporté à part)")
    vd.add_argument("--debut", type=float, help="début dans la vidéo (s)"); vd.add_argument("--fin", type=float, help="fin dans la vidéo (s)")
    vd.add_argument("--decoupe", default="silences", choices=["silences", "aucune"], help="découpe en pas aux silences (défaut) ou un seul pas")
    vd.add_argument("--pas-min", type=float, default=20, help="durée minimale d'un pas (s)"); vd.add_argument("--pas-max", type=float, default=90, help="durée maximale d'un pas (s)")
    vd.add_argument("--qualite", type=int, default=28, help="qualité H.264 (CRF) : 23 = meilleure et plus lourde, 32 = plus légère")
    vd.add_argument("--remplacer", action="store_true", help="retirer d'abord les pas déjà importés de ce fichier")
    fl = sp.add_parser("filmer", help="filmer écran + micro (+ webcam) et importer en pas vidéo"); fl.add_argument("chapitre", nargs="?")
    fl.add_argument("--section", help="partie/section (créée avec --titre si besoin)"); fl.add_argument("--titre")
    fl.add_argument("--ecran", type=int, default=1, help="numéro de l'écran (1 = principal)")
    fl.add_argument("--webcam", nargs="?", const="", help="filmer aussi la webcam (nom facultatif ; défaut : la première, hors infrarouge)")
    fl.add_argument("--micro", help="nom du micro (défaut : le premier)"); fl.add_argument("--sans-micro", action="store_true")
    fl.add_argument("--ips", type=int, default=20, help="images par seconde de l'écran (défaut 20)")
    fl.add_argument("--duree", type=float, help="arrêt automatique après tant de secondes")
    fl.add_argument("--sans-import", action="store_true", help="garder les fichiers sans les importer")
    fl.add_argument("--appareils", action="store_true", help="lister écrans, caméras et micros")
    fl.add_argument("--essai", action="store_true", help="sources synthétiques (sans appareils)")
    vx = sp.add_parser("voix", help="voix de synthèse d'un chapitre, phrase par phrase"); vx.add_argument("chapitre")
    vx.add_argument("--langue", required=True, help="langue de la voix (fr = pas sans enregistrement ; en, es… = traduction)")
    vx.add_argument("--moteur", default="piper", choices=["piper", "edge", "essai"], help="piper (sur cet ordinateur, défaut), edge (en ligne, gratuit), essai (voix factice pour les tests)")
    vx.add_argument("--voix", help="nom de la voix (défaut selon la langue, ex. en_GB-alan-medium, fr_FR-tom-medium)")
    vx.add_argument("--vitesse", type=float, default=1.0, help="1.0 = normale ; 1.1 = plus rapide")
    vx.add_argument("--sections", help="identifiants de parties ou de sections, séparés par des virgules")
    vx.add_argument("--refaire", action="store_true", help="refaire même si le texte n'a pas changé")
    v = sp.add_parser("verifier", help="contrôler une capsule"); v.add_argument("capsule")
    s = sp.add_parser("assembler", help="refaire le YAML depuis le journal"); s.add_argument("capsule"); s.add_argument("--titre")
    ap = sp.add_parser("approj", help="reprendre un projet ActivePresenter"); ap.add_argument("projet")
    ap.add_argument("--nom"); ap.add_argument("--titre")
    sp.add_parser("assistant", help="menu pas à pas")
    a = p.parse_args(argv)
    if not a.cmd:
        p.print_help(); return 0
    return {"enregistrer": cmd_enregistrer, "editer": cmd_editer, "construire": cmd_construire, "traduire": cmd_traduire, "voix": cmd_voix, "video": cmd_video, "filmer": cmd_filmer, "convertir": cmd_convertir, "plan": cmd_plan, "pptx": cmd_pptx, "transcrire": cmd_transcrire, "relire": cmd_relire, "verifier": cmd_verifier,
            "assembler": cmd_assembler, "approj": cmd_approj, "assistant": cmd_assistant}[a.cmd](a) or 0


if __name__ == "__main__":
    sys.exit(main())
