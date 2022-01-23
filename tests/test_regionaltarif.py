from datetime import datetime, timezone

import pytest  # type:ignore[import]

from bo4e.bo.regionaltarif import Regionaltarif, RegionaltarifSchema
from bo4e.enum.kundentyp import Kundentyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.tarifmerkmal import Tarifmerkmal
from bo4e.enum.tariftyp import Tariftyp
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_energiemix import example_energiemix  # type:ignore[import]
from tests.test_marktteilnehmer import example_marktteilnehmer  # type:ignore[import]
from tests.test_regionalepreisgarantie import example_regionale_preisgarantie  # type:ignore[import]
from tests.test_regionaleraufabschlag import example_regionaler_auf_abschlag  # type:ignore[import]
from tests.test_regionaletarifpreisposition import example_regionale_tarifpreisposition  # type:ignore[import]
from tests.test_tarifberechnungsparameter import example_tarifberechnungsparameter  # type:ignore[import]
from tests.test_tarifeinschraenkung import example_tarifeinschraenkung  # type:ignore[import]
from tests.test_vertragskonditionen import example_vertragskonditionen  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


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
                    tarifart=Tarifart.MEHRTARIF,
                    tariftyp=Tariftyp.GRUND_ERSATZVERSORGUNG,
                    tarifmerkmale=[Tarifmerkmal.HEIZSTROM],
                    anbieter=example_marktteilnehmer,
                ),
                id="required attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, regionaltarif: Regionaltarif):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(regionaltarif, RegionaltarifSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Regionaltarif()
        assert "missing 11 required" in str(excinfo.value)  # 3 from regionaltarif + 8 from tarifinfo

    def test_failing_validation_list_length_at_least_one(self):
        with pytest.raises(ValueError) as excinfo:
            _ = Regionaltarif(
                preisstand=datetime(2022, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                berechnungsparameter=example_tarifberechnungsparameter,
                tarifpreise=[],
                bezeichnung="foo",
                anbietername="der beste stromanbieter",
                sparte=Sparte.STROM,
                kundentypen=[Kundentyp.PRIVAT, Kundentyp.GEWERBE],
                tarifart=Tarifart.MEHRTARIF,
                tariftyp=Tariftyp.GRUND_ERSATZVERSORGUNG,
                tarifmerkmale=[Tarifmerkmal.HEIZSTROM],
                anbieter=example_marktteilnehmer,
            )

        assert "List tarifpreise must not be empty." in str(excinfo.value)
