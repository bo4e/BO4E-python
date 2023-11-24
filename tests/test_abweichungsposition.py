import pytest

from bo4e.com.abweichungsposition import Abweichungsposition
from tests.serialization_helper import assert_serialization_roundtrip


class TestAbweichungsposition:
    @pytest.mark.parametrize(
        "abweichungsposition",
        [
            pytest.param(
                Abweichungsposition(
                    abweichungsgrund_code="14",
                    abweichungsgrund_codeliste="G_0081",
                    abweichungsgrund_bemerkung="Umsatzsteuersatz",
                    zugehoerige_rechnung="458011",
                    zugehoerige_bestellung="foo",
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, abweichungsposition: Abweichungsposition) -> None:
        """
        Test de-/serialisation of Abweichungsposition.
        """
        assert_serialization_roundtrip(abweichungsposition)
