"""Repair verified TeX4ht navigation defects in a frozen full-reader EPUB."""

from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import posixpath
import re
import sys
from urllib.parse import unquote, urlsplit
from zipfile import ZipFile

from lxml import etree
from repair_epub_math_markup import fix_math_markup


XHTML = "{http://www.w3.org/1999/xhtml}"
EPUB = "{http://www.idpf.org/2007/ops}"
XLINK = "{http://www.w3.org/1999/xlink}"
MATH = "{http://www.w3.org/1998/Math/MathML}"
OPF = "{http://www.idpf.org/2007/opf}"
HYPERREF_FOOTNOTE = re.compile(r"#Hfootnote\.\d+")
TEX4HT_ID = re.compile(r"(?:TBL-|oframed-|framed-|x)\d[\w.-]*")
NOTEREF_ID = re.compile(r"fn\d+x\d+")
CAPTIONED_FIGURE_ALTS = (
    ("La réunion", "Diagramme de Venn. Les deux disques sont colorés, y compris leur intersection."),
    ("L’intersection", "Diagramme de Venn. Seule la région commune aux deux disques est colorée."),
    ("La différence", "Diagramme de Venn. Seule la région du disque A extérieure au disque B est colorée."),
    ("Une fonction associe", "Des flèches partent des éléments du domaine et aboutissent à leurs valeurs."),
    ("Une fonction surjective", "Chaque point de l’ensemble d’arrivée reçoit au moins une flèche."),
    ("Une fonction injective", "Les flèches issues de points distincts aboutissent à des points distincts."),
    ("Une fonction bijective", "Chaque point de l’ensemble d’arrivée reçoit une seule flèche."),
    ("La composée", "Les flèches de A vers B puis de B vers C représentent f puis g. Une flèche directe de A vers C représente leur composée."),
    ("Une machine de Turing qui exécute", "Trois états successifs du même ruban. De q₁ à q₂, la tête écrit 0 dans la case qu’elle lit. Elle se déplace d’une case vers la droite dans l’état q₃."),
)
HILBERT_FIGURE_ALTS = (
    "Six approximations successives de la courbe de Hilbert. À chaque étape, le tracé rouge parcourt une grille carrée plus fine.",
    "Première étape h₁ sur une grille 2 sur 2. Le tracé noir passe par les quatre quarts du carré. Deux segments rouges le relient au bord inférieur.",
    "Deuxième étape h₂ sur une grille 4 sur 4. Quatre copies réduites du tracé précédent sont reliées en vert. Deux segments rouges atteignent les bords gauche et droit.",
    "Troisième étape h₃ sur une grille 8 sur 8. Quatre copies réduites de h₂ sont reliées en vert. Deux segments rouges atteignent le bord inférieur.",
)
MODAL_RULE_TABLE_ALTS = (
    (
        "Règles des tableaux préfixés pour les connecteurs propositionnels",
        (
            "Négation vraie au préfixe σ. Sur la même branche, inscrire A signé faux au préfixe σ.",
            "Négation fausse au préfixe σ. Sur la même branche, inscrire A signé vrai au préfixe σ.",
            "Conjonction A et B vraie au préfixe σ. Sur la même branche, inscrire A et B signés vrais au préfixe σ.",
            "Conjonction A et B fausse au préfixe σ. Ouvrir deux branches, l’une avec A signé faux, l’autre avec B signé faux, au même préfixe.",
            "Disjonction A ou B vraie au préfixe σ. Ouvrir deux branches, l’une avec A signé vrai, l’autre avec B signé vrai, au même préfixe.",
            "Disjonction A ou B fausse au préfixe σ. Sur la même branche, inscrire A et B signés faux au préfixe σ.",
            "Implication de A vers B vraie au préfixe σ. Ouvrir deux branches, l’une avec A signé faux, l’autre avec B signé vrai, au même préfixe.",
            "Implication de A vers B fausse au préfixe σ. Sur la même branche, inscrire A signé vrai et B signé faux au préfixe σ.",
        ),
    ),
    (
        "Les règles modales pour K.",
        (
            "Nécessité de A vraie au préfixe σ. Inscrire A signé vrai au préfixe successeur σ.n, déjà utilisé sur la branche.",
            "Nécessité de A fausse au préfixe σ. Inscrire A signé faux à un nouveau préfixe successeur σ.n.",
            "Possibilité de A vraie au préfixe σ. Inscrire A signé vrai à un nouveau préfixe successeur σ.n.",
            "Possibilité de A fausse au préfixe σ. Inscrire A signé faux au préfixe successeur σ.n, déjà utilisé sur la branche.",
        ),
    ),
    (
        "Autres règles modales.",
        (
            "Règle T pour la nécessité. De la nécessité de A signée vraie au préfixe σ, inscrire A signé vrai au même préfixe.",
            "Règle T pour la possibilité. De la possibilité de A signée fausse au préfixe σ, inscrire A signé faux au même préfixe.",
            "Règle D pour la nécessité. De la nécessité de A signée vraie au préfixe σ, inscrire la possibilité de A signée vraie au même préfixe.",
            "Règle D pour la possibilité. De la possibilité de A signée fausse au préfixe σ, inscrire la nécessité de A signée fausse au même préfixe.",
            "Règle B pour la nécessité. De la nécessité de A signée vraie au préfixe successeur σ.n, inscrire A signé vrai au préfixe parent σ.",
            "Règle B pour la possibilité. De la possibilité de A signée fausse au préfixe successeur σ.n, inscrire A signé faux au préfixe parent σ.",
            "Règle 4 pour la nécessité. Transmettre la nécessité de A signée vraie du préfixe σ au préfixe successeur σ.n déjà utilisé.",
            "Règle 4 pour la possibilité. Transmettre la possibilité de A signée fausse du préfixe σ au préfixe successeur σ.n déjà utilisé.",
            "Règle 4r pour la nécessité. Transmettre la nécessité de A signée vraie du préfixe successeur σ.n au préfixe parent σ.",
            "Règle 4r pour la possibilité. Transmettre la possibilité de A signée fausse du préfixe successeur σ.n au préfixe parent σ.",
        ),
    ),
    (
        "Règles simplifiées pour S5.",
        (
            "Nécessité de A vraie au préfixe entier n. Inscrire A signé vrai à un préfixe entier m déjà utilisé.",
            "Nécessité de A fausse au préfixe entier n. Inscrire A signé faux à un nouveau préfixe entier m.",
            "Possibilité de A vraie au préfixe entier n. Inscrire A signé vrai à un nouveau préfixe entier m.",
            "Possibilité de A fausse au préfixe entier n. Inscrire A signé faux à un préfixe entier m déjà utilisé.",
        ),
    ),
    (
        "Règles modales supplémentaires.",
        (
            "Règle T pour la nécessité. Dans l’antécédent, remplacer A par □A. Les contextes Γ et Δ restent en place.",
            "Règle T pour la possibilité. Dans le conséquent, remplacer A par ◇A. Les contextes Γ et Δ restent en place.",
            "Règle D. Préfixer de □ chacune des formules de l’antécédent Γ et de ◇ chacune des formules du conséquent Δ.",
            "Règle B pour la nécessité. De Γ, ◇Π entraîne □Δ, Λ, A, on déduit □Γ, Π entraîne Δ, ◇Λ, □A.",
            "Règle B pour la possibilité. De A, ◇Γ, Π entraîne □Λ, Δ, on déduit ◇A, Γ, □Π entraîne Λ, ◇Δ.",
            "Règle 4 pour la nécessité. De □Γ entraîne ◇Δ, A, on déduit □Γ entraîne ◇Δ, □A.",
            "Règle 4 pour la possibilité. De A, □Γ entraîne ◇Δ, on déduit ◇A, □Γ entraîne ◇Δ.",
            "Règle 5 pour la nécessité. De □Γ, ◇Π entraîne □Δ, ◇Λ, A, on déduit □Γ, ◇Π entraîne □Δ, ◇Λ, □A.",
            "Règle 5 pour la possibilité. De A, ◇Γ, □Π entraîne ◇Δ, □Λ, on déduit ◇A, ◇Γ, □Π entraîne ◇Δ, □Λ.",
        ),
    ),
)
MODAL_K_SEQUENT_ALTS = (
    "Règle de nécessité pour K. De Γ entraîne Δ, A, on déduit □Γ entraîne ◇Δ, □A.",
    "Règle de possibilité pour K. De A, Γ entraîne Δ, on déduit ◇A, □Γ entraîne ◇Δ.",
)
INVALID_MODAL_K_SEQUENT_ALTS = (
    (
        "Dérivation avec une règle de nécessité invalide. À partir de A entraîne A, la négation à droite donne A et non A dans le conséquent vide d’antécédent. La règle invalide place □ devant les deux formules, puis la disjonction à droite donne □A ou □¬A.",
        "Dérivation avec une règle de possibilité invalide. À partir de A entraîne A, la négation à gauche donne non A et A dans l’antécédent vide de conséquent. La règle invalide place ◇ devant les deux formules. La négation à droite puis l’implication à droite donnent ◇A implique ¬◇¬A.",
    ),
    (
        "Dérivation avec une règle de nécessité invalide. À partir de A entraîne A, la négation à droite puis l’échange donnent non A, A dans le conséquent. La règle invalide place □ devant A seul. La disjonction à droite donne ¬A ou □A.",
        "Dérivation avec une règle de possibilité invalide. À partir de A entraîne A, la négation à gauche donne non A et A dans l’antécédent. La règle invalide place ◇ devant non A seul. La négation à droite puis l’implication à droite donnent A implique ¬◇¬A.",
    ),
)
NATURAL_DEDUCTION_RULE_ALTS = {
    "∧": (
        "Introduction de la conjonction. De A et de B, on déduit A et B.",
        "Élimination de la conjonction. De A et B, on déduit A.",
        "Élimination de la conjonction. De A et B, on déduit B.",
    ),
    "∨": (
        "Introduction de la disjonction. De A, on déduit A ou B.",
        "Introduction de la disjonction. De B, on déduit A ou B.",
        "Élimination de la disjonction. On dispose de A ou B, d’une dérivation de C sous l’hypothèse A et d’une dérivation de C sous l’hypothèse B. On conclut C et on décharge les deux hypothèses repérées par n.",
    ),
    "→": (
        "Introduction de l’implication. D’une dérivation de B sous l’hypothèse A, on conclut A implique B et on décharge l’hypothèse repérée par n.",
        "Élimination de l’implication. De A implique B et de A, on déduit B.",
    ),
    "¬": (
        "Introduction de la négation. D’une dérivation du faux sous l’hypothèse A, on conclut non A et on décharge l’hypothèse repérée par n.",
        "Élimination de la négation. De non A et de A, on déduit le faux.",
    ),
    "⊥": (
        "Règle intuitionniste du faux. Du faux, on déduit A.",
        "Règle classique du faux. D’une dérivation du faux sous l’hypothèse non A, on conclut A et on décharge l’hypothèse repérée par n.",
    ),
}
NATURAL_DEDUCTION_QUANTIFIER_ALTS = {
    "∀": (
        "Introduction de l’universel. De A(a), on déduit pour tout x, A(x). La constante a doit être absente de la conclusion et des hypothèses encore ouvertes de la dérivation de A(a).",
        "Élimination de l’universel. De pour tout x, A(x), on déduit A(t), où t est un terme clos.",
    ),
    "∃": (
        "Introduction de l’existentiel. De A(t), où t est un terme clos, on déduit il existe un x tel que A(x).",
        "Élimination de l’existentiel. De l’énoncé « il existe un x tel que A(x) » et d’une dérivation de C sous l’hypothèse A(a), on déduit C. On décharge les hypothèses repérées par n. La constante a est absente de la prémisse existentielle, de C et des autres hypothèses ouvertes.",
    ),
}
SEQUENT_PROPOSITIONAL_RULE_ALTS = {
    "¬": (
        "Négation à gauche. De Γ entraîne Δ, A, on déduit non A, Γ entraîne Δ.",
        "Négation à droite. De A, Γ entraîne Δ, on déduit Γ entraîne Δ, non A.",
    ),
    "∧": (
        "Conjonction à gauche. De A, Γ entraîne Δ, on déduit A et B, Γ entraîne Δ.",
        "Conjonction à gauche. De B, Γ entraîne Δ, on déduit A et B, Γ entraîne Δ.",
        "Conjonction à droite. De Γ entraîne Δ, A et de Γ entraîne Δ, B, on déduit Γ entraîne Δ, A et B.",
    ),
    "∨": (
        "Disjonction à gauche. De A, Γ entraîne Δ et de B, Γ entraîne Δ, on déduit A ou B, Γ entraîne Δ.",
        "Disjonction à droite. De Γ entraîne Δ, A, on déduit Γ entraîne Δ, A ou B.",
        "Disjonction à droite. De Γ entraîne Δ, B, on déduit Γ entraîne Δ, A ou B.",
    ),
    "→": (
        "Implication à gauche. De Γ entraîne Δ, A et de B, Π entraîne Λ, on déduit A implique B, Γ, Π entraîne Δ, Λ.",
        "Implication à droite. De A, Γ entraîne Δ, B, on déduit Γ entraîne Δ, A implique B.",
    ),
}
SEQUENT_QUANTIFIER_ALTS = {
    "∀": (
        "Universel à gauche. De A(t), Γ entraîne Δ, on déduit pour tout x, A(x), Γ entraîne Δ. Le terme t est clos.",
        "Universel à droite. De Γ entraîne Δ, A(a), on déduit Γ entraîne Δ, pour tout x, A(x). La constante a est absente du séquent inférieur.",
    ),
    "∃": (
        "Existentiel à gauche. De A(a), Γ entraîne Δ, on déduit il existe un x tel que A(x), Γ entraîne Δ. La constante a est absente du séquent inférieur.",
        "Existentiel à droite. De Γ entraîne Δ, A(t), on déduit Γ entraîne Δ, il existe un x tel que A(x). Le terme t est clos.",
    ),
}
SEQUENT_STRUCTURAL_RULE_ALTS = {
    "Affaiblissement": (
        "Affaiblissement à gauche. À partir d’un séquent Γ entraîne Δ, on ajoute A au début du membre gauche.",
        "Affaiblissement à droite. À partir d’un séquent Γ entraîne Δ, on ajoute A à la fin du membre droit.",
    ),
    "Contraction": (
        "Contraction à gauche. On remplace deux occurrences de A en tête du membre gauche par une seule.",
        "Contraction à droite. On remplace deux occurrences de A en fin du membre droit par une seule.",
    ),
    "Échange": (
        "Échange à gauche. On permute deux énoncés adjacents A et B dans le membre gauche.",
        "Échange à droite. On permute deux énoncés adjacents A et B dans le membre droit.",
    ),
}
SEQUENT_CUT_ALT = "Coupure. De Γ entraîne Δ, A et de A, Π entraîne Λ, on déduit Γ, Π entraîne Δ, Λ. Les deux occurrences désignées de A sont supprimées."
TABLEAU_PROPOSITIONAL_RULE_ALTS = {
    "¬": (
        "Négation vraie. Sur la même branche, on ajoute A signé faux.",
        "Négation fausse. Sur la même branche, on ajoute A signé vrai.",
    ),
    "∧": (
        "Conjonction vraie. Sur la même branche, on ajoute A signé vrai et B signé vrai.",
        "Conjonction fausse. On scinde la branche : A est signé faux sur la première et B est signé faux sur la seconde.",
    ),
    "∨": (
        "Disjonction vraie. On scinde la branche : A est signé vrai sur la première et B est signé vrai sur la seconde.",
        "Disjonction fausse. Sur la même branche, on ajoute A signé faux et B signé faux.",
    ),
    "→": (
        "Implication vraie. On scinde la branche : A est signé faux sur la première et B est signé vrai sur la seconde.",
        "Implication fausse. Sur la même branche, on ajoute A signé vrai et B signé faux.",
    ),
    "La règle de coupure": (
        "Coupure dans un tableau. On scinde la branche en ajoutant A signé vrai sur la première et A signé faux sur la seconde, pour un énoncé A quelconque.",
    ),
}
TABLEAU_QUANTIFIER_ALTS = {
    "∀": (
        "Universel vrai. On ajoute A(t) signé vrai sur la même branche, pour un terme clos t.",
        "Universel faux. On ajoute A(a) signé faux sur la même branche. La constante a doit être absente de la branche au-dessus de l’inférence.",
    ),
    "∃": (
        "Existentiel vrai. On ajoute A(a) signé vrai sur la même branche. La constante a doit être absente de la branche au-dessus de l’inférence.",
        "Existentiel faux. On ajoute A(t) signé faux sur la même branche, pour un terme clos t.",
    ),
}
PROOF_RULE_SHEETS = {
    "Déduction naturelle": {
        "Règles propositionnelles": NATURAL_DEDUCTION_RULE_ALTS,
        "Règles pour les quantificateurs": NATURAL_DEDUCTION_QUANTIFIER_ALTS,
    },
    "Le calcul des séquents": {
        "Règles propositionnelles": SEQUENT_PROPOSITIONAL_RULE_ALTS,
        "Règles pour les quantificateurs": SEQUENT_QUANTIFIER_ALTS,
        "Règles structurelles": SEQUENT_STRUCTURAL_RULE_ALTS,
    },
    "Tableaux": {
        "Règles propositionnelles": TABLEAU_PROPOSITIONAL_RULE_ALTS,
        "Règles pour les quantificateurs": TABLEAU_QUANTIFIER_ALTS,
    },
}
EQUALITY_RULE_ALTS = {
    "derivations-avec-legalite": (
        "Égalité dans le calcul des séquents. Si le séquent a t₁ = t₂ à gauche et A(t₁) à droite, on peut remplacer A(t₁) par A(t₂). Le reste du séquent est conservé.",
        "Égalité dans le calcul des séquents. Si le séquent a t₁ = t₂ à gauche et A(t₂) à droite, on peut remplacer A(t₂) par A(t₁). Le reste du séquent est conservé.",
    ),
    "derivations-avec-egalite": (
        "Introduction de l’égalité en déduction naturelle. On conclut t = t sans prémisse, pour un terme clos t.",
        "Élimination de l’égalité en déduction naturelle. De t₁ = t₂ et de A(t₁), on déduit A(t₂).",
        "Élimination de l’égalité en déduction naturelle. De t₁ = t₂ et de A(t₂), on déduit A(t₁).",
    ),
    "tableaux-avec-egalite": (
        "Réflexivité de l’égalité dans un tableau. On peut ajouter t = t signé vrai sans prémisse, pour un terme clos t.",
        "Égalité dans un tableau. Si une branche contient t₁ = t₂ signé vrai et A(t₁) signé vrai, on ajoute A(t₂) signé vrai sur cette branche.",
        "Égalité dans un tableau. Si une branche contient t₁ = t₂ signé vrai et A(t₁) signé faux, on ajoute A(t₂) signé faux sur cette branche.",
    ),
}


def local_fragment(document, value):
    url = urlsplit(value)
    if url.scheme or url.netloc or url.query or not url.fragment:
        return None
    path = posixpath.normpath(posixpath.join(posixpath.dirname(document), unquote(url.path)))
    return (path if url.path else document, unquote(url.fragment))


def repair_ordinal_footnote(root, name, ids):
    count = 0
    for outer in tuple(root.iter(MATH + "mstyle")):
        href = outer.get(XLINK + "href", "")
        if not HYPERREF_FOOTNOTE.fullmatch(href) or (name, href[1:]) in ids:
            continue
        inner = outer[0] if len(outer) else None
        if (
            inner is None or inner.tag != MATH + "mstyle"
            or inner.get(EPUB + "type") != "noteref"
            or inner.get("role") != "doc-noteref"
            or len(inner) != 1
            or inner[0].tag != MATH + "sup"
            or inner[0].get("class") != "textsuperscript"
            or len(inner[0]) != 1 or inner[0][0].tag != MATH + "mi"
            or len(inner[0][0]) or not (inner[0][0].text or "").strip().isdigit()
            or local_fragment(name, inner.get(XLINK + "href", "")) not in ids
            or any(isinstance(child.tag, str) for child in list(outer)[1:])
        ):
            continue
        text = etree.Element(MATH + "mtext")
        link = etree.SubElement(text, XHTML + "a", {
            "href": inner.get(XLINK + "href"), "role": "doc-noteref", EPUB + "type": "noteref",
        })
        marker = etree.SubElement(link, XHTML + "sup", {"class": "textsuperscript"})
        marker.text = inner[0][0].text
        text.tail = outer.tail
        outer.getparent().replace(outer, text)
        count += 1
    return count


def repair_html_structure(root):
    result = Counter()
    for heading in root.iter(XHTML + "h2"):
        if "chapterHead" not in heading.get("class", "").split():
            continue
        mark = heading.find(XHTML + "span")
        if mark is not None and mark.get("class") == "titlemark" and re.fullmatch(r"éhapitre\s+\d+", mark.text or ""):
            mark.text = "C" + mark.text[1:]
            result["french_chapter_marks"] += 1
    for table in root.iter(XHTML + "table"):
        if table.get("rules") == "groups":
            del table.attrib["rules"]
            table.set("class", " ".join(filter(None, (table.get("class"), "column-group-rules"))))
            result["legacy_table_rules_moved_to_css"] += 1
    for caption in tuple(root.iter(XHTML + "figcaption")):
        wrapper = caption.getparent()
        figure = wrapper.getparent()
        if (
            wrapper.tag != XHTML + "div" or wrapper.get("class") != "center"
            or figure is None or figure.tag != XHTML + "figure"
            or any(isinstance(e.tag, str) for e in caption.itersiblings())
            or any(isinstance(e.tag, str) for e in wrapper.itersiblings())
        ):
            continue
        figure.append(caption)
        figure.set("class", " ".join(filter(None, (figure.get("class"), "centered-caption"))))
        result["figure_captions_attached_to_figure"] += 1
    return result


def add_checked_figure_descriptions(root):
    result = Counter()
    for figure in root.iter(XHTML + "figure"):
        caption = next(figure.iter(XHTML + "figcaption"), None)
        images = list(figure.iter(XHTML + "img"))
        if caption is None or len(images) != 1 or images[0].get("alt", "").strip():
            continue
        title = " ".join("".join(caption.itertext()).split()).partition(" : ")[2]
        for prefix, description in CAPTIONED_FIGURE_ALTS:
            if title.startswith(prefix):
                images[0].set("alt", description)
                result["captioned_figures_described"] += 1
                break
    hilbert = False
    figures = []
    for node in root.iter(etree.Element):
        if node.tag == XHTML + "h3":
            title = " ".join("".join(node.itertext()).split())
            hilbert = "les courbes de Hilbert remplissant l’espace" in title
        elif node.tag == XHTML + "img" and not node.get("alt", "").strip() and node.get("src", "").endswith(".svg"):
            if hilbert:
                figures.append(node)
    if len(figures) == 3:
        for img, description in zip(figures, HILBERT_FIGURE_ALTS[1:]):
            img.set("alt", description)
            result["hilbert_figures_described"] += 1
    # The overview belongs to the pathologies section immediately before the
    # construction. Identify it by its captionless center and its exact title.
    title = root.findtext(f"{XHTML}head/{XHTML}title", "")
    if len(figures) == 3 and "Histoire et mythologie de la th" in title:
        overview = [img for img in root.iter(XHTML + "img") if not img.get("alt", "").strip()]
        if len(overview) == 1 and overview[0].get("src", "").endswith(".svg"):
            overview[0].set("alt", HILBERT_FIGURE_ALTS[0])
            result["hilbert_figures_described"] += 1
    return result


def heading_text(heading):
    return " ".join("".join(heading.itertext()).split())


def remove_empty_exercise_sections(roots):
    """Remove generated exercise headings whose only body is a pair of anchors."""
    ncx = "{http://www.daisy.org/z3986/2005/ncx/}"
    candidates = []
    targets = {}
    for name, root in roots.items():
        if not name.endswith(".xhtml"):
            continue
        for heading in root.iter(XHTML + "h3"):
            if heading.get("class") != "likesectionHead" or heading_text(heading) != "Exercices":
                continue
            siblings = [node for node in heading.itersiblings() if isinstance(node.tag, str)]
            if len(siblings) != 2:
                continue
            body, crosslinks = siblings
            if body.tag != XHTML + "p" or crosslinks.get("class") != "crosslinks" or heading_text(body):
                continue
            if set(body.attrib) != {"id"} or not re.fullmatch(r"exercices\d+", body.get("id", "")):
                continue
            anchors = [node for node in body if isinstance(node.tag, str)]
            if not anchors or any(
                anchor.tag != XHTML + "a" or set(anchor.attrib) != {"id"} or len(anchor)
                for anchor in anchors
            ):
                continue
            candidate = (name, heading, body)
            candidates.append(candidate)
            for node in (heading, body):
                for child in node.iter(etree.Element):
                    if ident := child.get("id"):
                        targets[name, ident] = candidate

    navigation_entries = defaultdict(set)
    blocked = set()
    for name, root in roots.items():
        for node in root.iter(etree.Element):
            for attribute in ("href", "src", XLINK + "href"):
                destination = local_fragment(name, node.get(attribute, ""))
                if destination not in targets:
                    continue
                candidate = targets[destination]
                parent = node.getparent()
                if (
                    node.tag == XHTML + "a" and parent is not None and parent.tag == XHTML + "li"
                    and len(parent) == 1 and heading_text(parent) == "Exercices"
                ):
                    navigation_entries[candidate].add((name, parent))
                elif (
                    node.tag == ncx + "content" and parent is not None and parent.tag == ncx + "navPoint"
                    and parent.find(ncx + "navPoint") is None and heading_text(parent) == "Exercices"
                ):
                    navigation_entries[candidate].add((name, parent))
                else:
                    blocked.add(candidate)
            for attribute in ("aria-labelledby", "aria-describedby", "headers", "for"):
                for ident in node.get(attribute, "").split():
                    if (name, ident) in targets:
                        blocked.add(targets[name, ident])

    changed = set()
    counts = Counter()
    removed_entries = set()
    for candidate in candidates:
        if candidate in blocked:
            continue
        name, heading, body = candidate
        heading.getparent().remove(heading)
        body.getparent().remove(body)
        changed.add(name)
        counts["empty_exercise_sections"] += 1
        for nav_name, entry in navigation_entries[candidate] - removed_entries:
            entry.getparent().remove(entry)
            removed_entries.add((nav_name, entry))
            changed.add(nav_name)
            counts["empty_exercise_navigation_entries"] += 1
    for name in changed:
        if not name.endswith(".ncx"):
            continue
        points = list(roots[name].iter(ncx + "navPoint"))
        if all(point.get("playOrder", "").isdigit() for point in points):
            for order, point in enumerate(sorted(points, key=lambda p: int(p.get("playOrder"))), 1):
                point.set("playOrder", str(order))
    return changed, counts


def add_proof_rule_descriptions(root):
    """Describe the source-checked rule sheets by chapter, section and order."""
    chapter = root.find(".//" + XHTML + "h2")
    if chapter is None:
        return 0
    chapter_title = heading_text(chapter)
    sheets = next((sections for title, sections in PROOF_RULE_SHEETS.items() if chapter_title.endswith(title)), None)
    if sheets is None:
        return 0
    count = 0
    for heading in root.iter(XHTML + "h3"):
        equality = EQUALITY_RULE_ALTS.get(heading.get("id"))
        if equality is not None:
            count += describe_equality_rule_frame(heading, equality)
            continue
        title = heading_text(heading)
        alternatives = next((alts for section, alts in sheets.items() if title.endswith(section)), None)
        if alternatives is None:
            continue
        groups = {}
        used_frames = set()
        extra_frames = []
        for sibling in heading.itersiblings():
            if sibling.tag in {XHTML + "h2", XHTML + "h3"}:
                break
            if sibling.tag == XHTML + "div" and sibling.get("class") == "framedenv" and sibling not in used_frames:
                extra_frames.append(sibling)
            if sibling.tag != XHTML + "h4":
                continue
            formula = sibling.find(".//" + MATH + "math")
            key = heading_text(formula).replace("\u2061", "").strip() if formula is not None else heading_text(sibling)
            frame = sibling.getnext()
            if key not in alternatives or key in groups or frame is None or frame.get("class") != "framedenv":
                break
            images = checked_rule_images(frame, len(alternatives[key]))
            if images is None:
                break
            groups[key] = images
            used_frames.add(frame)
        if tuple(groups) != tuple(alternatives):
            continue
        for key, images in groups.items():
            for image, description in zip(images, alternatives[key], strict=True):
                image.set("alt", description)
                count += 1
        if alternatives is SEQUENT_STRUCTURAL_RULE_ALTS and len(extra_frames) == 1:
            images = checked_rule_images(extra_frames[0], 1)
            if images is not None:
                images[0].set("alt", SEQUENT_CUT_ALT)
                count += 1
    return count


def describe_modal_tableau_tables(root):
    """Match the modal rule tables by their rendered captions and cell order."""
    captions = dict(MODAL_RULE_TABLE_ALTS)
    count = 0
    for figure in root.iter(XHTML + "figure"):
        caption = next(figure.iter(XHTML + "figcaption"), None)
        if caption is None:
            continue
        title = heading_text(caption).partition(" : ")[2].replace("𝐒", "S")
        alternatives = captions.get(title)
        if alternatives is None:
            continue
        images = checked_rule_images(figure, len(alternatives))
        if images is not None:
            for image, description in zip(images, alternatives, strict=True):
                image.set("alt", description)
                count += 1
    return count


def describe_modal_k_sequents(root):
    chapter = root.find(".//" + XHTML + "h2")
    if chapter is None or chapter.get("id") != "calcul-des-sequents-pour-la-logique-modale":
        return 0
    expected = (
        ("Introduction", (MODAL_K_SEQUENT_ALTS,)),
        ("Règles pour K", (MODAL_K_SEQUENT_ALTS, *INVALID_MODAL_K_SEQUENT_ALTS)),
    )
    sections = list(root.iter(XHTML + "h3"))
    count = 0
    for heading, (title, tables) in zip(sections, expected):
        if not heading_text(heading).replace("𝐊", "K").endswith(title):
            continue
        equations = []
        for item in heading.itersiblings():
            if item.tag == XHTML + "h3":
                break
            if item.tag == XHTML + "table" and item.get("class") == "equation-star":
                equations.append(item)
        if len(equations) != len(tables):
            continue
        for equation, descriptions in zip(equations, tables, strict=True):
            images = checked_rule_images(equation, len(descriptions))
            if images is not None:
                for image, description in zip(images, descriptions, strict=True):
                    image.set("alt", description)
                    count += 1
    return count


def describe_equality_rule_frame(heading, alternatives):
    frames = []
    for sibling in heading.itersiblings():
        if sibling.tag in {XHTML + "h2", XHTML + "h3"}:
            break
        if sibling.tag == XHTML + "div" and sibling.get("class") == "framedenv":
            frames.append(sibling)
    if len(frames) != 1:
        return 0
    images = checked_rule_images(frames[0], len(alternatives))
    if images is None:
        return 0
    for image, description in zip(images, alternatives, strict=True):
        image.set("alt", description)
    return len(images)


def checked_rule_images(frame, count):
    images = list(frame.iter(XHTML + "img"))
    if len(images) == count and all(
        " ".join(image.get("alt", "").split()) == "Arbre de dérivation"
        and image.get("src", "").endswith(".svg")
        for image in images
    ):
        return images
    return None


def repair(source, output):
    with ZipFile(source) as book:
        roots = {
            name: etree.fromstring(book.read(name))
            for name in book.namelist()
            if name.endswith((".xhtml", ".svg", ".ncx"))
        }
        exercise_documents, exercise_counts = remove_empty_exercise_sections(roots)
        ids = defaultdict(list)
        note_locations = defaultdict(list)
        referenced = set()
        stylesheets = b"\n".join(book.read(name) for name in book.namelist() if name.endswith(".css"))
        for name, root in roots.items():
            for element in root.iter(etree.Element):
                if ident := element.get("id"):
                    ids[name, ident].append(element)
                    if element.tag == XHTML + "aside" and element.get(EPUB + "type") == "footnote":
                        note_locations[ident].append(name)
                for attribute in ("href", XLINK + "href", "src"):
                    if (value := element.get(attribute)) and (dest := local_fragment(name, value)):
                        referenced.add(dest)
                for attribute in ("aria-labelledby", "aria-describedby", "headers", "for"):
                    referenced.update((name, ident) for ident in element.get(attribute, "").split())
                for value in element.attrib.values():
                    referenced.update((name, ident) for ident in re.findall(r"url\(#([^)]+)\)", value))
        changed = {
            name: etree.tostring(roots[name], encoding="utf-8", xml_declaration=True)
            for name in exercise_documents
        }
        totals = exercise_counts
        unresolved = []
        for name, root in roots.items():
            if not name.endswith(".xhtml"):
                continue
            repairs = Counter()
            for link in tuple(root.iter(XHTML + "a")):
                href = link.get("href", "")
                if HYPERREF_FOOTNOTE.fullmatch(href) and (name, href[1:]) not in ids:
                    if (
                        set(link.attrib) != {"href"} or (link.text or "").strip()
                        or len(link) != 1 or link[0].tag != XHTML + "a"
                        or link[0].get(EPUB + "type") != "noteref"
                        or (link[0].tail or "").strip()
                    ):
                        unresolved.append([name, href, "unrecognized nested footnote link"])
                        continue
                    child = link[0]
                    note = local_fragment(name, child.get("href", ""))
                    if note is None or not NOTEREF_ID.fullmatch(note[1]) or not note_locations[note[1]]:
                        unresolved.append([name, href, "unrecognized footnote destination"])
                        continue
                    child.tail = (child.tail or "") + (link.tail or "")
                    link.getparent().replace(link, child)
                    repairs["redundant_html_footnote_links"] += 1
                elif link.get(EPUB + "type") == "noteref":
                    note = local_fragment(name, href)
                    if note is None or note in ids:
                        continue
                    locations = note_locations[note[1]]
                    if not NOTEREF_ID.fullmatch(note[1]) or len(locations) != 1:
                        unresolved.append([name, href, "no unique footnote destination"])
                        continue
                    new_path = posixpath.relpath(locations[0], posixpath.dirname(name))
                    link.set("href", new_path + "#" + note[1])
                    repairs["cross_document_footnote_links"] += 1

            seen = set()
            for element in root.iter(etree.Element):
                ident = element.get("id")
                if not ident or len(ids[name, ident]) < 2:
                    continue
                if ident not in seen:
                    seen.add(ident)
                    continue
                if (
                    not TEX4HT_ID.fullmatch(ident) or (name, ident) in referenced
                    or b"#" + ident.encode("utf-8") in stylesheets
                ):
                    unresolved.append([name, ident, "duplicate ID may be referenced"])
                    continue
                del element.attrib["id"]
                repairs["unreferenced_duplicate_generated_ids"] += 1

            head = root.find(XHTML + "head")
            title = head.find(XHTML + "title") if head is not None else None
            if name.endswith("/reader.xhtml") and title is not None and not "".join(title.itertext()).strip():
                title.text = "OpenLogic — Édition française"
                repairs["empty_reader_title"] += 1
            if title is not None and re.fullmatch(r"\d+ Histoire et mythologie de la thérie des ensembles", title.text or ""):
                title.text = title.text.replace("thérie", "théorie")
                repairs["set_theory_document_title"] += 1
            repairs.update(fix_math_markup(root))
            repairs.update(repair_html_structure(root))
            repairs.update(add_checked_figure_descriptions(root))
            if described := add_proof_rule_descriptions(root):
                repairs["proof_rules_described"] += described
            if described := describe_modal_tableau_tables(root):
                repairs["modal_rule_tables_described"] += described
            if described := describe_modal_k_sequents(root):
                repairs["modal_k_sequents_described"] += described
            if corrected := repair_ordinal_footnote(root, name, ids):
                repairs["linked_ordinal_footnote_markers"] += corrected
            if repairs:
                changed[name] = etree.tostring(root, encoding="utf-8", xml_declaration=True)
                totals.update(repairs)
        for name in book.namelist():
            if name.endswith(".css") and totals["legacy_table_rules_moved_to_css"]:
                css = book.read(name)
                if b"table[rules]" in css:
                    changed[name] = css.replace(b"table[rules]", b"table.column-group-rules") + (
                        b"\ntable.column-group-rules > colgroup { border-left: 0.4pt solid black; }\n"
                        b"figure.centered-caption > figcaption { margin-top: 1em; }\n"
                    )
            if not name.endswith(".opf"):
                continue
            root = etree.fromstring(book.read(name))
            repaired = False
            for item in root.iter(OPF + "item"):
                properties = item.get("properties", "").split()
                if "mathml" not in properties or not item.get("href", "").endswith(".xhtml"):
                    continue
                path = posixpath.normpath(posixpath.join(posixpath.dirname(name), item.get("href")))
                if path in roots and roots[path].find(".//" + MATH + "math") is None:
                    remaining = " ".join(x for x in properties if x != "mathml")
                    if remaining:
                        item.set("properties", remaining)
                    else:
                        del item.attrib["properties"]
                    repaired = True
                    totals["unused_mathml_manifest_property"] += 1
            if repaired:
                changed[name] = etree.tostring(root, encoding="utf-8", xml_declaration=True)
        with ZipFile(output, "x") as repaired:
            for item in book.infolist():
                repaired.writestr(item, changed[item.filename] if item.filename in changed else book.read(item))

    return dict(
        input_sha256=sha256(source.read_bytes()).hexdigest(),
        output_sha256=sha256(output.read_bytes()).hexdigest(),
        changed_members=sorted(changed),
        repairs=dict(totals),
        unresolved=unresolved,
    )


if __name__ == "__main__":
    source, output = map(Path, sys.argv[1:])
    report = repair(source, output)
    output.with_suffix(".json").write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n"
    )
    print(json.dumps({**report, "changed_members": len(report["changed_members"])}))
