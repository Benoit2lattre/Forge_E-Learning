"""CapsuleForge — raccourcis clavier et bips des enregistreurs (Windows).

Commun à l'enregistreur de didacticiel (``enregistrer``) et à l'enregistreur d'écran, de micro et de webcam
(``filmer``) : les bips de départ, de pause et de fin, la lecture des touches Ctrl, Maj, Alt et Windows
réellement enfoncées, et l'interception des raccourcis avant l'application enregistrée.

Les modificateurs sont lus dans l'état réel du clavier au moment de l'appui : une touche « restée enfoncée »
après un changement de fenêtre ne fausse pas le raccourci. Un raccourci intercepté n'arrive pas à l'application
enregistrée, et une touche maintenue enfoncée ne le répète pas.

Licence : GPL v3.
"""
from __future__ import annotations

import threading
import time

WM_CLAVIER = (0x100, 0x101, 0x104, 0x105)       # WM_KEYDOWN, WM_KEYUP, WM_SYSKEYDOWN, WM_SYSKEYUP
WM_RELACHE = (0x101, 0x105)


def son_bip(n: int = 1, frequence: int = 1000, duree_ms: int = 90, silence_ms: int = 60, taux: int = 22050) -> bytes:
    """Renvoie un fichier WAV (octets) de ``n`` bips courts séparés par un silence."""
    import io
    import math
    import struct
    import wave
    nb, ns = int(taux * duree_ms / 1000), int(taux * silence_ms / 1000)
    rampe = max(1, int(taux * 0.005))                     # 5 ms de montée et de descente : pas de claquement
    ton = b"".join(struct.pack("<h", int(12000 * min(1, i / rampe, (nb - i) / rampe) * math.sin(2 * math.pi * frequence * i / taux)))
                   for i in range(nb))
    pause = b"\0\0" * ns
    f = io.BytesIO()
    with wave.open(f, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(taux)
        w.writeframes(pause.join([ton] * n) + pause)
    return f.getvalue()


def bip(n: int = 1):
    """Signal sonore sans bloquer l'enregistrement : 1 = départ ou nouvelle étape, 2 = pause / reprise, 3 = fin.

    Joué par la sortie son habituelle de Windows (``winsound.PlaySound``) ; ``winsound.Beep``, muet sur
    beaucoup d'ordinateurs portables, ne sert plus qu'en secours.
    """
    def _jouer():
        try:
            import winsound
        except ImportError:
            return
        try:
            winsound.PlaySound(son_bip(n), winsound.SND_MEMORY | winsound.SND_NODEFAULT)
        except Exception:
            try:
                for _ in range(n):
                    winsound.Beep(1000, 90)
                    time.sleep(0.06)
            except Exception:
                pass
    threading.Thread(target=_jouer, daemon=True).start()


def modificateurs_enfonces() -> set:
    """Renvoie les modificateurs réellement enfoncés (Windows) : ``ctrl``, ``shift``, ``alt``, ``cmd``.

    Renvoie un ensemble vide hors de Windows.
    """
    try:
        import ctypes
        etat = ctypes.windll.user32.GetAsyncKeyState
    except Exception:
        return set()
    m = set()
    if etat(0x11) & 0x8000: m.add("ctrl")
    if etat(0x10) & 0x8000: m.add("shift")
    if etat(0x12) & 0x8000: m.add("alt")
    if (etat(0x5B) | etat(0x5C)) & 0x8000: m.add("cmd")
    return m


class Intercepteur:
    """Filtre Windows du clavier : exécute les raccourcis et les retire du flux.

    ``action_de(vk)`` reçoit le code virtuel d'une touche appuyée ou relâchée et renvoie la fonction à exécuter
    si c'est un raccourci (en lisant au besoin :func:`modificateurs_enfonces`), sinon ``None``. La fonction est
    exécutée une fois à l'appui ; l'appui et le relâchement de la touche ne parviennent pas à l'application.
    """

    def __init__(self, action_de):
        self.action_de = action_de
        self.ecouteur = None
        self._vk_bloque = None

    def filtre(self, msg, data):
        """Filtre passé à ``pynput`` (``win32_event_filter``)."""
        if msg not in WM_CLAVIER:
            return True
        vk = data.vkCode
        relache = msg in WM_RELACHE
        if relache and vk == self._vk_bloque:
            self._vk_bloque = None
            self.ecouteur.suppress_event()
        action = self.action_de(vk)
        if action is None:
            return True
        if not relache:
            if vk != self._vk_bloque:                       # pas de répétition si la touche reste enfoncée
                self._vk_bloque = vk
                action()
            self.ecouteur.suppress_event()
        return True

    def ecouteur_clavier(self, **rappels):
        """Crée l'écouteur ``pynput`` du clavier avec ce filtre (``rappels`` : ``on_press``, ``on_release``…).

        L'écouteur n'est pas démarré.
        """
        from pynput import keyboard
        self.ecouteur = keyboard.Listener(win32_event_filter=self.filtre, **rappels)
        return self.ecouteur
