import pytest

from bo4e import Gueltigkeitstyp, Regionskriterium, Regionskriteriumtyp
from tests.serialization_helper import assert_serialization_roundtrip


class TestRegionskriterium:
    @pytest.mark.parametrize(
        "regionskriterium",
        [
            pytest.param(
                Regionskriterium(
                    regionskriteriumtyp=Regionskriteriumtyp.REGELGEBIET_NAME,
                    gueltigkeitstyp=Gueltigkeitstyp.NICHT_IN,
                    wert="Was ist ein Regionskriterium?",
                ),
            ),
        ],
    )
    def test_regionskriterium_serialization_roundtrip(self, regionskriterium: Regionskriterium) -> None:
        """
        Test de-/serialisation of Regionskriterium with minimal attributes.
        """
        assert_serialization_roundtrip(regionskriterium)
