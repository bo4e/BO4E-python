from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Tagesvektor, Zeitreihenwertkompakt
from tests.serialization_helper import assert_serialization_roundtrip

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


class TestTagesvektor:
    @pytest.mark.parametrize(
        "tagesvektor",
        [
            pytest.param(
                example_tagesvektor,
            ),
        ],
    )
    def test_serialization_roundtrip(self, tagesvektor: Tagesvektor) -> None:
        """
        Test de-/serialisation of Preisstaffel.
        """
        assert_serialization_roundtrip(tagesvektor)

    # add tests for issues 261 and 262 here
