"""CapsuleForge — enregistreur de simulation logicielle (Windows).

Ce qu'il enregistre, comme ActivePresenter en mode « simulation interactive » :

- une image de l'écran juste avant chaque action (clic, double-clic, clic droit, glisser, molette,
  saisie au clavier, raccourci) ;
- la trajectoire de la souris depuis l'action précédente ;
- le contrôle visé, lu par l'accessibilité de Windows (UI Automation) : nom, type, rectangle.
  Si l'application n'expose rien (vue 3D, OpenGL…), le pas reste valide avec une zone par défaut.

Raccourcis pendant l'enregistrement (modifiables par options, ex. ``--touche-etape f8``) : ::

  Ctrl+Maj+E : nouvelle étape (le pas suivant ouvre une étape)        1 bip
  Ctrl+Maj+P : pause / reprise (avant de taper un mot de passe)       2 bips
  Ctrl+Maj+F : fin de l'enregistrement                                3 bips

Ils sont interceptés : l'application enregistrée ne les reçoit pas. Pas de touches F1-F12 par
défaut : sur les portables et claviers compacts, elles demandent Fn et commandent souvent le
système (mode avion, émojis…).

Sortie : ``<dossier>/journal.jsonl`` (écrit au fil de l'eau), ``<dossier>/images/pNNN.png``, puis
``<dossier>/capsule.yaml`` (assemblé à la fin ; à refaire avec « capsuleforge assembler » si besoin).

Dépendances (Windows) : pynput, mss, Pillow ; uiautomation facultatif (sans lui : pas de nom de contrôle).
Licence : GPL v3.
"""
from __future__ import annotations

import ctypes
import json
import queue
import sys
import threading
import time
from collections import deque
from datetime import date
from pathlib import Path

import assemblage as A
from raccourcis import Intercepteur, bip, modificateurs_enfonces

DOUBLE_CLIC_MS = 450         # deux clics plus rapprochés = double-clic
DOUBLE_CLIC_PX = 6
GLISSER_PX = 12              # déplacement bouton enfoncé au-delà duquel le clic devient un glisser
MOLETTE_REGROUPE_MS = 700    # crans de molette successifs = un seul pas
IMAGES_PAR_SECONDE = 8       # cadence de l'anneau de captures (image prise avant l'action)
SURVOL_MS = 120              # cadence de lecture de l'accessibilité sous la souris


def _dpi_physique():
    """Coordonnées en pixels physiques (écran à 150 % : la souris et les captures doivent concorder)."""
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(2)
    except Exception:
        try:
            ctypes.windll.user32.SetProcessDPIAware()
        except Exception:
            pass


def _echelle_ecran() -> float | None:
    """Renvoie l'échelle d'affichage de Windows (1.5 pour 150 %), ou ``None`` si elle n'est pas lisible."""
    try:
        return round(ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100, 2)
    except Exception:
        return None


class Enregistreur:
    """Enregistreur d'une manipulation : captures d'écran, souris, clavier et accessibilité de Windows.

    À la création, le dossier ``images/`` est créé et ``journal.jsonl`` ouvert en ajout dans ``dossier``.
    :meth:`lancer` déroule l'enregistrement jusqu'au raccourci de fin. ``ecran`` est le numéro d'écran de
    ``mss`` (1 = principal) ; ``touche_etape``, ``touche_pause`` et ``touche_fin`` sont des raccourcis au
    format de :func:`lire_raccourci` ; ``accessibilite=False`` désactive la lecture des noms de contrôles.
    """

    def __init__(self, dossier: Path, ecran: int = 1, titre: str | None = None, application: str | None = None,
                 touche_etape="ctrl+shift+e", touche_pause="ctrl+shift+p", touche_fin="ctrl+shift+f",
                 accessibilite: bool = True):
        import mss  # noqa: F401  (vérifie la présence avant de commencer)
        self.dossier = Path(dossier)
        (self.dossier / "images").mkdir(parents=True, exist_ok=True)
        self.journal = open(self.dossier / "journal.jsonl", "a", encoding="utf-8")
        self.num_ecran = ecran
        self.titre, self.application = titre, application
        self.touches = {"etape": touche_etape, "pause": touche_pause, "fin": touche_fin}
        self.raccourcis = {k: lire_raccourci(v) for k, v in self.touches.items()}
        self.kl = None
        self.intercepteur = Intercepteur(self._action_vk)
        self.avec_acc = accessibilite

        self.t0 = time.perf_counter()
        self.actif = True
        self.en_pause = False
        self.fini = threading.Event()
        self.verrou = threading.Lock()

        self.anneau = deque(maxlen=6)          # (t_ms, octets BGRA, (l, h))
        self.survol = None                     # (t_ms, x, y, cible) : dernière lecture d'accessibilité
        self.trajet: list[list[float]] = []
        self.dernier_point = None
        self.n = 0
        self.dernier_clic = None               # (t, x, y, bouton, id) pour reconnaître le double-clic
        self.appui = None                      # (t, x, y, bouton, image, cible) au moment du bouton enfoncé
        self.saisie = None                     # dict en cours de saisie clavier
        self.molette = None                    # dict en cours de molette
        self.modifs = set()
        self.a_ecrire: queue.Queue = queue.Queue()
        self.demandes: queue.Queue = queue.Queue()   # (id, x, y) : contrôle à relire après coup
        self.verrou_journal = threading.Lock()
        self.moniteur = None

    # ------------------------------------------------------------------ temps, journal, images
    def t(self) -> int:
        """Renvoie le temps écoulé depuis la création de l'enregistreur, en millisecondes."""
        return int((time.perf_counter() - self.t0) * 1000)

    def ecrire(self, evt: dict):
        """Ajoute un événement au journal (une ligne JSON), écrit immédiatement sur le disque."""
        with self.verrou_journal:
            self.journal.write(json.dumps(evt, ensure_ascii=False) + "\n")
            self.journal.flush()

    def _boucle_captures(self):
        """Capture l'écran en continu (hors pause) dans l'anneau des dernières images."""
        import mss
        with mss.mss() as sct:
            mon = sct.monitors[self.num_ecran]
            self.moniteur = mon
            pas_s = 1.0 / IMAGES_PAR_SECONDE
            while not self.fini.is_set():
                debut = time.perf_counter()
                if not self.en_pause:
                    img = sct.grab(mon)
                    self.anneau.append((self.t(), bytes(img.bgra), img.size))
                time.sleep(max(0.0, pas_s - (time.perf_counter() - debut)))

    def image_avant(self, t_evt: int):
        """Renvoie la dernière image de l'anneau prise avant l'instant ``t_evt`` (en ms).

        Renvoie le couple (octets BGRA, (largeur, hauteur)) ; à défaut la plus ancienne image de l'anneau, ou
        ``None`` si l'anneau est vide.
        """
        for t_img, octets, taille in reversed(self.anneau):
            if t_img <= t_evt:
                return octets, taille
        return (self.anneau[0][1], self.anneau[0][2]) if self.anneau else None

    def _boucle_ecriture(self):
        """Écrit en PNG les images mises en file, jusqu'à recevoir ``None``."""
        from PIL import Image
        while True:
            item = self.a_ecrire.get()
            if item is None:
                break
            chemin, octets, taille = item
            try:
                Image.frombuffer("RGB", taille, octets, "raw", "BGRX").save(self.dossier / chemin, optimize=True)
            except Exception as exc:                       # une image perdue ne doit pas arrêter l'enregistrement
                print(f"  ! image {chemin} non écrite : {exc}")

    def sauver_image(self, nom: str, img) -> str | None:
        """Met l'image en file d'écriture sous ``images/<nom>.png`` ; renvoie ce chemin relatif, ou ``None`` sans image."""
        if img is None:
            return None
        chemin = f"images/{nom}.png"
        self.a_ecrire.put((chemin, img[0], img[1]))
        return chemin

    # ------------------------------------------------------------------ accessibilité
    def _boucle_survol(self):
        """Lit régulièrement le contrôle sous la souris et complète les cibles des pas restés sans cible."""
        if not self.avec_acc:
            return
        try:
            import uiautomation as auto
        except ImportError:
            print("  (uiautomation absent : les bulles seront génériques ; uv pip install uiautomation)")
            self.avec_acc = False
            return
        with auto.UIAutomationInitializerInThread(debug=False):
            while not self.fini.is_set():
                # d'abord les clics restés sans cible (souris pas encore immobile au moment du clic)
                while not self.demandes.empty():
                    d = self.demandes.get()
                    if d[0] == "focus":
                        # saisie au clavier : la cible est le champ qui a le focus, pas ce qui est sous la souris
                        sa = d[1]
                        try:
                            c = self._lire_controle(auto, 0, 0, auto.GetFocusedControl())
                        except Exception:
                            c = None
                        if c:
                            if sa.get("pid"):
                                self.ecrire({"e": "modif", "id": sa["pid"], "cible": self.cible_rel(c)})
                            else:
                                sa["cible"] = c
                        continue
                    pid, x, y = d
                    c = self._lire_controle(auto, x, y)
                    if c:
                        self.ecrire({"e": "modif", "id": pid, "cible": self.cible_rel(c)})
                if not self.en_pause and self.dernier_point:
                    x, y = self.dernier_point
                    self.survol = (self.t(), x, y, self._lire_controle(auto, x, y))
                time.sleep(SURVOL_MS / 1000)

    def _lire_controle(self, auto, x, y, c=None):
        """Décrit le contrôle au point (x, y), ou le contrôle ``c`` donné ; ``None`` si la lecture échoue."""
        try:
            c = c or auto.ControlFromPoint(int(x), int(y))
            if c is None:
                return None
            r = c.BoundingRectangle
            nom = (c.Name or "").strip()
            # un élément sans nom (icône seule) : on remonte au parent s'il est petit et nommé
            if not nom:
                p = c.GetParentControl()
                if p is not None and (p.Name or "").strip():
                    pr = p.BoundingRectangle
                    if (pr.right - pr.left) * (pr.bottom - pr.top) < 4 * max(1, (r.right - r.left) * (r.bottom - r.top)):
                        c, r, nom = p, pr, p.Name.strip()
            out = {"nom": nom, "type": c.ControlTypeName,
                   "cadre_abs": [r.left, r.top, r.right - r.left, r.bottom - r.top],
                   "origine": "accessibilite"}
            try:                                            # fenêtre et programme : repérer la barre des tâches, etc.
                haut = c.GetTopLevelControl()
                if haut is not None:
                    out["fenetre"] = (haut.Name or "").strip()[:80]
                    out["classe"] = haut.ClassName or ""
                out["processus"] = nom_processus(c.ProcessId)
            except Exception:
                pass
            return out
        except Exception:
            return None

    def cible_au_point(self, x, y, t_evt):
        """Renvoie une copie de la dernière cible lue sous la souris si elle est récente et proche du point.

        La lecture doit dater de moins de 1,5 s et être à 4 px au plus de (x, y) ; sinon renvoie ``None``.
        """
        s = self.survol
        if s and abs(s[1] - x) <= 4 and abs(s[2] - y) <= 4 and t_evt - s[0] < 1500 and s[3]:
            return dict(s[3])
        return None

    # ------------------------------------------------------------------ conversions de coordonnées
    def rel(self, x, y):
        """Convertit des coordonnées d'écran absolues en coordonnées relatives à l'écran enregistré."""
        m = self.moniteur or {"left": 0, "top": 0}
        return [int(x - m["left"]), int(y - m["top"])]

    def cible_rel(self, cible):
        """Renvoie une copie de la cible avec ``cadre_abs`` remplacé par ``cadre`` en coordonnées relatives."""
        if not cible:
            return None
        c = dict(cible)
        if c.get("cadre_abs"):
            x, y, l, h = c.pop("cadre_abs")
            c["cadre"] = self.rel(x, y) + [l, h]
        return c

    # ------------------------------------------------------------------ pas
    def nouveau_pas(self, action, x, y, t_evt, img, cible, **extra) -> str:
        """Écrit un pas dans le journal (image, point, trajet, cible) et renvoie son identifiant (``p001``…).

        Les champs de ``extra`` sont ajoutés tels quels à l'événement. Un clic sans cible est mis en file pour
        être relu par l'accessibilité après coup.
        """
        self.n += 1
        pid = f"p{self.n:03d}"
        image = self.sauver_image(pid, img)
        evt = {"e": "pas", "id": pid, "action": action, "image": image, "point": self.rel(x, y),
               "trajet": [self.rel(px, py) + [pt] for px, py, pt in self.trajet],
               "cible": self.cible_rel(cible) or {"origine": "aucune"}, "t": t_evt}
        evt.update(extra)
        self.ecrire(evt)
        self.recents = [x for x in getattr(self, "recents", []) if time.monotonic() - x[2] < 5] + [(pid, action, time.monotonic())]
        if cible is None and self.avec_acc and action not in ("saisie", "touche"):
            self.demandes.put((pid, x, y))
        self.trajet = [[x, y, t_evt]]
        print(f"  {pid} {action:<11} {(cible or {}).get('nom', '') or ''}"[:78])
        return pid

    def vider_saisie(self):
        """Termine la saisie au clavier en cours et l'écrit comme pas « saisie » si elle contient du texte."""
        s, self.saisie = self.saisie, None
        if s and s["texte"]:
            s["pid"] = self.nouveau_pas("saisie", s["x"], s["y"], s["t"], s["img"], s.get("cible"), texte=s["texte"])

    def vider_molette(self):
        """Termine la série de crans de molette en cours et l'écrit comme pas « molette »."""
        m, self.molette = self.molette, None
        if m:
            self.nouveau_pas("molette", m["x"], m["y"], m["t"], m["img"], m["cible"], crans=m["crans"])

    # ------------------------------------------------------------------ souris
    def on_move(self, x, y):
        """Suit la souris (rappel de ``pynput``) : dernier point et trajet depuis l'action précédente."""
        if self.en_pause:
            return
        self.dernier_point = (x, y)
        t = self.t()
        if not self.trajet or abs(self.trajet[-1][0] - x) + abs(self.trajet[-1][1] - y) >= 6 or t - self.trajet[-1][2] > 80:
            self.trajet.append([x, y, t])

    def on_click(self, x, y, bouton, enfonce):
        """Traite un appui ou un relâchement de bouton (rappel de ``pynput``).

        Au relâchement, écrit un pas « glisser », « clic », « clic_droit » ou « clic_milieu » ; un second clic
        gauche rapproché transforme le pas précédent en « double_clic ».
        """
        if self.en_pause or not self.actif:
            return
        t = self.t()
        nom_b = getattr(bouton, "name", str(bouton))
        with self.verrou:
            if enfonce:
                self.vider_saisie()
                self.vider_molette()
                self.appui = (t, x, y, nom_b, self.image_avant(t), self.cible_au_point(x, y, t))
                return
            if not self.appui:
                return
            t0, x0, y0, b0, img, cible = self.appui
            self.appui = None
            if abs(x - x0) + abs(y - y0) > GLISSER_PX:
                self.nouveau_pas("glisser", x0, y0, t0, img, cible, arrivee=self.rel(x, y), bouton=b0)
                self.dernier_clic = None
                return
            action = {"left": "clic", "right": "clic_droit", "middle": "clic_milieu"}.get(b0, "clic")
            dc = self.dernier_clic
            if (action == "clic" and dc and dc[3] == "left" and t0 - dc[0] <= DOUBLE_CLIC_MS
                    and abs(x0 - dc[1]) <= DOUBLE_CLIC_PX and abs(y0 - dc[2]) <= DOUBLE_CLIC_PX):
                # le pas précédent devient un double-clic (on garde son image, prise avant le 1er clic)
                self.ecrire({"e": "modif", "id": dc[4], "action": "double_clic"})
                print(f"  {dc[4]} -> double_clic")
                self.dernier_clic = None
                return
            pid = self.nouveau_pas(action, x0, y0, t0, img, cible)
            self.dernier_clic = (t0, x0, y0, b0, pid)

    def on_scroll(self, x, y, dx, dy):
        """Regroupe les crans de molette successifs au même endroit en un seul pas (rappel de ``pynput``)."""
        if self.en_pause or not self.actif:
            return
        t = self.t()
        with self.verrou:
            self.vider_saisie()
            m = self.molette
            if m and t - m["dernier"] <= MOLETTE_REGROUPE_MS and abs(x - m["x"]) + abs(y - m["y"]) < 40:
                m["crans"] += int(dy)
                m["dernier"] = t
            else:
                self.vider_molette()
                self.molette = {"x": x, "y": y, "t": t, "dernier": t, "crans": int(dy),
                                "img": self.image_avant(t), "cible": self.cible_au_point(x, y, t)}

    # ------------------------------------------------------------------ clavier
    def _nom_touche(self, key) -> str:
        """Renvoie le nom d'une touche ``pynput`` (nom spécial, caractère ou lettre du code virtuel)."""
        nom = getattr(key, "name", None)
        if nom:
            return nom
        ch = getattr(key, "char", None)
        if ch and ch.isprintable():
            return ch
        vk = getattr(key, "vk", None)
        if vk and 0x30 <= vk <= 0x5A:
            return chr(vk).lower()
        return str(key)

    # ------------------------------------------------------------------ raccourcis de l'enregistreur
    def _quel_raccourci(self, nom: str, mods: set) -> str | None:
        """Renvoie l'action de l'enregistreur (« etape », « pause », « fin ») associée à la touche, ou ``None``."""
        for action, (m, touche) in self.raccourcis.items():
            if nom == touche and set(m) == set(mods):
                return action
        return None

    def _faire(self, action: str):
        """Exécute une action de l'enregistreur : fin, pause / reprise ou nouvelle étape."""
        if action == "fin":
            bip(3)
            self.terminer()
        elif action == "pause":
            self.en_pause = not self.en_pause
            self.trajet = []
            bip(2)
            print("  -- pause --" if self.en_pause else "  -- reprise --")
        elif action == "etape" and not self.en_pause and self.actif:
            with self.verrou:
                self.vider_saisie(); self.vider_molette()
                self.ecrire({"e": "etape", "t": self.t()})
            bip(1)
            print("  ---- nouvelle étape ----")

    def _commandes(self):
        """Lit l'entrée : une ligne « etape » ou « pause » fait l'action, toute autre ligne (ou la fin de l'entrée)
        termine — l'Atelier Forge envoie « fin », y compris par son bouton Arrêter."""
        try:
            for ligne in sys.stdin:
                if not self.actif:
                    return
                cmd = ligne.strip().lower()
                for pid, action, quand in getattr(self, "recents", []):   # clics pour revenir à l'atelier et sur son bouton :
                    if action == "clic" and time.monotonic() - quand < 3:     # écartés de la capsule
                        self.ecrire({"e": "modif", "id": pid, "ignorer": True, "raison": "clic dans l'Atelier Forge (bouton de l'enregistrement)"})
                self.recents = []
                if cmd in ("etape", "pause"):
                    self._faire(cmd)
                else:
                    self._faire("fin")
                    return
        except (OSError, ValueError):
            pass

    def _action_vk(self, vk: int):
        """Renvoie l'action à exécuter si la touche ``vk``, avec les modificateurs enfoncés, est un raccourci de
        l'enregistreur (voir :class:`raccourcis.Intercepteur`), sinon ``None``."""
        nom = nom_vk(vk)
        if nom is None:
            return None
        action = self._quel_raccourci(nom, modificateurs_enfonces())
        return None if action is None else (lambda: self._faire(action))

    def on_press(self, key):
        """Traite l'appui d'une touche (rappel de ``pynput``).

        Les caractères s'accumulent dans la saisie en cours ; une touche spéciale ou un raccourci devient un pas
        « touche ». Renvoie ``False`` (arrêt de l'écoute) sur le raccourci de fin.
        """
        nom = self._nom_touche(key)
        if nom in MODIFICATEURS:                    # suivis même en pause (pour reconnaître la reprise)
            self.modifs.add(nom.split("_")[0])
            return
        # secours si le filtre Windows n'a pas intercepté le raccourci
        action = self._quel_raccourci(nom, {m for m in self.modifs})
        if action:
            self._faire(action)
            return False if action == "fin" else None
        if self.en_pause or not self.actif:
            return
        t = self.t()
        with self.verrou:
            mods = [m for m in ("ctrl", "alt", "cmd") if m in self.modifs]
            ch = getattr(key, "char", None)
            if not mods and ch and ch.isprintable():
                if self.saisie is None:
                    x, y = self.dernier_point or (0, 0)
                    self.saisie = {"x": x, "y": y, "t": t, "texte": "", "img": self.image_avant(t), "cible": None}
                    if self.avec_acc:
                        self.demandes.put(("focus", self.saisie))
                self.saisie["texte"] += ch
                return
            if nom == "backspace" and self.saisie:
                self.saisie["texte"] = self.saisie["texte"][:-1]
                return
            if nom == "space" and self.saisie is not None and not mods:
                self.saisie["texte"] += " "
                return
            # touche spéciale ou raccourci : termine la saisie en cours et devient un pas « touche »
            self.vider_saisie(); self.vider_molette()
            libelle = "+".join([{"ctrl": "Ctrl", "alt": "Alt", "cmd": "Win"}[m] for m in mods]
                               + [NOMS_TOUCHES.get(nom, nom.upper() if len(nom) == 1 else nom)])
            x, y = self.dernier_point or (0, 0)
            self.nouveau_pas("touche", x, y, t, self.image_avant(t), None, touches=libelle)

    def on_release(self, key):
        """Retire un modificateur relâché de l'ensemble suivi (rappel de ``pynput``)."""
        nom = self._nom_touche(key)
        for m in ("ctrl", "alt", "cmd", "shift"):
            if nom.startswith(m):
                self.modifs.discard(m)

    # ------------------------------------------------------------------ déroulement
    def terminer(self):
        """Termine l'enregistrement : vide la saisie et la molette en cours, écrit l'événement « fin » et son image."""
        if not self.actif:
            return
        self.actif = False
        with self.verrou:
            self.vider_saisie(); self.vider_molette()
            t = self.t()
            img = self.image_avant(t)
            self.ecrire({"e": "fin", "t": t, "image": self.sauver_image("fin", img)})
        self.fini.set()

    def lancer(self, compte_a_rebours: int = 3):
        """Déroule l'enregistrement : fils de capture, compte à rebours, écoute de la souris et du clavier.

        Bloque jusqu'au raccourci de fin, attend l'écriture des images puis ferme le journal.
        """
        from pynput import mouse
        _dpi_physique()
        th_cap = threading.Thread(target=self._boucle_captures, daemon=True)
        th_ecr = threading.Thread(target=self._boucle_ecriture, daemon=True)
        th_acc = threading.Thread(target=self._boucle_survol, daemon=True)
        th_cap.start(); th_ecr.start(); th_acc.start()
        while self.moniteur is None:
            time.sleep(0.05)
        m = self.moniteur
        self.ecrire({"e": "debut", "t": 0, "date": date.today().isoformat(), "titre": self.titre,
                     "application": self.application, "langue": "fr",
                     "ecran": {k: v for k, v in {"largeur": m["width"], "hauteur": m["height"],
                                                  "echelle": _echelle_ecran()}.items() if v}})
        print(f"Écran {self.num_ecran} : {m['width']}×{m['height']} px.\n"
              f"  {libelle_raccourci(self.touches['etape']):<14} nouvelle étape (1 bip)\n"
              f"  {libelle_raccourci(self.touches['pause']):<14} pause / reprise (2 bips)\n"
              f"  {libelle_raccourci(self.touches['fin']):<14} fin (3 bips)")
        if any(lire_raccourci(t)[1].startswith("f") and lire_raccourci(t)[1][1:].isdigit() for t in self.touches.values()):
            print("  Touches F : sur un portable ou un clavier compact, appuyer sur Fn+F8 (ou activer Verr Fn) ;\n"
                  "  vérifier d'abord que la touche ne commande pas le système (mode avion, émojis…).")
        for i in range(compte_a_rebours, 0, -1):
            print(f"  début dans {i} s… (passez dans l'application)")
            time.sleep(1)
        print("  ● enregistrement")
        self.trajet = []
        if not sys.stdin.isatty():                    # lancé par l'Atelier Forge : boutons Étape, Pause, Fin
            threading.Thread(target=self._commandes, daemon=True).start()
        kl = self.intercepteur.ecouteur_clavier(on_press=self.on_press, on_release=self.on_release)
        self.kl = kl
        with mouse.Listener(on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll):
            kl.start()
            self.fini.wait()
            kl.stop()
        self.a_ecrire.put(None)
        th_ecr.join(timeout=30)
        self.journal.close()


_PROCESSUS: dict = {}


def nom_processus(pid: int) -> str:
    """Nom de l'exécutable d'un processus (FreeCAD.exe, explorer.exe…), sans dépendance externe."""
    if pid in _PROCESSUS:
        return _PROCESSUS[pid]
    nom = ""
    try:
        k32 = ctypes.windll.kernel32
        h = k32.OpenProcess(0x1000, False, int(pid))         # PROCESS_QUERY_LIMITED_INFORMATION
        if h:
            buf = ctypes.create_unicode_buffer(1024)
            n = ctypes.c_ulong(1024)
            if k32.QueryFullProcessImageNameW(h, 0, buf, ctypes.byref(n)):
                nom = buf.value.replace("/", "\\").split("\\")[-1]
            k32.CloseHandle(h)
    except Exception:
        pass
    _PROCESSUS[pid] = nom
    return nom


def lire_raccourci(texte: str):
    """Analyse un raccourci écrit en texte et renvoie le couple (modificateurs, touche).

    Accepte « Ctrl+Maj+E », « ctrl+shift+e », « F8 » et des variantes d'écriture ; les modificateurs sont
    rendus sous la forme ``ctrl``, ``shift``, ``alt`` ou ``cmd`` et la touche en minuscules.
    """
    alias = {"ctrl": "ctrl", "ctl": "ctrl", "control": "ctrl", "controle": "ctrl", "contrôle": "ctrl",
             "shift": "shift", "maj": "shift", "majuscule": "shift", "alt": "alt",
             "win": "cmd", "windows": "cmd", "cmd": "cmd"}
    morceaux = [m.strip().lower() for m in texte.replace("-", "+").split("+") if m.strip()]
    mods = frozenset(alias[m] for m in morceaux[:-1] if m in alias)
    return mods, morceaux[-1] if morceaux else ""


def libelle_raccourci(texte: str) -> str:
    """Renvoie le libellé affichable d'un raccourci (ex. « Ctrl+Maj+E »)."""
    mods, t = lire_raccourci(texte)
    noms = [n for k, n in (("ctrl", "Ctrl"), ("alt", "Alt"), ("shift", "Maj"), ("cmd", "Win")) if k in mods]
    return "+".join(noms + [t.upper()])


def nom_vk(vk: int) -> str | None:
    """Renvoie le nom d'un code de touche virtuelle Windows au format de :func:`lire_raccourci`.

    Seuls les lettres, chiffres et touches F1 à F24 sont reconnus ; renvoie ``None`` pour les autres.
    """
    if 0x41 <= vk <= 0x5A or 0x30 <= vk <= 0x39:
        return chr(vk).lower()
    if 0x70 <= vk <= 0x87:
        return f"f{vk - 0x6F}"
    return None


MODIFICATEURS = ("ctrl_l", "ctrl_r", "ctrl", "alt_l", "alt_r", "alt_gr", "alt", "cmd", "cmd_l", "cmd_r",
                 "shift", "shift_l", "shift_r")

NOMS_TOUCHES = {"enter": "Entrée", "tab": "Tab", "esc": "Échap", "delete": "Suppr", "backspace": "Retour arrière",
                "up": "Haut", "down": "Bas", "left": "Gauche", "right": "Droite", "home": "Début", "end": "Fin",
                "page_up": "Page préc.", "page_down": "Page suiv.", "space": "Espace", "insert": "Inser"}


def enregistrer(dossier: Path, **options) -> Path:
    """Enregistre une manipulation dans ``dossier`` puis assemble la capsule ; renvoie le chemin de ``capsule.yaml``.

    Les ``options`` sont passées à :class:`Enregistreur`. Fonctionne sous Windows seulement et refuse un dossier
    qui contient déjà un enregistrement (``SystemExit``).
    """
    if sys.platform != "win32":
        raise SystemExit("L'enregistreur fonctionne sous Windows (souris, clavier et accessibilité de Windows).")
    dossier = Path(dossier)
    if (dossier / "capsule.yaml").exists() or (dossier / "chapitre.yaml").exists():
        raise SystemExit(f"{dossier} contient déjà une capsule : choisir un autre nom.")
    if (dossier / "journal.jsonl").exists():          # enregistrement interrompu (fenêtre fermée, tâche arrêtée) :
        rebut = dossier / f"_interrompu_{time.strftime('%Y%m%d_%H%M%S')}"   # mis de côté, on recommence
        rebut.mkdir()
        for f in list(dossier.iterdir()):
            if f != rebut and not f.name.startswith("_interrompu_"):
                f.rename(rebut / f.name)
        print(f"Enregistrement interrompu précédent mis de côté dans {rebut.name}/")
    rec = Enregistreur(dossier, **options)
    rec.lancer()
    cap = A.assembler(A.lire_journal(dossier / "journal.jsonl"), titre=options.get("titre"))
    A.ecrire_yaml(cap, dossier / "capsule.yaml")
    return dossier / "capsule.yaml"
