import pytest
from pydantic import ValidationError

from bo4e import Region
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

    def test_region_id(self) -> None:
        region = Region(
            bezeichnung="Bikini Bottom",
            id="foo",
            positiv_liste=[example_regionskriterium],
            negativ_liste=[example_regionskriterium],
        )
        region_dict = region.model_dump(by_alias=True)
        assert "_id" in region_dict
        assert Region.model_validate(region_dict) == region
