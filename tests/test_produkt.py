import pytest

from bo4e import BoTyp, Produkt, Produkttyp, Tarif
from tests.serialization_helper import assert_serialization_roundtrip


class TestProdukt:
    @pytest.mark.parametrize(
        "produkt",
        [
            pytest.param(
                Produkt(
                    bezeichnung="Ökostrom Basis",
                    beschreibung="100% Ökostrom",
                    produkttyp=Produkttyp.TARIFPRODUKT,
                    tarif=Tarif(),
                    website="https://foo.inv",
                ),
                id="max attributes",
            ),
            pytest.param(Produkt(), id="min attributes"),
        ],
    )
    def test_serialization_roundtrip(self, produkt: Produkt) -> None:
        assert_serialization_roundtrip(produkt)

    def test_produkt_typ(self) -> None:
        assert Produkt().typ == BoTyp.PRODUKT
