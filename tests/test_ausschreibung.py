from datetime import datetime, timezone

import pytest  # type:ignore[import]

from bo4e.bo.ausschreibung import Ausschreibung, AusschreibungSchema
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.enum.ausschreibungsportal import Ausschreibungsportal
from bo4e.enum.ausschreibungsstatus import Ausschreibungsstatus
from bo4e.enum.ausschreibungstyp import Ausschreibungstyp
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_adresse import example_adresse  # type:ignore[import]
from tests.test_ausschreibungslos import example_ausschreibungslos  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


class TestAusschreibung:
    @pytest.mark.parametrize(
        "ausschreibung",
        [
            pytest.param(
                Ausschreibung(
                    ausschreibungsnummer="239230",
                    ausschreibungstyp=Ausschreibungstyp.PRIVATRECHTLICH,
                    ausschreibungsstatus=Ausschreibungsstatus.PHASE3,
                    kostenpflichtig=True,
                    ausschreibungportal=Ausschreibungsportal.BMWI,
                    webseite="https://meineausschreibungswebsite.inv/",
                    veroeffentlichungszeitpunkt=datetime(2022, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    abgabefrist=example_zeitraum,
                    bindefrist=example_zeitraum,
                    ausschreibender=Geschaeftspartner(
                        name1="Batman",
                        gewerbekennzeichnung=True,
                        geschaeftspartnerrolle=[Geschaeftspartnerrolle.LIEFERANT],
                        partneradresse=example_adresse,
                    ),
                    lose=[example_ausschreibungslos],
                ),
                id="maximal attributes",
            ),
            pytest.param(
                Ausschreibung(
                    ausschreibungsnummer="239230",
                    ausschreibungstyp=Ausschreibungstyp.PRIVATRECHTLICH,
                    ausschreibungsstatus=Ausschreibungsstatus.PHASE3,
                    kostenpflichtig=True,
                    veroeffentlichungszeitpunkt=datetime(2022, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                    abgabefrist=example_zeitraum,
                    bindefrist=example_zeitraum,
                    ausschreibender=Geschaeftspartner(
                        name1="Batman",
                        gewerbekennzeichnung=True,
                        geschaeftspartnerrolle=[Geschaeftspartnerrolle.LIEFERANT],
                        partneradresse=example_adresse,
                    ),
                    lose=[example_ausschreibungslos],
                ),
                id="minimal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, ausschreibung: Ausschreibung):
        assert_serialization_roundtrip(ausschreibung, AusschreibungSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Ausschreibung()

        assert "missing 9 required" in str(excinfo.value)
