from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e import Mengeneinheit, Preisstatus, Preistyp, Tarifpreis, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip


class TestTarifpreis:
    def test_wrong_datatype(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Tarifpreis(
                wert="blubb",  # type: ignore[arg-type]
                einheit=Waehrungseinheit.EUR,
                bezugswert=Mengeneinheit.KWH,
                preistyp=Preistyp.ARBEITSPREIS_HT,
            )

        assert "1 validation error" in str(excinfo.value)
        assert "wert" in str(excinfo.value)
        assert "type=decimal_parsing" in str(excinfo.value)

    @pytest.mark.parametrize(
        "tarifpreis",
        [
            pytest.param(
                Tarifpreis(
                    wert=Decimal(3.50),
                    einheit=Waehrungseinheit.EUR,
                    bezugswert=Mengeneinheit.KWH,
                    status=Preisstatus.ENDGUELTIG,
                    preistyp=Preistyp.ARBEITSPREIS_HT,
                    beschreibung="Das ist ein HT Arbeitspreis",
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifpreis: Tarifpreis) -> None:
        """
        Test de-/serialisation of Tarifpreis.
        """
        assert_serialization_roundtrip(tarifpreis)
