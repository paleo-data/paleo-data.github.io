"""Define site-specific constants"""

print("Setting constants")

import os
from pathlib import Path

import yaml

# The site root. Do not modify.
try:
    BASEPATH = Path(os.environ["GITHUB_WORKSPACE"])
    IS_GITHUB = True
except KeyError:
    BASEPATH = Path("..")
    IS_GITHUB = False

print(f"Basepath: {BASEPATH}")

# Read list of valid tags
with open(BASEPATH / "_data" / "topics.txt") as f:
    VALID_TAGS = set(f.read().splitlines())

with open(BASEPATH / "_data" / "glossary.yml", encoding="utf-8") as f:

    try:
        GLOSSARY = {
            (t.get("namespace", "") + ":" + t["term"].lower()).lstrip(":"): t
            for t in yaml.safe_load(f)
        }
    except TypeError:
        GLOSSARY = {}
