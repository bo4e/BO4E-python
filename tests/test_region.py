import pytest
from pydantic import ValidationError

from bo4e.bo.region import Region
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_regionskriterium import example_regionskriterium


class TestRegion:
    @pytest.mark.parametrize(
        "region",
        [
            pytest.param(
                Region(
                    bezeichnung="Bikini Bottom",
                    positiv_liste=[example_regionskriterium],
                    negativ_liste=[example_regionskriterium],
                ),
                id="max attributes",
            ),
            pytest.param(
                Region(bezeichnung="Bikini Bottom", positiv_liste=[example_regionskriterium]), id="min attributes"
            ),
        ],
    )
    def test_serialization_roundtrip(self, region: Region) -> None:
        assert_serialization_roundtrip(region)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Region()  # type: ignore[call-arg]

        assert "2 validation errors" in str(excinfo.value)

    def test_region_positiv_liste_required_and_negativ_liste_not_required(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Region(
                bezeichnung="Bikini Bottom",
                positiv_liste=[],
                negativ_liste=[],
            )

        assert "1 validation error" in str(excinfo.value)
        assert "too_short" in str(excinfo.value)
