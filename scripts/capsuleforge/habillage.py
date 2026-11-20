"""CapsuleForge — habillage d'une capsule pour une édition de cours (option ``construire --cours``).

La capsule reste nue (aucun établissement nommé) ; l'habillage est lu dans le profil de l'école de l'édition (clés
``charte`` et ``habillage``) et dans la déclaration du cours (``cours.yaml`` : titre, codes, promo, année), puis
appliqué à la construction : couleurs et logo du lecteur, écran d'accueil, pied de page sous l'image, crédits en fin
de capsule, filigrane sur les images, titre et nom des paquets SCORM.

Clé ``habillage`` du profil (toutes facultatives) ::

    habillage:
      logo: logo.png                         # dans le dossier du profil ; logo_nuit facultatif
      cadre: principal                       # couleur des bandes autour des images (rôle ou couleur de la charte)
      pied: "{code} · {promo} · {ecole}"     # sous l'image
      filigrane: {texte: "{ecole} · {promo}", position: bas-droite, opacite: 0.35}
      mentions: "Document réservé aux étudiants de {ecole}"
      licence: "CC BY-NC-SA 4.0"

Champs des textes : ``{cours}`` (titre du cours), ``{code}`` (code de l'enseignement), ``{bloc}``, ``{promo}``,
``{annee}`` (2026-2027), ``{ecole}``, ``{declinaison}``, ``{edition}``, ``{enseignant}``, ``{capsule}``.
Le filigrane n'est posé que pour une édition qui le demande (``filigrane: true`` dans ``cours.yaml``). La variante
de la capsule (``variante`` de la déclinaison, ou de l'édition qui la remplace) choisit ce qui ne vaut que pour ce
public (``variantes.py``).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / "commun"))
import chemins  # noqa: E402

POSITIONS = ("bas-droite", "bas-gauche", "haut-droite", "haut-gauche", "centre")
CHAMP = re.compile(r"\{(\w+)\}")


def remplir(texte: str | None, champs: dict) -> str:
    """Remplace les champs ``{…}`` connus ; un champ inconnu ou vide disparaît (avec un séparateur « · » orphelin)."""
    if not texte:
        return ""
    t = CHAMP.sub(lambda m: str(champs.get(m.group(1)) or ""), str(texte))
    t = re.sub(r"(\s*·\s*){2,}", " · ", t)
    return t.strip(" ·—-")


def _fichier_profil(nom: str) -> Path | None:
    for f in chemins.fichiers_profils():
        if chemins.nom_profil(f) == nom:
            return f
    return None


def _couleur(charte: dict, v) -> str | None:
    """Rôle (``principal``), nom de couleur de la charte (``violet``) ou valeur (``470A68``) → ``#470A68``."""
    if not v:
        return None
    couleurs = charte.get("couleurs") or {}
    roles = charte.get("roles") or {}
    v = roles.get(v, v)
    v = couleurs.get(v, v)
    v = str(v).lstrip("#")
    return "#" + v if re.fullmatch(r"[0-9A-Fa-f]{6}", v) else None


def pour_cours(spec: str, titre_capsule: str = "") -> dict:
    """Habillage d'une édition (``--cours cours[:déclinaison[/édition]]``) : champs, couleurs, logo, textes, filigrane."""
    import yaml
    import cours_options
    import cours as K
    r = cours_options.resoudre(spec)
    c = K.trouver(r["cours"])
    d = K.declinaison(c, r["declinaison"]) if r.get("declinaison") else None
    e = K.edition(c, r["declinaison"], r["edition"]) if d and r.get("edition") else None
    profil = r.get("profil")
    fp = _fichier_profil(profil) if profil else None
    pr = (yaml.safe_load(fp.read_text(encoding="utf-8")) or {}) if fp else {}
    charte = pr.get("charte") or {}
    hab = pr.get("habillage") if isinstance(pr.get("habillage"), dict) else {}
    annee = str((e or {}).get("nom") or "")
    codes = (d or {}).get("codes") or {}
    champs = {"cours": str(c.get("titre") or c["nom"]), "code": codes.get("enseignement") or "", "bloc": codes.get("bloc") or "",
              "promo": (e or {}).get("promo") or "", "annee": f"{annee}-{int(annee) + 1}" if annee.isdigit() else annee,
              "ecole": str(pr.get("nom") or (d or {}).get("ecole") or ""), "declinaison": (d or {}).get("nom") or "",
              "edition": annee, "enseignant": str((e or {}).get("enseignant") or c.get("enseignant") or c.get("auteur") or ""),
              "capsule": titre_capsule}
    roles = charte.get("roles") or {}
    principal = _couleur(charte, "principal") if "principal" in roles else None
    couleurs = {k: v for k, v in {"navy": principal, "navy2": principal,
                                  "slate-l": _couleur(charte, "principal_clair") if "principal_clair" in roles else None,
                                  "texte": _couleur(charte, "texte") if "texte" in roles else None}.items() if v}
    logo = None
    if hab.get("logo") and fp:
        f = fp.parent / str(hab["logo"])
        logo = f if f.is_file() else None
    fil = hab.get("filigrane") if isinstance(hab.get("filigrane"), dict) else None
    filigrane = None
    if fil and (e or {}).get("filigrane"):
        filigrane = {"texte": remplir(fil.get("texte") or "{ecole} · {promo}", champs),
                     "position": fil.get("position") if fil.get("position") in POSITIONS else "bas-droite",
                     "opacite": max(0.05, min(1.0, float(fil.get("opacite") or 0.35)))}
    return {"spec": spec, "cours": r["cours"], "declinaison": r.get("declinaison"), "edition": r.get("edition"),
            "libelle": r["libelle"], "profil": profil, "champs": champs, "couleurs": couleurs,
            "cadre": _couleur(charte, hab.get("cadre")) or principal,
            "police_texte": charte.get("police_texte"), "police_titres": charte.get("police_titres"),
            "polices_url": charte.get("polices_url"), "logo": logo,
            "pied": remplir(hab.get("pied") or "{code} · {promo} · {ecole}", champs),
            "mentions": remplir(hab.get("mentions"), champs), "licence": str(hab.get("licence") or ""),
            "filigrane": filigrane, "variante": (e or {}).get("variante") or (d or {}).get("variante") or None}


def resume(h: dict) -> dict:
    """Ce qui fait l'empreinte d'un habillage (pas de chemin absolu, le logo par son contenu)."""
    import hashlib
    out = {k: v for k, v in h.items() if k not in ("logo", "spec")}
    if h.get("logo"):
        out["logo"] = hashlib.md5(Path(h["logo"]).read_bytes()).hexdigest()[:12]
    return out


def filigraner(im, f: dict):
    """Pose le filigrane ``f`` ({texte, position, opacite}) sur l'image PIL ``im`` (RGB) et la renvoie."""
    from PIL import Image, ImageDraw, ImageFont
    if not f or not f.get("texte"):
        return im
    taille = max(12, round(im.height * 0.035))
    police = None
    for nom in ("DejaVuSans-Bold.ttf", "arialbd.ttf", "Arial Bold.ttf", "segoeuib.ttf"):
        try:
            police = ImageFont.truetype(nom, taille)
            break
        except OSError:
            continue
    police = police or ImageFont.load_default()
    calque = Image.new("RGBA", im.size, (0, 0, 0, 0))
    dessin = ImageDraw.Draw(calque)
    x0, y0, x1, y1 = dessin.textbbox((0, 0), f["texte"], font=police)
    lt, ht = x1 - x0, y1 - y0
    marge = round(im.height * 0.03)
    pos = f.get("position") or "bas-droite"
    x = {"bas-droite": im.width - lt - marge, "haut-droite": im.width - lt - marge}.get(pos, marge)
    y = {"bas-droite": im.height - ht - marge * 2, "bas-gauche": im.height - ht - marge * 2}.get(pos, marge)
    if pos == "centre":
        x, y = (im.width - lt) // 2, (im.height - ht) // 2
    a = round(255 * float(f.get("opacite") or 0.35))
    dessin.text((x - x0 + 1, y - y0 + 1), f["texte"], font=police, fill=(0, 0, 0, a // 2))
    dessin.text((x - x0, y - y0), f["texte"], font=police, fill=(255, 255, 255, a))
    return Image.alpha_composite(im.convert("RGBA"), calque).convert("RGB")


def nom_paquet(h: dict | None, capsule: str, label: str | None = None) -> str:
    """Nom de base des paquets : ``traction_ecole1-meca_2026_v1`` (capsule nue : le nom de la capsule)."""
    if not h:
        return capsule
    morceaux = [capsule, h.get("declinaison") or h["cours"], h.get("edition") or "", label or ""]
    return "_".join(re.sub(r"[^\w.-]+", "-", m) for m in morceaux if m)
