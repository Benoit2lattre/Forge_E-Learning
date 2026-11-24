"""CapsuleForge — vidéo insérée dans une diapositive : extraction, recadrage, première et dernière images.

La vidéo est lue dans l'archive du diaporama, recadrée comme dans PowerPoint, mise à la taille voulue et
réencodée sans son (H.264). Ses première et dernière images sont écrites à part : la première est montrée avant
le départ, la dernière après la lecture et dans le PDF.

Taille (``qualite``, réglage ``powerpoint: {video: …}`` du chapitre ou ``capsuleforge pptx --video``) :

- ``standard`` : la taille de la zone de la vidéo dans le lecteur ;
- ``fine`` (défaut) : 1,5 fois cette taille (écrans haute densité, zoom) ;
- ``source`` : toute la définition de la vidéo recadrée.

Jamais plus grande que la source. Une vidéo déjà faite avec les mêmes réglages n'est pas refaite.

Licence : GPL v3.
"""
from __future__ import annotations

import hashlib
import json
import zipfile
from fractions import Fraction
from pathlib import Path

QUALITES = {"standard": 1.0, "fine": 1.5, "source": None}
CRF = 23


def _pair(n: float) -> int:
    return max(2, int(n) // 2 * 2)


def qualite_chapitre(chap: dict, demandee: str | None = None) -> str:
    q = demandee or ((chap.get("powerpoint") or {}).get("video")) or "fine"
    return q if q in QUALITES else "fine"


def extraire(pptx: Path, membre: str, recadrage: dict, largeur_zone: int, qualite: str, dst: Path,
             premiere: Path, derniere: Path) -> dict:
    """Extrait la vidéo ``membre`` du diaporama dans ``dst`` ; renvoie ``{duree_s, largeur, hauteur, refaite}``."""
    import av
    import numpy as np
    from PIL import Image
    with zipfile.ZipFile(pptx) as z:
        brut = z.read(membre)
    cle = hashlib.md5(brut + json.dumps([recadrage, largeur_zone, qualite, CRF], sort_keys=True).encode()).hexdigest()[:16]
    temoin = dst.with_suffix(".json")
    if dst.is_file() and premiere.is_file() and derniere.is_file() and temoin.is_file():
        try:
            t = json.loads(temoin.read_text(encoding="utf-8"))
            if t.get("cle") == cle:
                return {**t["infos"], "refaite": False}
        except ValueError:
            pass
    dst.parent.mkdir(parents=True, exist_ok=True)
    premiere.parent.mkdir(parents=True, exist_ok=True)
    src = dst.with_suffix(".source" + Path(membre).suffix)
    src.write_bytes(brut)
    tmp = dst.with_suffix(".tmp.mp4")
    try:
        with av.open(str(src)) as e:
            vs = e.streams.video[0]
            l0, h0 = vs.codec_context.width, vs.codec_context.height
            x0, y0 = round(l0 * recadrage.get("l", 0)), round(h0 * recadrage.get("t", 0))
            x1, y1 = round(l0 * (1 - recadrage.get("r", 0))), round(h0 * (1 - recadrage.get("b", 0)))
            lc, hc = max(2, x1 - x0), max(2, y1 - y0)
            f = QUALITES[qualite]
            l1 = lc if f is None else min(lc, largeur_zone * f)
            l1, h1 = _pair(l1), _pair(hc * l1 / lc)
            ips = max(1, round(float(vs.average_rate or vs.guessed_rate or 25)))
            with av.open(str(tmp), "w", format="mp4", options={"movflags": "+faststart"}) as s:
                ov = s.add_stream("libx264", rate=ips)
                ov.width, ov.height, ov.pix_fmt = l1, h1, "yuv420p"
                ov.options = {"crf": str(CRF), "preset": "veryfast"}
                n, derniere_im = 0, None
                for tr in e.decode(vs):
                    a = tr.to_ndarray(format="rgb24")[y0:y1, x0:x1]
                    im = Image.fromarray(a).resize((l1, h1), Image.LANCZOS)
                    if n == 0:
                        im.save(premiere)
                    derniere_im = im
                    fr = av.VideoFrame.from_ndarray(np.asarray(im), format="rgb24").reformat(format="yuv420p")
                    fr.pts, fr.time_base = n, Fraction(1, ips)
                    for pq in ov.encode(fr):
                        s.mux(pq)
                    n += 1
                for pq in ov.encode(None):
                    s.mux(pq)
            if derniere_im is not None:
                derniere_im.save(derniere)
        tmp.replace(dst)
    finally:
        src.unlink(missing_ok=True)
        tmp.unlink(missing_ok=True)
    infos = {"duree_s": round(n / ips, 2), "largeur": l1, "hauteur": h1, "images": n, "ips": ips,
             "source": [l0, h0], "recadree": [lc, hc]}
    temoin.write_text(json.dumps({"cle": cle, "infos": infos}), encoding="utf-8")
    return {**infos, "refaite": True}
