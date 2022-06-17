import pytest  # type:ignore[import]
from pydantic import ValidationError
from bo4e.com.tarifpreispositionproort import TarifpreispositionProOrt, TarifpreispositionProOrt
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_tarifpreisstaffelproort import example_tarifpreisstaffelproort  # type:ignore[import]

example_tarifpreispositionproort = TarifpreispositionProOrt(
    postleitzahl="82031",
    ort="Grünwald",
    netznr="0815",
    preisstaffeln=[example_tarifpreisstaffelproort],
)


class TestTarifpreispositionProOrt:
    @pytest.mark.parametrize(
        "tarifpreispositionproort",
        [
            pytest.param(
                example_tarifpreispositionproort,
                id="minimal and maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifpreispositionproort: TarifpreispositionProOrt):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarifpreispositionproort)

    def test_missing_required_attribute(self):
        with pytest.raises(ValidationError) as excinfo:
            _ = TarifpreispositionProOrt()

        assert "4 validation errors" in str(excinfo.value)
