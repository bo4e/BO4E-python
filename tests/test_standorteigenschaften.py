import pytest
from pydantic import ValidationError

from bo4e import Standorteigenschaften
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_standorteigenschaftengas import example_standorteigenschaften_gas
from tests.test_standorteigenschaftenstrom import example_standorteigenschaften_strom


class TestStandorteigenschaften:
    @pytest.mark.parametrize(
        "standorteigenschaften",
        [
            pytest.param(
                Standorteigenschaften(
                    eigenschaften_strom=[example_standorteigenschaften_strom],
                    eigenschaften_gas=example_standorteigenschaften_gas,
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, standorteigenschaften: Standorteigenschaften) -> None:
        assert_serialization_roundtrip(standorteigenschaften)
