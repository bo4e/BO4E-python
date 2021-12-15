from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.sigmoidparameter import Sigmoidparameter, SigmoidparameterSchema
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]

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
                {"a": "1", "b": "2", "c": "3", "d": "4"},
            ),
        ],
    )
    def test_sigmoidparameter_serialization_roundtrip(
        self, sigmoidparameter: Sigmoidparameter, expected_json_dict: dict
    ):
        """
        Test de-/serialisation of Sigmoidparameter with minimal attributes.
        """
        assert_serialization_roundtrip(sigmoidparameter, SigmoidparameterSchema(), expected_json_dict)

    def test_sigmoidparameter_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Sigmoidparameter()
        assert "missing 4 required" in str(excinfo.value)

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
    def test_lp_calculation(self, sigmoidparameter: Sigmoidparameter, leistung: Decimal, expected_lp: Decimal):
        assert sigmoidparameter.calculate(leistung) == expected_lp
