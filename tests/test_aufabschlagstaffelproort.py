from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import AufAbschlagstaffelProOrt
from tests.serialization_helper import assert_serialization_roundtrip


class TestAufAbschlagstaffelProOrt:
    @pytest.mark.parametrize(
        "aufabschlagstaffelproort",
        [
            pytest.param(
                AufAbschlagstaffelProOrt(
                    wert=Decimal(2.5),
                    staffelgrenze_von=Decimal(1),
                    staffelgrenze_bis=Decimal(5),
                ),
            ),
        ],
    )
    def test_aufabschlagstaffelproort_required_attributes(
        self, aufabschlagstaffelproort: AufAbschlagstaffelProOrt
    ) -> None:
        """
        Test de-/serialisation of AufAbschlagstaffelProOrt with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlagstaffelproort)
