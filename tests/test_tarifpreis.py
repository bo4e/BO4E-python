from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e.com.tarifpreis import Tarifpreis
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.preistyp import Preistyp
from bo4e.enum.waehrungseinheit import Waehrungseinheit

example_tarifpreis = Tarifpreis(
    wert=Decimal(12.5),
    einheit=Waehrungseinheit.EUR,
    bezugswert=Mengeneinheit.KWH,
    preistyp=Preistyp.ARBEITSPREIS_HT,
)


class TestTarifpreis:
    def test_tarifpreis_only_required(self) -> None:
        """
        Test de-/serialisation of Tarifpreis (only has required attributes).
        """
        tarifpreis = example_tarifpreis

        json_string = tarifpreis.model_dump_json(by_alias=True)

        assert "ARBEITSPREIS_HT" in json_string
        assert "null" in json_string

        tarifpreis_deserialized = Tarifpreis.model_validate_json(json_string)

        assert isinstance(tarifpreis_deserialized.wert, Decimal)
        assert isinstance(tarifpreis_deserialized.einheit, Waehrungseinheit)
        assert isinstance(tarifpreis_deserialized.bezugswert, Mengeneinheit)
        assert isinstance(tarifpreis_deserialized.preistyp, Preistyp)
        assert tarifpreis_deserialized.beschreibung is None
        assert tarifpreis == tarifpreis_deserialized

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
        assert "should be a valid decimal" in str(excinfo.value)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Tarifpreis(  # type: ignore[call-arg]
                wert=Decimal(3.50),
                einheit=Waehrungseinheit.EUR,
                status=Preisstatus.ENDGUELTIG,
                bezugswert=Mengeneinheit.KWH,
            )

        assert "1 validation error" in str(excinfo.value)

    def test_optional_attribute(self) -> None:
        tarifpreis = Tarifpreis(
            wert=Decimal(3.50),
            einheit=Waehrungseinheit.EUR,
            bezugswert=Mengeneinheit.KWH,
            status=Preisstatus.ENDGUELTIG,
            preistyp=Preistyp.ARBEITSPREIS_HT,
            beschreibung="Das ist ein HT Arbeitspreis",
        )

        json_string = tarifpreis.model_dump_json(by_alias=True)

        assert "Das ist ein HT Arbeitspreis" in json_string

        tarifpreis_deserialized = Tarifpreis.model_validate_json(json_string)

        assert isinstance(tarifpreis_deserialized.beschreibung, str)
        assert tarifpreis_deserialized.beschreibung == "Das ist ein HT Arbeitspreis"
        assert tarifpreis_deserialized == tarifpreis
