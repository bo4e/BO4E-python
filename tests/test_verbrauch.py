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
        "verbrauch, expected_json_dict",
        [
            pytest.param(
                Verbrauch(
                    wert=Decimal(40),
                    startdatum=datetime(2021, 12, 1, 0, 0, 0).replace(tzinfo=timezone.utc),
                    enddatum=datetime(2021, 12, 2, 0, 0, 0).replace(tzinfo=timezone.utc),
                    obis_kennzahl="1-0:1.8.1",
                    einheit=Mengeneinheit.KWH,
                    wertermittlungsverfahren=Wertermittlungsverfahren.MESSUNG,
                ),
                {
                    "startdatum": datetime(2021, 12, 1, 0, 0, tzinfo=timezone.utc),
                    "wert": Decimal("40"),
                    "einheit": Mengeneinheit.KWH,
                    "enddatum": datetime(2021, 12, 2, 0, 0, tzinfo=timezone.utc),
                    "wertermittlungsverfahren": Wertermittlungsverfahren.MESSUNG,
                    "obisKennzahl": "1-0:1.8.1",
                    "_id": None,
                },
            ),
            pytest.param(
                example_verbrauch,
                {
                    "wert": Decimal("40"),
                    "einheit": Mengeneinheit.KWH,
                    "wertermittlungsverfahren": Wertermittlungsverfahren.MESSUNG,
                    "startdatum": None,
                    "enddatum": None,
                    "obisKennzahl": "1-0:1.8.1",
                    "_id": None,
                },
            ),
        ],
    )
    def test_serialization_roundtrip(self, verbrauch: Verbrauch, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of Verbrauch.
        """
        assert_serialization_roundtrip(verbrauch, expected_json_dict)
