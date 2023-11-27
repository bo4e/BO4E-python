from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e import Mengeneinheit, Preis, Preisstatus, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip


class TestPreis:
    def test_wrong_datatype(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Preis(wert="lululululu", einheit=Waehrungseinheit.EUR, bezugswert=Mengeneinheit.KWH)  # type: ignore[arg-type]

        assert "1 validation error" in str(excinfo.value)
        assert "wert" in str(excinfo.value)
        assert "type=decimal_parsing" in str(excinfo.value)

    @pytest.mark.parametrize(
        "preis",
        [
            pytest.param(
                Preis(
                    wert=Decimal(3.50),
                    einheit=Waehrungseinheit.EUR,
                    bezugswert=Mengeneinheit.KWH,
                    status=Preisstatus.ENDGUELTIG,
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, preis: Preis) -> None:
        """
        Test de-/serialisation of Preis.
        """
        assert_serialization_roundtrip(preis)
