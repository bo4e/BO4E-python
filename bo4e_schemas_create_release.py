from typing import Any

import click
import requests


def ensure_status_code(response: requests.Response) -> None:
    """
    Ensure that the response status code is 2xx
    """
    if not response.ok:
        raise requests.HTTPError(
            f"Request failed with status code {response.status_code}\n"
            f"response-body: {response.json()}\n"
            f"request: {response.request.body}"
        )


def get_release_infos(github_token: str, version: str) -> dict[str, str]:
    """
    Get the release infos from the github api
    """
    response = requests.get(
        f"https://api.github.com/repos/BO4E/BO4E-Python/releases/tags/{version}",
        headers={"Authorization": f"token {github_token}", "Accept": "application/vnd.github.v3+json"},
    )
    ensure_status_code(response)
    return response.json()


def get_latest_release_tag(github_token: str) -> str:
    """
    Get the latest release from the github api
    """
    response = requests.get(
        "https://api.github.com/repos/BO4E/BO4E-Python/releases/latest",
        headers={"Authorization": f"token {github_token}", "Accept": "application/vnd.github.v3+json"},
    )
    ensure_status_code(response)
    return response.json()["tag_name"]


def get_commit_sha(
    github_token: str,
) -> str:
    """
    Get the latest commit sha from the github api
    """
    response = requests.get(
        "https://api.github.com/repos/Hochfrequenz/BO4E-Schemas/git/refs/heads/main",
        headers={"Authorization": f"token {github_token}", "Accept": "application/vnd.github.v3+json"},
    )
    ensure_status_code(response)
    return response.json()["object"]["sha"]


def create_release(
    github_token: str, version: str, commit_sha: str, release_infos: dict[str, Any], is_latest: bool
) -> None:
    """
    Create a release in the github api
    """
    response = requests.post(
        "https://api.github.com/repos/Hochfrequenz/BO4E-Schemas/releases",
        headers={"Authorization": f"token {github_token}", "Accept": "application/vnd.github.v3+json"},
        json={
            "tag_name": version,
            "target_commitish": commit_sha,
            "name": release_infos["name"],
            "body": release_infos["body"],
            "draft": False,
            "prerelease": release_infos["prerelease"],
            "make_latest": str(is_latest),
        },
    )
    ensure_status_code(response)
    return response.json()


@click.command()
@click.option(
    "--github-token",
    "-t",
    help="the github token to use for the release workflow",
    required=True,
    envvar="GITHUB_TOKEN",
    type=click.STRING,
)
@click.option(
    "--version",
    "-v",
    help="the tagged version known inside the release workflow",
    required=True,
    type=click.STRING,
    envvar="VERSION",
)
def main(github_token: str, version: str):
    """create a release in the BO4E-Schemas repository"""
    release_infos = get_release_infos(github_token, version)
    commit_sha = get_commit_sha(github_token)
    is_latest = version == get_latest_release_tag(github_token)
    create_release(github_token, version, commit_sha, release_infos, is_latest)


if __name__ == "__main__":
    main()
