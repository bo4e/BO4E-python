import pytest  # type:ignore[import]

from src.bo4e.com.regionskriterium import Regionskriterium, RegionskriteriumSchema
from src.bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp
from src.bo4e.enum.regionskriteriumtyp import Regionskriteriumtyp
from tests.serialization_test_helper import test_serialization_roundtrip


class TestRegionskriterium:
    @pytest.mark.parametrize(
        "regionskriterium, expected_json_dict",
        [
            pytest.param(
                Regionskriterium(
                    regionskriteriumtyp=Regionskriteriumtyp.REGELGEBIET_NAME,
                    gueltigkeitstyp=Gueltigkeitstyp.NICHT_IN,
                    wert="Was ist ein Regionskriterium?",
                ),
                {
                    "gueltigkeitstyp": "NICHT_IN",
                    "regionskriteriumtyp": "REGELGEBIET_NAME",
                    "wert": "Was ist ein Regionskriterium?",
                },
            ),
        ],
    )
    def test_regionskriterium_serialization_roundtrip(
        self, regionskriterium: Regionskriterium, expected_json_dict: dict
    ):
        """
        Test de-/serialisation of Regionskriterium with minimal attributes.
        """
        test_serialization_roundtrip(regionskriterium, RegionskriteriumSchema(), expected_json_dict)

    def test_regionskriterium_missing_required_attribute(self):
        with pytest.raises(TypeError):
            _ = Regionskriterium()
