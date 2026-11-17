"""CapsuleForge — petit serveur local commun aux écrans ouverts dans le navigateur.

L'éditeur de capsule (``editer``), la relecture d'un chapitre (``relire``) et la relecture d'une traduction
(``traduire --relire``) passent tous par ce module : un serveur qui n'écoute que sur cet ordinateur (127.0.0.1),
refuse les requêtes venues d'un autre site ouvert dans le navigateur et sert la page, ses données et ses fichiers.

Chaque écran définit une sous-classe de :class:`Gestionnaire` avec ses méthodes ``get`` et ``post`` ; ce module
fournit le reste : envoi des réponses, fichiers, sons avec lecture partielle, choix du port, boucle du serveur.

Licence : GPL v3.
"""
from __future__ import annotations

import json
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

TYPES = {".html": "text/html; charset=utf-8", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
         ".webp": "image/webp", ".json": "application/json", ".mp3": "audio/mpeg", ".wav": "audio/wav",
         ".m4a": "audio/mp4", ".ogg": "audio/ogg", ".js": "text/javascript", ".css": "text/css"}
HOTES = ("127.0.0.1", "localhost")


def type_de(f: Path) -> str:
    """Type MIME d'un fichier d'après son extension."""
    return TYPES.get(Path(f).suffix.lower(), "application/octet-stream")


class Gestionnaire(BaseHTTPRequestHandler):
    """Gestionnaire HTTP de base des écrans de CapsuleForge.

    Une sous-classe définit ``get(chemin, url)`` et ``post(chemin, corps)`` ; un chemin inconnu reçoit 404.
    Une erreur levée dans ces méthodes est renvoyée à la page en JSON (``{"ok": false, "message": …}``, code 500).
    """
    server_version = "CapsuleForge"

    def log_message(self, *a):          # console silencieuse
        pass

    # ----------------------------------------------------------------- réponses
    def _envoyer(self, code: int, corps: bytes, type_: str, entetes: dict | None = None):
        self.send_response(code)
        self.send_header("Content-Type", type_)
        self.send_header("Content-Length", str(len(corps)))
        for k, v in (entetes or {"Cache-Control": "no-store"}).items():
            self.send_header(k, v)
        self.end_headers()
        self.wfile.write(corps)

    def _json(self, obj, code: int = 200):
        self._envoyer(code, json.dumps(obj, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def _introuvable(self):
        self._envoyer(404, b"introuvable", "text/plain")

    def _fichier(self, f: Path | None, cache: bool = False):
        """Envoie un fichier entier (``cache`` : gardé une heure par le navigateur)."""
        if not f or not Path(f).is_file():
            return self._introuvable()
        self._envoyer(200, Path(f).read_bytes(), type_de(f), {"Cache-Control": "max-age=3600" if cache else "no-store"})

    def _media(self, f: Path | None):
        """Envoie un fichier avec lecture partielle (Range) : nécessaire pour se déplacer dans un son."""
        if not f:
            return self._introuvable()
        taille = f.stat().st_size
        type_ = type_de(f)
        plage = self.headers.get("Range") or ""
        debut, fin = 0, taille - 1
        if plage.startswith("bytes="):
            a, _, b = plage[6:].split(",")[0].partition("-")
            try:
                if a:
                    debut = int(a); fin = min(int(b), taille - 1) if b else taille - 1
                else:
                    debut = max(0, taille - int(b))
            except ValueError:
                debut, fin = 0, taille - 1
            if debut > fin or debut >= taille:
                return self._envoyer(416, b"", type_, {"Content-Range": f"bytes */{taille}"})
        with open(f, "rb") as h:
            h.seek(debut)
            corps = h.read(fin - debut + 1)
        entetes = {"Accept-Ranges": "bytes", "Cache-Control": "no-cache"}
        if plage.startswith("bytes="):
            entetes["Content-Range"] = f"bytes {debut}-{fin}/{taille}"
            return self._envoyer(206, corps, type_, entetes)
        self._envoyer(200, corps, type_, entetes)

    # ----------------------------------------------------------------- requêtes
    def _local(self) -> bool:
        """Refuse ce qui ne vient pas de la page elle-même (un autre site ouvert dans le navigateur)."""
        hote = (self.headers.get("Host") or "").split(":")[0]
        if hote not in HOTES:
            return False
        origine = self.headers.get("Origin")
        return not origine or urlparse(origine).hostname in HOTES

    def _traiter(self, fonction, *args):
        try:
            fonction(*args)
        except (BrokenPipeError, ConnectionResetError):       # la page est partie avant la réponse
            pass
        except Exception as e:                                # la page affiche le message
            self._json({"ok": False, "message": f"{type(e).__name__} : {e}"}, 500)

    def do_GET(self):
        if not self._local():
            return self._envoyer(403, b"refuse", "text/plain")
        u = urlparse(self.path)
        self._traiter(self.get, unquote(u.path), u)

    def do_POST(self):
        if not self._local():
            return self._envoyer(403, b"refuse", "text/plain")
        corps = self.rfile.read(int(self.headers.get("Content-Length") or 0))
        self._traiter(self.post, urlparse(self.path).path, corps)

    def get(self, chemin: str, url):
        """Répond à ``GET chemin`` (``url`` : adresse analysée, pour les paramètres)."""
        self._introuvable()

    def post(self, chemin: str, corps: bytes):
        """Répond à ``POST chemin`` ; ``corps`` : octets reçus."""
        self._introuvable()


def demarrer(gestionnaire: type[Gestionnaire], port: int, essais: int = 20) -> tuple[ThreadingHTTPServer, str]:
    """Crée le serveur sur le premier port libre à partir de ``port`` ; renvoie (serveur, adresse).

    Le serveur n'écoute que sur 127.0.0.1 et n'est pas encore lancé.
    """
    dernier = None
    for p in range(port, port + essais):
        try:
            return ThreadingHTTPServer(("127.0.0.1", p), gestionnaire), f"http://127.0.0.1:{p}/"
        except OSError as e:
            dernier = e
    raise SystemExit(f"Aucun port libre entre {port} et {port + essais - 1} ({dernier})")


def servir(srv: ThreadingHTTPServer, adresse: str, navigateur: bool = True) -> bool:
    """Ouvre la page (si ``navigateur``) et fait tourner le serveur jusqu'à son arrêt ou Ctrl+C.

    Renvoie ``True`` si l'arrêt vient de Ctrl+C.
    """
    if navigateur:
        threading.Timer(0.4, lambda: webbrowser.open(adresse)).start()
    try:
        srv.serve_forever()
        return False
    except KeyboardInterrupt:
        return True
    finally:
        srv.server_close()
