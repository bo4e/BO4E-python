from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Energieherkunft, Erzeugungsart
from tests.serialization_helper import assert_serialization_roundtrip

# this can be imported by other tests
example_energieherkunft = Energieherkunft(erzeugungsart=Erzeugungsart.BIOMASSE, anteil_prozent=Decimal(25.5))


class TestEnergieherkunft:
    @pytest.mark.parametrize(
        "energieherkunft",
        [
            pytest.param(example_energieherkunft),
        ],
    )
    def test_energieherkunft_required_attributes(
        self,
        energieherkunft: Energieherkunft,
    ) -> None:
        """
        Test de-/serialisation of Energieherkunft with minimal attributes.
        """
        assert_serialization_roundtrip(energieherkunft)
