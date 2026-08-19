from decimal import Decimal

import pytest

from bo4e import Menge, Mengeneinheit, Tarifeinschraenkung, Voraussetzungen, Zaehlertyp
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifeinschraenkung:
    @pytest.mark.parametrize(
        "tarifeinschraenkung",
        [
            pytest.param(
                Tarifeinschraenkung(
                    zusatzprodukte=["foo", "bar"],
                    voraussetzungen=[Voraussetzungen.ALTVERTRAG, Voraussetzungen.DIREKTVERTRIEB],
                    einschraenkungzaehler=[
                        Zaehlertyp.DREHSTROMZAEHLER,
                        Zaehlertyp.INTELLIGENTES_MESSSYSTEM,
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
