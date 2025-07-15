"""Removes elements from local build that do not need to be committed"""

import re
from pathlib import Path

import yaml

from const import BASEPATH


if __name__ == "__main__":

    # Remove glossary includes. These are added automatically when the site is built.
    for path in BASEPATH.glob("**/*.md"):
        with open(path, encoding="utf-8") as f:
            content = f.read()
        content_ = content
        for match in re.findall(r"{% include glossary.*?%}", content):
            term = re.search("term=['\"](.*?)['\"]", match).group(1)
            namespace = re.search("namespace=['\"](.*?)['\"]", match).group(1)
            if namespace:
                term = f"{namespace}:{term}"
            content_ = content_.replace(match, term)
        if content_ != content:
            print(f"Removed glossary includes from {path}")
            with open(path, "w", encoding="utf-8") as f:
                f.write(content_)

    # Clear sourced values from glossary. These are added from a canonical source when
    # the site is built.
    sources = ["Darwin Core"]
    with open(BASEPATH / "_data" / "glossary.yml", encoding="utf-8") as f:
        glossary = [t for t in yaml.safe_load(f) if t.get("source") not in sources]

    with open(BASEPATH / "_data" / "glossary.yml", "w", encoding="utf-8") as f:
        yaml.safe_dump(glossary, f, sort_keys=False)
