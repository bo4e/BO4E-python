from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.aufabschlagstaffelproort import AufAbschlagstaffelProOrt, AufAbschlagstaffelProOrtSchema
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestAufAbschlagstaffelProOrt:
    @pytest.mark.parametrize(
        "aufabschlagstaffelproort, expected_json_dict",
        [
            pytest.param(
                AufAbschlagstaffelProOrt(
                    wert=Decimal(2.5),
                    staffelgrenze_von=Decimal(1),
                    staffelgrenze_bis=Decimal(5),
                ),
                {
                    "wert": "2.5",
                    "staffelgrenzeVon": "1",
                    "staffelgrenzeBis": "5",
                },
            ),
        ],
    )
    def test_aufabschlagstaffelproort_required_attributes(self, aufabschlagstaffelproort, expected_json_dict):
        """
        Test de-/serialisation of AufAbschlagstaffelProOrt with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlagstaffelproort, AufAbschlagstaffelProOrtSchema(), expected_json_dict)

    def test_aufabschlagstaffelproort_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = AufAbschlagstaffelProOrt()

        assert "missing 3 required" in str(excinfo.value)
