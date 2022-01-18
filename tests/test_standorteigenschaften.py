import pytest  # type:ignore[import]

from bo4e.bo.standorteigenschaften import Standorteigenschaften, StandorteigenschaftenSchema
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_standorteigenschaftenallgemein import example_standorteigenschaften_allgemein  # type:ignore[import]
from tests.test_standorteigenschaftengas import example_standorteigenschaften_gas  # type:ignore[import]
from tests.test_standorteigenschaftenstrom import example_standorteigenschaften_strom  # type:ignore[import]


class TestStandorteigenschaften:
    @pytest.mark.parametrize(
        "standorteigenschaften",
        [
            pytest.param(
                Standorteigenschaften(
                    eigenschaften_allgemein=example_standorteigenschaften_allgemein,
                    eigenschaften_strom=[example_standorteigenschaften_strom],
                    eigenschaften_gas=example_standorteigenschaften_gas,
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, standorteigenschaften: Standorteigenschaften):
        assert_serialization_roundtrip(standorteigenschaften, StandorteigenschaftenSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Standorteigenschaften()

        assert "missing 2 required" in str(excinfo.value)
