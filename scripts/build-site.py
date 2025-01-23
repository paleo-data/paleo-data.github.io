import os
from pathlib import Path

BASEPATH = Path(os.environ["GITHUB_WORKSPACE"])
print(BASEPATH)
