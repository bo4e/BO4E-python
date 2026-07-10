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
                    anzahl_abschlaege=3,
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
