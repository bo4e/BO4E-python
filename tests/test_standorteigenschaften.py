import pytest

from bo4e import Standorteigenschaften, StandorteigenschaftenGas, StandorteigenschaftenStrom
from tests.serialization_helper import assert_serialization_roundtrip


class TestStandorteigenschaften:
    @pytest.mark.parametrize(
        "standorteigenschaften",
        [
            pytest.param(
                Standorteigenschaften(
                    eigenschaften_strom=[StandorteigenschaftenStrom()],
                    eigenschaften_gas=StandorteigenschaftenGas(),
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, standorteigenschaften: Standorteigenschaften) -> None:
        """
        Test de-/serialisation of Sigmoidparameter with minimal attributes.
        """
        assert_serialization_roundtrip(standorteigenschaften)
