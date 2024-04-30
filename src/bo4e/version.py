"""
Version information for the bo4e package.
"""

import re
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("bo4e")
except PackageNotFoundError:
    __version__ = "0.0.0"
# Please keep this name in sync with the name of the project in pyproject.toml
# This name is the name of the package on pypi.org
if re.match(r"^(\d+\.\d+\.\d+)(rc\d+)?$", __version__):

    def _repl(match: re.Match[str]) -> str:
        if match.group(2) is not None:
            return f"v{match.group(1)}-{match.group(2)}"
        return f"v{match.group(1)}"

    __gh_version__ = re.sub(r"^(\d+\.\d+\.\d+)(rc\d+)?$", _repl, __version__)
else:
    __gh_version__ = f"v{__version__}"
