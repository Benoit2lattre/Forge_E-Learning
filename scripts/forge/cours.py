#!/usr/bin/env python3
"""Cours, déclinaisons et éditions de Forge (fichier ``cours.yaml``, format ``forge-cours/1``).

Un **cours** décrit un contenu stable (description, objectifs, compétences, documents, sources) ; une
**déclinaison** est ce cours dans une école (campus, parcours, niveau, codes, langue, Moodle) ; une **édition** est
une année de cette déclinaison (promo, groupes et leur campus, séances datées). Un cours désigne ses dossiers et
fichiers (sources) sans les déplacer ; un cours nouveau reçoit une arborescence standard sous ``data/cours/<nom>/``.

L'atelier s'en sert pour son sélecteur « Cours » et pour trier ses listes ; la ligne de commande donne la même vue :

    python scripts/forge/cours.py liste
    python scripts/forge/cours.py montrer mef
    python scripts/forge/cours.py verifier [mef]
    python scripts/forge/cours.py proposer mef          # sources trouvées dans data/ pour un nom court
"""
from __future__ import annotations

import argparse
import copy
import fnmatch
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "commun"))
import chemins                    # noqa: E402
import profil_cours               # noqa: E402

FORMAT = "forge-cours/1"
FICHIER = "cours.yaml"
RACINES = (chemins.DATA / "cours", chemins.DONNEES / "cours")      # privés, puis démonstration publique
TYPES = {"questions": "Classeurs de questions", "exercices": "Fiches d'exercices", "capsules": "Capsules",
         "diaporamas": "Diaporamas", "exports": "Exports Moodle et bilans"}
DOCUMENTS = {"syllabus": "Syllabus", "plan": "Plan de cours", "fiche_competences": "Fiche de compétences",
             "autre": "Autre document"}
STANDARD = {"documents": None, "diaporamas": "diaporamas", "questions": "questions", "exercices": "exercices",
            "capsules": "capsules"}                              # sous-dossiers d'un cours nouveau → type de source
NOM = re.compile(r"[a-z0-9][a-z0-9_-]{0,23}")
LIMITE_CHEMIN = 200
EN_TETE = ("# Cours Forge (format forge-cours/1) : écrit par l'Atelier Forge ; modifiable à la main.\n"
           "# Chemins relatifs à la racine du dépôt. Mode d'emploi : outils/atelier/README.md (Cours).\n")


# --------------------------------------------------------------------------------------------- lecture, écriture
def _yaml():
    import yaml
    return yaml


def rel(p: Path) -> str:
    try:
        return Path(p).resolve().relative_to(chemins.RACINE).as_posix()
    except ValueError:
        return str(Path(p).resolve())


def absolu(chemin: str) -> Path:
    p = Path(chemin)
    return p if p.is_absolute() else chemins.RACINE / p


def fichiers() -> list[Path]:
    """Fichiers ``cours.yaml`` de data/cours puis de donnees/cours (un nom déjà vu dans data/ masque la démo)."""
    out, vus = [], set()
    for base in RACINES:
        if not base.is_dir():
            continue
        for d in sorted(base.iterdir(), key=lambda x: x.name):
            f = d / FICHIER
            if f.is_file() and d.name not in vus:
                vus.add(d.name)
                out.append(f)
    return out


# Codes d'une déclinaison : noms génériques (le profil d'établissement donne les mots de l'école, clé
# ``vocabulaire``) ; les anciens noms sont lus et réécrits sous les nouveaux.
CODES = ("enseignement", "bloc")
ANCIENS_CODES = {"module": "enseignement", "ue": "bloc"}


def lire(f: Path) -> dict:
    c = _yaml().safe_load(f.read_text(encoding="utf-8")) or {}
    if not isinstance(c, dict):
        raise ValueError(f"{rel(f)} : ce n'est pas un cours")
    c.setdefault("nom", f.parent.name)
    c["_fichier"] = f
    for d in c.get("declinaisons") or []:            # anciens noms des codes : module → enseignement, ue → bloc
        cs = d.get("codes")
        if isinstance(cs, dict):
            d["codes"] = {ANCIENS_CODES.get(k, k): v for k, v in cs.items()}
    if c.get("active"):                              # ancien champ : une seule édition en cours pour tout le cours
        decl, _, ed = str(c.pop("active")).partition("/")
        for d in c.get("declinaisons") or []:
            if d.get("nom") == decl and not d.get("en_cours"):
                d["en_cours"] = ed
    return c


def ecrire(c: dict) -> Path:
    f = c["_fichier"]
    propre = {k: v for k, v in c.items() if not k.startswith("_")}
    propre["format"] = FORMAT
    ordre = ["format", "nom", "titre", "domaine", "langues", "description", "objectifs", "competences", "inclut",
             "derive_de", "documents", "sources", "erreurs", "etiquettes", "declinaisons", "comparaisons"]
    propre = {k: propre[k] for k in ordre if k in propre} | {k: v for k, v in propre.items() if k not in ordre}
    f.parent.mkdir(parents=True, exist_ok=True)
    texte = _yaml().safe_dump(propre, allow_unicode=True, sort_keys=False, width=110, default_flow_style=False)
    f.write_text(EN_TETE + texte, encoding="utf-8", newline="\n")
    return f


def tous() -> dict[str, dict]:
    out = {}
    for f in fichiers():
        try:
            c = lire(f)
        except Exception as e:                       # un fichier illisible n'empêche pas les autres
            c = {"nom": f.parent.name, "titre": f.parent.name, "_fichier": f, "_erreur": str(e)}
        out[c["nom"]] = c
    return out


def trouver(nom: str) -> dict:
    c = tous().get(nom)
    if not c:
        raise ValueError(f"cours inconnu : {nom}")
    if c.get("_erreur"):
        raise ValueError(f"cours illisible : {c['_erreur']}")
    return c


def dossier_cours(c: dict) -> Path:
    return c["_fichier"].parent


# --------------------------------------------------------------------------------------------- déclinaisons, éditions
def declinaison(c: dict, nom: str) -> dict:
    for d in c.get("declinaisons") or []:
        if d.get("nom") == nom:
            return d
    raise ValueError(f"déclinaison inconnue : {nom}")


def edition(c: dict, decl: str, ed: str) -> dict:
    for e in declinaison(c, decl).get("editions") or []:
        if str(e.get("nom")) == str(ed):
            return e
    raise ValueError(f"édition inconnue : {decl}/{ed}")


def libelle(c: dict, decl: str | None = None, ed: str | None = None) -> str:
    t = str(c.get("titre") or c.get("nom"))
    if decl:
        d = declinaison(c, decl)
        t += " — " + " ".join(str(x) for x in (d.get("ecole"), d.get("parcours")) if x) if (d.get("ecole") or d.get("parcours")) else " — " + decl
    if ed:
        t += " — " + str(ed)
    return t


def choix_possibles() -> list[dict]:
    """Ce que propose le sélecteur : chaque cours, et chaque édition de chacune de ses déclinaisons."""
    out = []
    for c in tous().values():
        if c.get("_erreur"):
            out.append({"cours": c["nom"], "libelle": f"{c['nom']} (illisible)", "erreur": c["_erreur"]})
            continue
        out.append({"cours": c["nom"], "libelle": libelle(c)})
        for d in c.get("declinaisons") or []:
            for e in d.get("editions") or []:
                out.append({"cours": c["nom"], "declinaison": d.get("nom"), "edition": str(e.get("nom")),
                            "libelle": libelle(c, d.get("nom"), str(e.get("nom")))})
    return out


def nom_valide(nom: str, quoi: str = "nom court") -> str:
    nom = (nom or "").strip().lower()
    if not NOM.fullmatch(nom):
        raise ValueError(f"{quoi} : 1 à 24 caractères, lettres minuscules sans accent, chiffres, - et _")
    return nom


def texte_valide(v, maxi: int = 200, lignes: bool = False) -> str:
    v = str(v or "").strip()
    if len(v) > maxi or "\0" in v or (not lignes and any(x in v for x in "\r\n")):
        raise ValueError("texte trop long ou mal formé")
    return v


# --------------------------------------------------------------------------------------------- appartenance
def motifs(c: dict, cours_par_nom: dict | None = None, deja: set | None = None) -> list[str]:
    """Chemins et motifs (``*``) désignés par un cours, ses déclinaisons et les cours qu'il inclut, plus son dossier."""
    cours_par_nom = cours_par_nom if cours_par_nom is not None else tous()
    deja = deja or set()
    deja.add(c.get("nom"))
    out = [rel(dossier_cours(c))]
    for liste in (c.get("sources") or {}).values():
        out += [str(x) for x in liste or []]
    for d in c.get("declinaisons") or []:
        for liste in (d.get("sources") or {}).values():
            out += [str(x) for x in liste or []]
        for e in d.get("editions") or []:
            out += [str(e[k]) for k in ("exports", "bilans") if e.get(k)]
    for n in c.get("inclut") or []:                   # C11 : les sources d'un cours inclus s'ajoutent, sans copie
        if n in cours_par_nom and n not in deja:
            out += motifs(cours_par_nom[n], cours_par_nom, deja)
    return out


def _forme(chemin) -> str:
    p = Path(chemin)
    p = p if p.is_absolute() else chemins.RACINE / p
    try:
        p = p.resolve()
    except OSError:
        pass
    return p.as_posix().lower() if sys.platform == "win32" else p.as_posix()


def correspond(chemin, motif: str) -> bool:
    """Vrai si ``chemin`` est le motif, est dedans, ou s'il correspond au motif (``*`` sur un nom)."""
    c, m = _forme(chemin), _forme(motif) if not any(x in motif for x in "*?[") else None
    if m is not None:
        return c == m or c.startswith(m.rstrip("/") + "/")
    mp = (Path(motif) if Path(motif).is_absolute() else chemins.RACINE / motif).as_posix()
    mp = mp.lower() if sys.platform == "win32" else mp
    if fnmatch.fnmatchcase(c, mp):
        return True
    return any(fnmatch.fnmatchcase(p, mp) for p in _ancetres(c))


def _ancetres(c: str):
    parts = c.split("/")
    for i in range(len(parts) - 1, 1, -1):
        yield "/".join(parts[:i])


class Index:
    """Appartenance des objets aux cours, calculée une fois par requête."""

    def __init__(self):
        self.cours = {n: c for n, c in tous().items() if not c.get("_erreur")}
        self.motifs = {n: motifs(c, self.cours) for n, c in self.cours.items()}

    def de(self, chemin) -> list[str]:
        return [n for n, ms in self.motifs.items() if any(correspond(chemin, m) for m in ms)]

    def dossiers(self, type_: str) -> list[Path]:
        """Dossiers où chercher les objets d'un type (sources désignées et dossiers standard des cours)."""
        out = []
        for c in self.cours.values():
            dc = dossier_cours(c)
            if type_ in STANDARD.values() and (dc / type_).is_dir():
                out.append(dc / type_)
            if type_ == "exports":
                out.append(dc)
            listes = [(c.get("sources") or {}).get(type_)] + [(d.get("sources") or {}).get(type_)
                                                              for d in c.get("declinaisons") or []]
            for liste in listes:
                for m in liste or []:
                    base = str(m).split("*")[0] if "*" in str(m) else str(m)
                    p = absolu(base.rstrip("/")) if base else None
                    if p and not p.exists() and "*" in str(m):
                        p = p.parent
                    if p and p.is_dir():
                        out.append(p)
        vus, uniques = set(), []
        for p in out:
            r = p.resolve()
            if r not in vus:
                vus.add(r)
                uniques.append(p)
        return uniques


def filtrer(objets: list[dict], cle: str, choix: dict | None, index: Index | None = None, chemin=None) -> list[dict]:
    """Ajoute à chaque objet la liste ``dans_cours`` de ses cours, puis garde ceux du choix (cours, « sans » ou tous)."""
    index = index or Index()
    choix = choix or {}
    out = []
    for o in objets:
        o["dans_cours"] = index.de(chemin(o) if chemin else o.get(cle) or "")
        if choix.get("cours") == "_sans":
            if not o["dans_cours"]:
                out.append(o)
        elif choix.get("cours"):
            if choix["cours"] in o["dans_cours"]:
                out.append(o)
        else:
            out.append(o)
    return out


# --------------------------------------------------------------------------------------------- création
def proposer(nom: str) -> list[dict]:
    """Sources de ``data/`` dont le nom contient le nom court (dossiers, classeurs, fiches, capsules, diaporamas)."""
    cle = nom.lower()
    motif = re.compile(rf"(^|[^a-z0-9]){re.escape(cle)}([^a-z]|$)", re.IGNORECASE)
    out, vus = [], set()

    def ajouter(type_, p: Path):
        r = rel(p)
        if r not in vus:
            vus.add(r)
            out.append({"type": type_, "chemin": r, "libelle": p.name + ("/" if p.is_dir() else "")})

    bases = {"quizforge": "questions", "exoforge": "exercices", "capsuleforge": "capsules", "diagforge": "exports"}
    for outil, type_ in bases.items():
        base = chemins.DATA / outil
        if not base.is_dir():
            continue
        for p in sorted(base.rglob("*")):
            relp = p.relative_to(base)
            if len(relp.parts) > 3 or any(x.startswith(("_", ".")) or x.endswith("_QuizForge") for x in relp.parts):
                continue
            if not motif.search(p.stem if p.is_file() else p.name):
                continue
            if any(rel(p).startswith(v + "/") for v in vus):
                continue
            if p.is_dir():
                ajouter(type_ if not (outil == "capsuleforge" and relp.parts[0] == "PPTX") else "diaporamas", p)
            elif p.suffix.lower() == ".pptx":
                ajouter("diaporamas", p)
            elif outil == "quizforge" and p.suffix.lower() == ".xlsx" and not p.name.startswith("~$"):
                ajouter("questions", p)
            elif outil == "exoforge" and p.suffix.lower() in (".yaml", ".yml"):
                ajouter("exercices", p)
    return out


def _modele_syllabus(titre: str) -> str:
    return (f"# {titre} — syllabus\n\n## Description\n\n\n## Objectifs\n\n- \n\n## Prérequis\n\n- \n\n"
            "## Plan\n\n1. \n\n## Évaluation\n\n\n## Bibliographie\n\n- \n")


def _modele_competences(titre: str) -> str:
    return (f"# {titre} — fiche de compétences\n\n| Compétence | Niveau visé | Évaluée par |\n| --- | --- | --- |\n"
            "|  |  |  |\n")


def creer(nom: str, titre: str, domaine: str = "", langues=None, sources: list[dict] | None = None,
          standard: bool = False, base: Path | None = None) -> tuple[dict, list[str]]:
    """Crée un cours : à partir de sources existantes (désignées) et/ou avec l'arborescence standard.

    Renvoie le cours et les avertissements (chemins trop longs).
    """
    nom = nom_valide(nom)
    titre = texte_valide(titre) or nom
    if nom in tous():
        raise ValueError(f"un cours « {nom} » existe déjà")
    d = (base or RACINES[0]) / nom
    c = {"_fichier": d / FICHIER, "format": FORMAT, "nom": nom, "titre": titre, "domaine": texte_valide(domaine),
         "langues": langues or ["fr"], "description": "", "objectifs": [], "competences": [], "inclut": [],
         "derive_de": None, "documents": {}, "sources": {}, "erreurs": None, "etiquettes": [],
         "declinaisons": [], "comparaisons": []}
    for s in sources or []:
        if s.get("type") not in TYPES:
            raise ValueError("type de source inconnu")
        if not absolu(s["chemin"]).exists():
            raise ValueError(f"introuvable : {s['chemin']}")
        c["sources"].setdefault(s["type"], []).append(rel(absolu(s["chemin"])))
    avert = []
    if standard:
        for sous in STANDARD:
            (d / sous).mkdir(parents=True, exist_ok=True)
        (d / "documents" / "syllabus.md").write_text(_modele_syllabus(titre), encoding="utf-8")
        (d / "documents" / "competences.md").write_text(_modele_competences(titre), encoding="utf-8")
        c["documents"] = {"syllabus": rel(d / "documents" / "syllabus.md"),
                          "fiche_competences": rel(d / "documents" / "competences.md")}
        avert += longueur(d / "capsules" / ("x" * 24) / "videos" / ("x" * 40))
    ecrire(c)
    return c, avert


def longueur(p: Path) -> list[str]:
    n = len(str(p.resolve()))
    return [f"chemin de {n} caractères ({rel(p)}) : au-delà de {LIMITE_CHEMIN}, Windows risque de refuser des "
            "fichiers ; prenez des noms plus courts"] if n > LIMITE_CHEMIN else []


def _liste(v, maxi: int) -> list[str]:
    return [texte_valide(x, maxi) for x in (v.split(",") if isinstance(v, str) else v or []) if str(x).strip()]


def langues_declinaison(d: dict) -> list[str]:
    """Langues d'une déclinaison (``langues``, ou l'ancien ``langue`` seul)."""
    return list(d.get("langues") or ([d["langue"]] if d.get("langue") else []))


def _champs_declinaison(c: dict, d: dict) -> dict:
    langues = _liste(d.get("langues") if d.get("langues") is not None else d.get("langue"), 5)
    return {"ecole": texte_valide(d.get("ecole"), 80), "campus": _liste(d.get("campus"), 60),
            "parcours": texte_valide(d.get("parcours"), 80), "niveau": texte_valide(d.get("niveau"), 20),
            "codes": {ANCIENS_CODES.get(k, k): texte_valide(v, 40) for k, v in (d.get("codes") or {}).items()
                      if str(v or "").strip()},
            **{k: texte_valide(d.get(k), 40) for k in ("formation", "modalite", "rncp") if str(d.get(k) or "").strip()},
            **({"variantes": vs} if (vs := _liste(d.get("variantes") if d.get("variantes") is not None
                                                   else d.get("variante"), 40)) else {}),
            **({"abreges": ab} if (ab := {k: texte_valide(v, 12) for k, v in (d.get("abreges") or {}).items()
                                          if k in ("bloc", "cours") and str(v or "").strip()}) else {}),
            "langues": langues or (c.get("langues") or ["fr"])[:1],
            "moodle": {k: texte_valide(v, 120) for k, v in (d.get("moodle") or {}).items()
                       if k in ("cours", "categorie") and str(v or "").strip()}}


def ajouter_declinaison(c: dict, d: dict) -> dict:
    nom = nom_valide(d.get("nom"), "nom de la déclinaison")
    if any(x.get("nom") == nom for x in c.get("declinaisons") or []):
        raise ValueError(f"la déclinaison « {nom} » existe déjà")
    neuve = {"nom": nom, **_champs_declinaison(c, d), "sources": {}, "editions": []}
    c.setdefault("declinaisons", []).append(neuve)
    return neuve


def modifier_declinaison(c: dict, nom: str, d: dict) -> dict:
    """Change école, campus, parcours, niveau, codes et langues ; le nom court (nom des dossiers) reste."""
    x = declinaison(c, nom)
    x.pop("langue", None)
    for k in ("formation", "modalite", "rncp", "abreges", "variante", "variantes"):
        x.pop(k, None)
    x.update(_champs_declinaison(c, d))
    return x


def supprimer_declinaison(c: dict, nom: str):
    x = declinaison(c, nom)
    if x.get("editions"):
        raise ValueError("cette déclinaison a des éditions : elle ne peut pas être supprimée")
    c["declinaisons"].remove(x)


def modifier_edition(c: dict, decl: str, ed: str, e: dict) -> dict:
    x = edition(c, decl, ed)
    _champs_edition(x, e)
    return x


def _champs_edition(x: dict, e: dict):
    if e.get("promo") is not None:
        x["promo"] = texte_valide(e["promo"], 40)
    if e.get("groupes") is not None:
        x["groupes"] = _groupes(e["groupes"])
    if e.get("effectif") is not None:
        v = str(e["effectif"]).strip()
        if v and not v.isdigit():
            raise ValueError("effectif : un nombre d'étudiants")
        if v:
            x["effectif"] = int(v)
        else:
            x.pop("effectif", None)
    if e.get("seances") is not None:
        x["seances"] = _seances(e["seances"])
    if e.get("enseignant") is not None:
        t = texte_valide(e["enseignant"], 80)
        if t:
            x["enseignant"] = t
        else:
            x.pop("enseignant", None)
    if e.get("variantes") is not None or e.get("variante") is not None:   # variantes des capsules ajoutées à celles de la déclinaison
        vs = _liste(e.get("variantes") if e.get("variantes") is not None else e.get("variante"), 40)
        x.pop("variante", None)
        if vs:
            x["variantes"] = vs
        else:
            x.pop("variantes", None)
    if e.get("filigrane") is not None:              # filigrane d'édition sur les images des capsules (habillage)
        if e["filigrane"] in (True, "true", "1", 1):
            x["filigrane"] = True
        else:
            x.pop("filigrane", None)


def _seances(v) -> list[dict]:
    """Séances datées : liste de dicts, ou lignes « n ; date ; titre » (date AAAA-MM-JJ ou JJ/MM/AAAA)."""
    import datetime as dt
    if isinstance(v, list):
        lignes = [f"{s.get('n', '')};{s.get('date', '')};{s.get('titre', '')}" for s in v if isinstance(s, dict)]
    else:
        lignes = str(v).splitlines()
    out = []
    for i, ligne in enumerate(lignes, 1):
        if not ligne.strip():
            continue
        morceaux = [m.strip() for m in ligne.split(";")]
        n, date, titre = (morceaux + ["", ""])[:3]
        if not n.isdigit():
            raise ValueError(f"séance ligne {i} : « n ; date ; titre » (n, numéro de la séance)")
        s = {"n": int(n)}
        if date:
            try:
                j = dt.date.fromisoformat(date) if "-" in date else dt.datetime.strptime(date, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError(f"séance {n} : date « {date} » (AAAA-MM-JJ ou JJ/MM/AAAA)") from None
            s["date"] = j.isoformat()
        if titre:
            s["titre"] = texte_valide(titre, 120)
        out.append(s)
    return sorted(out, key=lambda s: s["n"])


def _groupe(nom, campus=None, langue=None) -> dict:
    g = {"nom": texte_valide(nom, 40)}
    if str(campus or "").strip():
        g["campus"] = texte_valide(campus, 60)
    if str(langue or "").strip():
        g["langue"] = texte_valide(langue, 5).lower()
    return g


def _groupes(g) -> list[dict]:
    """« Aero1:Nord:fr, Aero3:Sud:en » (campus et langue facultatifs) ou une liste de dicts → [{nom, campus, langue}]."""
    if isinstance(g, list):
        return [_groupe(x.get("nom"), x.get("campus"), x.get("langue")) for x in g
                if isinstance(x, dict) and str(x.get("nom") or "").strip()]
    out = []
    for morceau in str(g or "").split(","):
        if morceau.strip():
            n, cp, lg = (morceau.split(":") + ["", ""])[:3]
            out.append(_groupe(n, cp, lg))
    return out


def ajouter_edition(c: dict, decl: str, e: dict) -> dict:
    """Nouvelle édition d'une déclinaison : copie de la précédente (séances décalées d'un an), puis les champs donnés."""
    d = declinaison(c, decl)
    nom = texte_valide(e.get("nom"), 12)
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,11}", nom):
        raise ValueError("nom de l'édition : l'année (2026) ou un nom court sans espace")
    eds = d.setdefault("editions", [])
    if any(str(x.get("nom")) == nom for x in eds):
        raise ValueError(f"l'édition « {nom} » existe déjà")
    neuve = copy.deepcopy(eds[-1]) if eds else {}
    for k in ("exports", "bilans"):
        neuve.pop(k, None)
    if neuve.get("seances") and eds and str(eds[-1].get("nom")).isdigit() and nom.isdigit():
        ecart = int(nom) - int(eds[-1]["nom"])
        for s in neuve["seances"]:
            if s.get("date"):
                s["date"] = _decaler(s["date"], ecart)
    neuve["nom"] = nom
    _champs_edition(neuve, e)
    neuve.setdefault("groupes", [])
    neuve.setdefault("seances", [])
    base = dossier_cours(c) / decl / nom
    neuve["exports"] = rel(base / "exports")
    neuve["bilans"] = rel(base / "bilans")
    (base / "exports").mkdir(parents=True, exist_ok=True)
    (base / "bilans").mkdir(parents=True, exist_ok=True)
    eds.append(neuve)
    d["en_cours"] = nom                              # la nouvelle édition devient celle en cours de sa déclinaison
    return neuve


def en_cours(d: dict) -> str | None:
    """Édition en cours d'une déclinaison (chacune la sienne : deux parcours peuvent avoir lieu en même temps)."""
    eds = [str(e.get("nom")) for e in d.get("editions") or []]
    return str(d["en_cours"]) if d.get("en_cours") and str(d["en_cours"]) in eds else (eds[-1] if eds else None)


def _decaler(date, ans: int):
    import datetime as dt
    try:
        j = date if isinstance(date, dt.date) else dt.date.fromisoformat(str(date))
        try:
            return j.replace(year=j.year + ans)
        except ValueError:                          # 29 février
            return j.replace(year=j.year + ans, day=28)
    except ValueError:
        return date


def ajouter_source(c: dict, type_: str, chemin: str) -> str:
    if type_ not in TYPES:
        raise ValueError("type de source inconnu")
    p = absolu(chemin)
    if not p.exists():
        raise ValueError(f"introuvable : {chemin}")
    r = rel(p)
    liste = c.setdefault("sources", {}).setdefault(type_, [])
    if r not in liste:
        liste.append(r)
    return r


def retirer_source(c: dict, type_: str, chemin: str):
    liste = (c.get("sources") or {}).get(type_) or []
    if chemin not in liste:
        raise ValueError("source absente de ce cours")
    liste.remove(chemin)


# --------------------------------------------------------------------------------------------- vérification
def verifier(c: dict, cours_par_nom: dict | None = None) -> list[str]:
    """Remarques sur un cours : format, sources introuvables, noms en double, choix actif, chemins trop longs."""
    cours_par_nom = cours_par_nom if cours_par_nom is not None else tous()
    r = []
    if c.get("_erreur"):
        return [c["_erreur"]]
    if c.get("format") != FORMAT:
        r.append(f"format « {c.get('format')} » (attendu {FORMAT})")
    if c.get("nom") != dossier_cours(c).name:
        r.append(f"nom « {c.get('nom')} » différent du dossier « {dossier_cours(c).name} »")
    for t, liste in (c.get("sources") or {}).items():
        if t not in TYPES:
            r.append(f"type de source inconnu : {t}")
        for m in liste or []:
            if "*" not in str(m) and not absolu(str(m)).exists():
                r.append(f"source introuvable ({t}) : {m}")
    for k, v in (c.get("documents") or {}).items():
        if v and not absolu(str(v)).exists():
            r.append(f"document introuvable ({k}) : {v}")
    for n in c.get("inclut") or []:
        if n not in cours_par_nom:
            r.append(f"cours inclus inconnu : {n}")
    if c.get("derive_de") and c["derive_de"] not in cours_par_nom:
        r.append(f"« dérivé de » inconnu : {c['derive_de']}")
    noms = [d.get("nom") for d in c.get("declinaisons") or []]
    for n in {x for x in noms if noms.count(x) > 1}:
        r.append(f"déclinaison en double : {n}")
    for d in c.get("declinaisons") or []:
        lgs = langues_declinaison(d)
        for e in d.get("editions") or []:
            for g in e.get("groupes") or []:
                if g.get("langue") and lgs and g["langue"] not in lgs:
                    r.append(f"groupe {g.get('nom')} ({d.get('nom')}/{e.get('nom')}) en {g['langue']}, langue absente de la déclinaison")
        r += profil_cours.remarques_codes(d)
        eds = [str(e.get("nom")) for e in d.get("editions") or []]
        for n in {x for x in eds if eds.count(x) > 1}:
            r.append(f"édition en double : {d.get('nom')}/{n}")
    for d in c.get("declinaisons") or []:
        if d.get("en_cours") and str(d["en_cours"]) not in {str(e.get("nom")) for e in d.get("editions") or []}:
            r.append(f"édition en cours inconnue : {d.get('nom')}/{d['en_cours']}")
    r += longueur(dossier_cours(c) / FICHIER)
    return r


# --------------------------------------------------------------------------------------------- ligne de commande
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="cours", description="Cours, déclinaisons et éditions de Forge.")
    sp = ap.add_subparsers(dest="cmd", required=True)
    sp.add_parser("liste", help="lister les cours et leurs éditions")
    m = sp.add_parser("montrer", help="résumer un cours")
    m.add_argument("nom")
    v = sp.add_parser("verifier", help="vérifier un cours (ou tous)")
    v.add_argument("nom", nargs="?")
    pr = sp.add_parser("proposer", help="sources de data/ qui portent ce nom court")
    pr.add_argument("nom")
    a = ap.parse_args(argv)
    if a.cmd == "liste":
        for x in choix_possibles():
            print(("  " if x.get("edition") else "") + x["libelle"] + (f"  [{x['cours']}/{x['declinaison']}/{x['edition']}]"
                                                                     if x.get("edition") else f"  [{x['cours']}]"))
        return 0
    if a.cmd == "montrer":
        c = trouver(a.nom)
        print(f"{c.get('titre')} [{c['nom']}] — {rel(c['_fichier'])}")
        for t, liste in (c.get("sources") or {}).items():
            print(f"  {TYPES.get(t, t)} : " + ", ".join(liste or []))
        for d in c.get("declinaisons") or []:
            print(f"  déclinaison {d.get('nom')} : {d.get('ecole', '')} {', '.join(d.get('campus') or [])} "
                  f"{d.get('parcours', '')} {d.get('niveau', '')} {'/'.join(langues_declinaison(d))}".rstrip())
            for e in d.get("editions") or []:
                g = ", ".join(x["nom"] + (f" ({', '.join(v for v in (x.get('campus'), x.get('langue')) if v)})"
                                          if x.get("campus") or x.get("langue") else "") for x in e.get("groupes") or [])
                print(f"    édition {e.get('nom')} : promo {e.get('promo', '–')} ; groupes {g or '–'}")
        return 0
    if a.cmd == "verifier":
        cs = tous()
        cibles = [cs[a.nom]] if a.nom else list(cs.values())
        if a.nom and a.nom not in cs:
            raise SystemExit(f"cours inconnu : {a.nom}")
        n = 0
        for c in cibles:
            r = verifier(c, cs)
            n += len(r)
            print(f"{c['nom']} : " + ("✓" if not r else f"{len(r)} remarque(s)"))
            for x in r:
                print("  - " + x)
        return 1 if n else 0
    if a.cmd == "proposer":
        for x in proposer(a.nom):
            print(f"{TYPES[x['type']]:<28} {x['chemin']}")
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())
