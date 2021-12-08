from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.steuerbetrag import Steuerbetrag, SteuerbetragSchema
from bo4e.enum.steuerkennzeichen import Steuerkennzeichen
from bo4e.enum.waehrungscode import Waehrungscode
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestSteuerbetrag:
    @pytest.mark.parametrize(
        "steuerbetrag, expected_json_dict",
        [
            pytest.param(
                Steuerbetrag(
                    steuerkennzeichen=Steuerkennzeichen.UST_7,
                    basiswert=Decimal(100),
                    steuerwert=Decimal(19),
                    waehrung=Waehrungscode.EUR,
                ),
                {"steuerkennzeichen": "UST_7", "basiswert": "100", "steuerwert": "19", "waehrung": "EUR"},
            ),
        ],
    )
    def test_steuerbetrag_required_attributes(self, steuerbetrag, expected_json_dict):
        """
        Test de-/serialisation of Steuerbetrag with minimal attributes.
        """
        assert_serialization_roundtrip(steuerbetrag, SteuerbetragSchema(), expected_json_dict)

    def test_steuerbetrag_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Steuerbetrag()

        assert "missing 4 required" in str(excinfo.value)
