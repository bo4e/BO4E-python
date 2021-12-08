from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.tarifpreis import Tarifpreis, TarifpreisSchema
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.preistyp import Preistyp
from bo4e.enum.waehrungseinheit import Waehrungseinheit


class TestPreis:
    def test_tarifpreis_only_required(self):
        """
        Test de-/serialisation of Tarifpreis (only has required attributes).
        """
        tarifpreis = Tarifpreis(
            wert=Decimal(3.78),
            einheit=Waehrungseinheit.EUR,
            bezugswert=Mengeneinheit.KWH,
            preistyp=Preistyp.ARBEITSPREIS_HT,
        )

        schema = TarifpreisSchema()
        json_string = schema.dumps(tarifpreis, ensure_ascii=False)

        assert "ARBEITSPREIS_HT" in json_string
        assert "null" in json_string

        tarifpreis_deserialized = schema.loads(json_string)

        assert isinstance(tarifpreis_deserialized.wert, Decimal)
        assert isinstance(tarifpreis_deserialized.einheit, Waehrungseinheit)
        assert isinstance(tarifpreis_deserialized.bezugswert, Mengeneinheit)
        assert isinstance(tarifpreis_deserialized.preistyp, Preistyp)
        assert tarifpreis_deserialized.beschreibung is None
        assert tarifpreis == tarifpreis_deserialized

    def test_wrong_datatype(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Tarifpreis(
                wert=3.50, einheit=Waehrungseinheit.EUR, bezugswert=Mengeneinheit.KWH, preistyp=Preistyp.ARBEITSPREIS_HT
            )

        assert "'wert' must be <class 'decimal.Decimal'>" in str(excinfo.value)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Tarifpreis(
                wert=Decimal(3.50),
                einheit=Waehrungseinheit.EUR,
                status=Preisstatus.ENDGUELTIG,
                bezugswert=Mengeneinheit.KWH,
            )

        assert "missing 1 required" in str(excinfo.value)

    def test_optional_attribute(self):
        tarifpreis = Tarifpreis(
            wert=Decimal(3.50),
            einheit=Waehrungseinheit.EUR,
            bezugswert=Mengeneinheit.KWH,
            status=Preisstatus.ENDGUELTIG,
            preistyp=Preistyp.ARBEITSPREIS_HT,
            beschreibung="Das ist ein HT Arbeitspreis",
        )

        schema = TarifpreisSchema()
        json_string = schema.dumps(tarifpreis, ensure_ascii=False)

        assert "Das ist ein HT Arbeitspreis" in json_string

        tarifpreis_deserialized = schema.loads(json_string)

        assert isinstance(tarifpreis_deserialized.beschreibung, str)
        assert tarifpreis_deserialized.beschreibung == "Das ist ein HT Arbeitspreis"
        assert tarifpreis_deserialized == tarifpreis
