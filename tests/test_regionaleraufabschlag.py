import pytest  # type:ignore[import]

from bo4e.com.regionaleraufabschlag import RegionalerAufAbschlag, RegionalerAufAbschlagSchema
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.aufabschlagsziel import AufAbschlagsziel
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_energiemix import example_energiemix  # type:ignore[import]
from tests.test_preisgarantie import example_preisgarantie  # type:ignore[import]
from tests.test_regionalepreisstaffel import example_regionale_preisstaffel  # type:ignore[import]
from tests.test_vertragskonditionen import example_vertragskonditionen  # type:ignore[import]
from tests.test_zeitraum import example_zeitraum  # type:ignore[import]


class TestRegionalerAufAbschlag:
    @pytest.mark.parametrize(
        "regionaler_auf_abschlag",
        [
            pytest.param(
                RegionalerAufAbschlag(
                    bezeichnung="Foo",
                    beschreibung="Bar",
                    auf_abschlagstyp=AufAbschlagstyp.RELATIV,
                    auf_abschlagsziel=AufAbschlagsziel.ARBEITSPREIS_HT,
                    einheit=Waehrungseinheit.CT,
                    website="https://www.hochfrequenz.de",
                    zusatzprodukte=["ein standmixer", "ein thermomix"],
                    voraussetzungen=["lecker essen", "mit ökostrom gekocht"],
                    tarifnamensaenderungen="Super-Duper Tarif",
                    staffeln=[example_regionale_preisstaffel],
                    gueltigkeitszeitraum=example_zeitraum,
                    energiemixaenderung=example_energiemix,
                    vertagskonditionsaenderung=example_vertragskonditionen,
                    garantieaenderung=example_preisgarantie,
                    einschraenkungsaenderung=Tarifeinschraenkung(),
                ),
                id="maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, regionaler_auf_abschlag: RegionalerAufAbschlag):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(regionaler_auf_abschlag, RegionalerAufAbschlagSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = RegionalerAufAbschlag()
        assert "missing 2 required" in str(excinfo.value)
