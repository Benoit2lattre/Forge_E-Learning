"""CapsuleForge — équations natives d'Office (OMML) converties en LaTeX.

Les équations de PowerPoint (Insertion, Équation) sont écrites en OMML dans le diaporama. :func:`latex` en donne
le LaTeX, pour MathJax (volet « Texte » du lecteur, PDF) : fractions, racines, exposants et indices, parenthèses
et crochets, fonctions (exp, ln, sin…), sommes et intégrales, accents, matrices, lettres grecques et symboles
courants. Ce qui n'est pas reconnu garde son texte.

Licence : GPL v3.
"""
from __future__ import annotations

import unicodedata

M = "{http://schemas.openxmlformats.org/officeDocument/2006/math}"

GRECS = {"α": "alpha", "β": "beta", "γ": "gamma", "δ": "delta", "ε": "epsilon", "ϵ": "epsilon", "ζ": "zeta",
         "η": "eta", "θ": "theta", "ϑ": "vartheta", "ι": "iota", "κ": "kappa", "λ": "lambda", "μ": "mu", "ν": "nu",
         "ξ": "xi", "π": "pi", "ρ": "rho", "σ": "sigma", "ς": "varsigma", "τ": "tau", "υ": "upsilon", "φ": "phi",
         "ϕ": "phi", "χ": "chi", "ψ": "psi", "ω": "omega", "Γ": "Gamma", "Δ": "Delta", "Θ": "Theta", "Λ": "Lambda",
         "Ξ": "Xi", "Π": "Pi", "Σ": "Sigma", "Φ": "Phi", "Ψ": "Psi", "Ω": "Omega"}
SYMBOLES = {"−": "-", "×": r"\times ", "⋅": r"\cdot ", "·": r"\cdot ", "÷": r"\div ", "±": r"\pm ", "∓": r"\mp ",
            "≠": r"\neq ", "≤": r"\leq ", "≥": r"\geq ", "≈": r"\approx ", "≡": r"\equiv ", "∝": r"\propto ",
            "∞": r"\infty ", "∂": r"\partial ", "∇": r"\nabla ", "∈": r"\in ", "∉": r"\notin ", "⊂": r"\subset ",
            "∪": r"\cup ", "∩": r"\cap ", "→": r"\to ", "←": r"\leftarrow ", "⇒": r"\Rightarrow ", "⇔": r"\Leftrightarrow ",
            "∀": r"\forall ", "∃": r"\exists ", "∅": r"\emptyset ", "…": r"\ldots ", "⋯": r"\cdots ", "°": r"^{\circ}",
            "′": "'", "∗": "*", "∣": r"\mid ", "‖": r"\| ", "ℝ": r"\mathbb{R}", "ℕ": r"\mathbb{N}", "ℤ": r"\mathbb{Z}",
            "ℂ": r"\mathbb{C}", "ℏ": r"\hbar ", "ℓ": r"\ell ", "{": r"\{", "}": r"\}", "%": r"\%", "#": r"\#",
            "&": r"\&", "_": r"\_", " ": " ", "⁡": "", "⁢": "", "⁣": "", "⁤": ""}
FONCTIONS = {"exp", "ln", "log", "sin", "cos", "tan", "sinh", "cosh", "tanh", "arcsin", "arccos", "arctan", "max",
             "min", "lim", "sup", "inf", "det", "dim", "arg", "deg", "ker", "Pr", "gcd"}
GRANDS = {"∑": r"\sum", "∏": r"\prod", "∫": r"\int", "∬": r"\iint", "∭": r"\iiint", "∮": r"\oint", "⋃": r"\bigcup",
          "⋂": r"\bigcap"}
ACCENTS = {"̂": r"\hat", "̃": r"\tilde", "̄": r"\bar", "̅": r"\overline", "̇": r"\dot",
           "̈": r"\ddot", "⃗": r"\vec", "́": r"\acute", "̀": r"\grave", "̌": r"\check"}
DELIMS = {"(": "(", ")": ")", "[": "[", "]": "]", "{": r"\{", "}": r"\}", "|": "|", "‖": r"\|", "⟨": r"\langle",
          "⟩": r"\rangle", "⌊": r"\lfloor", "⌋": r"\rfloor", "⌈": r"\lceil", "⌉": r"\rceil", "": "."}


def _car(c: str) -> str:
    """Un caractère de texte mathématique en LaTeX (lettres italiques mathématiques ramenées à leur lettre)."""
    if c in SYMBOLES:
        return SYMBOLES[c]
    if 0x1D400 <= ord(c) <= 0x1D7FF:                  # 𝑥, 𝜎… : lettres mathématiques Unicode
        nom = unicodedata.name(c, "")
        base = unicodedata.normalize("NFKC", c)
        if "GREEK" in nom or base in GRECS:
            return "\\" + GRECS.get(base, base) + " " if base in GRECS else base
        if "BOLD" in nom and "ITALIC" not in nom:
            return r"\mathbf{" + base + "}"
        return base
    if c in GRECS:
        return "\\" + GRECS[c] + " "
    return c


def _texte(t: str, droit: bool) -> str:
    brut = "".join(unicodedata.normalize("NFKC", c) if 0x1D400 <= ord(c) <= 0x1D7FF else c for c in t).strip()
    if brut in FONCTIONS:
        return "\\" + brut + " "
    if droit and len(brut) > 1 and brut.isalpha():
        return r"\mathrm{" + brut + "}"
    return "".join(_car(c) for c in t)


def _val(el, chemin: str, defaut=None):
    e = el.find(chemin)
    return e.get(M + "val", defaut) if e is not None else defaut


def _fils(el, nom: str) -> str:
    e = el.find(M + nom)
    return _suite(e) if e is not None else ""


def _suite(el) -> str:
    return "".join(_noeud(e) for e in el)


def _groupe(s: str) -> str:
    s = s.strip()
    return s if len(s) == 1 else "{" + s + "}"


def _noeud(e) -> str:
    t = e.tag
    if t == M + "r":
        droit = _val(e, M + "rPr/" + M + "sty") == "p" or e.find(M + "rPr/" + M + "nor") is not None
        return _texte("".join(x.text or "" for x in e.iter(M + "t")), droit)
    if t == M + "f":
        num, den = _fils(e, "num"), _fils(e, "den")
        typ = _val(e, M + "fPr/" + M + "type", "bar")
        if typ == "lin":
            return f"{num}/{den}"
        if typ == "noBar":
            return r"\genfrac{}{}{0pt}{}{" + num + "}{" + den + "}"
        return r"\frac{" + num + "}{" + den + "}"
    if t == M + "rad":
        deg = _fils(e, "deg").strip()
        cache = _val(e, M + "radPr/" + M + "degHide") in ("on", "1", "true")
        return r"\sqrt" + ("" if cache or not deg else "[" + deg + "]") + "{" + _fils(e, "e") + "}"
    if t == M + "sSup":
        return _groupe(_fils(e, "e")) + "^" + _groupe(_fils(e, "sup"))
    if t == M + "sSub":
        return _groupe(_fils(e, "e")) + "_" + _groupe(_fils(e, "sub"))
    if t == M + "sSubSup":
        return _groupe(_fils(e, "e")) + "_" + _groupe(_fils(e, "sub")) + "^" + _groupe(_fils(e, "sup"))
    if t == M + "sPre":
        return "{}_" + _groupe(_fils(e, "sub")) + "^" + _groupe(_fils(e, "sup")) + _fils(e, "e")
    if t == M + "d":
        pr = e.find(M + "dPr")
        deb = _val(pr, M + "begChr", "(") if pr is not None else "("
        fin = _val(pr, M + "endChr", ")") if pr is not None else ")"
        sep = _val(pr, M + "sepChr", "|") if pr is not None else "|"
        corps = (" " + DELIMS.get(sep, sep) + " ").join(_suite(x) for x in e.findall(M + "e"))
        return r"\left" + DELIMS.get(deb, deb) + " " + corps + r" \right" + DELIMS.get(fin, fin)
    if t == M + "func":
        return _fils(e, "fName").strip() + " " + _groupe(_fils(e, "e")) if not _fils(e, "e").startswith(r"\left") \
            else _fils(e, "fName").strip() + _fils(e, "e")
    if t == M + "nary":
        pr = e.find(M + "naryPr")
        c = _val(pr, M + "chr", "∫") if pr is not None else "∫"
        op = GRANDS.get(c, _car(c))
        bas = "" if _val(pr, M + "subHide") in ("on", "1") else _fils(e, "sub")
        haut = "" if _val(pr, M + "supHide") in ("on", "1") else _fils(e, "sup")
        return op + (("_" + _groupe(bas)) if bas.strip() else "") + (("^" + _groupe(haut)) if haut.strip() else "") \
            + " " + _fils(e, "e")
    if t == M + "acc":
        c = _val(e, M + "accPr/" + M + "chr", "̂")
        return ACCENTS.get(c, r"\hat") + "{" + _fils(e, "e") + "}"
    if t == M + "bar":
        pos = _val(e, M + "barPr/" + M + "pos", "top")
        return (r"\overline{" if pos == "top" else r"\underline{") + _fils(e, "e") + "}"
    if t == M + "groupChr":
        pos = _val(e, M + "groupChrPr/" + M + "pos", "bot")
        return (r"\underbrace{" if pos == "bot" else r"\overbrace{") + _fils(e, "e") + "}"
    if t == M + "limLow":
        return _fils(e, "e").strip() + "_" + _groupe(_fils(e, "lim"))
    if t == M + "limUpp":
        return _fils(e, "e").strip() + "^" + _groupe(_fils(e, "lim"))
    if t == M + "eqArr":
        return r"\begin{aligned}" + r" \\ ".join(_suite(x) for x in e.findall(M + "e")) + r"\end{aligned}"
    if t == M + "m":
        lignes = [" & ".join(_suite(c) for c in ligne.findall(M + "e")) for ligne in e.findall(M + "mr")]
        return r"\begin{matrix}" + r" \\ ".join(lignes) + r"\end{matrix}"
    if t in (M + "box", M + "borderBox", M + "phant"):
        return _fils(e, "e")
    if t == M + "oMath":
        return _suite(e)
    if t.endswith("Pr") or t == M + "ctrlPr":
        return ""
    return _suite(e)


def latex(o_math) -> str:
    """LaTeX d'un élément ``m:oMath`` (ou ``m:oMathPara``), espaces superflus réduits."""
    if o_math.tag == M + "oMathPara":
        morceaux = [latex(x) for x in o_math.iter(M + "oMath")]
        return r" \\ ".join(m for m in morceaux if m)
    s = _noeud(o_math)
    return " ".join(s.split())
