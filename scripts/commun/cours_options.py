"""Forge E-Learning — option ``--cours`` commune aux outils : réglages d'un cours, d'une déclinaison, d'une édition.

``--cours traction``, ``--cours traction:ecole1-meca`` ou ``--cours traction:ecole1-meca/2026`` (déclinaison et édition facultatives :
la seule déclinaison du cours, puis son édition en cours). Les options données sur la ligne de commande l'emportent ;
les étiquettes du cours s'ajoutent à celles données.
"""
from __future__ import annotations

import datetime as dt
import sys
from pathlib import Path

import chemins

sys.path.insert(0, str(chemins.SCRIPTS / "forge"))


def resoudre(spec: str) -> dict:
    """Réglages pour ``spec`` : profil, étiquettes, catégorie Moodle, langues, séances, effectif, dossiers, libellé."""
    import cours as K
    nom, _, reste = (spec or "").partition(":")
    decl_nom, _, ed_nom = reste.partition("/")
    c = K.trouver(nom.strip())
    decls = c.get("declinaisons") or []
    d = K.declinaison(c, decl_nom) if decl_nom else (decls[0] if len(decls) == 1 else None)
    ed = None
    if d:
        ed_nom = ed_nom or K.en_cours(d)
        ed = K.edition(c, d["nom"], ed_nom) if ed_nom else None
    profils = {chemins.nom_profil(f) for f in chemins.fichiers_profils()}
    tags = [str(x) for x in c.get("etiquettes") or []]
    if d:
        tags += [str(v) for v in (d.get("codes") or {}).values() if v]
    return {"cours": c["nom"], "titre": str(c.get("titre") or c["nom"]),
            "declinaison": d.get("nom") if d else None, "edition": str(ed.get("nom")) if ed else None,
            "libelle": K.libelle(c, d.get("nom") if d else None, str(ed.get("nom")) if ed else None),
            "profil": d.get("ecole") if d and d.get("ecole") in profils else None,
            "tags": list(dict.fromkeys(tags)), "categorie": ((d or {}).get("moodle") or {}).get("categorie") or None,
            "langues": K.langues_declinaison(d) if d else list(c.get("langues") or []),
            "seances": [dict(s) for s in (ed or {}).get("seances") or []], "effectif": (ed or {}).get("effectif"),
            "groupes": list((ed or {}).get("groupes") or []),
            "exports": (ed or {}).get("exports"), "bilans": (ed or {}).get("bilans")}


def seance(r: dict, n: int) -> dict | None:
    return next((s for s in r.get("seances") or [] if int(s.get("n") or 0) == int(n)), None)


def prochaine(r: dict, jour: dt.date | None = None) -> dict | None:
    """Première séance datée d'aujourd'hui ou après (sinon None)."""
    jour = jour or dt.date.today()
    for s in sorted(r.get("seances") or [], key=lambda s: str(s.get("date") or "")):
        try:
            if dt.date.fromisoformat(str(s.get("date"))) >= jour:
                return s
        except ValueError:
            continue
    return None


def decrire_seance(s: dict | None) -> str:
    if not s:
        return ""
    try:
        date = dt.date.fromisoformat(str(s.get("date"))).strftime("%d/%m/%Y")
    except ValueError:
        date = str(s.get("date") or "")
    return " ".join(x for x in (f"séance {s.get('n')}", f"du {date}" if date else "", f"« {s['titre']} »" if s.get("titre") else "") if x)
