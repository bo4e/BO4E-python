from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.sigmoidparameter import Sigmoidparameter
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
                {"A": Decimal("1"), "B": Decimal("2"), "C": Decimal("3"), "D": Decimal("4")},
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

    def test_sigmoidparameter_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Sigmoidparameter()  # type: ignore[call-arg]
        assert "4 validation errors" in str(excinfo.value)

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
