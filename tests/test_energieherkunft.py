from decimal import Decimal

import pytest

from bo4e import Energieherkunft, Erzeugungsart
from tests.serialization_helper import assert_serialization_roundtrip


class TestEnergieherkunft:
    @pytest.mark.parametrize(
        "energieherkunft",
        [
            pytest.param(
                Energieherkunft(
                    erzeugungsart=Erzeugungsart.BIOMASSE,
                    anteil_prozent=Decimal(25.5),
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(
        self,
        energieherkunft: Energieherkunft,
    ) -> None:
        """
        Test de-/serialisation of Energieherkunft with minimal attributes.
        """
        assert_serialization_roundtrip(energieherkunft)
