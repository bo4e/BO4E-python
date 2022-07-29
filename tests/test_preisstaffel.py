from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.preisstaffel import Preisstaffel
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_sigmoidparameter import example_sigmoidparameter

example_preisstaffel = Preisstaffel(
    einheitspreis=Decimal(40.0), staffelgrenze_von=Decimal(12.5), staffelgrenze_bis=Decimal(25.0)
)


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
                    "einheitspreis": Decimal("40"),
                    "sigmoidparameter": {"A": Decimal("1"), "B": Decimal("2"), "C": Decimal("3"), "D": Decimal("4")},
                    "staffelgrenzeVon": Decimal("12.5"),
                    "staffelgrenzeBis": Decimal("25"),
                },
                id="all attributes",
            ),
            pytest.param(
                example_preisstaffel,
                {
                    "einheitspreis": Decimal("40"),
                    "staffelgrenzeVon": Decimal("12.5"),
                    "staffelgrenzeBis": Decimal("25"),
                    "sigmoidparameter": None,
                },
                id="only required params",
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisstaffel: Preisstaffel, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of Preisstaffel.
        """
        assert_serialization_roundtrip(preisstaffel, expected_json_dict)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Preisstaffel()  # type: ignore[call-arg]

        assert "3 validation errors" in str(excinfo.value)

    @pytest.mark.parametrize(
        "not_a_sigmoid_parameter",
        [
            pytest.param(17),  # not a sigmoid parameter instance
            pytest.param("foo"),  # not a sigmoid parameter instance
        ],
    )
    def test_failing_validation(self, not_a_sigmoid_parameter: Any) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Preisstaffel(
                einheitspreis=Decimal(40.0),
                staffelgrenze_von=Decimal(12.5),
                staffelgrenze_bis=Decimal(25.0),
                sigmoidparameter=not_a_sigmoid_parameter,
            )

        assert "1 validation error" in str(excinfo.value)
        assert "sigmoidparameter" in str(excinfo.value)
