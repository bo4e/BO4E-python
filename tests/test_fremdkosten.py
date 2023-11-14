import pytest

from bo4e import Betrag, Fremdkosten, Fremdkostenblock, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestFremdkosten:
    @pytest.mark.parametrize(
        "fremdkosten",
        [
            pytest.param(
                Fremdkosten(
                    gueltigkeit=Zeitraum(),
                    summe_kosten=Betrag(),
                    kostenbloecke=[Fremdkostenblock()],
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, fremdkosten: Fremdkosten) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(fremdkosten)
