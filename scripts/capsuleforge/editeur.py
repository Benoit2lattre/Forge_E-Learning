"""CapsuleForge — éditeur visuel d'une capsule (serveur local + page editeur.html).

« capsuleforge editer tuto1 » démarre un petit serveur sur cet ordinateur seulement (127.0.0.1) et ouvre
l'éditeur dans le navigateur. La page lit et écrit ``capsule.yaml`` par ce serveur ; rien ne sort de cet ordinateur.

Ce que fait le serveur (module :mod:`serveur_local`) : ::

  GET  /                      la page de l'éditeur
  GET  /api/capsule           la capsule (JSON) et la liste des images
  POST /api/capsule           enregistre capsule.yaml (copie de l'ancien dans sauvegardes/, une par séance)
  GET  /images/<nom>          une image de la capsule
  GET  /vendor/mathjax.js      MathJax, pour l'aperçu des formules
  GET  /vignette/<nom>?x=&y=  vignette centrée sur le point cliqué (chronologie)
  POST /api/image             ajoute une image (diapositive exportée, capture) ramenée à la taille de l'écran
  POST /api/apercu            construit le lecteur (mode aperçu) ; GET /apercu/… le sert

Licence : GPL v3.
"""
from __future__ import annotations

import io
import json
import shutil
import threading
import time
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs

import assemblage as A
import serveur_local as S

ICI = Path(__file__).resolve().parent

# ordre des clés d'un pas dans le YAML (les clés inconnues suivent, dans leur ordre d'arrivée)
ORDRE_PAS = ["ignorer", "raison", "id", "action", "image", "point", "arrivee", "crans", "texte", "accepte", "tolerance",
             "touches", "ou", "observer", "indice", "cible", "bulle", "bulle_position", "retour_juste", "retour_faux", "lecture_s", "trajectoire", "trajet",
             "duree_ms", "processus", "autre_programme"]
ORDRE_ETAPE = ["titre", "narration", "audio", "arret", "pas"]
ORDRE_CAPSULE = ["format", "titre", "langue", "ecran", "source", "reglages", "masques", "etapes", "image_finale"]


def _ordonner(d: dict, ordre: list[str]) -> dict:
    """Renvoie une copie de ``d`` dont les clés suivent ``ordre`` ; les autres clés viennent ensuite."""
    return {**{k: d[k] for k in ordre if k in d}, **{k: v for k, v in d.items() if k not in ordre}}


def _entiers(v):
    """Coordonnées en entiers (le navigateur renvoie des flottants après un glisser)."""
    if isinstance(v, list):
        return [_entiers(x) for x in v]
    return int(round(v)) if isinstance(v, float) else v


def normaliser(cap: dict) -> dict:
    """Renvoie la capsule reçue de la page, prête à écrire : clés vides retirées, ordre stable, coordonnées entières."""
    etapes = []
    for et in cap.get("etapes") or []:
        pas = []
        for p in et.get("pas") or []:
            p = {k: v for k, v in p.items() if (v not in (None, "", []) and v is not False) or k in ("bulle", "indice")}
            for k in ("point", "arrivee", "bulle_position"):
                if k in p:
                    p[k] = _entiers(p[k])
            if isinstance(p.get("cible"), dict):
                c = {k: v for k, v in p["cible"].items() if v not in (None, "")}
                if "cadre" in c:
                    c["cadre"] = _entiers(c["cadre"])
                p["cible"] = _ordonner(c, ["nom", "type", "dans", "cadre", "origine"])
            if isinstance(p.get("ou"), list):          # gestes acceptés en plus : zones en entiers
                p["ou"] = [{k: (_entiers(v) if k == "cadre" else v) for k, v in q.items() if v not in (None, "")}
                           for q in p["ou"] if isinstance(q, dict)]
            pas.append(_ordonner(p, ORDRE_PAS))
        e2 = dict(et)
        e2["pas"] = pas
        e2.setdefault("narration", "")
        e2.setdefault("arret", True)
        if not e2.get("audio"):
            e2.pop("audio", None)
        etapes.append(_ordonner(e2, ORDRE_ETAPE))
    out = dict(cap)
    out["etapes"] = etapes
    out["masques"] = _entiers(cap.get("masques") or [])
    out.setdefault("format", A.FORMAT)
    return _ordonner(out, ORDRE_CAPSULE)


class Seance:
    """État du serveur de l'éditeur pour un ``capsule.yaml`` : lecture, écriture, images, vignettes, aperçu.

    ``sortie`` est le dossier où l'aperçu du lecteur est construit.
    """

    def __init__(self, capsule_yaml: Path, sortie: Path):
        self.yaml = Path(capsule_yaml)
        self.dossier = self.yaml.parent
        self.sortie = Path(sortie)
        self.sauvegarde_faite = False
        self.verrou = threading.Lock()
        self.vignettes: dict = {}

    # ---------------------------------------------------------------- capsule
    def lire(self) -> dict:
        """Renvoie la capsule, la liste des images, les erreurs, les avertissements et les types de contrôle."""
        cap = A.lire_yaml(self.yaml)
        images = sorted(f.name for f in (self.dossier / "images").glob("*") if f.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"))
        err, av = A.verifier(cap, self.dossier)
        return {"capsule": cap, "images": images, "nom": self.dossier.name, "erreurs": err, "avertissements": av,
                "types_controle": A.TYPES_CONTROLE}

    def ecrire(self, cap: dict) -> dict:
        """Normalise et enregistre la capsule envoyée par la page ; renvoie erreurs, avertissements et heure.

        Une copie de l'ancien ``capsule.yaml`` est faite dans ``sauvegardes/`` à la première écriture ; le fichier
        est écrit sous un nom temporaire puis renommé. ``ValueError`` si ``etapes`` ou ``ecran`` manque.
        """
        if not isinstance(cap.get("etapes"), list) or not cap.get("ecran"):
            raise ValueError("capsule incomplète (etapes ou ecran manquant) : rien n'a été écrit")
        cap = normaliser(cap)
        with self.verrou:
            if not self.sauvegarde_faite and self.yaml.is_file():
                d = self.dossier / "sauvegardes"
                d.mkdir(exist_ok=True)
                shutil.copy2(self.yaml, d / f"capsule_{time.strftime('%Y%m%d_%H%M%S')}.yaml")
                self.sauvegarde_faite = True
            tmp = self.yaml.with_name("capsule.yaml.tmp")
            A.ecrire_yaml(cap, tmp)
            tmp.replace(self.yaml)
        err, av = A.verifier(cap, self.dossier)
        return {"ok": True, "erreurs": err, "avertissements": av, "heure": time.strftime("%H:%M:%S")}

    # ---------------------------------------------------------------- images
    def chemin_image(self, nom: str) -> Path | None:
        """Renvoie le chemin de l'image ``nom`` dans ``images/`` si elle existe, sinon ``None``."""
        f = (self.dossier / "images" / Path(nom).name)
        return f if f.is_file() else None

    def vignette(self, nom: str, x: float | None, y: float | None, l: int = 176, h: int = 110) -> bytes | None:
        """Renvoie une vignette JPEG de l'image ``nom`` (``None`` si l'image manque).

        Avec un point (x, y), la vignette montre la zone de 704 × 440 px qui l'entoure (ce que l'on clique) ;
        sinon l'image entière. Les vignettes sont gardées en mémoire.
        """
        from PIL import Image
        f = self.chemin_image(nom)
        if not f:
            return None
        cle = (nom, f.stat().st_mtime, None if x is None else int(x) // 8, None if y is None else int(y) // 8)
        if cle in self.vignettes:
            return self.vignettes[cle]
        with Image.open(f) as im:
            im = im.convert("RGB")
            if x is not None and y is not None:
                L, H = l * 4, h * 4
                x0 = int(max(0, min(x - L / 2, im.width - L)))
                y0 = int(max(0, min(y - H / 2, im.height - H)))
                im = im.crop((x0, y0, min(im.width, x0 + L), min(im.height, y0 + H)))
            im.thumbnail((l, h))
            b = io.BytesIO()
            im.save(b, "JPEG", quality=72)
        if len(self.vignettes) > 600:
            self.vignettes.clear()
        self.vignettes[cle] = b.getvalue()
        return self.vignettes[cle]

    def ajouter_image(self, octets: bytes, ecran: dict) -> str:
        """Ajoute une image importée dans ``images/ajout_NNN.png`` et renvoie son nom.

        L'image est ramenée à la taille de l'écran de la capsule (bandes noires si les proportions diffèrent).
        """
        from PIL import Image
        im = Image.open(io.BytesIO(octets)).convert("RGB")
        L, H = int(ecran["largeur"]), int(ecran["hauteur"])
        k = min(L / im.width, H / im.height)
        im = im.resize((max(1, round(im.width * k)), max(1, round(im.height * k))), Image.LANCZOS)
        fond = Image.new("RGB", (L, H), (0, 0, 0))
        fond.paste(im, ((L - im.width) // 2, (H - im.height) // 2))
        d = self.dossier / "images"
        d.mkdir(exist_ok=True)
        n = 1
        while (d / f"ajout_{n:03d}.png").exists():
            n += 1
        fond.save(d / f"ajout_{n:03d}.png", "PNG")
        return f"ajout_{n:03d}.png"

    def apercu(self) -> dict:
        """Construit le lecteur en mode aperçu dans le dossier de sortie ; renvoie l'adresse ou le message d'erreur."""
        import construire
        try:
            construire.construire(self.yaml, self.sortie, apercu=True)
        except SystemExit as e:
            return {"ok": False, "message": str(e)}
        return {"ok": True, "url": "/apercu/index.html"}


def _gestionnaire(seance: Seance):
    """Renvoie la classe de gestionnaire HTTP liée à ``seance`` (routes : voir l'en-tête du module)."""
    class G(S.Gestionnaire):

        def get(self, chemin, url):
            if chemin in ("/", "/index.html"):
                return self._fichier(ICI / "editeur.html")
            if chemin == "/api/capsule":
                return self._json(seance.lire())
            if chemin.startswith("/images/"):
                return self._fichier(seance.chemin_image(chemin[8:]))
            if chemin.startswith("/vignette/"):
                q = parse_qs(url.query)
                x = float(q["x"][0]) if "x" in q else None
                y = float(q["y"][0]) if "y" in q else None
                v = seance.vignette(chemin[10:], x, y)
                return self._envoyer(200, v, "image/jpeg", {"Cache-Control": "max-age=3600"}) if v \
                    else self._envoyer(404, b"", "text/plain")
            if chemin == "/vendor/mathjax.js":
                import construire
                return self._fichier(construire.MATHJAX, True)
            if chemin.startswith("/apercu/"):
                f = (seance.sortie / chemin[8:]).resolve()
                if seance.sortie.resolve() not in f.parents:
                    return self._envoyer(403, b"refuse", "text/plain")
                return self._fichier(f)
            self._introuvable()

        def post(self, chemin, corps):
            if chemin == "/api/capsule":
                return self._json(seance.ecrire(json.loads(corps.decode("utf-8"))))
            if chemin == "/api/image":
                cap = A.lire_yaml(seance.yaml)
                return self._json({"ok": True, "nom": seance.ajouter_image(corps, cap["ecran"])})
            if chemin == "/api/apercu":
                return self._json(seance.apercu())
            self._introuvable()

    return G


def demarrer(capsule_yaml: Path, sortie: Path, port: int = 8765) -> tuple[ThreadingHTTPServer, str]:
    """Crée le serveur sur le premier port libre à partir de ``port`` ; renvoie (serveur, adresse).

    Le serveur n'écoute que sur 127.0.0.1 et n'est pas encore lancé.
    """
    return S.demarrer(_gestionnaire(Seance(capsule_yaml, sortie)), port)


def editer(capsule_yaml: Path, sortie: Path, port: int = 8765, navigateur: bool = True):
    """Lance l'éditeur visuel d'une capsule : serveur local et, si ``navigateur``, ouverture de la page.

    ``sortie`` reçoit l'aperçu du lecteur. Bloque jusqu'à Ctrl+C.
    """
    if not Path(capsule_yaml).is_file():
        raise SystemExit(f"Capsule introuvable : {capsule_yaml}")
    srv, adresse = demarrer(capsule_yaml, sortie, port)
    print(f"Éditeur de « {Path(capsule_yaml).parent.name} » : {adresse}")
    print("Laisser cette fenêtre ouverte pendant l'édition ; Ctrl+C pour arrêter.")
    if S.servir(srv, adresse, navigateur):
        print("\nÉditeur arrêté.")
