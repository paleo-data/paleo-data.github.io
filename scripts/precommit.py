"""Removes elements from local build that do not need to be committed"""

import re
from pathlib import Path

import yaml

try:
    import requests_cache
except ModuleNotFoundError:
    pass

from const import BASEPATH
from utils import add_dwc_terms


if __name__ == "__main__":

    # Use cache when building the site locally. Cached requests expire after 8 hrs.
    try:
        session = requests_cache.CachedSession(expire_after=28800)
    except NameError:
        session = requests.Session()

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

    # Update glossary
    add_dwc_terms(session)
