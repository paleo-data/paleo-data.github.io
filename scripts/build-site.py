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


def autolink(text: str) -> str:
    """Locates and adds anchor tags to external links in text"""
    for url in set(re.findall(r"https?://[^\s]+", text)):
        text = text.replace(url, f'<a href="{url}">{url}</a>')
    return text


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
            "creators": "; ".join([p["name"] for p in metadata["creators"]]),
            "description": autolink(re.sub("\n{2,}", "<br><br>", desc.text)),
            "link": rec["doi_url"],
            "url": f"{to_slug(metadata['title'])}.md",
        }

        rows[rec["doi_url"]] = row

        with open(path / f"{to_slug(row['title'])}.md", "w", encoding="utf-8") as f:
            f.write(
                write_header(
                    {"title": row["title"], "parent": "Resources", "layout": "single"}
                )
            )

    with open(BASEPATH / "_data" / "resources.yml", "w", encoding="utf-8") as f:
        yaml.dump(rows, f)

    # Read page headers
    headers = {}
    for path in Path("..").glob("**/*.md"):
        header = parse_header(path)
        header["path"] = path
        headers[header["title"]] = header

    # Build navigation from page headers
    nav = {}
    for title, header in headers.items():
        path = [header["path"].stem]
        if path[0] == "index":
            path.insert(0, to_slug(header["title"]))
        try:
            parent = headers[header["parent"]]
        except KeyError:
            parent = None
        while parent:
            path.insert(0, to_slug(parent["title"]))
            try:
                parent = headers[headers["parent"]]
            except KeyError:
                break

        if path[0] == "home":
            path = path[1:]

        header["path"] = "/".join(path) + ".md"

        if path[-1] == "index":
            path = path[:-1]

        url = "/" + "/".join(path)

        if len(path) == 1:
            nav.setdefault("main", []).append({"title": title, "url": url})

    with open(BASEPATH / "_data" / "navigation.yml", "w") as f:
        yaml.dump(nav, f, sort_keys=False)

    # Index tags
    tags = {}
    for header in headers.values():
        for tag in header.get("tags", []):
            tags.setdefault(tag, []).append(
                {"title": header["title"], "path": header["path"]}
            )

    with open(BASEPATH / "_data" / "tags.yml", "w") as f:
        yaml.dump(dict(sorted(tags.items(), key=lambda kv: kv[0])), f)
