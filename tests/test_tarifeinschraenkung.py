from decimal import Decimal

import pytest

from bo4e import Geraet, Menge, Mengeneinheit, Tarifeinschraenkung, Voraussetzungen
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_geraet import example_geraet


class TestTarifeinschraenkung:
    @pytest.mark.parametrize(
        "tarifeinschraenkung",
        [
            pytest.param(
                Tarifeinschraenkung(
                    zusatzprodukte=["foo", "bar"],
                    voraussetzungen=[Voraussetzungen.ALTVERTRAG, Voraussetzungen.DIREKTVERTRIEB],
                    einschraenkungzaehler=[
                        example_geraet,
                        Geraet(geraetenummer="197foo"),
                    ],
                    einschraenkungleistung=[
                        Menge(wert=Decimal(12.5), einheit=Mengeneinheit.MWH),
                        Menge(wert=Decimal(30), einheit=Mengeneinheit.KWH),
                    ],
                ),
                id="maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifeinschraenkung: Tarifeinschraenkung) -> None:
        """
        Test de-/serialisation of Tarifeinschraenkung
        """
        assert_serialization_roundtrip(tarifeinschraenkung)
