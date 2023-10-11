from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Mengeneinheit, Verbrauch, Wertermittlungsverfahren
from tests.serialization_helper import assert_serialization_roundtrip

example_verbrauch = Verbrauch(
    wert=Decimal(40),
    obis_kennzahl="1-0:1.8.1",
    einheit=Mengeneinheit.KWH,
    wertermittlungsverfahren=Wertermittlungsverfahren.MESSUNG,
)


class TestVerbrauch:
    @pytest.mark.parametrize(
        "verbrauch",
        [
            pytest.param(
                Verbrauch(
                    wert=Decimal(40),
                    startdatum=datetime(2021, 12, 1, 0, 0, 0).replace(tzinfo=timezone.utc),
                    enddatum=datetime(2021, 12, 2, 0, 0, 0).replace(tzinfo=timezone.utc),
                    obis_kennzahl="1-0:1.8.1",
                    einheit=Mengeneinheit.KWH,
                    wertermittlungsverfahren=Wertermittlungsverfahren.MESSUNG,
                )
            ),
            pytest.param(example_verbrauch),
        ],
    )
    def test_serialization_roundtrip(self, verbrauch: Verbrauch) -> None:
        """
        Test de-/serialisation of Verbrauch.
        """
        assert_serialization_roundtrip(verbrauch)
