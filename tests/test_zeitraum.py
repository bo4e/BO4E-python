from datetime import date, time, timedelta, timezone

import pytest

from bo4e import Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestZeitraum:
    @pytest.mark.parametrize(
        "zeitraum",
        [
            pytest.param(
                Zeitraum(
                    dauer="P1DT30H4S",
                ),
                id="period-P1DT30H4S",
            ),
            pytest.param(
                Zeitraum(
                    startdatum=date(2025, 1, 1),
                    enddatum=date(2025, 1, 31),
                ),
                id="startdatum-enddatum",
            ),
            pytest.param(
                Zeitraum(
                    startuhrzeit=time(10, 0, 0),
                    enduhrzeit=time(11, 0, 0),
                ),
                id="startuhrzeit-enduhrzeit",
            ),
            pytest.param(
                Zeitraum(
                    startuhrzeit=time(10, 0, 0, tzinfo=timezone.utc),
                    enduhrzeit=time(11, 0, 0, tzinfo=timezone.utc),
                ),
                id="startuhrzeit-enduhrzeit-utc-timezone",
            ),
            pytest.param(
                Zeitraum(
                    startuhrzeit=time(18, 0, 0, tzinfo=timezone(timedelta(hours=1), "Europe/Berlin")),
                    enduhrzeit=time(19, 0, 0, tzinfo=timezone(timedelta(hours=1), "Europe/Berlin")),
                ),
                id="startuhrzeit-enduhrzeit-berlin-timezone",
            ),
        ],
    )
    def test_serialization_roundtrip(self, zeitraum: Zeitraum) -> None:
        """
        Test de-/serialisation of Zeitraum.
        """
        assert_serialization_roundtrip(zeitraum)
