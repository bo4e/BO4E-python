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
