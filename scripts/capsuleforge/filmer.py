"""CapsuleForge — enregistreur intégré : écran, micro et webcam en même temps (Windows), puis import dans un chapitre.

Commande : ::

    capsuleforge filmer <chapitre> --section partie/section [--titre "…"] [--ecran 1] [--webcam [NOM]] [--micro NOM | --sans-micro]
                        [--ips 20] [--duree s] [--sans-import] [--appareils]

Raccourcis (comme l'enregistreur de didacticiel) : Ctrl+Maj+P pause / reprise (2 bips), Ctrl+Maj+F fin (3 bips) ;
dans la fenêtre de commande, Entrée termine aussi. Un compte à rebours de 3 s précède l'enregistrement.

Chaque source a son fil ; chaque image et chaque morceau de son reçoit l'instant de l'horloge commune (pauses
retirées) : l'écran, la webcam et la voix restent calés, même si une source démarre en retard (le micro met environ
une seconde à s'ouvrir : le début du son est complété par du silence). Fichiers bruts dans
``<chapitre>/enregistrements/<date>/`` (``ecran_<date>.mp4``, ``micro_<date>.wav``, ``camera_<date>.mp4``, ``journal.txt``), puis import
comme ``capsuleforge video … --son micro.wav`` : pas vidéo découpés aux silences ; la webcam devient le caméo de ces
pas. Appareils : DirectShow (noms lus dans le journal de ffmpeg) ; écrans : mss. ``--appareils`` les liste.
Essai sans appareils (toutes plateformes) : ``--essai`` (mire et son synthétiques).
Licence : GPL v3.
"""
from __future__ import annotations

import queue
import re
import sys
import threading
import time
import wave
from fractions import Fraction
from pathlib import Path

import numpy as np

from raccourcis import Intercepteur, bip, modificateurs_enfonces

TAUX = 48000


# --------------------------------------------------------------------------- appareils

def appareils() -> tuple[list[str], list[str]]:
    """Renvoie les listes (caméras, micros) des appareils DirectShow.

    ffmpeg écrit la liste dans son journal, par morceaux : on les recolle. La caméra virtuelle d'OBS est
    écartée et les caméras infrarouges sont placées en dernier.
    """
    import av
    av.logging.set_level(av.logging.INFO)
    with av.logging.Capture(True) as journal:
        try:
            av.open("dummy", format="dshow", options={"list_devices": "true"})
        except Exception:
            pass
    av.logging.set_level(None)
    texte = "".join(m for _n, _c, m in journal)
    videos = [n for n, t in re.findall(r'"([^"@]+)"\s*\((video|audio)\)', texte) if t == "video"]
    audios = [n for n, t in re.findall(r'"([^"@]+)"\s*\((video|audio)\)', texte) if t == "audio"]
    videos = [v for v in videos if "obs virtual" not in v.lower()]
    videos.sort(key=lambda n: " ir " in f" {n.lower()} " or "infrared" in n.lower())   # caméra infrarouge (Windows Hello) en dernier
    return videos, audios


def ecrans() -> list[dict]:
    """Renvoie les écrans vus par ``mss`` (``left``, ``top``, ``width``, ``height``), ou une liste vide."""
    try:
        import mss
        with mss.mss() as m:
            return [dict(e) for e in m.monitors[1:]]
    except Exception:
        return []


# --------------------------------------------------------------------------- horloge commune et sources

class Horloge:
    """Temps utile de l'enregistrement : depuis le départ, pauses retirées."""

    def __init__(self):
        self.t0 = None
        self.pause_debut = None
        self.pauses = 0.0
        self.fin = threading.Event()

    def demarrer(self):
        """Fixe l'instant de départ de l'horloge."""
        self.t0 = time.monotonic()

    def en_pause(self) -> bool:
        """Indique si l'enregistrement est en pause."""
        return self.pause_debut is not None

    def basculer(self) -> bool:
        """Met en pause ou reprend ; renvoie ``True`` si l'enregistrement vient d'entrer en pause."""
        if self.pause_debut is None:
            self.pause_debut = time.monotonic()
            return True
        self.pauses += time.monotonic() - self.pause_debut
        self.pause_debut = None
        return False

    def maintenant(self, t: float | None = None) -> float:
        """Renvoie le temps utile (s) à l'instant ``t`` de ``time.monotonic()``, ou maintenant par défaut."""
        t = time.monotonic() if t is None else t
        return t - self.t0 - self.pauses


class Video(threading.Thread):
    """Une source d'images (écran ou webcam) -> MP4 H.264, chaque image à son instant (cadence variable)."""

    def __init__(self, nom: str, entree: str, fmt: str, options: dict, dst: Path, horloge: Horloge,
                 ips: int = 20, largeur_max: int | None = None, crf: int = 23):
        super().__init__(daemon=True, name=nom)
        self.nom, self.entree, self.fmt, self.options, self.dst = nom, entree, fmt, options, dst
        self.h, self.ips, self.largeur_max, self.crf = horloge, ips, largeur_max, crf
        self.file: queue.Queue = queue.Queue(maxsize=int(ips * 2))
        self.n = self.perdues = 0
        self.erreur = None
        self.pret = threading.Event()

    def run(self):
        """Lit la source et met en file les images horodatées (hors pause) ; un second fil les encode."""
        import av
        try:
            with av.open(self.entree, format=self.fmt, options=self.options) as e:
                vs = e.streams.video[0]
                l0, h0 = vs.codec_context.width, vs.codec_context.height
                l1 = min(l0, self.largeur_max or l0)
                self.taille = (l1 // 2 * 2, int(h0 * l1 / l0) // 2 * 2)
                ecrivain = threading.Thread(target=self._ecrire, daemon=True)
                ecrivain.start()
                self.pret.set()
                for tr in e.decode(vs):
                    t = time.monotonic()
                    if self.h.fin.is_set():
                        break
                    if self.h.t0 is None or self.h.en_pause():
                        continue
                    try:
                        self.file.put_nowait((self.h.maintenant(t), tr))
                    except queue.Full:
                        self.perdues += 1                                  # encodage en retard : on saute l'image
                self.file.put(None)
                ecrivain.join()
        except Exception as ex:
            self.erreur = f"{type(ex).__name__} : {ex}"
            self.pret.set()

    def _ecrire(self):
        """Encode en H.264 les images de la file, à leur instant, jusqu'à recevoir ``None``."""
        import av
        l, h = self.taille
        with av.open(str(self.dst), "w") as s:
            ov = s.add_stream("libx264", rate=self.ips)
            ov.width, ov.height, ov.pix_fmt = l, h, "yuv420p"
            ov.options = {"preset": "ultrafast", "crf": str(self.crf)}
            dernier = -1
            while True:
                x = self.file.get()
                if x is None:
                    break
                t, tr = x
                pts = int(round(t * self.ips))
                if pts <= dernier or t < 0:
                    continue
                dernier = pts
                im = tr.reformat(width=l, height=h, format="yuv420p")
                im.pts, im.time_base = pts, Fraction(1, self.ips)
                for p in ov.encode(im):
                    s.mux(p)
                self.n += 1
            for p in ov.encode(None):
                s.mux(p)


class Micro(threading.Thread):
    """Le micro -> WAV mono 48 kHz ; le début est complété par du silence pour être calé sur l'horloge commune."""

    def __init__(self, entree: str, fmt: str, options: dict, dst: Path, horloge: Horloge):
        super().__init__(daemon=True, name="micro")
        self.entree, self.fmt, self.options, self.dst, self.h = entree, fmt, options, dst, horloge
        self.ecrits = 0
        self.combles = 0
        self.retard = None
        self.erreur = None
        self.pret = threading.Event()
        self.niveaux: list[float] = []

    def run(self):
        """Écrit le son du micro dans le WAV, calé sur l'horloge commune.

        Le retard d'ouverture et les trous de plus de 0,15 s sont comblés par du silence ; le niveau de chaque
        morceau est noté dans ``niveaux``.
        """
        import av
        try:
            with av.open(self.entree, format=self.fmt, options=self.options) as e, wave.open(str(self.dst), "wb") as w:
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(TAUX)
                r = av.AudioResampler(format="s16", layout="mono", rate=TAUX)
                self.pret.set()
                for tr in e.decode(e.streams.audio[0]):
                    t = time.monotonic()
                    if self.h.fin.is_set():
                        break
                    if self.h.t0 is None or self.h.en_pause():
                        continue
                    for x in r.resample(tr):
                        a = x.to_ndarray().reshape(-1).astype(np.int16)
                        if self.retard is None:                            # premier son reçu : silence jusqu'à lui
                            self.retard = max(0.0, self.h.maintenant(t) - len(a) / TAUX)
                            w.writeframes(np.zeros(int(self.retard * TAUX), np.int16).tobytes())
                            self.ecrits += int(self.retard * TAUX)
                        else:                                              # son perdu par Windows (machine chargée) :
                            manque = int(self.h.maintenant(t) * TAUX) - (self.ecrits + len(a))     # on comble pour rester calé
                            if manque > 0.15 * TAUX:
                                w.writeframes(np.zeros(manque, np.int16).tobytes())
                                self.ecrits += manque
                                self.combles += manque
                        w.writeframes(a.tobytes())
                        self.ecrits += len(a)
                        self.niveaux.append(float(np.sqrt(np.mean(a.astype(float) ** 2))) if len(a) else 0.0)
        except Exception as ex:
            self.erreur = f"{type(ex).__name__} : {ex}"
            self.pret.set()


# --------------------------------------------------------------------------- l'enregistrement

def enregistrer(dossier: Path, ecran: int | None = 1, webcam: str | bool | None = None, micro: str | bool | None = True,
                ips: int = 20, duree: float | None = None, essai: bool = False, journal=print) -> dict:
    """Filme l'écran, le micro et la webcam demandés dans ``dossier`` jusqu'à la fin demandée.

    La fin vient du raccourci Ctrl+Maj+F, de la touche Entrée ou de ``duree`` (secondes utiles). Écrit les
    fichiers des sources et ``journal.txt`` ; renvoie le dictionnaire des chemins écrits (clés ``ecran``,
    ``micro``, ``camera`` selon les sources). ``essai=True`` remplace les appareils par des sources synthétiques.
    """
    dossier.mkdir(parents=True, exist_ok=True)
    h = Horloge()
    nom = lambda base, ext: dossier / f"{base}_{dossier.name}.{ext}"          # noms uniques : les vidéos importées les gardent
    sources: list = []
    vids, auds = ([], []) if essai else appareils()
    # écran
    if essai:
        sources.append(Video("écran", f"testsrc2=size=1280x800:rate={ips},realtime", "lavfi", {}, nom("ecran", "mp4"), h, ips))
    else:
        es = ecrans()
        opt = {"framerate": str(ips), "draw_mouse": "1"}
        if es:
            e = es[min(len(es), max(1, ecran or 1)) - 1]
            opt.update(offset_x=str(e["left"]), offset_y=str(e["top"]), video_size=f"{e['width']}x{e['height']}")
            journal(f"  écran n° {ecran or 1} : {e['width']} × {e['height']}")
        sources.append(Video("écran", "desktop", "gdigrab", opt, nom("ecran", "mp4"), h, ips))
    # webcam
    if webcam:
        if essai:
            sources.append(Video("webcam", "testsrc=size=640x360:rate=25,realtime", "lavfi", {}, nom("camera", "mp4"), h, 25, 640, 26))
        else:
            cam = webcam if isinstance(webcam, str) else (vids[0] if vids else None)
            if not cam:
                raise SystemExit("Aucune webcam trouvée (capsuleforge filmer --appareils)")
            journal(f"  webcam : {cam}")
            sources.append(Video("webcam", f"video={cam}", "dshow", {"rtbufsize": "100M"}, nom("camera", "mp4"), h, 25, 1280, 26))
    # micro
    mic = None
    if micro:
        if essai:
            mic = Micro("sine=frequency=330:sample_rate=48000,arealtime", "lavfi", {}, nom("micro", "wav"), h)
        else:
            m = micro if isinstance(micro, str) else (auds[0] if auds else None)
            if not m:
                raise SystemExit("Aucun micro trouvé (capsuleforge filmer --appareils)")
            journal(f"  micro : {m}")
            mic = Micro(f"audio={m}", "dshow", {"audio_buffer_size": "100", "rtbufsize": "50M"}, nom("micro", "wav"), h)
        sources.append(mic)
    for s in sources:
        s.start()
    for s in sources:
        s.pret.wait(15)
        if s.erreur:
            h.fin.set()
            raise SystemExit(f"Impossible d'ouvrir {s.name} : {s.erreur}")
    # raccourcis : interceptés avant l'application filmée (filtre Windows, comme l'enregistreur de didacticiel) ;
    # les modificateurs sont lus dans l'état réel du clavier (pas de touche « restée enfoncée » après un changement de fenêtre)
    ecouteur = None
    try:
        if not essai:

            def pause():
                p = h.basculer()
                bip(2)
                journal("  ⏸ pause" if p else "  ▶ reprise")

            def fin():
                h.fin.set()
                bip(3)
            actions = {0x50: pause, 0x46: fin}                                # P, F (avec Ctrl+Maj exactement)

            def action_de(vk):
                return actions[vk] if vk in actions and modificateurs_enfonces() == {"ctrl", "shift"} else None
            ecouteur = Intercepteur(action_de).ecouteur_clavier()
            ecouteur.start()
    except Exception as ex:
        journal(f"  raccourcis indisponibles ({type(ex).__name__}) : Entrée pour finir")
    if not essai and duree is None:
        threading.Thread(target=lambda: (input(), h.fin.set()), daemon=True).start()
    for k in (3, 2, 1):
        journal(f"  départ dans {k}…")
        time.sleep(1)
    bip(1)
    h.demarrer()
    journal("  ● enregistrement — Ctrl+Maj+P pause, Ctrl+Maj+F (ou Entrée) fin")
    while not h.fin.is_set():
        if duree is not None and h.maintenant() >= duree:
            h.fin.set()
            break
        time.sleep(0.1)
    total = h.maintenant()
    if ecouteur:
        ecouteur.stop()
    for s in sources:
        s.join(20)
    res = {}
    lignes = [f"durée utile {total:.1f} s, pauses {h.pauses:.1f} s"]
    for s in sources:
        if isinstance(s, Video):
            lignes.append(f"{s.name} : {s.n} images ({s.n / max(total, 0.1):.1f} im/s), {s.perdues} sautées"
                          + (f", ERREUR {s.erreur}" if s.erreur else ""))
            res["ecran" if s.name == "écran" else "camera"] = s.dst
        else:
            niv = 20 * np.log10(max(1.0, float(np.median(s.niveaux))) / 32768) if s.niveaux else -99
            lignes.append(f"micro : {s.ecrits / TAUX:.1f} s (départ retardé de {s.retard or 0:.2f} s, complété ; "
                          f"{s.combles / TAUX:.2f} s de son perdu comblées), niveau {niv:.0f} dBFS"
                          + (f", ERREUR {s.erreur}" if s.erreur else ""))
            if s.niveaux and niv < -50:
                lignes.append("  ATTENTION : micro très faible (coupé dans Windows, ou mauvais micro) : "
                              "« capsuleforge filmer --appareils » puis --micro \"nom\"")
            res["micro"] = s.dst
    (dossier / "journal.txt").write_text("\n".join(lignes) + "\n", encoding="utf-8")
    for l in lignes:
        journal("  " + l)
    return res


def filmer(yaml_chap: Path, section: str, titre: str | None = None, ecran: int | None = 1, webcam=None, micro=True,
           ips: int = 20, duree: float | None = None, importer: bool = True, essai: bool = False, journal=print) -> Path:
    """Filme dans ``enregistrements/<date_heure>/`` du chapitre puis importe la vidéo dans la section.

    ``section`` est de la forme ``partie/section`` ; ``titre`` sert si la section est à créer. La section est
    vérifiée avant de filmer. Avec ``importer=False``, la section peut manquer : les fichiers sont gardés et la
    commande d'import est affichée. Renvoie le dossier de
    l'enregistrement.
    """
    if importer:                        # section vérifiée avant de filmer, pas après
        import format2 as F
        import video
        video._section(F.lire(yaml_chap), section, titre)
    dossier = yaml_chap.parent / "enregistrements" / time.strftime("%Y%m%d_%H%M%S")
    journal(f"Enregistrement dans {dossier}")
    res = enregistrer(dossier, ecran, webcam, micro, ips, duree, essai, journal)
    if importer:
        import video
        video.importer(yaml_chap, res["ecran"], section, titre=titre, son=res.get("micro"), camera=res.get("camera"),
                       journal=journal)
    else:
        journal(f"  import : capsuleforge video \"{res['ecran']}\" --son \"{res.get('micro')}\" --chapitre {yaml_chap.parent.name} --section {section or 'partie/section'}")
    return dossier
