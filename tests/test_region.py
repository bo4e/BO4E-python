import pytest  # type:ignore[import]

from bo4e.bo.region import Region, RegionSchema
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_regionskriterium import example_regionskriterium  # type:ignore[import]


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
    def test_serialization_roundtrip(self, region: Region):
        assert_serialization_roundtrip(region, RegionSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Region()

        assert "missing 2 required" in str(excinfo.value)

    def test_region_positiv_liste_required_and_negativ_liste_not_required(self):
        with pytest.raises(ValueError) as excinfo:
            _ = Region(
                bezeichnung="Bikini Bottom",
                positiv_liste=[],
                negativ_liste=[],
            )

        assert "List positiv_liste must not be empty." in str(excinfo.value)
