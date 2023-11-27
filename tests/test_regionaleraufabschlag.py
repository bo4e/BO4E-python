import pytest

from bo4e import (
    AufAbschlagstyp,
    AufAbschlagsziel,
    Energiemix,
    Preisgarantie,
    RegionalePreisstaffel,
    RegionalerAufAbschlag,
    Tarifeinschraenkung,
    Vertragskonditionen,
    Waehrungseinheit,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


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
                    staffeln=[RegionalePreisstaffel()],
                    gueltigkeitszeitraum=Zeitraum(),
                    energiemixaenderung=Energiemix(),
                    vertagskonditionsaenderung=Vertragskonditionen(),
                    garantieaenderung=Preisgarantie(),
                    einschraenkungsaenderung=Tarifeinschraenkung(),
                ),
                id="maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, regionaler_auf_abschlag: RegionalerAufAbschlag) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(regionaler_auf_abschlag)
