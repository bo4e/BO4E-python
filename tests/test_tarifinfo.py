from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from bo4e import Kundentyp, Registeranzahl, Sparte, Tarifinfo, Tarifmerkmal, Tariftyp
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_energiemix import example_energiemix
from tests.test_marktteilnehmer import example_marktteilnehmer
from tests.test_vertragskonditionen import example_vertragskonditionen
from tests.test_zeitraum import example_zeitraum


class TestTarifinfo:
    @pytest.mark.parametrize(
        "tarifinfo",
        [
            pytest.param(
                Tarifinfo(
                    bezeichnung="foo",
                    anbietername="der beste stromanbieter",
                    sparte=Sparte.STROM,
                    kundentypen=[Kundentyp.PRIVAT, Kundentyp.GEWERBE],
                    registeranzahl=Registeranzahl.MEHRTARIF,
                    tariftyp=Tariftyp.GRUND_ERSATZVERSORGUNG,
                    tarifmerkmale=[Tarifmerkmal.HEIZSTROM],
                    website="https://foo.inv",
                    bemerkung="super billig aber auch super dreckig",
                    vertragskonditionen=example_vertragskonditionen,
                    zeitliche_gueltigkeit=example_zeitraum,
                    energiemix=example_energiemix,
                    anbieter=example_marktteilnehmer,
                    anwendung_von=datetime(2022, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifinfo: Tarifinfo) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarifinfo)
