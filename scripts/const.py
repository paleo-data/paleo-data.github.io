"""Define site-specific constants"""

print("Setting constants")

import os
from pathlib import Path

# The site root. Do not modify.
try:
    BASEPATH = Path(os.environ["GITHUB_WORKSPACE"])
except KeyError:
    BASEPATH = Path("..")

print(BASEPATH)

# Set of valid tags
VALID_TAGS = {"symbiota"}
