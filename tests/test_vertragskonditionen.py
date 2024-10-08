from datetime import date
from decimal import Decimal

import pytest

from bo4e import Vertragskonditionen, Zeitspanne
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
                        startdatum=date(2012, 9, 21),
                        enddatum=date(2013, 10, 11),
                    ),
                    kuendigungsfrist=Zeitspanne(),
                    vertragsverlaengerung=Zeitspanne(),
                    abschlagszyklus=Zeitspanne(),
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
