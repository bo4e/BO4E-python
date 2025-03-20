import pytest

from bo4e import TarifpreispositionProOrt, TarifpreisstaffelProOrt
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifpreispositionProOrt:
    @pytest.mark.parametrize(
        "tarifpreispositionproort",
        [
            pytest.param(
                TarifpreispositionProOrt(
                    postleitzahl="82031",
                    ort="Grünwald",
                    netznr="0815",
                    preisstaffeln=[TarifpreisstaffelProOrt()],
                ),
                id="minimal and maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifpreispositionproort: TarifpreispositionProOrt) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarifpreispositionproort)
