import pytest

from bo4e import Gueltigkeitstyp, KriteriumWert, RegionaleGueltigkeit, Tarifregionskriterium
from tests.serialization_helper import assert_serialization_roundtrip


class TestRegionaleGueltigkeit:
    @pytest.mark.parametrize(
        "regionalegueltigkeit",
        [
            pytest.param(
                RegionaleGueltigkeit(
                    gueltigkeitstyp=Gueltigkeitstyp.NUR_IN,
                    kriteriums_werte=[
                        KriteriumWert(
                            kriterium=Tarifregionskriterium.NETZ_NUMMER,
                            wert="12345",
                        ),
                    ],
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_regionalegueltigkeit_serialization_roundtrip(self, regionalegueltigkeit: RegionaleGueltigkeit) -> None:
        """
        Test de-/serialisation of RegionaleGueltigkeit with minimal attributes.
        """
        assert_serialization_roundtrip(regionalegueltigkeit)
