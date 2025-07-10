"""Creates and indexes pages based using YAML files in _data"""

import re
import shutil
from pathlib import Path

import html5lib
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

    # Update resources from Zenodo
    res_path = Path(BASEPATH / "_data" / "resources")
    upd_path = Path(BASEPATH / "_data" / "resources-updated")
    for path in [res_path, upd_path]:
        path.mkdir(parents=True, exist_ok=True)

    print("Updating resources")
    for path_ in res_path.glob("*.yml"):

        with open(path_, encoding="utf-8") as f:
            rec = yaml.safe_load(f.read())

        # Fill in Zenodo records
        doi = rec.get("doi")
        match = re.search(r"https?://doi.org/10.5281/zenodo.(\d+)$", doi if doi else "")
        if match:
            resp = requests.get(f"https://zenodo.org/api/records/{match.group(1)}")
            zrec = resp.json()
            metadata = zrec["metadata"]
            desc = BeautifulSoup(metadata["description"], "html5lib")

            # The value in path is used in a link tag, which expects the location of
            # the file in the _site directory. Note that those paths omit the
            # collections directory (defined in collections_dir in the config file).
            row = {
                "title": metadata["title"],
                "creators": "; ".join([p["name"] for p in metadata["creators"]]),
                "description": autolink(re.sub("\n{2,}", "\n\n", desc.text)),
                "resource_url": zrec["doi_url"],
                "path": f"_resources/{to_slug(metadata['title'])}.md",
                "nav_order": 1,
            }

            # Migrate custom keys from the original record
            for key, val in rec.items():
                if key not in row:
                    row[key] = val
            if not row.get("access_url"):
                row["access_url"] = row["resource_url"]

            with open(upd_path / path_.name, "w", encoding="utf-8") as f:
                yaml.safe_dump(row, f)
            print(f" Updated {path_.name}")

        else:
            # Copy non-Zenodo records as they are
            shutil.copy2(path_, upd_path)
            print(f" Copied {path_.name}")

    # Construct the navigation and build a tag index using file front matter. This
    # section should generally not be modified.

    print("Reading front matter")
    fms = read_fms(BASEPATH)

    print("Determining URLs")
    compute_urls(fms)

    print("Indexing tags")
    index_tags(fms, "topics")

    print("Building navigation")
    build_nav(fms, include_main=["topics.md"])
