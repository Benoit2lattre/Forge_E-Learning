"""CapsuleForge — diagnostic de capture sous Windows (écran, webcam, micro) avec PyAV, à lancer si ``capsuleforge filmer`` ne trouve pas un appareil.

Utilisation : ::

    uv run scripts/capsuleforge/essai_capture.py            # liste les appareils, filme 5 s d'écran
    uv run scripts/capsuleforge/essai_capture.py --tout     # + 5 s de webcam et de micro (premiers appareils trouvés)
    uv run scripts/capsuleforge/essai_capture.py --tout --ecran 2   # écran n° 2 (défaut : l'écran principal)

Écrit dans data/capsuleforge/_essai_capture/ : ecran.mp4, webcam.mp4, micro.wav et rapport.txt (à joindre à un signalement).
Rien d'autre n'est modifié.
Licence : GPL v3.
"""
from __future__ import annotations

import platform
import re
import sys
import time
import traceback
import wave
from fractions import Fraction
from pathlib import Path

ICI = Path(__file__).resolve().parent
SORTIE = ICI.parent.parent / "data" / "capsuleforge" / "_essai_capture"
LIGNES: list[str] = []


def dire(t: str = "") -> None:
    """Affiche une ligne et la garde pour le rapport écrit à la fin (``rapport.txt``)."""
    print(t)
    LIGNES.append(t)


def appareils(av) -> tuple[list[str], list[str]]:
    """Renvoie les noms des appareils DirectShow (vidéo, audio).

    ffmpeg les écrit dans son journal avec l'option ``list_devices`` ; deux formes de journal sont lues
    (récente : une ligne par appareil suivie de ``(video)`` ou ``(audio)`` ; ancienne : deux sections).
    """
    videos, audios = [], []
    av.logging.set_level(av.logging.INFO)                         # PyAV ≥ 13 coupe le journal de ffmpeg par défaut
    with av.logging.Capture(True) as journal:
        try:
            av.open("dummy", format="dshow", options={"list_devices": "true"})
        except Exception:
            pass
    dire(f"  journal de ffmpeg : {len(journal)} ligne(s)" + "".join(f"\n    | {n} : {m.rstrip()}" for _l, n, m in list(journal)[:14]))
    for _niveau, _nom, msg in journal:
        m = re.search(r'"(.+?)"\s*\((video|audio)\)', msg)
        if m:
            (videos if m.group(2) == "video" else audios).append(m.group(1))
    if not videos and not audios:                                   # anciennes versions de ffmpeg : deux sections
        mode = None
        for _niveau, _nom, msg in journal:
            if "video devices" in msg.lower():
                mode = videos
            elif "audio devices" in msg.lower():
                mode = audios
            else:
                m = re.search(r'^\s*"(.+?)"\s*$', msg)
                if m and mode is not None and "@device" not in m.group(1):
                    mode.append(m.group(1))
    av.logging.set_level(None)
    return videos, audios


def appareils_windows() -> tuple[list[str], list[str]]:
    """Renvoie, en secours, les noms des caméras et micros vus par Windows (via PowerShell).

    Ces noms sont souvent les mêmes que ceux de DirectShow ; la caméra infrarouge est placée en dernier.
    """
    import subprocess
    def ps(cmd):
        r = subprocess.run(["powershell", "-NoProfile", "-Command", "[Console]::OutputEncoding = [Text.Encoding]::UTF8; " + cmd],
                           capture_output=True, text=True, encoding="utf-8", errors="replace")
        return [l.strip() for l in r.stdout.splitlines() if l.strip()]
    cams = ps("Get-PnpDevice -PresentOnly | Where-Object { $_.Class -in 'Camera','Image' -and $_.Status -eq 'OK' } | ForEach-Object FriendlyName")
    mics = ps("Get-PnpDevice -PresentOnly -Class AudioEndpoint | Where-Object { $_.Status -eq 'OK' -and $_.FriendlyName -match 'Micro|Mic|Entrée|Input|Réseau de' } | ForEach-Object FriendlyName")
    cams = sorted(cams, key=lambda n: " IR " in f" {n} " or "infrared" in n.lower())   # la caméra infrarouge (Windows Hello) en dernier
    return cams, mics


def ecran(n: int | None) -> dict:
    """Renvoie les options gdigrab pour filmer un seul écran.

    La géométrie vient de ``mss`` ; ``n`` = 1 (ou ``None``) pour l'écran principal. Renvoie un dictionnaire
    vide (tout le bureau) si la géométrie est inconnue.
    """
    try:
        import mss
        with mss.mss() as m:
            ms = m.monitors[1:]                                      # [0] = tous les écrans réunis
            dire(f"  écrans : " + " ; ".join(f"n° {k + 1} {e['width']} × {e['height']} en ({e['left']}, {e['top']})" for k, e in enumerate(ms)))
            e = ms[(n or 1) - 1]
            return {"offset_x": str(e["left"]), "offset_y": str(e["top"]), "video_size": f"{e['width']}x{e['height']}"}
    except Exception as ex:
        dire(f"  géométrie des écrans inconnue ({type(ex).__name__}) : tout le bureau sera filmé")
        return {}


def filmer(av, entree: str, fmt: str, options: dict, dst: Path, duree: float, ips: int = 15) -> None:
    """Filme ``duree`` secondes depuis une entrée ffmpeg (écran ou webcam) et les écrit en H.264 dans ``dst``.

    ``ips`` : images par seconde de la vidéo écrite. Le bilan (taille, cadence obtenue) va dans le rapport.
    """
    t0 = time.time()
    with av.open(entree, format=fmt, options=options) as e, av.open(str(dst), "w") as s:
        vs = e.streams.video[0]
        l, h = vs.codec_context.width, vs.codec_context.height
        ov = s.add_stream("libx264", rate=ips)
        ov.width, ov.height, ov.pix_fmt = l // 2 * 2, h // 2 * 2, "yuv420p"
        ov.options = {"preset": "ultrafast", "crf": "23"}      # capture rapide ; l'import recomprime ensuite
        n = 0
        for tr in e.decode(vs):
            if time.time() - t0 > duree:
                break
            im = tr.reformat(width=ov.width, height=ov.height, format="yuv420p")
            im.pts, im.time_base = n, Fraction(1, ips)
            n += 1
            for p in ov.encode(im):
                s.mux(p)
        for p in ov.encode(None):
            s.mux(p)
    dt = time.time() - t0
    dire(f"  OK {dst.name} : {l} × {h}, {n} images en {dt:.1f} s ({n / max(dt, 0.1):.1f} im/s), {dst.stat().st_size / 1e6:.2f} Mo")


def micro(av, nom: str, dst: Path, duree: float) -> None:
    """Enregistre ``duree`` secondes du micro DirectShow ``nom`` dans le WAV ``dst`` (mono, 48 kHz, 16 bits).

    Le niveau moyen (dBFS) est noté dans le rapport.
    """
    import numpy as np
    t0 = time.time()
    morceaux, taux = [], 48000
    with av.open(f"audio={nom}", format="dshow") as e:
        a = e.streams.audio[0]
        r = av.AudioResampler(format="s16", layout="mono", rate=taux)
        for tr in e.decode(a):
            if time.time() - t0 > duree:
                break
            for x in r.resample(tr):
                morceaux.append(x.to_ndarray().reshape(-1))
    son = np.concatenate(morceaux) if morceaux else np.zeros(0, np.int16)
    with wave.open(str(dst), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(taux); w.writeframes(son.astype(np.int16).tobytes())
    niveau = 20 * np.log10(max(1, float(np.sqrt(np.mean(son.astype(float) ** 2))) if len(son) else 1) / 32768)
    dire(f"  OK {dst.name} : {len(son) / taux:.1f} s, niveau moyen {niveau:.0f} dBFS (parler pendant l'essai : > -45 attendu)")


def main() -> int:
    """Lance l'essai (options ``--tout`` et ``--ecran N`` lues dans ``sys.argv``) et renvoie le code de sortie."""
    tout = "--tout" in sys.argv
    n_ecran = int(sys.argv[sys.argv.index("--ecran") + 1]) if "--ecran" in sys.argv else None
    SORTIE.mkdir(parents=True, exist_ok=True)
    dire(f"Essai de capture CapsuleForge — {time.strftime('%Y-%m-%d %H:%M')}")
    dire(f"Python {platform.python_version()} · {platform.platform()}")
    try:
        import av
    except ImportError:
        dire("PyAV absent : uv pip install av")
        return 1
    dire(f"PyAV {av.__version__} · bibliothèques : {', '.join(f'{k} {v}' for k, v in list(av.library_versions.items())[:3])}")
    for fmt in ("gdigrab", "dshow", "ddagrab"):
        try:
            av.format.ContainerFormat(fmt)
            dire(f"  format d'entrée {fmt} : disponible")
        except Exception as e:
            dire(f"  format d'entrée {fmt} : ABSENT ({type(e).__name__})")
    dire("")
    dire("Appareils (DirectShow) :")
    videos, audios = [], []
    try:
        videos, audios = appareils(av)
        dire(f"  caméras : {videos or 'aucune trouvée'}")
        dire(f"  micros  : {audios or 'aucun trouvé'}")
    except Exception as e:
        dire(f"  ÉCHEC de la liste : {type(e).__name__} : {e}")
    try:
        cw, mw = appareils_windows()
        dire(f"  vus par Windows — caméras : {cw or 'aucune'} ; micros : {mw or 'aucun'}")
        videos, audios = videos or cw, audios or mw
    except Exception as e:
        dire(f"  liste Windows impossible : {type(e).__name__} : {e}")
    dire("")
    dire("Écran (gdigrab, 5 s, 15 im/s) :")
    try:
        filmer(av, "desktop", "gdigrab", {"framerate": "15", "draw_mouse": "1", **ecran(n_ecran)}, SORTIE / "ecran.mp4", 5)
    except Exception as e:
        dire(f"  ÉCHEC : {type(e).__name__} : {e}")
        LIGNES.append(traceback.format_exc())
    if tout:
        dire("")
        dire("Webcam (5 s) :")
        for v in videos:
            try:
                dire(f"  essai avec « {v} »")
                filmer(av, f"video={v}", "dshow", {"rtbufsize": "100M"}, SORTIE / "webcam.mp4", 5, ips=30)
                break
            except Exception as e:
                dire(f"  ÉCHEC : {type(e).__name__} : {e}")
        if not videos:
            dire("  pas de caméra à essayer")
        dire("")
        dire("Micro (5 s : parler) :")
        for a in audios[:3]:                                     # le premier nom peut ne pas être celui de DirectShow
            try:
                micro(av, a, SORTIE / "micro.wav", 5)
                break
            except Exception as e:
                dire(f"  ÉCHEC avec « {a} » : {type(e).__name__} : {e}")
        if not audios:
            dire("  pas de micro à essayer")
    (SORTIE / "rapport.txt").write_text("\n".join(LIGNES) + "\n", encoding="utf-8")
    dire("")
    dire(f"Rapport : {SORTIE / 'rapport.txt'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
