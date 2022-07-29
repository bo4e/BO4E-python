from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from bo4e.bo.tarif import Tarif
from bo4e.enum.kundentyp import Kundentyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.tarifart import Tarifart
from bo4e.enum.tarifmerkmal import Tarifmerkmal
from bo4e.enum.tariftyp import Tariftyp
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_aufabschlagregional import example_aufabschlagregional
from tests.test_energiemix import example_energiemix
from tests.test_marktteilnehmer import example_marktteilnehmer
from tests.test_preisgarantie import example_preisgarantie
from tests.test_regionaletarifpreisposition import example_regionale_tarifpreisposition
from tests.test_tarifberechnungsparameter import example_tarifberechnungsparameter
from tests.test_tarifeinschraenkung import example_tarifeinschraenkung
from tests.test_tarifpreispositionproort import example_tarifpreispositionproort
from tests.test_vertragskonditionen import example_vertragskonditionen
from tests.test_zeitraum import example_zeitraum


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
    def test_serialization_roundtrip(self, tarif: Tarif) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarif)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Tarif()  # type: ignore[call-arg]
        assert "11 validation error" in str(excinfo.value)  # 3 from Tarif + 8 from tarifinfo
