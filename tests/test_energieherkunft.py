from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.energieherkunft import Energieherkunft, EnergieherkunftSchema
from bo4e.enum.erzeugungsart import Erzeugungsart
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]

# this can be imported by other tests
example_energieherkunft = Energieherkunft(erzeugungsart=Erzeugungsart.BIOMASSE, anteil_prozent=Decimal(25.5))


class TestEnergieherkunft:
    @pytest.mark.parametrize(
        "energieherkunft, expected_json_dict",
        [
            pytest.param(
                example_energieherkunft,
                {
                    "erzeugungsart": "BIOMASSE",
                    "anteilProzent": "25.5",
                },
            ),
        ],
    )
    def test_energieherkunft_required_attributes(self, energieherkunft, expected_json_dict):
        """
        Test de-/serialisation of Energieherkunft with minimal attributes.
        """
        assert_serialization_roundtrip(energieherkunft, EnergieherkunftSchema(), expected_json_dict)

    def test_energieherkunft_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Energieherkunft()

        assert "missing 2 required" in str(excinfo.value)

    @pytest.mark.parametrize(
        "failing_percentage",
        [
            pytest.param(100.1),
            pytest.param(-2),
        ],
    )
    def test_energieherkunft_failing_validation(self, failing_percentage):
        with pytest.raises(ValueError) as excinfo:
            _ = (Energieherkunft(erzeugungsart=Erzeugungsart.BIOMASSE, anteil_prozent=Decimal(failing_percentage)),)

        assert "anteil_prozent must be between 0 and 100" in str(excinfo.value)
