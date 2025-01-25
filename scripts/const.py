"""Define site-specific constants"""

import os
from pathlib import Path

# The site root. Do not modify.
try:
    BASEPATH = Path(os.environ["GITHUB_WORKSPACE"])
except KeyError:
    BASEPATH = Path("..")

# Set of valid tags
VALID_TAGS = {"test"}
