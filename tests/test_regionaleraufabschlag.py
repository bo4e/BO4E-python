import pytest
from pydantic import ValidationError

from bo4e.com.regionaleraufabschlag import RegionalerAufAbschlag
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.aufabschlagsziel import AufAbschlagsziel
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_energiemix import example_energiemix
from tests.test_preisgarantie import example_preisgarantie
from tests.test_regionalepreisstaffel import example_regionale_preisstaffel
from tests.test_vertragskonditionen import example_vertragskonditionen
from tests.test_zeitraum import example_zeitraum

example_regionaler_auf_abschlag = RegionalerAufAbschlag(
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
)


class TestRegionalerAufAbschlag:
    @pytest.mark.parametrize(
        "regionaler_auf_abschlag",
        [
            pytest.param(
                example_regionaler_auf_abschlag,
                id="maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, regionaler_auf_abschlag: RegionalerAufAbschlag) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(regionaler_auf_abschlag)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = RegionalerAufAbschlag()  # type: ignore[call-arg]
        assert "2 validation errors" in str(excinfo.value)
