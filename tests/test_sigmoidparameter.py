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

    @pytest.mark.parametrize(
        "sigmoidparameter, leistung, expected_lp",
        [
            pytest.param(
                Sigmoidparameter(
                    A=Decimal(1),
                    B=Decimal(3),
                    C=Decimal(3),
                    D=Decimal(4),
                ),
                Decimal(3),
                Decimal(4.5),
            ),
        ],
    )
    def test_lp_calculation(self, sigmoidparameter: Sigmoidparameter, leistung: Decimal, expected_lp: Decimal) -> None:
        assert sigmoidparameter.calculate(leistung) == expected_lp
