import pytest

from bo4e import (
    AufAbschlagProOrt,
    AufAbschlagRegional,
    AufAbschlagstyp,
    AufAbschlagsziel,
    Energiemix,
    Preisgarantie,
    Tarifeinschraenkung,
    Vertragskonditionen,
    Waehrungseinheit,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestAufAbschlagRegional:
    @pytest.mark.parametrize(
        "aufabschlagregional",
        [
            pytest.param(
                AufAbschlagRegional(
                    bezeichnung="foo",
                    betraege=[AufAbschlagProOrt()],
                    beschreibung="bar",
                    auf_abschlagstyp=AufAbschlagstyp.RELATIV,
                    auf_abschlagsziel=AufAbschlagsziel.ARBEITSPREIS_HT,
                    einheit=Waehrungseinheit.EUR,
                    website="foo.bar",
                    zusatzprodukte=["Asterix", "Obelix"],
                    voraussetzungen=["Petterson", "Findus"],
                    tarifnamensaenderungen="foobar",
                    gueltigkeitszeitraum=Zeitraum(),
                    energiemixaenderung=Energiemix(),
                    vertagskonditionsaenderung=Vertragskonditionen(),
                    garantieaenderung=Preisgarantie(),
                    einschraenkungsaenderung=Tarifeinschraenkung(),
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, aufabschlagregional: AufAbschlagRegional) -> None:
        """
        Test de-/serialisation of AufAbschlagRegional with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlagregional)
