from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.aufabschlagproort import AufAbschlagProOrt, AufAbschlagProOrtSchema
from bo4e.com.aufabschlagstaffelproort import AufAbschlagstaffelProOrt
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestAufAbschlagProOrt:
    @pytest.mark.parametrize(
        "aufabschlagproort, expected_json_dict",
        [
            pytest.param(
                AufAbschlagProOrt(
                    postleitzahl="01187",
                    ort="Dresden",
                    netznr="2",
                    staffeln=[
                        AufAbschlagstaffelProOrt(
                            wert=Decimal(2.5),
                            staffelgrenze_von=Decimal(1),
                            staffelgrenze_bis=Decimal(5),
                        )
                    ],
                ),
                {
                    "postleitzahl": "01187",
                    "ort": "Dresden",
                    "netznr": "2",
                    "staffeln": [
                        {
                            "wert": "2.5",
                            "staffelgrenzeVon": "1",
                            "staffelgrenzeBis": "5",
                        }
                    ],
                },
            )
        ],
    )
    def test_serialization_roundtrip(self, aufabschlagproort, expected_json_dict):
        """
        Test de-/serialisation of AufAbschlagProOrt with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlagproort, AufAbschlagProOrtSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = AufAbschlagProOrt()

        assert "missing 4 required" in str(excinfo.value)

    def test_failing_validation_list_length_at_least_one(self):
        with pytest.raises(ValueError) as excinfo:
            _ = AufAbschlagProOrt(
                postleitzahl="01187",
                ort="Dresden",
                netznr="2",
                staffeln=[],
            )

        assert "List staffeln must not be empty." in str(excinfo.value)
