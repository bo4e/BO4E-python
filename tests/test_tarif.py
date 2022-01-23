from datetime import datetime, timezone

import pytest  # type:ignore[import]

from bo4e.bo.tarif import Tarif, TarifSchema
from bo4e.enum.kundentyp import Kundentyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.tarifmerkmal import Tarifmerkmal
from bo4e.enum.tariftyp import Tariftyp
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_aufabschlagregional import example_aufabschlagregional  # type:ignore[import]
from tests.test_energiemix import example_energiemix  # type:ignore[import]
from tests.test_marktteilnehmer import example_marktteilnehmer  # type:ignore[import]
from tests.test_preisgarantie import example_preisgarantie  # type:ignore[import]
from tests.test_regionaletarifpreisposition import example_regionale_tarifpreisposition  # type:ignore[import]
from tests.test_tarifberechnungsparameter import example_tarifberechnungsparameter  # type:ignore[import]
from tests.test_tarifeinschraenkung import example_tarifeinschraenkung  # type:ignore[import]
from tests.test_tarifpreispositionproort import example_tarifpreispositionproort  # type:ignore[import]
from tests.test_vertragskonditionen import example_vertragskonditionen  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


class TestTarif:
    @pytest.mark.parametrize(
        "tarif",
        [
            pytest.param(
                Tarif(
                    preisstand=datetime(2022, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                    berechnungsparameter=example_tarifberechnungsparameter,
                    tarif_auf_abschlaege=[example_aufabschlagregional],
                    tarifpreise=[example_tarifpreispositionproort],
                    preisgarantie=example_preisgarantie,
                    tarifeinschraenkung=example_tarifeinschraenkung,
                    # below are the attributes of tarifinfo
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
                ),
                id="required and optional attributes",
            ),
            pytest.param(
                Tarif(
                    preisstand=datetime(2022, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                    berechnungsparameter=example_tarifberechnungsparameter,
                    tarifpreise=[example_tarifpreispositionproort],
                    # below are the attributes of tarifinfo
                    bezeichnung="foo",
                    anbietername="der beste stromanbieter",
                    sparte=Sparte.STROM,
                    kundentypen=[Kundentyp.PRIVAT, Kundentyp.GEWERBE],
                    tarifart=Tarifart.MEHRTARIF,
                    tariftyp=Tariftyp.GRUND_ERSATZVERSORGUNG,
                    tarifmerkmale=[Tarifmerkmal.HEIZSTROM],
                    anbieter=example_marktteilnehmer,
                ),
                id="only required attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarif: Tarif):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarif, TarifSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Tarif()
        assert "missing 11 required" in str(excinfo.value)  # 3 from Tarif + 8 from tarifinfo
