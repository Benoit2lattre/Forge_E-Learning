"""CapsuleForge — variantes d'une capsule : ce qui ne vaut que pour certains publics (une école, un client).

La capsule source reste unique et nue ; une **variante** (``variantes`` du chapitre, choisie par la déclinaison du
cours ou ``construire --variante``) ajoute, retire ou remplace des morceaux à la construction :

- partie, section, pas ou phrase avec ``variantes: [psa]`` : seulement pour ces variantes (absent de la capsule nue) ;
  avec ``sauf: [psa]`` : retiré pour ces variantes ;
- phrase avec ``pour: {psa: "…"}`` : autre texte pour cette variante (sous-titres, texte de la section) ; avec
  ``audio_pour: {psa: audio/….wav}``, le son de la phrase est remplacé aussi ;
- pas avec ``fond_pour: {psa: images/….png}`` : autre image ;
- masque ``{zone: [x, y, l, h], variantes: […]}`` ou ``{zone: …, sauf: […]}`` : zone floutée selon la variante.

Une phrase retirée coupe son extrait de narration (du début de la phrase au début de la suivante) dans le son du
pas et dans les voix de synthèse des autres langues ; les phrases et objets qui suivent sont recalés. Un pas vidéo
garde son film : seuls les sous-titres changent (signalé).
"""
from __future__ import annotations

import copy
import sys
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))


def retenu(e: dict, variante: str | None) -> bool:
    """Un élément (partie, section, pas, phrase, masque) est-il gardé pour cette variante (None : capsule nue) ?"""
    if not isinstance(e, dict):
        return True
    seules = e.get("variantes")
    if seules and (variante not in seules):
        return False
    if variante and variante in (e.get("sauf") or []):
        return False
    return True


def masques(liste: list, variante: str | None) -> list:
    """Masques retenus, sous la forme ``[x, y, l, h]``."""
    out = []
    for m in liste or []:
        if isinstance(m, dict):
            if retenu(m, variante) and m.get("zone"):
                out.append(list(m["zone"]))
        else:
            out.append(m)
    return out


def _signal(chemin: Path):
    """Son mono en flottants et sa fréquence (WAV lu directement, sinon PyAV)."""
    import numpy as np
    import wave
    if chemin.suffix.lower() == ".wav":
        try:
            with wave.open(str(chemin)) as w:
                c, l, f = w.getnchannels(), w.getsampwidth(), w.getframerate()
                brut = w.readframes(w.getnframes())
            if l == 2:
                x = np.frombuffer(brut, dtype="<i2").astype("float32") / 32768.0
                return (x.reshape(-1, c).mean(axis=1) if c > 1 else x), f
        except wave.Error:
            pass
    import av
    morceaux, freq = [], 44100
    with av.open(str(chemin)) as ct:
        flux = ct.streams.audio[0]
        freq = flux.rate or 44100
        conv = av.AudioResampler(format="s16", layout="mono", rate=freq)
        for trame in ct.decode(flux):
            for t in conv.resample(trame) or []:
                morceaux.append(t.to_ndarray().reshape(-1))
    return np.concatenate(morceaux).astype("float32") / 32768.0, freq


def _monter(src: Path, coupes: list, inserts: dict, dst: Path) -> None:
    """Écrit ``dst`` : ``src`` privé des intervalles ``coupes`` [(a, b)], avec ``inserts`` {a: fichier} posés à la
    place de la coupe qui commence en a."""
    import numpy as np
    import sons
    x, f = _signal(src)
    morceaux, t = [], 0.0
    for a, b in sorted(coupes):
        morceaux.append(x[int(t * f):int(a * f)])
        if a in inserts:
            y, fy = _signal(inserts[a])
            morceaux.append(sons.reechantillonner(y, fy, f))
        t = b
    morceaux.append(x[int(t * f):])
    sons.ecrire_wav(dst, np.concatenate(morceaux) if morceaux else x, f)


def _decaler(t: float, coupes: list) -> float:
    """Instant ``t`` après les coupes ``[(a, b, nouvelle_longueur)]`` (une coupe peut être remplacée par un insert)."""
    d = 0.0
    for a, b, n in coupes:
        if t >= b:
            d += (b - a) - n
        elif t > a:
            return max(a - d, 0.0) + min(t - a, n)
    return t - d


def _duree(chemin: Path) -> float:
    x, f = _signal(chemin)
    return len(x) / f


def appliquer(chap: dict, variante: str | None, dossier: Path, travail: Path, journal=print) -> dict:
    """Copie du chapitre pour une variante (None : capsule nue), sons recoupés écrits dans ``travail``."""
    c = copy.deepcopy(chap)
    c["masques"] = masques(c.get("masques"), variante)
    n_phr = n_pas = 0
    parties = []
    for p in c.get("parties") or []:
        if not retenu(p, variante):
            continue
        sections = []
        for s in p.get("sections") or []:
            if not retenu(s, variante):
                continue
            pas = []
            for q in s.get("pas") or []:
                if not retenu(q, variante):
                    n_pas += 1
                    continue
                if variante and (q.get("fond_pour") or {}).get(variante):
                    q["fond"] = q["fond_pour"][variante]
                n_phr += _phrases(q, variante, dossier, travail, journal)
                pas.append(q)
            s["pas"] = pas
            sections.append(s)
        p["sections"] = sections
        parties.append(p)
    c["parties"] = parties
    nom = f"variante {variante}" if variante else "capsule nue"
    if n_pas or n_phr:
        journal(f"  {nom} : {n_pas} pas et {n_phr} phrase(s) retirés ou remplacés")
    return c


def _phrases(q: dict, variante: str | None, dossier: Path, travail: Path, journal) -> int:
    """Retire ou remplace les phrases d'un pas ; recoupe son son et ses voix ; renvoie le nombre de phrases touchées."""
    phr = q.get("phrases") or []
    if not phr:
        return 0
    garder, coupes, inserts, touchees = [], [], {}, 0
    horo = [ph for ph in phr if ph.get("debut_s") is not None]
    for i, ph in enumerate(phr):
        ok = retenu(ph, variante)
        nouveau = (ph.get("pour") or {}).get(variante) if variante else None
        son_neuf = (ph.get("audio_pour") or {}).get(variante) if variante else None
        if ok and nouveau is None:
            garder.append(ph)
            continue
        touchees += 1
        if ph.get("debut_s") is None:                  # phrase sans horodatage : texte seulement
            if ok:
                garder.append(dict(ph, texte=nouveau))
            continue
        k = horo.index(ph)
        a = float(ph["debut_s"])
        b = float(horo[k + 1]["debut_s"]) if k + 1 < len(horo) else float(ph.get("fin_s") or a)
        if not ok:                                     # phrase retirée : son coupé
            coupes.append((a, b, None, i))
        elif son_neuf and (dossier / son_neuf).is_file():   # phrase remplacée avec son propre son
            coupes.append((a, b, dossier / son_neuf, i))
            garder.append(dict(ph, texte=nouveau))
        else:                                          # phrase remplacée, sous-titres seulement
            garder.append(dict(ph, texte=nouveau))
            journal(f"  pas {q.get('id')} : phrase remplacée dans les sous-titres seulement (le son dit encore "
                    f"l'ancienne ; « audio_pour » ou voix de synthèse)")
    if not coupes:
        q["phrases"] = garder
        return touchees
    if q.get("video"):
        journal(f"  pas {q.get('id')} (vidéo) : film gardé tel quel, seuls les sous-titres changent")
        q["phrases"] = garder
        return touchees
    longueurs = {i: (_duree(f) if f else 0.0) for a, b, f, i in coupes}
    cc = [(a, b, longueurs[i]) for a, b, f, i in coupes]
    if q.get("audio") and (dossier / q["audio"]).is_file():
        src = dossier / q["audio"]
        dst = travail / f"{src.stem}_{q.get('id')}_{variante or 'nue'}.wav"
        _monter(src, [(a, b) for a, b, _, _ in coupes], {a: f for a, b, f, _ in coupes if f}, dst)
        q["audio"] = str(dst)
    for ph in garder:
        if ph.get("debut_s") is not None:
            ph["debut_s"] = round(_decaler(float(ph["debut_s"]), cc), 2)
            ph["fin_s"] = round(_decaler(float(ph.get("fin_s") or ph["debut_s"]), cc), 2)
    for o in q.get("objets") or []:
        if o.get("debut_s") is not None:
            d0 = float(o["debut_s"])
            o["debut_s"] = round(_decaler(d0, cc), 2)
            if o.get("duree_s") is not None:
                o["duree_s"] = round(max(0.3, _decaler(d0 + float(o["duree_s"]), cc) - o["debut_s"]), 2)
    if q.get("duree_s"):
        q["duree_s"] = round(_decaler(float(q["duree_s"]), cc), 2)
    retirees = {i for _, _, f, i in coupes if not f}
    for l, v in (q.get("voix") or {}).items():          # voix de synthèse : même phrase coupée, à ses propres temps
        tv = v.get("phrases") or []
        if not v.get("audio") or len(tv) != len(horo) or not (dossier / v["audio"]).is_file():
            continue
        cv = []
        for k, ph in enumerate(horo):
            if phr.index(ph) in retirees:
                a = float(tv[k][0])
                b = float(tv[k + 1][0]) if k + 1 < len(tv) else float(tv[k][1])
                cv.append((a, b))
        if not cv:
            continue
        dst = travail / f"{Path(v['audio']).stem}_{q.get('id')}_{variante or 'nue'}.wav"
        _monter(dossier / v["audio"], cv, {}, dst)
        ccv = [(a, b, 0.0) for a, b in cv]
        v["audio"] = str(dst)
        v["phrases"] = [[round(_decaler(float(t[0]), ccv), 2), round(_decaler(float(t[1]), ccv), 2)]
                        for k, t in enumerate(tv) if phr.index(horo[k]) not in retirees]
        v["duree_s"] = round(_decaler(float(v.get("duree_s") or 0), ccv), 2)
    q["phrases"] = garder
    return touchees


def _textes(x) -> list[str]:
    if isinstance(x, dict):
        return [str(v) for v in x.values() if v]
    return [str(x)] if x else []


def noms_a_eviter(chap: dict, fichier: Path | None = None) -> list[str]:
    """Noms d'établissements trouvés dans la capsule nue (liste privée ``data/capsuleforge/noms_a_eviter.txt`` :
    un nom par ligne, ``#`` pour un commentaire). Seul ce qui reste dans la capsule nue est cherché : un pas ou une
    phrase réservé à une variante peut nommer son client."""
    import re
    if fichier is None:
        sys.path.insert(0, str(ICI.parent / "commun"))
        import chemins
        fichier = chemins.DATA / "capsuleforge" / "noms_a_eviter.txt"
    if not Path(fichier).is_file():
        return []
    noms = [l.split("#")[0].strip() for l in Path(fichier).read_text(encoding="utf-8").splitlines()]
    noms = [n for n in noms if n]
    if not noms:
        return []
    motif = re.compile(r"(?<!\w)(" + "|".join(re.escape(n) for n in noms) + r")(?!\w)", re.I)
    trouves = []

    def voir(textes, ou):
        for t in textes:
            m = motif.search(t)
            if m:
                trouves.append(f"« {m.group(1)} » dans la capsule nue : {ou}")
                return

    voir(_textes(chap.get("titre")), "titre du chapitre")
    for p in chap.get("parties") or []:
        if not retenu(p, None):
            continue
        voir(_textes(p.get("titre")), f"partie {p.get('id')}")
        for s in p.get("sections") or []:
            if not retenu(s, None):
                continue
            voir(_textes(s.get("titre")) + _textes(s.get("objectif")) + _textes(s.get("narration")) + _textes(s.get("ouverture")),
                 f"section {s.get('id')}")
            for q in s.get("pas") or []:
                if not retenu(q, None) or q.get("ecarte"):
                    continue
                for k, ph in enumerate(q.get("phrases") or []):
                    if retenu(ph, None):
                        voir(_textes(ph.get("texte")), f"pas {q.get('id')}, phrase {k + 1}")
                for o in q.get("objets") or []:
                    voir(_textes(o.get("texte")), f"pas {q.get('id')}, objet {o.get('id') or o.get('type')}")
    return trouves[:30] + ([f"… et {len(trouves) - 30} autres"] if len(trouves) > 30 else [])
