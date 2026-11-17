"""QuizForge — graphiques du bilan (DiagForge) : images PNG pour les étudiants et la fiche du professeur.

Nécessite matplotlib (dans l'environnement : ``uv pip install matplotlib``). Sans matplotlib, le bilan
est produit sans images et le signale.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "commun"))
from charte import COULEUR_PRINCIPALE  # noqa: E402


def disponible():
    """Indique si matplotlib est installé (``True`` / ``False``)."""
    try:
        import matplotlib  # noqa: F401
        return True
    except ImportError:
        return False


def _plt():
    """Importe pyplot (moteur Agg, sans fenêtre) avec le style commun des graphiques et le renvoie."""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False,
                         "axes.titleweight": "bold", "axes.titlesize": 13, "figure.dpi": 150})
    return plt


def palette(principal=COULEUR_PRINCIPALE):
    """Renvoie la couleur principale du profil et une liste de teintes distinctes pour les groupes.

    Renvoie ``(principale, couleurs)`` ; ``couleurs`` commence par la couleur principale.
    """
    base = "#" + principal.lstrip("#")
    return base, [base, "#E0B989", "#4D62C9", "#6F8F78", "#DF231D", "#748CAB", "#FC4C02", "#9B2743"]


def histogramme(notes20, titre, sortie: Path, couleur="#" + COULEUR_PRINCIPALE, sous_titre=""):
    """Trace l'histogramme des notes sur 20 (classes de 2 points), avec moyenne et médiane.

    Enregistre l'image dans ``sortie`` et renvoie ce chemin.
    """
    import statistics
    plt = _plt()
    fig, ax = plt.subplots(figsize=(8, 4.2))
    bornes = list(range(0, 22, 2))
    ax.hist(notes20, bins=bornes, color=couleur, edgecolor="white", linewidth=1.5)
    if notes20:
        m, med = statistics.fmean(notes20), statistics.median(notes20)
        ax.axvline(m, color="#1D1D1D", linewidth=1.8, label=f"moyenne {m:.1f}")
        ax.axvline(med, color="#1D1D1D", linewidth=1.8, linestyle="--", label=f"médiane {med:.1f}")
        ax.legend(frameon=False, loc="upper left")
    ax.set_xlim(0, 20); ax.set_xticks(bornes)
    ax.set_xlabel("Note sur 20"); ax.set_ylabel("Nombre d'étudiants")
    ax.yaxis.get_major_locator().set_params(integer=True)
    ax.set_title(titre + (f"\n{sous_titre}" if sous_titre else ""), loc="left")
    fig.tight_layout(); fig.savefig(sortie); plt.close(fig)
    return sortie


def comparaison_groupes(par_groupe: dict, titre, sortie: Path, couleurs):
    """Trace les boîtes à moustaches des notes sur 20 par groupe, avec points individuels (anonymes) et effectifs.

    ``par_groupe`` : groupe → liste de notes. Enregistre l'image dans ``sortie`` et renvoie ce chemin.
    """
    import random
    plt = _plt()
    noms = list(par_groupe)
    fig, ax = plt.subplots(figsize=(max(7, 1.6 * len(noms) + 2), 4.2))
    b = ax.boxplot([par_groupe[g] for g in noms], patch_artist=True, widths=0.5, showfliers=False,
                   medianprops={"color": "#1D1D1D", "linewidth": 2})
    for k, (patch, g) in enumerate(zip(b["boxes"], noms)):
        patch.set_facecolor(couleurs[k % len(couleurs)]); patch.set_alpha(0.35)
        rnd = random.Random(k)
        ax.scatter([k + 1 + rnd.uniform(-0.12, 0.12) for _ in par_groupe[g]], par_groupe[g], s=14,
                   color=couleurs[k % len(couleurs)], zorder=3)
    ax.set_xticks(range(1, len(noms) + 1), [f"{g}\n(n = {len(par_groupe[g])})" for g in noms])
    ax.set_ylim(0, 20); ax.set_ylabel("Note sur 20")
    ax.set_title(titre, loc="left")
    fig.tight_layout(); fig.savefig(sortie); plt.close(fig)
    return sortie


def reussite(lignes, titre, sortie: Path, couleur, groupes=(), couleurs=()):
    """Trace en barres horizontales la réussite moyenne (%) par regroupement (tag, type…), promotion et groupes.

    ``lignes`` : ``[{"nom", "promo": fraction, "groupes": {g: fraction}, "n_questions"}]``, triées du plus
    faible au plus fort. Enregistre l'image dans ``sortie`` et renvoie ce chemin.
    """
    plt = _plt()
    lignes = list(reversed(lignes))          # le plus faible en haut
    h = 0.8 / (1 + len(groupes))
    fig, ax = plt.subplots(figsize=(8.5, max(2.6, 0.55 * len(lignes) * (1 + 0.5 * len(groupes)) + 1.2)))
    ys = range(len(lignes))
    barres = [("Promotion", [l["promo"] for l in lignes], couleur)]
    barres += [(g, [l["groupes"].get(g) for l in lignes], couleurs[(k + 1) % len(couleurs)]) for k, g in enumerate(groupes)]
    for j, (lab, vals, c) in enumerate(barres):
        pos = [y + (len(barres) - 1) * h / 2 - j * h for y in ys]
        ax.barh(pos, [100 * (v or 0) for v in vals], height=h * 0.92, color=c, label=lab, alpha=1 if j == 0 else 0.75)
        for p, v in zip(pos, vals):
            if v is not None:
                ax.text(100 * v + 1, p, f"{100 * v:.0f} %", va="center", fontsize=9)
    ax.set_yticks(list(ys), [f"{l['nom']}  ({l['n_questions']} q.)" for l in lignes])
    ax.set_xlim(0, 110); ax.set_xticks(range(0, 101, 20), [f"{x} %" for x in range(0, 101, 20)])
    ax.set_xlabel("Réussite moyenne")
    ax.axvline(50, color="#BBBBBB", linewidth=1, linestyle=":")
    if groupes:                               # légende au-dessus des barres, sous le titre
        ax.legend(frameon=False, loc="lower left", bbox_to_anchor=(0, 1.0), ncol=len(barres), fontsize=9)
        ax.set_title(titre, loc="left", pad=26)
    else:
        ax.set_title(titre, loc="left")
    fig.tight_layout(); fig.savefig(sortie); plt.close(fig)
    return sortie
