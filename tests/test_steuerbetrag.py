from decimal import Decimal

import pytest

from bo4e import Steuerart, Steuerbetrag, Waehrungscode
from tests.serialization_helper import assert_serialization_roundtrip


class TestSteuerbetrag:
    @pytest.mark.parametrize(
        "steuerbetrag",
        [
            pytest.param(
                Steuerbetrag(
                    steuerart=Steuerart.UST,
                    steuersatz=Decimal(7),
                    basiswert=Decimal(100),
                    steuerwert=Decimal(19),
                    waehrungscode=Waehrungscode.EUR,
                ),
            ),
        ],
    )
    def test_steuerbetrag_required_attributes(self, steuerbetrag: Steuerbetrag) -> None:
        """
        Test de-/serialisation of Steuerbetrag with minimal attributes.
        """
        assert_serialization_roundtrip(steuerbetrag)
