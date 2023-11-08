from datetime import datetime, timezone
from decimal import Decimal

import pytest

from bo4e import Vertragskonditionen, Zeiteinheit, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip

example_vertragskonditionen = Vertragskonditionen(
    beschreibung="Foobar",
    anzahl_abschlaege=Decimal(3),
    vertragslaufzeit=Zeitraum(
        startdatum=datetime(2012, 9, 21, tzinfo=timezone.utc),
        enddatum=datetime(2013, 10, 11, tzinfo=timezone.utc),
    ),
    kuendigungsfrist=Zeitraum(einheit=Zeiteinheit.WOCHE, dauer=Decimal(3)),
    vertragsverlaengerung=Zeitraum(einheit=Zeiteinheit.TAG, dauer=Decimal(14)),
    abschlagszyklus=Zeitraum(einheit=Zeiteinheit.TAG, dauer=Decimal(5)),
)


class TestVertragskonditionen:
    @pytest.mark.parametrize(
        "vertragskonditionen",
        [
            pytest.param(
                Vertragskonditionen(
                    example_vertragskonditionen,
                ),
            ),
            pytest.param(
                Vertragskonditionen(
                    Vertragskonditionen(),
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, vertragskonditionen: Vertragskonditionen) -> None:
        """
        Test de-/serialisation of Vertragskonditionen.
        """
        assert_serialization_roundtrip(vertragskonditionen)
