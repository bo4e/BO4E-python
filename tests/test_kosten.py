import pytest

from bo4e import Betrag, Kosten, Kostenblock, Kostenklasse, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestKosten:
    @pytest.mark.parametrize(
        "kosten",
        [
            pytest.param(
                Kosten(
                    kostenklasse=Kostenklasse.FREMDKOSTEN,
                    gueltigkeit=Zeitraum(),
                    kostenbloecke=[Kostenblock()],
                    summe_kosten=[Betrag()],
                ),
                id="all attributes at first level",
            )
        ],
    )
    def test_serialization_roundtrip(self, kosten: Kosten) -> None:
        """
        Test de-/serialisation of Kosten.
        """
        assert_serialization_roundtrip(kosten)
