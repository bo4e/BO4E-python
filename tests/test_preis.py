from decimal import Decimal

import pytest  # type:ignore[import]
from pydantic import ValidationError
from bo4e.com.preis import Preis, Preis
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.waehrungseinheit import Waehrungseinheit

example_preis = Preis(wert=Decimal(12.5), einheit=Waehrungseinheit.EUR, bezugswert=Mengeneinheit.KWH)


class TestPreis:
    def test_preis_only_required(self):
        """
        Test de-/serialisation of Preis (only has required attributes).
        """
        preis = example_preis

        json_string = preis.json(by_alias=True, ensure_ascii=False)

        assert "KWH" in json_string
        assert "EUR" in json_string
        assert "null" in json_string

        preis_deserialized = Preis.parse_raw(json_string)

        assert isinstance(preis_deserialized.wert, Decimal)
        assert isinstance(preis_deserialized.einheit, Waehrungseinheit)
        assert isinstance(preis_deserialized.bezugswert, Mengeneinheit)
        assert preis_deserialized.status is None
        assert preis == preis_deserialized

    def test_wrong_datatype(self):
        with pytest.raises(ValidationError) as excinfo:
            _ = Preis(wert=3.50, einheit=Waehrungseinheit.EUR, bezugswert=Mengeneinheit.KWH)

        assert "'wert' must be <class 'decimal.Decimal'>" in str(excinfo.value)

    def test_missing_required_attribute(self):
        with pytest.raises(ValidationError) as excinfo:
            _ = Preis(wert=Decimal(3.50), einheit=Waehrungseinheit.EUR, status=Preisstatus.ENDGUELTIG)

        assert "1 validation error" in str(excinfo.value)

    def test_optional_attribute(self):
        preis = Preis(
            wert=Decimal(3.50),
            einheit=Waehrungseinheit.EUR,
            bezugswert=Mengeneinheit.KWH,
            status=Preisstatus.ENDGUELTIG,
        )

        json_string = preis.json(by_alias=True, ensure_ascii=False)

        assert "ENDGUELTIG" in json_string

        preis_deserialized = Preis.parse_raw(json_string)

        assert isinstance(preis_deserialized.status, Preisstatus)
