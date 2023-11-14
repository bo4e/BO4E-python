from datetime import datetime, timezone

import pytest

from bo4e import (
    Ausschreibung,
    Ausschreibungslos,
    Ausschreibungsportal,
    Ausschreibungsstatus,
    Ausschreibungstyp,
    Geschaeftspartner,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestAusschreibung:
    @pytest.mark.parametrize(
        "ausschreibung",
        [
            pytest.param(
                Ausschreibung(
                    ausschreibungsnummer="239230",
                    ausschreibungstyp=Ausschreibungstyp.PRIVATRECHTLICH,
                    ausschreibungsstatus=Ausschreibungsstatus.PHASE3,
                    ist_kostenpflichtig=True,
                    ausschreibungportal=Ausschreibungsportal.BMWI,
                    webseite="https://meineausschreibungswebsite.inv/",
                    veroeffentlichungszeitpunkt=datetime(2022, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    abgabefrist=Zeitraum(),
                    bindefrist=Zeitraum(),
                    ausschreibender=Geschaeftspartner(),
                    lose=[Ausschreibungslos()],
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, ausschreibung: Ausschreibung) -> None:
        """
        Test de-/serialisation of Ausschreibung.
        """
        assert_serialization_roundtrip(ausschreibung)
