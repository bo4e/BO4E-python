from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e import TarifpreisstaffelProOrt
from tests.serialization_helper import assert_serialization_roundtrip

example_tarifpreisstaffelproort = TarifpreisstaffelProOrt(
    arbeitspreis=Decimal(10),
    arbeitspreis_n_t=Decimal(11),
    grundpreis=Decimal(12),
    staffelgrenze_von=Decimal(13),
    staffelgrenze_bis=Decimal(14),
)


class TestTarifpreisstaffelProOrt:
    @pytest.mark.parametrize(
        "tarifpreisstaffelproort",
        [
            pytest.param(
                example_tarifpreisstaffelproort,
                id="maximal (and minimal) attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifpreisstaffelproort: TarifpreisstaffelProOrt) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarifpreisstaffelproort)
