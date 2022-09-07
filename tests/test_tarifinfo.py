from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from bo4e.bo.tarifinfo import Tarifinfo
from bo4e.enum.kundentyp import Kundentyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.tarifmerkmal import Tarifmerkmal
from bo4e.enum.tariftyp import Tariftyp
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
                    tarifart=Tarifart.MEHRTARIF,
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

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Tarifinfo()  # type: ignore[call-arg]

        assert "8 validation errors" in str(excinfo.value)
