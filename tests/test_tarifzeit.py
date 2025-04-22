import pytest

from datetime import date
from bo4e import Zeitraum
from bo4e.enum.tarifstufen import Tarifstufen
from bo4e.com.tarifzeit import Tarifzeit
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifzeit:
    @pytest.mark.parametrize(
        "tarifzeit",
        [
            pytest.param(
                Tarifzeit(
                    zeitraum=Zeitraum(
                        startdatum=date(2025, 1, 1),
                        enddatum=date(2025, 1, 31),
                    ),
                    tarifstufe=Tarifstufen("HT"),
                )
            )
        ]
    )
    def test_serialization_roundtrip(self, tarifzeit: Tarifzeit) -> None:
        """
        Test de-/serialisation of Tarifzeit.
        """
        assert_serialization_roundtrip(tarifzeit)