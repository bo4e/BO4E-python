from datetime import datetime, timezone

import pytest

from bo4e import (
    Energiemix,
    Kundentyp,
    Marktteilnehmer,
    RegionalePreisgarantie,
    RegionalerAufAbschlag,
    RegionaleTarifpreisposition,
    Regionaltarif,
    Registeranzahl,
    Sparte,
    Tarifberechnungsparameter,
    Tarifeinschraenkung,
    Tarifmerkmal,
    Tariftyp,
    Vertragskonditionen,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestRegionaltarif:
    @pytest.mark.parametrize(
        "regionaltarif",
        [
            pytest.param(
                Regionaltarif(
                    preisstand=datetime(2022, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                    berechnungsparameter=Tarifberechnungsparameter(),
                    tarif_auf_abschlaege=[RegionalerAufAbschlag()],
                    tarifpreise=[RegionaleTarifpreisposition()],
                    preisgarantien=[RegionalePreisgarantie()],
                    tarifeinschraenkung=Tarifeinschraenkung(),
                    # ^^ above are the attributes of Regionaltarif
                    # vv below is all copy pasted from Tarifinfo test
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
            )
        ],
    )
    def test_serialization_roundtrip(self, regionaltarif: Regionaltarif) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(regionaltarif)
