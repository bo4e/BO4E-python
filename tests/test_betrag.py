import pytest

from bo4e.bo.geschaeftspartner import Geschaeftspartner, GeschaeftspartnerSchema
from bo4e.com.adresse import Adresse
from bo4e.com.externereferenz import ExterneReferenz, ExterneReferenzSchema
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle


class TestBetrag:
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
        assert_serialization_roundtrip(regionskriterium, RegionskriteriumSchema(), expected_json_dict)

    def test_regionskriterium_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Regionskriterium()
        assert "missing 3 required" in str(excinfo.value)
