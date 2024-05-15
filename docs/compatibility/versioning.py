"""
This module provides a CLI to check if a version tag has the expected format we expect in the BO4E repository.
"""

import functools
import logging
import re
import subprocess
import sys
from typing import ClassVar, Literal, Optional

import click
from bost.pull import get_source_repo
from github.GitRelease import GitRelease
from pydantic import BaseModel, ConfigDict

from .__main__ import compare_bo4e_versions

logger = logging.getLogger(__name__)


@functools.total_ordering
class Version(BaseModel):
    """
    A class to represent a BO4E version number.
    """

    version_pattern_with_rc: ClassVar[re.Pattern[str]] = re.compile(
        r"^v(?P<major>\d{6})\.(?P<functional>\d+)\.(?P<technical>\d+)(?:-rc(?P<candidate>\d+))?$"
    )
    version_pattern: ClassVar[re.Pattern[str]] = re.compile(
        r"^v(?P<major>\d{6})\.(?P<functional>\d+)\.(?P<technical>\d+)$"
    )

    major: int
    functional: int
    technical: int
    candidate: Optional[int] = None
    model_config = ConfigDict(frozen=True)

    @classmethod
    def from_string(cls, version: str, allow_candidate: bool = False) -> "Version":
        """
        Parse a version string and return a Version object.
        Raises a ValueError if the version string does not match the expected pattern.
        Raises a ValueError if allow_candidate is False and the version string contains a candidate version.
        """
        if allow_candidate:
            pattern = cls.version_pattern_with_rc
        else:
            pattern = cls.version_pattern
        match = pattern.fullmatch(version)
        if match is None:
            raise ValueError(f"Expected version to match {pattern}, got {version}")
        return cls(
            major=int(match.group("major")),
            functional=int(match.group("functional")),
            technical=int(match.group("technical")),
            candidate=int(match.group("candidate")) if allow_candidate else None,
        )

    @property
    def tag(self) -> str:
        """
        Return the tag name for this version.
        """
        return f"v{self.major}.{self.functional}.{self.technical}" + (
            f"-rc{self.candidate}" if self.is_candidate() else ""
        )

    def is_candidate(self) -> bool:
        """
        Return True if this version is a candidate version.
        """
        return self.candidate is not None

    def bumped_major(self, other: "Version") -> bool:
        """
        Return True if this version is a major bump from the other version.
        """
        return self.major > other.major

    def bumped_functional(self, other: "Version") -> bool:
        """
        Return True if this version is a functional bump from the other version.
        Return False if major bump is detected.
        """
        return not self.bumped_major(other) and self.functional > other.functional

    def bumped_technical(self, other: "Version") -> bool:
        """
        Return True if this version is a technical bump from the other version.
        Return False if major or functional bump is detected.
        """
        return not self.bumped_functional(other) and self.technical > other.technical

    def bumped_candidate(self, other: "Version") -> bool:
        """
        Return True if this version is a candidate bump from the other version.
        Return False if major, functional or technical bump is detected.
        Raises ValueError if one of the versions is not a candidate version.
        """
        if self.candidate is not None or other.candidate is not None:
            raise ValueError("Cannot compare candidate versions if one of them is not a candidate.")
        return not self.bumped_technical(other) and self.candidate > other.candidate

    def __gt__(self, other: "Version"):
        if not isinstance(other, Version):
            return NotImplemented
        return (
            self.major > other.major
            or self.functional > other.functional
            or self.technical > other.technical
            or (self.is_candidate() and (not other.is_candidate() or self.candidate > other.candidate))
        )

    def __eq__(self, other: "Version"):
        if not isinstance(other, Version):
            return NotImplemented
        return (
            self.major == other.major
            and self.functional == other.functional
            and self.technical == other.technical
            and self.is_candidate() == other.is_candidate()
            and (not self.is_candidate() or self.candidate == other.candidate)
        )

    def __str__(self):
        return self.tag


def get_latest_release(gh_token: str | None = None) -> GitRelease:
    """
    Get the release from BO4E-python repository which is marked as 'latest'.
    """
    repo = get_source_repo(gh_token)
    latest_release = repo.get_latest_release()
    # Ensure that the latest release is on main branch
    commit_id = subprocess.check_output(["git", "rev-parse", f"tags/{latest_release.tag_name}~0"]).decode().strip()
    output = subprocess.check_output(["git", "branch", "--contains", f"{commit_id}"]).decode()
    branches_containing_commit = [line.lstrip("*").strip() for line in output.splitlines()]
    if "main" not in branches_containing_commit:
        raise ValueError(
            f"Fatal Error: Latest release {latest_release.tag_name} is not on main branch "
            f"(branches {branches_containing_commit} contain commit {commit_id}).\n"
            f"Output from git-command: {output}"
        )
    return latest_release


def determine_commits_ahead_behind(cur_version: Version, base_version: Version) -> tuple[int, int]:
    """
    Compares the commits of the version tags cur_version...base_version
    Returns the number of commits ahead and behind the base_version as tuple.
    """
    expected_output_pattern = re.compile(r"^\s*(\d+)\s+(\d+)\s*$")
    output = subprocess.check_output(["git", "rev-list", "--left-right", "--count", f"{cur_version}...{base_version}"])
    match = expected_output_pattern.fullmatch(output.decode())
    if match is None:
        raise ValueError(f"Expected output to match {expected_output_pattern}, got {output}")
    return int(match.group(1)), int(match.group(2))


def check_version_consistent_with_commit_history(
    cur_version: Version, latest_version: Version
) -> Literal["behind", "ahead"]:
    """
    Check if the current version is consistent with the commit history.
    Returns "behind" if the current version is behind the latest version.
    Returns "ahead" if the current version is ahead of the latest version.
    """
    commits_ahead, commits_behind = determine_commits_ahead_behind(cur_version, latest_version)
    if commits_behind == 0:
        if cur_version < latest_version:
            raise ValueError(
                f"Current version is {commits_ahead} commits ahead and 0 commits behind the latest version "
                f"but version number has decreased. {cur_version} < {latest_version}"
            )
        return "ahead"
    # commits_behind > 0
    if cur_version > latest_version:
        raise ValueError(
            f"Current version is {commits_ahead} commits ahead and {commits_behind} commits behind the latest version "
            f"but version number has increased. {cur_version} > {latest_version}"
        )
    return "behind"


def compare_work_tree_with_latest_version(gh_version: str, gh_token: str | None = None):
    """
    Compare the work tree with the latest release from the BO4E repository.
    """
    logger.info("Github Access Token %s", "provided" if gh_token is not None else "not provided")
    new_version = Version.from_string(gh_version, allow_candidate=True)
    logger.info("Retrieving the latest release version")
    latest_release = get_latest_release(gh_token).tag_name
    latest_version = Version.from_string(latest_release, allow_candidate=False)

    if new_version == latest_version:
        logger.info("Version is equal to the latest version %s. Skipping further checks.", latest_version)
        return
    mode = check_version_consistent_with_commit_history(new_version, latest_version)
    if mode == "ahead":
        version_ahead = new_version
        version_behind = latest_version
    else:
        version_ahead = latest_version
        version_behind = new_version

    logger.info("Mode '%s': Comparing versions: %s -> %s", mode, version_behind, version_ahead)
    if version_ahead.bumped_major(version_behind):
        logger.info("Major version bump detected. No further checks needed.")
        return
    logger.info("Comparing versions iteratively: %s -> %s", version_behind, version_ahead)
    changes = list(compare_bo4e_versions(version_behind.tag, version_ahead.tag, gh_token=gh_token, from_local=True))
    logger.info("Check if functional or technical release bump is needed")
    functional_changes = any(changes)
    logger.info("%s release bump is needed", "Functional" if functional_changes else "Technical")

    if not functional_changes and version_ahead.bumped_functional(version_behind):
        raise ValueError(
            "Functional version bump detected but no functional changes found. "
            "Please bump the technical release count instead of the functional."
        )
    if functional_changes and not version_ahead.bumped_functional(version_behind):
        raise ValueError(
            "No functional version bump detected but functional changes found. "
            "Please bump the functional release count."
        )


@click.command()
@click.option("--gh-version", type=str, required=True, help="The new version to compare the latest release with.")
@click.option(
    "--gh-token", type=str, default=None, help="GitHub Access token. This helps to avoid rate limiting errors."
)
def compare_work_tree_with_latest_version_cli(gh_version: str, gh_token: str | None = None):
    """
    Check a version tag and compare the work tree with the latest release from the BO4E repository.
    Exits with status code 1 iff the version is inconsistent with the commit history or if the detected changes in
    the JSON-schemas are inconsistent with the version bump.
    """
    try:
        compare_work_tree_with_latest_version(gh_version, gh_token)
    except Exception as error:
        logger.error("An error occurred.", exc_info=error)
        raise click.exceptions.Exit(1)
    logger.info("All checks passed.")


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    compare_work_tree_with_latest_version_cli()


def test_compare_work_tree_with_latest_version():
    logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
    compare_work_tree_with_latest_version("v202401.1.2-rc3", gh_token=None)
