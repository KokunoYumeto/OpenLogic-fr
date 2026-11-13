"""Normalize specific TeX4ht MathML forms while preserving content and order."""

from collections import Counter
import re

from lxml import etree


MATH = "{http://www.w3.org/1998/Math/MathML}"
XHTML = "{http://www.w3.org/1999/xhtml}"
MATH_SCRIPT = {MATH + name for name in ("msup", "msub", "msubsup", "mover", "munder")}
MATH_OPERATOR = {"−", "∗", "′", "″", "‴", "∈", "↦", "→", "+", "<"}


def math_element(name, **attributes):
    return etree.Element(MATH + name, **attributes)


def replace_node(node, replacement):
    replacement.tail = node.tail
    node.getparent().replace(node, replacement)


def add_content(wrapper, content):
    for child in list(content):
        wrapper.append(child)
    wrapper.text = content.text


def fix_nicefractions(root):
    count = 0
    for top in tuple(root.iter(MATH + "sup")):
        slash = top.getnext()
        bottom = slash.getnext() if slash is not None else None
        if (
            top.get("class") != "nicefrac"
            or slash is None or slash.tag != MATH + "mo" or slash.text != "/" or len(slash)
            or bottom is None or bottom.tag != MATH + "sub" or bottom.get("class") != "nicefrac"
            or any((node.tail or "").strip() for node in (top, slash))
            or any(set(node.attrib) != {"class"} for node in (top, bottom))
        ):
            continue
        parent = top.getparent()
        fraction = math_element("mfrac", bevelled="true")
        for old in (top, bottom):
            operand = math_element("mrow")
            add_content(operand, old)
            fraction.append(operand)
        parent.insert(parent.index(top), fraction)
        fraction.tail = bottom.tail
        for old in (top, slash, bottom):
            parent.remove(old)
        count += 1
    return count


def fix_image_annotations(root):
    count = 0
    for semantic in tuple(root.iter(MATH + "semantics")):
        if len(semantic) != 1 or semantic.attrib or (semantic.text or "").strip():
            continue
        annotation = semantic[0]
        if (
            annotation.tag != MATH + "annotation-xml"
            or annotation.get("encoding") != "application/xhtml+xml"
            or len(annotation) != 1
            or annotation[0].tag != XHTML + "img"
            or (annotation.text or "").strip() or (annotation.tail or "").strip()
            or (annotation[0].tail or "").strip()
        ):
            continue
        image = annotation[0]
        if not image.get("src", "").endswith(".svg"):
            continue
        # HTML images inside mtext are presentation content. In the original
        # wrapper the image was only an annotation with no presentation child.
        text = math_element("mtext")
        if image.get("alt") == "Arbrededérivation":
            image.set("alt", "Arbre de dérivation")
        text.append(image)
        replace_node(semantic, text)
        count += 1
    return count


def fix_embedded_math_in_tokens(root):
    count = 0
    for token in tuple(root.iter(MATH + "mi", MATH + "mo")):
        children = list(token)
        if not children or any(
            child.tag not in MATH_SCRIPT | {MATH + "mrow"}
            for child in children
        ):
            continue
        if set(token.attrib) - {"class", "stretchy", "mathvariant"}:
            continue
        row = math_element("mrow")
        if css_class := token.get("class"):
            row.set("class", css_class)
        segments = [token.text, *(child.tail for child in children)]
        for index, value in enumerate(segments):
            if value and value.strip():
                fragment = etree.Element(token.tag, **dict(token.attrib))
                fragment.text = value
                row.append(fragment)
            if index < len(children):
                child = children[index]
                child.tail = None
                if token.tag == MATH + "mi" and token.get("mathvariant"):
                    variant = math_element("mstyle", mathvariant=token.get("mathvariant"))
                    variant.append(child)
                    row.append(variant)
                else:
                    row.append(child)
        replace_node(token, row)
        count += 1
    return count


def fix_script_tokens(root):
    count = 0
    for row in root.iter(MATH + "mrow"):
        parent = row.getparent()
        if parent is None:
            continue
        value = (row.text or "").strip()
        if not value or len(row) or row.attrib:
            continue
        overlay = parent.tag == MATH + "mrow" and parent.get("class") == "oalign"
        if overlay:
            if value not in {"↦", "→"}:
                continue
            row.tag = MATH + "mo"
            count += 1
            continue
        if parent.tag not in MATH_SCRIPT:
            continue
        if re.fullmatch(r"\d+", value):
            row.tag = MATH + "mn"
        elif len(value) == 1 and value.isalpha():
            row.tag = MATH + "mi"
        elif value in MATH_OPERATOR:
            row.tag = MATH + "mo"
        elif value == "true":
            row.tag = MATH + "mtext"
        else:
            continue
        count += 1
    return count


def fix_quotient_atoms(root):
    count = 0
    for style in root.iter(MATH + "mstyle"):
        text = style.text or ""
        if style.attrib or not re.fullmatch(r"\s*[cfR]𝔐/", text) or len(style) != 1:
            continue
        space = style[0]
        if space.tag != MATH + "mspace" or space.get("class") != "negthinspace" or space.tail != "≈":
            continue
        style.text = None
        space.tail = None
        for i, (tag, value) in enumerate((("mi", text.strip()[0]), ("mi", "𝔐"), ("mo", "/"))):
            token = math_element(tag)
            token.text = value
            style.insert(i, token)
        approximation = math_element("mo")
        approximation.text = "≈"
        style.append(approximation)
        count += 1
    return count


def fix_math_text_styles(root):
    result = Counter()
    for strong in root.iter(MATH + "strong"):
        parent = strong.getparent()
        if strong.attrib or parent.tag != MATH + "mstyle" or parent.get("mathvariant") != "bold":
            continue
        strong.tag = MATH + "mrow"
        result["bold_math_groups"] += 1
    for span in root.iter(MATH + "span"):
        if dict(span.attrib) == {"class": "small-caps"}:
            span.tag = MATH + "mrow"
            result["small_caps_math_groups"] += 1
    return result


def fix_math_markup(root):
    result = Counter({
        "nicefrac_to_bevelled_fraction": fix_nicefractions(root),
        "svg_annotations_to_presented_images": fix_image_annotations(root),
        "split_tokens_containing_math_expressions": fix_embedded_math_in_tokens(root),
        "script_tokens_given_mathml_types": fix_script_tokens(root),
        "quotient_notation_atoms": fix_quotient_atoms(root),
    })
    result.update(fix_math_text_styles(root))
    for table in root.iter(MATH + "mtable"):
        if "rowlines" in table.attrib and not table.get("rowlines").strip():
            del table.attrib["rowlines"]
            result["empty_mathml_rowlines_omitted"] += 1
    return +result
