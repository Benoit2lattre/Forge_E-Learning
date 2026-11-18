"""Atelier Forge — écran « Capsules » (CapsuleForge) : liste des capsules, état section par section, actions.

Une capsule est un dossier de ``data/capsuleforge`` qui contient ``chapitre.yaml`` (lecteur actuel) ou seulement
``capsule.yaml`` (didacticiel enregistré pour l'ancien lecteur, à mettre à jour). L'état est lu dans le fichier ;
les actions sont des commandes ``capsuleforge`` lancées par l'atelier (voir ``forge.Atelier.actions``).

Licence : GPL v3.
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / "commun"))
sys.path.insert(0, str(ICI.parent / "capsuleforge"))
import chemins                    # noqa: E402

DOSSIER = chemins.DATA / "capsuleforge"
SORTIES = chemins.SORTIES / "capsuleforge"
SCRIPT = chemins.SCRIPTS / "capsuleforge" / "capsuleforge.py"
REGLAGES = chemins.DATA / "_atelier" / "reglages.json"
GENRES = {"pptx": "diaporama", "video": "vidéo", "captation": "didacticiel", "ajout": "didacticiel", "approj": "didacticiel"}
LANGUES = {"fr": "français", "en": "anglais", "es": "espagnol", "de": "allemand", "it": "italien", "pt": "portugais",
           "ar": "arabe", "zh": "chinois"}


def F():
    import format_chapitre
    return format_chapitre


# ------------------------------------------------------------------------------------------------ réglages
def reglages() -> dict:
    try:
        return json.loads(REGLAGES.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def garder_reglage(cle: str, valeur):
    r = reglages()
    r[cle] = valeur
    REGLAGES.parent.mkdir(parents=True, exist_ok=True)
    REGLAGES.write_text(json.dumps(r, ensure_ascii=False, indent=1), encoding="utf-8")


# ------------------------------------------------------------------------------------------------ liste
def dossier(nom: str) -> Path:
    """Dossier d'une capsule de ``data/capsuleforge`` (nom exact, sans chemin) ; ``ValueError`` sinon."""
    if not nom or "/" in nom or "\\" in nom or nom.startswith((".", "_")):
        raise ValueError("capsule inconnue")
    d = DOSSIER / nom
    if not ((d / "chapitre.yaml").is_file() or (d / "capsule.yaml").is_file()):
        raise ValueError(f"capsule inconnue : {nom}")
    return d


def texte(v) -> str:
    return F().texte(v) if v is not None else ""


def liste() -> list[dict]:
    out = []
    if not DOSSIER.is_dir():
        return out
    for d in sorted(DOSSIER.iterdir(), key=lambda x: x.name.lower()):
        if not d.is_dir() or d.name.startswith(("_", ".")):
            continue
        ch, cap = d / "chapitre.yaml", d / "capsule.yaml"
        if not (ch.is_file() or cap.is_file()):
            continue
        try:
            c = F().lire(ch if ch.is_file() else cap)
        except Exception:
            c = {}
        out.append({"nom": d.name, "titre": texte(c.get("titre")) or d.name,
                    "ancienne": not ch.is_file(), "construit": _date(SORTIES / d.name / "index.html")})
    return out


def _date(f: Path):
    return f.stat().st_mtime if f.is_file() else None


# ------------------------------------------------------------------------------------------------ détail
def _phrases_texte(q: dict, langue: str) -> tuple[int, int]:
    """(phrases du pas, phrases qui ont un texte dans ``langue``)."""
    ph = q.get("phrases") or []
    n = sum(1 for x in ph if isinstance(x.get("texte"), dict) and (x["texte"].get(langue) or "").strip())
    return len(ph), n


def _etat(fait: int, total: int) -> dict:
    """État d'une colonne : ``fait`` sur ``total`` (``total`` 0 = sans objet)."""
    return {"fait": fait, "total": total}


def detail(nom: str) -> dict:
    d = dossier(nom)
    ch = d / "chapitre.yaml"
    if not ch.is_file():
        cap = F().lire(d / "capsule.yaml")
        return {"nom": nom, "titre": texte(cap.get("titre")) or nom, "ancienne": True,
                "etapes": len(cap.get("etapes") or []), "pas": sum(len(e.get("pas") or []) for e in cap.get("etapes") or []),
                "construit": _date(SORTIES / nom / "index.html"),
                "lecteur": f"/dist/capsuleforge/{nom}/index.html" if (SORTIES / nom / "index.html").is_file() else None}
    Fm = F()
    chap = Fm.lire(ch)
    N = Fm.noms(chap)
    langues = chap.get("langues") or {}
    source = langues.get("source") or "fr"
    autres = [l for l in langues.get("autres") or [] if l != source]
    largeur = (chap.get("ecran") or {}).get("largeur") or 1920
    parties, diaporamas, total_s = [], {}, 0.0
    for p in chap.get("parties") or []:
        sections = []
        for s in p.get("sections") or []:
            pas = [q for q in s.get("pas") or [] if not q.get("ecarte")]
            src = s.get("source") or {}
            types = sorted({GENRES.get((q.get("source") or {}).get("type"), "didacticiel" if q.get("gestes") else "diapositive") for q in pas})
            if src.get("fichier"):
                diaporamas.setdefault(src["fichier"], []).append(N[("section", p.get("id"), s.get("id"))])
            attendus = len(src.get("diapos") or []) if src.get("fichier") else 0
            repris = sum(1 for q in pas if (q.get("source") or {}).get("type") == "pptx")
            images = sum(1 for q in pas if q.get("fond") and (d / q["fond"]).is_file())
            avec_son = [q for q in pas if q.get("audio")]
            parle = [q for q in pas if q.get("audio") or q.get("phrases") or (q.get("narration") or "").strip()
                     or (q.get("source") or {}).get("type") in ("pptx", "video")]
            texte_ok = sum(1 for q in parle if q.get("phrases") or (q.get("narration") or "").strip())
            relus = sum(1 for q in pas if (q.get("source") or {}).get("relu"))
            par_langue = {}
            for l in autres:
                tot = fait = 0
                for q in pas:
                    a, b = _phrases_texte(q, l)
                    tot, fait = tot + a, fait + b
                voix = sum(1 for q in pas if (q.get("voix") or {}).get(l))
                par_langue[l] = {"texte": _etat(fait, tot), "voix": _etat(voix, len(parle) if tot else 0)}
            synth = sum(1 for q in pas if (q.get("source") or {}).get("voix") == "synthese")
            dur = Fm.duree_section_s(s, largeur=largeur)
            total_s += dur or 0
            sections.append({
                "id": s.get("id"), "nom": N[("section", p.get("id"), s.get("id"))], "titre": texte(s.get("titre")),
                "duree_s": dur, "pas": len(pas), "types": types,
                "source": (f"{src['fichier']}, diapositives {_plage(src.get('diapos'))}" if src.get("fichier") else ""),
                "repris": _etat(repris, attendus), "images": _etat(images, len(pas)),
                "texte": _etat(texte_ok, len(parle)), "relu": _etat(relus, len(avec_son)),
                "voix_source": synth, "langues": par_langue,
                "questions": sum(int(x.get("nombre") or 1) for x in s.get("questions") or [])})
        ex = p.get("exercice")
        exercices = [texte((e or {}).get("titre")) or (e or {}).get("fiche") for e in (ex if isinstance(ex, list) else [ex] if ex else [])]
        parties.append({"id": p.get("id"), "nom": N[("partie", p.get("id"))], "titre": texte(p.get("titre")),
                        "type": p.get("type", "tronc"), "sections": sections, "exercices": exercices})
    err, av = Fm.verifier(chap, d)
    trad = {}
    for l in autres:
        f = d / "traductions" / f"{l}.yaml"
        try:
            el = (Fm.lire(f).get("elements") or []) if f.is_file() else []
        except Exception:
            el = []
        trad[l] = {"fichier": f.is_file(), "elements": len(el), "relus": sum(1 for e in el if e.get("relu"))}
    connus = reglages().get("diaporamas") or {}
    return {"nom": nom, "titre": texte(chap.get("titre")) or nom, "ancienne": False, "aussi_ancienne": (d / "capsule.yaml").is_file(),
            "langue": source, "autres": autres, "noms_langues": LANGUES, "duree_s": total_s,
            "parties": parties, "erreurs": err, "avertissements": av, "traductions": trad,
            "diaporamas": [{"fichier": f, "sections": secs, "chemin": _diaporama(f, connus)} for f, secs in diaporamas.items()],
            "construit": _date(SORTIES / nom / "index.html"),
            "lecteur": f"/dist/capsuleforge/{nom}/index.html" if (SORTIES / nom / "index.html").is_file() else None,
            "paquets": paquets(nom), "voix": voix_disponibles()}


def _plage(diapos) -> str:
    v = sorted(int(x) for x in diapos or [])
    if not v:
        return "?"
    morceaux, debut = [], v[0]
    for a, b in zip(v, v[1:] + [None]):
        if b != a + 1:
            morceaux.append(f"{debut}" if debut == a else f"{debut} à {a}")
            debut = b
    return ", ".join(morceaux)


def _diaporama(nom_fichier: str, connus: dict) -> str | None:
    """Chemin d'un diaporama : retenu par l'atelier, à côté du chapitre, ou cherché dans e_learning (voisin du dépôt)."""
    c = connus.get(nom_fichier)
    if c and Path(c).is_file():
        return c
    for base, prof in ((DOSSIER, 3), (chemins.RACINE.parent / "e_learning", 4)):
        trouve = _chercher(base, nom_fichier, prof)
        if trouve:
            return str(trouve)
    return None


def _chercher(base: Path, nom: str, profondeur: int):
    if not base.is_dir() or profondeur < 0:
        return None
    try:
        enfants = list(base.iterdir())
    except OSError:
        return None
    for f in enfants:
        if f.is_file() and f.name == nom:
            return f
    for f in enfants:
        if f.is_dir() and not f.name.startswith((".", "_")) and f.name not in ("images", "audio", "sauvegardes", "videos"):
            r = _chercher(f, nom, profondeur - 1)
            if r:
                return r
    return None


def paquets(nom: str) -> list[dict]:
    if not SORTIES.is_dir():
        return []
    out = []
    for z in sorted(SORTIES.glob(f"{nom}_*.zip")):
        m = re.fullmatch(re.escape(nom) + r"(?:_([A-Z]+)_(.+?))?_scorm(12|2004)", z.stem)
        if not m:
            continue
        version = "SCORM 1.2" if m.group(3) == "12" else "SCORM 2004"
        quoi = f"partie {m.group(1)} ({m.group(2).replace('_', ' ')})" if m.group(1) else "capsule entière"
        out.append({"fichier": z.name, "libelle": quoi, "version": version, "chemin": chemins_rel(z), "date": z.stat().st_mtime})
    out.sort(key=lambda x: (x["libelle"] != "capsule entière", x["libelle"], x["version"]))
    return out


def chemins_rel(f: Path) -> str:
    try:
        return f.resolve().relative_to(chemins.RACINE).as_posix()
    except ValueError:
        return str(f)


def voix_disponibles() -> dict:
    """Voix Piper téléchargées, par langue (fr_FR-tom-medium → fr) ; voix Edge proposées par défaut."""
    piper = {}
    for v in sorted((DOSSIER / "_voix").glob("*.onnx")):
        piper.setdefault(v.stem.split("_")[0], []).append(v.stem)
    try:
        import voix as V
        edge = {l: [n] for l, n in V.VOIX_DEFAUT.get("edge", {}).items()}
        for l, n in V.VOIX_DEFAUT.get("piper", {}).items():
            if n not in piper.get(l, []):
                piper.setdefault(l, []).append(n + " (à télécharger)")
    except Exception:
        edge = {}
    return {"piper": piper, "edge": edge}


# ------------------------------------------------------------------------------------------------ commandes
def ident_section(titre: str, existants: set) -> str:
    s = unicodedata.normalize("NFD", titre.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")[:24] or "section"
    base, k = s, 2
    while s in existants:
        s, k = f"{base}_{k}", k + 1
    return s


def sections_valides(d: Path, ids) -> list[str]:
    if not ids:
        return []
    chap = F().lire(d / "chapitre.yaml")
    connus = {p.get("id") for p in chap.get("parties") or []} | {s.get("id") for p in chap.get("parties") or []
                                                                    for s in p.get("sections") or []}
    ids = [str(i) for i in ids]
    inconnus = [i for i in ids if i not in connus]
    if inconnus:
        raise ValueError("sections inconnues : " + ", ".join(inconnus))
    return ids


def langue_valide(l: str) -> str:
    l = (l or "").strip().lower()
    if not re.fullmatch(r"[a-z]{2,3}(-[a-z0-9]{2,8})?", l):
        raise ValueError(f"code de langue invalide : {l!r} (ex. en, es, de)")
    return l


def nom_propose(titre: str) -> str:
    """Nom de dossier libre tiré d'un titre (« Traction simple » → traction_simple)."""
    s = unicodedata.normalize("NFD", (titre or "").lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    base = re.sub(r"[^a-z0-9]+", "_", s).strip("_")[:40] or "capsule"
    nom, k = base, 2
    while (DOSSIER / nom).exists():
        nom, k = f"{base}_{k}", k + 1
    return nom


def argv_base(py: str, cmd: str) -> list[str]:
    return [py, str(SCRIPT), cmd]
