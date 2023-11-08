import datetime

import pytest
from pydantic import ValidationError

from bo4e import (
    Kundentyp,
    Marktteilnehmer,
    Sparte,
    Tarifart,
    Tarifberechnungsparameter,
    Tarifeinschraenkung,
    Tarifmerkmal,
    Tarifpreisblatt,
    Tariftyp,
    Vertragskonditionen,
)
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_aufabschlag import example_aufabschlag
from tests.test_energiemix import example_energiemix
from tests.test_preisgarantie import example_preisgarantie
from tests.test_tarifpreisposition import example_tarifpreisposition
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
                    tarifart=Tarifart.MEHRTARIF,
                    tariftyp=Tariftyp.GRUND_ERSATZVERSORGUNG,
                    tarifmerkmale=[Tarifmerkmal.HEIZSTROM],
                    website="https://foo.inv",
                    bemerkung="super billig aber auch super dreckig",
                    vertragskonditionen=Vertragskonditionen(),
                    zeitliche_gueltigkeit=example_zeitraum,
                    energiemix=example_energiemix,
                    anbieter=Marktteilnehmer(),
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
        Test de-/serialisation Tarifpreisblatt.
        """
        assert_serialization_roundtrip(tarifpreisblatt)
