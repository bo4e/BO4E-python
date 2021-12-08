from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.betrag import Betrag, BetragSchema
from bo4e.enum.waehrungscode import Waehrungscode
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestBetrag:
    @pytest.mark.parametrize(
        "betrag, expected_json_dict",
        [
            pytest.param(
                Betrag(
                    waehrung=Waehrungscode.EUR,
                    wert=Decimal(12.5),
                ),
                {"wert": "12.5", "waehrung": "EUR"},
            ),
        ],
    )
    def test_regionskriterium_serialization_roundtrip(self, betrag: Betrag, expected_json_dict: dict):
        """
        Test de-/serialisation of Regionskriterium with minimal attributes.
        """
        assert_serialization_roundtrip(betrag, BetragSchema(), expected_json_dict)

    def test_regionskriterium_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Betrag()
        assert "missing 2 required" in str(excinfo.value)
