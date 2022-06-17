from decimal import Decimal

import pytest  # type:ignore[import]
from pydantic import ValidationError
from bo4e.com.steuerbetrag import Steuerbetrag
from bo4e.enum.steuerkennzeichen import Steuerkennzeichen
from bo4e.enum.waehrungscode import Waehrungscode
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]

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
                    "waehrung": "EUR",
                },
            ),
        ],
    )
    def test_steuerbetrag_required_attributes(self, steuerbetrag, expected_json_dict):
        """
        Test de-/serialisation of Steuerbetrag with minimal attributes.
        """
        assert_serialization_roundtrip(steuerbetrag, expected_json_dict)

    def test_steuerbetrag_missing_required_attribute(self):
        with pytest.raises(ValidationError) as excinfo:
            _ = Steuerbetrag()

        assert "4 validation errors" in str(excinfo.value)
