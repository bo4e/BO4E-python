from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import AufAbschlagProOrt, AufAbschlagstaffelProOrt
from tests.serialization_helper import assert_serialization_roundtrip


class TestAufAbschlagProOrt:
    @pytest.mark.parametrize(
        "aufabschlagproort",
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
            )
        ],
    )
    def test_serialization_roundtrip(
        self,
        aufabschlagproort: AufAbschlagProOrt,
    ) -> None:
        """
        Test de-/serialisation of AufAbschlagProOrt with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlagproort)
