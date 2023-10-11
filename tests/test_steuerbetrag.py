from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Steuerbetrag, Steuerkennzeichen, Waehrungscode, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip

example_steuerbetrag = Steuerbetrag(
    steuerkennzeichen=Steuerkennzeichen.UST_7,
    basiswert=Decimal(100),
    steuerwert=Decimal(19),
    waehrung=Waehrungscode.EUR,
)


class TestSteuerbetrag:
    @pytest.mark.parametrize(
        "steuerbetrag",
        [
            pytest.param(
                example_steuerbetrag,
            ),
        ],
    )
    def test_steuerbetrag_required_attributes(self, steuerbetrag: Steuerbetrag) -> None:
        """
        Test de-/serialisation of Steuerbetrag with minimal attributes.
        """
        assert_serialization_roundtrip(steuerbetrag)
