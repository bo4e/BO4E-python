from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Betrag, Waehrungscode, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip

example_betrag = Betrag(
    waehrung=Waehrungscode.EUR,
    wert=Decimal(12.5),
)

example_betrag_json = {"wert": Decimal("12.5"), "waehrung": Waehrungseinheit.EUR, "_id": None}


class TestBetrag:
    @pytest.mark.parametrize(
        "betrag, expected_json_dict",
        [
            pytest.param(example_betrag, example_betrag_json),
        ],
    )
    def test_regionskriterium_serialization_roundtrip(self, betrag: Betrag, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of Regionskriterium with minimal attributes.
        """
        assert_serialization_roundtrip(betrag, expected_json_dict)
