import pytest

from bo4e.com.abweichung import Abweichung
from bo4e.enum.abweichungsgrund import Abweichungsgrund
from tests.serialization_helper import assert_serialization_roundtrip


class Test_Abweichung:
    @pytest.mark.parametrize(
        "abweichung",
        [
            pytest.param(
                Abweichung(
                    abweichungsgrund=Abweichungsgrund.UNBEKANNTE_MARKTLOKATION_MESSLOKATION,
                    abweichungsgrund_bemerkung="sonst",
                    zugehoerige_rechnung="458011",
                    abschlagsrechnung="4580112",
                    abweichungsgrund_code="14",
                    abweichungsgrund_codeliste="G_0081",
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, abweichung: Abweichung) -> None:
        """
        Test de-/serialisation of Abweichung.
        """
        assert_serialization_roundtrip(abweichung)
