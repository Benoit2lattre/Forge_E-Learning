"""CapsuleForge — construction du lecteur HTML à partir de capsule.yaml.

Sortie : <sortie>/index.html (lecteur autonome, données incluses : s'ouvre aussi depuis le disque)
et <sortie>/images/ (copiées, masques floutés, éventuellement réduites ou converties en WebP).
Les coordonnées restent celles de l'écran enregistré : le lecteur les ramène en pourcentages.
Licence : GPL v3.
"""
from __future__ import annotations

import html
import json
import shutil
from pathlib import Path

import assemblage as A

ICI = Path(__file__).resolve().parent
MATHJAX = ICI.parent / "exoforge" / "moteur" / "vendor" / "mathjax-tex-svg-full.js"


def _masquer(img, masques, echelle):
    """Pixellise puis floute, dans l'image, les zones ``[x, y, l, h]`` des masques."""
    from PIL import ImageFilter
    for m in masques or []:
        x, y, l, h = [int(round(v * echelle)) for v in m]
        x2, y2 = min(img.width, x + l), min(img.height, y + h)
        x, y = max(0, x), max(0, y)
        if x2 - x < 2 or y2 - y < 2:
            continue
        zone = img.crop((x, y, x2, y2))
        petit = zone.resize((max(1, (x2 - x) // 14), max(1, (y2 - y) // 14)))      # pixellisation, puis flou
        zone = petit.resize(zone.size).filter(ImageFilter.GaussianBlur(4))
        img.paste(zone, (x, y))
    return img


def construire(capsule_yaml: Path, sortie: Path, largeur: int | None = None, fmt: str = "png",
               apercu: bool = False) -> Path:
    """Construit le lecteur HTML d'une capsule et renvoie le chemin de ``<sortie>/index.html``.

    ``largeur`` : largeur maximale des images (réduction seulement) ; ``fmt`` : ``png`` ou ``webp``.
    ``apercu=True`` (éditeur) : images non optimisées et non refaites si elles sont à jour.
    Arrête le programme (``SystemExit``) si la capsule ne passe pas la vérification.
    """
    from PIL import Image
    capsule_yaml = Path(capsule_yaml)
    dossier = capsule_yaml.parent
    cap = A.lire_yaml(capsule_yaml)
    err, av = A.verifier(cap, dossier)
    if err:
        raise SystemExit("Capsule non construite :\n  - " + "\n  - ".join(err))
    sortie = Path(sortie)
    (sortie / "images").mkdir(parents=True, exist_ok=True)     # images réécrites une à une (rien n'est supprimé)

    W = cap["ecran"]["largeur"]
    echelle = min(1.0, largeur / W) if largeur else 1.0
    fmt = fmt.lower().lstrip(".")
    converties: dict[str, str] = {}
    # aperçu : une image déjà convertie avec les mêmes réglages et plus récente que sa source est gardée
    empreinte = json.dumps([cap.get("masques") or [], largeur, fmt], sort_keys=True)
    temoin = sortie / "images" / "_reglages.json"
    a_jour = apercu and temoin.is_file() and temoin.read_text(encoding="utf-8") == empreinte
    temoin.write_text(empreinte, encoding="utf-8")

    def convertir(rel: str | None) -> str | None:
        if not rel:
            return rel
        if rel in converties:
            return converties[rel]
        src = dossier / rel
        nom = Path(rel).stem + "." + ("webp" if fmt == "webp" else "png")
        dst = sortie / "images" / nom
        if a_jour and dst.is_file() and dst.stat().st_mtime >= src.stat().st_mtime:
            converties[rel] = f"images/{nom}"
            return converties[rel]
        with Image.open(src) as im:
            im = im.convert("RGB")
            masques = list(cap.get("masques") or [])
            im = _masquer(im, masques, 1.0)
            if echelle < 1:
                im = im.resize((round(im.width * echelle), round(im.height * echelle)), Image.LANCZOS)
            if fmt == "webp":
                im.save(dst, "WEBP", lossless=True, method=6)
            else:
                im.save(dst, "PNG", optimize=not apercu, compress_level=1 if apercu else 6)
        converties[rel] = f"images/{nom}"
        return converties[rel]

    donnees = {k: cap.get(k) for k in ("titre", "langue", "ecran", "reglages", "image_finale")}
    donnees["image_finale"] = convertir(cap.get("image_finale")) if cap.get("image_finale") and (dossier / cap["image_finale"]).is_file() else None
    donnees["etapes"] = []
    for et in cap["etapes"]:
        actifs = [p for p in et["pas"] if not p.get("ignorer")]
        if not actifs:
            continue
        e2 = {"titre": et.get("titre", ""), "narration": et.get("narration") or "", "arret": et.get("arret", True), "pas": []}
        if et.get("audio"):
            dst = sortie / "audio" / Path(et["audio"]).name
            dst.parent.mkdir(exist_ok=True)
            shutil.copy2(dossier / et["audio"], dst)
            e2["audio"] = f"audio/{dst.name}"
        for p in actifs:
            q = {k: p[k] for k in ("id", "action", "point", "cible", "bulle", "bulle_position", "texte", "touches",
                                   "arrivee", "crans", "accepte", "tolerance", "observer", "indice", "lecture_s",
                                   "trajectoire", "ou", "retour_juste", "retour_faux")
                 if p.get(k) not in (None, "")}
            if (p.get("trajectoire") or (cap.get("reglages") or {}).get("trajectoire")) == "enregistree" and p.get("trajet"):
                q["trajet"] = p["trajet"]           # le trajet enregistré n'est embarqué que s'il est rejoué
            q["image"] = convertir(p["image"])
            e2["pas"].append(q)
        donnees["etapes"].append(e2)

    gabarit = (ICI / "lecteur.html").read_text(encoding="utf-8")
    js = json.dumps(donnees, ensure_ascii=False).replace("</", "<\\/")
    # formules LaTeX ($…$) : MathJax (celui d'ExoForge) n'est embarqué que si la capsule en contient
    textes = " ".join(str(v) for et in donnees["etapes"] for v in
                      [et["narration"]] + [p.get(k, "") for p in et["pas"] for k in ("bulle", "retour_juste", "retour_faux")])
    balise = ""
    if ("$" in textes or "\\(" in textes) and MATHJAX.is_file():
        shutil.copy2(MATHJAX, sortie / "mathjax.js")
        shutil.copy2(MATHJAX.with_name("MATHJAX_LICENSE"), sortie / "MATHJAX_LICENSE") if MATHJAX.with_name("MATHJAX_LICENSE").is_file() else None
        balise = '<script src="mathjax.js" defer></script>'
    gabarit = gabarit.replace("__MATHJAX__", balise)
    page = (gabarit.replace("__CAPSULE_JSON__", js)
            .replace("__TITRE__", html.escape(cap.get("titre") or "Capsule"))
            .replace("__LANGUE__", html.escape(cap.get("langue") or "fr")))
    (sortie / "index.html").write_text(page, encoding="utf-8")
    for a in av:
        print("  avertissement :", a)
    taille = sum(f.stat().st_size for f in sortie.rglob("*") if f.is_file())
    n_ign = sum(1 for et in cap["etapes"] for p in et["pas"] if p.get("ignorer"))
    if n_ign:
        print(f"  {n_ign} pas écartés (ignorer: true)")
    print(f"  {sortie / 'index.html'}  ({len(converties)} images, {taille / 1e6:.1f} Mo)")
    return sortie / "index.html"
