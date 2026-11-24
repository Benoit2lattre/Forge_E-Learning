"""CapsuleForge — relecture d'un chapitre (serveur local + page relecture.html).

« capsuleforge relire fiabilite » démarre un petit serveur sur cet ordinateur seulement (127.0.0.1) et ouvre la
page de relecture : la diapositive, le son, et le texte dit, phrase par phrase. On y corrige le texte en
l'écoutant, on coupe ou on fusionne les phrases, et on pose les apparitions à l'instant voulu.

Les phrases horodatées d'un pas (``phrases``) sont la seule source du texte dit : la narration et, plus tard, les
sous-titres en sont tirés. À la première ouverture, elles sont préparées à partir de la narration et de la
transcription (``transcriptions/<id>.json``), sans rien écrire tant que l'on n'enregistre pas.

Routes du serveur (module :mod:`serveur_local`) : ::

  GET  /                  la page
  GET  /api/chapitre      le chapitre : pas, phrases, apparitions, mots horodatés de la transcription
  POST /api/pas           enregistre les pas modifiés dans chapitre.yaml (copie de l'ancien dans sauvegardes/)
  POST /api/fin           arrête le serveur (bouton « Quitter ») ; il s'arrête aussi seul quand la page est fermée
  POST /api/depart        la page se ferme ou se recharge : arrêt dans 4 s, sauf si elle revient
  POST /api/<action>      autres écrans (traduction…) : transmis à la méthode action de la séance
  GET  /media/<chemin>    une image ou un son du chapitre (lecture partielle acceptée, pour se déplacer dans le son)

Licence : GPL v3.
"""
from __future__ import annotations

import json
import re
import shutil
import threading
import time
from http.server import ThreadingHTTPServer
from pathlib import Path

import calage as CAL
import format_chapitre as F
import serveur_local as S
import transcription as T

ICI = Path(__file__).resolve().parent
TYPES = {".html": "text/html; charset=utf-8", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg",
         ".webp": "image/webp", ".mp3": "audio/mpeg", ".wav": "audio/wav", ".m4a": "audio/mp4", ".ogg": "audio/ogg"}


AJOUTS = ("spot", "cadre", "pointeur", "cache")       # objets que la page de relecture sait poser


class SeanceRelecture:
    """État du serveur de relecture pour un ``chapitre.yaml`` : lecture, écriture des pas, arrêt automatique.

    Une sous-classe peut définir ``PAGE`` (page HTML servie à la place de ``relecture.html``) et une méthode
    ``action(nom, donnees)`` appelée pour les autres requêtes ``POST /api/<nom>``.
    """

    def __init__(self, chemin: Path):
        self.arreter = lambda: None
        self.minuterie = None
        self.yaml = Path(chemin)
        self.dossier = self.yaml.parent
        self.sauvegarde_faite = False
        self.verrou = threading.Lock()

    def _pas(self, chap):
        """Parcourt les pas du chapitre ; produit des triplets (partie, section, pas)."""
        for partie in chap.get("parties") or []:
            for sec in partie.get("sections") or []:
                for pas in sec.get("pas") or []:
                    yield partie, sec, pas

    def remarques(self, chap: dict) -> tuple[dict, list]:
        """Résultat de :func:`format_chapitre.verifier` rangé pour la page : ``(remarques par pas, remarques générales)``.

        Chaque remarque est ``{"niveau": "erreur" | "avertissement", "texte": …}`` ; un message de la forme
        « D3-2 (d08) : … » est rangé sous le pas ``d08``, les autres (sections, parties, chapitre) sont générales.
        """
        try:
            err, av = F.verifier(chap, self.dossier)
        except Exception as e:  # la relecture reste utilisable même si la vérification échoue
            return {}, [{"niveau": "erreur", "texte": f"vérification impossible : {e}"}]
        ids = {q.get("id") for _, _, q in self._pas(chap)}
        par_pas, autres = {}, []
        for niveau, liste in (("erreur", err), ("avertissement", av)):
            for t in liste:
                m = re.match(r"^\S+ \(([^()]+)\) : (.+)$", t)
                if m and m.group(1) in ids:
                    par_pas.setdefault(m.group(1), []).append({"niveau": niveau, "texte": m.group(2)})
                else:
                    autres.append({"niveau": niveau, "texte": t})
        return par_pas, autres

    def lire(self) -> dict:
        """Renvoie le chapitre tel que la page l'affiche : pas non écartés, phrases, apparitions, objets, mots.

        Un pas sans ``phrases`` reçoit des phrases préparées à partir de la narration et de la transcription
        (marqué ``prepare``) ; rien n'est écrit sur le disque.
        """
        chap = F.lire(self.yaml)
        N = F.noms(chap)
        out = []
        for partie, sec, pas in self._pas(chap):
            if pas.get("ecarte"):
                continue
            CAL.appliquer_pas(pas, chap)                   # objets accrochés : instants d'après les phrases
            prepare = False
            phrases = pas.get("phrases")
            if not phrases:
                phrases = T.phrases_du_pas(pas, self.dossier) or []
                prepare = bool(phrases)
            f = self.dossier / "transcriptions" / f"{pas.get('id')}.json"
            mots = []
            if f.is_file():
                try:
                    mots = [[m["debut"], m["fin"]] for m in T.mots_du_fichier(json.loads(f.read_text(encoding="utf-8")))]
                except Exception:
                    mots = []
            out.append({
                "id": pas["id"], "nom": N.get(("pas", pas["id"]), pas["id"]),
                "section": f"{N.get(('section', partie.get('id'), sec.get('id')), '')} {F.texte(sec.get('titre'))}".strip(),
                "titre": (pas.get("source") or {}).get("titre") or "",
                "fond": pas.get("fond"), "audio": pas.get("audio"), "duree_s": pas.get("duree_s"),
                "phrases": [{"debut_s": ph.get("debut_s") if pas.get("audio") else None,
                             "fin_s": ph.get("fin_s") if pas.get("audio") else None, "texte": F.texte(ph.get("texte")),
                             **{k: ph[k] for k in ("variantes", "sauf", "pour", "pause_s") if ph.get(k) is not None and ph.get(k) != ""}}
                            for ph in phrases],
                "apparitions": [{"id": o["id"], "fichier": o.get("fichier"), "debut_s": o.get("debut_s") or 0,
                                 **{k: o[k] for k in CAL.CLES if o.get(k) is not None}}
                                for o in pas.get("objets") or [] if o.get("type") == "apparition"],
                "objets": [{k: o[k] for k in ("id", "type", "forme", "cadre", "position", "trajet", "couleur", "debut_s", "duree_s", "origine",
                                              *CAL.CLES) if k in o}
                           for o in pas.get("objets") or [] if o.get("type") in AJOUTS],
                "mots": mots, "prepare": prepare, "relu": (pas.get("source") or {}).get("relu") or "",
            })
        par_pas, generales = self.remarques(chap)
        reg = CAL.reglages(chap)
        return {"ok": True, "titre": F.texte(chap.get("titre")), "dossier": self.dossier.name,
                "calage": {"decalage_s": reg["decalage_s"], "pause_s": reg["pause_s"], "avant_s": reg["avant_s"],
                           "debit": CAL.debit(chap)},
                "variantes": [{"id": v.get("id"), "titre": F.texte(v.get("titre")) or v.get("id")}
                              for v in chap.get("variantes") or [] if v.get("id")],
                "ecran": chap.get("ecran") or {}, "pas": out, "remarques": par_pas, "generales": generales}

    def ecrire(self, modifs: dict) -> dict:
        """Enregistre dans ``chapitre.yaml`` les modifications envoyées par la page ; renvoie un compte rendu.

        ``modifs`` associe à l'identifiant d'un pas un dictionnaire pouvant contenir ``phrases`` (liste),
        ``apparitions`` (identifiant -> instant), ``objets`` (spots, cadres, pointeurs, caches) et ``relu``
        (booléen). Le chapitre est relu sur le disque et seuls ces champs sont changés ; une copie de l'ancien
        fichier est faite dans ``sauvegardes/`` à la première écriture.
        """
        with self.verrou:
            chap = F.lire(self.yaml)
            n = 0
            nouvelles: list[str] = []
            for _, _, pas in self._pas(chap):
                m = modifs.get(pas.get("id"))
                if not m:
                    continue
                n += 1
                if "phrases" in m:
                    src = (chap.get("langues") or {}).get("source") or "fr"
                    # une phrase dont le texte n'a pas changé garde ses traductions ({fr: …, en: …})
                    traduites = {" ".join(str(v.get(src) or "").split()): v for v in
                                 (ph.get("texte") for ph in pas.get("phrases") or []) if isinstance(v, dict)}
                    anciennes = {" ".join(F.texte(ph.get("texte")).split()): ph for ph in pas.get("phrases") or []}
                    phrases = []
                    for ph in m["phrases"]:
                        txt = " ".join(str(ph.get("texte") or "").split())
                        if not txt:
                            continue
                        x = {}
                        if ph.get("debut_s") is not None:
                            x["debut_s"] = round(float(ph["debut_s"]), 2)
                        if ph.get("fin_s") is not None:
                            x["fin_s"] = round(float(ph["fin_s"]), 2)
                        x["texte"] = dict(traduites[txt]) if txt in traduites else txt
                        for k in ("variantes", "sauf"):            # public de la phrase (variantes de la capsule)
                            ids = [str(v).strip() for v in ph.get(k) or [] if str(v).strip()][:20]
                            if ids:
                                x[k] = ids
                        pour = {str(v).strip(): " ".join(str(t).split()) for v, t in (ph.get("pour") or {}).items()
                                if str(v).strip() and str(t or "").strip()}
                        if pour:
                            x["pour"] = pour
                        connues = {v.get("id") for v in chap.get("variantes") or []}
                        for v in list(x.get("variantes") or []) + list(x.get("sauf") or []) + list(x.get("pour") or {}):
                            if v not in connues and v not in nouvelles:
                                nouvelles.append(v)
                        if txt in anciennes and anciennes[txt].get("audio_pour"):
                            x["audio_pour"] = anciennes[txt]["audio_pour"]
                        pause = ph.get("pause_s", (anciennes.get(txt) or {}).get("pause_s"))
                        if pause is not None and str(pause).strip() != "":
                            x["pause_s"] = round(min(max(float(pause), 0.0), 30.0), 2)
                        phrases.append(x)
                    if phrases:
                        if not m.get("accroches"):               # la page n'envoie pas les accroches : elles suivent ici
                            CAL.suivre_decoupage(pas, chap, phrases)
                        pas["phrases"] = phrases
                        pas.pop("narration", None)          # une seule source du texte dit : les phrases
                    else:
                        pas.pop("phrases", None)
                reg, t_ph = CAL.reglages(chap), CAL.temps(pas, chap)
                n_ph = len(pas.get("phrases") or [])

                def accroche_page(o, v):
                    """Accroche envoyée par la page (phrase, ancre, décalage) ; ``None`` : instant fixe."""
                    for k in CAL.CLES:
                        o.pop(k, None)
                    k = v.get("phrase")
                    if k is None or not n_ph:
                        return
                    o["phrase"] = min(max(int(k), 1), n_ph)
                    if v.get("ancre") == "fin":
                        o["ancre"] = "fin"
                    if v.get("decalage_s") is not None:
                        o["decalage_s"] = round(min(max(float(v["decalage_s"]), -30.0), 30.0), 2)
                for o in pas.get("objets") or []:
                    v = (m.get("apparitions") or {}).get(o.get("id")) if o.get("type") == "apparition" else None
                    if isinstance(v, dict):                    # page à jour : instant et accroche
                        accroche_page(o, v)
                        t = CAL.instant(o, t_ph, reg) if o.get("phrase") is not None else None
                        o["debut_s"] = t if t is not None else round(float(v.get("debut_s") or 0), 1)
                        continue
                    if o.get("type") == "apparition" and o.get("id") in (m.get("apparitions") or {}):
                        t = round(float(m["apparitions"][o["id"]]), 2)
                        if o.get("phrase") is not None and t_ph and abs(t - (CAL.instant(o, t_ph, reg) or 0)) > 0.05:
                            CAL.decalage(o, t, t_ph, reg)      # posé à la main : l'accroche garde ce réglage
                        o["debut_s"] = round(t, 1) if o.get("phrase") is None else CAL.instant(o, t_ph, reg) or t
                if "objets" in m:
                    accroches = {o.get("id"): o for o in pas.get("objets") or [] if o.get("phrase") is not None}
                    gardes = [o for o in pas.get("objets") or [] if o.get("type") not in AJOUTS]
                    pris = {o.get("id") for o in gardes}
                    for o in m["objets"]:
                        if o.get("type") not in AJOUTS:
                            continue
                        x = {"id": str(o.get("id") or ""), "type": o["type"]}
                        k = 1
                        while not x["id"] or x["id"] in pris:
                            x["id"] = f"o{k}"; k += 1
                        pris.add(x["id"])
                        if o.get("cadre"):
                            x["cadre"] = [int(round(float(v))) for v in o["cadre"][:4]]
                        if o.get("position"):
                            x["position"] = [int(round(float(v))) for v in o["position"][:2]]
                        if o.get("forme") == "ellipse" and o["type"] in ("spot", "cadre"):
                            x["forme"] = "ellipse"
                        if o.get("trajet") and o["type"] == "pointeur":
                            x["trajet"] = [[int(round(float(a))), int(round(float(b)))] for a, b in o["trajet"]]
                        if o.get("origine"):
                            x["origine"] = str(o["origine"])
                        if o.get("couleur"):
                            x["couleur"] = str(o["couleur"])[:9]
                        x["debut_s"] = round(float(o.get("debut_s") or 0), 1)
                        x["duree_s"] = round(max(0.1, float(o.get("duree_s") or 0)), 1)
                        if m.get("accroches") and o["type"] != "cache":   # page à jour : son accroche
                            accroche_page(x, o)
                            t = CAL.instant(x, t_ph, reg) if x.get("phrase") is not None else None
                            if t is not None:
                                x["debut_s"] = t
                            gardes.append(F.ordonner(x, F.ORDRE_OBJET))
                            continue
                        vieux = accroches.get(x["id"])
                        if vieux is not None and t_ph:            # objet accroché : il le reste
                            x.update({k: vieux[k] for k in CAL.CLES if k in vieux})
                            if abs(x["debut_s"] - (CAL.instant(x, t_ph, reg) or 0)) > 0.05:
                                CAL.decalage(x, x["debut_s"], t_ph, reg)
                        gardes.append(F.ordonner(x, F.ORDRE_OBJET))
                    if gardes:
                        pas["objets"] = gardes
                    else:
                        pas.pop("objets", None)
                src = pas.setdefault("source", {})
                if "relu" in m:
                    if m["relu"]:
                        src["relu"] = src.get("relu") or time.strftime("%Y-%m-%d")
                        src.pop("narration", None); src.pop("minutage", None)
                    else:
                        src.pop("relu", None)
                ordonne = F.ordonner(pas, F.ORDRE_PAS)
                pas.clear(); pas.update(ordonne)
            if not n:
                return {"ok": True, "message": "rien à enregistrer"}
            if not self.sauvegarde_faite:
                (self.dossier / "sauvegardes").mkdir(exist_ok=True)
                shutil.copy2(self.yaml, self.dossier / "sauvegardes" / f"chapitre_{time.strftime('%Y%m%d_%H%M%S')}.yaml")
                self.sauvegarde_faite = True
            if nouvelles:                                  # une variante nommée dans la relecture rejoint la liste du chapitre
                chap["variantes"] = list(chap.get("variantes") or []) + [{"id": v, "titre": v} for v in nouvelles]
            F.ecrire(chap, self.yaml)
            par_pas, generales = self.remarques(chap)
            return {"ok": True, "message": f"{n} pas enregistré(s)", "remarques": par_pas, "generales": generales}

    def page_partie(self):
        """Programme l'arrêt du serveur dans 4 s : la page se ferme ou se recharge (annulé si elle revient)."""
        self.page_revenue()
        self.minuterie = threading.Timer(4.0, self.arreter)
        self.minuterie.daemon = True
        self.minuterie.start()

    def page_revenue(self):
        """Annule l'arrêt programmé par :meth:`page_partie`."""
        if self.minuterie:
            self.minuterie.cancel()
            self.minuterie = None

    def media(self, rel: str) -> Path | None:
        """Renvoie le fichier du chapitre désigné par ``rel`` s'il est dans le dossier et d'un type servi, sinon ``None``."""
        f = (self.dossier / rel).resolve()
        if self.dossier.resolve() not in f.parents or f.suffix.lower() not in TYPES or not f.is_file():
            return None
        return f


def _gestionnaire(seance: SeanceRelecture):
    """Renvoie la classe de gestionnaire HTTP liée à ``seance`` (routes : voir l'en-tête du module)."""
    class G(S.Gestionnaire):
        protocol_version = "HTTP/1.1"

        def get(self, chemin, url):
            if chemin in ("/", "/index.html", "/api/chapitre"):
                seance.page_revenue()
            if chemin in ("/", "/index.html"):
                return self._envoyer(200, (ICI / getattr(seance, "PAGE", "relecture.html")).read_bytes(), S.TYPES[".html"])
            if chemin == "/api/chapitre":
                return self._json(seance.lire())
            if chemin.startswith("/media/"):
                return self._media(seance.media(chemin[7:]))
            self._introuvable()

        def post(self, chemin, corps):
            if chemin == "/api/pas":
                seance.page_revenue()
                return self._json(seance.ecrire(json.loads(corps.decode("utf-8"))))
            if chemin == "/api/fin":
                self._json({"ok": True})
                return threading.Thread(target=seance.arreter, daemon=True).start()
            if chemin == "/api/depart":
                seance.page_partie()
                return self._json({"ok": True})
            if chemin.startswith("/api/") and hasattr(seance, "action"):      # autres écrans (traduction…)
                seance.page_revenue()
                return self._json(seance.action(chemin[5:], json.loads(corps.decode("utf-8") or "{}")))
            self._introuvable()

    return G


def demarrer(chapitre_yaml: Path, port: int = 8775, seance=None) -> tuple[ThreadingHTTPServer, str]:
    """Crée le serveur sur le premier port libre à partir de ``port`` ; renvoie (serveur, adresse).

    ``seance`` permet de fournir une autre séance que :class:`SeanceRelecture` (écran de traduction, par exemple). Le
    serveur n'écoute que sur 127.0.0.1 et n'est pas encore lancé.
    """
    seance = seance or SeanceRelecture(chapitre_yaml)
    srv, adresse = S.demarrer(_gestionnaire(seance), port)
    seance.arreter = srv.shutdown
    return srv, adresse


def relire(chapitre_yaml: Path, port: int = 8775, navigateur: bool = True):
    """Lance la relecture d'un chapitre : serveur local et, si ``navigateur``, ouverture de la page.

    Bloque jusqu'à la fermeture de la page, au bouton « Quitter » ou à Ctrl+C.
    """
    if not Path(chapitre_yaml).is_file():
        raise SystemExit(f"Chapitre introuvable : {chapitre_yaml}")
    srv, adresse = demarrer(chapitre_yaml, port)
    print(f"Relecture de « {Path(chapitre_yaml).parent.name} » : {adresse}")
    print("Laisser cette fenêtre ouverte pendant la relecture. Elle se libère quand la page est fermée")
    print("(ou par le bouton « Quitter » de la page, ou par Ctrl+C ici).")
    S.servir(srv, adresse, navigateur)
    print("Relecture terminée.")
