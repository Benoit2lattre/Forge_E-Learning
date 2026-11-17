"""CapsuleForge — transcription de la narration enregistrée (Whisper, sur cet ordinateur).

Sert à reprendre un cours déjà enregistré sans scénario écrit : chaque audio de pas est transcrit, le texte
devient un premier jet de narration À RELIRE, et le minutage mot par mot est gardé dans ``transcriptions/`` pour
les sous-titres et le calage des apparitions. Rien ne quitte cet ordinateur (le modèle est téléchargé une fois).

Dépendance facultative : faster-whisper (``uv pip install faster-whisper``).
Licence : GPL v3.
"""
from __future__ import annotations

import json
from pathlib import Path

import format2 as F


def charger_modele(nom: str = "small"):
    """Charge et renvoie le modèle Whisper ``nom`` (faster-whisper, sur processeur, en int8)."""
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        raise SystemExit("La transcription demande faster-whisper :  uv pip install faster-whisper")
    return WhisperModel(nom, device="cpu", compute_type="int8")


def vocabulaire(chap: dict) -> str:
    """Renvoie les titres du chapitre (900 caractères au plus), donnés au modèle comme amorce.

    Les termes techniques sont ainsi mieux reconnus.
    """
    mots = [F.texte(chap.get("titre"))]
    for p in chap.get("parties") or []:
        mots.append(F.texte(p.get("titre")))
        mots += [F.texte(s.get("titre")) for s in p.get("sections") or []]
    return ". ".join(m for m in mots if m)[:900]


FREQ = 16000        # fréquence attendue par Whisper


def _reechantillonner(x, freq: int):
    """Ramène un signal mono float32 à 16 kHz : filtre passe-bas (sinus cardinal fenêtré) puis interpolation linéaire."""
    import numpy as np
    if freq == FREQ:
        return x.astype("float32")
    if freq > FREQ:                                    # éviter le repliement avant de réduire la cadence
        coupure, n = 0.45 * FREQ / freq, 101
        k = np.arange(n) - (n - 1) / 2
        h = 2 * coupure * np.sinc(2 * coupure * k) * np.hamming(n)
        x = np.convolve(x, h / h.sum(), mode="same")
    t = np.arange(int(len(x) * FREQ / freq)) * (freq / FREQ)
    return np.interp(t, np.arange(len(x)), x).astype("float32")


def charger_audio(chemin: Path):
    """Lit un fichier audio et renvoie un signal mono à 16 kHz (float32, entre -1 et 1).

    Les WAV sont lus sans bibliothèque externe ; les autres formats (mp3, m4a) passent par PyAV.
    On ne dépend pas du décodeur de faster-whisper, dont une version s'est révélée incompatible avec PyAV.
    """
    import numpy as np
    chemin = Path(chemin)
    if chemin.suffix.lower() == ".wav":
        import wave
        try:
            with wave.open(str(chemin)) as w:
                canaux, largeur, freq = w.getnchannels(), w.getsampwidth(), w.getframerate()
                brut = w.readframes(w.getnframes())
            if largeur == 2:
                x = np.frombuffer(brut, dtype="<i2").astype("float32") / 32768.0
            elif largeur == 1:
                x = (np.frombuffer(brut, dtype="u1").astype("float32") - 128.0) / 128.0
            elif largeur == 4:
                x = np.frombuffer(brut, dtype="<i4").astype("float32") / 2147483648.0
            else:
                raise ValueError(f"WAV sur {8 * largeur} bits")
            if canaux > 1:
                x = x.reshape(-1, canaux).mean(axis=1)
            return _reechantillonner(x, freq)
        except (wave.Error, ValueError):
            pass                                       # WAV compressé ou inhabituel : on passe par PyAV
    import av
    morceaux = []
    with av.open(str(chemin)) as conteneur:
        flux = conteneur.streams.audio[0]
        conv = av.AudioResampler(format="s16", layout="mono", rate=FREQ)
        for trame in conteneur.decode(flux):
            sorties = conv.resample(trame)
            for t in (sorties if isinstance(sorties, list) else [sorties]):
                if t is not None:
                    morceaux.append(t.to_ndarray().reshape(-1))
    if not morceaux:
        raise ValueError(f"aucun son lisible dans {chemin.name}")
    return np.concatenate(morceaux).astype("float32") / 32768.0


def transcrire_fichier(modele, audio: Path, langue: str, amorce: str) -> dict:
    """Transcrit un fichier audio et renvoie la transcription (segments horodatés, avec leurs mots).

    Le dictionnaire renvoyé contient ``audio``, ``langue``, ``duree_s`` et ``segments`` ; chaque segment a
    ``debut``, ``fin``, ``texte`` et ``mots``.
    """
    signal = charger_audio(audio)
    segments, info = modele.transcribe(signal, language=langue, initial_prompt=amorce or None,
                                       word_timestamps=True, vad_filter=True)
    out = []
    for s in segments:
        out.append({"debut": round(s.start, 2), "fin": round(s.end, 2), "texte": s.text.strip(),
                    "mots": [{"debut": round(w.start, 2), "fin": round(w.end, 2), "mot": w.word.strip()}
                             for w in (s.words or [])]})
    return {"audio": audio.name, "langue": langue, "duree_s": round(len(signal) / FREQ, 1), "segments": out}


def transcrire_chapitre(chap: dict, dossier: Path, modele, refaire: bool = False, sections: set | None = None,
                        journal=print) -> int:
    """Transcrit l'audio des pas sans narration (ou de tous avec ``refaire=True``) et renvoie le nombre de pas traités.

    Chaque transcription est écrite dans ``transcriptions/<pas>.json`` ; les phrases du pas sont remplacées
    par les segments reconnus, marqués à relire. Le chapitre (dictionnaire) est modifié sur place, pas écrit.
    """
    dossier = Path(dossier)
    (dossier / "transcriptions").mkdir(exist_ok=True)
    langue = (chap.get("langues") or {}).get("source", "fr")
    amorce = vocabulaire(chap)
    N = F.noms(chap)
    n = 0
    for partie in chap.get("parties") or []:
        for sec in partie.get("sections") or []:
            if sections and sec.get("id") not in sections and partie.get("id") not in sections:
                continue
            for pas in sec.get("pas") or []:
                audio = pas.get("audio")
                if not audio or pas.get("ecarte") or not (dossier / audio).is_file():
                    continue
                if F.narration_pas(pas).strip() and not refaire:
                    continue
                t = transcrire_fichier(modele, dossier / audio, langue, amorce)
                (dossier / "transcriptions" / f"{pas['id']}.json").write_text(
                    json.dumps(t, ensure_ascii=False, indent=1), encoding="utf-8")
                texte = " ".join(s["texte"] for s in t["segments"]).strip()
                pas.pop("narration", None)
                pas["phrases"] = phrases_des_segments(t)
                pas.setdefault("source", {})["narration"] = "transcription automatique, à relire"
                mots = len(texte.split())
                journal(f"  {N.get(('pas', pas['id']), pas['id'])} ({pas['id']}) : {mots} mots, "
                        f"{round(mots * 60 / max(1.0, t['duree_s']))} mots/min")
                n += 1
    return n


# --------------------------------------------------------------------------- phrases horodatées

def _norme(mot: str) -> str:
    import unicodedata
    s = unicodedata.normalize("NFD", mot.lower())
    return "".join(c for c in s if c.isalnum() and unicodedata.category(c) != "Mn")


def decouper_phrases(texte: str) -> list[str]:
    """Découpe un texte en phrases (règle commune : :func:`format2.decouper_phrases`)."""
    return F.decouper_phrases(texte)


def mots_du_fichier(transcription: dict) -> list[dict]:
    """Renvoie tous les mots horodatés d'une transcription, dans l'ordre."""
    return [m for s in transcription.get("segments") or [] for m in s.get("mots") or []]


def phrases_des_segments(transcription: dict) -> list[dict]:
    """Renvoie une phrase horodatée par segment reconnu (texte tel qu'il est dans la transcription)."""
    return [{"debut_s": s["debut"], "fin_s": s["fin"], "texte": s["texte"].strip()}
            for s in transcription.get("segments") or [] if s.get("texte", "").strip()]


def phrases_alignees(texte: str, transcription: dict) -> list[dict]:
    """Découpe un texte corrigé en phrases et donne à chacune son début et sa fin.

    Les mots de chaque phrase sont retrouvés parmi les mots horodatés de la transcription ; une phrase dont
    aucun mot n'est retrouvé est placée entre ses voisines.
    """
    import difflib
    phrases = decouper_phrases(texte)
    mots = [m for m in mots_du_fichier(transcription) if _norme(m["mot"])]
    if not phrases:
        return []
    if not mots:
        return [{"texte": p} for p in phrases]
    a, proprietaire = [], []                       # mots du texte corrigé et rang de leur phrase
    for i, p in enumerate(phrases):
        for m in p.split():
            if _norme(m):
                a.append(_norme(m)); proprietaire.append(i)
    b = [_norme(m["mot"]) for m in mots]
    paire = [None] * len(a)                        # rang du mot reconnu pour chaque mot du texte
    for bloc in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(bloc.size):
            paire[bloc.a + k] = bloc.b + k
    out = []
    for i, p in enumerate(phrases):
        rangs = [paire[k] for k in range(len(a)) if proprietaire[k] == i and paire[k] is not None]
        out.append({"debut_s": mots[rangs[0]]["debut"] if rangs else None,
                    "fin_s": mots[rangs[-1]]["fin"] if rangs else None, "texte": p})
    fin_audio = transcription.get("duree_s") or mots[-1]["fin"]
    for i, ph in enumerate(out):                   # phrases sans aucun mot retrouvé : entre leurs voisines
        if ph["debut_s"] is None:
            avant = out[i - 1]["fin_s"] if i else 0.0
            apres = next((x["debut_s"] for x in out[i + 1:] if x["debut_s"] is not None), fin_audio)
            ph["debut_s"], ph["fin_s"] = avant, apres
    for i in range(1, len(out)):                   # ordre strict
        out[i]["debut_s"] = max(out[i]["debut_s"], out[i - 1]["debut_s"])
        out[i - 1]["fin_s"] = min(max(out[i - 1]["fin_s"], out[i - 1]["debut_s"]), out[i]["debut_s"]) \
            if out[i - 1]["fin_s"] > out[i]["debut_s"] else out[i - 1]["fin_s"]
    for ph in out:
        ph["debut_s"], ph["fin_s"] = round(ph["debut_s"], 2), round(max(ph["fin_s"], ph["debut_s"]), 2)
    return out


def phrases_du_pas(pas: dict, dossier: Path) -> list[dict] | None:
    """Renvoie les phrases d'un pas qui n'en a pas encore (``None`` s'il n'y a rien).

    Par ordre de préférence : sa narration alignée sur sa transcription, sinon les segments de la
    transcription, sinon la narration découpée sans horodatage.
    """
    f = Path(dossier) / "transcriptions" / f"{pas.get('id')}.json"
    t = json.loads(f.read_text(encoding="utf-8")) if f.is_file() else None
    narration = F.texte(pas.get("narration")).strip()
    if narration and t:
        return phrases_alignees(narration, t)
    if t:
        return phrases_des_segments(t)
    if narration:
        return [{"texte": p} for p in decouper_phrases(narration)]
    return None
