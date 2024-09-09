from datetime import time, timezone

import pytest

from bo4e.com.erreichbarkeit import Erreichbarkeit
from bo4e.com.zeitfenster import Zeitfenster
from tests.serialization_helper import assert_serialization_roundtrip


class TestErreichbarkeit:
    @pytest.mark.parametrize(
        "erreichbarkeit",
        [
            pytest.param(
                Erreichbarkeit(
                    montag_erreichbarkeit=Zeitfenster(
                        startzeit=time(8, 00, tzinfo=timezone.utc), endzeit=time(17, 00, tzinfo=timezone.utc)
                    ),
                    dienstag_erreichbarkeit=Zeitfenster(
                        startzeit=time(8, 00, tzinfo=timezone.utc), endzeit=time(17, 00, tzinfo=timezone.utc)
                    ),
                    mittwoch_erreichbarkeit=Zeitfenster(
                        startzeit=time(8, 00, tzinfo=timezone.utc), endzeit=time(17, 00, tzinfo=timezone.utc)
                    ),
                    donnerstag_erreichbarkeit=Zeitfenster(
                        startzeit=time(8, 00, tzinfo=timezone.utc), endzeit=time(17, 00, tzinfo=timezone.utc)
                    ),
                    freitag_erreichbarkeit=Zeitfenster(
                        startzeit=time(8, 00, tzinfo=timezone.utc), endzeit=time(17, 00, tzinfo=timezone.utc)
                    ),
                    mittagspause=Zeitfenster(
                        startzeit=time(12, 00, tzinfo=timezone.utc), endzeit=time(13, 00, tzinfo=timezone.utc)
                    ),
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, erreichbarkeit: Erreichbarkeit) -> None:
        """
        Test de-/serialisation of Erreichbarkeit.
        """
        assert_serialization_roundtrip(erreichbarkeit)
