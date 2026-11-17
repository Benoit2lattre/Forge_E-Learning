"""Figure de test pour le pointeur : vecteur contrainte et ses composantes (sans étiquettes)."""
import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

a = np.radians(65)                          # direction de la normale
n = np.array([np.cos(a), np.sin(a)])
t = np.array([np.sin(a), -np.cos(a)])       # tangente, côté du vecteur contrainte
T = 3 * (np.cos(np.radians(30)) * n + np.sin(np.radians(30)) * t)
sn, st = T @ n * n, T @ t * t               # composantes normale et tangentielle

C = {"axe": "#847E71", "n": "#28406B", "T": "#B85C50", "sn": "#5C8A66", "st": "#C98A3E", "proj": "#9B2743"}
fig, ax = plt.subplots(figsize=(10, 8), dpi=100)
ax.set_aspect("equal"); ax.axis("off")

# surface courbée (arc de cercle tangent en M, convexe du côté de n)
R = 3.2
th = np.linspace(-0.75, 0.75, 200)
centre = -R * n
arc = centre[:, None] + R * (np.outer(n, np.cos(th)) + np.outer(t, np.sin(th)))
ax.plot(*arc, color="#44403A", lw=2.5)
ax.fill(*np.hstack([arc, (centre + 0.85 * (arc.T - centre)).T[:, ::-1]]), color="#E3E0D9", lw=0)

# axes normal et tangent (trait mixte)
for d, L in ((n, (-0.6, 3.6)), (t, (-1.4, 2.4))):
    ax.plot(*np.outer(d, L), color=C["axe"], ls="-.", lw=1.4)

# projections (tirets) de l'extrémité de T vers les composantes
ax.plot(*np.array([T, sn]).T, color=C["proj"], ls="--", lw=1.4)
ax.plot(*np.array([T, st]).T, color=C["proj"], ls="--", lw=1.4)

# composantes (trait plein épais)
ax.plot(*np.array([[0, 0], sn]).T, color=C["sn"], lw=9, solid_capstyle="butt", alpha=.55, zorder=2)
ax.plot(*np.array([[0, 0], st]).T, color=C["st"], lw=9, solid_capstyle="butt", alpha=.55, zorder=2)

# vecteurs (trait plein + flèche)
def fleche(v, c, lw=2.6):
    ax.annotate("", xy=v, xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=c, lw=lw, mutation_scale=22, shrinkA=0, shrinkB=0), zorder=4)
fleche(n, C["n"]); fleche(T, C["T"])

ax.plot(0, 0, "o", color="#1A1815", ms=8, zorder=5)    # point M
ax.set_xlim(-2.6, 3.6); ax.set_ylim(-1.6, 3.4)
fig.subplots_adjust(0, 0, 1, 1)
fig.savefig("vecteur_contrainte.png", dpi=100)
print("|T| =", round(float(np.hypot(*T)), 3), " sigma_n =", round(float(T @ n), 3), " tau =", round(float(T @ t), 3))
