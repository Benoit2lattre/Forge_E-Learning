"""CapsuleForge — petites fonctions sur les sons (signal mono en flottants entre -1 et 1).

Communes à la transcription, à la voix de synthèse et à l'import de vidéo.

Licence : GPL v3.
"""
from __future__ import annotations

import wave
from pathlib import Path

import numpy as np


def reechantillonner(a: np.ndarray, de: int, vers: int) -> np.ndarray:
    """Ramène un signal mono de la fréquence ``de`` à la fréquence ``vers`` (Hz) ; renvoie du float32.

    Pour réduire la fréquence, un filtre passe-bas (sinus cardinal fenêtré) évite le repliement ; puis
    interpolation linéaire.
    """
    a = np.asarray(a, dtype=np.float32)
    if de == vers or not len(a):
        return a
    if de > vers:                                      # éviter le repliement avant de réduire la cadence
        coupure, n = 0.45 * vers / de, 101
        k = np.arange(n) - (n - 1) / 2
        h = 2 * coupure * np.sinc(2 * coupure * k) * np.hamming(n)
        a = np.convolve(a, h / h.sum(), mode="same")
    t = np.arange(int(len(a) * vers / de)) * (de / vers)
    return np.interp(t, np.arange(len(a)), a).astype(np.float32)


def ecrire_wav(chemin: Path, a: np.ndarray, taux: int) -> None:
    """Écrit un son mono en WAV 16 bits (dossier créé au besoin ; valeurs hors de [-1, 1] écrêtées)."""
    chemin = Path(chemin)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(chemin), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(taux)
        w.writeframes((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes())
