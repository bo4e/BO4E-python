from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.angebotsposition import Angebotsposition, AngebotspositionSchema
from bo4e.com.betrag import Betrag
from bo4e.com.menge import Menge
from bo4e.com.preis import Preis
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.waehrungscode import Waehrungscode
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestAngebotsposition:
    @pytest.mark.parametrize(
        "ap, expected_json_dict",
        [
            pytest.param(
                Angebotsposition(
                    positionsmenge=Menge(wert=Decimal(4000), einheit=Mengeneinheit.KWH),
                    positionspreis=Preis(
                        wert=Decimal(0.2456), einheit=Waehrungseinheit.EUR, bezugswert=Mengeneinheit.KWH
                    ),
                    positionskosten=Betrag(
                        waehrung=Waehrungscode.EUR,
                        wert=Decimal(98240),
                    ),
                    positionsbezeichnung="Beispielangebotsposition",
                ),
                {
                    "positionsbezeichnung": "Beispielangebotsposition",
                    "positionsmenge": {"wert": "4000", "einheit": "KWH"},
                    "positionskosten": {"waehrung": "EUR", "wert": "98240"},
                    "positionspreis": {
                        "bezugswert": "KWH",
                        "status": None,
                        "wert": "0.2456000000000000127453603226967970840632915496826171875",
                        "einheit": "EUR",
                    },
                },
            ),
        ],
    )
    def test_serialization_roundtrip(self, ap: Angebotsposition, expected_json_dict: dict):
        """
        Test de-/serialisation of Regionskriterium with minimal attributes.
        """
        assert_serialization_roundtrip(ap, AngebotspositionSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Angebotsposition()
        assert "missing 2 required" in str(excinfo.value)
