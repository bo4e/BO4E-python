from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from bo4e.bo.ausschreibung import Ausschreibung
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.enum.ausschreibungsportal import Ausschreibungsportal
from bo4e.enum.ausschreibungsstatus import Ausschreibungsstatus
from bo4e.enum.ausschreibungstyp import Ausschreibungstyp
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_adresse import example_adresse
from tests.test_ausschreibungslos import example_ausschreibungslos
from tests.test_zeitraum import example_zeitraum


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
    def test_serialization_roundtrip(self, ausschreibung: Ausschreibung) -> None:
        assert_serialization_roundtrip(ausschreibung)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Ausschreibung()  # type: ignore[call-arg]

        assert "9 validation errors" in str(excinfo.value)
