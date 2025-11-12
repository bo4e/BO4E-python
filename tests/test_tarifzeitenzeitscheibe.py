from datetime import date

import pytest

from bo4e import Tarifzeit, TarifzeitenZeitscheibe, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifzeitenZeitscheibe:
    @pytest.mark.parametrize(
        "tarifzeitenzeitscheibe",
        [
            pytest.param(
                TarifzeitenZeitscheibe(
                    gueltigkeit=Zeitraum(),
                    tarifzeiten=[Tarifzeit()],
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifzeitenzeitscheibe: TarifzeitenZeitscheibe) -> None:
        """
        Test de-/serialisation of TarifzeitenZeitscheibe.
        """
        assert_serialization_roundtrip(tarifzeitenzeitscheibe)
