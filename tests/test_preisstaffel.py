from decimal import Decimal
from typing import Any

import pytest
from pydantic import ValidationError

from bo4e import Preisstaffel, Sigmoidparameter
from tests.serialization_helper import assert_serialization_roundtrip


class TestPreisstaffel:
    @pytest.mark.parametrize(
        "preisstaffel",
        [
            pytest.param(
                Preisstaffel(
                    einheitspreis=Decimal(40.0),
                    staffelgrenze_von=Decimal(12.5),
                    staffelgrenze_bis=Decimal(25.0),
                    sigmoidparameter=Sigmoidparameter(),
                ),
                id="all attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisstaffel: Preisstaffel) -> None:
        """
        Test de-/serialisation of Preisstaffel.
        """
        assert_serialization_roundtrip(preisstaffel)

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
