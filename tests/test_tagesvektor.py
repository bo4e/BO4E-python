from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Tagesvektor, Zeitreihenwertkompakt
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_sigmoidparameter import example_sigmoidparameter

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
    "tag": datetime(2021, 12, 15, 5, 0, tzinfo=timezone.utc),
    "werte": [
        {"wert": Decimal("40"), "statuszusatz": None, "status": None, "_id": None},
        {"wert": Decimal("50"), "statuszusatz": None, "status": None, "_id": None},
    ],
    "_id": None,
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
    def test_serialization_roundtrip(self, tagesvektor: Tagesvektor, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of Preisstaffel.
        """
        assert_serialization_roundtrip(tagesvektor, expected_json_dict)

    # add tests for issues 261 and 262 here
