#!/bin/bash

#echo "GITHUB_TOKEN: $GITHUB_TOKEN"
#echo "VERSION: $VERSION"

# Get release information in BO4E-Python by tag name (VERSION)

if ! release_infos=$(curl --fail -L \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  "https://api.github.com/repos/BO4E/BO4E-Python/releases/tags/$VERSION"); then

  echo "Release not found in BO4E-Python: $($release_infos | jq -r .message)"
  exit 1
fi

# Somehow the release information does not contain the information if it is the latest release. Therefore, we have to
# get the latest release and compare the tag names.

if ! latest_release_infos=$(curl --fail -L \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  "https://api.github.com/repos/BO4E/BO4E-Python/releases/latest"); then

  echo "Latest release not found in BO4E-Python: $($release_infos | jq -r .message)"
  echo "This is not a problem, but the release will not be marked as latest."
  IS_LATEST=false
else
  IS_LATEST=$(echo "$latest_release_infos" | jq -r ".tag_name == \"$VERSION\"")
fi

# Get commit SHA in BO4E-Schemas by branch name

if ! commit_infos=$(curl --fail -s -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/repos/Hochfrequenz/BO4E-Schemas/git/refs/heads/main"); then

  echo "Commit not found in BO4E-Schemas: $($commit_infos | jq -r .message)"
  exit 1
fi
COMMIT_SHA=$(echo "$commit_infos" | jq -r ".object.sha")

echo "Commit SHA: $COMMIT_SHA"

# Create release in BO4E-Schemas

if ! release=$(curl --fail -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  "https://api.github.com/repos/Hochfrequenz/BO4E-Schemas/releases" \
  -d '{
    "tag_name": "'$VERSION'",
    "name": '$(echo $release_infos | jq ".name")',
    "body": '"$(echo $release_infos | jq ".body")"',
    "draft": false,
    "prerelease": '$(echo $release_infos | jq -r ".prerelease")',
    "make_latest": "'$IS_LATEST'",
    "target_commitish": "'$COMMIT_SHA'"
  }'); then

  echo "Release not created in BO4E-Schemas: $($release | jq -r .message)"
  exit 1
fi
