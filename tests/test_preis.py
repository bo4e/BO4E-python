from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.preis import Preis, PreisSchema
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.waehrungseinheit import Waehrungseinheit


class TestPreis:
    def test_preis_only_required(self):
        """
        Test de-/serialisation of Preis (only has required attributes).
        """
        preis = Preis(wert=Decimal(2.53), einheit=Waehrungseinheit.EUR, bezugswert=Mengeneinheit.KWH)

        schema = PreisSchema()
        json_string = schema.dumps(preis, ensure_ascii=False)

        assert "KWH" in json_string
        assert "EUR" in json_string
        assert "null" in json_string

        preis_deserialized = schema.loads(json_string)

        assert isinstance(preis_deserialized.wert, Decimal)
        assert isinstance(preis_deserialized.einheit, Waehrungseinheit)
        assert isinstance(preis_deserialized.bezugswert, Mengeneinheit)
        assert preis_deserialized.status is None
        assert preis == preis_deserialized

    def test_wrong_datatype(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Preis(wert=3.50, einheit=Waehrungseinheit.EUR, bezugswert=Mengeneinheit.KWH)

        assert "'wert' must be <class 'decimal.Decimal'>" in str(excinfo.value)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Preis(wert=Decimal(3.50), einheit=Waehrungseinheit.EUR, status=Preisstatus.ENDGUELTIG)

        assert "missing 1 required" in str(excinfo.value)

    def test_optional_attribute(self):
        preis = Preis(
            wert=Decimal(3.50),
            einheit=Waehrungseinheit.EUR,
            bezugswert=Mengeneinheit.KWH,
            status=Preisstatus.ENDGUELTIG,
        )

        schema = PreisSchema()
        json_string = schema.dumps(preis, ensure_ascii=False)

        assert "ENDGUELTIG" in json_string

        preis_deserialized = schema.loads(json_string)

        assert isinstance(preis_deserialized.status, Preisstatus)
