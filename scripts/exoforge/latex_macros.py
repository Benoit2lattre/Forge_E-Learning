"""Lecture des macros LaTeX de l'auteur (préambule IguanaTeX) pour MathJax.

- ``\\newcommand{\\nom}[n]{corps}`` → ``{"nom": ["corps", n]}`` (configuration MathJax ``tex.macros``) ;
- ``\\definecolor{Nom}{rgb}{r,g,b}`` → ``{"Nom": "#rrggbb"}`` (couleurs déclarées au chargement) ;
- ``\\colorlet{alias}{Nom}`` → même couleur (couleurs par rôle : ``roleDef``, ``rolePro``…).

Les ``\\usepackage``, ``\\include``, environnements et commandes non mathématiques sont ignorés.
"""
import re
from pathlib import Path

REMPLACEMENTS = {r"\mathbbm": r"\mathbb"}       # bbm n'existe pas dans MathJax


def _accolade(s: str, i: int):
    """Lit le groupe entre accolades qui commence en ``s[i]`` (qui vaut ``{``).

    Renvoie ``(contenu, indice après l'accolade fermante)`` ; lève ``ValueError`` si l'accolade n'est pas fermée.
    """
    prof, j = 0, i
    while j < len(s):
        if s[j] == "\\":
            j += 2
            continue
        if s[j] == "{":
            prof += 1
        elif s[j] == "}":
            prof -= 1
            if prof == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError("accolade non fermée")


def lire_macros(*fichiers):
    """Lit les fichiers LaTeX donnés et renvoie ``(macros, couleurs, ignorees)``.

    - ``macros`` : nom (sans barre oblique inverse) → corps, ou ``[corps, nombre d'arguments]`` ;
    - ``couleurs`` : nom → code ``#RRGGBB`` (``\\definecolor`` en ``rgb``, ``RGB`` ou ``HTML``, et alias ``\\colorlet``) ;
    - ``ignorees`` : extraits des définitions non comprises et des ``\\colorlet`` vers une couleur inconnue.

    Les commentaires ``%`` sont retirés avant la lecture ; ``\\mathbbm`` est remplacé par ``\\mathbb``.
    """
    macros, couleurs, ignorees = {}, {}, []
    for f in fichiers:
        txt = Path(f).read_text(encoding="utf-8", errors="replace")
        txt = "\n".join(re.sub(r"(?<!\\)%.*", "", l) for l in txt.splitlines())
        for m in re.finditer(r"\\(?:re)?newcommand\s*", txt):
            i = m.end()
            try:
                if txt[i] == "{":
                    nom, i = _accolade(txt, i)
                else:
                    nom = re.match(r"\\[A-Za-z]+", txt[i:]).group(0); i += len(nom)
                nom = nom.strip().lstrip("\\")
                while txt[i].isspace(): i += 1
                n = 0
                if txt[i] == "[":
                    k = txt.index("]", i); n = int(txt[i + 1:k]); i = k + 1
                while txt[i].isspace(): i += 1
                corps, i = _accolade(txt, i)
            except (ValueError, AttributeError, IndexError):
                ignorees.append(txt[m.start():m.start() + 40]); continue
            for a, b in REMPLACEMENTS.items():
                corps = corps.replace(a, b)
            corps = re.sub(r"\s+", " ", corps).strip()
            macros[nom] = [corps, n] if n else corps
        for m in re.finditer(r"\\definecolor\s*\{(\w+)\}\s*\{(rgb|RGB|HTML)\}\s*\{([^}]*)\}", txt):
            modele, val = m.group(2), m.group(3).strip()
            if modele == "HTML":
                couleurs[m.group(1)] = "#" + val.upper()
                continue
            r, g, b = (float(x) for x in val.split(","))
            k = 255 if modele == "rgb" else 1
            couleurs[m.group(1)] = "#%02X%02X%02X" % (round(r * k), round(g * k), round(b * k))
        # \colorlet{roleDef}{bleuE} : alias d'une couleur déjà définie (couleurs par rôle)
        for m in re.finditer(r"\\colorlet\s*\{(\w+)\}\s*\{(\w+)\}", txt):
            if m.group(2) in couleurs:
                couleurs[m.group(1)] = couleurs[m.group(2)]
            else:
                ignorees.append(f"\\colorlet{{{m.group(1)}}}{{{m.group(2)}}} : couleur inconnue")
    return macros, couleurs, ignorees


def couleurs_inconnues(macros, couleurs):
    """Repère les ``\\textcolor{X}`` vers une couleur jamais définie (faute de frappe).

    Renvoie la liste des couples ``(nom de la macro, couleur inconnue)`` ; les couleurs standard
    (``white``, ``black``, ``red``…) sont admises.
    """
    std = {"white", "black", "red", "green", "blue", "gray", "yellow", "orange"}
    out = []
    for nom, v in macros.items():
        corps = v[0] if isinstance(v, list) else v
        for c in re.findall(r"\\textcolor\{(\w+)\}", corps):
            if c not in couleurs and c not in std:
                out.append((nom, c))
    return out


if __name__ == "__main__":
    import json, sys
    m, c, ig = lire_macros(*sys.argv[1:])
    print(len(m), "macros,", len(c), "couleurs ; ignorées :", ig)
    print("couleurs inconnues :", couleurs_inconnues(m, c))
    print(json.dumps({k: m[k] for k in list(m)[:5]}, ensure_ascii=False))
