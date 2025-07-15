print("Loading utils")

import io
import re
from pathlib import Path

import pandas as pd
import yaml
from unidecode import unidecode

from const import BASEPATH, GLOSSARY, IS_GITHUB, VALID_TAGS


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
    while path != path.parent:
        segments.insert(0, path.name)
        path = path.parent
    segments.insert(0, str(path))
    return segments


def read_fm(path: Path) -> dict:
    """Parses the Jekyll front matter in a markdown file"""
    with open(path, encoding="utf-8") as f:
        try:
            return yaml.safe_load(f.read().lstrip("---").split("---")[0])
        except Exception as exc:
            raise ValueError(path) from exc


def read_fms(path: Path) -> dict:
    """Read page front_matters, omitting the vendor directory used by GitHub actions"""
    fms = {}
    for path in path.glob("**/*.md"):
        if "vendor" not in split_path(path) and path.name != "README.md":
            fm = read_fm(path)
            fm["path"] = path
            fms[fm["title"]] = fm
    return fms


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


def write_fm(fm: dict) -> str:
    """Writes Jekyll front matter to a markdown file"""
    return "\n".join(["---", yaml.dump(fm, sort_keys=False).rstrip(), "---", ""])


def compute_urls(fms: dict) -> dict:
    """Computes the root-relative URL to a page in the Jekyll site

    These URLs can be used in anchors in Jekyll page templates. They must be
    accompanied by the relative_url filter.
    """
    for _, fm in fms.items():

        key = None
        segments = split_path(fm["path"])

        # Collections get their own sidebar
        if "collections" in segments:
            path = segments[segments.index("collections") + 1 :]
            path[0] = path[0].lstrip("_")
            path[-1] = Path(path[-1]).stem
            key = path[0]
            heading = path[-2]

        # Build paths to non-collection content using the parent attribute
        else:
            path = [fm["path"].stem]
            if path[0] == "index":
                path.insert(0, to_slug(fm["title"]))

            try:
                parent = fms[fm["parent"]]
            except KeyError:
                parent = None

            while parent:
                path.insert(0, to_slug(parent["title"]))
                try:
                    parent = fms[fms["parent"]]
                except KeyError:
                    break

            # Omit site index
            if len(path) == 2 and path[-1] == "index":
                path = path[1:]

            # Omit index
            if path[-1] == "index":
                path = path[:-1]

            # Include direct descendants of home in the main navigation
            heading = None
            if len(path) == 1:
                key = "main"

        # Add navigation info to fm
        fm["key"] = key
        fm["heading"] = heading
        fm["url"] = "/" + "/".join(path)

        # NOTE: If internal links need to be converted to use the link tag (for
        # example, to take advantage of the link checking ability of that tag),
        # use the full path to the original file, including extension and excluding
        # the collections folder for items on that path.

    return fms


def index_tags(fms: dict, key: str = "tags") -> dict:
    """Indexes front matter tags"""

    tagged = []

    # Get tags from front matter of pages
    for fm in fms.values():
        tags = fm.get(key, [])
        if tags:
            if not isinstance(tags, list):
                tags = [tags]
            invalid = set(tags) - VALID_TAGS
            if invalid:
                print(f"Invalid tags omitted: {invalid} (url={fm['url']})")
                tags = sorted(set(tags) & VALID_TAGS)
            tagged.append(
                {
                    "title": fm["title"],
                    "kind": "page",
                    "url": fm["url"],
                    "tags": tags,
                }
            )

    # Get tags from resources
    for path in (BASEPATH / "_data" / "resources-updated").glob("*.yml"):
        with open(path, encoding="utf-8") as f:
            resource = yaml.safe_load(f)
            resource["kind"] = "external"
            resource["url"] = resource["access_url"]
            resource["tags"] = resource[key]
            tagged.append(
                {
                    k: v
                    for k, v in resource.items()
                    if k in {"title", "kind", "url", "tags"}
                }
            )

    # Get tags from happy hours
    with open(BASEPATH / "_data" / "pdwg-happy-hours.yml", encoding="utf-8") as f:
        for event in yaml.safe_load(f):
            event["url"] = f"/community/pdwg-happy-hours#{event['date']}"
            event["kind"] = "PDWG happy hour"
            event["tags"] = event.get(key, [])
            tagged.append(
                {
                    k: v
                    for k, v in event.items()
                    if k in {"title", "kind", "url", "tags"}
                }
            )

    tagged.sort(key=lambda t: t["title"])
    with open(BASEPATH / "_data" / f"{key}.yml", "w", encoding="utf-8") as f:
        yaml.safe_dump(tagged, f)

    """
    # Create tag collection
    path = BASEPATH / "collections" / f"_{key}"
    path.mkdir(parents=True, exist_ok=True)

    with open(path / "index.md", "w") as f:
        f.write(write_fm({"title": "Topics"}))

    with open(BASEPATH / "templates" / "pages" / "tag", encoding="utf-8") as f:
        template = f.read()

    for tag, pages in tags.items():
        fpath = path / f"{to_slug(tag)}.md"
        with open(fpath, "w", encoding="utf-8") as f:
            f.write(write_fm({"title": tag, "pages": pages}))
            f.write("\n")
            f.write(template)
        print(f"Wrote {fpath.name}")
        fms[tag] = {
            "key": key,
            "heading": key,
            "title": tag,
            "url": f"/{key}/{to_slug(tag)}",
        }
    """

    return tags


def build_nav(
    fms: dict,
    headers: dict = None,
    include_main: list = None,
    exclude_main: list = None,
) -> None:
    """Builds a navigation sidebar"""
    if headers is None:
        headers = {}

    nav = {}

    # Order front matter based on top-level pages
    parents = {}
    for title, fm in fms.items():
        if fm["path"]:
            parents.setdefault(fm["path"].parent, []).append(fm)
    main = parents[sorted(parents, key=lambda p: len(str(p)))[0]]
    main.sort(key=lambda p: p.get("nav_order", 100000))

    for fm in main:
        if fm["path"].name not in {"index.md", "test.md"}:
            if (
                not (include_main or exclude_main)
                or (include_main and fm["path"].name in include_main)
                or (exclude_main and fm["path"].name not in exclude_main)
            ):
                nav.setdefault("main", []).append(
                    {"title": fm["title"], "url": fm["url"]}
                )
            nav.setdefault("sidebar", []).append(
                {"title": fm["title"], "url": fm["url"]}
            )

    fms = dict(
        sorted(
            fms.items(),
            key=lambda kv: (kv[1].get("nav_order", 100), kv[1]["title"].lower()),
        )
    )
    for title, fm in fms.items():
        if not fm.get("nav_exclude") and fm["key"] and fm["heading"]:

            try:
                heading = headers[fm["heading"]]
            except KeyError:
                heading = " ".join(fm["heading"].split("-")).title()

            group = [g for g in nav.get("sidebar", []) if g["title"] == heading][0]
            group.setdefault("children", []).append({"title": title, "url": fm["url"]})

    fpath = BASEPATH / "_data" / "navigation.yml"
    with open(fpath, "w", encoding="utf-8") as f:
        yaml.dump(nav, f, sort_keys=False)


def add_tooltips(path, glossary=None, exclude=(".github", "README.md", "vendor")):
    """Adds definitions as tooltips"""

    if glossary is None:
        glossary = GLOSSARY

    # Build pattern to find elements that should not inclide tooltips
    subpatterns = (
        r"#.*?\n",  # markdown headers
        r"\[.*?\]\(.*?\)",  # markdown links
        r"{%.*?%}",  # Jekyll includes
    )
    pattern = f"({'|'.join(subpatterns)})"

    for path in path.glob("**/*.md"):

        # This function modifies the markdown files. The modified files should not
        # be committed, so it only runs on test.md if run locally.
        if not IS_GITHUB and path.name != "test.md":
            continue

        # Skip files including any of the exclude keywords
        if any((s in str(path) for s in exclude)):
            continue

        # Create a copy of the glossary. Terms are removed as they are found so that
        # only the first occurrence in each document has the tooltip.
        glossary_ = glossary.copy()

        with open(path, encoding="utf-8") as f:
            try:
                _, fm, content = f.read().split("---", 2)
            except Exception as exc:
                raise ValueError(f"No YAML header: {path}") from exc
            parts = re.split(pattern, content)
            for i, part in enumerate(parts):
                if not re.match(pattern, part):
                    for key in list(glossary_):
                        # Find the first match for the term in the part
                        match = re.search(rf"\b{key}\b", part, flags=re.I)
                        if match is not None:
                            # Use the matched term so that case is preserved
                            term = match.group()
                            try:
                                namespace, term = term.split(":")
                            except ValueError:
                                namespace = ""
                            include = f'{{% include glossary term="{term}" namespace="{namespace}" %}}'
                            parts[i] = re.sub(
                                rf"\b{match.group()}\b", include, parts[i], 1
                            )
                            del glossary_[key]
            content_ = "---" + fm + "---" + "".join(parts)

        # Do not mess with the file unless it has been changed
        if content != content_:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content_)


def add_dwc_terms(session):
    """Updates the glossary with terms from Darwin Core"""

    def assign_namespace(val):
        if "dwc/terms" in val:
            return "dwc"
        elif "dwc/iri" in val:
            return "dwciri"
        elif "dublincore" in val:
            return "dc"
        else:
            raise ValueError(f"Unknown namespace: {val}")

    source = "Darwin Core"
    url = "https://raw.githubusercontent.com/tdwg/dwc/refs/heads/master/vocabulary/term_versions.csv"
    resp = session.get(url)
    df = pd.read_csv(io.StringIO(resp.text))

    # Restrict to recommended terms
    df = df[df["status"] == "recommended"]

    # Assign namespaces based on IRI
    df["namespace"] = df["iri"].apply(assign_namespace)

    glossary = [t for t in GLOSSARY.values() if t.get("source") != source]
    for _, row in df.iterrows():
        term = row["term_localName"]
        glossary.append(
            {
                "term": term,
                "definition": row["definition"],
                "namespace": row["namespace"],
                "source": source,
                "url": f"https://dwc.tdwg.org/terms/#dwc:{term}",
            }
        )
    glossary.sort(key=lambda t: t["term"])

    with open(BASEPATH / "_data" / "glossary.yml", "w", encoding="utf-8") as f:
        yaml.safe_dump(glossary, f, sort_keys=False)

    return {
        (t.get("namespace", "") + ":" + t["term"].lower()).lstrip(":"): t
        for t in glossary
    }
