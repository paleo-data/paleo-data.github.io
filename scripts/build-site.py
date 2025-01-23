import re
import os
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup
from unidecode import unidecode

try:
    BASEPATH = Path(os.environ["GITHUB_WORKSPACE"])
except KeyError:
    BASEPATH = Path("..")


def parse_header(path: Path) -> dict:
    """Parses the Jekyll header in a markdown file"""
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f.read().lstrip("---").split("---")[0])


def to_slug(val: str) -> str:
    """Constructs a python attribute string from the given value"""
    val = val.replace("/", "")
    val = unidecode(val)
    val = re.sub(r'["\']', "", val)
    val = re.sub(r"[^A-z\d]+", "_", val)
    val = re.sub(r"([A-Z])(?!(?:[A-Za-z_]|$))", r"_\1", val)
    val = re.sub(r"(?<![A-Z_])([A-Z])", r"_\1", val)
    val = re.sub(r"(?<![\d_])([\d])", r"_\1", val)
    val = re.sub(r"_+", "_", val)
    return val.lower().strip("_").replace("_", "-")


def write_header(header: dict) -> str:
    """Parses the Jekyll header in a markdown file"""
    return "\n".join(["---", yaml.dump(header, sort_keys=False), "---", ""])


if __name__ == "__main__":

    path = BASEPATH / "collections" / "_resources"
    path.mkdir(parents=True, exist_ok=True)

    with open(BASEPATH / "_data" / "zenodo.yml") as f:
        zenodo_ids = yaml.safe_load(f)

    # Get data from Zenodo
    rows = {}
    for zid in zenodo_ids:
        resp = requests.get(f"https://zenodo.org/api/records/{zid}")
        rec = resp.json()

        metadata = rec["metadata"]
        desc = BeautifulSoup(metadata["description"], "html5lib")

        row = {
            "title": metadata["title"],
            "creators": [p["name"] for p in metadata["creators"]],
            "description": re.sub("\n{2,}", "<br><br>", desc.text),
            "link": rec["doi_url"],
        }

        rows[rec["doi_url"]] = row

        with open(path / f"{to_slug(row['title'])}.md", "w", encoding="utf-8") as f:
            f.write(write_header({"title": row["title"], "parent": "Resources"}))
            f.write("\n")
            f.write(f"# {row['title']}")

    with open(BASEPATH / "_data" / "resources.yml", "w", encoding="utf-8") as f:
        yaml.dump(rows, f)
