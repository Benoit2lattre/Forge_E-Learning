"""Forge E-Learning — ce que le profil d'établissement dit des cours (clés facultatives, lues par AtelierForge).

Chaque école découpe ses formations, nomme ses niveaux, code ses enseignements et nomme ses promotions à sa
façon. Le profil le décrit ; sans ces clés, les mots et les listes génériques ci-dessous s'appliquent et les
codes restent libres.

- ``structure`` : niveaux d'organisation, par défaut ``[parcours, bloc, enseignement]`` ;
- ``vocabulaire`` : mots de l'école pour ``enseignement``, ``bloc`` et ``parcours`` ;
- ``campus``, ``parcours`` : listes de noms, ou de ``{nom, code}`` (code court utilisé dans les gabarits) ;
- ``formations`` : ``{code, nom, niveaux, modalites, rncp, suite}`` ; ``suite`` = code de la formation qui la
  prolonge, pour le calcul de l'année de diplomation (une licence suivie d'un master) ;
- ``codes`` : gabarits des codes, ``{longueurs: {bloc: 3, cours: 2}, bloc: "{bloc}-{niveau}",
  enseignement: "{bloc}-{niveau}-{cours}"}`` ;
- ``promo`` : gabarit du nom de promotion, ``"P{diplomation}"`` ou ``"X{entree:aa}"``.

Champs des gabarits : ``{niveau}`` (L3), ``{formation}`` (L), ``{annee}`` (3), ``{modalite}``, ``{campus}``,
``{parcours}`` (codes courts), ``{bloc}`` et ``{cours}`` (abrégés saisis) ; pour la promo ``{diplomation}`` et
``{entree}`` (quatre chiffres, ou deux avec ``:aa``).
"""
from __future__ import annotations

import re

STRUCTURE = ["parcours", "bloc", "enseignement"]
VOCABULAIRE = {"enseignement": "Enseignement", "bloc": "Bloc", "parcours": "Parcours"}
MODALITES_INGENIEUR = ["FISE", "FISA", "FISEA", "FC"]
FORMATIONS = [
    {"code": "L", "nom": "Licence", "niveaux": ["L1", "L2", "L3"]},
    {"code": "M", "nom": "Master", "niveaux": ["M1", "M2"]},
    {"code": "B", "nom": "Bachelor", "niveaux": ["B1", "B2", "B3"]},
    {"code": "I", "nom": "Ingénieur", "niveaux": ["I1", "I2", "I3"], "modalites": MODALITES_INGENIEUR},
]
CHAMP = re.compile(r"\{(\w+)(?::(aa))?\}")


def _codes_courts(v) -> list[dict]:
    """Liste de noms ou de ``{nom, code}`` → ``[{nom, code}]`` (sans code : le nom)."""
    out = []
    for x in v or []:
        if isinstance(x, dict) and str(x.get("nom") or "").strip():
            out.append({"nom": str(x["nom"]), "code": str(x.get("code") or x["nom"])})
        elif str(x or "").strip() and not isinstance(x, dict):
            out.append({"nom": str(x), "code": str(x)})
    return out


def _formations(v) -> list[dict]:
    out = []
    for f in v or []:
        if not isinstance(f, dict) or not str(f.get("code") or "").strip():
            continue
        code = str(f["code"])
        niveaux = [str(n) for n in f.get("niveaux") or []] or [f"{code}{i}" for i in (1, 2, 3)]
        out.append({"code": code, "nom": str(f.get("nom") or code), "niveaux": niveaux,
                    "modalites": [str(m) for m in f.get("modalites") or []],
                    **({"rncp": str(f["rncp"])} if f.get("rncp") else {}),
                    **({"suite": str(f["suite"])} if f.get("suite") else {})})
    return out


def lire(d: dict | None) -> dict:
    """Profil (dict lu du YAML) → réglages des cours, complétés par les valeurs génériques."""
    d = d if isinstance(d, dict) else {}
    voc = d.get("vocabulaire") if isinstance(d.get("vocabulaire"), dict) else {}
    codes = d.get("codes") if isinstance(d.get("codes"), dict) else {}
    lg = codes.get("longueurs") if isinstance(codes.get("longueurs"), dict) else {}
    return {
        "structure": [str(x) for x in d.get("structure") or []] or STRUCTURE,
        "vocabulaire": {k: str(voc.get(k) or v) for k, v in VOCABULAIRE.items()},
        "campus": _codes_courts(d.get("campus")),
        "parcours": _codes_courts(d.get("parcours")),
        "formations": _formations(d.get("formations")) or [dict(f) for f in FORMATIONS],
        "codes": {k: str(codes[k]) for k in ("bloc", "enseignement") if codes.get(k)}
                 | ({"longueurs": {k: int(v) for k, v in lg.items() if str(v).isdigit()}} if lg else {}),
        "promo": str(d["promo"]) if d.get("promo") else None,
    }


def generique() -> dict:
    return lire({})


def formation_du_niveau(reglages: dict, niveau: str, formation: str | None = None) -> dict | None:
    fs = reglages.get("formations") or []
    return next((f for f in fs if f["code"] == formation and niveau in f["niveaux"]), None) or \
        next((f for f in fs if niveau in f["niveaux"]), None)


def appliquer(gabarit: str, champs: dict) -> str:
    """Remplit un gabarit ; un champ vide laisse ``?`` (code incomplet, visible)."""
    def rempl(m):
        v = str(champs.get(m.group(1)) or "")
        return (v[-2:] if m.group(2) and v else v) or "?"
    return CHAMP.sub(rempl, gabarit)


def motif(gabarit: str, longueurs: dict | None = None) -> re.Pattern:
    """Expression régulière d'un code conforme au gabarit (pour ``cours.py verifier``)."""
    longueurs = longueurs or {}
    morceaux, fin = [], 0
    for m in CHAMP.finditer(gabarit):
        morceaux.append(re.escape(gabarit[fin:m.start()]))
        n = 2 if m.group(2) else longueurs.get(m.group(1))
        morceaux.append(rf"[A-Za-z0-9]{{{n}}}" if n else r"[A-Za-z0-9]+")
        fin = m.end()
    morceaux.append(re.escape(gabarit[fin:]))
    return re.compile("^" + "".join(morceaux) + "$")


def champs_declinaison(reglages: dict, d: dict) -> dict:
    """Champs des gabarits d'une déclinaison (codes courts du campus et du parcours, abrégés saisis)."""
    niveau = str(d.get("niveau") or "")
    f = formation_du_niveau(reglages, niveau, d.get("formation"))
    m = re.match(r"^(\D*)(\d+)$", niveau)
    campus = [c for c in d.get("campus") or [] if c]
    court = lambda liste, nom: next((x["code"] for x in reglages.get(liste) or [] if x["nom"] == nom), nom)
    ab = d.get("abreges") or {}
    return {"niveau": niveau, "formation": d.get("formation") or (f or {}).get("code") or (m.group(1) if m else ""),
            "annee": m.group(2) if m else "", "modalite": d.get("modalite") or "",
            "campus": court("campus", campus[0]) if len(campus) == 1 else "",
            "parcours": court("parcours", d.get("parcours") or "") if d.get("parcours") else "",
            "bloc": ab.get("bloc") or "", "cours": ab.get("cours") or ""}


def annees_promo(reglages: dict, niveau: str, annee_edition: int, formation: str | None = None) -> dict | None:
    """Années d'entrée et de diplomation d'une édition (année scolaire qui commence en ``annee_edition``),
    d'après la place du niveau dans sa formation et les formations qui la prolongent (``suite``)."""
    f = formation_du_niveau(reglages, niveau, formation)
    if not f:
        return None
    i = f["niveaux"].index(niveau)
    reste, vues, suite = len(f["niveaux"]) - i, {f["code"]}, f.get("suite")
    while suite and suite not in vues:
        vues.add(suite)
        g = next((x for x in reglages.get("formations") or [] if x["code"] == suite), None)
        if not g:
            break
        reste += len(g["niveaux"])
        suite = g.get("suite")
    return {"entree": annee_edition - i, "diplomation": annee_edition + reste}


def pour_ecole(nom: str | None) -> dict | None:
    """Réglages des cours du profil d'établissement ``nom`` (None si aucun profil ne porte ce nom)."""
    if not nom:
        return None
    import yaml
    import chemins
    for f in chemins.fichiers_profils():
        if chemins.nom_profil(f) == nom:
            try:
                return lire(yaml.safe_load(f.read_text(encoding="utf-8")) or {})
            except Exception:
                return lire({})
    return None


def remarques_codes(d: dict) -> list[str]:
    """Codes d'une déclinaison qui ne suivent pas les gabarits du profil de son école."""
    reg = pour_ecole(d.get("ecole"))
    if not reg:
        return []
    gab, out = reg.get("codes") or {}, []
    for k in ("bloc", "enseignement"):
        v = str((d.get("codes") or {}).get(k) or "")
        if v and gab.get(k) and not motif(gab[k], gab.get("longueurs")).match(v):
            out.append(f"code {k} « {v} » ({d.get('nom')}) : gabarit de {d.get('ecole')} {gab[k]}")
    return out
