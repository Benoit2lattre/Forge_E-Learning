"""CapsuleForge — import d'une vidéo dans un chapitre (format 2) : pas de type vidéo.

Utilisation : ::

    capsuleforge video <fichier> --chapitre <ch> --section <partie/section> [--son audio.mp4] [--titre T] [--debut s] [--fin s]
                       [--decoupe silences|aucune] [--pas-min 20] [--pas-max 90] [--qualite 28] [--remplacer]

Sources : enregistrement d'écran, vidéo exportée d'ActivePresenter, clip quelconque (MP4, MKV, MOV, WEBM…).
ActivePresenter range le son à part (``audio_NNN.mp4`` à côté de ``Video_NNN.mp4``) : le donner avec ``--son``.

1. La vidéo est comprimée une fois dans ``<chapitre>/videos/<nom>.mp4`` (H.264 « veryfast », qualité CRF 28 par
   défaut, largeur au plus celle de l'écran du chapitre, 30 images/s au plus, son AAC mono 64 kb/s).
2. Elle est découpée en pas aux silences de la voix (pas de 20 à 90 s par défaut ; « aucune » = un seul pas).
3. Chaque pas reçoit : ``video: {fichier, debut_s, fin_s}`` (son extrait de la vidéo), ``duree_s``, une image
   d'affiche ``fond`` (``images/<id>.png``, première image du pas) et son propre son ``audio`` (``audio/<id>.wav``) : la
   relecture, la transcription (``capsuleforge transcrire``), la traduction et les voix fonctionnent comme pour
   une diapositive. Identifiants : v01, v02… (uniques dans le chapitre).

La section peut être créée : ``--section partie/nouvel_id --titre "Titre"``. ``--remplacer`` retire d'abord de la
section les pas déjà importés de ce même fichier (``source.fichier``).
Licence : GPL v3.
"""
from __future__ import annotations

import shutil
import time
import wave
from fractions import Fraction
from pathlib import Path

import numpy as np

import format2 as F

TAUX_SON = 22050


def _pair(n: int) -> int:
    """Renvoie l'entier pair inférieur ou égal à ``n`` (au moins 2), comme l'exige H.264."""
    return max(2, int(n) // 2 * 2)


def comprimer(src: Path, dst: Path, largeur_max: int = 1440, qualite: int = 28, debut: float = 0.0,
              fin: float | None = None, ips_max: int = 30, son_src: Path | None = None, muet: bool = False,
              journal=print) -> dict:
    """Comprime la vidéo ``src`` dans ``dst`` (H.264 + AAC mono), entre ``debut`` et ``fin`` (secondes).

    Le son vient de la vidéo, ou de ``son_src`` (ActivePresenter exporte le son à part : ``audio_NNN.mp4``) ;
    ``muet=True`` n'en met aucun. Renvoie ``{duree_s, largeur, hauteur, son: (échantillons mono float32, taux)}``.
    """
    import av
    dst.parent.mkdir(parents=True, exist_ok=True)
    tmp = dst.with_suffix(".tmp.mp4")
    sons: list[np.ndarray] = []
    garder = lambda t: t is not None and t >= debut - 1e-3 and (fin is None or t <= fin)
    with av.open(str(src)) as e, av.open(str(tmp), "w", format="mp4") as s:
        if not e.streams.video:
            raise SystemExit(f"{src.name} : pas de piste vidéo")
        vs = e.streams.video[0]
        l0, h0 = vs.codec_context.width, vs.codec_context.height
        l1 = min(l0, largeur_max)
        h1 = _pair(round(h0 * l1 / l0)); l1 = _pair(l1)
        ips = min(ips_max, max(1, round(float(vs.average_rate or vs.guessed_rate or 30))))
        ov = s.add_stream("libx264", rate=ips)
        ov.width, ov.height, ov.pix_fmt = l1, h1, "yuv420p"
        ov.options = {"crf": str(qualite), "preset": "veryfast"}
        source_son = None if muet else Path(son_src) if son_src else (src if e.streams.audio else None)
        oa = None
        if source_son:
            oa = s.add_stream("aac", rate=48000)
            oa.bit_rate = 64000
            try:
                oa.layout = "mono"
            except Exception:
                pass
        # 1. images
        n_img, dernier = 0, -1
        for tr in e.decode(vs):
            t = float(tr.time) if tr.time is not None else None
            if not garder(t):
                continue
            pts = int(round((t - debut) * ips))                  # chaque image à son instant (captures à cadence irrégulière)
            if pts <= dernier:                                   # au plus ips images par seconde
                continue
            dernier = pts
            im = tr.reformat(width=l1, height=h1, format="yuv420p")
            im.pts, im.time_base = pts, Fraction(1, ips)
            n_img += 1
            for pq in ov.encode(im):
                s.mux(pq)
        for pq in ov.encode(None):
            s.mux(pq)
        # 2. son (de la vidéo ou du fichier à part)
        if source_son:
            r_aac = av.AudioResampler(format="fltp", layout="mono", rate=48000)
            r_son = av.AudioResampler(format="flt", layout="mono", rate=TAUX_SON)
            with av.open(str(source_son)) as ea:
                if not ea.streams.audio:
                    raise SystemExit(f"{Path(source_son).name} : pas de piste son")
                t0 = None
                for tr in ea.decode(ea.streams.audio[0]):
                    t = float(tr.time) if tr.time is not None else 0.0
                    if fin is not None and t > fin:
                        break
                    t0 = t if t0 is None else t0
                    tr.pts = None
                    for x in r_son.resample(tr):                 # son des pas : tout, rogné plus bas à l'échantillon
                        sons.append(x.to_ndarray().reshape(-1))
                    if t + tr.samples / tr.sample_rate < debut:
                        continue
                    for x in r_aac.resample(tr):
                        for pq in oa.encode(x):
                            s.mux(pq)
                for x in r_aac.resample(None):
                    for pq in oa.encode(x):
                        s.mux(pq)
                for pq in oa.encode(None):
                    s.mux(pq)
    tmp.replace(dst)
    son = np.concatenate(sons).astype(np.float32) if sons else np.zeros(0, np.float32)
    if source_son and len(son):                              # rogné à l'échantillon près sur [debut, fin]
        a = max(0, int(round((debut - (t0 or 0.0)) * TAUX_SON)))
        son = son[a: a + int(round(((fin if fin is not None else 1e9) - debut) * TAUX_SON))] if fin is not None else son[a:]
    duree = round((dernier + 1) / ips, 2) if dernier >= 0 else 0.0
    if not source_son and not muet:
        journal(f"  ATTENTION : {src.name} n'a pas de son (ActivePresenter exporte le son à part, fichier audio_NNN.mp4 : "
                "le donner avec --son) ; découpe en pas réguliers")
    journal(f"  {src.name} -> {dst.name} : {l1} × {h1}, {ips} im/s, {duree:.1f} s"
            + (f", son de {Path(source_son).name}" if son_src else "") + f", {dst.stat().st_size / 1e6:.1f} Mo")
    return {"duree_s": duree, "largeur": l1, "hauteur": h1, "son": (son, TAUX_SON)}


def silences(son: np.ndarray, taux: int, min_s: float = 0.6) -> list[tuple[float, float]]:
    """Renvoie les intervalles de silence ``(début, fin)`` d'au moins ``min_s`` secondes, seuil adapté au niveau de la voix."""
    if not len(son):
        return []
    f = int(taux * 0.05)
    n = len(son) // f
    if n < 4:
        return []
    rms = np.sqrt(np.mean(son[: n * f].reshape(n, f) ** 2, axis=1) + 1e-12)
    db = 20 * np.log10(rms)
    seuil = max(np.percentile(db, 15) + 6, np.percentile(db, 90) - 30, -55)
    calme = db < seuil
    res, k = [], 0
    while k < n:
        if calme[k]:
            j = k
            while j < n and calme[j]:
                j += 1
            if (j - k) * 0.05 >= min_s:
                res.append((k * 0.05, j * 0.05))
            k = j
        else:
            k += 1
    return res


def coupes(duree: float, sil: list[tuple[float, float]], pas_min: float, pas_max: float) -> list[float]:
    """Renvoie les instants de coupe des pas, au milieu d'un silence.

    Tant que le reste dépasse ``pas_max``, la coupe se fait au premier silence d'au moins 1 s situé entre
    ``pas_min`` et ``pas_max`` après le début du pas, sinon au plus long silence de cet intervalle, sinon à
    ``pas_max`` ; un dernier bout plus court que ``pas_min / 2`` n'est pas créé.
    """
    res, debut = [], 0.0
    milieux = [((a + b) / 2, b - a) for a, b in sil]
    while duree - debut > pas_max:
        ok = [(m, l) for m, l in milieux if debut + pas_min <= m <= debut + pas_max]
        if ok:
            premier_long = next((m for m, l in ok if l >= 1.0), None)
            c = premier_long if premier_long is not None else max(ok, key=lambda x: x[1])[0]
        else:
            c = debut + pas_max
        if duree - c < pas_min / 2:                      # pas de dernier bout trop court
            break
        res.append(round(c, 2))
        debut = c
    if not res and duree > pas_max:
        res = [round(duree / 2, 2)]
    return res


def affiche(video: Path, t: float, dst: Path) -> None:
    """Enregistre dans ``dst`` l'image de la vidéo à l'instant ``t`` (première image décodée à partir de ``t``)."""
    import av
    dst.parent.mkdir(parents=True, exist_ok=True)
    with av.open(str(video)) as e:
        vs = e.streams.video[0]
        if t > 0.5:
            e.seek(int(max(0.0, t - 1.0) / vs.time_base), stream=vs, backward=True)
        dernier = None
        for tr in e.decode(vs):
            dernier = tr
            if tr.time is not None and tr.time >= t - 1e-3:
                break
        if dernier is not None:
            dernier.to_image().save(dst)


def _ecrire_wav(chemin: Path, a: np.ndarray, taux: int) -> None:
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(chemin), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(taux)
        w.writeframes((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes())


def _section(chap: dict, ref: str, titre: str | None):
    """Renvoie ``(partie, section)`` désignées par « partie/section » ou « section ».

    Avec « partie/nouvelle » et un titre (``--titre``), la section est créée.
    """
    if "/" in ref:
        pid, sid = ref.split("/", 1)
        p = next((x for x in chap.get("parties") or [] if x.get("id") == pid), None)
        if not p:
            raise SystemExit(f"Partie introuvable : {pid}")
        s = next((x for x in p.get("sections") or [] if x.get("id") == sid), None)
        if not s:
            if not titre:
                raise SystemExit(f"Section {ref} introuvable (pour la créer : --titre \"…\")")
            s = {"id": sid, "titre": titre, "arret": True, "questions": [], "pas": []}
            p.setdefault("sections", []).append(s)
        return p, s
    trouvees = [(p, s) for p in chap.get("parties") or [] for s in p.get("sections") or [] if s.get("id") == ref]
    if len(trouvees) != 1:
        raise SystemExit(f"Section « {ref} » : {len(trouvees)} trouvée(s) ; écrire partie/section")
    return trouvees[0]


def importer(yaml_chap: Path, fichier: Path, section: str, titre: str | None = None, debut: float = 0.0,
             fin: float | None = None, decoupe: str = "silences", pas_min: float = 20, pas_max: float = 90,
             qualite: int = 28, remplacer: bool = False, son: Path | None = None, camera: Path | None = None,
             journal=print) -> int:
    """Importe une vidéo dans une section d'un chapitre, découpée en pas vidéo ; renvoie le nombre de pas créés.

    Écrit la vidéo comprimée (``videos/``), une image d'affiche et un son par pas (``images/``, ``audio/``),
    éventuellement la vidéo de la webcam (``camera``), puis sauvegarde et réécrit le chapitre.
    """
    fichier = Path(fichier)
    if not fichier.is_file():
        raise SystemExit(f"Vidéo introuvable : {fichier}")
    dossier = yaml_chap.parent
    chap = F.lire(yaml_chap)
    partie, sec = _section(chap, section, titre)
    largeur = (chap.get("ecran") or {}).get("largeur") or 1440
    nom = "".join(c if c.isalnum() or c in "-_" else "_" for c in fichier.stem).strip("_")[:60] or "video"
    if debut or fin:
        nom += f"_{int(debut)}-{int(fin) if fin else 'fin'}"
    rel = f"videos/{nom}.mp4"
    journal(f"Compression de {fichier.name} (peut prendre du temps : environ la durée de la vidéo)…")
    if son and not Path(son).is_file():
        raise SystemExit(f"Son introuvable : {son}")
    info = comprimer(fichier, dossier / rel, largeur_max=largeur, qualite=qualite, debut=debut, fin=fin,
                     son_src=Path(son) if son else None, journal=journal)
    son, taux = info["son"]
    duree = info["duree_s"]
    rel_cam = None
    if camera:                                               # webcam filmée en même temps : caméo calé sur la vidéo
        rel_cam = f"videos/{nom}_camera.mp4"
        comprimer(Path(camera), dossier / rel_cam, largeur_max=640, qualite=30, debut=debut, fin=fin, muet=True, journal=journal)
    if decoupe != "silences":
        cps = []
    elif len(son):
        cps = coupes(duree, silences(son, taux), pas_min, pas_max)
    else:                                                    # pas de son : pas réguliers d'au plus pas_max
        n = int(np.ceil(duree / pas_max)) if duree > pas_max else 1
        cps = [round(duree * k / n, 2) for k in range(1, n)]
    bornes = [0.0] + cps + [duree]
    if remplacer:
        avant = len(sec.get("pas") or [])
        sec["pas"] = [q for q in sec.get("pas") or [] if (q.get("source") or {}).get("fichier") != fichier.name]
        journal(f"  {avant - len(sec['pas'])} pas déjà importés de {fichier.name} retirés")
    pris = {q.get("id") for p in chap.get("parties") or [] for s in p.get("sections") or [] for q in s.get("pas") or []}
    k = 1
    nouveaux = []
    for a, b in zip(bornes, bornes[1:]):
        while f"v{k:02d}" in pris:
            k += 1
        pid = f"v{k:02d}"
        pris.add(pid)
        affiche(dossier / rel, a, dossier / "images" / f"{pid}.png")
        _ecrire_wav(dossier / "audio" / f"{pid}.wav", son[int(a * taux): int(b * taux)], taux)
        q = {"id": pid, "fond": f"images/{pid}.png", "audio": f"audio/{pid}.wav", "duree_s": round(b - a, 2),
             "video": {"fichier": rel, "debut_s": round(a, 2), "fin_s": round(b, 2)},
             "source": {"type": "video", "fichier": fichier.name, "debut_s": round(debut + a, 2), "fin_s": round(debut + b, 2)},
             "objets": []}
        if rel_cam:
            q["camera"] = {"fichier": rel_cam, "debut_s": round(a, 2), "fin_s": round(b, 2)}
        nouveaux.append(q)
    sec.setdefault("pas", []).extend(nouveaux)
    if (chap.get("source") or {}).get("conversion"):       # chapitre converti d'une capsule : il devient la source
        chap["source"].pop("conversion")
        journal(f"  {yaml_chap.name} n'est plus refait par « convertir » (il porte maintenant des pas vidéo) ; "
                "construire le lecteur au format 2 : « construire … --lecteur 2 »")
    (dossier / "sauvegardes").mkdir(exist_ok=True)
    if yaml_chap.is_file():
        shutil.copy2(yaml_chap, dossier / "sauvegardes" / f"chapitre_{time.strftime('%Y%m%d_%H%M%S')}.yaml")
    F.ecrire(chap, yaml_chap)
    detail = ", ".join(f"{q['id']} {q['duree_s']:.0f} s" for q in nouveaux)
    journal(f"  section {partie.get('id')}/{sec.get('id')} : {len(nouveaux)} pas vidéo ({detail})")
    journal(f"  suite : capsuleforge transcrire {dossier.name} --sections {sec.get('id')} puis capsuleforge relire {dossier.name}")
    return len(nouveaux)
