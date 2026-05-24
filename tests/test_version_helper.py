"""Tests for the inline Version helper in generate_or_validate_json_schemas."""

import pytest

from generate_or_validate_json_schemas import Version


class TestVersionFromStr:
    def test_clean_release(self) -> None:
        v = Version.from_str("v202401.0.1")
        assert v.major == 202401
        assert v.functional == 0
        assert v.technical == 1
        assert v.candidate is None
        assert v.commit is None
        assert v.date is None

    def test_release_candidate(self) -> None:
        v = Version.from_str("v202401.5.0-rc3")
        assert v.candidate == 3

    def test_release_candidate_empty_number(self) -> None:
        # bo4e-cli's regex permits 'rc' followed by zero digits.
        v = Version.from_str("v202401.0.0-rc")
        assert v.candidate is None  # empty match -> falsy -> None

    def test_dirty_with_commit(self) -> None:
        v = Version.from_str("v202401.0.1+gabc1234")
        assert v.commit == "abc1234"
        assert v.date is None

    def test_dirty_with_date(self) -> None:
        v = Version.from_str("v202401.0.1.d20240315")
        assert v.commit is None
        assert v.date == "20240315"

    def test_dirty_with_commit_and_date(self) -> None:
        v = Version.from_str("v202401.0.1+gabc1234.d20240315")
        assert v.commit == "abc1234"
        assert v.date == "20240315"

    def test_invalid_raises(self) -> None:
        with pytest.raises(ValueError, match="Invalid version"):
            Version.from_str("not-a-version")

    def test_missing_v_prefix_raises(self) -> None:
        with pytest.raises(ValueError):
            Version.from_str("202401.0.1")


class TestVersionStr:
    def test_clean_roundtrip(self) -> None:
        assert str(Version.from_str("v202401.0.1")) == "v202401.0.1"

    def test_rc_roundtrip(self) -> None:
        assert str(Version.from_str("v202401.5.0-rc3")) == "v202401.5.0-rc3"

    def test_dirty_with_commit_roundtrip(self) -> None:
        s = "v202401.0.1+gabc1234"
        assert str(Version.from_str(s)) == s

    def test_dirty_full_roundtrip(self) -> None:
        s = "v202401.0.1-rc1+gabc1234.d20240315"
        assert str(Version.from_str(s)) == s

    def test_major_zero_padded(self) -> None:
        v = Version(major=202401, functional=0, technical=0)
        assert str(v) == "v202401.0.0"
