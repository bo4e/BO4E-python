from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.verbrauch import Verbrauch
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.wertermittlungsverfahren import Wertermittlungsverfahren
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
                },
            ),
        ],
    )
    def test_serialization_roundtrip(self, verbrauch: Verbrauch, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of Verbrauch.
        """
        assert_serialization_roundtrip(verbrauch, expected_json_dict)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Verbrauch()  # type: ignore[call-arg]

        assert "4 validation errors" in str(excinfo.value)

    @pytest.mark.parametrize(
        "not_a_valid_obis",
        [
            pytest.param("foo"),  # not a obis instance
        ],
    )
    def test_failing_validation_obis(self, not_a_valid_obis: str) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Verbrauch(
                obis_kennzahl=not_a_valid_obis,
                wert=Decimal(40),
                startdatum=datetime(2021, 12, 1, 0, 0, 0).replace(tzinfo=timezone.utc),
                enddatum=datetime(2021, 12, 2, 0, 0, 0).replace(tzinfo=timezone.utc),
                einheit=Mengeneinheit.KWH,
                wertermittlungsverfahren=Wertermittlungsverfahren.MESSUNG,
            )

        assert "1 validation error" in str(excinfo.value)
        assert "obis_kennzahl" in str(excinfo.value)
        assert "should match pattern" in str(excinfo.value)

    def test_failing_validation_end_later_than_start(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Verbrauch(
                obis_kennzahl="1-0:1.8.1",
                wert=Decimal(40),
                startdatum=datetime(2021, 12, 2, 0, 0, 0).replace(tzinfo=timezone.utc),
                enddatum=datetime(2021, 12, 1, 0, 0, 0).replace(tzinfo=timezone.utc),
                einheit=Mengeneinheit.KWH,
                wertermittlungsverfahren=Wertermittlungsverfahren.MESSUNG,
            )
        assert "has to be later than the start" in str(excinfo.value)
