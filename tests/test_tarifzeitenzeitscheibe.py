from datetime import date

import pytest

from bo4e import Zeitraum
from bo4e.com.tarifzeit import Tarifzeit
from bo4e.com.tarifzeitenzeitscheibe import TarifzeitenZeitscheibe
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifzeitenZeitscheibe:
    @pytest.mark.parametrize(
        "zeitscheibe",
        [
            pytest.param(
                TarifzeitenZeitscheibe(
                    gueltigkeit=Zeitraum(
                        startdatum=date(2025, 1, 1),
                        enddatum=date(2025, 1, 31),
                    ),
                    tarifzeiten=[
                        Tarifzeit(
                            zeitraum=Zeitraum(
                                startdatum=date(2025, 1, 1),
                                enddatum=date(2025, 1, 31),
                            ),
                            tarifstufe="HT",
                        )
                    ],
                )
            )
        ]
    )
    def test_serialization_roundtrip(self, zeitscheibe: TarifzeitenZeitscheibe) -> None:
        """
        Test de-/serialisation of TarifzeitenZeitscheibe.
        """
        assert_serialization_roundtrip(zeitscheibe)
