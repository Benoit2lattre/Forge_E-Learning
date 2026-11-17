"""CapsuleForge — traduction d'un chapitre (format 2), en deux temps, quel que soit le moteur.

1. ``capsuleforge traduire <chapitre> --langue en [--moteur aucun|argos|deepl]``
   écrit ou complète ``<chapitre>/traductions/<langue>.yaml`` : un élément par texte à traduire (clé, source, cible,
   relu). Le moteur pré-remplit les cibles vides ; « aucun » les laisse vides (traduction à la main, par un
   collègue ou par un assistant d'IA). Une cible déjà écrite n'est jamais remplacée.
2. ``capsuleforge traduire <chapitre> --langue en --importer``
   recopie les cibles dans ``chapitre.yaml`` : le texte devient ``{fr: …, en: …}``. Une cible dont la source a changé
   depuis (phrase corrigée dans la relecture) est signalée et laissée de côté.

Textes traduits : titre du chapitre, titres des parties, titre / objectif / ouverture des sections, phrases dites
(sous-titres et voix de synthèse), narration d'un pas sans phrases, texte des bulles et textes posés sur l'image ;
textes des questions QuizForge posées en fin de section (énoncé, options, rétroactions, indices, unité) et textes
affichés des exercices ExoForge du chapitre. Ces deux dernières traductions restent dans ``traductions/<langue>.yaml``
(la banque et la fiche ne sont pas modifiées) et sont prises à la construction du lecteur ; « importer » ne les
recopie pas dans ``chapitre.yaml``.
Moteurs : « aucun » (gratuit), « argos » (Argos Translate, gratuit, hors ligne : ``pip install argostranslate``, modèle
téléchargé à la première utilisation), « deepl » (API DeepL ; clé dans la variable ``DEEPL_AUTH_KEY`` ; l'offre
« API Free » a un quota gratuit).
Licence : GPL v3.
"""
from __future__ import annotations

import re
import json
import os
import shutil
import time
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

import format_chapitre as F

MOTEURS = ("aucun", "argos", "deepl")


def _source(valeur, langue: str) -> str:
    if isinstance(valeur, dict):
        return str(valeur.get(langue) or "")
    return str(valeur or "")


def elements(chap: dict):
    """Produit le triplet ``(clé, objet parent, champ)`` de chaque texte traduisible du chapitre, dans l'ordre du fichier."""
    yield "chapitre/titre", chap, "titre"
    for c in chap.get("parcours") or []:
        yield f"parcours/{c.get('id')}/titre", c, "titre"
    for p in chap.get("parties") or []:
        yield f"partie/{p.get('id')}/titre", p, "titre"
        for s in p.get("sections") or []:
            for champ in ("titre", "objectif", "ouverture"):
                if s.get(champ):
                    yield f"section/{p.get('id')}/{s.get('id')}/{champ}", s, champ
            for q in s.get("pas") or []:
                if q.get("ecarte"):
                    continue
                if q.get("phrases"):
                    for k, ph in enumerate(q["phrases"]):
                        yield f"pas/{q.get('id')}/phrase/{k}", ph, "texte"
                elif q.get("narration"):
                    yield f"pas/{q.get('id')}/narration", q, "narration"
                for o in q.get("objets") or []:
                    if o.get("type") in ("bulle", "texte") and o.get("texte"):
                        yield f"objet/{q.get('id')}/{o.get('id')}/texte", o, "texte"


def _a_traduire(texte) -> bool:
    """Vrai si le texte contient des mots (au moins deux lettres) : « 4,75 », « β » ou « 2 » ne se traduisent pas."""
    return len(re.findall(r"[^\W\d_]", re.sub(r"\\[A-Za-z]+|<[^>]*>|\{=[^}]*\}", "", str(texte or "")))) >= 2


def elements_questions(chap: dict, dossier: Path):
    """Produit ``(clé, texte, contexte)`` pour chaque texte des questions QuizForge posées par le chapitre.

    Clés ``question/<banque>/<titre>/<chemin>`` ; une question posée par plusieurs sections n'apparaît qu'une fois.
    La banque n'est pas modifiée : la traduction reste dans le fichier du chapitre et sert à la construction.
    """
    import construire_chapitre as CH
    N = F.noms(chap)
    cache, vus = {}, set()
    for p in chap.get("parties") or []:
        for s in p.get("sections") or []:
            gs = f"{N.get(('section', p.get('id'), s.get('id')), '')} {F.texte(s.get('titre'))}".strip()
            for ref in s.get("questions") or []:
                if not isinstance(ref, dict) or not ref.get("banque"):
                    continue
                for x in CH.questions_ref(ref, dossier, cache, journal=lambda *a: None, sec_id=s.get("id")) or []:
                    for chemin, texte in CH.textes_question(x):
                        cle = f"{x['cle_tr']}/{chemin}"
                        if cle in vus or not _a_traduire(texte):
                            continue
                        vus.add(cle)
                        quoi = {"question": "énoncé", "feedback": "rétroaction générale", "feedback_juste": "rétroaction si juste",
                                "feedback_faux": "rétroaction si faux", "unite": "unité"}.get(chemin)
                        if not quoi:
                            k = chemin.split("/")
                            quoi = (f"option {int(k[1]) + 1}" + (" (rétroaction)" if k[2] == "feedback" else "")) if k[0] == "choix" else \
                                   f"rétroaction de l'erreur {int(k[1]) + 1}" if k[0] == "erreurs" else f"indice {int(k[1]) + 1}"
                        yield cle, texte, {"groupe": gs, "quoi": f"question « {x.get('titre')} » : {quoi}"}


def elements_exercices(chap: dict, dossier: Path):
    """Produit ``(clé, texte, contexte)`` pour chaque texte affiché des fiches ExoForge appelées par le chapitre.

    Clés ``exercice/<id>/<chemin>`` (chemins de :func:`construire_chapitre.textes_fiche`). La fiche n'est pas modifiée :
    à la construction, une page traduite de l'exercice est produite à côté de l'originale.
    """
    import construire_chapitre as CH
    vus = set()
    for p in chap.get("parties") or []:
        refs = p.get("exercice") or []
        for ref in [refs] if isinstance(refs, dict) else refs:
            if not isinstance(ref, dict) or not ref.get("fiche"):
                continue
            fiche = CH.fiche_exoforge(ref["fiche"], dossier)
            if not fiche:
                continue
            cfg = yaml.safe_load(fiche.read_text(encoding="utf-8")) or {}
            ident = cfg.get("id") or fiche.stem
            if ident in vus:
                continue
            vus.add(ident)
            titre = F.texte(cfg.get("titre")) or ident
            for chemin, texte in CH.textes_fiche({k: v for k, v in cfg.items() if k != "latex"}):
                if not _a_traduire(texte):
                    continue
                yield f"exercice/{ident}/{chemin}", texte, {"groupe": f"Exercice « {titre} »", "quoi": chemin.replace("/", " › ")}


def _pas_de(cle: str) -> str | None:
    return cle.split("/")[1] if cle.startswith(("pas/", "objet/")) else None


# --------------------------------------------------------------------------- moteurs

def _argos(textes: list[str], src: str, cible: str) -> list[str]:
    import argostranslate.package
    import argostranslate.translate
    installes = argostranslate.translate.get_installed_languages()
    if not any(l.code == src and any(t.to_lang.code == cible for t in l.translations_from) for l in installes):
        argostranslate.package.update_package_index()
        pq = next((x for x in argostranslate.package.get_available_packages()
                   if x.from_code == src and x.to_code == cible), None)
        if not pq:
            raise SystemExit(f"Argos : pas de modèle {src} → {cible}")
        print(f"Argos : téléchargement du modèle {src} → {cible}…")
        argostranslate.package.install_from_path(pq.download())
    return [argostranslate.translate.translate(t, src, cible) for t in textes]


def _deepl(textes: list[str], src: str, cible: str) -> list[str]:
    cle = os.environ.get("DEEPL_AUTH_KEY")
    if not cle:
        raise SystemExit("DeepL : mettre la clé de l'API dans la variable d'environnement DEEPL_AUTH_KEY")
    hote = "https://api-free.deepl.com" if cle.endswith(":fx") else "https://api.deepl.com"
    code = {"en": "EN-GB"}.get(cible, cible.upper())
    res = []
    for i in range(0, len(textes), 40):
        corps = urllib.parse.urlencode([("source_lang", src.upper()), ("target_lang", code)]
                                       + [("text", t) for t in textes[i:i + 40]]).encode()
        req = urllib.request.Request(hote + "/v2/translate", data=corps,
                                     headers={"Authorization": "DeepL-Auth-Key " + cle})
        with urllib.request.urlopen(req, timeout=60) as r:
            res += [t["text"] for t in json.loads(r.read().decode("utf-8"))["translations"]]
    return res


def _traduire(textes: list[str], src: str, cible: str, moteur: str) -> list[str]:
    if moteur == "argos":
        return _argos(textes, src, cible)
    if moteur == "deepl":
        return _deepl(textes, src, cible)
    return [""] * len(textes)


# --------------------------------------------------------------------------- les deux temps

def preparer(yaml_chap: Path, langue: str, moteur: str = "aucun", journal=print) -> Path:
    """Écrit ou complète ``traductions/<langue>.yaml`` et renvoie son chemin.

    Les cibles existantes sont gardées (retrouvées par clé, ou par texte source si la phrase a été découpée) ;
    le moteur ne remplit que les cibles vides. L'ancien fichier est d'abord copié en ``.yaml.bak`` horodaté.
    """
    chap = F.lire(yaml_chap)
    src = (chap.get("langues") or {}).get("source") or "fr"
    if langue == src:
        raise SystemExit(f"« {langue} » est la langue source du chapitre")
    fichier = yaml_chap.parent / "traductions" / f"{langue}.yaml"
    ancien = (yaml.safe_load(fichier.read_text(encoding="utf-8")) or {}) if fichier.is_file() else {}
    par_cle = {e["cle"]: e for e in ancien.get("elements") or []}
    par_texte = {(_pas_de(e["cle"]), e.get("source")): e for e in ancien.get("elements") or [] if e.get("cible")}
    elts = []
    for cle, parent, champ in elements(chap):
        source = " ".join(_source(parent.get(champ), src).split())
        if not source:
            continue
        deja = parent.get(champ).get(langue) if isinstance(parent.get(champ), dict) else None
        e = par_cle.get(cle)
        if e and e.get("source") != source:                 # phrase corrigée ou découpée : on cherche par le texte
            e = par_texte.get((_pas_de(cle), source))
        x = {"cle": cle, "source": source, "cible": (e or {}).get("cible") or deja or "",
             "relu": bool((e or {}).get("relu")) or bool(deja and not e)}
        if e and e.get("moteur"):
            x["moteur"] = e["moteur"]
        elts.append(x)
    for cle, texte, _ in list(elements_questions(chap, yaml_chap.parent)) + list(elements_exercices(chap, yaml_chap.parent)):
        source = " ".join(texte.split())
        e = par_cle.get(cle)
        x = {"cle": cle, "source": source, "cible": (e or {}).get("cible") or "", "relu": bool((e or {}).get("relu"))}
        if e and e.get("source") != source:          # question modifiée dans la banque : à retraduire
            x["cible"], x["relu"] = "", False
        if e and e.get("moteur") and x["cible"]:
            x["moteur"] = e["moteur"]
        elts.append(x)
    vides = [x for x in elts if not x["cible"]]
    if vides and moteur != "aucun":
        journal(f"  {len(vides)} texte(s) à traduire par {moteur}…")
        for x, t in zip(vides, _traduire([x["source"] for x in vides], src, langue, moteur)):
            x["cible"], x["moteur"], x["relu"] = t, moteur, False
    fichier.parent.mkdir(exist_ok=True)
    if fichier.is_file():
        shutil.copy2(fichier, fichier.with_name(f"{langue}_{time.strftime('%Y%m%d_%H%M%S')}.yaml.bak"))
    tete = (f"# Traduction {src} → {langue} du chapitre « {F.texte(chap.get('titre'), src)} ».\n"
            f"# Remplir « cible » (ou corriger celle du moteur), passer « relu » à true, puis :\n"
            f"#   capsuleforge traduire {yaml_chap.parent.name} --langue {langue} --importer\n")
    corps = {"source": src, "langue": langue, "elements": elts}
    fichier.write_text(tete + yaml.dump(corps, allow_unicode=True, sort_keys=False, width=110), encoding="utf-8")
    n = sum(1 for x in elts if x["cible"])
    journal(f"  {fichier} : {len(elts)} texte(s), {n} traduit(s), {sum(1 for x in elts if x['relu'])} relu(s)")
    return fichier


def importer(yaml_chap: Path, langue: str, journal=print) -> int:
    """Recopie les cibles de ``traductions/<langue>.yaml`` dans ``chapitre.yaml`` et renvoie le nombre de textes posés.

    Une cible dont la source a changé depuis la traduction est signalée et laissée de côté. Si un texte est posé,
    le chapitre est sauvegardé dans ``sauvegardes/`` et la langue ajoutée à ``langues.autres``.
    """
    fichier = yaml_chap.parent / "traductions" / f"{langue}.yaml"
    if not fichier.is_file():
        raise SystemExit(f"Pas de fichier de traduction : {fichier} (lancer d'abord « traduire » sans --importer)")
    trad = yaml.safe_load(fichier.read_text(encoding="utf-8")) or {}
    par_cle = {e["cle"]: e for e in trad.get("elements") or [] if e.get("cible")}
    chap = F.lire(yaml_chap)
    src = (chap.get("langues") or {}).get("source") or "fr"
    n, ecartes = 0, []
    for cle, parent, champ in elements(chap):
        e = par_cle.get(cle)
        if not e:
            continue
        source = " ".join(_source(parent.get(champ), src).split())
        if e.get("source") != source:
            ecartes.append(cle)
            continue
        v = parent.get(champ)
        v = dict(v) if isinstance(v, dict) else {src: v}
        if v.get(langue) != e["cible"]:
            v[langue] = e["cible"]
            parent[champ] = v
            n += 1
    if ecartes:
        journal(f"  {len(ecartes)} texte(s) dont la source a changé depuis la traduction (non importés) : "
                + ", ".join(ecartes[:8]) + (" …" if len(ecartes) > 8 else ""))
        journal("  relancer « traduire » sans --importer pour les remettre dans le fichier")
    if n:
        langues = chap.setdefault("langues", {"source": src})
        autres = langues.get("autres") or []
        if langue not in autres:
            langues["autres"] = autres + [langue]
        (yaml_chap.parent / "sauvegardes").mkdir(exist_ok=True)
        shutil.copy2(yaml_chap, yaml_chap.parent / "sauvegardes" / f"chapitre_{time.strftime('%Y%m%d_%H%M%S')}.yaml")
        F.ecrire(chap, yaml_chap)
    nonrelus = sum(1 for e in par_cle.values() if not e.get("relu"))
    journal(f"  {n} texte(s) {langue} posé(s) dans {yaml_chap.name}" + (f" ({nonrelus} non relu(s))" if nonrelus else ""))
    return n


# --------------------------------------------------------------------------- écran de relecture des traductions

def _contextes(chap: dict, langue: str, dossier: Path | None = None) -> dict:
    """Renvoie, pour chaque clé, le contexte affiché : groupe (section), diapositive à l'instant de la phrase, son d'origine, voix traduite."""
    N = F.noms(chap)
    ctx = {"chapitre/titre": {"groupe": "Chapitre", "quoi": "titre du chapitre"}}
    for c in chap.get("parcours") or []:
        ctx[f"parcours/{c.get('id')}/titre"] = {"groupe": "Chapitre", "quoi": "titre d'un parcours"}
    for p in chap.get("parties") or []:
        gp = f"{N.get(('partie', p.get('id')), '')} {F.texte(p.get('titre'))}".strip()
        ctx[f"partie/{p.get('id')}/titre"] = {"groupe": gp, "quoi": "titre de la partie"}
        for s in p.get("sections") or []:
            gs = f"{N.get(('section', p.get('id'), s.get('id')), '')} {F.texte(s.get('titre'))}".strip()
            for champ in ("titre", "objectif", "ouverture"):
                ctx[f"section/{p.get('id')}/{s.get('id')}/{champ}"] = {"groupe": gs, "quoi": f"{champ} de la section"}
            for q in s.get("pas") or []:
                objets = q.get("objets") or []
                def image(t):
                    f = q.get("fond")
                    for o in sorted((o for o in objets if o.get("type") == "apparition" and o.get("fichier")),
                                    key=lambda o: o.get("debut_s") or 0):
                        if (o.get("debut_s") or 0) <= t + 0.05:
                            f = o["fichier"]
                    return f
                v = (q.get("voix") or {}).get(langue) or {}
                for k, ph in enumerate(q.get("phrases") or []):
                    d = ph.get("debut_s")
                    c = {"groupe": gs, "quoi": f"{N.get(('pas', q.get('id')), q.get('id'))} · phrase {k + 1}",
                         "image": image(d or 0), "audio": q.get("audio"), "debut_s": d, "fin_s": ph.get("fin_s")}
                    if v.get("audio") and k < len(v.get("phrases") or []):
                        c["voix"] = {"audio": v["audio"], "debut_s": v["phrases"][k][0], "fin_s": v["phrases"][k][1]}
                    ctx[f"pas/{q.get('id')}/phrase/{k}"] = c
                ctx[f"pas/{q.get('id')}/narration"] = {"groupe": gs, "quoi": "narration du pas", "image": q.get("fond")}
                for o in objets:
                    ctx[f"objet/{q.get('id')}/{o.get('id')}/texte"] = {"groupe": gs, "quoi": f"texte de l'objet {o.get('id')}", "image": q.get("fond")}
    if dossier is not None:
        for cle, _, c in list(elements_questions(chap, dossier)) + list(elements_exercices(chap, dossier)):
            ctx[cle] = c
    return ctx


def _seance_traduction(yaml_chap: Path, langue: str):
    """Renvoie la séance de l'écran de relecture des traductions (actions « enregistrer » et « importer »)."""
    import relecture

    class SeanceTraduction(relecture.SeanceRelecture):
        PAGE = "traduction.html"

        def __init__(self):
            super().__init__(yaml_chap)
            self.langue = langue
            self.fichier = yaml_chap.parent / "traductions" / f"{langue}.yaml"
            self.copie_faite = False

        def _lire_fichier(self):
            texte = self.fichier.read_text(encoding="utf-8")
            return "".join(l for l in texte.splitlines(True) if l.startswith("#")), yaml.safe_load(texte) or {}

        def lire(self) -> dict:
            chap = F.lire(self.yaml)
            _, trad = self._lire_fichier()
            ctx = _contextes(chap, self.langue, self.dossier)
            elts = [dict(e, **{"contexte": ctx.get(e["cle"], {"groupe": "", "quoi": e["cle"]})}) for e in trad.get("elements") or []]
            return {"ok": True, "titre": F.texte(chap.get("titre")), "dossier": self.dossier.name,
                    "source": trad.get("source"), "langue": self.langue, "elements": elts}

        def action(self, nom: str, data: dict) -> dict:
            with self.verrou:
                if nom == "enregistrer":
                    tete, trad = self._lire_fichier()
                    par_cle = {e["cle"]: e for e in trad.get("elements") or []}
                    n = 0
                    for m in data.get("elements") or []:
                        e = par_cle.get(m.get("cle"))
                        if not e:
                            continue
                        cible = " ".join(str(m.get("cible") or "").split())
                        if cible != e.get("cible"):
                            e["cible"] = cible
                            e["moteur"] = (e.get("moteur") + " + relecture") if e.get("moteur") and "relecture" not in e["moteur"] else e.get("moteur") or "relecture"
                        e["relu"] = bool(m.get("relu"))
                        n += 1
                    if n:
                        if not self.copie_faite:
                            shutil.copy2(self.fichier, self.fichier.with_name(f"{self.langue}_{time.strftime('%Y%m%d_%H%M%S')}.yaml.bak"))
                            self.copie_faite = True
                        self.fichier.write_text(tete + yaml.dump(trad, allow_unicode=True, sort_keys=False, width=110), encoding="utf-8")
                    return {"ok": True, "message": f"{n} enregistré(s)"}
                if nom == "importer":
                    lignes = []
                    k = importer(self.yaml, self.langue, journal=lignes.append)
                    return {"ok": True, "message": " ".join(l.strip() for l in lignes), "poses": k}
            return {"ok": False, "message": f"action inconnue : {nom}"}

    return SeanceTraduction()


def relire_traduction(yaml_chap: Path, langue: str, port: int = 8776, navigateur: bool = True):
    """Prépare (ou met à jour) ``traductions/<langue>.yaml`` puis ouvre l'écran de relecture des traductions.

    Le serveur local tourne jusqu'à la fermeture de la page (ou Ctrl+C).
    """
    import relecture
    import serveur_local
    preparer(yaml_chap, langue, "aucun")
    srv, adresse = relecture.demarrer(yaml_chap, port, seance=_seance_traduction(yaml_chap, langue))
    print(f"Relecture de la traduction {langue} de « {yaml_chap.parent.name} » : {adresse}")
    print("Laisser cette fenêtre ouverte. Elle se libère quand la page est fermée (ou bouton « Quitter », ou Ctrl+C).")
    serveur_local.servir(srv, adresse, navigateur)
    print("Relecture de la traduction terminée.")
