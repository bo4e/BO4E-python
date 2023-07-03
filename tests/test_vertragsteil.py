from datetime import datetime, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e.com.menge import Menge
from bo4e.com.vertragsteil import Vertragsteil
from bo4e.enum.mengeneinheit import Mengeneinheit


class TestVertragsteil:
    def test_vertragsteil_only_required_attributes(self) -> None:
        """
        Test de-/serialisation of Vertragsteil with minimal attributes.
        """
        vertragsteil = Vertragsteil(
            vertragsteilbeginn=datetime(2001, 3, 15, tzinfo=timezone.utc),
            vertragsteilende=datetime(2007, 11, 27, tzinfo=timezone.utc),
        )

        json_string = vertragsteil.model_dump_json(by_alias=True)

        assert "2001-03-15T00:00:00Z" in json_string
        assert "2007-11-27T00:00:00Z" in json_string

        vertragsteil_deserialized = Vertragsteil.model_validate_json(json_string)

        assert isinstance(vertragsteil_deserialized.vertragsteilbeginn, datetime)
        assert vertragsteil_deserialized.vertragsteilbeginn == datetime(2001, 3, 15, tzinfo=timezone.utc)
        assert isinstance(vertragsteil_deserialized.vertragsteilende, datetime)
        assert vertragsteil_deserialized.vertragsteilende == datetime(2007, 11, 27, tzinfo=timezone.utc)

    def test_vertragsteil_required_and_optional_attributes(self) -> None:
        """
        Test de-/serialisation of Vertragsteil with maximal attributes.
        """
        vertragsteil = Vertragsteil(
            vertragsteilbeginn=datetime(2001, 3, 15, tzinfo=timezone.utc),
            vertragsteilende=datetime(2007, 11, 27, tzinfo=timezone.utc),
            lokation="Bar",
            vertraglich_fixierte_menge=Menge(wert=Decimal(3.1), einheit=Mengeneinheit.KWH),
            minimale_abnahmemenge=Menge(wert=Decimal(2000), einheit=Mengeneinheit.KWH),
            maximale_abnahmemenge=Menge(wert=Decimal(0.111111), einheit=Mengeneinheit.KWH),
        )

        json_string = vertragsteil.model_dump_json(by_alias=True)

        assert "2001-03-15T00:00:00Z" in json_string
        assert "2007-11-27T00:00:00Z" in json_string
        assert "Bar" in json_string
        assert "KWH" in json_string
        assert "0.111111" in json_string

        vertragsteil_deserialized = Vertragsteil.model_validate_json(json_string)

        assert isinstance(vertragsteil_deserialized.vertragsteilbeginn, datetime)
        assert vertragsteil_deserialized.vertragsteilbeginn == datetime(2001, 3, 15, tzinfo=timezone.utc)
        assert isinstance(vertragsteil_deserialized.vertragsteilende, datetime)
        assert vertragsteil_deserialized.vertragsteilende == datetime(2007, 11, 27, tzinfo=timezone.utc)
        assert isinstance(vertragsteil_deserialized.lokation, str)
        assert vertragsteil_deserialized.lokation == "Bar"
        assert isinstance(vertragsteil_deserialized.minimale_abnahmemenge, Menge)
        assert vertragsteil_deserialized.minimale_abnahmemenge == Menge(wert=Decimal(2000), einheit=Mengeneinheit.KWH)

    def test_vertragsteil_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Vertragsteil(vertragsteilende=datetime(2007, 11, 27, tzinfo=timezone.utc))  # type: ignore[call-arg]

        assert "1 validation error" in str(excinfo.value)
