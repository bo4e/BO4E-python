#!/bin/bash

# Get tag information in BO4E-Python by SHA

if ! tag_infos=$(curl --fail -L \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/BO4E/BO4E-Python/git/tags/$TAG_SHA); then

  echo "Tag not found in BO4E-Python: $($tag_infos | jq -r .message)"
  exit 1
fi

# Get release information in BO4E-Python by tag name (VERSION)

if ! release_infos=$(curl --fail -L \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/BO4E/BO4E-Python/releases/tags/$VERSION); then

  echo "Release not found in BO4E-Python: $($release_infos | jq -r .message)"
  exit 1
fi

# Somehow the release information does not contain the information if it is the latest release. Therefore, we have to
# get the latest release and compare the tag names.

if ! latest_release_infos=$(curl --fail -L \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/BO4E/BO4E-Python/releases/latest); then

  echo "Latest release not found in BO4E-Python: $($release_infos | jq -r .message)"
  echo "This is not a problem, but the release will not be marked as latest."
  IS_LATEST=false
else
  IS_LATEST=$(echo "$latest_release_infos" | jq -r ".tag_name == \"$VERSION\"")
fi

# Get commit SHA in BO4E-Schemas by branch name

if ! commit_infos=$(curl --fail -s -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/Hochfrequenz/BO4E-Schemas/git/refs/heads/main); then

  echo "Commit not found in BO4E-Schemas: $($commit_infos | jq -r .message)"
  exit 1
fi
COMMIT_SHA=$(echo "$commit_infos" | jq -r ".object.sha")

echo "Commit SHA: $COMMIT_SHA"

# Create annotated tag in BO4E-Schemas (only together with the lightweight tag the tag will be visible in the UI)

if ! annotated_tag=$(curl --fail -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/Hochfrequenz/BO4E-Schemas/git/tags \
  -d '{
    "tag": "'$VERSION'",
    "object": "'$COMMIT_SHA'",
    "message": "'"$(echo "$tag_infos" | jq -r ".message")"'",
    "type": "commit",
    "tagger": {
      "name": "'"$(echo "$tag_infos" | jq -r ".tagger.name")"'
      "email": "'"$(echo "$tag_infos" | jq -r ".tagger.email")"'",
      "date": "'"$(echo "$tag_infos" | jq -r ".tagger.date")"'"
    }
  }'); then

  echo "Annotated tag not created in BO4E-Schemas: $($annotated_tag | jq -r .message)"
  exit 1
fi

echo "Step 1 response: annotated_tag"

# Create a lightweight tag in BO4E-Schemas

if ! lightweight_tag=$(curl --fail -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/Hochfrequenz/BO4E-Schemas/git/refs \
  -d '{
    "ref": "refs/tags/'$VERSION'",
    "sha": "'$(echo $annotated_tag | jq -r ".sha")'"
  }'); then

  echo "Lightweight tag not created in BO4E-Schemas: $($lightweight_tag | jq -r .message)"
  exit 1
fi

echo "Step 2 response: $step2_response"

# Create a release in BO4E-Schemas

if ! release=$(curl --fail -X POST \
  -H "Authorization: token $GITHUB_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/Hochfrequenz/BO4E-Schemas/releases \
  -d '{
    "tag_name": "'$VERSION'",
    "name": "'$(echo $release_infos | jq -r ".name")'",
    "body": "'$(echo $release_infos | jq -r ".body")'",
    "draft": false,
    "prerelease": '$(echo $release_infos | jq -r ".prerelease")',
    "make_latest": "'$IS_LATEST'"
  }'); then

  echo "Release not created in BO4E-Schemas: $($release | jq -r .message)"
  exit 1
fi
