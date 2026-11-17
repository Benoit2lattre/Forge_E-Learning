"""ExoForge — construction des fiches génériques (étapes info / choix, rappel, audio, LaTeX).

Appelé par ``build.py`` quand la fiche contient « etapes ».

Deux temps, comme avec ActivePresenter :

1. construction initiale, sans média : l'exercice fonctionne, et ``media/<id>/script_enregistrement.md``
   liste chaque emplacement audio avec le texte à dire et les apparitions à marquer ;
2. reprise : les fichiers déposés dans ``media/<id>/`` sont pris en compte à la construction suivante ::

      <slot>.mp3 (ou .m4a, .wav, .ogg)  enregistrement
      <slot>_a1.mp3, <slot>_a2.mp3 …    ou : enregistrement découpé (dans Audacity) ; le segment k fait
                                        apparaître le k-ième élément, et les segments sont lus à la suite
      <slot>.txt                        transcription affichée sous l'étape (accessibilité)
      <slot>.reperes.json               temps d'apparition (fichier unique), relevés avec le mode auteur
      <id>_explication.mp3              facultatif : commentaire audio de l'explication d'une question
      <id>_retour_<lettre>.mp3          facultatif : commentaire audio du retour de la proposition a, b, c…

   Les noms sont reconnus sans tenir compte des majuscules (``rappel_PPV.mp3`` = ``rappel_ppv.mp3``) ;
   dans le paquet SCORM ils sont écrits en minuscules (Moodle distingue les majuscules).
"""
import difflib
import json
import re
import shutil
import sys
import zipfile
from html import escape
from pathlib import Path

import yaml

import latex_macros

RACINE = Path(__file__).resolve().parent
sys.path.insert(0, str(RACINE.parent / "commun"))
import chemins  # noqa: E402
MOTEUR = RACINE / "moteur" / "exercice.html"
FEUILLE = chemins.STYLE / "web" / "exercice.css"     # style générique, injecté dans la page
MATHJAX = RACINE / "moteur" / "vendor" / "mathjax-tex-svg-full.js"
EXT_AUDIO = (".mp3", ".m4a", ".wav", ".ogg")

# commandes LaTeX connues de MathJax (liste courte : sert seulement à signaler les macros inconnues)
CONNUES = set("""
forall exists in notin subset subseteq cup cap times cdot wedge vee perp parallel equiv approx sim neq leq geq le ge
int iint iiint oint sum prod lim infty partial nabla to rightarrow leftarrow Rightarrow Longrightarrow longrightarrow
mapsto Leftrightarrow iff implies quad qquad left right big Big bigg Bigg frac dfrac tfrac sqrt hat bar tilde vec dot ddot
underline overline mathbb mathscr mathcal mathrm mathbf mathit mathsf mbox text textrm textbf textit emptyset varnothing
begin end cases array matrix pmatrix bmatrix alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa
lambda mu nu xi pi varpi rho varrho sigma varsigma tau upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi
Sigma Upsilon Phi Psi Omega textcolor color colorbox definecolor displaystyle textstyle scriptstyle ldots cdots dots
vdots ddots prime circ bullet star ast pm mp div setminus mid langle rangle lbrace rbrace lvert rvert Vert vert stackrel
overset underset rule hspace vspace kern mathop operatorname limits nolimits sin cos tan exp log ln det dim ker min max
sup inf arg deg emph boldsymbol bm not neg land lor top bot angle triangle square Box diamond boxed
""".split())


def _cle(t):
    """Normalise un nom pour la comparaison : sans accents, en minuscules, lettres et chiffres seulement."""
    import unicodedata
    return re.sub(r"[^a-z0-9]", "", unicodedata.normalize("NFKD", str(t)).encode("ascii", "ignore").decode().lower())


def trouver_profil(nom):
    """Renvoie le fichier du profil demandé (``profils/<nom>/profil.yaml``).

    ``nom`` peut être le nom, un alias ou la première lettre (si elle ne désigne qu'un profil) ;
    sans nom, c'est le profil marqué ``defaut`` (ou ``None``). Le premier trouvé l'emporte
    (local, puis privé, puis dépôt). Quitte le programme si le nom n'est pas compris.
    """
    table, defaut = {}, None
    for g in chemins.fichiers_profils():
        lu = yaml.safe_load(g.read_text(encoding="utf-8")) or {}
        for a in [chemins.nom_profil(g)] + [str(x) for x in lu.get("alias", [])]:
            table.setdefault(_cle(a), g)
        if lu.get("defaut") and defaut is None:
            defaut = g
    if not nom:
        return defaut
    f = table.get(_cle(nom))
    if f is None:
        cands = {g for k, g in table.items() if k[:1] == _cle(nom)[:1]}
        if len(cands) != 1:
            sys.exit(f"Profil « {nom} » non compris. Possibles : {', '.join(sorted({chemins.nom_profil(g) for g in table.values()}))}")
        f = cands.pop()
        print(f"Compris : profil « {nom} » → {chemins.nom_profil(f)}")
    return f


def textes_tex(obj):
    """Énumère toutes les chaînes de la fiche, à toute profondeur (pour vérifier les macros)."""
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from textes_tex(v)
    elif isinstance(obj, list):
        for v in obj:
            yield from textes_tex(v)


def _fichiers_inclus(p: Path, schema=None) -> list[tuple[str, Path]]:
    """Renvoie les fichiers appelés par ``\\input`` / ``\\include`` dans ``p`` : ``(nom écrit, chemin)``.

    Un fichier est cherché à côté de ``p``, puis dans ``style/latex`` et les dossiers de profils ; le chemin
    renvoyé peut ne pas exister. Avec un ``schema`` de profil, le jeu de couleurs inclus (``…ColorScheme``) est
    sauté : il est remplacé par celui du profil.
    """
    res = []
    for inc in re.findall(r"^[^%\n]*\\(?:input|include)\{([^}]+)\}", p.read_text(encoding="utf-8", errors="replace"), re.M):
        if schema and "colorscheme" in inc.lower():
            continue
        q = p.parent / (inc if inc.endswith(".tex") else inc + ".tex")
        if not q.exists():                    # fichier inclus rangé ailleurs (style/latex, profils)
            q = next((d / q.name for d in chemins.dossiers_latex() if (d / q.name).exists()), q)
        res.append((inc, q))
    return res


def preparer_latex(cfg, dossier, avert, schema=None):
    """Lit les fichiers LaTeX de la fiche et renvoie ``(macros, couleurs)`` pour MathJax.

    Les fichiers de ``latex.fichiers`` sont cherchés à côté de la fiche, puis dans ``style/latex`` et
    les dossiers de profils ; leurs ``\\input`` / ``\\include`` sont suivis. Les macros de ``latex.macros``
    s'ajoutent ou remplacent. Une couleur mal tapée est remplacée par la plus proche.
    Les avertissements (fichier introuvable, macro inconnue…) sont ajoutés à la liste ``avert``.

    ``schema`` : jeu de couleurs LaTeX du profil (ex. ``Ecole1_ColorScheme.tex``) ; il remplace le
    ``\\include{…ColorScheme}`` du préambule, pour que ``\\TB``, ``\\TV``… prennent les couleurs de l'établissement.
    """
    L = cfg.get("latex") or {}
    fichiers = []
    for f in L.get("fichiers", []):
        p = (dossier / f).resolve()
        if not p.exists():                    # fiche déplacée : on cherche le fichier par son nom (style/latex, profils)
            p = next((d / Path(f).name for d in chemins.dossiers_latex() if (d / Path(f).name).exists()), p)
        if not p.exists():
            avert.append(f"fichier de macros introuvable : {f}")
            continue
        fichiers.append(p)
        # \input / \include d'autres fichiers du même dossier (ex. New_BD_ColorScheme)
        for _, q in _fichiers_inclus(p, schema):
            if q.exists() and q not in fichiers:
                fichiers.append(q)
    if schema:
        cands = [d / schema for d in [p.parent for p in fichiers] + [dossier / "../latex"] + chemins.dossiers_latex()]
        trouve = next((c.resolve() for c in cands if c.exists()), None)
        if trouve:
            fichiers.append(trouve)
        else:
            avert.append(f"jeu de couleurs du profil introuvable : {schema}")
    # fichiers inclus par les fichiers trouvés (ex. \\input{couleurs_roles} à la fin d'un jeu de couleurs)
    k = 0
    while k < len(fichiers):
        p = fichiers[k]; k += 1
        for inc, q in _fichiers_inclus(p, schema):
            if q.exists() and q.resolve() not in fichiers:
                fichiers.insert(k, q.resolve())
            elif not q.exists():
                avert.append(f"{p.name} : fichier inclus introuvable : {inc}")
    macros, couleurs, ignorees = latex_macros.lire_macros(*fichiers) if fichiers else ({}, {}, [])
    avert += [f"LaTeX : {x}" for x in ignorees if "colorlet" in x]
    for nom, v in (L.get("macros") or {}).items():
        macros[nom.lstrip("\\")] = v
    # couleurs mal tapées : la plus proche, avec avertissement
    for nom, col in latex_macros.couleurs_inconnues(macros, couleurs):
        proche = difflib.get_close_matches(col, list(couleurs), 1, 0.6)
        if proche:
            corps = macros[nom][0] if isinstance(macros[nom], list) else macros[nom]
            corps = corps.replace("{" + col + "}", "{" + proche[0] + "}")
            macros[nom] = [corps, macros[nom][1]] if isinstance(macros[nom], list) else corps
            avert.append(f"\\{nom} : couleur « {col} » inconnue, remplacée par « {proche[0]} » (corrigez le .tex)")
    utilisees = set()
    for t in textes_tex({k: v for k, v in cfg.items() if k != "latex"}):
        utilisees |= set(re.findall(r"\\([A-Za-z]+)", t))
    inconnues = sorted(u for u in utilisees if u not in macros and u not in CONNUES)
    if inconnues:
        avert.append("macros LaTeX inconnues (rendues en rouge) : " + ", ".join("\\" + u for u in inconnues))
    return macros, couleurs


def instances(e):
    """Renvoie les instances d'une étape sous forme de couples ``(suffixe, étape)``.

    Une seule, de suffixe vide, pour une étape simple ; suffixes ``"1"`` … ``"n"`` pour « repeter: n ».
    """
    n = e.get("repeter")
    if not n:
        return [("", e)]
    return [(str(i), e) for i in range(1, int(n) + 1)]


def slots(cfg):
    """Renvoie les emplacements audio ``(nom, étape)``, dans l'ordre de l'exercice.

    Une étape répétée donne ``bloc1``, ``bloc2``… ; la conclusion vient en dernier si elle a un audio.
    """
    out = []
    for e in cfg.get("etapes", []):
        if e.get("audio"):
            out += [(e["audio"] + suf, e) for suf, _ in instances(e)]
    c = cfg.get("conclusion") or {}
    if c.get("audio"):
        out.append((c["audio"], dict(c, titre=c.get("titre", "Conclusion"))))
    return out


def slots_facultatifs(cfg):
    """Renvoie les noms des commentaires audio facultatifs des questions.

    Pour une étape ``choix`` : explication et retour de chaque proposition ; pour une étape
    ``numerique`` : explication (si ``solution``) et aide.
    """
    out = []
    for e in cfg.get("etapes", []):
        for suf, _ in instances(e):
            ident = e["id"] + suf
            if e.get("type") == "choix":
                if e.get("explication"):
                    out.append(f"{ident}_explication")
                for k, o in enumerate(e.get("options", [])):
                    if isinstance(o, dict) and o.get("retour"):
                        out.append(f"{ident}_retour_{chr(97 + k)}")
            elif e.get("type") == "numerique":
                if e.get("solution"):
                    out.append(f"{ident}_explication")
                if (e.get("aide") or {}).get("texte"):
                    out.append(f"{ident}_aide")
    return out


def nb_apparitions(e):
    """Nombre d'éléments qui apparaissent avec le commentaire de l'étape."""
    n = len(e.get("contenu", [])) + (1 if e.get("enonce") else 0)
    if e.get("options_une_par_une"):
        n += len(e.get("options", []))
    return n


def _brut(t):
    """Convertit un texte de fiche en texte brut lisible (pour le script d'enregistrement)."""
    t = re.sub(r"\{=([^{}]+)\}", r"[\1]", str(t))          # valeurs calculées : [expression]
    t = re.sub(r"<sub>(.*?)</sub>", r"_\1", t)
    t = re.sub(r"<sup>(.*?)</sup>", r"^\1", t)
    t = re.sub(r"<[^>]+>", "", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    return re.sub(r"\s+", " ", t).strip()


def script_enregistrement(cfg, dossier, presents):
    """Écrit ``script_enregistrement.md`` dans ``dossier`` et renvoie son chemin.

    Le script liste chaque emplacement audio (présent ou à enregistrer, selon ``presents``), le texte
    de chaque apparition et les commentaires facultatifs possibles.
    """
    L = [f"# Script d'enregistrement — {cfg['titre']}", "",
         f"Déposez dans ce dossier ({dossier.name}) un fichier par emplacement : `<emplacement>.mp3` "
         "(ou .m4a, .wav, .ogg), puis relancez `python build.py`.",
         "Facultatif : `<emplacement>.txt` = transcription affichée sous l'étape ; "
         "`<emplacement>.reperes.json` = temps d'apparition, relevés avec le mode auteur (ouvrir index.html?auteur).",
         "Découpe dans Audacity : au lieu d'un fichier unique, exportez `<emplacement>_a1.mp3`, `<emplacement>_a2.mp3`… "
         "(un segment par apparition ci-dessous) : ils sont lus à la suite et chaque segment fait apparaître l'élément suivant.",
         "Les noms sont reconnus sans tenir compte des majuscules.",
         "Les textes ci-dessous sont ceux de la fiche : une base pour écrire votre commentaire, pas un texte imposé.", ""]
    for slot, e in slots(cfg):
        etat = "présent" if slot in presents else "à enregistrer"
        L += [f"## `{slot}` — {_brut(e.get('titre', ''))} ({etat})", ""]
        n = 0
        for b in e.get("contenu", []):
            n += 1
            b = {"texte": b} if isinstance(b, str) else b
            morceaux = [b.get("texte", "")] + (b.get("liste") or []) + ([b["legende"]] if b.get("legende") else [])
            if b.get("formule"):
                morceaux.insert(1, "[formule : $" + b["formule"].strip() + "$]")
            L.append(f"{n}. *(apparition {n})* " + " ".join(_brut(m) for m in morceaux if m))
        if e.get("enonce"):
            n += 1
            L.append(f"{n}. *(apparition {n})* {_brut(e['enonce'])}")
        if e.get("options"):
            une = bool(e.get("options_une_par_une"))
            L.append("   Propositions" + (" (lues une par une : une apparition chacune, dans cet ordre) :" if une
                                          else " (affichées dès le début) :"))
            for k, o in enumerate(e["options"]):
                o = {"texte": o} if isinstance(o, str) else o
                if une:
                    n += 1
                L.append((f"{n}. *(apparition {n})* " if une else "   ") + f"{chr(97 + k)}) " + _brut(o.get("texte") or "")
                         + (f" ${o['tex'].strip()}$" if o.get("tex") else "") + ("  ← juste" if o.get("correct") else ""))
        if n > 1:
            L.append(f"   → {n} apparitions : `{slot}_a1` … `{slot}_a{n}`, ou un seul fichier + `{slot}.reperes.json`.")
        if e.get("type") == "numerique":
            ident = e["id"] + slot[len(e.get("audio", "")):]
            if e.get("attendu"):
                L.append(f"   Réponse attendue : [{e['attendu']}]" + (f" ; solution : {_brut(e['solution'])}" if e.get("solution") else ""))
            fac = ([f"`{ident}_aide` (rappel de méthode)"] if (e.get("aide") or {}).get("texte") else []) \
                + ([f"`{ident}_explication` (solution)"] if e.get("solution") else [])
            if fac:
                L.append("   Facultatif : " + ", ".join(fac) + ".")
        if e.get("type") == "choix":
            fac = []
            if e.get("explication"):
                fac.append(f"`{e['id']}_explication` (explication)")
            fac += [f"`{e['id']}_retour_{chr(97 + k)}` (retour de {chr(97 + k)})"
                    for k, o in enumerate(e.get("options", [])) if isinstance(o, dict) and o.get("retour")]
            if fac:
                L.append("   Facultatif : " + ", ".join(fac) + ".")
        L.append("")
    f = dossier / "script_enregistrement.md"
    f.write_text("\n".join(L) + "\n", encoding="utf-8")
    return f


def medias_presents(cfg, dossier, avert=None):
    """Recense les médias déposés dans ``dossier`` et renvoie ``(audios, transcriptions, reperes)``.

    Audios : fichier unique ou segments ``_a1``, ``_a2``… ; transcriptions ``.txt`` ; repères
    ``.reperes.json``. Les noms sont reconnus sans tenir compte des majuscules. Les incohérences
    (audio manquant, nombre de segments ou de repères) sont ajoutées à ``avert``.
    """
    avert = avert if avert is not None else []
    index = {f.name.lower(): f for f in dossier.iterdir() if f.is_file()}
    def chercher(nom):
        for ext in EXT_AUDIO:
            if nom.lower() + ext in index:
                return index[nom.lower() + ext]
        return None
    audios, trans, reperes = {}, {}, {}
    principaux = [s for s, _ in slots(cfg)]
    for slot in principaux + slots_facultatifs(cfg):
        segs, k = [], 1
        while chercher(f"{slot}_a{k}"):
            segs.append(chercher(f"{slot}_a{k}")); k += 1
        seul = chercher(slot)
        if segs:
            audios[slot] = segs
            if seul:
                avert.append(f"{slot} : segments {slot}_a1… et fichier {seul.name} présents — les segments sont utilisés")
        elif seul:
            audios[slot] = seul
        t = index.get(f"{slot}.txt".lower())
        if t:
            trans[slot] = t.read_text(encoding="utf-8").strip()
        r = index.get(f"{slot}.reperes.json".lower())
        if r and isinstance(audios.get(slot), list):
            avert.append(f"{r.name} ignoré : {slot} est découpé en segments")
        elif r:
            try:
                reperes[slot] = json.loads(r.read_text(encoding="utf-8"))
            except ValueError:
                avert.append(f"{r.name} illisible, ignoré")
    if audios:
        manque = [s for s in principaux if s not in audios]
        if manque:
            avert.append("audio absent pour : " + ", ".join(manque))
    for slot, e in slots(cfg):
        n, a = nb_apparitions(e), audios.get(slot)
        if isinstance(a, list) and len(a) != n:
            avert.append(f"{slot} : {len(a)} segment(s) pour {n} apparition(s)")
        if slot in reperes and len(reperes[slot]) != n:
            avert.append(f"{slot}.reperes.json : {len(reperes[slot])} temps pour {n} apparition(s)")
    return audios, trans, reperes


def images(cfg):
    """Renvoie les chemins des images citées par la fiche (rappel, contenus des étapes et de la conclusion)."""
    out = []
    if (cfg.get("rappel") or {}).get("image"):
        out.append(cfg["rappel"]["image"])
    for e in cfg.get("etapes", []) + [cfg.get("conclusion") or {}]:
        for b in e.get("contenu", []) or []:
            if isinstance(b, dict) and b.get("image"):
                out.append(b["image"])
    return out


def manifeste(cfg, fichiers):
    """Renvoie le texte du manifeste SCORM 1.2 (``imsmanifest.xml``) d'un exercice et de ses fichiers."""
    ident, titre = cfg["id"], escape(cfg["titre"])
    f = "".join(f'\n      <file href="{escape(m)}"/>' for m in fichiers)
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="ExoForge_{ident}" version="1.0"
  xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"
  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd
                      http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">
  <metadata><schema>ADL SCORM</schema><schemaversion>1.2</schemaversion></metadata>
  <organizations default="ORG_{ident}">
    <organization identifier="ORG_{ident}">
      <title>{titre}</title>
      <item identifier="ITEM_{ident}" identifierref="RES_{ident}"><title>{titre}</title></item>
    </organization>
  </organizations>
  <resources>
    <resource identifier="RES_{ident}" type="webcontent" adlcp:scormtype="sco" href="index.html">
      <file href="index.html"/>{f}
    </resource>
  </resources>
</manifest>
"""


def verifier(cfg):
    """Vérifie la structure de la fiche (identifiants, types d'étapes, options, renvois ``aller_a``).

    Quitte le programme avec la liste des problèmes s'il y en a.
    """
    pbs = []
    if not re.fullmatch(r"\w+", str(cfg.get("id", ""))):
        pbs.append("id manquant ou invalide (lettres, chiffres, _)")
    vus = set()
    for k, e in enumerate(cfg.get("etapes", []), 1):
        if not e.get("id"):
            pbs.append(f"étape {k} sans id")
        elif e["id"] in vus:
            pbs.append(f"id d'étape en double : {e['id']}")
        vus.add(e.get("id"))
        if e.get("type") not in ("info", "choix", "numerique"):
            pbs.append(f"étape {e.get('id')} : type « {e.get('type')} » (possibles : info, choix, numerique)")
        if e.get("repeter") is not None and not isinstance(e.get("repeter"), int):
            pbs.append(f"étape {e.get('id')} : « repeter » doit être un nombre entier")
        if e.get("type") == "choix":
            ops = e.get("options") or []
            if len(ops) < 2:
                pbs.append(f"étape {e.get('id')} : au moins 2 options")
            n = sum(bool(isinstance(o, dict) and o.get("correct")) for o in ops)
            if e.get("note") is False or e.get("correct") is not None:
                pass                                          # non notée, ou bonne option calculée
            elif n == 0:
                pbs.append(f"étape {e.get('id')} : aucune option correcte (ou « correct: <expression> », ou « note: false »)")
            elif n > 1 and not e.get("plusieurs"):
                pbs.append(f"étape {e.get('id')} : {n} options correctes, ajoutez « plusieurs: true »")
        if e.get("type") == "numerique" and not e.get("attendu"):
            pbs.append(f"étape {e.get('id')} : « attendu » manquant (expression de la réponse)")
    ids = {e.get("id") for e in cfg.get("etapes", [])}
    for e in cfg.get("etapes", []):
        for o in e.get("options") or []:
            if isinstance(o, dict) and o.get("aller_a") and o["aller_a"] not in ids:
                pbs.append(f"étape {e.get('id')} : aller_a « {o['aller_a']} » ne correspond à aucune étape")
    if pbs:
        sys.exit("Fiche à corriger :\n - " + "\n - ".join(pbs))


def construire_generique(fiche: Path, cfg: dict, profil=None, auteur=False, style_profil=None) -> Path:
    """Construit l'exercice et renvoie le chemin du paquet SCORM.

    Écrit ``dist/exoforge/<id>/index.html``, ``imsmanifest.xml`` et les médias copiés, puis
    ``dist/exoforge/<id>_scorm12.zip`` ; met à jour le script d'enregistrement dans le dossier des
    médias. ``style_profil`` : fonction qui renvoie le bloc de style du profil (voir ``build.py``).
    Affiche un bilan et les points à vérifier.
    """
    verifier(cfg)
    dossier = fiche.parent
    avert = []
    fp = trouver_profil(profil or cfg.get("profil"))
    schema = None
    if fp:
        schema = ((yaml.safe_load(fp.read_text(encoding="utf-8")) or {}).get("charte") or {}).get("latex_couleurs")
        if schema and (fp.parent / schema).exists():
            schema = str((fp.parent / schema).resolve())     # jeu de couleurs rangé avec le profil
    macros, couleurs = preparer_latex(cfg, dossier, avert, schema)
    dmedia = chemins.media_exoforge(dossier, cfg["id"])
    dmedia.mkdir(parents=True, exist_ok=True)
    audios, trans, reperes = medias_presents(cfg, dmedia, avert)
    script = script_enregistrement(cfg, dmedia, audios)

    sortie = chemins.SORTIES / "exoforge" / cfg["id"]
    sortie.mkdir(parents=True, exist_ok=True)       # rien n'est supprimé : les fichiers sont remplacés
    fichiers = []
    def copier(src: Path, rel: str):
        dst = sortie / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(src, dst)
        fichiers.append(rel)
    for img in images(cfg):
        src_img = chemins.fichier_exoforge(dossier, img)
        if src_img.exists():
            copier(src_img, img)
        else:
            avert.append(f"image introuvable : {img}")
    donnees = {k: v for k, v in cfg.items() if k != "latex"}
    donnees["audios"] = {}
    for slot, f in audios.items():
        liste = []
        for g in (f if isinstance(f, list) else [f]):
            rel = f"media/{cfg['id']}/{g.name.lower()}"      # minuscules : Moodle distingue les majuscules
            copier(g, rel)
            liste.append(rel)
        donnees["audios"][slot] = liste if isinstance(f, list) else liste[0]
    # effets sonores facultatifs du profil (charte.sons : {juste: fichier, faux: fichier}, relatifs au dossier du profil)
    donnees["sons"] = {}
    if fp and cfg.get("sons", True) is not False:
        sons = ((yaml.safe_load(fp.read_text(encoding="utf-8")) or {}).get("charte") or {}).get("sons") or {}
        for nom, chemin in sons.items():
            src = (fp.parent / chemin)
            if src.exists():
                rel = f"sons/{nom}{src.suffix.lower()}"
                copier(src, rel)
                donnees["sons"][nom] = rel
            else:
                avert.append(f"son introuvable : {chemin} (profil {chemins.nom_profil(fp)})")
    donnees.update(transcriptions=trans, reperes=reperes, latex_macros=macros, latex_couleurs=couleurs,
                   avertissements=avert, auteur_mode=bool(auteur))
    copier(MATHJAX, "mathjax.js")
    if MATHJAX.with_name("MATHJAX_LICENSE").is_file():          # licence Apache 2.0, jointe au fichier redistribué
        copier(MATHJAX.with_name("MATHJAX_LICENSE"), "MATHJAX_LICENSE")

    gabarit = MOTEUR.read_text(encoding="utf-8")
    js = json.dumps(donnees, ensure_ascii=False, indent=1).replace("</", "<\\/")
    page = gabarit.replace("__STYLE__", FEUILLE.read_text(encoding="utf-8").rstrip(), 1)
    page = page.replace("__CONFIG__", js).replace("__TITRE__", escape(cfg["titre"]))
    if fp and style_profil:
        page = page.replace("</head>", style_profil(fp) + "</head>", 1)
    (sortie / "index.html").write_text(page, encoding="utf-8")
    (sortie / "imsmanifest.xml").write_text(manifeste(cfg, fichiers), encoding="utf-8")
    paquet = chemins.SORTIES / "exoforge" / f"{cfg['id']}_scorm12.zip"
    with zipfile.ZipFile(paquet, "w", zipfile.ZIP_DEFLATED) as z:
        for rel in ["imsmanifest.xml", "index.html"] + fichiers:
            z.write(sortie / rel, rel)
    n = len(slots(cfg))
    n_fac = sum(1 for s in slots_facultatifs(cfg) if s in audios)
    print(f"OK : {sortie / 'index.html'}  (mode auteur : ouvrir index.html?auteur)")
    print(f"OK : {paquet}")
    print(f"Profil : {chemins.nom_profil(fp) if fp else 'aucun'}{' (couleurs LaTeX : ' + Path(schema).name + ')' if schema else ''} ; audios : {len(audios) - n_fac}/{n}{f' (+ {n_fac} retour(s))' if n_fac else ''} ; transcriptions : {len(trans)} ; "
          f"repères : {len(reperes)} — script : {script}")
    for a in avert:
        print("À VÉRIFIER :", a)
    return paquet
