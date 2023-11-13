from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Angebotsposition, Betrag, Menge, Mengeneinheit, Preis, Waehrungscode, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip


class TestAngebotsposition:
    @pytest.mark.parametrize(
        "ap",
        [
            pytest.param(
                Angebotsposition(
                    positionsmenge=Menge(),
                    positionspreis=Preis(),
                    positionskosten=Betrag(),
                    positionsbezeichnung="Beispielangebotsposition",
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, ap: Angebotsposition) -> None:
        """
        Test de-/serialisation of Regionskriterium with minimal attributes.
        """
        assert_serialization_roundtrip(ap)
