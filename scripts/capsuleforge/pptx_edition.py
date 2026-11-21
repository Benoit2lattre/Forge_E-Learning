"""CapsuleForge — images des diapositives PowerPoint d'une édition (``construire --cours``).

Les images d'un chapitre repris d'un diaporama sont celles de la capsule nue. Une diapositive qui porte des formes
d'édition (« cf édition », « cf édition ecole1 », « cf nu ») ou des champs (``{cours}``, ``{promo}``…) est
réexportée par PowerPoint pour l'édition : formes montrées pour son public (école du profil et variantes),
champs remplis. Les autres diapositives gardent les images nues. Si le profil de l'école donne un modèle
PowerPoint (``habillage: {modele: modele_ecole.potx}``), toutes les diapositives sont réexportées avec ce modèle
appliqué (thème, polices, couleurs et masque de l'école ; dispositions appariées par leur nom).

Le diaporama est cherché là où il a été repris (``source.chemin`` de la section), à côté du chapitre, dans
``sources/``, puis parmi les diaporamas retenus par l'atelier. Les images d'une édition sont gardées en cache dans ``<chapitre>/_editions/<clé>/`` : elles ne sont refaites que
si le diaporama, la liste des diapositives, l'habillage ou la largeur change. Sans PowerPoint (hors Windows), le
cache sert s'il est à jour ; sinon la construction s'arrête plutôt que de ranger une édition mal habillée.
Licence : GPL v3.
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pptx_lire as L

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "commun"))
import chemins  # noqa: E402


def publics(h: dict) -> list[str]:
    """Publics d'une édition, pour les formes « cf édition … » : l'école du profil, puis les variantes actives."""
    out = [str(h["profil"]).lower()] if h.get("profil") else []
    out += [str(v).lower() for v in h.get("variante") or []]
    return list(dict.fromkeys(out))


def trouver(dossier: Path, fichier: str, chemin: str | None = None) -> Path | None:
    """Cherche le diaporama d'une section : chemin noté à la reprise (``source.chemin``, relatif au chapitre), à côté
    du chapitre, dans ``sources/`` (et plus bas), puis celui que l'atelier a retenu (réglages de l'atelier)."""
    cands = []
    if chemin:
        c = Path(chemin)
        cands.append(c if c.is_absolute() else dossier / c)
    cands += [dossier / fichier, dossier / "sources" / fichier]
    for c in cands:
        if c.is_file() and c.name == fichier:
            return c.resolve()
    src = dossier / "sources"
    if src.is_dir():
        for c in sorted(src.rglob(fichier)):
            if c.is_file() and not c.name.startswith("~$"):
                return c
    try:                                                # diaporama choisi dans l'atelier (« Reprendre le diaporama »)
        connus = json.loads((chemins.DATA / "_atelier" / "reglages.json").read_text(encoding="utf-8")).get("diaporamas") or {}
        c = Path(connus.get(fichier) or "")
        if c.name == fichier and c.is_file():
            return c
    except (OSError, ValueError, AttributeError):
        pass
    return None


def _md5(f: Path) -> str:
    h = hashlib.md5()
    with open(f, "rb") as fl:
        for bloc in iter(lambda: fl.read(1 << 20), b""):
            h.update(bloc)
    return h.hexdigest()


def a_habiller(d: dict, masque: str, champs_masque: list, modele: bool = False) -> bool:
    """Vrai si l'image d'une diapositive change d'une édition à l'autre (toutes, avec un modèle d'école)."""
    return bool(modele or d.get("edition") or d.get("champs") or (masque == "garder" and champs_masque))


def controler_modele(chemin: Path, modele: Path, diapos: list[int], journal=print) -> list[int]:
    """Compare le diaporama et le modèle de l'école avant de l'appliquer ; renvoie les diapositives dont la
    disposition n'existe pas dans le modèle (PowerPoint en choisirait une autre)."""
    a, b = L.dispositions(chemin), L.dispositions(modele)
    if a["taille"] and b["taille"] and a["taille"][0] * b["taille"][1] != a["taille"][1] * b["taille"][0]:
        journal(f"  {chemin.name} et {modele.name} n'ont pas le même format de diapositive : la mise en page et les "
                "annotations calées peuvent se décaler")
    manquent = [n for n in diapos if a["diapos"].get(n) and a["diapos"][n] not in b["dispositions"]]
    if manquent:
        noms = sorted({a["diapos"][n] for n in manquent})
        journal(f"  dispositions absentes de {modele.name} : {', '.join(noms)} (diapositives "
                f"{', '.join(map(str, manquent))}) ; elles gardent le thème du diaporama")
    return manquent


def plan(y: Path, chap: dict, h: dict, journal=print) -> dict | None:
    """Prépare l'habillage PowerPoint d'une édition, sans PowerPoint : diapositives à refaire par diaporama.

    Renvoie ``None`` si aucune diapositive du chapitre n'en a besoin. Sinon ``{publics, champs, masque, largeur,
    diaporamas: [{fichier, chemin, md5, diapos, rels}], cle}``, où ``rels`` sont les images du chapitre remplacées.
    """
    dossier = Path(y).parent
    par_fichier: dict = {}
    notes: dict = {}                                    # chemins notés à la reprise
    for p in chap.get("parties") or []:
        for s in p.get("sections") or []:
            for q in s.get("pas") or []:
                src = q.get("source") or {}
                if src.get("type") == "pptx" and src.get("fichier") and src.get("diapo"):
                    par_fichier.setdefault(src["fichier"], []).append(q)
                    if (s.get("source") or {}).get("chemin"):
                        notes.setdefault(src["fichier"], s["source"]["chemin"])
    if not par_fichier:
        return None
    masque = L.masque_chapitre(chap)
    modele = Path(h["modele"]) if h.get("modele") else None
    champs_modele = L.dispositions(modele)["champs_masque"] if modele else []
    pub = publics(h)
    largeur = (chap.get("ecran") or {}).get("largeur") or 1440
    diaporamas, utilises = [], set()
    for fichier, pas in sorted(par_fichier.items()):
        chemin = trouver(dossier, fichier, notes.get(fichier))
        if chemin is None:
            journal(f"  diaporama {fichier} introuvable (ni à l'endroit de la reprise, ni à côté du chapitre, ni dans "
                    "sources/) : images de la capsule nue, sans formes d'édition ni champs")
            continue
        lu = L.lire(chemin)
        par_n = {d["n"]: d for d in lu["diapos"]}
        voulus = sorted({q["source"]["diapo"] for q in pas})
        a_faire = [n for n in voulus if n in par_n and a_habiller(par_n[n], masque, lu.get("champs_masque"), bool(modele))]
        if not a_faire:
            continue
        rels = sorted({r for q in pas if q["source"]["diapo"] in a_faire
                       for r in [q.get("fond")] + [o.get("fichier") for o in q.get("objets") or [] if o.get("type") == "apparition"]
                       if r})
        for n in a_faire:
            utilises |= {c for v in (par_n[n].get("champs") or {}).values() for c in v}
        if masque == "garder" and not modele:
            utilises |= set(lu.get("champs_masque") or [])
        utilises |= set(champs_modele)
        sans_modele = controler_modele(chemin, modele, a_faire, journal) if modele else []
        diaporamas.append({"fichier": fichier, "chemin": str(chemin), "md5": _md5(chemin), "diapos": a_faire, "rels": rels,
                           "sans_modele": sans_modele})
    if not diaporamas:
        return None
    champs = {c: str((h.get("champs") or {}).get(c) or "") for c in sorted(utilises)}
    pl = {"publics": pub, "champs": champs, "masque": masque, "largeur": largeur, "diaporamas": diaporamas,
          "modele": str(modele) if modele else None, "modele_md5": _md5(modele) if modele else None}
    pl["cle"] = hashlib.md5(json.dumps([pub, champs, masque, largeur, pl["modele_md5"]], sort_keys=True)
                            .encode("utf-8")).hexdigest()[:10]
    return pl


def resume(pl: dict | None) -> dict | None:
    """Ce qui fait l'empreinte de l'habillage PowerPoint (sans chemin) : diaporamas, diapositives, habillage, code."""
    if not pl:
        return None
    ici = Path(__file__).resolve().parent
    code = hashlib.md5(b"".join((ici / n).read_bytes() for n in ("pptx_images.py", "pptx_edition.py"))).hexdigest()[:12]
    return {"diaporamas": [{k: d[k] for k in ("fichier", "md5", "diapos")} for d in pl["diaporamas"]],
            "publics": pl["publics"], "champs": pl["champs"], "masque": pl["masque"], "largeur": pl["largeur"],
            "modele": pl.get("modele_md5"), "code": code}


def produire(pl: dict | None, dossier: Path, journal=print) -> dict:
    """Produit (ou reprend du cache) les images de l'édition et renvoie ``{image du chapitre: image de l'édition}``.

    Arrête le programme si PowerPoint manque et que le cache n'est pas à jour.
    """
    if not pl:
        return {}
    dossier = Path(dossier)
    racine = dossier / "_editions" / pl["cle"]
    out = {}
    resu = resume(pl)
    for d in pl["diaporamas"]:
        cache = racine / Path(d["fichier"]).stem
        temoin = cache / "temoin.json"
        attendu = json.dumps({**{k: d[k] for k in ("md5", "diapos")}, **{k: resu[k] for k in ("publics", "champs", "masque", "largeur", "modele", "code")}},
                             sort_keys=True)
        complet = all((cache / r).is_file() for r in d["rels"] if r.startswith("images/"))
        if temoin.is_file() and temoin.read_text(encoding="utf-8") == attendu and complet:
            journal(f"  {d['fichier']} : images de l'édition reprises du cache ({len(d['diapos'])} diapositive(s))")
        else:
            if sys.platform != "win32":
                raise SystemExit(f"{d['fichier']} porte des formes d'édition ou des champs (diapositives "
                                 f"{', '.join(map(str, d['diapos']))}) : leurs images pour cette édition demandent "
                                 "PowerPoint (Windows). Construire l'édition sous Windows ; le cache servira ensuite.")
            import pptx_images
            lu = L.lire(Path(d["chemin"]))
            diapos = [x for x in lu["diapos"] if x["n"] in d["diapos"]]
            journal(f"  {d['fichier']} : images de l'édition pour {', '.join(pl['publics']) or 'toute édition'}, "
                    f"diapositives {', '.join(map(str, d['diapos']))}"
                    + (f", modèle {Path(pl['modele']).name}" if pl.get("modele") else ""))
            cache.mkdir(parents=True, exist_ok=True)
            if temoin.is_file():
                temoin.unlink()
            pptx_images.exporter(Path(d["chemin"]), diapos, cache, pl["largeur"], journal=journal,
                                 edition={"publics": pl["publics"], "champs": pl["champs"], "masque": pl["masque"],
                                          "modele": pl.get("modele")})
            temoin.write_text(attendu, encoding="utf-8")
        for r in d["rels"]:
            if (cache / r).is_file():
                out[r] = cache / r
    return out
