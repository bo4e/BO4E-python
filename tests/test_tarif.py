from datetime import datetime, timezone

import pytest

from bo4e import (
    AufAbschlagRegional,
    Energiemix,
    Kundentyp,
    Marktteilnehmer,
    Preisgarantie,
    Registeranzahl,
    Sparte,
    Tarif,
    Tarifberechnungsparameter,
    Tarifeinschraenkung,
    Tarifmerkmal,
    TarifpreispositionProOrt,
    Tariftyp,
    Vertragskonditionen,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarif:
    @pytest.mark.parametrize(
        "tarif",
        [
            pytest.param(
                Tarif(
                    preisstand=datetime(2022, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                    berechnungsparameter=Tarifberechnungsparameter(),
                    tarif_auf_abschlaege=[AufAbschlagRegional()],
                    tarifpreise=[TarifpreispositionProOrt()],
                    preisgarantie=Preisgarantie(),
                    tarifeinschraenkung=Tarifeinschraenkung(),
                    # below are the attributes of tarifinfo
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
                ),
                id="all attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarif: Tarif) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarif)
