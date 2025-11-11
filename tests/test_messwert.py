from datetime import datetime, timezone

import pytest

from bo4e import Menge, Messwert, Messwertstatus, Messwertstatuszusatz
from tests.serialization_helper import assert_serialization_roundtrip


class TestMesswert:
    @pytest.mark.parametrize(
        "messwert",
        [
            pytest.param(
                Messwert(
                    messwertstatus=Messwertstatus.ABGELESEN,
                    messwertstatuszusatz=Messwertstatuszusatz.Z84_LEERSTAND,
                    zeitpunkt=datetime(2022, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                    wert=Menge(),
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, messwert: Messwert) -> None:
        """
        Test de-/serialisation roundtrip.
        """
        assert_serialization_roundtrip(messwert)
