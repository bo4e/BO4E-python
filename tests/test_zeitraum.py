from decimal import Decimal

import pytest

from bo4e import Mengeneinheit, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestZeitraum:
    @pytest.mark.parametrize(
        "zeitraum",
        [
            pytest.param(
                Zeitraum(
                    einheit=Mengeneinheit.TAG,
                    dauer=Decimal(21),
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, zeitraum: Zeitraum) -> None:
        """
        Test de-/serialisation of Zeitraum.
        """
        assert_serialization_roundtrip(zeitraum)
