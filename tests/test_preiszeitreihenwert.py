import pytest

from bo4e import (
    Menge,
    Preis,
    Preiszeitreihenwert,
    Zeitraum
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestPreiszeitreihenwert:
    @pytest.mark.parametrize(
        "preiszeitreihenwert",
        [
            pytest.param(
                Preiszeitreihenwert(
                    zeitraum=Zeitraum(),
                    preis=Preis(),
                    menge=Menge(),
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preiszeitreihenwert: Preiszeitreihenwert) -> None:
        """
        Test de-/serialisation of Preiszeitreihenwert
        """
        assert_serialization_roundtrip(preiszeitreihenwert)
