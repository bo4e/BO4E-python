import datetime

import pytest

from bo4e import (
    AufAbschlag,
    Energiemix,
    Kundentyp,
    Marktteilnehmer,
    Preisgarantie,
    Registeranzahl,
    Sparte,
    Tarifberechnungsparameter,
    Tarifeinschraenkung,
    Tarifmerkmal,
    Tarifpreisblatt,
    Tarifpreisposition,
    Tariftyp,
    Vertragskonditionen,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifpreisblatt:
    @pytest.mark.parametrize(
        "tarifpreisblatt",
        [
            pytest.param(
                Tarifpreisblatt(
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
                    # ^^ above is all copy pasted from Tarifinfo BO
                    # vv below are the attributes of tarifpreisblatt
                    preisstand=datetime.datetime(2022, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc),
                    berechnungsparameter=Tarifberechnungsparameter(),
                    tarif_auf_abschlaege=[AufAbschlag()],
                    tarifpreise=[Tarifpreisposition()],
                    preisgarantie=Preisgarantie(),
                    tarifeinschraenkung=Tarifeinschraenkung(),
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifpreisblatt: Tarifpreisblatt) -> None:
        """
        Test de-/serialisation Tarifpreisblatt.
        """
        assert_serialization_roundtrip(tarifpreisblatt)
