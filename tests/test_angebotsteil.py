import pytest

from bo4e import Angebotsposition, Angebotsteil, Betrag, Marktlokation, Menge, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestAngebotsteil:
    @pytest.mark.parametrize(
        "angebotsteil",
        [
            pytest.param(
                Angebotsteil(
                    positionen=[Angebotsposition()],
                    anfrage_subreferenz="teststring",
                    lieferstellenangebotsteil=[Marktlokation()],
                    gesamtmengeangebotsteil=Menge(),
                    gesamtkostenangebotsteil=Betrag(),
                    lieferzeitraum=Zeitraum(),
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, angebotsteil: Angebotsteil) -> None:
        """
        Test de-/serialisation of Angebotsteil with minimal attributes.
        """
        assert_serialization_roundtrip(angebotsteil)
