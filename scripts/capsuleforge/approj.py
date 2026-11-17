"""CapsuleForge — reprise d'une simulation enregistrée dans ActivePresenter (.approj) en capsule.yaml.

Lecture seule : le projet est d'abord copié dans un dossier temporaire (il peut être ouvert dans
ActivePresenter, avec ses fichiers -wal et -shm), puis lu avec SQLite. Rien n'est écrit à côté du projet.

Ce qui est repris, diapositive par diapositive : l'image de fond, la trajectoire de la souris,
la zone de clic (nom du contrôle compris) et le type d'action. L'audio, les bulles mises en forme et les
objets ajoutés à la main ne sont pas repris (les bulles sont réécrites par assemblage.bulle_auto).

Unités d'ActivePresenter 10 (constatées sur un projet de simulation) : positions et tailles en
millièmes de pixel (2560000 = 2560 px).
Licence : GPL v3.
"""
from __future__ import annotations

import json
import re
import shutil
import sqlite3
import tempfile
from pathlib import Path

import assemblage as A

MILLI = 1000.0


def _json(s):
    if isinstance(s, (bytes, bytearray)):
        s = s.decode("utf-8", "replace")
    return json.loads(re.sub(r":\+(\d)", r":\1", s))      # AP écrit parfois « :+10 »


def _type_depuis_texte(txt: str) -> str:
    t = txt.lower()
    for motif, typ in (("zone de texte", "Edit"), ("bouton", "Button"), ("boîte de liste", "List"),
                       ("liste déroulante", "ComboBox"), ("élément de menu", "MenuItem"), ("menu", "MenuItem"),
                       ("onglet", "TabItem"), ("case", "CheckBox"), ("élément d'arbre", "TreeItem"),
                       ("lien", "Hyperlink")):
        if motif in t:
            return typ
    return ""


def _action_depuis_texte(txt: str) -> str:
    t = txt.lower()
    if "double" in t:
        return "double_clic"
    if "droit" in t:
        return "clic_droit"
    return "clic"


def importer(approj: Path, sortie: Path, titre: str | None = None) -> dict:
    """Lit un projet ActivePresenter (.approj) et renvoie la capsule correspondante (dictionnaire).

    Les images de fond sont écrites dans ``<sortie>/images/`` ; le titre par défaut est le nom du projet.
    Le projet lui-même n'est pas modifié (lecture d'une copie temporaire).
    """
    approj = Path(approj)
    sortie = Path(sortie)
    (sortie / "images").mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        copie = Path(tmp) / "projet.db"
        shutil.copy2(approj, copie)
        for suffixe in ("-wal", "-shm"):
            f = approj.with_name(approj.name + suffixe)
            if f.is_file() and f.stat().st_size:
                shutil.copy2(f, Path(tmp) / ("projet.db" + suffixe))
        con = sqlite3.connect(copie)
        try:
            cap = _lire(con, sortie, titre or approj.stem, approj.name)
        finally:
            con.close()
    return cap


def _lire(con, sortie: Path, titre: str, projet: str = "") -> dict:
    """Construit la capsule à partir de la base SQLite ouverte (une étape, un pas par diapositive)."""
    lignes = con.execute("select `index`, name, contents from slides order by `index`").fetchall()
    ressources = {rid: (hint, data) for rid, hint, data in con.execute("select id, hint, data from resources")}
    largeur = hauteur = None
    pas = []
    avert = []
    for idx, nom, contenu in lignes:
        d = _json(contenu)
        rv = (d.get("resp_values") or [{}])[0]
        largeur, hauteur = largeur or rv.get("w"), hauteur or rv.get("h")
        ecran = {"largeur": largeur, "hauteur": hauteur}
        pid = f"p{idx + 1:03d}"

        # image de fond
        image = None
        m = re.search(r'"imageid"\s*:\s*(\d+)', json.dumps(d.get("background_image") or {}))
        if m and int(m.group(1)) in ressources and ressources[int(m.group(1))][1]:
            data = ressources[int(m.group(1))][1]
            if bytes(data[:8]) == b"\x89PNG\r\n\x1a\n":
                image = f"images/{pid}.png"
                (sortie / image).write_bytes(bytes(data))
        if image is None:
            avert.append(f"diapositive {idx + 1} : pas d'image de fond lisible")

        # trajectoire : durées cumulées (ms), positions en millièmes de pixel
        traj, t = [], 0
        for c in (d.get("cursorpath") or {}).get("cursors", []):
            v = (c.get("responsive_values") or [{}])[0]
            traj.append([v.get("position_x", 0) / MILLI, v.get("position_y", 0) / MILLI, t])
            t += int(c.get("duration", 0))

        # zone de clic (contrôle kind 11) et texte de la légende (contrôle de type 0 avec texte)
        zone, legende = None, ""
        for ct in d.get("controls", []):
            st = (ct.get("states") or [{}])[0]
            if ct.get("kind") == 11 and zone is None:
                r = (st.get("respvalues") or [{}])[0]
                zone = (ct.get("itext") or "", [r.get("x", 0) / MILLI, r.get("y", 0) / MILLI,
                                                 r.get("w", 0) / MILLI, r.get("h", 0) / MILLI])
            elif ct.get("type") == 0 and st.get("htmltext") and not legende:
                legende = re.sub(r"<[^>]+>", "", st["htmltext"]).strip()
        legende = legende or re.sub(r"<[^>]+>", "", nom or "")

        point = traj[-1][:2] if traj else ([zone[1][0] + zone[1][2] / 2, zone[1][1] + zone[1][3] / 2] if zone else [0, 0])
        cible = {"origine": "aucune"}
        if zone:
            cible = {"nom": zone[0], "type": _type_depuis_texte(legende),
                     "cadre": [int(round(v)) for v in zone[1]],
                     "origine": "accessibilite" if zone[0] else "aucune"}
        evt = {"e": "pas", "id": pid, "action": _action_depuis_texte(legende), "image": image,
               "point": [int(round(v)) for v in point], "trajet": traj, "cible": cible,
               "t": None}
        p = A.construire_pas(evt, ecran, None)
        p["duree_ms"] = int(d.get("duration", 0))
        pas.append(p)

    cap = {
        "format": A.FORMAT,
        "titre": titre,
        "langue": "fr",
        "ecran": {"largeur": largeur, "hauteur": hauteur},
        "source": {"outil": "capsuleforge approj", "projet": projet},
        "reglages": {"mode": "les_deux", "essais": 3},
        "masques": [],
        "etapes": [{"titre": "Étape 1", "narration": "", "arret": True, "pas": pas}],
    }
    if avert:
        cap["_avertissements_import"] = avert
    return cap
