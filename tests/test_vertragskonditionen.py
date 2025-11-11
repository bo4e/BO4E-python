from datetime import datetime, timezone
from decimal import Decimal

import pytest

from bo4e import Mengeneinheit, Vertragskonditionen, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestVertragskonditionen:
    @pytest.mark.parametrize(
        "vertragskonditionen",
        [
            pytest.param(
                Vertragskonditionen(
                    beschreibung="Foobar",
                    anzahl_abschlaege=Decimal(3),
                    vertragslaufzeit=Zeitraum(
                        startdatum=datetime(2012, 9, 21, tzinfo=timezone.utc),
                        enddatum=datetime(2013, 10, 11, tzinfo=timezone.utc),
                    ),
                    kuendigungsfrist=Zeitraum(dauer="P3W"),
                    vertragsverlaengerung=Zeitraum(dauer="P14D"),
                    abschlagszyklus=Zeitraum(dauer="P5D"),
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
