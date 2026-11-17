"""CapsuleForge — construction du lecteur d'un chapitre (format 2) : de ``chapitre.yaml`` à ``index.html``.

Sortie : ``<sortie>/index.html`` (lecteur autonome, données incluses : s'ouvre aussi depuis le disque),
``<sortie>/images/`` (WebP par défaut) et ``<sortie>/audio/`` (MP3 mono par défaut, WAV recopié si la conversion
n'est pas possible). Rien n'est supprimé dans la sortie ; un média déjà converti et plus récent que sa source
est gardé.

Le lecteur joue les pas d'une section à la suite : image de départ, apparitions, sous-titres tirés des phrases,
spots, cadres, pointeurs et caches. Les parcours du chapitre filtrent le plan (annexes absentes, à la demande
ou intégrées). En fin de section, il pose les questions tirées de la banque QuizForge désignée par la section
(vrai/faux, QCM, numérique), avec leurs rétroactions.

Une partie peut porter un exercice ExoForge (``exercice: {outil: exoforge, fiche: …yaml}``, ou une liste) : la fiche
est construite par ``scripts/exoforge/build.py`` si ``dist/exoforge/<id>/`` manque ou est plus ancien qu'elle ou que le
moteur, ses fichiers sont recopiés dans ``<sortie>/exercices/<id>/``, et l'exercice devient la dernière section de la
partie. Le lecteur l'affiche dans un cadre et lui fournit une API SCORM 1.2 : score, réussite et réponses sont
gardés dans le navigateur (jauge « Pratique », journal « exercices »).

Paquets SCORM 2004 (option ``scorm``) : « chapitre » = un paquet pour tout le chapitre ; « parties » = un paquet par partie
du tronc, avec les annexes et exercices qu'elle appelle ; « tout » = les deux. Dans une plateforme (Moodle), le lecteur
y garde l'avancement (``cmi.suspend_data``), renvoie l'achèvement (sections du tronc vues), une note = la pratique en %
pondérée (question : poids 1, 1 si juste au moins une fois ; exercice : ``poids`` de l'entrée ``exercice``, par défaut sa
durée en minutes, fois son meilleur score ; poids 0 = hors note) et une interaction par section vue, question
répondue et réponse d'exercice. Paquets écrits à côté de la sortie : ``<nom>_scorm2004.zip``, ``<nom>_<lettre>_<id>_scorm2004.zip``.
Licence : GPL v3.
"""
from __future__ import annotations

import html
import json
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

import format2 as F
import voix as voix_mod

ICI = Path(__file__).resolve().parent
DEBIT_MP3 = 64000            # mono : 0,48 Mo par minute
OBJETS = ("spot", "cadre", "pointeur", "cache")


def _mp3(src: Path, dst: Path, debit: int = DEBIT_MP3) -> None:
    """Convertit un son en MP3 mono avec PyAV (bibliothèque « av », déjà là pour la transcription)."""
    import av
    with av.open(str(src)) as entree, av.open(str(dst), "w", format="mp3") as sortie:
        piste = entree.streams.audio[0]
        taux = piste.rate if piste.rate in (16000, 22050, 24000, 32000, 44100, 48000) else 44100
        flux = sortie.add_stream("libmp3lame", rate=taux)
        flux.bit_rate = debit if taux >= 32000 else min(debit, 48000)
        try:
            flux.layout = "mono"
        except Exception:
            pass
        reech = av.AudioResampler(format=flux.format.name if flux.format else "s16p", layout="mono", rate=taux)
        for trame in entree.decode(piste):
            for t in reech.resample(trame):
                for paquet in flux.encode(t):
                    sortie.mux(paquet)
        for t in reech.resample(None):
            for paquet in flux.encode(t):
                sortie.mux(paquet)
        for paquet in flux.encode(None):
            sortie.mux(paquet)


MINUTES_PAR_ETAPE = 1.5      # durée estimée d'un exercice ExoForge, faute de `duree_min`


def _fiche_exoforge(nom: str, dossier: Path) -> Path | None:
    """Renvoie le chemin d'une fiche ExoForge, cherchée à côté du chapitre puis dans ``data/exoforge`` (``None`` si absente)."""
    f = dossier / nom
    if f.is_file():
        return f
    racine = dossier.parent.parent / "exoforge"
    trouves = sorted(racine.rglob(Path(nom).name)) if racine.is_dir() else []
    return trouves[0] if trouves else None


def exercices_partie(p: dict, dossier: Path, sortie: Path, journal=print) -> list[dict]:
    """Renvoie les exercices ExoForge d'une partie sous forme de sections « exercice » du lecteur (HTML de l'exercice inclus).

    Chaque fiche est construite si besoin (``scripts/exoforge/build.py``) et ses fichiers sont recopiés dans
    ``<sortie>/exercices/<id>/`` ; une fiche introuvable ou qui ne se construit pas est signalée et ignorée.
    """
    import yaml
    refs = p.get("exercice") or []
    refs = [refs] if isinstance(refs, dict) else list(refs)
    depot = ICI.parent.parent
    moteur = depot / "scripts" / "exoforge" / "moteur" / "exercice.html"
    sections = []
    for ref in refs:
        if not isinstance(ref, dict) or (ref.get("outil") or "exoforge") != "exoforge" or not ref.get("fiche"):
            journal(f"  partie {p.get('id')} : exercice ignoré ({ref})")
            continue
        fiche = _fiche_exoforge(ref["fiche"], dossier)
        if not fiche:
            journal(f"  partie {p.get('id')} : fiche ExoForge introuvable « {ref['fiche']} » (exercice ignoré)")
            continue
        cfg = yaml.safe_load(fiche.read_text(encoding="utf-8")) or {}
        ident = cfg.get("id") or fiche.stem
        construit = depot / "dist" / "exoforge" / ident
        page = construit / "index.html"
        sources = [fiche] + ([moteur] if moteur.is_file() else [])
        if not page.is_file() or page.stat().st_mtime < max(f.stat().st_mtime for f in sources):
            journal(f"  exercice {ident} : construction ExoForge…")
            r = subprocess.run([sys.executable, str(depot / "scripts" / "exoforge" / "build.py"), str(fiche)],
                               cwd=str(depot), capture_output=True, text=True, encoding="utf-8", errors="replace")
            if r.returncode or not page.is_file():
                journal(f"  exercice {ident} : construction impossible (exercice ignoré)\n"
                        + "\n".join("    " + l for l in (r.stdout + r.stderr).strip().splitlines()[-8:]))
                continue
        cible = sortie / "exercices" / ident
        for f in construit.rglob("*"):                   # mathjax.js, médias ; la page est incluse dans le lecteur
            if f.is_file() and f.name not in ("index.html", "imsmanifest.xml"):
                d = cible / f.relative_to(construit)
                if not (d.is_file() and d.stat().st_mtime >= f.stat().st_mtime and d.stat().st_size == f.stat().st_size):
                    d.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(f, d)
        code = page.read_text(encoding="utf-8")
        code = code.replace("<head>", '<head>\n<base href="__BASE__">', 1)    # adresse absolue posée par le lecteur
        etapes = len(cfg.get("etapes") or [])
        duree = ref.get("duree_min") or max(3, round(etapes * MINUTES_PAR_ETAPE))
        sections.append({"id": "exo-" + ident, "titre": F.texte(ref.get("titre") or cfg.get("titre") or ident),
                         "objectif": F.texte(ref.get("objectif") or ""), "ouverture": "", "arret": True, "annexes": [],
                         "questions": 0, "lots": [], "duree_s": float(duree) * 60, "pas": [],
                         "exercice": {"id": ident, "base": f"exercices/{ident}/", "etapes": etapes, "html": code,
                                      "poids": float(ref["poids"]) if ref.get("poids") is not None else float(duree)}})
        journal(f"  exercice {ident} ({etapes} étapes, ~{duree} min, poids {sections[-1]['exercice']['poids']:g}) dans la partie {p.get('id')}")
    return sections


TYPES_QUESTION = ("vf", "qcm", "numerique")


def _manifeste_2004(ident: str, titre: str, fichiers: list[str]) -> str:
    """Renvoie le ``imsmanifest.xml`` SCORM 2004 (4e édition) : un seul SCO, le lecteur."""
    e = lambda t: html.escape(t, quote=True)
    lignes = "\n".join(f'      <file href="{e(f)}"/>' for f in fichiers)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="CF_{e(ident)}" version="1"
  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_v1p3"
  xmlns:adlseq="http://www.adlnet.org/xsd/adlseq_v1p3"
  xmlns:adlnav="http://www.adlnet.org/xsd/adlnav_v1p3"
  xmlns:imsss="http://www.imsglobal.org/xsd/imsss"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 imscp_v1p1.xsd http://www.adlnet.org/xsd/adlcp_v1p3 adlcp_v1p3.xsd http://www.adlnet.org/xsd/adlseq_v1p3 adlseq_v1p3.xsd http://www.adlnet.org/xsd/adlnav_v1p3 adlnav_v1p3.xsd http://www.imsglobal.org/xsd/imsss imsss_v1p0.xsd">
  <metadata>
    <schema>ADL SCORM</schema>
    <schemaversion>2004 4th Edition</schemaversion>
  </metadata>
  <organizations default="ORG_{e(ident)}">
    <organization identifier="ORG_{e(ident)}">
      <title>{e(titre)}</title>
      <item identifier="ITEM_{e(ident)}" identifierref="RES_{e(ident)}">
        <title>{e(titre)}</title>
      </item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES_{e(ident)}" type="webcontent" adlcp:scormType="sco" href="index.html">
{lignes}
    </resource>
  </resources>
</manifest>
'''


def _medias(parties: list[dict], sortie: Path) -> list[str]:
    """Renvoie les fichiers (chemins relatifs à la sortie) dont ces parties ont besoin : images, sons, dossiers d'exercices."""
    rels: list[str] = []
    for p in parties:
        for s in p["sections"]:
            for q in s["pas"]:
                rels += [q.get("fond"), q.get("audio"), (q.get("video") or {}).get("src")] + [a[1] for a in q.get("apparitions") or []]
                rels += [v.get("audio") for v in (q.get("voix") or {}).values()]
            if s.get("exercice"):
                d = sortie / s["exercice"]["base"]
                rels += [f.relative_to(sortie).as_posix() for f in sorted(d.rglob("*")) if f.is_file()]
    vus, res = set(), []
    for r in rels:
        if r and r not in vus and (sortie / r).is_file():
            vus.add(r); res.append(r)
    return res


def _paquet(zip_: Path, ident: str, titre: str, page: str, sortie: Path, rels: list[str]) -> Path:
    """Écrit le paquet SCORM 2004 ``zip_`` (manifeste, page du lecteur, médias) et renvoie son chemin."""
    fichiers = ["index.html"] + rels
    with zipfile.ZipFile(zip_, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("imsmanifest.xml", _manifeste_2004(ident, titre, fichiers))
        z.writestr("index.html", page)
        for r in rels:
            z.write(sortie / r, r, compress_type=zipfile.ZIP_STORED if Path(r).suffix.lower() in (".mp3", ".webp", ".png", ".wav") else zipfile.ZIP_DEFLATED)
    return zip_


def _banque(nom: str, dossier: Path, cache: dict) -> list | None:
    """Renvoie les questions d'une banque QuizForge (``…_banque.yaml``), cherchée à côté du chapitre puis dans ``data/quizforge``.

    Renvoie ``None`` si la banque est introuvable ; le résultat est gardé dans ``cache``.
    """
    if nom in cache:
        return cache[nom]
    import yaml
    f = dossier / nom
    if not f.is_file():
        racine = dossier.parent.parent / "quizforge"
        trouves = sorted(racine.rglob(Path(nom).name)) if racine.is_dir() else []
        f = trouves[0] if trouves else None
    cache[nom] = (yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("questions") or [] if f else None
    return cache[nom]


def _question(q: dict) -> dict:
    """Convertit une question de la banque en ce dont le lecteur a besoin (français seulement pour l'instant)."""
    x = {"type": q["type"], "titre": q.get("titre", ""), "question": q.get("question", ""), "feedback": q.get("feedback", "")}
    if q["type"] == "vf":
        x["reponse"] = bool(q.get("reponse"))
        x["feedback_juste"], x["feedback_faux"] = q.get("feedback_juste", ""), q.get("feedback_faux", "")
    elif q["type"] == "qcm":
        x["plusieurs"] = bool(q.get("plusieurs"))
        x["choix"] = [{"texte": c.get("texte", ""), "feedback": c.get("feedback", ""), "correct": bool(c.get("correct")),
                       "erreur": c.get("erreur", "")} for c in q.get("choix") or []]
    else:
        x["valeur"], x["tolerance"] = q.get("valeur"), q.get("tolerance") or 0
        x["erreurs"] = [{"valeur": e.get("valeur"), "tolerance": e.get("tolerance") or 0, "feedback": e.get("feedback", ""),
                         "code": e.get("code", "")} for e in q.get("erreurs") or []]
        x["feedback_juste"], x["feedback_faux"] = q.get("feedback_juste", ""), q.get("feedback_faux", "")
        x["indices"] = q.get("indices") or []
        x["unite"] = q.get("unite", "")
    return x


def questions_section(sec: dict, dossier: Path, cache: dict, journal=print) -> list[dict]:
    """Convertit les renvois « questions » d'une section en lots ``[{nombre, questions}]``.

    Le lecteur tire ``nombre`` questions par lot ; seuls les types vrai/faux, QCM et numérique sont gardés.
    """
    lots = []
    for ref in sec.get("questions") or []:
        if not isinstance(ref, dict) or not ref.get("banque"):
            continue
        banque = _banque(ref["banque"], dossier, cache)
        if banque is None:
            journal(f"  section {sec.get('id')} : banque introuvable « {ref['banque']} » (questions ignorées)")
            continue
        if ref.get("id"):
            choisies = [q for q in banque if q.get("titre") == ref["id"]]
        elif ref.get("etiquette"):
            choisies = [q for q in banque if ref["etiquette"] in (q.get("tags") or [])]
        else:
            choisies = list(banque)
        ecartees = [q.get("titre") for q in choisies if q.get("type") not in TYPES_QUESTION]
        if ecartees:
            journal(f"  section {sec.get('id')} : types non joués par le lecteur ({', '.join(map(str, ecartees))})")
        choisies = [_question(q) for q in choisies if q.get("type") in TYPES_QUESTION]
        if not choisies:
            journal(f"  section {sec.get('id')} : aucune question pour {ref}")
            continue
        lots.append({"nombre": min(int(ref.get("nombre") or len(choisies)), len(choisies)), "questions": choisies})
    return lots


def didacticiel(q: dict, chap: dict) -> dict | None:
    """Renvoie, pour un pas de didacticiel (gestes, bulle), ce que le lecteur joue en « Regarder » et attend en « À vous ».

    Renvoie ``None`` si le pas n'a ni geste ni bulle.
    """
    gestes = q.get("gestes") or []
    objets = q.get("objets") or []
    bulle = next((o for o in objets if o.get("type") == "bulle"), None)
    montre = next((o for o in objets if o.get("type") == "cadre" and o.get("id") == "cadre"), None)
    if not gestes and not bulle:
        return None
    reg = chap.get("reglages") or {}
    d: dict = {}
    if gestes:
        g = gestes[0]
        d["action"] = g.get("type", "clic")
        for a, b in (("point", "point"), ("cadre", "zone"), ("texte", "texte"), ("touches", "touches"), ("arrivee", "arrivee"),
                     ("crans", "crans"), ("accepte", "accepte"), ("tolerance", "tolerance")):
            if g.get(b) not in (None, "", []):
                d[a] = g[b]
        if (g.get("trajectoire") or reg.get("trajectoire")) == "enregistree" and g.get("trajet"):
            d["trajet"] = g["trajet"]
        if (g.get("cible") or {}).get("origine"):
            d["origine"] = g["cible"]["origine"]
        ou = [{"action": h.get("type", "clic"), **({"cadre": h["zone"]} if h.get("zone") else {}),
               **({"touches": h["touches"]} if h.get("touches") else {})} for h in gestes[1:]]
        if ou:
            d["ou"] = ou
    else:
        d["action"] = "montrer"
        if montre and montre.get("cadre"):
            d["cadre"] = montre["cadre"]
    if d.get("cadre") and not d.get("point"):
        c = d["cadre"]
        d["point"] = [c[0] + c[2] / 2, c[1] + c[3] / 2]
    if bulle:
        d["bulle"] = F.texte(bulle.get("texte"), (chap.get("langues") or {}).get("source") or "fr")
        if bulle.get("position"):
            d["bulle_position"] = bulle["position"]
    for k in ("observer", "indice"):
        if (q.get("a_vous") or {}).get(k) is not None:
            d[k] = q["a_vous"][k]
    for a, b in (("juste", "retour_juste"), ("faux", "retour_faux")):
        if (q.get("retours") or {}).get(a):
            d[b] = F.texte(q["retours"][a])
    if q.get("duree_s") and not q.get("audio"):
        d["lecture_s"] = q["duree_s"]
    return d


def construire(chapitre_yaml: Path, sortie: Path, largeur: int | None = None, fmt: str = "webp",
               audio: str = "mp3", journal=print, scorm: str | None = None) -> Path:
    """Construit le lecteur d'un chapitre et renvoie le chemin de ``<sortie>/index.html``.

    ``largeur`` : largeur maximale des images (réduction seulement) ; ``fmt`` : ``webp`` ou ``png`` ;
    ``audio`` : ``mp3`` pour convertir les sons (sinon recopiés) ; ``scorm`` : ``chapitre``, ``parties`` ou
    ``tout`` pour écrire aussi les paquets SCORM 2004. Arrête le programme (``SystemExit``) si le chapitre
    contient des erreurs bloquantes.
    """
    from PIL import Image
    chapitre_yaml = Path(chapitre_yaml)
    dossier = chapitre_yaml.parent
    chap = F.lire(chapitre_yaml)
    err, av_ = F.verifier(chap, dossier)
    if err:
        raise SystemExit("Chapitre non construit :\n  - " + "\n  - ".join(err))
    sortie = Path(sortie)
    (sortie / "images").mkdir(parents=True, exist_ok=True)
    (sortie / "audio").mkdir(parents=True, exist_ok=True)
    ecran = chap.get("ecran") or {}
    W = ecran.get("largeur") or 1440
    echelle = min(1.0, largeur / W) if largeur else 1.0
    fmt = (fmt or "webp").lower().lstrip(".")
    masques = chap.get("masques") or []
    reglages = json.dumps([largeur, fmt, audio, masques], sort_keys=True)
    temoin = sortie / "_reglages.json"
    memes = temoin.is_file() and temoin.read_text(encoding="utf-8") == reglages
    temoin.write_text(reglages, encoding="utf-8")
    images: dict[str, str] = {}
    sons: dict[str, str] = {}
    etat = {"mp3": audio == "mp3", "prevenu": False}

    def a_jour(src: Path, dst: Path) -> bool:
        return memes and dst.is_file() and dst.stat().st_size > 0 and dst.stat().st_mtime >= src.stat().st_mtime

    def image(rel: str | None) -> str | None:
        if not rel:
            return None
        if rel in images:
            return images[rel]
        src = dossier / rel
        nom = Path(rel).stem + (".webp" if fmt == "webp" else ".png")
        dst = sortie / "images" / nom
        if not a_jour(src, dst):
            with Image.open(src) as im:
                im = im.convert("RGB")
                if masques:                                  # zones floutées du chapitre (barre des tâches…)
                    import construire as C1
                    im = C1._masquer(im, masques, im.width / W)
                if echelle < 1:
                    im = im.resize((round(im.width * echelle), round(im.height * echelle)), Image.LANCZOS)
                if fmt == "webp":
                    im.save(dst, "WEBP", quality=86, method=5)
                else:
                    im.save(dst, "PNG", optimize=True)
        images[rel] = f"images/{nom}"
        return images[rel]

    videos: dict[str, str] = {}

    def video(rel: str) -> str:
        """Recopie la vidéo d'un pas telle quelle (déjà comprimée à l'import) dans ``<sortie>/videos/``."""
        if rel not in videos:
            src = dossier / rel
            dst = sortie / "videos" / src.name
            dst.parent.mkdir(parents=True, exist_ok=True)
            if not (dst.is_file() and dst.stat().st_size == src.stat().st_size and dst.stat().st_mtime >= src.stat().st_mtime):
                shutil.copy2(src, dst)
            videos[rel] = f"videos/{src.name}"
        return videos[rel]

    def son(rel: str | None) -> str | None:
        if not rel:
            return None
        if rel in sons:
            return sons[rel]
        src = dossier / rel
        if etat["mp3"] and src.suffix.lower() != ".mp3":
            dst = sortie / "audio" / (src.stem + ".mp3")
            try:
                if not a_jour(src, dst):
                    _mp3(src, dst)
                sons[rel] = f"audio/{dst.name}"
                return sons[rel]
            except Exception as e:                       # pas de PyAV, ou codec absent : on recopie le son d'origine
                etat["mp3"] = False
                if not etat["prevenu"]:
                    journal(f"  conversion MP3 impossible ({type(e).__name__} : {e}) : sons recopiés tels quels")
                    etat["prevenu"] = True
        dst = sortie / "audio" / src.name
        if not a_jour(src, dst):
            shutil.copy2(src, dst)
        sons[rel] = f"audio/{dst.name}"
        return sons[rel]

    N = F.noms(chap)
    banques: dict = {}
    src = (chap.get("langues") or {}).get("source") or "fr"
    autres = [l for l in (chap.get("langues") or {}).get("autres") or [] if l != src]

    def tr(obj: dict, champs) -> dict:
        """Renvoie les traductions présentes : ``{langue: {champ: texte}}`` (le lecteur retombe sur la source sinon)."""
        res = {}
        for l in autres:
            d = {c: obj[c][l] for c in champs if isinstance(obj.get(c), dict) and obj[c].get(l)}
            if d:
                res[l] = d
        return res
    parties = []
    for p in chap.get("parties") or []:
        sections = []
        for s in p.get("sections") or []:
            pas = []
            for q in s.get("pas") or []:
                if q.get("ecarte"):
                    continue
                objets = q.get("objets") or []
                x = {"id": q["id"], "nom": N.get(("pas", q["id"]), q["id"]), "fond": image(q.get("fond")),
                     "audio": son(q.get("audio")), "duree_s": q.get("duree_s"),
                     "phrases": [[ph.get("debut_s"), ph.get("fin_s"), F.texte(ph.get("texte"), src)]
                                 for ph in q.get("phrases") or [] if ph.get("debut_s") is not None],
                     "apparitions": sorted(([o.get("debut_s") or 0, image(o.get("fichier"))] for o in objets
                                            if o.get("type") == "apparition" and o.get("fichier")), key=lambda a: a[0]),
                     "objets": [{k: o[k] for k in ("type", "forme", "cadre", "position", "trajet", "couleur", "debut_s", "duree_s")
                                 if k in o} for o in objets if o.get("type") in OBJETS]}
                d = didacticiel(q, chap)
                if d:
                    x["didac"] = d
                v = q.get("video")
                if v and v.get("fichier") and (dossier / v["fichier"]).is_file():
                    x["video"] = {"src": video(v["fichier"]), "debut": float(v.get("debut_s") or 0),
                                  "fin": float(v.get("fin_s") or (v.get("debut_s") or 0) + (q.get("duree_s") or 0))}
                if not x["duree_s"]:
                    d, _ = F.duree_pas_s(q, None, W)
                    x["duree_s"] = round(max(d, len(F.narration_pas(q).split()) * 60 / F.MOTS_PAR_MINUTE, 2.0), 1)
                if not x["phrases"] and F.narration_pas(q, src).strip():
                    x["texte"] = F.narration_pas(q, src).strip()
                horodatees = [ph for ph in q.get("phrases") or [] if ph.get("debut_s") is not None]
                trad = {l: [ph["texte"].get(l, "") if isinstance(ph.get("texte"), dict) else "" for ph in horodatees] for l in autres}
                x["trad"] = {l: t for l, t in trad.items() if any(t)}
                if (q.get("source") or {}).get("voix") == "synthese":
                    x["synthese"] = True
                x["voix"] = {}
                for l, v in (q.get("voix") or {}).items():
                    if l == src or not v.get("audio") or not (dossier / v["audio"]).is_file() or len(v.get("phrases") or []) != len(x["phrases"]):
                        continue
                    t0 = [[a, b] for a, b, _ in x["phrases"]]
                    rc = lambda t: round(voix_mod.recaler(t, t0, v["phrases"], x["duree_s"], v["duree_s"]), 2)
                    x["voix"][l] = {"audio": son(v["audio"]), "duree_s": v["duree_s"], "temps": v["phrases"], "synthese": True,
                                    "apparitions": [[rc(a[0]), a[1]] for a in x["apparitions"]],
                                    "objets": [dict(o, debut_s=rc(o.get("debut_s") or 0),
                                                    duree_s=round(rc((o.get("debut_s") or 0) + (o.get("duree_s") or 0)) - rc(o.get("debut_s") or 0), 2))
                                               for o in x["objets"]]}
                pas.append(x)
            lots = questions_section(s, dossier, banques, journal)
            duree = sum(x["duree_s"] for x in pas) if pas else F.duree_section_s(s, largeur=W)
            sections.append({"id": s.get("id"), "nom": N.get(("section", p.get("id"), s.get("id")), ""),
                             "titre": F.texte(s.get("titre"), src), "objectif": F.texte(s.get("objectif"), src),
                             "narration": F.texte(s.get("narration"), src),
                             "ouverture": F.texte(s.get("ouverture"), src), "arret": s.get("arret", True),
                             "tr": tr(s, ("titre", "objectif", "ouverture")),
                             "annexes": s.get("annexes") or [],
                             "questions": sum(l["nombre"] for l in lots), "lots": lots,
                             "duree_s": round(duree, 1) if duree else None, "pas": pas})
        nom_p = N.get(("partie", p.get("id")), "")
        exos = exercices_partie(p, dossier, sortie, journal)
        for k, x in enumerate(exos):
            x["nom"] = nom_p + "-Ex" + (str(k + 1) if len(exos) > 1 else "")
        sections += exos
        parties.append({"id": p.get("id"), "nom": nom_p, "titre": F.texte(p.get("titre"), src), "tr": tr(p, ("titre",)),
                        "type": p.get("type", "tronc"), "place": p.get("place", "libre"),
                        "parcours": p.get("parcours"), "sections": sections})
    noms_l = {"fr": "Français", "en": "English", "es": "Español", "de": "Deutsch", "it": "Italiano", "pt": "Português",
              "zh": "中文", "ar": "العربية"}
    reg = chap.get("reglages") or {}
    donnees = {"titre": F.texte(chap.get("titre"), src), "tr": tr(chap, ("titre",)), "cle": dossier.name,
               "didac": {"modes": reg.get("modes") or ["regarder", "a_vous"], "essais": reg.get("essais") or 3,
                         "juste": F.texte((reg.get("retours") or {}).get("juste")) or "Oui.",
                         "faux": F.texte((reg.get("retours") or {}).get("faux")) or "Pas tout à fait.",
                         "trajectoire": reg.get("trajectoire") or "arc"},
               "langues": {"source": src, "autres": autres, "noms": {l: noms_l.get(l, l) for l in [src] + autres}}, "ecran": {"largeur": W, "hauteur": ecran.get("hauteur") or 1080},
               "parcours": [{"id": c.get("id"), "titre": F.texte(c.get("titre"), src), "tr": tr(c, ("titre",)), "annexes": c.get("annexes", "a_la_demande"), "questions": c.get("questions", "proposees"), "exercices": bool(c.get("exercices"))}
                            for c in chap.get("parcours") or []],
               "parties": parties}
    gabarit = (ICI / "lecteur2.html").read_text(encoding="utf-8")
    langue = html.escape((chap.get("langues") or {}).get("source", "fr"))

    def rendre(d: dict) -> str:
        return (gabarit.replace("__CHAPITRE_JSON__", json.dumps(d, ensure_ascii=False).replace("</", "<\\/"))
                .replace("__TITRE__", html.escape(d["titre"] or "Chapitre")).replace("__LANGUE__", langue))
    page = rendre(donnees)
    (sortie / "index.html").write_text(page, encoding="utf-8")
    utiles = [sortie / "index.html"] + [sortie / v for v in list(images.values()) + list(sons.values()) + list(videos.values())]
    taille = sum(f.stat().st_size for f in utiles if f.is_file())
    minutes = sum(x["duree_s"] for p in parties for s in p["sections"] for x in s["pas"]) / 60
    n_sec = sum(1 for p in parties for s in p["sections"] if s["pas"])
    journal(f"  {sortie / 'index.html'}")
    n_x = sum(1 for p in parties for s in p["sections"] if s.get("exercice"))
    if n_x:
        journal(f"  {n_x} exercice(s) ExoForge (dossier exercices/)")
    n_q = sum(s["questions"] for p in parties for s in p["sections"])
    if n_q:
        journal(f"  {n_q} question(s) posée(s) en fin de section")
    journal(f"  {n_sec} section(s) jouable(s), {minutes:.1f} min, {len(images)} images, {len(sons)} sons, {taille / 1e6:.1f} Mo"
            + (f" ({taille / 1e6 / minutes:.1f} Mo/min)" if minutes else ""))
    if scorm:
        paquets = []
        nom = sortie.name
        if scorm in ("chapitre", "tout"):
            paquets.append(_paquet(sortie.parent / f"{nom}_scorm2004.zip", nom, donnees["titre"] or nom, page, sortie,
                                   _medias(parties, sortie)))
        if scorm in ("parties", "tout"):
            jouable = lambda p: any(s["pas"] or s.get("exercice") for s in p["sections"])
            for p in parties:
                if p["type"] != "tronc":
                    continue
                ids = {p["id"]} | {a for s in p["sections"] for a in s["annexes"]}
                sous = [x for x in parties if x["id"] in ids]
                if not any(jouable(x) for x in sous):
                    continue
                d = dict(donnees, parties=sous, cle=f"{donnees['cle']}-{p['id']}", titre=f"{donnees['titre']} — {p['titre']}")
                ident = f"{nom}_{p['nom']}_{p['id']}"
                paquets.append(_paquet(sortie.parent / f"{ident}_scorm2004.zip", ident, d["titre"], rendre(d), sortie,
                                       _medias(sous, sortie)))
            seules = [p["id"] for p in parties if p["type"] != "tronc" and jouable(p)
                      and not any(p["id"] in s["annexes"] for x in parties if x["type"] == "tronc" for s in x["sections"])]
            if seules:
                journal(f"  parties hors de tout paquet par partie (appelées par aucune partie du tronc) : {', '.join(seules)}")
        for z in paquets:
            journal(f"  SCORM 2004 : {z} ({z.stat().st_size / 1e6:.1f} Mo)")
    return sortie / "index.html"
