from datetime import datetime, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e import Messwertstatus, Messwertstatuszusatz, Zeitreihenwert
from tests.serialization_helper import assert_serialization_roundtrip


class TestZeitreihenwert:
    @pytest.mark.parametrize(
        "zeitreihenwert",
        [
            pytest.param(
                Zeitreihenwert(
                    datum_uhrzeit_von=datetime(2001, 3, 15, tzinfo=timezone.utc),
                    datum_uhrzeit_bis=datetime(2007, 11, 27, tzinfo=timezone.utc),
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
