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

print(f" BASEPATH: {BASEPATH}")
print(f" IS_GITHUB: {IS_GITHUB}")

# Read list of valid tags
with open(BASEPATH / "_data" / "topics.yml", encoding="utf-8") as f:
    TAGS = yaml.safe_load(f)

GLOSSARY = {}
for _path in (BASEPATH / "_data" / "glossaries").glob("*.yml"):
    try:
        with open(_path, encoding="utf-8") as f:
            GLOSSARY.update(
                {
                    (t.get("namespace", "") + ":" + t["term"].lower()).lstrip(":"): t
                    for t in yaml.safe_load(f)
                }
            )
    except TypeError:
        pass
