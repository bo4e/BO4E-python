from datetime import datetime
from decimal import Decimal

import pytest

from bo4e import Messwertstatus, Messwertstatuszusatz, Zeitraum, Zeitreihenwert
from tests.serialization_helper import assert_serialization_roundtrip


class TestZeitreihenwert:
    @pytest.mark.parametrize(
        "zeitreihenwert",
        [
            pytest.param(
                Zeitreihenwert(
                    zeitraum=Zeitraum(startdatum=datetime(2013, 5, 1), enddatum=datetime(2022, 1, 28)),
                    wert=Decimal(2.5),
                    status=Messwertstatus.ABGELESEN,
                    statuszusatz=Messwertstatuszusatz.Z78_GERAETEWECHSEL,
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, zeitreihenwert: Zeitreihenwert) -> None:
        """
        Test de-/serialisation of Zeitreihenwert.
        """
        assert_serialization_roundtrip(zeitreihenwert)
