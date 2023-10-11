from datetime import datetime, timezone

import pytest

from bo4e import Kundentyp, Regionaltarif, Sparte, Tarifmerkmal, Tariftyp
from bo4e.enum.registeranzahl import Registeranzahl
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_energiemix import example_energiemix
from tests.test_marktteilnehmer import example_marktteilnehmer
from tests.test_regionalepreisgarantie import example_regionale_preisgarantie
from tests.test_regionaleraufabschlag import example_regionaler_auf_abschlag
from tests.test_regionaletarifpreisposition import example_regionale_tarifpreisposition
from tests.test_tarifberechnungsparameter import example_tarifberechnungsparameter
from tests.test_tarifeinschraenkung import example_tarifeinschraenkung
from tests.test_vertragskonditionen import example_vertragskonditionen
from tests.test_zeitraum import example_zeitraum


class TestRegionaltarif:
    @pytest.mark.parametrize(
        "regionaltarif",
        [
            pytest.param(
                Regionaltarif(
                    preisstand=datetime(2022, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                    berechnungsparameter=example_tarifberechnungsparameter,
                    tarif_auf_abschlaege=[example_regionaler_auf_abschlag],
                    tarifpreise=[example_regionale_tarifpreisposition],
                    preisgarantien=[example_regionale_preisgarantie],
                    tarifeinschraenkung=example_tarifeinschraenkung,
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
                    vertragskonditionen=example_vertragskonditionen,
                    zeitliche_gueltigkeit=example_zeitraum,
                    energiemix=example_energiemix,
                    anbieter=example_marktteilnehmer,
                ),
                id="required and optional attributes",
            ),
            pytest.param(
                Regionaltarif(
                    preisstand=datetime(2022, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                    berechnungsparameter=example_tarifberechnungsparameter,
                    tarifpreise=[example_regionale_tarifpreisposition],
                    # ^^ above are the attributes of Regionaltarif
                    # vv below is all copy pasted from Tarifinfo test
                    bezeichnung="foo",
                    anbietername="der beste stromanbieter",
                    sparte=Sparte.STROM,
                    kundentypen=[Kundentyp.PRIVAT, Kundentyp.GEWERBE],
                    registeranzahl=Registeranzahl.MEHRTARIF,
                    tariftyp=Tariftyp.GRUND_ERSATZVERSORGUNG,
                    tarifmerkmale=[Tarifmerkmal.HEIZSTROM],
                    anbieter=example_marktteilnehmer,
                ),
                id="required attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, regionaltarif: Regionaltarif) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(regionaltarif)
