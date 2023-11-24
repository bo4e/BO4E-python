from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Steuerbetrag, Steuerkennzeichen, Waehrungscode, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip

example_steuerbetrag = Steuerbetrag(
    steuerkennzeichen=Steuerkennzeichen.UST_7,
    basiswert=Decimal(100),
    steuerwert=Decimal(19),
    waehrung=Waehrungscode.EUR,
)


class TestSteuerbetrag:
    @pytest.mark.parametrize(
        "steuerbetrag, expected_json_dict",
        [
            pytest.param(
                example_steuerbetrag,
                {
                    "steuerkennzeichen": "UST_7",
                    "basiswert": Decimal("100"),
                    "steuerwert": Decimal("19"),
                    "waehrung": Waehrungseinheit.EUR,
                    "_id": None,
                },
            ),
        ],
    )
    def test_steuerbetrag_required_attributes(
        self, steuerbetrag: Steuerbetrag, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Steuerbetrag with minimal attributes.
        """
        assert_serialization_roundtrip(steuerbetrag, expected_json_dict)
