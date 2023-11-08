from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from bo4e import Kundentyp, Marktteilnehmer, Sparte, Tarifart, Tarifinfo, Tarifmerkmal, Tariftyp, Vertragskonditionen
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_energiemix import example_energiemix
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
                    tarifart=Tarifart.MEHRTARIF,
                    tariftyp=Tariftyp.GRUND_ERSATZVERSORGUNG,
                    tarifmerkmale=[Tarifmerkmal.HEIZSTROM],
                    website="https://foo.inv",
                    bemerkung="super billig aber auch super dreckig",
                    vertragskonditionen=Vertragskonditionen(),
                    zeitliche_gueltigkeit=example_zeitraum,
                    energiemix=example_energiemix,
                    anbieter=Marktteilnehmer(),
                    anwendung_von=datetime(2022, 1, 1, 0, 0, 0, tzinfo=timezone.utc),
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifinfo: Tarifinfo) -> None:
        """
        Test de-/serialisation Tarifinfo.
        """
        assert_serialization_roundtrip(tarifinfo)
