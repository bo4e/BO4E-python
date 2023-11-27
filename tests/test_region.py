import pytest

from bo4e import Region, Regionskriterium
from tests.serialization_helper import assert_serialization_roundtrip


class TestRegion:
    @pytest.mark.parametrize(
        "region",
        [
            pytest.param(
                Region(
                    bezeichnung="Bikini Bottom",
                    positiv_liste=[Regionskriterium()],
                    negativ_liste=[Regionskriterium()],
                ),
                id="max attributes",
            ),
            pytest.param(Region(bezeichnung="Bikini Bottom", positiv_liste=[Regionskriterium()]), id="min attributes"),
        ],
    )
    def test_serialization_roundtrip(self, region: Region) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(region)
