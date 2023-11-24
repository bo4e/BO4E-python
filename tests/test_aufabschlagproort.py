from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import AufAbschlagProOrt, AufAbschlagstaffelProOrt
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
                            "_id": None,
                        }
                    ],
                    "_id": None,
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
