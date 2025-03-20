import pytest

from bo4e import AufAbschlag, AufAbschlagstyp, AufAbschlagsziel, Preisstaffel, Waehrungseinheit, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestAufAbschlag:
    @pytest.mark.parametrize(
        "aufabschlag",
        [
            pytest.param(
                AufAbschlag(
                    bezeichnung="foo",
                    beschreibung="bar",
                    auf_abschlagstyp=AufAbschlagstyp.ABSOLUT,
                    auf_abschlagsziel=AufAbschlagsziel.GESAMTPREIS,
                    einheit=Waehrungseinheit.EUR,
                    website="foo.bar",
                    gueltigkeitszeitraum=Zeitraum(),
                    staffeln=[Preisstaffel()],
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, aufabschlag: AufAbschlag) -> None:
        """
        Test de-/serialisation of AufAbschlag with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlag)
