"""CapsuleForge — images d'un diaporama, une par état d'animation, produites par PowerPoint (Windows).

PowerPoint est piloté par COM : le fichier est ouvert en lecture seule, sans fenêtre ; pour chaque état, les
formes et paragraphes qui ne sont pas encore apparus sont cachés en mémoire, puis la diapositive est exportée
en PNG. Rien n'est enregistré dans le diaporama. Si PowerPoint était déjà ouvert, il le reste.

Habillage (paramètre ``edition`` de :func:`exporter`) : les formes « cf édition … » et « cf nu » sont montrées ou
cachées selon le public, les champs ``{cours}``, ``{promo}``… sont remplis (vides pour la capsule nue ; une forme
qui n'a plus que des séparateurs est cachée), et, masque nu, les formes du masque (« Masquer les graphiques
d'arrière-plan ») et les pieds de page sans champ sont cachés ; le fond et les couleurs du thème restent. Avec
le modèle d'une école (``edition["modele"]``), ce modèle est appliqué au diaporama ouvert (jamais enregistré) et
son masque est montré ; les pieds de page de l'auteur restent cachés.

Dépendance : ``comtypes`` (déjà installé avec ``uiautomation``).
Licence : GPL v3.
"""
from __future__ import annotations

import sys
from pathlib import Path

MSO_GROUPE, MSO_MEDIA = 6, 16
CHAMPS = ("cours", "code", "bloc", "promo", "annee", "ecole", "declinaison", "edition", "enseignant", "capsule")


def _formes(diapo) -> dict:
    """Renvoie les formes d'une diapositive par identifiant, groupes dépliés."""
    out = {}
    coll = diapo.Shapes
    for i in range(1, coll.Count + 1):
        f = coll.Item(i)
        out[int(f.Id)] = f
        if int(f.Type) == MSO_GROUPE:
            g = f.GroupItems
            for j in range(1, g.Count + 1):
                out[int(g.Item(j).Id)] = g.Item(j)
    return out


def _paragraphe(forme, i: int):
    """Renvoie le paragraphe n° ``i`` (compté à partir de 1) du texte d'une forme.

    ``Paragraphs`` est une propriété à paramètres : selon la façon dont le pilotage dynamique la présente,
    elle s'indexe, s'appelle ou se parcourt ; les différentes formes d'accès sont essayées tour à tour.
    """
    plage = forme.TextFrame2.TextRange
    acces = plage.Paragraphs
    erreurs = []
    for essai in (lambda: acces[i, 1], lambda: acces(i, 1), lambda: acces.Item(i), lambda: plage.Paragraphs(i, 1)):
        try:
            par = essai()
            par.Font                                   # vérifie que c'est bien une plage de texte
            return par
        except Exception as exc:
            erreurs.append(f"{type(exc).__name__}: {exc}")
    raise RuntimeError("paragraphe inaccessible — " + " | ".join(erreurs))


def _plages(forme) -> list:
    """Renvoie les plages de texte d'une forme : son cadre de texte, ou les cellules d'un tableau."""
    out = []
    try:
        if int(forme.HasTextFrame) and int(forme.TextFrame.HasText):
            out.append(forme.TextFrame.TextRange)
    except Exception:
        pass
    try:
        if int(forme.HasTable):
            t = forme.Table
            for i in range(1, t.Rows.Count + 1):
                for j in range(1, t.Columns.Count + 1):
                    out.append(t.Cell(i, j).Shape.TextFrame.TextRange)
    except Exception:
        pass
    return out


SEPARATEURS = " \t·•|,;:/—–-"
FINS = "\r\n\v\x0b"


def _effacer(plage, cle: str) -> bool:
    """Efface un champ vide et un séparateur voisin (« Benoit Delattre - {code} » → « Benoit Delattre »).

    Champ en fin de ligne : le séparateur qui le précède part avec lui ; en début ou au milieu de ligne : celui
    qui le suit. Renvoie faux si le champ n'est plus dans le texte.
    """
    t = str(plage.Text)
    i = t.find(cle)
    if i < 0:
        return False
    j = i + len(cle)
    k = i
    while k > 0 and t[k - 1] in SEPARATEURS:
        k -= 1
    m = j
    while m < len(t) and t[m] in SEPARATEURS:
        m += 1
    debut, fin = (k, m) if (m == len(t) or t[m] in FINS) else (i, m)
    try:
        plage.Characters(debut + 1, fin - debut).Text = ""
    except Exception:                                   # à défaut, le champ seul
        r = plage.Find(cle)
        if r is None:
            return False
        r.Text = ""
    return True


def remplir(forme, valeurs: dict) -> str:
    """Remplace les champs ``{…}`` du texte d'une forme par ``valeurs``, mise en forme gardée ; un champ vide est
    effacé avec un séparateur voisin. Renvoie le texte obtenu."""
    import re
    texte = []
    for plage in _plages(forme):
        for nom in CHAMPS:
            cle = "{" + nom + "}"
            val = str(valeurs.get(nom) or "")
            for _ in range(50):                                 # chaque occurrence, sans boucle sans fin
                if cle not in str(plage.Text):
                    break
                if not val:
                    if not _effacer(plage, cle):
                        break
                    continue
                r = plage.Find(cle)
                if r is None:
                    break
                r.Text = val
        texte.append(str(plage.Text))
    return re.sub(r"\s+", " ", " ".join(texte)).strip()


def _vide(texte: str) -> bool:
    """Vrai si un texte n'a plus que des espaces et des séparateurs (« · », « - », « , »…)."""
    import re
    return not re.sub(r"[\s·•|,;:/—–\-()]+", "", texte or "")


def _masques(pres, valeurs: dict, journal) -> None:
    """Remplit les champs écrits dans les masques et les dispositions du diaporama (masque gardé)."""
    for i in range(1, pres.Designs.Count + 1):
        try:
            m = pres.Designs.Item(i).SlideMaster
            collections = [m.Shapes] + [m.CustomLayouts.Item(j).Shapes for j in range(1, m.CustomLayouts.Count + 1)]
        except Exception as exc:
            journal(f"  masque {i} : non lu ({type(exc).__name__})")
            continue
        for coll in collections:
            for k in range(1, coll.Count + 1):
                try:
                    remplir(coll.Item(k), valeurs)
                except Exception as exc:
                    journal(f"  masque : champ non rempli ({type(exc).__name__})")


def appliquer_modele(pres, modele: Path, numeros: list[int], journal) -> None:
    """Applique le modèle de l'école au diaporama ouvert (en mémoire, jamais enregistré) et vérifie que chaque
    diapositive garde sa disposition (appariée par son nom) ; sinon, la remet d'après son nom si le modèle l'a."""
    avant = {}
    for n in numeros:
        try:
            avant[n] = str(pres.Slides.Item(n).CustomLayout.Name)
        except Exception:
            pass
    pres.ApplyTemplate(str(Path(modele).resolve()))
    journal(f"  modèle {Path(modele).name} appliqué")
    par_nom = {}
    for i in range(1, pres.Designs.Count + 1):
        m = pres.Designs.Item(i).SlideMaster
        for j in range(1, m.CustomLayouts.Count + 1):
            lay = m.CustomLayouts.Item(j)
            par_nom.setdefault(str(lay.Name), lay)
    for n, nom in avant.items():
        diapo = pres.Slides.Item(n)
        try:
            apres = str(diapo.CustomLayout.Name)
        except Exception:
            continue
        if apres == nom:
            continue
        if nom in par_nom:
            try:
                diapo.CustomLayout = par_nom[nom]
                journal(f"  diapo {n} : disposition « {nom} » remise (PowerPoint avait choisi « {apres} »)")
                continue
            except Exception:
                pass
        journal(f"  diapo {n} : disposition « {nom} » absente du modèle, « {apres} » à la place : à vérifier")


def montree(f: dict, publics) -> bool:
    """Dit si une forme d'édition (``pptx_lire``) est montrée pour ces publics (``None`` : capsule nue)."""
    if f["cas"] == "nu":
        return publics is None
    return publics is not None and (not f["publics"] or bool(set(f["publics"]) & set(publics)))


def _powerpoint(journal):
    """Obtient PowerPoint et renvoie ``(application, déjà_ouverte)``.

    L'instance déjà ouverte est reprise si elle existe, sinon une nouvelle est créée ; si Windows refuse de
    la créer (« Échec de l'exécution du serveur »), PowerPoint est lancé comme par un double-clic puis rattaché.
    """
    import os
    import time
    import comtypes.client

    def actif():
        try:
            return comtypes.client.GetActiveObject("PowerPoint.Application", dynamic=True)
        except Exception:
            return None

    app = actif()
    if app is not None:
        journal("  PowerPoint déjà ouvert : je m'y rattache")
        return app, True
    try:
        return comtypes.client.CreateObject("PowerPoint.Application", dynamic=True), False
    except Exception as exc:
        journal(f"  création directe de PowerPoint refusée ({type(exc).__name__} {getattr(exc, 'winerror', '')}) : "
                "je le lance normalement et je m'y rattache")
    try:
        os.startfile("powerpnt.exe")
    except Exception as exc:
        raise SystemExit(f"PowerPoint ne se lance pas ({exc}). Est-il installé en version bureau ?")
    for _ in range(60):                               # jusqu'à 60 s : écran d'accueil, connexion du compte…
        time.sleep(1)
        app = actif()
        if app is not None:
            return app, False
    raise SystemExit(
        "PowerPoint s'est lancé mais ne répond pas aux commandes. Causes habituelles :\n"
        "  - une fenêtre de PowerPoint attend une réponse (connexion, activation, récupération de fichier) : la fermer ;\n"
        "  - ce terminal est lancé « en tant qu'administrateur » alors que PowerPoint ne l'est pas (ou l'inverse) ;\n"
        "  - PowerPoint vient du Microsoft Store, qui limite le pilotage : dans ce cas, dites-le-moi.\n"
        "Puis relancer la même commande, PowerPoint restant ouvert.")


def exporter(fichier: Path, diapos: list[dict], dossier: Path, largeur: int, journal=print,
             edition: dict | None = None) -> list[str]:
    """Écrit ``<dossier>/images/dNN_eK.png`` pour chaque état des diapositives données et renvoie les chemins relatifs écrits.

    ``diapos`` : diapositives issues de ``pptx_lire.lire`` ; ``largeur`` : largeur des images en pixels.
    ``edition`` : ``{publics, champs, masque, modele}`` — ``publics`` : écoles et variantes de l'édition, ``None``
    pour la capsule nue ; ``champs`` : valeurs des champs ; ``masque`` : ``nu`` (défaut) ou ``garder`` ;
    ``modele`` : modèle PowerPoint de l'école, appliqué avant l'export (son masque est alors montré). Sans ``edition``,
    tout est montré tel quel. Ne fonctionne que sous Windows, avec PowerPoint installé.
    """
    if sys.platform != "win32":
        raise SystemExit("L'export des images demande PowerPoint, donc Windows.")
    import comtypes
    import comtypes.client
    fichier, dossier = Path(fichier).resolve(), Path(dossier).resolve()
    (dossier / "images").mkdir(parents=True, exist_ok=True)
    comtypes.CoInitialize()
    app, deja_ouvert = _powerpoint(journal)
    pres = None
    ecrits = []
    signales: set = set()
    try:
        pres = app.Presentations.Open(str(fichier), -1, 0, 0)          # lecture seule, sans fenêtre
        hauteur = round(largeur * float(pres.PageSetup.SlideHeight) / float(pres.PageSetup.SlideWidth))
        valeurs = (edition or {}).get("champs") or {}
        garder = (edition or {}).get("masque") == "garder"
        modele = (edition or {}).get("modele")
        if modele:
            appliquer_modele(pres, Path(modele), [d["n"] for d in diapos], journal)
        montrer_masque = garder or bool(modele)              # masque neutre gardé, ou celui de l'école
        if edition is not None and montrer_masque:
            _masques(pres, valeurs, journal)
        for d in diapos:
            diapo = pres.Slides.Item(d["n"])
            formes = _formes(diapo)
            fixes: set = set()                                          # cachées dans tous les états
            if edition is not None:
                publics = edition.get("publics")
                fixes |= {f["spid"] for f in d.get("edition") or [] if not montree(f, publics)}
                champs = {int(k): v for k, v in (d.get("champs") or {}).items()}
                if not montrer_masque:
                    try:
                        diapo.DisplayMasterShapes = 0                   # « Masquer les graphiques d'arrière-plan »
                    except Exception as exc:
                        journal(f"  diapo {d['n']} : masque non caché ({type(exc).__name__})")
                if not garder:                                          # pied de page de l'auteur : jamais repris
                    fixes |= {s for s in d.get("pieds") or [] if s not in champs}
                for s in champs:
                    if s in fixes or s not in formes:
                        continue
                    try:
                        if _vide(remplir(formes[s], valeurs)):
                            fixes.add(s)                                # champ vide seul dans sa forme : cachée
                    except Exception as exc:
                        journal(f"  diapo {d['n']} : champs de la forme {s} non remplis ({type(exc).__name__} : {exc})")
                for s in fixes:
                    try:
                        formes[s].Visible = 0
                    except Exception:
                        pass
            for f in formes.values():                                   # icône de la narration : jamais montrée
                try:
                    if int(f.Type) == MSO_MEDIA:
                        f.Visible = 0
                except Exception:
                    pass
            for f in d.get("formes") or []:                             # annotations « cf … » : jamais sur l'image
                try:
                    formes[f["spid"]].Visible = 0
                except Exception as e:
                    journal(f"  diapositive {d['n']} : annotation « {f.get('nom')} » non cachée ({type(e).__name__})")
            # tout ce qu'une animation fait apparaître ou disparaître dans cette diapositive
            animes = {tuple(c) if isinstance(c, list) else c for e in d["etats"] for c in e}
            animes = {c for c in animes if (c[0] if isinstance(c, tuple) else c) not in fixes}
            # Du dernier état au premier : le texte ne fait alors que se cacher, jamais se remontrer. Remontrer
            # un paragraphe abîme sa puce (une puce image redevient un numéro), constaté sur un diaporama réel.
            par_caches: set = set()
            for k in reversed(range(len(d["etats"]))):
                caches = {tuple(c) if isinstance(c, list) else c for c in d["etats"][k]}
                for c in animes:
                    visible = c not in caches
                    try:
                        if isinstance(c, tuple):                        # paragraphes d'une forme
                            if visible == (c not in par_caches):
                                continue                                # déjà dans le bon état
                            for i in range(c[1] + 1, c[2] + 2):
                                par = _paragraphe(formes[c[0]], i)
                                par.Font.Fill.Transparency = 0.0 if visible else 1.0
                                try:
                                    par.ParagraphFormat.Bullet.Visible = -1 if visible else 0
                                except Exception:
                                    pass
                            if visible:
                                par_caches.discard(c)
                                journal(f"  diapo {d['n']} : paragraphes {c[1]}-{c[2]} remontrés (animation de sortie) : puce à vérifier")
                            else:
                                par_caches.add(c)
                        else:
                            formes[c].Visible = -1 if visible else 0
                    except KeyError:
                        journal(f"  diapo {d['n']} : forme {c} introuvable (ignorée)")
                    except Exception as exc:
                        if (d["n"], c) not in signales:                 # une fois par élément, avec le détail
                            signales.add((d["n"], c))
                            journal(f"  diapo {d['n']} : {c} non réglé ({type(exc).__name__} : {exc})")
                rel = f"images/d{d['n']:02d}_e{k}.png"
                diapo.Export(str(dossier / rel), "PNG", int(largeur), int(hauteur))
                ecrits.append(rel)
            journal(f"  diapo {d['n']} : {len(d['etats'])} image(s)")
    finally:
        if pres is not None:
            pres.Saved = -1
            pres.Close()
        if not deja_ouvert:
            try:
                app.Quit()
            except Exception:
                pass
    return ecrits
