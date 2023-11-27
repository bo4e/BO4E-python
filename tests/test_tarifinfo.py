from datetime import datetime, timezone

import pytest

from bo4e import (
    Energiemix,
    Kundentyp,
    Marktteilnehmer,
    Registeranzahl,
    Sparte,
    Tarifinfo,
    Tarifmerkmal,
    Tariftyp,
    Vertragskonditionen,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


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
                    vertragskonditionen=Vertragskonditionen(),
                    zeitliche_gueltigkeit=Zeitraum(),
                    energiemix=Energiemix(),
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
