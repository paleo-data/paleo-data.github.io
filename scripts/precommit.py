"""Removes elements from local build that should not be committed"""

import re

try:
    import requests_cache
except ModuleNotFoundError:
    import requests

from const import BASEPATH
from utils import add_dwc_terms, autodate


if __name__ == "__main__":

    # Use cache when building the site locally. Cached requests expire after 1 week.
    try:
        session = requests_cache.CachedSession(expire_after=60 * 60 * 24 * 7)
    except NameError:
        session = requests.Session()

    # Remove glossary includes. These are added automatically when the site is built.
    print("Removing glossary includes")
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
            print(f" {path}: Removed glossary includes")
            with open(path, "w", encoding="utf-8") as f:
                f.write(content_)

    # Add update date
    # for path in BASEPATH.glob("*.md"):
    #    if path.name != "README.md":
    #        autodate(path)
    # for path in (BASEPATH / "collections").glob("**/*.md"):
    #    autodate(path)

    # Update glossary
    add_dwc_terms(session)
