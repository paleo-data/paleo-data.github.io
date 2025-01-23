"""Creates and indexes pages based using YAML files in _data"""

import re
import os
import time
from pathlib import Path

import requests
import yaml
from bs4 import BeautifulSoup
from unidecode import unidecode


def autolink(text: str, fmt: str = "markdown") -> str:
    """Locates and adds anchor tags to external links in text"""
    for url in set(re.findall(r"https?://[^\s]+", text)):
        strip_chars = ",."
        if "(" not in url:
            strip_chars += ")"
        url = url.rstrip(strip_chars)
        if fmt == "html":
            text = text.replace(url, f'<a href="{url}">{url}</a>')
        elif fmt == "markdown":
            text = text.replace(url, f"[{url}]({url})")
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

        # Remove all markdown files from collections
        for path in (basepath / "collections").glob("**/*.md"):
            path.unlink()

    # Construct a collection of external resources
    path = basepath / "collections" / "_resources"
    path.mkdir(parents=True, exist_ok=True)

    with open(basepath / "templates" / "resource", encoding="utf-8") as f:
        template = f.read()

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
            "description": autolink(re.sub("\n{2,}", "\n\n", desc.text)),
            "resource_url": rec["doi_url"],
            "path": f"_resources/{to_slug(metadata['title'])}.md",
            "nav_order": 1,
        }

        fpath = path / f"{to_slug(row['title'])}.md"
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(write_header(row))
            f.write("\n")
            f.write(template)
        print(f"Wrote {fpath.name}")

    # Read page headers. Omit the vendor directory used by GitHub actions.
    headers = {}
    for path in Path("..").glob("**/*.md"):
        if "vendor" not in split_path(path):
            header = parse_header(path)
            header["path"] = path
            headers[header["title"]] = header

    # Determine paths to individual pages
    for title, header in headers.items():

        key = None
        segments = split_path(header["path"])

        # Collections get their own sidebar
        if "collections" in segments:
            key = segments[-2].lstrip("_")
            path = [key, Path(segments[-1]).stem]

        else:

            # Build paths to content based on the parent attribute
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

            # Omit home
            if path[0] == "home":
                path = path[1:]

            # Omit index
            if path[-1] == "index":
                path = path[:-1]

            if len(path) == 1:
                key = "main"

        # Add navigation info to header
        header["key"] = key
        header["path"] = "/".join(path) + ".md"

    # Index tags in headers
    tags = {}
    for header in headers.values():
        for tag in header.get("tags", []):
            tags.setdefault(tag, []).append(
                {"title": header["title"], "path": header["path"]}
            )

    # Create tag collection
    path = basepath / "collections" / "_tags"
    path.mkdir(parents=True, exist_ok=True)

    with open(basepath / "templates" / "tag", encoding="utf-8") as f:
        template = f.read()

    for tag, pages in tags.items():
        fpath = path / f"{to_slug(tag)}.md"
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(write_header({"title": tag, "pages": pages}))
            f.write("\n")
            f.write(template)
        print(f"Wrote {fpath.name}")
        headers[tag] = {"key": "tags", "title": tag, "path": f"tags/{to_slug(tag)}"}

    # Sort header by nav_order, then title
    headers = dict(
        sorted(
            headers.items(),
            key=lambda kv: (kv[1].get("nav_order", 100), kv[1]["title"].lower()),
        )
    )

    # Build navigation
    nav = {}
    for title, header in headers.items():
        key = header["key"]
        url = "/" + header["path"].rsplit(".", 1)[0]
        if key == "main":
            nav.setdefault(key, []).append({"title": title, "url": url})
        elif key:
            nav.setdefault(key, []).append({"title": key})
            nav[key][-1].setdefault("children", []).append({"title": title, "url": url})

    fpath = basepath / "_data" / "navigation.yml"
    with open(fpath, "w", encoding="utf-8") as f:
        yaml.dump(nav, f, sort_keys=False)

    print(f"Wrote {fpath.name}")
