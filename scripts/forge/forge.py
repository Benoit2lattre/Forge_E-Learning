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
  GET  /api/capsules          capsules de data/capsuleforge
  GET  /api/capsule/<nom>     état d'une capsule, section par section (``capsules.detail``)
  GET  /api/quizforge/classeurs, /api/diagforge/dossiers   listes des écrans Questions et Bilans
  GET  /api/reglages          réglages de l'atelier (data/_atelier/reglages.json)
  GET  /api/taches            résumé des tâches de la séance
  GET  /api/tache/<id>?depuis=n   lignes du journal d'une tâche à partir de la n-ième
  GET  /dist/<chemin>         fichiers construits (essayer un exercice, ouvrir un lecteur)
  POST /api/lancer            {action, params} : lance une tâche
  POST /api/envoyer           {id, ligne: pause|fin} : commande envoyée à une tâche qui l'accepte (filmer)
  GET  /api/appareils         écrans, caméras et micros (filmer)
  POST /api/arreter           {id} : arrête une tâche
  POST /api/parcourir         {dossier?, types?} : dialogue de fichiers de Windows, renvoie le chemin choisi
  POST /api/montrer           {chemin} : ouvre l'explorateur sur un fichier ou un dossier du dépôt
  POST /api/ouvrir            {chemin} : ouvre un fichier du dépôt avec son programme (Excel, navigateur…)
  POST /api/reglages          {reglages: {profil?, diaporamas?: {}}} : enregistre les réglages
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
import capsules as C              # noqa: E402
import questions_bilans as QB      # noqa: E402
import cours as K                  # noqa: E402
import chemins                    # noqa: E402
import profil_cours as PC          # noqa: E402
import serveur_local as S         # noqa: E402

VERSION = "0.5"
RACINE = chemins.RACINE
PY = sys.executable
PORT = 8770
MAX_LIGNES = 5000                 # lignes gardées par tâche (les plus anciennes sont retirées)
TYPES = dict(S.TYPES, **{".svg": "image/svg+xml", ".woff": "font/woff", ".woff2": "font/woff2", ".ttf": "font/ttf",
                         ".mp4": "video/mp4", ".webm": "video/webm", ".xml": "application/xml", ".txt": "text/plain; charset=utf-8",
                         ".zip": "application/zip", ".pdf": "application/pdf", ".gif": "image/gif"})
WINDOWS = os.name == "nt"
ADRESSE = re.compile(r"http://127\.0\.0\.1:\d+/")


def rel(p: Path) -> str:
    """Chemin relatif au dépôt, avec des « / » (sinon le chemin absolu)."""
    try:
        return Path(p).resolve().relative_to(RACINE).as_posix()
    except ValueError:
        return str(p)


def dans_depot(chemin: str) -> Path:
    """Chemin absolu d'un fichier du dépôt (ou d'un classeur ajouté, et de son dossier de sortie) ; refuse le reste."""
    p = (RACINE / chemin).resolve() if not Path(chemin).is_absolute() else Path(chemin).resolve()
    if p == RACINE or RACINE in p.parents:
        return p
    try:                                                 # dossiers désignés par un cours, même hors du dépôt
        for ms in K.Index().motifs.values():
            for m in ms:
                if "*" not in m and K.correspond(p, m):
                    return p
    except Exception:
        pass
    for c in C.reglages().get("classeurs") or []:
        c = Path(c).resolve()
        sortie = c.parent / f"{c.stem}_QuizForge"
        if p == c or p == sortie or sortie in p.parents:
            return p
    raise ValueError("chemin hors du dépôt")


# --------------------------------------------------------------------------------------------- tâches
class Tache:
    """Une commande Forge lancée par l'atelier : sous-processus, journal, état."""

    def __init__(self, ident: str, titre: str, outil: str, argv: list[str], verrou: str | None = None,
                 apres=None, entree: bool = False, genre: str = ""):
        self.id, self.titre, self.outil, self.argv, self.verrou = ident, titre, outil, argv, verrou
        self.apres = apres                     # fonction (tache) -> dict de liens, appelée à la fin si la tâche réussit
        self.entree = entree                   # entrée de la commande ouverte (filmer : « pause », « fin »)
        self.genre = genre                     # « filmer », « enregistrer » : la page montre un panneau d'enregistrement
        self.rec = "pret"                      # pret, actif, pause
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
                                         stdin=subprocess.PIPE if self.entree else subprocess.DEVNULL, env=env, text=True, encoding="utf-8",
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
                    self.liens = {**{k: v for k, v in self.liens.items() if k != "ouvrir"}, **(self.apres(self) or {})}
                except Exception as e:                     # un lien manquant ne fait pas échouer la tâche
                    self.ajouter(f"(liens non trouvés : {e})")
            quand_fini(self)
        threading.Thread(target=lire, daemon=True).start()

    def ajouter(self, ligne: str):
        if self.genre:                                   # état d'un enregistrement, lu dans son journal
            if "● enregistrement" in ligne or "-- reprise --" in ligne or "▶ reprise" in ligne:
                self.rec = "actif"
            elif "⏸ pause" in ligne or "-- pause --" in ligne:
                self.rec = "pause"
        if "ouvrir" not in self.liens:
            m = ADRESSE.search(ligne)
            if m and self.outil == "capsuleforge":
                self.liens = dict(self.liens, ouvrir=m.group(0))
        self.lignes.append(ligne)
        if len(self.lignes) > MAX_LIGNES:
            del self.lignes[:500]
            self.retirees += 500

    def envoyer(self, ligne: str) -> bool:
        """Envoie une ligne à la commande (entrée ouverte seulement)."""
        if not (self.entree and self.proc and self.proc.poll() is None and self.proc.stdin):
            return False
        try:
            self.proc.stdin.write(ligne + "\n")
            self.proc.stdin.flush()
            return True
        except OSError:
            return False

    def arreter(self):
        if (self.genre and self.rec in ("actif", "pause") and not getattr(self, "fin_demandee", False)
                and self.envoyer("fin")):                # enregistrement en cours : on le termine et on le garde
            self.fin_demandee = True
            self.ajouter("(Arrêter : enregistrement terminé et gardé ; cliquer encore sur Arrêter pour tout abandonner)")
            return
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
        return {"id": self.id, "titre": self.titre, "outil": self.outil, "genre": self.genre, "rec": self.rec, "etat": self.etat, "code": self.code,
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
        self.montres: dict[str, float] = {}
        self._appareils = None         # dernière ouverture de l'explorateur par chemin
        self.page_partie_le: float | None = None
        self.arreter = lambda: None            # remplacé par srv.shutdown
        self.journal = chemins.DATA / "_atelier" / "journal.jsonl"
        self.actions = {"exoforge.construire": self.a_exo_construire, "capsule.pptx": self.a_cap_pptx,
                        "capsule.transcrire": self.a_cap_transcrire, "capsule.relire": self.a_cap_relire,
                        "capsule.traduire": self.a_cap_traduire, "capsule.voix": self.a_cap_voix,
                        "capsule.accrocher": self.a_cap_accrocher,
                        "capsule.verifier": self.a_cap_simple("verifier", "Vérifier"),
                        "capsule.convertir": self.a_cap_simple("convertir", "Mettre à jour pour le lecteur actuel"),
                        "capsule.construire": self.a_cap_construire, "capsule.video": self.a_cap_video,
                        "capsule.nouvelle": self.a_cap_nouvelle,
                        "quiz.valider": self.a_quiz_valider, "quiz.convertir": self.a_quiz_convertir,
                        "quiz.modele": self.a_quiz_modele, "quiz.fusionner": self.a_quiz_fusionner,
                        "diag.bilan": self.a_diag_bilan, "capsule.filmer": self.a_cap_filmer,
                        "capsule.editer": self.a_cap_editer, "capsule.enregistrer": self.a_cap_enregistrer,
                        "capsule.approj": self.a_cap_approj, "capsule.cameo": self.a_cap_cameo}

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

    # ------------------------------------------------------------------ cours
    def cours_actif(self) -> dict:
        """Choix du sélecteur : {cours, declinaison?, edition?}, {cours: "_sans"} ou {} (tous les cours)."""
        r = C.reglages().get("cours_actif") or {}
        if r.get("cours") and r["cours"] != "_sans" and r["cours"] not in K.tous():
            return {}
        return r

    def filtre(self, objets: list[dict], cle: str, chemin=None) -> list[dict]:
        try:
            return K.filtrer(objets, cle, self.cours_actif(), chemin=chemin)
        except Exception:                                # un cours mal écrit ne vide pas les listes
            return objets

    def cours_liste(self) -> dict:
        resumes = []
        for c in K.tous().values():
            resumes.append({"nom": c["nom"], "titre": str(c.get("titre") or c["nom"]), "domaine": c.get("domaine") or "",
                            "fichier": rel(c["_fichier"]), "erreur": c.get("_erreur"),
                            "declinaisons": len(c.get("declinaisons") or []),
                            "public": K.RACINES[1] in c["_fichier"].parents})
        return {"ok": True, "choix": K.choix_possibles(), "actif": self.cours_actif(), "cours": resumes}

    def cours_detail(self, nom: str) -> dict:
        c = K.trouver(nom)
        propre = json.loads(json.dumps({k: v for k, v in c.items() if not k.startswith("_")}, ensure_ascii=False, default=str))
        return {"ok": True, "cours": propre, "fichier": rel(c["_fichier"]), "remarques": K.verifier(c),
                "types": K.TYPES, "documents": K.DOCUMENTS, "profils": profils_campus(), "generique": PC.generique(),
                "autres": [n for n in K.tous() if n != nom]}

    def cours_sans(self) -> dict:
        idx = K.Index()
        def sans(objs, cle, chemin=None):
            return [o for o in K.filtrer(objs, cle, {"cours": "_sans"}, idx, chemin=chemin) if o.get("origine") != "exemple"]
        return {"ok": True, "objets": {
            "questions": [{"chemin": o["classeur"], "libelle": o["nom"]} for o in sans(QB.classeurs(C.reglages().get("classeurs")), "classeur")],
            "exercices": [{"chemin": o["fiche"], "libelle": o["titre"]} for o in sans(self.fiches_exoforge(), "fiche")],
            "capsules": [{"chemin": o["dossier"], "libelle": o["titre"]} for o in sans(C.liste(), "dossier")],
            "exports": [{"chemin": o["dossier"], "libelle": o["dossier"]} for o in sans(QB.dossiers_exports(), "dossier")]},
            "types": K.TYPES, "cours": [{"nom": c["nom"], "titre": str(c.get("titre") or c["nom"])} for c in K.tous().values()]}

    def cours_action(self, p: dict) -> dict:
        """Modifications d'un cours venues de l'écran Cours (un formulaire, jamais le YAML)."""
        action, avert = p.get("action"), []
        if action == "actif":
            choix = {}
            if p.get("cours") == "_sans":
                choix = {"cours": "_sans"}
            elif p.get("cours"):
                c = K.trouver(p["cours"])
                choix = {"cours": c["nom"]}
                if p.get("declinaison"):
                    K.edition(c, p["declinaison"], p.get("edition") or "")
                    choix.update(declinaison=p["declinaison"], edition=str(p["edition"]))
            C.garder_reglage("cours_actif", choix)
            return {"ok": True, "actif": choix}
        if action == "proposer":
            return {"ok": True, "propositions": K.proposer(K.nom_valide(p.get("nom")))}
        if action == "nouveau":
            c, avert = K.creer(p.get("nom"), p.get("titre"), p.get("domaine") or "",
                               [K.texte_valide(x, 5) for x in (p.get("langues") or ["fr"])],
                               sources=p.get("sources") or [], standard=bool(p.get("standard")))
            C.garder_reglage("cours_actif", {"cours": c["nom"]})
            return {"ok": True, "nom": c["nom"], "avertissements": avert}
        c = K.trouver(p.get("nom") or "")
        if action == "fiche":
            f = p.get("fiche") or {}
            lignes = lambda v: [K.texte_valide(x, 300) for x in (v if isinstance(v, list) else str(v or "").splitlines()) if str(x).strip()]
            if "titre" in f:
                c["titre"] = K.texte_valide(f["titre"]) or c["nom"]
            for k in ("domaine", "erreurs"):
                if k in f:
                    c[k] = K.texte_valide(f[k]) or None
            if "description" in f:
                c["description"] = K.texte_valide(f["description"], 4000, lignes=True)
            for k in ("objectifs", "competences"):
                if k in f:
                    c[k] = lignes(f[k])
            for k in ("langues", "etiquettes"):
                if k in f:
                    c[k] = [K.texte_valide(x, 40) for x in (f[k] if isinstance(f[k], list) else str(f[k]).split(",")) if str(x).strip()]
            if "inclut" in f:
                c["inclut"] = [n for n in f["inclut"] or [] if n in K.tous() and n != c["nom"]]
            if "derive_de" in f:
                c["derive_de"] = f["derive_de"] if f["derive_de"] in K.tous() and f["derive_de"] != c["nom"] else None
        elif action == "declinaison":
            K.ajouter_declinaison(c, p.get("declinaison") or {})
        elif action == "declinaison_modifier":
            K.modifier_declinaison(c, p.get("declinaison_nom") or "", p.get("declinaison") or {})
        elif action == "declinaison_supprimer":
            K.supprimer_declinaison(c, p.get("declinaison_nom") or "")
        elif action == "edition_modifier":
            K.modifier_edition(c, p.get("declinaison") or "", p.get("edition_nom") or "", p.get("edition") or {})
        elif action == "edition":
            e = K.ajouter_edition(c, p.get("declinaison") or "", p.get("edition") or {})
            avert += K.longueur(K.absolu(e["exports"]))
        elif action == "active":
            K.edition(c, p.get("declinaison") or "", p.get("edition") or "")
            K.declinaison(c, p["declinaison"])["en_cours"] = str(p["edition"])
        elif action in ("source_ajouter", "ranger"):
            K.ajouter_source(c, p.get("type") or "", p.get("chemin") or "")
        elif action == "source_retirer":
            K.retirer_source(c, p.get("type") or "", p.get("chemin") or "")
        elif action == "document_ajouter":
            cle = p.get("cle") if p.get("cle") in K.DOCUMENTS else "autre"
            f = K.absolu(p.get("chemin") or "")
            if not f.is_file():
                raise ValueError("document introuvable")
            docs = c.setdefault("documents", {})
            if cle == "autre":
                n = 1
                while f"autre{n}" in docs:
                    n += 1
                cle = f"autre{n}"
            docs[cle] = K.rel(f)
        elif action == "document_retirer":
            (c.get("documents") or {}).pop(p.get("cle"), None)
        else:
            raise ValueError("action inconnue")
        K.ecrire(c)
        return {"ok": True, "avertissements": avert}

    def cours_spec(self) -> str | None:
        """Valeur de ``--cours`` pour le choix du sélecteur (rien pour « tous » ou « sans cours »)."""
        a = self.cours_actif()
        if not a.get("cours") or a["cours"] == "_sans":
            return None
        return a["cours"] + (f":{a['declinaison']}/{a['edition']}" if a.get("declinaison") else "")

    def option_cours(self) -> list[str]:
        s = self.cours_spec()
        return ["--cours", s] if s else []

    def cours_reglages(self) -> dict:
        """Réglages de l'édition choisie (profil, étiquettes, catégorie, séances, effectif, dossiers), pour les formulaires."""
        s = self.cours_spec()
        if not s:
            return {"ok": True, "reglages": None}
        sys.path.insert(0, str(chemins.SCRIPTS / "commun"))
        import cours_options as CO
        try:
            r = CO.resoudre(s)
        except Exception as e:
            return {"ok": False, "message": str(e)}
        r["prochaine"] = CO.prochaine(r)
        for k in ("exports", "bilans"):
            if r.get(k):
                K.absolu(r[k]).mkdir(parents=True, exist_ok=True)
        return {"ok": True, "reglages": json.loads(json.dumps(r, ensure_ascii=False, default=str))}

    def registres(self, q: dict) -> dict:
        """Registres des versions de quiz : de l'édition et du cours demandés (ou choisis en haut), sinon tous."""
        sys.path.insert(0, str(chemins.SCRIPTS / "commun"))
        import cours_options as CO
        import registre as R
        spec = (q.get("cours") + (f":{q['declinaison']}/{q['edition']}" if q.get("declinaison") else "")) if q.get("cours") else self.cours_spec()
        bases, editions = [], []
        if spec:
            r = CO.resoudre(spec)
            bases = [(R.base(r), r["libelle"])]
            if r.get("edition"):
                bases.append((R.base({"cours": r["cours"]}), f"{r['titre']} (extraits communs aux déclinaisons)"))
            c = K.trouver(r["cours"])
            editions = [f"{d['nom']}/{e['nom']}" for d in c.get("declinaisons") or [] for e in d.get("editions") or []]
        else:
            bases = [(b, R.rel(b)) for b in R.tous()]
        out = []
        for b, titre in bases:
            vs = R.lire(b)["versions"]
            if q.get("classeur"):
                vs = [v for v in vs if R.genre(v) == "quiz" and R.nom_source(v) == Path(q["classeur"]).stem]
            if q.get("fiche"):
                vs = [v for v in vs if R.genre(v) == "exercice" and R.nom_source(v) == q["fiche"]]
            if q.get("capsule"):
                vs = [v for v in vs if R.genre(v) == "capsule" and R.nom_source(v) == q["capsule"]]
            out.append({"base": R.rel(b), "titre": titre, "commun": b == bases[-1][0] and len(bases) == 2,
                        "versions": json.loads(json.dumps(vs[::-1], ensure_ascii=False, default=str))})
        return {"ok": True, "registres": out, "editions": editions, "etats": R.LIBELLES}

    def registre_modifier(self, p: dict) -> dict:
        sys.path.insert(0, str(chemins.SCRIPTS / "commun"))
        import registre as R
        b = R.absolu(p.get("base") or "")
        if not (b / R.FICHIER).is_file() or b.resolve() not in [x.resolve() for x in R.tous()]:
            raise ValueError("registre inconnu")
        v = R.modifier(b, p.get("id") or "", p.get("champs") or {})
        return {"ok": True, "version": json.loads(json.dumps(v, ensure_ascii=False, default=str))}

    def versions_classeurs(self, classeurs: list[dict]) -> list[dict]:
        """Dernière version de chaque classeur dans les registres du choix (ou tous) : {id, etat, nombre}."""
        try:
            regs = self.registres({})["registres"]
        except Exception:
            return classeurs
        for c in classeurs:
            nom, genre = (Path(c["classeur"]).stem, "quiz") if "classeur" in c else (c.get("id"), "exercice")
            vs = [v for r in regs for v in r["versions"] if (v.get("genre") or "quiz") == genre
                  and (v.get("nom") or Path(v.get("classeur") or v.get("source") or "").stem) == nom]
            if vs:
                der = max(vs, key=lambda v: str(v.get("date")))
                c["versions"] = {"nombre": len(vs), "derniere": der["id"], "etat": der.get("etat"), "dossier": der.get("dossier")}
                if genre == "exercice":
                    zips = sorted(K.absolu(der.get("dossier", "")).glob("*_scorm12.zip"))
                    c["versions"]["paquet"] = rel(zips[0]) if zips else None
        return classeurs

    def rattacher(self, type_: str, chemin: Path):
        """Ajoute un objet créé par l'atelier au cours actif s'il n'y est pas déjà (sources du cours)."""
        actif = self.cours_actif().get("cours")
        if not actif or actif == "_sans" or not chemin.exists():
            return
        try:
            if actif not in K.Index().de(chemin):
                c = K.trouver(actif)
                K.ajouter_source(c, type_, str(chemin))
                K.ecrire(c)
        except Exception:
            pass

    def dossier_du_cours(self, type_: str, defaut: Path) -> Path:
        """Dossier standard du cours actif pour un type (``capsules/``, ``questions/``…), sinon ``defaut``."""
        actif = self.cours_actif().get("cours")
        if actif and actif != "_sans":
            try:
                d = K.dossier_cours(K.trouver(actif)) / type_
                if d.is_dir():
                    return d
            except ValueError:
                pass
        return defaut

    # ------------------------------------------------------------------ ExoForge
    def fiches_exoforge(self) -> list[dict]:
        """Fiches ExoForge du dépôt : exemples publiés et data/exoforge (fiches privées)."""
        import yaml
        trouvees = []
        vues = set()
        bases = [(chemins.OUTILS / "exoforge" / "exemples", "exemple"), (chemins.DATA / "exoforge", "data")]
        bases += [(b, "cours") for b in K.Index().dossiers("exercices")]
        for base, origine in bases:
            for f in sorted(base.rglob("*.y*ml")) if base.is_dir() else ([base] if base.is_file() else []):
                if f.resolve() in vues or (base.is_dir() and "media" in f.relative_to(base).parts) or f.name.startswith("_"):
                    continue
                d = lire_fiche(f, yaml)
                if d:
                    vues.add(f.resolve())
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
        argv += self.option_cours()

        def liens(t):
            ident = d["id"]
            out = {}
            if (chemins.SORTIES / "exoforge" / ident / "index.html").is_file():
                out["essayer"] = f"/dist/exoforge/{ident}/index.html"
            z = chemins.SORTIES / "exoforge" / f"{ident}_scorm12.zip"
            if z.is_file():
                out["paquet"] = rel(z)
            v = next((ligne[10:].strip() for ligne in reversed(t.lignes) if ligne.startswith("Version : ")), None)
            if v:                                        # paquet rangé comme version de l'édition
                zips = sorted(K.absolu(v).glob("*_scorm12.zip"))
                if zips:
                    out["paquet"] = rel(zips[0])
            return out
        return Tache(self.nouvel_id(), f"Construire « {d['titre']} »", "exoforge", argv,
                     verrou=str(f.resolve()), apres=liens)

    # ------------------------------------------------------------------ CapsuleForge
    def _cap(self, p: dict):
        d = C.dossier(p.get("capsule") or "")
        titre = C.texte(C.F().lire(d / "chapitre.yaml").get("titre")) if (d / "chapitre.yaml").is_file() else d.name
        return d, titre or d.name

    def _tache_cap(self, d: Path, titre: str, argv: list[str], apres=None) -> Tache:
        return Tache(self.nouvel_id(), titre, "capsuleforge", argv, verrou=str(d.resolve()), apres=apres)

    def a_cap_simple(self, cmd: str, libelle: str):
        def action(p):
            d, t = self._cap(p)
            return self._tache_cap(d, f"{libelle} « {t} »", C.argv_base(PY, cmd) + [str(d)])
        return action

    def a_cap_cameo(self, p: dict) -> Tache:
        d, t = self._cap(p)
        argv = C.argv_base(PY, "cameo") + [str(d)]
        if p.get("position"):
            if p["position"] not in ("bas-droite", "bas-gauche", "haut-droite", "haut-gauche", "aucune"):
                raise ValueError("position du caméo inconnue")
            argv += ["--position", p["position"]]
        if p.get("forme"):
            if p["forme"] not in ("rond", "rectangle"):
                raise ValueError("forme du caméo inconnue")
            argv += ["--forme", p["forme"]]
        if p.get("taille"):
            taille = float(p["taille"])
            if not 0.08 <= taille <= 0.5:
                raise ValueError("taille du caméo : entre 0,08 et 0,5")
            argv += ["--taille", f"{taille:g}"]
        return self._tache_cap(d, f"Caméo de « {t} »", argv)

    def tester_micro(self, p: dict) -> dict:
        """Écoute le micro 4 s (``capsuleforge filmer --tester-micro``) ; renvoie voix, crête (dBFS), avis, conseil."""
        nom = (p.get("micro") or "").strip()
        if len(nom) > 120 or any(c in nom for c in "\r\n\0\""):
            return {"ok": False, "message": "nom de micro invalide"}
        argv = C.argv_base(PY, "filmer") + ["--tester-micro"] + ([nom] if nom else []) + ["--duree", "4"]
        if p.get("essai"):
            argv.append("--essai")
        try:
            r = subprocess.run(argv, cwd=RACINE, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=30,
                               env=dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1"),
                               **({"creationflags": subprocess.CREATE_NO_WINDOW} if WINDOWS else {}))
        except (OSError, subprocess.TimeoutExpired) as e:
            return {"ok": False, "message": f"test du micro impossible : {e}"}
        m = re.search(r"voix (-?\d+) dBFS, crête (-?\d+) dBFS — ([^(\n]+?)(?: \((.*)\))?\s*$", r.stdout, re.M)
        if not m:
            return {"ok": False, "message": ((r.stderr or r.stdout).strip().splitlines() or ["test du micro impossible"])[-1]}
        return {"ok": True, "voix": int(m[1]), "crete": int(m[2]), "avis": m[3].strip(), "conseil": m[4] or ""}

    def a_cap_pptx(self, p: dict) -> Tache:
        d, t = self._cap(p)
        f = Path(p.get("chemin") or "")
        if f.suffix.lower() != ".pptx" or not f.is_file():
            raise ValueError("diaporama introuvable : choisissez le fichier .pptx")
        attendu = p.get("fichier")
        if attendu and f.name != attendu:
            raise ValueError(f"le fichier choisi s'appelle « {f.name} », la capsule attend « {attendu} »")
        connus = C.reglages().get("diaporamas") or {}
        connus[f.name] = str(f)
        C.garder_reglage("diaporamas", connus)
        argv = C.argv_base(PY, "pptx") + [str(f), "--chapitre", str(d)]
        if p.get("sans_images"):
            argv.append("--sans-images")
        return self._tache_cap(d, f"Reprendre « {f.name} » dans « {t} »", argv)

    def a_cap_transcrire(self, p: dict) -> Tache:
        d, t = self._cap(p)
        modele = p.get("modele") or "small"
        if modele not in ("small", "medium"):
            raise ValueError("modèle inconnu")
        argv = C.argv_base(PY, "transcrire") + [str(d), "--modele", modele]
        if p.get("refaire"):
            argv.append("--refaire")
        secs = C.sections_valides(d, p.get("sections"))
        if secs:
            argv += ["--sections", ",".join(secs)]
        return self._tache_cap(d, f"Transcrire « {t} »", argv)

    def a_cap_relire(self, p: dict) -> Tache:
        d, t = self._cap(p)
        return self._tache_cap(d, f"Relire « {t} »", C.argv_base(PY, "relire") + [str(d), "--sans-navigateur"])

    def a_cap_accrocher(self, p: dict) -> Tache:
        d, t = self._cap(p)
        argv = C.argv_base(PY, "accrocher") + [str(d)]
        if p.get("remplacer"):
            argv.append("--remplacer")
        secs = C.sections_valides(d, p.get("sections"))
        if secs:
            argv += ["--sections", ",".join(secs)]
        return self._tache_cap(d, f"Accrocher les objets aux phrases dans « {t} »", argv)

    def a_cap_traduire(self, p: dict) -> Tache:
        d, t = self._cap(p)
        langue = C.langue_valide(p.get("langue"))
        moteur = p.get("moteur") or "aucun"
        if moteur not in ("aucun", "argos", "deepl"):
            raise ValueError("moteur de traduction inconnu")
        argv = C.argv_base(PY, "traduire") + [str(d), "--langue", langue, "--moteur", moteur]
        if p.get("mode") == "importer":
            return self._tache_cap(d, f"Importer la traduction ({langue}) dans « {t} »", argv + ["--importer"])
        return self._tache_cap(d, f"Relire la traduction ({langue}) de « {t} »", argv + ["--relire", "--sans-navigateur"])

    def a_cap_voix(self, p: dict) -> Tache:
        d, t = self._cap(p)
        langue = C.langue_valide(p.get("langue"))
        moteur = p.get("moteur") or "piper"
        if moteur not in ("piper", "edge"):
            raise ValueError("moteur de voix inconnu")
        argv = C.argv_base(PY, "voix") + [str(d), "--langue", langue, "--moteur", moteur]
        nom = (p.get("voix") or "").replace(" (à télécharger)", "")
        if nom:
            if not re.fullmatch(r"[A-Za-z0-9_.-]+", nom):
                raise ValueError("nom de voix invalide")
            argv += ["--voix", nom]
        vitesse = float(p.get("vitesse") or 1.0)
        if not 0.5 <= vitesse <= 2.0:
            raise ValueError("vitesse entre 0,5 et 2")
        argv += ["--vitesse", f"{vitesse:g}"]
        if p.get("refaire"):
            argv.append("--refaire")
        secs = C.sections_valides(d, p.get("sections"))
        if secs:
            argv += ["--sections", ",".join(secs)]
        return self._tache_cap(d, f"Voix ({langue}) de « {t} »", argv)

    def a_cap_construire(self, p: dict) -> Tache:
        d, t = self._cap(p)
        argv = C.argv_base(PY, "construire") + [str(d)]
        scorm = p.get("scorm") or ""
        if scorm:
            if scorm not in ("chapitre", "parties", "tout"):
                raise ValueError("découpage SCORM inconnu")
            version = p.get("version") or "2004"
            if version not in ("2004", "1.2"):
                raise ValueError("version SCORM inconnue")
            argv += ["--scorm", scorm, "--scorm-version", version]
        if p.get("audio") == "origine":
            argv += ["--audio", "origine"]
        if p.get("pdf") and p.get("lecteur") != "1":           # PDF de la capsule (lecteur actuel seulement)
            contenu = p.get("pdf_contenu") or "texte"
            if contenu not in ("texte", "texte,diapo", "diapos"):
                raise ValueError("contenu du PDF inconnu")
            notes = p.get("pdf_notes") or "aucune"
            if notes not in ("aucune", "marge", "dessous"):
                raise ValueError("place des notes inconnue")
            argv += ["--pdf", "--pdf-contenu", contenu, "--pdf-notes", notes]
            if p.get("pdf_langue"):
                if not re.fullmatch(r"[a-z]{2,3}", str(p["pdf_langue"])):
                    raise ValueError("langue du PDF inconnue")
                argv += ["--pdf-langue", p["pdf_langue"]]
        if p.get("lecteur") in ("1", "2"):
            argv += ["--lecteur", p["lecteur"]]
        elif (d / "capsule.yaml").is_file() and (d / "chapitre.yaml").is_file():
            argv += ["--lecteur", "2"]                   # la capsule a été mise à jour : le lecteur actuel
        nom = d.name
        cours = self.option_cours() if (d / "chapitre.yaml").is_file() and p.get("lecteur") != "1" else []
        if cours and not scorm:                          # une version d'édition se range avec ses paquets
            argv += ["--scorm", "chapitre", "--scorm-version", p.get("version") if p.get("version") in ("2004", "1.2") else "1.2"]
        argv += cours                                    # édition choisie : capsule habillée, rangée comme version

        def liens(tache):
            out = {}
            habillees = sorted((x for x in C.SORTIES.glob(f"{nom}_*/index.html") if x.stat().st_mtime >= tache.debut - 1),
                               key=lambda x: x.stat().st_mtime)
            if cours and habillees:
                out["lecteur"] = "/dist/capsuleforge/" + habillees[-1].parent.name + "/index.html"
            elif (C.SORTIES / nom / "index.html").is_file():
                out["lecteur"] = f"/dist/capsuleforge/{nom}/index.html"
            neufs = [z for z in C.SORTIES.glob(f"{nom}_*.zip") if z.stat().st_mtime >= tache.debut - 1]
            if neufs:
                out["paquet"] = rel(sorted(neufs)[0])
            return out
        return self._tache_cap(d, f"Construire « {t} »", argv, apres=liens)

    def a_cap_nouvelle(self, p: dict) -> Tache:
        titre = (p.get("titre") or "").strip()
        if not titre:
            raise ValueError("donnez un titre à la capsule")
        nom = (p.get("nom") or "").strip()
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,47}", nom):
            raise ValueError("nom de dossier : lettres sans accent, chiffres, - et _")
        d = self.dossier_du_cours("capsules", C.DOSSIER) / nom
        if (d / "chapitre.yaml").exists() or (d / "capsule.yaml").exists() or nom in {x.name for x in C.dossiers_capsules()}:
            raise ValueError(f"une capsule « {nom} » existe déjà")
        argv = C.argv_base(PY, "nouvelle") + [str(d) if d.parent != C.DOSSIER else nom, "--titre", titre, "--langue", C.langue_valide(p.get("langue") or "fr")]
        if p.get("chemin"):
            f = Path(p["chemin"])
            if f.suffix.lower() != ".pptx" or not f.is_file():
                raise ValueError("diaporama introuvable : choisissez un fichier .pptx")
            decoupe = p.get("decoupe") or "auto"
            if decoupe not in ("auto", "diapositive", "une"):
                raise ValueError("découpage inconnu")
            minutes = float(p.get("minutes") or 6)
            if not 1 <= minutes <= 30:
                raise ValueError("durée des sections entre 1 et 30 min")
            argv += ["--diaporama", str(f), "--decoupe", decoupe, "--minutes", f"{minutes:g}"]
            connus = C.reglages().get("diaporamas") or {}
            connus[f.name] = str(f)
            C.garder_reglage("diaporamas", connus)
        def apres(tache):
            self.rattacher("capsules", d)
            return {"capsule": nom}
        t = Tache(self.nouvel_id(), f"Créer la capsule « {titre} »", "capsuleforge", argv, verrou=str(d.resolve()), apres=apres)
        return t

    def a_cap_filmer(self, p: dict) -> Tache:
        d, t = self._cap(p)
        chap = C.F().lire(d / "chapitre.yaml")
        parties = {x.get("id"): x for x in chap.get("parties") or []}
        partie = p.get("partie") or ""
        if partie not in parties:
            raise ValueError("partie inconnue")
        argv = C.argv_base(PY, "filmer") + [str(d)]
        if p.get("section"):
            if p["section"] not in {s.get("id") for s in parties[partie].get("sections") or []}:
                raise ValueError("section inconnue")
            argv += ["--section", f"{partie}/{p['section']}"]
        else:
            titre = (p.get("titre") or "").strip() or time.strftime("Film du %d/%m à %H:%M")
            ids = {s.get("id") for x in parties.values() for s in x.get("sections") or []}
            argv += ["--section", f"{partie}/{C.ident_section(titre, ids)}", "--titre", titre]
        ecran = int(p.get("ecran") or 1)
        if not 1 <= ecran <= 8:
            raise ValueError("écran inconnu")
        argv += ["--ecran", str(ecran)]
        for cle, option in (("webcam", "--webcam"), ("micro", "--micro")):
            v = (p.get(cle) or "").strip()
            if v:
                if len(v) > 120 or any(c in v for c in "\r\n\0\""):
                    raise ValueError("nom d'appareil invalide")
                argv += [option, v]
        if p.get("sans_micro"):
            argv.append("--sans-micro")
        if p.get("essai"):
            argv.append("--essai")
        return Tache(self.nouvel_id(), f"Filmer pour « {t} »", "capsuleforge", argv, verrou=str(d.resolve()),
                     entree=True, genre="filmer")

    def a_cap_editer(self, p: dict) -> Tache:
        d, t = self._cap(p)
        if not (d / "capsule.yaml").is_file():
            raise ValueError("cette capsule n'a pas de fichier pour l'ancien éditeur")
        return self._tache_cap(d, f"Éditer « {t} » (ancien éditeur)", C.argv_base(PY, "editer") + [str(d), "--sans-navigateur"])

    def _nouveau_dossier(self, p: dict) -> tuple[str, str, Path]:
        titre = (p.get("titre") or "").strip()
        if not titre:
            raise ValueError("donnez un titre à la capsule")
        nom = (p.get("nom") or "").strip()
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_-]{0,47}", nom):
            raise ValueError("nom de dossier : lettres sans accent, chiffres, - et _")
        d = C.DOSSIER / nom
        if (d / "chapitre.yaml").exists() or (d / "capsule.yaml").exists():
            raise ValueError(f"une capsule « {nom} » existe déjà")
        if d.exists() and not (d / "journal.jsonl").exists() and any(d.iterdir()):   # enregistrement interrompu : repris
            raise ValueError(f"le dossier « {nom} » existe déjà dans data/capsuleforge : choisissez un autre nom")
        return titre, nom, d

    def a_cap_enregistrer(self, p: dict) -> Tache:
        titre, nom, d = self._nouveau_dossier(p)
        ecran = int(p.get("ecran") or 1)
        if not 1 <= ecran <= 8:
            raise ValueError("écran inconnu")
        argv = C.argv_base(PY, "enregistrer") + [nom, "--titre", titre, "--ecran", str(ecran)]
        return Tache(self.nouvel_id(), f"Enregistrer une manipulation : « {titre} »", "capsuleforge", argv,
                     verrou=str(d.resolve()), apres=lambda tache: (self.rattacher("capsules", d), {"capsule": nom})[1],
                     entree=True, genre="enregistrer")

    def a_cap_approj(self, p: dict) -> Tache:
        titre, nom, d = self._nouveau_dossier(p)
        f = Path(p.get("chemin") or "")
        if f.suffix.lower() != ".approj" or not f.is_file():
            raise ValueError("projet ActivePresenter introuvable (.approj)")
        argv = C.argv_base(PY, "approj") + [str(f), "--nom", nom, "--titre", titre]
        return Tache(self.nouvel_id(), f"Reprendre « {f.name} »", "capsuleforge", argv, verrou=str(d.resolve()),
                     apres=lambda tache: {"capsule": nom})

    def appareils(self) -> dict:
        """Écrans, caméras et micros (``capsuleforge filmer --appareils``), gardés une minute."""
        if self._appareils and time.time() - self._appareils[0] < 60:
            return self._appareils[1]
        try:
            r = subprocess.run(C.argv_base(PY, "filmer") + ["--appareils"], cwd=RACINE, capture_output=True, text=True,
                               encoding="utf-8", errors="replace", timeout=40,
                               env=dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUTF8="1"),
                               **({"creationflags": subprocess.CREATE_NO_WINDOW} if WINDOWS else {}))
            sortie = r.stdout
        except (OSError, subprocess.TimeoutExpired) as e:
            return {"ok": False, "message": f"liste des appareils impossible : {e}"}
        import ast
        out = {"ok": True, "ecrans": [], "cameras": [], "micros": []}
        for ligne in sortie.splitlines():
            cle, _, reste = ligne.partition(":")
            reste = reste.strip()
            if cle.strip() == "Écrans":
                out["ecrans"] = [x.strip() for x in reste.split(";") if x.strip() and x.strip() != "?"]
            elif cle.strip() in ("Caméras", "Micros") and reste.startswith("["):
                try:
                    out["cameras" if cle.strip() == "Caméras" else "micros"] = list(ast.literal_eval(reste))
                except (ValueError, SyntaxError):
                    pass
        if not out["ecrans"]:
            out["ecrans"] = ["n° 1"]
        self._appareils = (time.time(), out)
        return out

    def a_cap_video(self, p: dict) -> Tache:
        d, t = self._cap(p)
        f = Path(p.get("chemin") or "")
        if not f.is_file():
            raise ValueError("vidéo introuvable : choisissez le fichier")
        chap = C.F().lire(d / "chapitre.yaml")
        parties = {x.get("id"): x for x in chap.get("parties") or []}
        partie = p.get("partie") or ""
        if partie not in parties:
            raise ValueError("partie inconnue")
        argv = C.argv_base(PY, "video") + [str(f), "--chapitre", str(d)]
        if p.get("section"):
            if p["section"] not in {s.get("id") for s in parties[partie].get("sections") or []}:
                raise ValueError("section inconnue")
            argv += ["--section", f"{partie}/{p['section']}"]
        else:
            titre = (p.get("titre") or "").strip() or f.stem
            ids = {s.get("id") for x in parties.values() for s in x.get("sections") or []}
            argv += ["--section", f"{partie}/{C.ident_section(titre, ids)}", "--titre", titre]
        son = p.get("son")
        if son:
            if not Path(son).is_file():
                raise ValueError("fichier de son introuvable")
            argv += ["--son", str(son)]
        if p.get("decoupe") == "aucune":
            argv += ["--decoupe", "aucune"]
        if p.get("remplacer"):
            argv.append("--remplacer")
        return self._tache_cap(d, f"Importer « {f.name} » dans « {t} »", argv)

    # ------------------------------------------------------------------ QuizForge
    def _profil(self, p: dict) -> list[str]:
        profil = p.get("profil") or ""
        if not profil:
            return []
        if profil not in noms_profils():
            raise ValueError(f"profil inconnu : {profil}")
        return ["--profil", profil]

    def a_quiz_valider(self, p: dict) -> Tache:
        f = QB.classeur_valide(p.get("classeur") or "")
        return Tache(self.nouvel_id(), f"Valider « {f.name} »", "quizforge", [PY, str(QB.QUIZFORGE), "valider", str(f)])

    def a_quiz_convertir(self, p: dict) -> Tache:
        f = QB.classeur_valide(p.get("classeur") or "")
        argv = [PY, str(QB.QUIZFORGE), "convertir", str(f)] + self._profil(p) + self.option_cours()
        for cle, option in (("categorie", "--categorie"), ("nom", "--nom"), ("tags", "--tags")):
            v = QB.texte_court(p.get(cle) or "")
            if v:
                argv += [option, v]
        formats = [x for x in (p.get("formats") or []) if x in ("xml", "gift")]
        if formats:
            argv += ["--formats", ";".join(formats)]
        if p.get("reparer"):
            argv.append("--reparer")
        if p.get("seance"):
            seance = int(p["seance"])
            if not 1 <= seance <= 99:
                raise ValueError("séance entre 1 et 99")
            argv += ["--seance", str(seance)]
            if p.get("etudiants"):
                argv += ["--etudiants", str(max(1, int(p["etudiants"])))]
        sortie = f.parent / f"{f.stem}_QuizForge"

        def liens(t):
            v = next((ligne[10:].strip() for ligne in reversed(t.lignes) if ligne.startswith("Version : ")), None)
            if v:                                        # conversion versionnée (cours choisi)
                return {"dossier": v}
            out = {"dossier": rel(sortie)} if sortie.is_dir() else {}
            plans = sorted(f.parent.glob(f"{f.stem}_plan_S*.md"), key=lambda x: x.stat().st_mtime)
            if plans and plans[-1].stat().st_mtime >= t.debut - 1:
                out["plan"] = rel(plans[-1])
            return out
        return Tache(self.nouvel_id(), f"Convertir « {f.name} » pour Moodle", "quizforge", argv, verrou=str(f.resolve()), apres=liens)

    def a_quiz_modele(self, p: dict) -> Tache:
        nom = (p.get("nom") or "").strip()
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9 _-]{0,60}", nom):
            raise ValueError("nom du classeur : lettres sans accent, chiffres, espaces, - et _")
        dossier = self.dossier_du_cours("questions", chemins.DATA / "quizforge")
        f = dossier / f"{nom}.xlsx"
        if f.exists():
            raise ValueError(f"{rel(f)} existe déjà : choisissez un autre nom")
        dossier.mkdir(parents=True, exist_ok=True)
        argv = [PY, str(QB.QUIZFORGE), "modele", "--sortie", str(f)] + (["--vide"] if p.get("vide") else [])
        def apres(t):
            self.rattacher("questions", f)
            return {"classeur": rel(f)} if f.is_file() else {}
        return Tache(self.nouvel_id(), f"Créer le classeur « {f.name} »", "quizforge", argv, apres=apres)

    def a_quiz_fusionner(self, p: dict) -> Tache:
        f = QB.classeur_valide(p.get("classeur") or "")
        tr = QB.classeur_valide(p.get("traduction") or "")
        langue = C.langue_valide(p.get("langue") or "en")
        return Tache(self.nouvel_id(), f"Réunir « {f.name} » et « {tr.name} »", "quizforge",
                     [PY, str(QB.QUIZFORGE), "fusionner", str(f), str(tr), "--langue", langue], verrou=str(f.resolve()))

    # ------------------------------------------------------------------ DiagForge
    def a_diag_bilan(self, p: dict) -> Tache:
        d = QB.dossier_valide(p.get("dossier") or "")
        argv = ([PY, str(QB.DIAGFORGE), str(d)] + [str(QB.dossier_valide(x)) for x in (p.get("autres") or [])][:4]
                + self._profil(p) + self.option_cours())
        if p.get("questions"):
            argv += ["--questions", str(QB.fichier_dans(d, p["questions"], (".xml",)))]
        if p.get("roster"):
            argv += ["--roster", str(QB.fichier_dans(d, p["roster"], (".csv", ".xlsx")))]
        tent = p.get("tentatives") or "toutes"
        if tent not in ("toutes", "premiere", "derniere", "meilleure"):
            raise ValueError("tentatives : toutes, premiere, derniere ou meilleure")
        argv += ["--tentatives", tent]
        if p.get("sans_images"):
            argv.append("--sans-images")
        return Tache(self.nouvel_id(), f"Bilan de « {d.name} »", "diagforge", argv, verrou=str(d.resolve()),
                     apres=lambda t: QB.liens_bilan(d, t.debut))

    def ouvrir(self, p: dict) -> dict:
        """Ouvre un fichier du dépôt avec son programme habituel (Excel, navigateur…)."""
        f = dans_depot(p.get("chemin") or "")
        if not f.is_file() or f.suffix.lower() not in (".xlsx", ".html", ".md", ".txt", ".xml", ".csv", ".pdf", ".yaml", ".docx", ".odt", ".pptx"):
            return {"ok": False, "message": "fichier introuvable ou d'un type que l'atelier n'ouvre pas"}
        cle, maintenant = "ouvrir:" + str(f), time.time()
        if maintenant - self.montres.get(cle, 0) < 8:
            return {"ok": True, "deja": True}
        self.montres[cle] = maintenant
        if WINDOWS:
            avant = set(fenetres())
            os.startfile(str(f))                         # noqa: S606 (fichier du dépôt)
            threading.Thread(target=premier_plan, args=(avant, f.stem, 20.0, False), daemon=True).start()
        else:
            subprocess.Popen(["xdg-open", str(f)], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return {"ok": True}

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
        """Ouvre l'explorateur sur un fichier (sélectionné) ou un dossier du dépôt, au premier plan.

        Une même demande répétée dans les 8 s est ignorée (l'explorateur met parfois du temps à s'ouvrir : sans cela,
        chaque clic en ouvrirait un de plus).
        """
        f = dans_depot(p.get("chemin") or "")
        if not f.exists():
            return {"ok": False, "message": "introuvable : " + rel(f)}
        cle, maintenant = str(f), time.time()
        if maintenant - self.montres.get(cle, 0) < 8:
            return {"ok": True, "deja": True}
        self.montres[cle] = maintenant
        if WINDOWS:
            avant = fenetres_explorateur()
            subprocess.Popen(["explorer", "/select,", str(f)] if f.is_file() else ["explorer", str(f)])
            dossier = f.parent if f.is_file() else f
            threading.Thread(target=premier_plan, args=(avant, dossier.name), daemon=True).start()
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


# --------------------------------------------------------------------------------------------- Windows : explorateur
def fenetres() -> dict:
    """Fenêtres visibles de premier niveau : {hwnd: (classe, titre)}."""
    import ctypes
    from ctypes import wintypes
    u = ctypes.windll.user32
    trouvees = {}
    classe, titre = ctypes.create_unicode_buffer(64), ctypes.create_unicode_buffer(300)

    @ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    def chaque(hwnd, _):
        if u.IsWindowVisible(hwnd):
            u.GetClassNameW(hwnd, classe, 64)
            u.GetWindowTextW(hwnd, titre, 300)
            trouvees[hwnd] = (classe.value, titre.value)
        return True
    u.EnumWindows(chaque, 0)
    return trouvees


def fenetres_explorateur() -> set:
    """Fenêtres de l'explorateur Windows ouvertes (classe CabinetWClass)."""
    return {h for h, (c, _) in fenetres().items() if c == "CabinetWClass"}


def premier_plan(avant, titre: str, delai: float = 6.0, explorateur: bool = True):
    """Met au premier plan la fenêtre qui vient de s'ouvrir.

    ``explorateur`` : une fenêtre d'explorateur nouvelle, ou déjà ouverte sur le dossier ``titre`` ; sinon : une fenêtre
    dont le titre contient ``titre`` (nom du fichier ouvert dans Excel, le navigateur…), nouvelle de préférence.
    Windows refuse le premier plan à un programme qui n'a pas la main (l'icône clignote dans la barre des tâches) :
    l'atelier emprunte la file d'entrée de la fenêtre active et simule un appui sur Alt, ce qui lève ce refus.
    """
    try:
        import ctypes
        from ctypes import wintypes
        u = ctypes.windll.user32
        debut, cible, cle = time.time(), None, titre.lower()
        while time.time() < debut + delai and not cible:
            time.sleep(0.2)
            f = fenetres()
            if explorateur:
                nouvelles = [h for h, (c, _) in f.items() if c == "CabinetWClass" and h not in avant]
                anciennes = [h for h, (c, x) in f.items() if c == "CabinetWClass" and x == titre]
            else:
                nouvelles = [h for h, (c, x) in f.items() if h not in avant and cle in x.lower()]
                anciennes = [h for h, (c, x) in f.items() if cle in x.lower()]
            if nouvelles:
                cible = nouvelles[0]
            elif anciennes and time.time() > debut + 1.5:      # fenêtre réutilisée (dossier ou fichier déjà ouvert)
                cible = anciennes[0]
        if not cible:
            return
        if u.IsIconic(cible):
            u.ShowWindow(cible, 9)                       # SW_RESTORE
        k = ctypes.windll.kernel32
        devant = u.GetForegroundWindow()
        fil_devant = u.GetWindowThreadProcessId(devant, None)
        fil_cible = u.GetWindowThreadProcessId(cible, None)
        ici = k.GetCurrentThreadId()
        VK_MENU, KEYUP = 0x12, 0x0002
        attaches = []
        for fil in {fil_devant, fil_cible} - {ici, 0}:      # partager la file d'entrée de la fenêtre qui a la main
            if u.AttachThreadInput(ici, fil, True):
                attaches.append(fil)
        try:
            u.keybd_event(VK_MENU, 0, 0, 0)
            u.keybd_event(VK_MENU, 0, KEYUP, 0)
            u.BringWindowToTop(wintypes.HWND(cible))
            u.SetForegroundWindow(wintypes.HWND(cible))
            if u.GetForegroundWindow() != cible:
                u.SwitchToThisWindow(wintypes.HWND(cible), True)
        finally:
            for fil in attaches:
                u.AttachThreadInput(ici, fil, False)
    except Exception:                                    # premier plan impossible : la fenêtre reste ouverte
        pass


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


def profils_campus() -> dict:
    """Profils d'établissement et ce qu'ils disent des cours (``profil_cours`` : structure, vocabulaire, campus,
    parcours, formations, gabarits des codes et de la promo), complétés par les valeurs génériques."""
    import yaml
    out = {}
    for f in chemins.fichiers_profils():
        n = chemins.nom_profil(f)
        if n in out:
            continue
        try:
            d = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        except Exception:
            d = {}
        out[n] = PC.lire(d)
    return out


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
                return self._json({"ok": True, "fiches": at.versions_classeurs(at.filtre(at.fiches_exoforge(), "fiche")), "actif": at.cours_actif()})
            if chemin == "/api/quizforge/classeurs":
                return self._json({"ok": True, "classeurs": at.versions_classeurs(at.filtre(QB.classeurs(C.reglages().get("classeurs")), "classeur")),
                                   "actif": at.cours_actif()})
            if chemin == "/api/diagforge/dossiers":
                return self._json({"ok": True, "dossiers": at.filtre(QB.dossiers_exports(), "dossier"), "actif": at.cours_actif()})
            if chemin == "/api/reglages":
                return self._json({"ok": True, "reglages": C.reglages()})
            if chemin == "/api/appareils":
                return self._json(at.appareils())
            if chemin == "/api/capsules":
                return self._json({"ok": True, "capsules": at.filtre(C.liste(), "dossier"), "actif": at.cours_actif()})
            if chemin == "/api/cours":
                return self._json(at.cours_liste())
            if chemin == "/api/registre":
                q = dict(x.split("=", 1) for x in (url.query or "").split("&") if "=" in x)
                from urllib.parse import unquote
                try:
                    return self._json(at.registres({k: unquote(v) for k, v in q.items()}))
                except ValueError as e:
                    return self._json({"ok": False, "message": str(e)})
            if chemin == "/api/cours_reglages":
                return self._json(at.cours_reglages())
            if chemin == "/api/cours_sans":
                return self._json(at.cours_sans())
            if chemin.startswith("/api/cours/"):
                try:
                    return self._json(at.cours_detail(chemin[11:]))
                except ValueError as e:
                    return self._json({"ok": False, "message": str(e)})
            if chemin.startswith("/api/capsule/"):
                try:
                    return self._json({"ok": True, **C.detail(chemin[13:])})
                except ValueError as e:
                    return self._json({"ok": False, "message": str(e)})
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
                if chemin == "/api/envoyer":
                    t = at.taches.get(p.get("id", ""))
                    ligne = p.get("ligne") if p.get("ligne") in ("pause", "fin", "etape") else None
                    return self._json({"ok": bool(t and ligne and t.envoyer(ligne))})
                if chemin == "/api/arreter":
                    t = at.taches.get(p.get("id", ""))
                    if t:
                        t.arreter()
                    return self._json({"ok": bool(t)})
                if chemin == "/api/parcourir":
                    return self._json(at.parcourir(p))
                if chemin == "/api/montrer":
                    return self._json(at.montrer(p))
                if chemin == "/api/tester_micro":
                    return self._json(at.tester_micro(p))
                if chemin == "/api/ouvrir":
                    return self._json(at.ouvrir(p))
                if chemin == "/api/cours":
                    return self._json(at.cours_action(p))
                if chemin == "/api/registre":
                    return self._json(at.registre_modifier(p))
                if chemin == "/api/reglages":
                    r = p.get("reglages") or {}
                    if "profil" in r:
                        if r["profil"] and r["profil"] not in noms_profils():
                            raise ValueError("profil inconnu")
                        C.garder_reglage("profil", r["profil"])
                    if "diaporamas" in r and r["diaporamas"] == {}:
                        C.garder_reglage("diaporamas", {})
                    if r.get("apparence") in ("auto", "jour", "nuit"):
                        C.garder_reglage("apparence", r["apparence"])
                    liste = C.reglages().get("classeurs") or []
                    if r.get("ajouter_classeur"):
                        f = QB.classeur_valide(r["ajouter_classeur"])
                        if str(f) not in liste:
                            C.garder_reglage("classeurs", liste + [str(f)])
                    if r.get("retirer_classeur"):
                        cible = str(QB.classeur_valide(r["retirer_classeur"]))
                        C.garder_reglage("classeurs", [x for x in liste if x != cible])
                    if r.get("classeurs") == []:
                        C.garder_reglage("classeurs", [])
                    return self._json({"ok": True, "reglages": C.reglages()})
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
    ap = argparse.ArgumentParser(description="AtelierForge : lancer les outils Forge depuis le navigateur.")
    ap.add_argument("--port", type=int, default=PORT)
    ap.add_argument("--sans-navigateur", action="store_true", help="ne pas ouvrir la page (essais)")
    a = ap.parse_args(argv)
    at = Atelier()
    srv, adresse = S.demarrer(gestionnaire(at), a.port)
    at.arreter = srv.shutdown
    page = f"{adresse}?j={at.jeton}"
    print(f"AtelierForge {VERSION} : {page}")
    print("Laisser cette fenêtre ouverte. Elle se ferme quand la page est fermée (ou par « Quitter » dans la page).")
    S.servir(srv, page, not a.sans_navigateur)
    for t in at.taches.values():
        t.arreter()
    print("Atelier fermé.")


if __name__ == "__main__":
    main()
