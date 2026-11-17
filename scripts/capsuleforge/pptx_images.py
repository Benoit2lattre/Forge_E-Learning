"""CapsuleForge — images d'un diaporama, une par état d'animation, produites par PowerPoint (Windows).

PowerPoint est piloté par COM : le fichier est ouvert en lecture seule, sans fenêtre ; pour chaque état, les
formes et paragraphes qui ne sont pas encore apparus sont cachés en mémoire, puis la diapositive est exportée
en PNG. Rien n'est enregistré dans le diaporama. Si PowerPoint était déjà ouvert, il le reste.

Dépendance : ``comtypes`` (déjà installé avec ``uiautomation``).
Licence : GPL v3.
"""
from __future__ import annotations

import sys
from pathlib import Path

MSO_GROUPE, MSO_MEDIA = 6, 16


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


def exporter(fichier: Path, diapos: list[dict], dossier: Path, largeur: int, journal=print) -> list[str]:
    """Écrit ``<dossier>/images/dNN_eK.png`` pour chaque état des diapositives données et renvoie les chemins relatifs écrits.

    ``diapos`` : diapositives issues de ``pptx_lire.lire`` ; ``largeur`` : largeur des images en pixels.
    Ne fonctionne que sous Windows, avec PowerPoint installé.
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
        for d in diapos:
            diapo = pres.Slides.Item(d["n"])
            formes = _formes(diapo)
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
