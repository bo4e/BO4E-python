from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.energieherkunft import Energieherkunft, EnergieherkunftSchema
from bo4e.enum.erzeugungsart import Erzeugungsart

from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestEnergieherkunft:
    @pytest.mark.parametrize(
        "energieherkunft, expected_json_dict",
        [
            pytest.param(
                Energieherkunft(
                    erzeugungsart=Erzeugungsart.BIOMASSE,
                    anteil_prozent=Decimal(25.5)
                ),
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