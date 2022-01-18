import datetime
from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.verbrauch import Verbrauch, VerbrauchSchema
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.wertermittlungsverfahren import Wertermittlungsverfahren
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]

example_verbrauch = Verbrauch(
    wert=Decimal(40),
    obis_kennzahl="1-0:1.8.1",
    mengeneinheit=Mengeneinheit.KWH,
    wertermittlungsverfahren=Wertermittlungsverfahren.MESSUNG,
)


class TestVerbrauch:
    @pytest.mark.parametrize(
        "verbrauch, expected_json_dict",
        [
            pytest.param(
                Verbrauch(
                    wert=Decimal(40),
                    startdatum=datetime.datetime(2021, 12, 1, 0, 0, 0).replace(tzinfo=datetime.timezone.utc),
                    enddatum=datetime.datetime(2021, 12, 2, 0, 0, 0).replace(tzinfo=datetime.timezone.utc),
                    obis_kennzahl="1-0:1.8.1",
                    mengeneinheit=Mengeneinheit.KWH,
                    wertermittlungsverfahren=Wertermittlungsverfahren.MESSUNG,
                ),
                {
                    "startdatum": "2021-12-01T00:00:00+00:00",
                    "wert": "40",
                    "mengeneinheit": "KWH",
                    "enddatum": "2021-12-02T00:00:00+00:00",
                    "wertermittlungsverfahren": "MESSUNG",
                    "obisKennzahl": "1-0:1.8.1",
                },
            ),
            pytest.param(
                example_verbrauch,
                {
                    "wert": "40",
                    "mengeneinheit": "KWH",
                    "wertermittlungsverfahren": "MESSUNG",
                    "startdatum": None,
                    "enddatum": None,
                    "obisKennzahl": "1-0:1.8.1",
                },
            ),
        ],
    )
    def test_serialization_roundtrip(self, verbrauch: Verbrauch, expected_json_dict: dict):
        """
        Test de-/serialisation of Verbrauch.
        """
        assert_serialization_roundtrip(verbrauch, VerbrauchSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Verbrauch()

        assert "missing 4 required" in str(excinfo.value)

    @pytest.mark.parametrize(
        "not_a_valid_obis",
        [
            pytest.param("foo"),  # not a obis instance
        ],
    )
    def test_failing_validation_obis(self, not_a_valid_obis: str):
        with pytest.raises(ValueError) as excinfo:
            _ = Verbrauch(
                obis_kennzahl=not_a_valid_obis,
                wert=Decimal(40),
                startdatum=datetime.datetime(2021, 12, 1, 0, 0, 0).replace(tzinfo=datetime.timezone.utc),
                enddatum=datetime.datetime(2021, 12, 2, 0, 0, 0).replace(tzinfo=datetime.timezone.utc),
                mengeneinheit=Mengeneinheit.KWH,
                wertermittlungsverfahren=Wertermittlungsverfahren.MESSUNG,
            )

        assert "'obis_kennzahl' must match regex " in str(excinfo.value)

    def test_failing_validation_end_later_than_start(self):
        with pytest.raises(ValueError) as excinfo:
            _ = Verbrauch(
                obis_kennzahl="1-0:1.8.1",
                wert=Decimal(40),
                startdatum=datetime.datetime(2021, 12, 2, 0, 0, 0).replace(tzinfo=datetime.timezone.utc),
                enddatum=datetime.datetime(2021, 12, 1, 0, 0, 0).replace(tzinfo=datetime.timezone.utc),
                mengeneinheit=Mengeneinheit.KWH,
                wertermittlungsverfahren=Wertermittlungsverfahren.MESSUNG,
            )
        assert "has to be later than the start" in str(excinfo)
