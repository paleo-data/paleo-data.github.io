"""Define site-specific constants"""

print("Setting constants")

import os
from pathlib import Path

# The site root. Do not modify.
try:
    BASEPATH = Path(os.environ["GITHUB_WORKSPACE"])
except KeyError:
    BASEPATH = Path("..")

print(f"Basepath: {BASEPATH}")

# Read list of valid tags
with open(f"../_data/topics.txt") as f:
    VALID_TAGS = set(f.read().splitlines())
