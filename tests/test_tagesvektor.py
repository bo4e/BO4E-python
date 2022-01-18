from datetime import datetime, timezone
from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.tagesvektor import Tagesvektor, TagesvektorSchema
from bo4e.com.zeitreihenwertkompakt import Zeitreihenwertkompakt
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_sigmoidparameter import example_sigmoidparameter  # type:ignore[import]

example_tagesvektor: Tagesvektor = Tagesvektor(
    tag=datetime(2021, 12, 15, 5, 0, tzinfo=timezone.utc),
    werte=[
        Zeitreihenwertkompakt(
            wert=Decimal(40),
        ),
        Zeitreihenwertkompakt(
            wert=Decimal(50),
        ),
    ],
)
example_tagesvektor_json = {
    "tag": "2021-12-15T05:00:00+00:00",
    "werte": [
        {"wert": "40", "statuszusatz": None, "status": None},
        {"wert": "50", "statuszusatz": None, "status": None},
    ],
}


class TestTagesvektor:
    @pytest.mark.parametrize(
        "tagesvektor, expected_json_dict",
        [
            pytest.param(
                example_tagesvektor,
                example_tagesvektor_json,
            ),
        ],
    )
    def test_serialization_roundtrip(self, tagesvektor: Tagesvektor, expected_json_dict: dict):
        """
        Test de-/serialisation of Preisstaffel.
        """
        assert_serialization_roundtrip(tagesvektor, TagesvektorSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Tagesvektor()

        assert "missing 2 required" in str(excinfo.value)

    def test_list_not_long_enough_attribute(self):
        with pytest.raises(ValueError) as excinfo:
            _ = Tagesvektor(tag=datetime(2021, 12, 15, 5, 0, tzinfo=timezone.utc), werte=[])

        assert "List werte must not be empty" in str(excinfo.value)

    # add tests for issues 261 and 262 here
