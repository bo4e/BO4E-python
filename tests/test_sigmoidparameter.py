from decimal import Decimal

import pytest

from bo4e import Sigmoidparameter
from tests.serialization_helper import assert_serialization_roundtrip


class TestSigmoidparameter:
    @pytest.mark.parametrize(
        "sigmoidparameter",
        [
            pytest.param(
                Sigmoidparameter(
                    A=Decimal(1),
                    B=Decimal(2),
                    C=Decimal(3),
                    D=Decimal(4),
                ),
            ),
        ],
    )
    def test_sigmoidparameter_serialization_roundtrip(self, sigmoidparameter: Sigmoidparameter) -> None:
        """
        Test de-/serialisation of Sigmoidparameter with minimal attributes.
        """
        assert_serialization_roundtrip(sigmoidparameter)
