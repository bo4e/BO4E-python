import datetime

import pytest
from pydantic import ValidationError

from bo4e import (
    Kundentyp,
    Registeranzahl,
    Sparte,
    Tarifberechnungsparameter,
    Tarifeinschraenkung,
    Tarifmerkmal,
    Tarifpreisblatt,
    Tariftyp,
)
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_aufabschlag import example_aufabschlag
from tests.test_energiemix import example_energiemix
from tests.test_marktteilnehmer import example_marktteilnehmer
from tests.test_preisgarantie import example_preisgarantie
from tests.test_tarifpreisposition import example_tarifpreisposition
from tests.test_vertragskonditionen import example_vertragskonditionen
from tests.test_zeitraum import example_zeitraum


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
                    vertragskonditionen=example_vertragskonditionen,
                    zeitliche_gueltigkeit=example_zeitraum,
                    energiemix=example_energiemix,
                    anbieter=example_marktteilnehmer,
                    # ^^ above is all copy pasted from Tarifinfo BO
                    # vv below are the attributes of tarifpreisblatt
                    preisstand=datetime.datetime(2022, 1, 1, 0, 0, 0, tzinfo=datetime.timezone.utc),
                    berechnungsparameter=Tarifberechnungsparameter(),
                    tarif_auf_abschlaege=[example_aufabschlag],
                    tarifpreise=[example_tarifpreisposition],
                    preisgarantie=example_preisgarantie,
                    tarifeinschraenkung=Tarifeinschraenkung(),
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifpreisblatt: Tarifpreisblatt) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarifpreisblatt)
