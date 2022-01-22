from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.tarifpreisstaffelproort import TarifpreisstaffelProOrt, TarifpreisstaffelProOrtSchema
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestTarifpreisstaffelProOrt:
    @pytest.mark.parametrize(
        "tarifpreisstaffel",
        [
            pytest.param(
                TarifpreisstaffelProOrt(
                    arbeitspreis=Decimal(10),
                    arbeitspreis_n_t=Decimal(11),
                    grundpreis=Decimal(12),
                    staffelgrenze_von=Decimal(13),
                    staffelgrenze_bis=Decimal(14),
                ),
                id="maximal (and minimal) attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifpreisstaffel: TarifpreisstaffelProOrt):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarifpreisstaffel, TarifpreisstaffelProOrtSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = TarifpreisstaffelProOrt()

        assert "missing 5 required" in str(excinfo.value)