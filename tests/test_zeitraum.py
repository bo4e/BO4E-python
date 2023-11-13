from datetime import datetime, timezone
from decimal import Decimal
from typing import Dict

import pytest
from pydantic import ValidationError

from bo4e import Zeiteinheit, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestZeitraum:
    @pytest.mark.parametrize(
        "zeitraum",
        [
            pytest.param(
                Zeitraum(
                    einheit=Zeiteinheit.TAG,
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
