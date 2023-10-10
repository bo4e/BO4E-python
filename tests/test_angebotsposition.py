from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Angebotsposition, Betrag, Menge, Mengeneinheit, Preis, Waehrungscode, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip


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
                    "positionsmenge": {"wert": Decimal("4000"), "einheit": Mengeneinheit.KWH, "_id": None},
                    "positionskosten": {"waehrung": Waehrungseinheit.EUR, "wert": Decimal("98240"), "_id": None},
                    "positionspreis": {
                        "bezugswert": Mengeneinheit.KWH,
                        "status": None,
                        "wert": Decimal("0.2456000000000000127453603226967970840632915496826171875"),
                        "einheit": Waehrungseinheit.EUR,
                        "_id": None,
                    },
                    "_id": None,
                },
            ),
        ],
    )
    def test_serialization_roundtrip(self, ap: Angebotsposition, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of Regionskriterium with minimal attributes.
        """
        assert_serialization_roundtrip(ap, expected_json_dict)
