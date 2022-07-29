from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.steuerbetrag import Steuerbetrag
from bo4e.enum.steuerkennzeichen import Steuerkennzeichen
from bo4e.enum.waehrungscode import Waehrungscode
from bo4e.enum.waehrungseinheit import Waehrungseinheit
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

    def test_steuerbetrag_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Steuerbetrag()  # type: ignore[call-arg]

        assert "4 validation errors" in str(excinfo.value)
