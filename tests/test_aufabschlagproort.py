from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.aufabschlagproort import AufAbschlagProOrt
from bo4e.com.aufabschlagstaffelproort import AufAbschlagstaffelProOrt
from tests.serialization_helper import assert_serialization_roundtrip


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
                            "wert": Decimal("2.5"),
                            "staffelgrenzeVon": Decimal("1"),
                            "staffelgrenzeBis": Decimal("5"),
                        }
                    ],
                },
            )
        ],
    )
    def test_serialization_roundtrip(
        self, aufabschlagproort: AufAbschlagProOrt, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of AufAbschlagProOrt with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlagproort, expected_json_dict)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = AufAbschlagProOrt()  # type: ignore[call-arg]

        assert "4 validation errors" in str(excinfo.value)

    def test_failing_validation_list_length_at_least_one(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = AufAbschlagProOrt(
                postleitzahl="01187",
                ort="Dresden",
                netznr="2",
                staffeln=[],
            )

        assert "1 validation error" in str(excinfo.value)
        assert "too_short" in str(excinfo.value)
