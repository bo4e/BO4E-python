from datetime import datetime, timezone
from decimal import Decimal

import pytest

from bo4e import Menge, Mengeneinheit, Vertragskonditionen, Zeitspanne
from tests.serialization_helper import assert_serialization_roundtrip


class TestVertragskonditionen:
    @pytest.mark.parametrize(
        "vertragskonditionen",
        [
            pytest.param(
                Vertragskonditionen(
                    beschreibung="Foobar",
                    anzahl_abschlaege=Decimal(3),
                    vertragslaufzeit=Zeitspanne(
                        start=datetime(2012, 9, 21, tzinfo=timezone.utc),
                        ende=datetime(2013, 10, 11, tzinfo=timezone.utc),
                    ),
                    kuendigungsfrist=Menge(einheit=Mengeneinheit.WOCHE, wert=Decimal(3)),
                    vertragsverlaengerung=Menge(einheit=Mengeneinheit.TAG, wert=Decimal(14)),
                    abschlagszyklus=Menge(einheit=Mengeneinheit.TAG, wert=Decimal(5)),
                ),
            ),
            pytest.param(
                Vertragskonditionen(),
            ),
        ],
    )
    def test_serialization_roundtrip(self, vertragskonditionen: Vertragskonditionen) -> None:
        """
        Test de-/serialisation of Vertragskonditionen.
        """
        assert_serialization_roundtrip(vertragskonditionen)
