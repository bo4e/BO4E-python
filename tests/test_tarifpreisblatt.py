import datetime

import pytest  # type:ignore[import]

from bo4e.bo.tarifpreisblatt import Tarifpreisblatt, TarifpreisblattSchema
from bo4e.com.tarifberechnungsparameter import Tarifberechnungsparameter
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung
from bo4e.enum.kundentyp import Kundentyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.tarifmerkmal import Tarifmerkmal
from bo4e.enum.tariftyp import Tariftyp
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_aufabschlag import example_aufabschlag  # type:ignore[import]
from tests.test_energiemix import example_energiemix  # type:ignore[import]
from tests.test_geraeteeigenschaften import example_geraeteeigenschaften  # type:ignore[import]
from tests.test_marktteilnehmer import example_marktteilnehmer  # type:ignore[import]
from tests.test_preisgarantie import example_preisgarantie  # type:ignore[import]
from tests.test_preisposition import example_preisposition  # type:ignore[import]
from tests.test_tarifpreisposition import example_tarifpreisposition  # type:ignore[import]
from tests.test_vertragskonditionen import example_vertragskonditionen  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


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
    def test_serialization_roundtrip(self, tarifpreisblatt: Tarifpreisblatt):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarifpreisblatt, TarifpreisblattSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Tarifpreisblatt()
        assert "missing 11 required" in str(excinfo.value)  # 8 from tarifinfo + 3 from tarifpreisblatt
