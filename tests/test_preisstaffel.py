from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.preisstaffel import Preisstaffel, PreisstaffelSchema
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_sigmoidparameter import example_sigmoidparameter  # type:ignore[import]


class TestPreisstaffel:
    @pytest.mark.parametrize(
        "preisstaffel, expected_json_dict",
        [
            pytest.param(
                Preisstaffel(
                    einheitspreis=Decimal(40.0),
                    staffelgrenze_von=Decimal(12.5),
                    staffelgrenze_bis=Decimal(25.0),
                    sigmoidparameter=example_sigmoidparameter,
                ),
                {
                    "einheitspreis": "40",
                    "sigmoidparameter": {"a": "1", "b": "2", "c": "3", "d": "4"},
                    "staffelgrenzeVon": "12.5",
                    "staffelgrenzeBis": "25",
                },
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisstaffel: Preisstaffel, expected_json_dict: dict):
        """
        Test de-/serialisation of Preisstaffel.
        """
        assert_serialization_roundtrip(preisstaffel, PreisstaffelSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Preisstaffel()

        assert "missing 3 required" in str(excinfo.value)

    @pytest.mark.parametrize(
        "not_a_sigmoid_parameter",
        [
            pytest.param(17),  # not a sigmoid parameter instance
            pytest.param("foo"),  # not a sigmoid parameter instance
        ],
    )
    def test_failing_validation(self, not_a_sigmoid_parameter):
        with pytest.raises(TypeError) as excinfo:
            _ = Preisstaffel(
                einheitspreis=Decimal(40.0),
                staffelgrenze_von=Decimal(12.5),
                staffelgrenze_bis=Decimal(25.0),
                sigmoidparameter=not_a_sigmoid_parameter,
            )

        assert "'sigmoidparameter' must be " in str(excinfo.value)
