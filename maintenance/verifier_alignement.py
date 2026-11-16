"""Retrouver les passages anglais et français dans l'archive publique de l'édition."""
import argparse
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile

INDEX = Path(__file__).with_name("alignement-v1.0.0.jsonl")
INDEX_SHA256 = "6391491267da31cb78ea7515f9e84483b5e19608f2830dfe87cb6330d6b605a6"
ARCHIVE_SHA256 = "fe6fb8041443e484d9339e4d1f263c7afc14a4d8c914d0e7cd447fb6176f11f4"


def digest(data):
    return hashlib.sha256(data).hexdigest()


def excerpt(text, address):
    mode = address["mode"]
    if mode != "lines-original":
        text = text.replace("\r\n", "\n")
    lines = text.split("\n")
    first, last = address["lines"]
    if not 1 <= first <= last <= len(lines):
        raise ValueError("Plage de lignes hors du fichier.")
    if mode == "characters-lf":
        start, end = address["characters"]
        if not 0 <= start <= end <= len(text):
            raise ValueError("Plage de caractères hors du fichier.")
        return text[start:end]
    if mode not in {"lines-lf", "lines-original"}:
        raise ValueError("Mode de découpage inconnu.")
    return "\n".join(lines[first-1:last])


def verify(archive_path):
    index = INDEX.read_bytes().replace(b"\r\n", b"\n")
    if digest(index) != INDEX_SHA256:
        raise ValueError("L’index diffère de celui de la version v1.0.0.")
    with archive_path.open("rb") as stream:
        if hashlib.file_digest(stream, "sha256").hexdigest() != ARCHIVE_SHA256:
            raise ValueError("L’archive ne correspond pas à la version v1.0.0.")
    seen_units, seen_segments = set(), set()
    with ZipFile(archive_path) as archive:
        manifest = archive.read("OpenLogic-fr/provenance/SOURCE_MANIFEST.jsonl")
        source_paths = {r["unit_id"]: r["source_path"] for r in map(json.loads, manifest.splitlines())}
        for unit in map(json.loads, index.splitlines()):
            key, path = unit["unit"], unit["path"]
            if key in seen_units or source_paths.get(key) != path:
                raise ValueError(f"Unité répétée ou chemin inattendu : {key}")
            seen_units.add(key)
            for segment in unit["segments"]:
                if segment["id"] in seen_segments:
                    raise ValueError(f"Identifiant répété : {segment['id']}")
                seen_segments.add(segment["id"])
            for side, directory in (("source", "upstream"), ("target", "fr")):
                data = archive.read(f"OpenLogic-fr/{directory}/{path}")
                if digest(data) != unit[side + "_sha256"]:
                    raise ValueError(f"Fichier différent : {key}, {side}")
                text = data.decode("utf-8")
                for segment in unit["segments"]:
                    address = segment[side]
                    part = excerpt(text, address)
                    if digest(part.encode("utf-8")) != address["sha256"]:
                        raise ValueError(f"Passage différent : {segment['id']}, {side}")
    if seen_units != source_paths.keys():
        raise ValueError("L’index ne couvre pas toutes les unités de l’archive.")
    return len(seen_units), len(seen_segments)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", type=Path, help="chemin de l’archive openlogic-fr-sources.zip")
    try:
        units, segments = verify(parser.parse_args().archive)
    except (OSError, ValueError, KeyError) as error:
        parser.exit(1, str(error) + "\n")
    print(f"{units} unités et {segments} paires de passages correspondent à l’archive.")
