"""Creates and indexes pages based using YAML files in _data"""

import re
import os
import time
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup
from unidecode import unidecode


def autolink(text: str) -> str:
    """Locates and adds anchor tags to external links in text"""
    for url in set(re.findall(r"https?://[^\s]+", text)):
        text = text.replace(url, f'<a href="{url}">{url}</a>')
    return text


def split_path(path: Path) -> list:
    """Splits a path into segments"""
    segments = []
    while str(path) != ".":
        segments.insert(0, path.name)
        path = path.parent
    return segments


def parse_header(path: Path) -> dict:
    """Parses the Jekyll front matter in a markdown file"""
    with open(path, encoding="utf-8") as f:
        try:
            return yaml.safe_load(f.read().lstrip("---").split("---")[0])
        except Exception as exc:
            raise ValueError(path) from exc


def to_slug(val: str) -> str:
    """Constructs a Python attribute string from the given value"""
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
    """Writes Jekyll front matter to a markdown file"""
    return "\n".join(["---", yaml.dump(header, sort_keys=False).rstrip(), "---", ""])


if __name__ == "__main__":

    try:
        basepath = Path(os.environ["GITHUB_WORKSPACE"])
    except KeyError:
        basepath = Path("..")

    # Construct a collection of external resources
    path = basepath / "collections" / "_resources"
    path.mkdir(parents=True, exist_ok=True)

    # Create pages from Zenodo records based on list of Zenodo IDs in the _data folder
    with open(basepath / "_data" / "zenodo.yml", encoding="utf-8") as f:
        zenodo_ids = yaml.safe_load(f)

    rows = {}
    for i, zid in enumerate(zenodo_ids):

        # Enforce a short delay between requests to Zenodo
        if i:
            time.sleep(0.5)

        resp = requests.get(f"https://zenodo.org/api/records/{zid}")
        rec = resp.json()

        metadata = rec["metadata"]
        desc = BeautifulSoup(metadata["description"], "html5lib")

        # The value in path is used in a link tag, which expects the location of
        # the file in the _site directory. Note that those paths omit the collections
        # directory (defined in collections_dir in the config file).
        row = {
            "title": metadata["title"],
            "creators": "; ".join([p["name"] for p in metadata["creators"]]),
            "description": autolink(re.sub("\n{2,}", "<br><br>", desc.text)),
            "link": rec["doi_url"],
            "path": f"_resources/{to_slug(metadata['title'])}.md",
        }

        rows[rec["doi_url"]] = row

        with open(path / f"{to_slug(row['title'])}.md", "w", encoding="utf-8") as f:
            f.write(
                write_header(
                    {"title": row["title"], "parent": "Resources", "layout": "single"}
                )
            )

    with open(basepath / "_data" / "resources.yml", "w", encoding="utf-8") as f:
        yaml.dump(rows, f)

    # Read page headers. Omit the vendor directory populated by GitHub actions.
    headers = {}
    for path in Path("..").glob("**/*.md"):
        if "vendor" not in split_path(path):
            header = parse_header(path)
            header["path"] = path
            headers[header["title"]] = header

    # Build navigation from page headers. Pages are sorted ny nav_order, then title.
    headers = dict(
        sorted(
            headers.items(),
            key=lambda kv: (kv[1].get("nav_order", 100), kv[1]["title"].lower()),
        )
    )

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

        # Both collections and home are not part of the site organization
        if path[0] in ("collections", "home"):
            path = path[1:]

        # The value in path can be used with the Jekyll link tag
        header["path"] = "/".join(path) + ".md"

        if path[-1] == "index":
            path = path[:-1]

        # URL is a root-relative URL. The minimal-mistakes theme uses this
        # format in URLs in _includes.
        url = "/" + "/".join(path)

        if len(path) == 1:
            nav.setdefault("main", []).append({"title": title, "url": url})

    with open(basepath / "_data" / "navigation.yml", "w", encoding="utf-8") as f:
        yaml.dump(nav, f, sort_keys=False)

    # Index tags
    tags = {}
    for header in headers.values():
        for tag in header.get("tags", []):
            tags.setdefault(tag, []).append(
                {"title": header["title"], "path": header["path"]}
            )

    with open(basepath / "_data" / "tags.yml", "w", encoding="utf-8") as f:
        yaml.dump(dict(sorted(tags.items(), key=lambda kv: kv[0])), f)
