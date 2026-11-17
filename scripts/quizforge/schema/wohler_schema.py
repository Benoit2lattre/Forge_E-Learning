#!/usr/bin/env python3
"""Prototype « Schéma » : courbe de Wöhler schématique + 3 questions glisser-déposer Moodle.

Usage ::

    python wohler_schema.py

Produit dans le dossier courant ::

    wohler_niveaux.png, wohler_transitions.png, wohler_domaines.png   (images de fond)
    wohler_schema_moodle.xml                                         (3 questions à importer)
    apercu_*.png                                                     (images avec les zones, pour contrôle)

Principe : la figure est tracée par le script, donc la position de chaque zone est calculée
à partir de coordonnées physiques (N, σ) et non mesurée à la main en pixels.
"""
import base64
import io
import sys
from pathlib import Path
from xml.sax.saxutils import escape

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Polygon as MplPolygon, Rectangle

LARGEUR, HAUTEUR, DPI = 600, 420, 100
L_ZONE = 170                         # largeur estimée d'une zone Moodle (dimensionnée sur l'étiquette la plus longue)
TAILLE_ZONE = {"ddimageortext": (170, 30), "ddimageortext_2l": (120, 52)}   # (largeur, hauteur) estimées


def borne(x, l=L_ZONE):
    """Arrondit l'abscisse ``x`` (pixels) d'une zone de largeur ``l`` pour qu'elle reste dans l'image (marge de 4 px)."""
    return round(min(max(x, 4), LARGEUR - l - 4))


COUL = {"courbe": "#28406B", "repere": "#847E71", "bande": "#D3DDEC", "texte": "#1A1815"}

# ---------------------------------------------------------------- courbe schématique (unités arbitraires)
RM, SIGMA_D = 600.0, 250.0           # plateau quasi statique, limite d'endurance
X0, K = 3.75, 1.3                    # centre et raideur de la transition (en log10 N)


def sigma(logn):
    """Renvoie l'amplitude de contrainte de la courbe schématique pour ``logn`` = log10 N (scalaire ou tableau).

    Courbe arrondie à 3 pentes : plateau Rm, pente de Basquin, plateau σD.
    """
    return SIGMA_D + (RM - SIGMA_D) / (1 + np.exp(K * (np.asarray(logn) - X0)))


RE = float(sigma(3.5))               # niveau de la transition oligo/poly (~ limite élastique)


# ---------------------------------------------------------------- figure
def figure(variante):
    """Trace la courbe de Wöhler schématique et renvoie ``(fig, ax)``.

    ``variante`` : ``"niveaux"`` (pointillés aux trois niveaux), ``"transitions"`` (bande de dispersion
    découpée par décade) ou ``"domaines"`` (bandes de couleur).
    """
    fig = plt.figure(figsize=(LARGEUR / DPI, HAUTEUR / DPI), dpi=DPI)
    ax = fig.add_axes([0.08, 0.13, 0.89, 0.82])
    x = np.linspace(-0.6, 9, 400)
    if variante == "transitions":
        dessiner_dispersion(ax)
    if variante == "domaines":
        dessiner_bandes(ax)
    ax.plot(x, sigma(x), color=COUL["courbe"], lw=2.6, zorder=5)
    ax.set_xlim(-0.6, 9)
    ax.set_ylim(0, 700)
    ax.set_xticks(range(0, 10))
    ax.set_xticklabels([f"$10^{{{i}}}$" for i in range(0, 10)], fontsize=9)
    ax.set_yticks([])
    ax.set_xlabel("Nombre de cycles à rupture N (échelle log)", fontsize=9, color=COUL["texte"])
    ax.set_ylabel("Amplitude de contrainte σ$_a$", fontsize=9, color=COUL["texte"])
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    if variante == "niveaux":
        for niv in (RM, RE, SIGMA_D):
            ax.axhline(niv, color=COUL["repere"], ls="--", lw=1)
    return fig, ax


# deux découpages superposés à la courbe : bande haute (oligo / poly), bande basse (limitée / illimitée)
BANDES = [  # (σ bas, σ haut, transition (a, b), couleur gauche, couleur droite)
    (330, 700, (3, 4), "#E0B989", "#748CAB"),
    (0, 215, (6, 7), "#6F8F78", "#BD7A5C"),
]


def _rgb(h):
    """Convertit une couleur ``#RRGGBB`` en tableau RVB de fractions entre 0 et 1."""
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)])


def dessiner_bandes(ax, alpha=0.45):
    """Dessine les bandes de ``BANDES`` : couleur différente de part et d'autre, dégradé dans la transition."""
    xs = np.linspace(-0.6, 9, 600)
    for bas, haut, (a, b), cg, cd in BANDES:
        t = np.clip((xs - a) / (b - a), 0, 1)[None, :, None]
        img = (1 - t) * _rgb(cg) + t * _rgb(cd)
        rgba = np.concatenate([img, np.full((1, len(xs), 1), alpha)], axis=2)
        ax.imshow(rgba, extent=(-0.6, 9, bas, haut), aspect="auto", zorder=1, interpolation="bilinear")


# dispersion : courbes 5 % et 95 % (décalage en contrainte), bande découpée par décade
DELTA = 48
DECADES = [(i, i + 1) for i in range(0, 9)]
COUL_DECADES = ["#D3DDEC", "#ECD2A8"]


def contour_decade(a, b, n=12):
    """Renvoie le contour ``[(log N, σ)…]`` de la bande de dispersion entre les décades ``a`` et ``b``."""
    xs = np.linspace(a, b, n)
    haut = [(x, sigma(x) + DELTA) for x in xs]
    bas = [(x, sigma(x) - DELTA) for x in xs[::-1]]
    return haut + bas


def dessiner_dispersion(ax):
    """Dessine la bande de dispersion découpée par décade et les courbes 5 %, 50 % et 95 %."""
    for k, (a, b) in enumerate(DECADES):
        ax.add_patch(MplPolygon(contour_decade(a, b), closed=True, fc=COUL_DECADES[k % 2],
                                ec="white", lw=1.5, zorder=2))
    x = np.linspace(-0.6, 9, 400)
    for d, nom in ((DELTA, "95 %"), (-DELTA, "5 %")):
        ax.plot(x, sigma(x) + d, color=COUL["repere"], lw=1, ls="--", zorder=3)
        ax.text(8.98, sigma(9) + d, nom, fontsize=8, color=COUL["repere"], ha="right",
                va="bottom" if d > 0 else "top")
    ax.text(8.98, sigma(9) + 4, "50 %", fontsize=8, color=COUL["courbe"], ha="right", va="bottom", zorder=6)


def vers_pixels(fig, ax, logn, s):
    """Convertit des coordonnées physiques (log N, σ) en pixels de l'image (origine en haut à gauche)."""
    xd, yd = ax.transData.transform((logn, s))
    return float(xd), float(HAUTEUR - yd)


def fig_vers_pixels(fig, fx, fy):
    """Convertit des coordonnées relatives à la figure (0 à 1) en pixels de l'image (origine en haut à gauche)."""
    return fx * LARGEUR, HAUTEUR - fy * HAUTEUR


def png(fig):
    """Renvoie l'image PNG de la figure, en octets."""
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=DPI)
    return buf.getvalue()


# ---------------------------------------------------------------- les trois questions
def q_niveaux():
    """Construit la question glisser-déposer sur image « nommer les trois niveaux de contrainte ».

    Renvoie ``(fig, question)``.
    """
    fig, ax = figure("niveaux")
    zones = []
    # étiquettes posées sur les pointillés, là où la courbe est loin
    for niv, logn, choix in ((RM, 5.5, 1), (RE, 6.5, 2), (SIGMA_D, 1.6, 3)):
        x, y = vers_pixels(fig, ax, logn, niv)
        zones.append({"x": borne(x - L_ZONE / 2), "y": round(y - 34), "choix": choix})
    etiquettes = ["Résistance à la traction R<sub>m</sub>", "Limite élastique R<sub>e</sub>",
                  "Limite d'endurance σ<sub>D</sub>", "Contrainte moyenne σ<sub>m</sub>"]
    return fig, {
        "type": "ddimageortext", "titre": "Wöhler-1 niveaux",
        "enonce": "<p>Placez sur la courbe de Wöhler schématique le nom de chacun des trois niveaux de "
                  "contrainte repérés en pointillés. Une étiquette est en trop.</p>",
        "feedback": "<p>Aux faibles nombres de cycles, la tenue est gouvernée par R<sub>m</sub> ; la transition "
                    "oligocyclique / polycyclique se situe vers R<sub>e</sub> ; le palier final est la limite "
                    "d'endurance σ<sub>D</sub>. La contrainte moyenne n'apparaît pas sur une courbe de Wöhler "
                    "tracée à σ<sub>m</sub> fixée.</p>",
        "etiquettes": etiquettes, "zones": zones}


def q_transitions():
    """Construit la question à marqueurs « pointer les deux zones de transition ».

    Les marqueurs se déposent dans la bande de dispersion découpée par décade ; les sept autres
    décades sont des leurres portés par la figure. Renvoie ``(fig, question)``.
    """
    fig, ax = figure("transitions")
    zones = []
    for (a, b), choix in (((3, 4), 1), ((6, 7), 2)):
        poly = [vers_pixels(fig, ax, x, y) for x, y in contour_decade(a, b)]
        zones.append({"forme": "polygon", "coords": ";".join(f"{round(x)},{round(y)}" for x, y in poly),
                      "choix": choix, "poly": poly})
    return fig, {
        "type": "ddmarker", "titre": "Wöhler-2 transitions",
        "enonce": "<p>La courbe de Wöhler est tracée avec sa dispersion (probabilités de rupture 5 %, 50 % et "
                  "95 %). La bande est découpée par décade. Déposez chaque marqueur dans la case où se situe la "
                  "transition qu'il désigne.</p>",
        "feedback": "<p>La transition oligocyclique / polycyclique se situe entre 10<sup>3</sup> et 10<sup>4</sup> "
                    "cycles, au niveau de la limite élastique. La transition endurance limitée / illimitée se "
                    "situe entre 10<sup>6</sup> et 10<sup>7</sup> cycles, au niveau de la limite d'endurance.</p>",
        "etiquettes": ["Oligocyclique / polycyclique", "Endurance limitée / illimitée"], "zones": zones}


def q_domaines():
    """Construit la question glisser-déposer sur image « nommer les quatre domaines » (bandes de couleur, une étiquette en trop).

    Renvoie ``(fig, question)``.
    """
    fig, ax = figure("domaines")
    lz, hz = TAILLE_ZONE["ddimageortext_2l"]
    zones = []
    # centre de chaque case (log N, σ), choisi dans la partie unie de la bande, loin de la courbe
    for logn, s_, choix in ((1.3, 455, 1), (6.5, 520, 2), (2.0, 105, 3), (8.05, 105, 4)):
        x, y = vers_pixels(fig, ax, logn, s_)
        zones.append({"x": borne(x - lz / 2, lz), "y": round(y - hz / 2), "choix": choix, "l": lz, "h": hz})
    etiquettes = ["Fatigue<br>oligocyclique", "Fatigue<br>polycyclique",
                  "Endurance<br>limitée", "Endurance<br>illimitée", "Fluage"]
    return fig, {
        "type": "ddimageortext", "titre": "Wöhler-3 domaines",
        "enonce": "<p>La courbe de Wöhler se découpe de deux façons : la bande du haut pour le premier découpage, "
                  "la bande du bas pour le second. Les dégradés indiquent les zones de transition approximatives. "
                  "Nommez chaque domaine. Une étiquette est en trop.</p>",
        "feedback": "<p>Premier découpage, autour de 10<sup>3</sup>–10<sup>4</sup> cycles : fatigue "
                    "oligocyclique (plasticité à chaque cycle) puis polycyclique. Second découpage, autour de "
                    "10<sup>6</sup>–10<sup>7</sup> cycles : endurance limitée puis illimitée (sous σ<sub>D</sub>, "
                    "pas de rupture attendue). Le fluage est un endommagement sous charge maintenue, pas un "
                    "domaine de la courbe de Wöhler.</p>",
        "etiquettes": etiquettes, "zones": zones}


# ---------------------------------------------------------------- Moodle XML
def _t(s):
    """Entoure un texte HTML d'une section CDATA."""
    return f"<![CDATA[{s}]]>"


def xml_question(q, image, nom_image):
    """Renvoie le XML Moodle d'une question glisser-déposer (``ddimageortext`` ou ``ddmarker``).

    ``image`` : octets PNG de l'image de fond, intégrée en base64 sous le nom ``nom_image``.
    """
    L = [f'  <question type="{q["type"]}">',
         f"    <name><text>{escape(q['titre'])}</text></name>",
         f'    <questiontext format="html"><text>{_t(q["enonce"])}</text></questiontext>',
         f'    <generalfeedback format="html"><text>{_t(q["feedback"])}</text></generalfeedback>',
         "    <defaultgrade>1</defaultgrade>", "    <penalty>0.3333333</penalty>", "    <hidden>0</hidden>",
         "    <shuffleanswers/>",
         '    <correctfeedback format="html"><text>Votre réponse est correcte.</text></correctfeedback>',
         '    <partiallycorrectfeedback format="html"><text>Votre réponse est partiellement correcte.</text></partiallycorrectfeedback>',
         '    <incorrectfeedback format="html"><text>Votre réponse est incorrecte.</text></incorrectfeedback>',
         "    <shownumcorrect/>"]
    if q["type"] == "ddmarker":
        L.append("    <showmisplaced/>")
    L.append(f'    <file name="{nom_image}" path="/" encoding="base64">{base64.b64encode(image).decode()}</file>')
    for i, e in enumerate(q["etiquettes"], 1):
        if q["type"] == "ddimageortext":
            L.append(f"    <drag><no>{i}</no><text>{_t(e)}</text><draggroup>1</draggroup></drag>")
        else:
            L.append(f"    <drag><no>{i}</no><text>{escape(e)}</text><noofdrags>1</noofdrags></drag>")
    for i, z in enumerate(q["zones"], 1):
        if q["type"] == "ddimageortext":
            L.append(f"    <drop><text></text><no>{i}</no><choice>{z['choix']}</choice>"
                     f"<xleft>{z['x']}</xleft><ytop>{z['y']}</ytop></drop>")
        else:
            L.append(f"    <drop><no>{i}</no><shape>{z['forme']}</shape><coords>{z['coords']}</coords>"
                     f"<choice>{z['choix']}</choice></drop>")
    L.append("  </question>")
    return "\n".join(L)


def apercu(fig, q, chemin):
    """Enregistre dans ``chemin`` une image de contrôle : zones et étiquettes dessinées par-dessus la figure."""
    ov = fig.add_axes([0, 0, 1, 1], facecolor="none")
    ov.set_xlim(0, LARGEUR); ov.set_ylim(HAUTEUR, 0); ov.axis("off")
    for z in q["zones"]:
        if "poly" in z:
            ov.add_patch(MplPolygon(z["poly"], fill=False, ec="#B85C50", lw=1.5, ls="--"))
            cx = sum(p[0] for p in z["poly"]) / len(z["poly"])
            cy = sum(p[1] for p in z["poly"]) / len(z["poly"])
        else:
            l, h = z.get("l", L_ZONE), z.get("h", 28)
            ov.add_patch(Rectangle((z["x"], z["y"]), l, h, fill=False, ec="#B85C50", lw=1.5, ls="--"))
            cx, cy = z["x"] + l / 2, z["y"] + h / 2
        ov.text(cx, cy, q["etiquettes"][z["choix"] - 1].replace("<sub>", "").replace("</sub>", "").replace("<br>", "\n"),
                ha="center", va="center", fontsize=7, color="#B85C50")
    fig.savefig(chemin, dpi=DPI)


def main():
    """Écrit dans le dossier courant les trois images, leurs aperçus et ``wohler_schema_moodle.xml``."""
    sortie = Path.cwd()
    blocs = ['<?xml version="1.0" encoding="UTF-8"?>', "<quiz>",
             '  <question type="category"><category><text>$course$/top/Prototype/Wohler_schema</text></category></question>']
    for fabrique, nom in ((q_niveaux, "niveaux"), (q_transitions, "transitions"), (q_domaines, "domaines")):
        fig, q = fabrique()
        image = png(fig)
        (sortie / f"wohler_{nom}.png").write_bytes(image)
        blocs.append(xml_question(q, image, f"wohler_{nom}.png"))
        apercu(fig, q, sortie / f"apercu_{nom}.png")
        plt.close(fig)
    blocs.append("</quiz>")
    (sortie / "wohler_schema_moodle.xml").write_text("\n".join(blocs) + "\n", encoding="utf-8")
    print("OK : wohler_schema_moodle.xml + 3 images + 3 aperçus")


if __name__ == "__main__":
    main()
