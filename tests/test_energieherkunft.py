from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.energieherkunft import Energieherkunft
from bo4e.enum.erzeugungsart import Erzeugungsart
from tests.serialization_helper import assert_serialization_roundtrip

# this can be imported by other tests
example_energieherkunft = Energieherkunft(erzeugungsart=Erzeugungsart.BIOMASSE, anteil_prozent=Decimal(25.5))


class TestEnergieherkunft:
    @pytest.mark.parametrize(
        "energieherkunft, expected_json_dict",
        [
            pytest.param(
                example_energieherkunft,
                {
                    "erzeugungsart": Erzeugungsart.BIOMASSE,
                    "anteilProzent": Decimal("25.5"),
                },
            ),
        ],
    )
    def test_energieherkunft_required_attributes(
        self, energieherkunft: Energieherkunft, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Energieherkunft with minimal attributes.
        """
        assert_serialization_roundtrip(energieherkunft, expected_json_dict)

    def test_energieherkunft_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Energieherkunft()  # type: ignore[call-arg]

        assert "2 validation errors" in str(excinfo.value)

    @pytest.mark.parametrize(
        "failing_percentage",
        [
            pytest.param(100.1),
            pytest.param(-2),
        ],
    )
    def test_energieherkunft_failing_validation(self, failing_percentage: float) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = (Energieherkunft(erzeugungsart=Erzeugungsart.BIOMASSE, anteil_prozent=Decimal(failing_percentage)),)

        assert "1 validation error" in str(excinfo.value)
        assert "should be less than 100" in str(excinfo.value) or "should be greater than 0" in str(excinfo.value)
