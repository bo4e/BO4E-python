"""
Version information for the bo4e package.
"""

import re
from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("bo4e")
    # Please keep this name in sync with the name of the project in pyproject.toml
    # This name is the name of the package on pypi.org
except PackageNotFoundError:
    __version__ = "0.0.0"


def _parse_version_to_gh_version(version_str: str) -> str:
    """
    Parse a version string into a GitHub version string.
    E.g. '202401.0.1-rc8+dev12asdf34' becomes 'v202401.0.1-rc8'.
    """
    _regex_version = re.compile(
        r"^(?P<major>\d{6})\."
        r"(?P<functional>\d+)\."
        r"(?P<technical>\d+)"
        r"(?:rc(?P<candidate>\d*))?"
        r"(?:\+g(?P<commit_part>\w+)"
        r"(?:\.d(?P<dirty_workdir_date_year>\d{4})"
        r"(?P<dirty_workdir_date_month>\d{2})"
        r"(?P<dirty_workdir_date_day>\d{2}))?)?$"
    )
    match = _regex_version.match(version_str)
    if match is None:
        raise ValueError(f"Invalid version string: {version_str}")

    return (
        f"v{match.group('major')}.{match.group('functional')}.{match.group('technical')}"
        + (f"-rc{match.group('candidate')}" if match.group("candidate") else "")
        + (f"+g{match.group('commit_part')}" if match.group("commit_part") else "")
        + (
            f".d{match.group('dirty_workdir_date_year')}"
            f"{match.group('dirty_workdir_date_month')}"
            f"{match.group('dirty_workdir_date_day')}"
            if match.group("dirty_workdir_date_year")
            else ""
        )
    )


__gh_version__ = _parse_version_to_gh_version(__version__)
