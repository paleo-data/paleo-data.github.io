"""Creates and indexes pages based using YAML files in _data"""

import re
import time

import requests
import yaml
from bs4 import BeautifulSoup

from const import BASEPATH
from utils import (
    autolink,
    build_nav,
    compute_urls,
    index_tags,
    read_fms,
    to_slug,
    write_fm,
)


if __name__ == "__main__":

    # Construct a collection of external resources from Zenodo
    path = BASEPATH / "collections" / "_resources"
    path.mkdir(parents=True, exist_ok=True)

    with open(BASEPATH / "templates" / "resource", encoding="utf-8") as f:
        template = f.read()

    # Create pages from Zenodo records based on list of Zenodo IDs in the _data folder
    with open(BASEPATH / "_data" / "zenodo.yml", encoding="utf-8") as f:
        zenodo_ids = yaml.safe_load(f)

    rows = {}
    for i, zrec in enumerate(zenodo_ids):

        # Enforce a short delay between requests to Zenodo
        if i:
            time.sleep(0.5)

        resp = requests.get(f"https://zenodo.org/api/records/{zrec['id']}")
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

        try:
            row["tags"] = zrec["tags"]
        except KeyError:
            pass

        fpath = path / f"{to_slug(row['title'])}.md"
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(write_fm({k: v for k, v in row.items() if k not in ("path",)}))
            f.write("\n")
            f.write(template)
        print(f"Wrote {fpath.name}")

    # Construct the navigation and build a tag index using file front matter. This
    # section should generally not be modified.
    fms = read_fms(BASEPATH)
    compute_urls(fms)
    index_tags(fms)
    build_nav(fms)
