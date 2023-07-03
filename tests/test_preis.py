from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e.com.preis import Preis
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.waehrungseinheit import Waehrungseinheit

example_preis = Preis(wert=Decimal(12.5), einheit=Waehrungseinheit.EUR, bezugswert=Mengeneinheit.KWH)


class TestPreis:
    def test_preis_only_required(self) -> None:
        """
        Test de-/serialisation of Preis (only has required attributes).
        """
        preis = example_preis

        json_string = preis.model_dump_json(by_alias=True)

        assert "KWH" in json_string
        assert "EUR" in json_string
        assert "null" in json_string

        preis_deserialized = Preis.model_validate_json(json_string)

        assert isinstance(preis_deserialized.wert, Decimal)
        assert isinstance(preis_deserialized.einheit, Waehrungseinheit)
        assert isinstance(preis_deserialized.bezugswert, Mengeneinheit)
        assert preis_deserialized.status is None
        assert preis == preis_deserialized

    def test_wrong_datatype(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Preis(wert="lululululu", einheit=Waehrungseinheit.EUR, bezugswert=Mengeneinheit.KWH)  # type: ignore[arg-type]

        assert "1 validation error" in str(excinfo.value)
        assert "wert" in str(excinfo.value)
        assert "type=decimal_parsing" in str(excinfo.value)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Preis(wert=Decimal(3.50), einheit=Waehrungseinheit.EUR, status=Preisstatus.ENDGUELTIG)  # type: ignore[call-arg]

        assert "1 validation error" in str(excinfo.value)

    def test_optional_attribute(self) -> None:
        preis = Preis(
            wert=Decimal(3.50),
            einheit=Waehrungseinheit.EUR,
            bezugswert=Mengeneinheit.KWH,
            status=Preisstatus.ENDGUELTIG,
        )

        json_string = preis.model_dump_json(by_alias=True)

        assert "ENDGUELTIG" in json_string

        preis_deserialized = Preis.model_validate_json(json_string)

        assert isinstance(preis_deserialized.status, Preisstatus)
