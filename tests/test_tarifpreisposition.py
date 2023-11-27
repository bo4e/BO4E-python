from decimal import Decimal

import pytest

from bo4e import Mengeneinheit, Preisstaffel, Preistyp, Tarifpreisposition, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifpreisposition:
    @pytest.mark.parametrize(
        "tarifpreisposition",
        [
            pytest.param(
                Tarifpreisposition(
                    preistyp=Preistyp.ENTGELT_ABLESUNG,
                    einheit=Waehrungseinheit.EUR,
                    bezugseinheit=Mengeneinheit.KWH,
                    preisstaffeln=[
                        Preisstaffel(
                            einheitspreis=Decimal(40.0),
                            staffelgrenze_von=Decimal(12.5),
                            staffelgrenze_bis=Decimal(25.0),
                        ),
                    ],
                    mengeneinheitstaffel=Mengeneinheit.STUECK,
                ),
                id="optional and required attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifpreisposition: Tarifpreisposition) -> None:
        """
        Test de-/serialisation of Tarifpreisposition.
        """
        assert_serialization_roundtrip(tarifpreisposition)
