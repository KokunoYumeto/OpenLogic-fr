"""Afficher les références associées à un passage de l'édition française."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
STATUS = {
    None: "Le registre ne précise pas de catégorie de contrôle.",
    "contextually_compared": "Comparaison en contexte.",
    "bounded_retrospective_reference_article_check": "Réexamen de l’article grammatical d’un renvoi.",
    "contextually_reexamined_during_repair": "Formulation réexaminée en contexte lors d’une correction.",
    "french_evidence_gap_pending": "Les attestations en français restent à compléter.",
    "retrospective_scoped_heading_evidence_recorded": "Attestation rétrospective limitée à l’intitulé.",
    "retrospective_scoped_french_evidence_recorded": "Attestation rétrospective limitée à certains choix.",
    "substantive_french_prose_canon_evidence_pending": "Attestation de la prose mathématique française à compléter.",
    "no_direct_passage": "Aucun passage directement associé.",
    "contextually_compared_after_drafting": "Comparaison en contexte après rédaction.",
    "substantive_french_language_evidence_pending": "Attestation des choix de langue française à compléter.",
    "not_needed_for_structural_driver": "Fichier d’assemblage à rôle structurel.",
    "terminology_compared": "Terminologie comparée.",
    "bounded_retrospective_reference_phrase_check": "Réexamen limité à la formulation d’un renvoi.",
}


def index(filename, key):
    with (ROOT / filename).open(encoding="utf-8") as stream:
        return {row[key]: row for row in map(json.loads, stream)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("segment", help="identifiant de l’index d’alignement, par exemple OLP-0248-R00")
    args = parser.parse_args()
    links = index("consultations-par-segment.jsonl", "segment")
    if args.segment not in links:
        parser.error("identifiant absent de l’index d’alignement")
    row = links[args.segment]
    passages = index("reperes-du-canon.jsonl", "id")
    sources = index("sources-du-canon.jsonl", "id")
    print(args.segment, STATUS[row["classement_historique"]], sep="\n")
    if row["classe_formelle_declaree"]:
        print("Segment classé comme formel dans le registre.")
    ids = []
    def group(label, refs):
        print(label, ", ".join(refs) or "Aucun repère consigné.", sep="\n  ")
        ids.extend(refs)
    group("Repères associés", row["passages_associes"])
    if "passages_du_reexamen" in row:
        group("Repères d’un réexamen", row["passages_du_reexamen"])
    for review in row.get("reexamens_retrospectifs", []):
        same = review.get("concorde_avec_edition")
        label = {True:"Réexamen du passage publié", False:"Réexamen d’une rédaction différente",
                 None:"Réexamen sans empreinte du passage"}[same]
        group(label, review["passages"])
    if "controle_du_francais" in row:
        review = row["controle_du_francais"]
        label = {"scoped_evidence_recorded_whole_unit_acceptance_pending":"Examen de langue limité à certains choix",
                 "pending_french_canon_consultation":"Examen de langue en attente"}[review["etat"]]
        group(label, review["passages"])
    for key in dict.fromkeys(ids):
        passage = passages[key]
        source = sources[passage["source"]]
        authors = source["auteurs"]
        byline = ", ".join(authors) if isinstance(authors, list) else authors
        print(f"\n{key} — {source['titre']}")
        if byline:
            print(byline)
        print(passage["repere"], source["url"], sep="\n")


if __name__ == "__main__":
    main()
