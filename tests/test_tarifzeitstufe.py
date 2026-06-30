from datetime import date

import pytest

from bo4e import Tarifzeitstufe, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifzeitstufe:
    @pytest.mark.parametrize(
        "tarifzeitstufe",
        [
            pytest.param(
                Tarifzeitstufe(
                    zeitraum=Zeitraum(),
                    tarifstufe="HT",
                ),
                id="all attributes at first level",
            )
        ],
    )
    def test_serialization_roundtrip(self, tarifzeitstufe: Tarifzeitstufe) -> None:
        """
        Test de-/serialisation of Tarifzeitstufe.
        """
        assert_serialization_roundtrip(tarifzeitstufe)
