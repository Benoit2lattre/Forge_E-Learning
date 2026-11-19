"""Forge E-Learning — contrôle du dépôt avant commit.

Usage ::

    python scripts/commun/verifier_depot.py           # fichiers qui partiraient en ligne (suivis + nouveaux non ignorés)
    python scripts/commun/verifier_depot.py --index   # fichiers préparés pour le prochain commit (utilisé par .githooks/pre-commit)

Refuse :

- tout fichier sous un dossier local (``data/``, ``_legacy/``, ``_brouillons/``, ``_pilotage/``, ``.venv/``…, voir ``LOCAUX``) ;
- tout fichier de plus de 5 Mo ;
- les types lourds ou personnels (``.pptx``, ``.mp4``, ``.mov``, ``.aup3``, ``.approj``, ``.wav``, ``.m4a``) ;
- toute adresse de courriel qui n'est pas fictive (domaines autorisés dans ``DOMAINES_FICTIFS``).

Code de sortie 1 s'il y a un problème : le commit est alors annulé.
"""
import re
import subprocess
import sys
from pathlib import Path

RACINE = Path(__file__).resolve().parents[2]
LOCAUX = ("data/", "_legacy/", "_brouillons/", "_pilotage/", "Claude outputs/", ".venv/")
TYPES_INTERDITS = (".pptx", ".mp4", ".mov", ".aup3", ".approj", ".wav", ".m4a")
TAILLE_MAX = 5 * 1024 * 1024
DOMAINES_FICTIFS = ("exemple.fr", "exemple.com", "example.com", "example.org", "moodle.a",
                    "users.noreply.github.com", "noreply.github.com")
COURRIEL = re.compile(rb"[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{1,})")
IMAGE_DENSITE = re.compile(r"^\d+x\.(png|jpe?g|webp|gif|svg|avif)$")  # logo@2x.png : nom d'image, pas une adresse
TEXTE = (".py", ".md", ".txt", ".csv", ".yaml", ".yml", ".json", ".xml", ".html", ".tex", ".bib", ".css", ".js", ".gift", ".bat")


def fichiers(index: bool):
    """Renvoie la liste des fichiers à contrôler (chemins relatifs à la racine du dépôt).

    Avec ``index`` vrai : fichiers ajoutés, copiés, modifiés ou renommés dans l'index git
    (prochain commit) ; sinon : fichiers suivis et nouveaux fichiers non ignorés.
    Quitte le programme si git échoue.
    """
    cmd = ["git", "diff", "--cached", "--name-only", "--diff-filter=ACMR"] if index else \
          ["git", "ls-files", "--cached", "--others", "--exclude-standard"]
    sortie = subprocess.run(cmd, cwd=RACINE, capture_output=True, text=True, encoding="utf-8")
    if sortie.returncode:
        sys.exit(f"verifier_depot : git a échoué ({sortie.stderr.strip()})")
    return [l for l in sortie.stdout.splitlines() if l.strip()]


def controler(chemins):
    """Contrôle une liste de fichiers et renvoie la liste des problèmes (messages), vide si tout va bien.

    Signale les fichiers sous un dossier local, les types exclus, les fichiers trop gros et,
    dans les fichiers texte, la première adresse de courriel dont le domaine n'est pas fictif.
    """
    problemes = []
    for c in chemins:
        p = RACINE / c
        if c.startswith(LOCAUX):
            problemes.append(f"{c} : dossier local, ne doit pas être suivi")
            continue
        if not p.is_file():
            continue
        if p.suffix.lower() in TYPES_INTERDITS:
            problemes.append(f"{c} : type de fichier exclu ({p.suffix})")
        taille = p.stat().st_size
        if taille > TAILLE_MAX:
            problemes.append(f"{c} : {taille / 1e6:.1f} Mo (maximum {TAILLE_MAX / 1e6:.0f} Mo)")
        if p.suffix.lower() in TEXTE and taille <= TAILLE_MAX:
            contenu = p.read_bytes()
            for m in COURRIEL.finditer(contenu):
                dom = m.group(1).decode("ascii", "ignore").lower()
                if IMAGE_DENSITE.match(dom):
                    continue
                if not any(dom == d or dom.endswith("." + d) for d in DOMAINES_FICTIFS):
                    ligne = contenu[:m.start()].count(b"\n") + 1
                    problemes.append(f"{c}:{ligne} : adresse de courriel réelle ? ({m.group(0).decode('utf-8', 'ignore')})")
                    break
    return problemes


def main():
    """Point d'entrée : contrôle les fichiers et quitte avec le code 1 en cas de problème."""
    index = "--index" in sys.argv
    liste = fichiers(index)
    pbs = controler(liste)
    if pbs:
        print("verifier_depot : commit refusé\n - " + "\n - ".join(pbs), file=sys.stderr)
        print("Corrigez, ou retirez ces fichiers du commit (git restore --staged <fichier>).", file=sys.stderr)
        sys.exit(1)
    print(f"verifier_depot : {len(liste)} fichier(s) contrôlé(s), rien à signaler")


if __name__ == "__main__":
    main()
