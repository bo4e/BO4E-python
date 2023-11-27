from decimal import Decimal

import pytest

from bo4e import Betrag, Waehrungscode
from tests.serialization_helper import assert_serialization_roundtrip


class TestBetrag:
    @pytest.mark.parametrize(
        "betrag",
        [
            pytest.param(
                Betrag(
                    waehrung=Waehrungscode.EUR,
                    wert=Decimal(12.5),
                ),
            ),
        ],
    )
    def test_regionskriterium_serialization_roundtrip(self, betrag: Betrag) -> None:
        """
        Test de-/serialisation of Regionskriterium with minimal attributes.
        """
        assert_serialization_roundtrip(betrag)
