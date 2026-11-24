"""CapsuleForge — voix de synthèse d'un chapitre (format 2).

Utilisation : ::

    capsuleforge voix <chapitre> --langue en [--moteur piper|edge] [--voix NOM] [--vitesse 1.0] [--sections a,b] [--refaire]

La voix est fabriquée phrase par phrase, à partir des phrases du pas (texte dans la langue demandée), puis mise
bout à bout avec des silences proches de ceux de l'original. On connaît donc exactement l'instant de chaque phrase
dans le nouveau son : sous-titres, apparitions et objets (spots, pointeurs…) sont recalés phrase à phrase.

Deux usages :

- une autre langue que la langue source : le son est rangé dans ``pas.voix.<langue>`` (audio, duree_s, phrases =
  instants [début, fin] de chaque phrase) ; le son d'origine n'est pas touché ;
- la langue source, pour un pas sans enregistrement (diapositive neuve) ou déjà synthétisé : le son devient le son
  du pas (``audio``, ``duree_s``, instants des phrases), marqué ``source.voix: synthese`` ; une narration sans phrases est
  d'abord découpée en phrases. Un pas qui a un enregistrement n'est jamais remplacé.

Un pas déjà synthétisé n'est refait que si son texte a changé (ou avec --refaire).

Moteurs (gratuits) : « piper » (voix neuronale sur cet ordinateur, ``pip install piper-tts`` ; modèle téléchargé à la première
utilisation dans ``data/capsuleforge/_voix/``), « edge » (voix neuronales de Microsoft Edge, en ligne, sans clé :
``pip install edge-tts`` ; le texte part chez Microsoft). Moteur ``essai`` : voix factice pour les tests (durée selon le nombre de mots). Autres moteurs (payants) : à brancher dans ``MOTEURS``.
Licence : GPL v3.
"""
from __future__ import annotations

import hashlib
import shutil
import time
from pathlib import Path

import numpy as np

import calage as CAL
import format_chapitre as F
import sons as S

VOIX_DEFAUT = {
    "piper": {"fr": "fr_FR-tom-medium", "en": "en_GB-alan-medium", "es": "es_ES-davefx-medium", "de": "de_DE-thorsten-medium"},
    "edge": {"fr": "fr-FR-HenriNeural", "en": "en-GB-RyanNeural", "es": "es-ES-AlvaroNeural", "de": "de-DE-ConradNeural"},
}
TAUX = 22050


# --------------------------------------------------------------------------- moteurs : texte -> (échantillons float32, taux)

class Piper:
    """Moteur Piper (voix neuronale locale) ; le modèle ``<nom>.onnx`` est téléchargé dans ``dossier`` s'il manque."""

    def __init__(self, nom: str, dossier: Path, vitesse: float = 1.0):
        try:
            from piper import PiperVoice, SynthesisConfig
        except ImportError:
            raise SystemExit("La voix Piper demande piper-tts :  uv pip install piper-tts")
        dossier.mkdir(parents=True, exist_ok=True)
        modele = dossier / f"{nom}.onnx"
        if not modele.is_file():
            from piper.download_voices import download_voice
            print(f"Téléchargement de la voix « {nom} » dans {dossier}…")
            download_voice(nom, dossier)
        self.voix = PiperVoice.load(str(modele))
        self.config = SynthesisConfig(length_scale=1.0 / max(0.5, vitesse))

    def dire(self, texte: str):
        """Synthétise ``texte`` et renvoie ``(échantillons float32, taux d'échantillonnage)``."""
        morceaux = [c.audio_int16_array for c in self.voix.synthesize(texte, syn_config=self.config)]
        a = np.concatenate(morceaux) if morceaux else np.zeros(0, np.int16)
        return a.astype(np.float32) / 32768.0, self.voix.config.sample_rate


class Edge:
    """Moteur Edge (voix neuronales en ligne de Microsoft, via ``edge-tts``)."""

    def __init__(self, nom: str, dossier: Path, vitesse: float = 1.0):
        try:
            import edge_tts  # noqa: F401
        except ImportError:
            raise SystemExit("La voix Edge demande edge-tts :  uv pip install edge-tts")
        self.nom, self.vitesse, self.tmp = nom, vitesse, dossier / "_tmp_edge.mp3"
        dossier.mkdir(parents=True, exist_ok=True)

    def dire(self, texte: str):
        """Synthétise ``texte`` (MP3 temporaire décodé) et renvoie ``(échantillons float32, taux)``."""
        import asyncio
        import edge_tts
        taux = f"{round((self.vitesse - 1) * 100):+d}%"
        asyncio.run(edge_tts.Communicate(texte, self.nom, rate=taux).save(str(self.tmp)))
        return _decoder(self.tmp)


class Essai:
    """Moteur factice (essais sans voix installée) : un son dont la durée suit le nombre de mots."""
    def __init__(self, nom: str, dossier: Path, vitesse: float = 1.0):
        self.vitesse = vitesse

    def dire(self, texte: str):
        """Renvoie un son sinusoïdal de 220 Hz, d'environ 160 mots par minute (au moins 0,6 s)."""
        d = max(0.6, len(texte.split()) * 60 / 160 / self.vitesse)
        t = np.arange(int(d * TAUX)) / TAUX
        return (0.1 * np.sin(2 * np.pi * 220 * t)).astype(np.float32), TAUX


MOTEURS = {"piper": Piper, "edge": Edge, "essai": Essai}


def _decoder(f: Path):
    import av
    with av.open(str(f)) as e:
        p = e.streams.audio[0]
        r = av.AudioResampler(format="flt", layout="mono", rate=p.rate)
        a = [t.to_ndarray().reshape(-1) for tr in e.decode(p) for t in r.resample(tr)]
        return (np.concatenate(a) if a else np.zeros(0, np.float32)).astype(np.float32), p.rate


# --------------------------------------------------------------------------- un pas

def _textes(pas: dict, langue: str) -> list[str] | None:
    """Renvoie les textes des phrases du pas dans cette langue (``None`` si une phrase n'est pas traduite)."""
    res = []
    for ph in pas.get("phrases") or []:
        v = ph.get("texte")
        t = v.get(langue) if isinstance(v, dict) else v if langue is None else None
        if not t:
            return None
        res.append(" ".join(str(t).replace("**", "").split()))
    return res


def _silences(pas: dict, n: int) -> tuple[float, list[float], float]:
    """Renvoie les silences avant la première phrase, entre les phrases et après la dernière, proches de l'original."""
    ph = pas.get("phrases") or []
    borne = lambda x, a, b: max(a, min(b, x))
    if len(ph) == n and all(p.get("debut_s") is not None and p.get("fin_s") is not None for p in ph):
        avant = borne(ph[0]["debut_s"], 0.3, 1.0)
        entre = [borne(ph[k + 1]["debut_s"] - ph[k]["fin_s"], 0.25, 1.2) for k in range(n - 1)]
        apres = borne((pas.get("duree_s") or ph[-1]["fin_s"]) - ph[-1]["fin_s"], 0.6, 1.5)
        return avant, entre, apres
    return 0.5, [0.4] * max(0, n - 1), 0.8


def silences_pas(pas: dict, chap: dict, n: int, langue: str, src: str) -> tuple[float, list[float], float]:
    """Silences de la voix d'un pas : la pause de chaque phrase (``pause_s``, sinon celle du chapitre).

    Langue source : avant la première phrase et entre les phrases, les réglages de calage ; après la dernière, sa
    pause si elle est plus longue que la fin habituelle. Autre langue : les silences de la voix d'origine, sauf
    là où une pause est donnée (elle est rendue telle quelle).
    """
    reg = CAL.reglages(chap)
    pauses = [ph.get("pause_s") for ph in (pas.get("phrases") or [])][:n]
    pauses += [None] * (n - len(pauses))
    if langue == src:
        avant = float(reg["avant_s"])
        entre = [float(p) if p is not None else float(reg["pause_s"]) for p in pauses[:max(0, n - 1)]]
        apres = 0.8
    else:
        avant, entre, apres = _silences(pas, n)
        entre = [float(pauses[k]) if pauses[k] is not None else e for k, e in enumerate(entre)]
    if n and pauses[-1] is not None:
        apres = max(apres, float(pauses[-1]))
    return avant, entre, apres


def _pauses(pas: dict, chap: dict) -> str:
    """Pauses qui comptent dans l'empreinte d'une voix (vide s'il n'y en a pas : les anciennes voix restent bonnes)."""
    p = [ph.get("pause_s") for ph in pas.get("phrases") or []]
    defaut = (chap.get("calage") or {}).get("pause_s")
    return "" if all(x is None for x in p) and defaut is None else f"|pauses:{p}|{defaut}"


def synthetiser(textes: list[str], moteur, silences) -> tuple[np.ndarray, int, list[list[float]]]:
    """Synthétise les phrases une à une et les met bout à bout, séparées par les silences donnés.

    ``silences`` : ``(avant, [entre…], après)`` en secondes. Renvoie le son, son taux d'échantillonnage et,
    pour chaque phrase, ses instants ``[début, fin]`` en secondes.
    """
    avant, entre, apres = silences
    morceaux, temps, t, taux = [], [], avant, None
    for k, txt in enumerate(textes):
        a, r = moteur.dire(txt)
        taux = taux or r
        a = S.reechantillonner(a, r, taux)
        d = len(a) / taux
        temps.append([round(t, 2), round(t + d, 2)])
        morceaux.append(a)
        t += d + (entre[k] if k < len(entre) else 0)
    taux = taux or TAUX
    tout = [np.zeros(int(avant * taux), np.float32)]
    for k, a in enumerate(morceaux):
        tout.append(a)
        tout.append(np.zeros(int((entre[k] if k < len(entre) else apres) * taux), np.float32))
    return np.concatenate(tout), taux, temps


def _empreinte(textes: list[str], moteur: str, nom: str, vitesse: float, pauses: str = "") -> str:
    return hashlib.sha1(("\n".join(textes) + f"|{moteur}|{nom}|{vitesse}" + pauses).encode("utf-8")).hexdigest()[:12]


def voix_chapitre(yaml_chap: Path, langue: str, moteur: str = "piper", nom: str | None = None, vitesse: float = 1.0,
                  sections: set | None = None, refaire: bool = False, journal=print) -> int:
    """Synthétise la voix des pas d'un chapitre dans une langue et renvoie le nombre de pas synthétisés.

    ``nom`` : voix du moteur (défaut : ``VOIX_DEFAUT``) ; ``sections`` : identifiants de parties ou de sections
    à traiter (toutes par défaut). Les sons sont écrits dans ``audio/voix/<pas>.<langue>.wav`` ; si au moins un pas
    a été fait, le chapitre est sauvegardé dans ``sauvegardes/`` puis réécrit.
    """
    chap = F.lire(yaml_chap)
    dossier = yaml_chap.parent
    src = (chap.get("langues") or {}).get("source") or "fr"
    nom = nom or VOIX_DEFAUT.get(moteur, {}).get(langue.split("-")[0])
    if moteur != "essai" and not nom:
        raise SystemExit(f"Pas de voix par défaut pour {langue} avec {moteur} : la donner avec --voix")
    m = MOTEURS[moteur](nom, dossier.parent / "_voix", vitesse)
    n, manque = 0, []
    for p in chap.get("parties") or []:
        for s in p.get("sections") or []:
            if sections and p.get("id") not in sections and s.get("id") not in sections:
                continue
            for q in s.get("pas") or []:
                if q.get("ecarte"):
                    continue
                source = q.setdefault("source", {}) if langue == src else None
                if langue == src:
                    if q.get("audio") and source.get("voix") != "synthese":
                        continue                                # enregistrement de l'auteur : jamais remplacé
                    if not q.get("phrases") and F.texte(q.get("narration"), src).strip():
                        q["phrases"] = [{"texte": t} for t in F.decouper_phrases(F.texte(q.get("narration"), src))]
                    textes = [F.texte(ph.get("texte"), src) for ph in q.get("phrases") or []]
                    textes = [" ".join(t.replace("**", "").split()) for t in textes]
                else:
                    textes = _textes(q, langue)
                if not textes or not all(textes):
                    if langue != src and q.get("phrases"):
                        manque.append(q.get("id"))
                    continue
                emp = _empreinte(textes, moteur, nom or "", vitesse, _pauses(q, chap))
                deja = q.get("audio") if langue == src else ((q.get("voix") or {}).get(langue) or {}).get("audio")
                ancienne = source.get("voix_empreinte") if langue == src else ((q.get("voix") or {}).get(langue) or {}).get("empreinte")
                if deja and (dossier / deja).is_file() and ancienne == emp and not refaire:
                    continue
                sil = silences_pas(q, chap, len(textes), langue, src)
                a, taux, temps = synthetiser(textes, m, sil)
                rel = f"audio/voix/{q['id']}.{langue}.wav"
                S.ecrire_wav(dossier / rel, a, taux)
                duree = round(len(a) / taux, 2)
                if langue == src:
                    q["audio"], q["duree_s"] = rel, duree
                    for ph, (d, f) in zip(q["phrases"], temps):
                        ph["debut_s"], ph["fin_s"] = d, f
                    CAL.appliquer_pas(q, chap)                  # les objets accrochés suivent la nouvelle voix
                    q.pop("narration", None)
                    source.update({"voix": "synthese", "voix_moteur": moteur, "voix_nom": nom or moteur, "voix_empreinte": emp})
                else:
                    q.setdefault("voix", {})[langue] = {"audio": rel, "duree_s": duree, "phrases": temps, "moteur": moteur,
                                                         "nom": nom or moteur, "empreinte": emp,
                                                         "date": time.strftime("%Y-%m-%d")}
                n += 1
                journal(f"  {q['id']} ({langue}) : {len(textes)} phrase(s), {duree:.1f} s")
    if manque:
        journal(f"  {len(manque)} pas sans traduction complète en {langue} (non faits) : {', '.join(manque[:10])}"
                + (" …" if len(manque) > 10 else "") + f" — « capsuleforge traduire {dossier.name} --langue {langue} »")
    if n:
        (dossier / "sauvegardes").mkdir(exist_ok=True)
        shutil.copy2(yaml_chap, dossier / "sauvegardes" / f"chapitre_{time.strftime('%Y%m%d_%H%M%S')}.yaml")
        F.ecrire(chap, yaml_chap)
    journal(f"  {n} pas synthétisé(s) en {langue} ({moteur}{' · ' + nom if nom else ''})")
    return n


def recaler(t: float, src: list[list[float]], cible: list[list[float]], d_src: float, d_cible: float) -> float:
    """Convertit un instant du son d'origine en instant du son traduit (linéaire par morceaux entre les bornes des phrases)."""
    ax = [0.0] + [x for d, f in src for x in (d, f)] + [d_src]
    ay = [0.0] + [y for d, f in cible for y in (d, f)] + [d_cible]
    # bornes croissantes (phrases qui se chevauchent dans l'original)
    for i in range(1, len(ax)):
        ax[i], ay[i] = max(ax[i], ax[i - 1]), max(ay[i], ay[i - 1])
    return float(np.interp(t, ax, ay))
