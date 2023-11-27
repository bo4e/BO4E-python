from decimal import Decimal

import pytest

from bo4e import TarifpreisstaffelProOrt
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifpreisstaffelProOrt:
    @pytest.mark.parametrize(
        "tarifpreisstaffelproort",
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
    def test_serialization_roundtrip(self, tarifpreisstaffelproort: TarifpreisstaffelProOrt) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarifpreisstaffelproort)
