import pytest
from pydantic import ValidationError

from bo4e import (
    AufAbschlagstyp,
    AufAbschlagsziel,
    Preisgarantie,
    RegionalerAufAbschlag,
    Tarifeinschraenkung,
    Vertragskonditionen,
    Waehrungseinheit,
)
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_energiemix import example_energiemix
from tests.test_regionalepreisstaffel import example_regionale_preisstaffel
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
    vertagskonditionsaenderung=Vertragskonditionen(),
    garantieaenderung=Preisgarantie(),
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
