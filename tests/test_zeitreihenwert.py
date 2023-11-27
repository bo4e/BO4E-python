from datetime import datetime, timezone
from decimal import Decimal

import pytest

from bo4e import Messwertstatus, Messwertstatuszusatz, Zeitreihenwert, Zeitspanne
from tests.serialization_helper import assert_serialization_roundtrip


class TestZeitreihenwert:
    @pytest.mark.parametrize(
        "zeitreihenwert",
        [
            pytest.param(
                Zeitreihenwert(
                    zeitspanne=Zeitspanne(
                        start=datetime(2013, 5, 1, tzinfo=timezone.utc), ende=datetime(2022, 1, 28, tzinfo=timezone.utc)
                    ),
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
