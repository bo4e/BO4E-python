from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Sigmoidparameter
from tests.serialization_helper import assert_serialization_roundtrip

# this sigmoid parameter can be imported by other tests
example_sigmoidparameter = Sigmoidparameter(
    A=Decimal(1),
    B=Decimal(2),
    C=Decimal(3),
    D=Decimal(4),
)


class TestSigmoidparameter:
    @pytest.mark.parametrize(
        "sigmoidparameter, expected_json_dict",
        [
            pytest.param(
                example_sigmoidparameter,
                {"A": Decimal("1"), "B": Decimal("2"), "C": Decimal("3"), "D": Decimal("4"), "_id": None},
            ),
        ],
    )
    def test_sigmoidparameter_serialization_roundtrip(
        self, sigmoidparameter: Sigmoidparameter, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Sigmoidparameter with minimal attributes.
        """
        assert_serialization_roundtrip(sigmoidparameter, expected_json_dict)

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
