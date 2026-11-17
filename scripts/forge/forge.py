"""Forge E-Learning — Atelier : une page dans le navigateur qui lance les outils Forge sans ligne de commande.

Double-clic sur ``Forge.bat`` (racine du dépôt), ou ``python scripts/forge/forge.py [--port 8770] [--sans-navigateur]``.

L'atelier ne refait aucun calcul : chaque bouton lance une commande Forge existante (``build.py``, ``capsuleforge``,
``quizforge``, ``diagforge``) dans un sous-processus et affiche son journal. Il ne lance que des actions connues, avec des
options vérifiées (jamais une ligne de commande libre). Le serveur n'écoute que sur cet ordinateur (127.0.0.1), refuse
les requêtes venues d'un autre site (``serveur_local``) et demande un jeton, tiré au lancement, pour toute action.

Routes :
  GET  /                      la page (``atelier.html``)
  GET  /api/etat              état du poste, profils, version
  GET  /api/exoforge/fiches   fiches ExoForge trouvées (exemples et data/exoforge)
  GET  /api/taches            résumé des tâches de la séance
  GET  /api/tache/<id>?depuis=n   lignes du journal d'une tâche à partir de la n-ième
  GET  /dist/<chemin>         fichiers construits (essayer un exercice, ouvrir un lecteur)
  POST /api/lancer            {action, params} : lance une tâche
  POST /api/arreter           {id} : arrête une tâche
  POST /api/parcourir         {dossier?, types?} : dialogue de fichiers de Windows, renvoie le chemin choisi
  POST /api/montrer           {chemin} : ouvre l'explorateur sur un fichier ou un dossier du dépôt
  POST /api/quitter           arrête l'atelier (refusé si une tâche tourne, sauf {forcer: true})
  POST /api/depart            la page se ferme : arrêt dans 4 s si elle ne revient pas et qu'aucune tâche ne tourne

Licence : GPL v3.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import secrets
import subprocess
import sys
import threading
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent / "commun"))
sys.path.insert(0, str(ICI.parent / "capsuleforge"))
import chemins                    # noqa: E402
import serveur_local as S         # noqa: E402

VERSION = "0.1"
RACINE = chemins.RACINE
PY = sys.executable
PORT = 8770
MAX_LIGNES = 5000                 # lignes gardées par tâche (les plus anciennes sont retirées)
TYPES = dict(S.TYPES, **{".svg": "image/svg+xml", ".woff": "font/woff", ".woff2": "font/woff2", ".ttf": "font/ttf",
                         ".mp4": "video/mp4", ".webm": "video/webm", ".xml": "application/xml", ".txt": "text/plain; charset=utf-8",
                         ".zip": "application/zip", ".pdf": "application/pdf", ".gif": "image/gif"})
WINDOWS = os.name == "nt"


def rel(p: Path) -> str:
    """Chemin relatif au dépôt, avec des « / » (sinon le chemin absolu)."""
    try:
        return Path(p).resolve().relative_to(RACINE).as_posix()
    except ValueError:
        return str(p)


def dans_depot(chemin: str) -> Path:
    """Chemin absolu d'un fichier du dépôt ; refuse ce qui sort du dépôt."""
    p = (RACINE / chemin).resolve() if not Path(chemin).is_absolute() else Path(chemin).resolve()
    if p != RACINE and RACINE not in p.parents:
        raise ValueError("chemin hors du dépôt")
    return p


# --------------------------------------------------------------------------------------------- tâches
class Tache:
    """Une commande Forge lancée par l'atelier : sous-processus, journal, état."""

    def __init__(self, ident: str, titre: str, outil: str, argv: list[str], verrou: str | None = None,
                 apres=None):
        self.id, self.titre, self.outil, self.argv, self.verrou = ident, titre, outil, argv, verrou
        self.apres = apres                     # fonction (tache) -> dict de liens, appelée à la fin si la tâche réussit
        self.lignes: list[str] = []
        self.retirees = 0                      # lignes retirées en tête (MAX_LIGNES)
        self.debut = time.time()
        self.fin: float | None = None
        self.code: int | None = None
        self.arretee = False
        self.liens: dict = {}
        self.proc: subprocess.Popen | None = None

    def lancer(self, quand_fini):
        env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1", PYTHONUNBUFFERED="1")
        options = {"creationflags": subprocess.CREATE_NO_WINDOW} if WINDOWS else {}
        self.ajouter("$ " + " ".join(["python"] + [rel(Path(a)) if Path(a).is_absolute() else a for a in self.argv[1:]]))
        try:
            self.proc = subprocess.Popen(self.argv, cwd=RACINE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                         stdin=subprocess.DEVNULL, env=env, text=True, encoding="utf-8",
                                         errors="replace", bufsize=1, **options)
        except OSError as e:
            self.ajouter(f"Lancement impossible : {e}")
            self.code, self.fin = -1, time.time()
            quand_fini(self)
            return

        def lire():
            for ligne in self.proc.stdout:
                self.ajouter(ligne.rstrip("\n"))
            self.code = self.proc.wait()
            self.fin = time.time()
            if self.code == 0 and self.apres:
                try:
                    self.liens = self.apres(self) or {}
                except Exception as e:                     # un lien manquant ne fait pas échouer la tâche
                    self.ajouter(f"(liens non trouvés : {e})")
            quand_fini(self)
        threading.Thread(target=lire, daemon=True).start()

    def ajouter(self, ligne: str):
        self.lignes.append(ligne)
        if len(self.lignes) > MAX_LIGNES:
            del self.lignes[:500]
            self.retirees += 500

    def arreter(self):
        if self.proc and self.proc.poll() is None:
            self.arretee = True
            self.proc.terminate()
            try:
                self.proc.wait(3)
            except subprocess.TimeoutExpired:
                self.proc.kill()

    @property
    def etat(self) -> str:
        if self.fin is None:
            return "en_cours"
        if self.arretee:
            return "arretee"
        return "reussie" if self.code == 0 else "echec"

    def resume(self) -> dict:
        return {"id": self.id, "titre": self.titre, "outil": self.outil, "etat": self.etat, "code": self.code,
                "debut": self.debut, "duree": (self.fin or time.time()) - self.debut,
                "lignes": self.retirees + len(self.lignes), "liens": self.liens}

    def depuis(self, n: int) -> dict:
        k = max(0, n - self.retirees)
        return {**self.resume(), "depuis": self.retirees + k, "nouvelles": self.lignes[k:]}


# --------------------------------------------------------------------------------------------- atelier
class Atelier:
    """État de la séance : tâches, jeton, arrêt."""

    def __init__(self):
        self.jeton = secrets.token_urlsafe(16)
        self.taches: dict[str, Tache] = {}
        self.ordre: list[str] = []
        self.verrou = threading.Lock()
        self.dialogue = threading.Lock()
        self.minuterie: threading.Timer | None = None
        self.page_partie_le: float | None = None
        self.arreter = lambda: None            # remplacé par srv.shutdown
        self.journal = chemins.DATA / "_atelier" / "journal.jsonl"
        self.actions = {"exoforge.construire": self.a_exo_construire}

    # ------------------------------------------------------------------ tâches
    def lancer(self, action: str, params: dict) -> dict:
        if action not in self.actions:
            raise ValueError(f"action inconnue : {action}")
        t = self.actions[action](params or {})
        with self.verrou:
            if t.verrou and any(x.verrou == t.verrou and x.etat == "en_cours" for x in self.taches.values()):
                return {"ok": False, "message": "Une tâche tourne déjà sur ce fichier : attendez sa fin ou arrêtez-la."}
            self.taches[t.id] = t
            self.ordre.append(t.id)
        t.lancer(self.tache_finie)
        return {"ok": True, "id": t.id}

    def nouvel_id(self) -> str:
        return f"t{len(self.ordre) + 1}"

    def tache_finie(self, t: Tache):
        try:
            self.journal.parent.mkdir(parents=True, exist_ok=True)
            with open(self.journal, "a", encoding="utf-8") as f:
                f.write(json.dumps({"date": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t.debut)),
                                    "titre": t.titre, "outil": t.outil, "commande": [rel(Path(a)) if Path(a).is_absolute() else a for a in t.argv[1:]], "etat": t.etat,
                                    "duree_s": round((t.fin or t.debut) - t.debut, 1)}, ensure_ascii=False) + "\n")
        except OSError:
            pass
        self.arret_si_parti()

    def en_cours(self) -> int:
        return sum(t.etat == "en_cours" for t in self.taches.values())

    # ------------------------------------------------------------------ ExoForge
    def fiches_exoforge(self) -> list[dict]:
        """Fiches ExoForge du dépôt : exemples publiés et data/exoforge (fiches privées)."""
        import yaml
        trouvees = []
        for base, origine in ((chemins.OUTILS / "exoforge" / "exemples", "exemple"), (chemins.DATA / "exoforge", "data")):
            if not base.is_dir():
                continue
            for f in sorted(base.rglob("*.y*ml")):
                if "media" in f.relative_to(base).parts or f.name.startswith("_"):
                    continue
                d = lire_fiche(f, yaml)
                if d:
                    trouvees.append({**d, "origine": origine})
        return trouvees

    def a_exo_construire(self, p: dict) -> Tache:
        f = Path(p.get("fiche") or "")
        f = f if f.is_absolute() else RACINE / f
        import yaml
        d = lire_fiche(f, yaml)
        if not d:
            raise ValueError("fiche ExoForge introuvable ou illisible")
        argv = [PY, str(chemins.SCRIPTS / "exoforge" / "build.py"), str(f)]
        profil = p.get("profil") or ""
        if profil:
            if profil not in noms_profils():
                raise ValueError(f"profil inconnu : {profil}")
            argv += ["--profil", profil]
        if p.get("auteur"):
            argv.append("--auteur")

        def liens(t):
            ident = d["id"]
            out = {}
            if (chemins.SORTIES / "exoforge" / ident / "index.html").is_file():
                out["essayer"] = f"/dist/exoforge/{ident}/index.html"
            z = chemins.SORTIES / "exoforge" / f"{ident}_scorm12.zip"
            if z.is_file():
                out["paquet"] = rel(z)
            return out
        return Tache(self.nouvel_id(), f"Construire « {d['titre']} »", "exoforge", argv,
                     verrou=str(f.resolve()), apres=liens)

    # ------------------------------------------------------------------ poste
    def etat_poste(self) -> list[dict]:
        def module(nom):
            try:
                return importlib.util.find_spec(nom) is not None
            except (ImportError, ValueError):
                return False
        lignes = [{"nom": "Python", "ok": sys.version_info >= (3, 10), "detail": sys.version.split()[0],
                   "sert": "tous les outils (3.10 ou plus)"}]
        for mod, nom, sert, utile in (("yaml", "PyYAML", "lire les fiches, chapitres et profils", True),
                                      ("openpyxl", "openpyxl", "classeurs QuizForge, bilans DiagForge", True),
                                      ("matplotlib", "matplotlib", "images des bilans DiagForge", True),
                                      ("av", "PyAV", "sons MP3 des lecteurs, vidéos, filmer", True),
                                      ("piper", "Piper", "voix de synthèse", False),
                                      ("faster_whisper", "faster-whisper", "transcrire la narration", False),
                                      ("comtypes", "comtypes", "images des diaporamas (PowerPoint)", False),
                                      ("pynput", "pynput", "raccourcis de filmer et enregistrer", False),
                                      ("argostranslate", "Argos Translate", "traduction hors ligne (facultatif)", False)):
            ok = module(mod)
            lignes.append({"nom": nom, "ok": ok, "facultatif": not utile, "detail": "installé" if ok else "absent",
                           "sert": sert})
        if WINDOWS:
            try:
                import winreg
                winreg.CloseKey(winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "PowerPoint.Application"))
                pp = True
            except OSError:
                pp = False
            lignes.append({"nom": "PowerPoint", "ok": pp, "facultatif": True, "detail": "installé" if pp else "absent",
                           "sert": "reprendre un diaporama avec ses images"})
        voix = sorted(v.stem for v in (chemins.DATA / "capsuleforge" / "_voix").glob("*.onnx"))
        lignes.append({"nom": "Voix Piper", "ok": bool(voix), "facultatif": True,
                       "detail": ", ".join(voix) if voix else "aucune téléchargée", "sert": "voix de synthèse hors ligne"})
        return lignes

    # ------------------------------------------------------------------ fichiers
    def parcourir(self, p: dict) -> dict:
        """Dialogue de fichiers du système (tkinter), au premier plan ; un seul à la fois."""
        if not self.dialogue.acquire(blocking=False):
            return {"ok": False, "message": "Un dialogue de fichiers est déjà ouvert."}
        try:
            import tkinter as tk
            from tkinter import filedialog
            racine = tk.Tk()
            racine.withdraw()
            racine.attributes("-topmost", True)
            depart = p.get("depart") or ""
            depart = str(dans_depot(depart)) if depart else str(RACINE)
            try:
                if p.get("dossier"):
                    choix = filedialog.askdirectory(parent=racine, initialdir=depart, title=p.get("titre") or "Choisir un dossier")
                else:
                    types = [(t[0], t[1]) for t in (p.get("types") or [])] + [("Tous les fichiers", "*.*")]
                    choix = filedialog.askopenfilename(parent=racine, initialdir=depart, filetypes=types,
                                                       title=p.get("titre") or "Choisir un fichier")
            finally:
                racine.destroy()
            if not choix:
                return {"ok": True, "chemin": None}
            return {"ok": True, "chemin": str(Path(choix)), "relatif": rel(Path(choix))}
        except Exception as e:                       # pas d'affichage (serveur sans écran), tkinter absent…
            return {"ok": False, "message": f"Dialogue de fichiers impossible : {e}"}
        finally:
            self.dialogue.release()

    def montrer(self, p: dict) -> dict:
        """Ouvre l'explorateur sur un fichier (sélectionné) ou un dossier du dépôt."""
        f = dans_depot(p.get("chemin") or "")
        if not f.exists():
            return {"ok": False, "message": "introuvable : " + rel(f)}
        if WINDOWS:
            if f.is_file():
                subprocess.Popen(["explorer", "/select,", str(f)])
            else:
                os.startfile(str(f))                     # noqa: S606 (dossier du dépôt)
        else:
            subprocess.Popen(["xdg-open", str(f if f.is_dir() else f.parent)])
        return {"ok": True}

    # ------------------------------------------------------------------ arrêt
    def page_partie(self):
        self.page_revenue()
        self.page_partie_le = time.time()
        self.minuterie = threading.Timer(4.0, self.arret_si_parti)
        self.minuterie.daemon = True
        self.minuterie.start()

    def page_revenue(self):
        self.page_partie_le = None
        if self.minuterie:
            self.minuterie.cancel()
            self.minuterie = None

    def arret_si_parti(self):
        """Arrête l'atelier si la page est partie depuis plus de 4 s et qu'aucune tâche ne tourne."""
        if self.page_partie_le and time.time() - self.page_partie_le >= 3.9 and not self.en_cours():
            threading.Thread(target=self.arreter, daemon=True).start()


def lire_fiche(f: Path, yaml) -> dict | None:
    """Résumé d'une fiche ExoForge (id, titre, profil, construction) ; ``None`` si ce n'en est pas une."""
    try:
        d = yaml.safe_load(f.read_text(encoding="utf-8"))
    except Exception:
        return None
    if not isinstance(d, dict) or not d.get("id") or not d.get("etapes"):
        return None
    ident = str(d["id"])
    page = chemins.SORTIES / "exoforge" / ident / "index.html"
    zipf = chemins.SORTIES / "exoforge" / f"{ident}_scorm12.zip"
    construit = page.stat().st_mtime if page.is_file() else None
    titre = d.get("titre") or ident
    if isinstance(titre, dict):
        titre = titre.get("fr") or next(iter(titre.values()), ident)
    titre = re.sub(r"^\s*(?:exercice|exercise)\s*:\s*", "", str(titre), flags=re.IGNORECASE) or ident
    titre = titre[:1].upper() + titre[1:]
    return {"id": ident, "titre": titre, "cours": str(d.get("cours") or ""), "profil": str(d.get("profil") or ""),
            "fiche": rel(f), "etapes": len(d.get("etapes") or []), "construit": construit,
            "a_refaire": bool(construit and f.stat().st_mtime > construit),
            "essayer": f"/dist/exoforge/{ident}/index.html" if construit else None,
            "paquet": rel(zipf) if zipf.is_file() else None}


def noms_profils() -> list[str]:
    noms = []
    for f in chemins.fichiers_profils():
        n = chemins.nom_profil(f)
        if n not in noms:
            noms.append(n)
    return noms


# --------------------------------------------------------------------------------------------- serveur
def gestionnaire(at: Atelier):
    class G(S.Gestionnaire):
        protocol_version = "HTTP/1.1"
        server_version = "Forge-Atelier"

        def _jeton_ok(self) -> bool:
            return secrets.compare_digest(self.headers.get("X-Jeton") or "", at.jeton)

        def get(self, chemin, url):
            if chemin in ("/", "/index.html"):
                at.page_revenue()
                return self._envoyer(200, (ICI / "atelier.html").read_bytes(), TYPES[".html"])
            if chemin.startswith("/dist/"):
                return self._dist(chemin[6:])
            if chemin.startswith("/static/"):
                return self._dans(chemins.STATIC, chemin[8:])
            if not chemin.startswith("/api/"):
                return self._introuvable()
            if not self._jeton_ok():
                return self._json({"ok": False, "message": "jeton absent ou faux : rouvrez l'atelier par Forge.bat"}, 403)
            at.page_revenue()
            if chemin == "/api/etat":
                return self._json({"ok": True, "version": VERSION, "racine": str(RACINE), "poste": at.etat_poste(),
                                   "profils": noms_profils(), "windows": WINDOWS})
            if chemin == "/api/exoforge/fiches":
                return self._json({"ok": True, "fiches": at.fiches_exoforge()})
            if chemin == "/api/taches":
                return self._json({"ok": True, "taches": [at.taches[i].resume() for i in at.ordre]})
            if chemin.startswith("/api/tache/"):
                t = at.taches.get(chemin[11:])
                if not t:
                    return self._introuvable()
                q = dict(x.split("=", 1) for x in (url.query or "").split("&") if "=" in x)
                return self._json({"ok": True, **t.depuis(int(q.get("depuis") or 0))})
            self._introuvable()

        def post(self, chemin, corps):
            if chemin == "/api/depart":                          # beacon : pas d'en-tête possible
                at.page_partie()
                return self._json({"ok": True})
            if not self._jeton_ok():
                return self._json({"ok": False, "message": "jeton absent ou faux : rouvrez l'atelier par Forge.bat"}, 403)
            at.page_revenue()
            p = json.loads(corps.decode("utf-8") or "{}")
            try:
                if chemin == "/api/lancer":
                    return self._json(at.lancer(p.get("action", ""), p.get("params") or {}))
                if chemin == "/api/arreter":
                    t = at.taches.get(p.get("id", ""))
                    if t:
                        t.arreter()
                    return self._json({"ok": bool(t)})
                if chemin == "/api/parcourir":
                    return self._json(at.parcourir(p))
                if chemin == "/api/montrer":
                    return self._json(at.montrer(p))
                if chemin == "/api/quitter":
                    if at.en_cours() and not p.get("forcer"):
                        return self._json({"ok": False, "en_cours": at.en_cours(),
                                           "message": "Des tâches tournent encore."})
                    for t in at.taches.values():
                        t.arreter()
                    self._json({"ok": True})
                    return threading.Thread(target=at.arreter, daemon=True).start()
            except ValueError as e:
                return self._json({"ok": False, "message": str(e)})
            self._introuvable()

        def _dans(self, base: Path, chemin: str):
            f = (base / chemin).resolve()
            if base.resolve() not in f.parents or not f.is_file():
                return self._introuvable()
            if f.suffix.lower() in (".mp3", ".wav", ".mp4", ".webm", ".m4a", ".ogg"):
                return self._media(f)
            self._envoyer(200, f.read_bytes(), TYPES.get(f.suffix.lower(), "application/octet-stream"))

        def _dist(self, chemin: str):
            return self._dans(chemins.SORTIES, chemin)

    return G


def main(argv=None):
    ap = argparse.ArgumentParser(description="Atelier Forge : lancer les outils Forge depuis le navigateur.")
    ap.add_argument("--port", type=int, default=PORT)
    ap.add_argument("--sans-navigateur", action="store_true", help="ne pas ouvrir la page (essais)")
    a = ap.parse_args(argv)
    at = Atelier()
    srv, adresse = S.demarrer(gestionnaire(at), a.port)
    at.arreter = srv.shutdown
    page = f"{adresse}?j={at.jeton}"
    print(f"Atelier Forge {VERSION} : {page}")
    print("Laisser cette fenêtre ouverte. Elle se ferme quand la page est fermée (ou par « Quitter » dans la page).")
    S.servir(srv, page, not a.sans_navigateur)
    for t in at.taches.values():
        t.arreter()
    print("Atelier fermé.")


if __name__ == "__main__":
    main()
