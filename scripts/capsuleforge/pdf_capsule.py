"""CapsuleForge — PDF d'une capsule (construire --pdf).

Le PDF est fait à partir du lecteur construit : mêmes images (habillage de l'édition, variantes, filigrane,
diapositives traduites), mêmes textes, même langue. Une page imprimable (``<sortie>/imprimer.html``) est écrite à côté
du lecteur, puis imprimée en PDF par Edge ou Chrome sans fenêtre (Edge est présent sur tout Windows). Sans navigateur,
la page reste : l'ouvrir et l'imprimer en PDF à la main.

Contenu : une couverture (logo, titre, cours, code, école, année, promo, enseignant, mentions, licence), puis, partie
par partie et section par section, chaque diapositive dans son dernier état (toutes ses apparitions) ; à la demande,
le texte dit, le texte de la diapositive (formules comprises) et de la place pour les notes, en marge ou dessous.
Pied de page et numéros de page sur chaque page sauf la couverture. Licence : GPL v3.
"""
from __future__ import annotations

import html
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

CONTENUS = ("texte", "diapo")                  # texte dit, texte de la diapositive
NOTES = ("aucune", "marge", "dessous")


def _typo(t: str, langue: str) -> str:
    """Espaces insécables du français (comme le lecteur) ; rien pour une autre langue."""
    if not isinstance(t, str) or not langue.startswith("fr"):
        return t
    t = re.sub(r"[   ]+([;!?])", " \\1", t)
    t = re.sub(r"[   ]+:(?!/)", " :", t)
    t = re.sub(r"«[   ]*", "« ", t)
    return re.sub(r"[   ]*»", " »", t)


def _e(t, langue: str = "fr") -> str:
    return html.escape(_typo(str(t or ""), langue))


def _tr(obj: dict, cle: str, langue: str, src: str) -> str:
    """Texte traduit d'un titre ou d'un objectif (``tr`` des données du lecteur), sinon le texte source."""
    if langue != src:
        t = ((obj.get("tr") or {}).get(langue) or {}).get(cle)
        if t:
            return t
    return obj.get(cle) or ""


def _image_finale(q: dict, langue: str) -> str | None:
    """Image d'un pas dans son dernier état (dernière apparition), dans la langue demandée s'il y a lieu."""
    f = q.get("fond")
    for a in sorted(q.get("apparitions") or [], key=lambda a: a[0] or 0):
        f = a[1] or f
    return ((q.get("fonds_tr") or {}).get(langue) or {}).get(f, f) if f else None


def _incrustes(q: dict, ecran: dict) -> str:
    """Vidéos insérées du pas, posées sur l'image finale : leur dernière image (la première si « rembobiner »),
    rien avec « masquer » (l'image posée à leur place sur la diapositive tient la zone)."""
    L, H = float(ecran.get("largeur") or 1920), float(ecran.get("hauteur") or 1080)
    out = []
    for v in q.get("incrustes") or []:
        im = None if v.get("m") else (v.get("af") if v.get("r") else v.get("fi"))
        if not im or not v.get("cadre"):
            continue
        x, y, l, h = v["cadre"]
        out.append(f'<img class="incruste" src="{html.escape(im)}" alt="" style="left:{100 * x / L:.3f}%;top:{100 * y / H:.3f}%;'
                   f'width:{100 * l / L:.3f}%;height:{100 * h / H:.3f}%">')
    return "".join(out)


def _texte_dit(q: dict, langue: str, src: str) -> str:
    phrases = [p[2] for p in q.get("phrases") or []]
    if langue != src:
        tr = (q.get("trad") or {}).get(langue) or []
        phrases = [tr[k] if k < len(tr) and tr[k] else t for k, t in enumerate(phrases)]
    return " ".join(p for p in phrases if p) or ((q.get("texte_tr") or {}).get(langue) if langue != src else None) \
        or (q.get("texte") or "")


def _liens(t: str, liens, langue: str) -> str:
    """Texte échappé, chaque texte lié devenu un lien."""
    morceaux, reste = [], t
    ok = [l for l in liens or [] if l[0] and re.match(r"(https?:|mailto:)", l[1] or "", re.I)]
    while reste:
        mieux = min(((reste.find(l[0]), l) for l in ok if l[0] in reste), default=None, key=lambda x: x[0])
        if not mieux:
            morceaux.append(_e(reste, langue))
            break
        i, l = mieux
        morceaux.append(_e(reste[:i], langue))
        morceaux.append(f'<a href="{html.escape(l[1])}">{_e(l[0], langue)}</a>')
        reste = reste[i + len(l[0]):]
    return "".join(morceaux)


def _diapo(q: dict, langue: str, src: str) -> str:
    out = []
    for b in q.get("diapo") or []:
        x = ((b.get("tr") or {}).get(langue) if langue != src else None) or b["x"]
        if b["k"] == "f":
            out.append(f'<div class="df">\\[{html.escape(b["x"])}\\]</div>')
        elif b["k"] == "c":
            lignes = "".join("<tr>" + "".join(f"<td>{_e(c, langue)}</td>" for c in l) + "</tr>" for l in x)
            out.append(f"<table>{lignes}</table>")
        else:
            style = f' style="margin-left:{1.2 * b["n"]}em"' if b.get("n") else ""
            out.append(f'<div class="{"dt" if b["k"] == "t" else "dp"}"{style}>{_liens(x, b.get("l"), langue)}</div>')
    return "".join(out)


def page(donnees: dict, langue: str | None = None, contenu=("texte",), notes: str = "aucune") -> tuple[str, bool]:
    """Écrit la page imprimable (HTML) d'une capsule à partir des données du lecteur ; renvoie ``(html, formules)``."""
    L = donnees.get("langues") or {}
    src = L.get("source") or "fr"
    langue = langue if langue in [src] + list(L.get("autres") or []) else src
    hab = donnees.get("habillage") or {}
    couleurs = hab.get("couleurs") or {}
    principal = couleurs.get("navy") or "#14213D"
    titre = _tr(donnees, "titre", langue, src) or "Capsule"
    formules = "diapo" in contenu and any(b.get("k") == "f" or b.get("m") for p in donnees["parties"] for s in p["sections"]
                                          for q in s["pas"] for b in q.get("diapo") or [])
    corps = []
    # couverture
    c = ['<section class="couverture">']
    if hab.get("logo"):
        c.append(f'<img class="logo" src="{html.escape(hab["logo"])}" alt="">')
    c.append(f"<h1>{_e(titre, langue)}</h1>")
    for k in ("cours", "ligne", "enseignant"):
        if hab.get(k):
            c.append(f'<p class="{k}">{_e(hab[k], langue)}</p>')
    if hab.get("mentions"):
        c.append(f'<p class="mentions">{_e(hab["mentions"], langue)}</p>')
    if hab.get("licence"):
        c.append(f'<p class="mentions">{_e(hab["licence"], langue)}</p>')
    c.append("</section>")
    corps.append("".join(c))
    for p in donnees["parties"]:
        sections = [s for s in p["sections"] if s.get("pas") or s.get("exercice")]
        if not sections:
            continue
        annexe = p.get("type") != "tronc"
        corps.append(f'<h1 class="partie">{_e(p.get("nom"))} — {_e(_tr(p, "titre", langue, src), langue)}'
                     + (' <span class="annexe">annexe</span>' if annexe else "") + "</h1>")
        for s in sections:
            corps.append(f'<h2>{_e(s.get("nom"))} — {_e(_tr(s, "titre", langue, src), langue)}</h2>')
            obj = _tr(s, "objectif", langue, src)
            if obj:
                corps.append(f'<p class="objectif">{_e(obj, langue)}</p>')
            if s.get("exercice"):
                corps.append(f'<p class="exercice">Exercice : à faire dans la capsule en ligne.</p>')
                continue
            for q in s["pas"]:
                bloc = []
                im = _image_finale(q, langue)
                if im:
                    bloc.append(f'<div class="scene"><img class="diapo" src="{html.escape(im)}" alt="">'
                                + _incrustes(q, donnees.get("ecran") or {}) + '</div>')
                if "diapo" in contenu and q.get("diapo"):
                    bloc.append(f'<div class="texte-diapo">{_diapo(q, langue, src)}</div>')
                if "texte" in contenu:
                    t = _texte_dit(q, langue, src)
                    if t:
                        bloc.append(f'<p class="dit">{_e(t, langue)}</p>')
                if not bloc:
                    continue
                if notes == "marge":
                    corps.append(f'<div class="pas marge"><div>{"".join(bloc)}</div><div class="lignes"></div></div>')
                elif notes == "dessous":
                    corps.append(f'<div class="pas">{"".join(bloc)}<div class="lignes dessous"></div></div>')
                else:
                    corps.append(f'<div class="pas">{"".join(bloc)}</div>')
    pied = hab.get("pied") or titre
    css_str = lambda t: '"' + str(t).replace("\\", "\\\\").replace('"', '\\"') + '"'
    police = f'"{hab["police_texte"]}", ' if hab.get("police_texte") else ""
    police_t = f'"{hab["police_titres"]}", ' if hab.get("police_titres") else police
    style = f"""
@page {{ size: A4; margin: 16mm 15mm 18mm;
  @bottom-left {{ content: {css_str(pied)}; font: 8pt {police}Verdana, sans-serif; color: #666; }}
  @bottom-right {{ content: counter(page) " / " counter(pages); font: 8pt {police}Verdana, sans-serif; color: #666; }} }}
@page :first {{ @bottom-left {{ content: none; }} @bottom-right {{ content: none; }} }}
* {{ box-sizing: border-box; }}
body {{ font-family: {police}Verdana, Arial, sans-serif; font-size: 10.5pt; line-height: 1.5; color: #1d1d1d; margin: 0; }}
h1, h2 {{ font-family: {police_t}Verdana, Arial, sans-serif; color: {principal}; }}
.couverture {{ height: 255mm; display: flex; flex-direction: column; justify-content: center; align-items: center;
  text-align: center; gap: 4mm; break-after: page; }}
.couverture .logo {{ max-height: 30mm; max-width: 80mm; margin-bottom: 8mm; }}
.couverture h1 {{ font-size: 26pt; margin: 0; }}
.couverture .cours {{ font-size: 14pt; margin: 0; }}
.couverture .ligne, .couverture .enseignant {{ font-size: 12pt; margin: 0; color: #333; }}
.couverture .mentions {{ font-size: 9pt; color: #555; margin: 0; }}
h1.partie {{ break-before: page; font-size: 17pt; border-bottom: 2px solid {principal}; padding-bottom: 2mm; }}
h1.partie .annexe {{ font-size: 10pt; color: #666; font-weight: normal; }}
h2 {{ font-size: 13pt; margin: 6mm 0 2mm; break-after: avoid; }}
.objectif {{ color: #444; margin: 0 0 4mm; }}
.exercice {{ color: #444; border-left: 3px solid {principal}; padding-left: 3mm; }}
.pas {{ break-inside: avoid; margin: 0 0 7mm; }}
.pas img.diapo {{ width: 100%; border: 1px solid #d8d8d8; display: block; }}
.pas .scene {{ position: relative; }}
.pas .scene img.incruste {{ position: absolute; display: block; }}
.marge {{ display: grid; grid-template-columns: 64% 1fr; gap: 5mm; }}
.lignes {{ background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='10' preserveAspectRatio='none'%3E%3Cline x1='0' y1='9.7' x2='10' y2='9.7' stroke='%23999999' stroke-width='0.8' vector-effect='non-scaling-stroke'/%3E%3C/svg%3E");
  background-size: 100% 7.5mm; background-repeat: repeat-y; min-height: 40mm; }}
.lignes.dessous {{ height: 45mm; margin-top: 2mm; }}
.dit {{ margin: 2mm 0 0; }}
.texte-diapo {{ margin: 2mm 0 0; padding: 1mm 3mm; border-left: 3px solid #d0d7e3; }}
.texte-diapo .dt {{ font-weight: bold; }}
.texte-diapo table {{ border-collapse: collapse; margin: 1mm 0; }}
.texte-diapo td {{ border: 1px solid #ccc; padding: 0.5mm 2mm; }}
a {{ color: inherit; }}
"""
    tete = [f'<!DOCTYPE html><html lang="{html.escape(langue)}"><head><meta charset="utf-8"><title>{_e(titre, langue)}</title>']
    if hab.get("polices_url"):
        tete.append(f'<link rel="stylesheet" href="{html.escape(hab["polices_url"])}">')
    tete.append(f"<style>{style}</style>")
    if formules:
        macros = json.dumps(donnees.get("latex_macros") or {}, ensure_ascii=False).replace("</", "<\\/")
        coul = json.dumps(donnees.get("latex_couleurs") or {}).replace("</", "<\\/")
        tete.append("""<script>window.MathJax = { tex: { packages: { "[+]": ["ams", "color"] }, macros: %s },
  svg: { fontCache: "global" }, startup: { typeset: false, ready() { MathJax.startup.defaultReady();
    const c = %s; const defs = Object.entries(c).map(([n, h]) => `\\\\definecolor{${n}}{RGB}{${parseInt(h.slice(1, 3), 16)},${parseInt(h.slice(3, 5), 16)},${parseInt(h.slice(5, 7), 16)}}`).join("");
    MathJax.startup.promise.then(() => { if (defs) MathJax.tex2svg(defs); return MathJax.typesetPromise(); }); } } };</script>
<script src="lecteur/mathjax.js"></script>""" % (macros, coul))
    tete.append("</head><body>")
    return "".join(tete) + "\n".join(corps) + "</body></html>", formules


def navigateur() -> str | None:
    """Edge ou Chrome (ou Chromium) installé, pour imprimer sans fenêtre ; variable ``FORGE_NAVIGATEUR`` d'abord."""
    if os.environ.get("FORGE_NAVIGATEUR") and Path(os.environ["FORGE_NAVIGATEUR"]).is_file():
        return os.environ["FORGE_NAVIGATEUR"]
    cands = []
    if sys.platform == "win32":
        for base in (os.environ.get("ProgramFiles(x86)"), os.environ.get("ProgramFiles"), os.environ.get("LOCALAPPDATA")):
            if base:
                cands += [Path(base) / "Microsoft/Edge/Application/msedge.exe", Path(base) / "Google/Chrome/Application/chrome.exe"]
    for c in cands:
        if c.is_file():
            return str(c)
    for nom in ("msedge", "microsoft-edge", "google-chrome", "chrome", "chromium", "chromium-browser"):
        w = shutil.which(nom)
        if w:
            return w
    return None


def imprimer(page_html: Path, pdf: Path, journal=print, attente_ms: int = 20000) -> bool:
    """Imprime la page en PDF avec Edge ou Chrome sans fenêtre ; renvoie vrai si le PDF est écrit."""
    nav = navigateur()
    if not nav:
        journal(f"  PDF : ni Edge ni Chrome trouvé ; ouvrir {page_html.name} et l'imprimer en PDF (Ctrl+P)")
        return False
    if pdf.exists():
        pdf.unlink()
    cmd = [nav, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--hide-scrollbars",
           f"--virtual-time-budget={attente_ms}", "--run-all-compositor-stages-before-draw",
           f"--print-to-pdf={pdf}", page_html.resolve().as_uri()]
    if sys.platform != "win32":
        cmd.insert(1, "--no-sandbox")
    try:
        subprocess.run(cmd, capture_output=True, timeout=180)
    except (OSError, subprocess.TimeoutExpired) as exc:
        journal(f"  PDF : l'impression a échoué ({type(exc).__name__}) ; ouvrir {page_html.name} et l'imprimer en PDF")
        return False
    if pdf.is_file() and pdf.stat().st_size > 1000:
        return True
    journal(f"  PDF : le navigateur n'a rien écrit ; ouvrir {page_html.name} et l'imprimer en PDF (Ctrl+P)")
    return False


def ecrire(donnees: dict, sortie: Path, nom: str, langue: str | None = None, contenu=("texte",), notes: str = "aucune",
           journal=print) -> Path | None:
    """Écrit ``<sortie>/imprimer.html`` puis ``<sortie>/<nom>.pdf`` ; renvoie le chemin du PDF, ou ``None``."""
    sortie = Path(sortie)
    texte, _ = page(donnees, langue, contenu, notes)
    p = sortie / "imprimer.html"
    p.write_text(texte, encoding="utf-8")
    pdf = sortie / f"{nom}.pdf"
    if imprimer(p, pdf, journal):
        journal(f"  PDF : {pdf} ({pdf.stat().st_size / 1e6:.1f} Mo)")
        return pdf
    return None
