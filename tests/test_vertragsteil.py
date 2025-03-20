from datetime import datetime, timezone
from decimal import Decimal

import pytest

from bo4e import Menge, Mengeneinheit, Vertragsteil
from tests.serialization_helper import assert_serialization_roundtrip


class TestVertragsteil:
    @pytest.mark.parametrize(
        "vertragsteil",
        [
            pytest.param(
                Vertragsteil(
                    vertragsteilbeginn=datetime(2001, 3, 15, tzinfo=timezone.utc),
                    vertragsteilende=datetime(2007, 11, 27, tzinfo=timezone.utc),
                    lokation="Bar",
                    vertraglich_fixierte_menge=Menge(wert=Decimal(3.1), einheit=Mengeneinheit.KWH),
                    minimale_abnahmemenge=Menge(wert=Decimal(2000), einheit=Mengeneinheit.KWH),
                    maximale_abnahmemenge=Menge(wert=Decimal(0.111111), einheit=Mengeneinheit.KWH),
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, vertragsteil: Vertragsteil) -> None:
        """
        Test de-/serialisation of Vertragsteil.
        """
        assert_serialization_roundtrip(vertragsteil)
