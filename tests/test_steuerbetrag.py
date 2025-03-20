from decimal import Decimal

import pytest

from bo4e import Steuerbetrag, Steuerkennzeichen, Waehrungscode
from tests.serialization_helper import assert_serialization_roundtrip


class TestSteuerbetrag:
    @pytest.mark.parametrize(
        "steuerbetrag",
        [
            pytest.param(
                Steuerbetrag(
                    steuerkennzeichen=Steuerkennzeichen.UST_7,
                    basiswert=Decimal(100),
                    steuerwert=Decimal(19),
                    waehrung=Waehrungscode.EUR,
                ),
            ),
        ],
    )
    def test_steuerbetrag_required_attributes(self, steuerbetrag: Steuerbetrag) -> None:
        """
        Test de-/serialisation of Steuerbetrag with minimal attributes.
        """
        assert_serialization_roundtrip(steuerbetrag)
