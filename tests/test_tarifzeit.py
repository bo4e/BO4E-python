from datetime import date

import pytest

from bo4e import Tarifzeit, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifzeit:
    @pytest.mark.parametrize(
        "tarifzeit",
        [
            pytest.param(
                Tarifzeit(
                    zeitraum=Zeitraum(),
                    tarifstufe="HT",
                ),
                id="all attributes at first level",
            )
        ],
    )
    def test_serialization_roundtrip(self, tarifzeit: Tarifzeit) -> None:
        """
        Test de-/serialisation of Tarifzeit.
        """
        assert_serialization_roundtrip(tarifzeit)
