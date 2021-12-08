import pytest  # type:ignore[import]

from bo4e.com.kriteriumwert import KriteriumWert, KriteriumWertSchema
from bo4e.enum.tarifregionskriterium import Tarifregionskriterium
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestKriteriumWert:
    @pytest.mark.parametrize(
        "kriteriumwert, expected_json_dict",
        [
            pytest.param(
                KriteriumWert(
                    kriterium=Tarifregionskriterium.ORT,
                    wert="Grünwald",
                ),
                {"kriterium": "ORT", "wert": "Grünwald"},
            ),
        ],
    )
    def test_kriteriumwert_serialization_roundtrip(self, kriteriumwert: KriteriumWert, expected_json_dict: dict):
        """
        Test de-/serialisation of KriteriumWert with minimal attributes.
        """
        assert_serialization_roundtrip(kriteriumwert, KriteriumWertSchema(), expected_json_dict)

    def test_kriteriumwert_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = KriteriumWert()
        assert "missing 2 required" in str(excinfo.value)
