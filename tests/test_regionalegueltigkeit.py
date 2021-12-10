import pytest  # type:ignore[import]

from bo4e.com.kriteriumwert import KriteriumWert
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit, RegionaleGueltigkeitSchema
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp
from bo4e.enum.tarifregionskriterium import Tarifregionskriterium
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestRegionaleGueltigkeit:
    @pytest.mark.parametrize(
        "regionalegueltigkeit, expected_json_dict",
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
                {
                    "gueltigkeitstyp": "NUR_IN",
                    "kriteriumsWerte": [
                        {
                            "kriterium": "NETZ_NUMMER",
                            "wert": "12345",
                        }
                    ],
                },
                id="only required attributes",
            ),
        ],
    )
    def test_regionalegueltigkeit_serialization_roundtrip(self, regionalegueltigkeit, expected_json_dict):
        """
        Test de-/serialisation of RegionaleGueltigkeit with minimal attributes.
        """
        assert_serialization_roundtrip(regionalegueltigkeit, RegionaleGueltigkeitSchema(), expected_json_dict)

    def test_regionalegueltigkeit_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = RegionaleGueltigkeit()

        assert "missing 2 required" in str(excinfo.value)

    def test_regionalegueltigkeit_kriteriumswerte_required(self):
        with pytest.raises(ValueError) as excinfo:
            _ = RegionaleGueltigkeit(
                gueltigkeitstyp=Gueltigkeitstyp.NUR_IN,
                kriteriums_werte=[],
            )

        assert "kriteriumswerte must not be empty." in str(excinfo.value)
