import pytest

from bo4e import (
    Energiemix,
    Kosten,
    Kundentyp,
    Marktteilnehmer,
    Registeranzahl,
    Sparte,
    Tarifkosten,
    Tarifmerkmal,
    Tariftyp,
    Vertragskonditionen,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifkosten:
    @pytest.mark.parametrize(
        "tarifkosten",
        [
            pytest.param(
                Tarifkosten(
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
                    kosten=Kosten(),
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifkosten: Tarifkosten) -> None:
        """
        Test de-/serialisation Tarifkosten.
        """
        assert_serialization_roundtrip(tarifkosten)
