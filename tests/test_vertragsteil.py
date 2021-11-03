from datetime import datetime, timezone
from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.menge import Menge
from bo4e.com.vertragsteil import Vertragsteil, VertragsteilSchema
from bo4e.enum.mengeneinheit import Mengeneinheit


class TestVertragsteil:
    def test_vertragsteil_only_required_attributes(self):
        """
        Test de-/serialisation of Vertragsteil with minimal attributes.
        """
        vertragsteil = Vertragsteil(
            vertragsteilbeginn=datetime(2001, 3, 15, tzinfo=timezone.utc),
            vertragsteilende=datetime(2007, 11, 27, tzinfo=timezone.utc),
        )

        schema = VertragsteilSchema()
        json_string = schema.dumps(vertragsteil, ensure_ascii=False)

        assert "2001-03-15T00:00:00+00:00" in json_string
        assert "2007-11-27T00:00:00+00:00" in json_string

        vertragsteil_deserialized = schema.loads(json_string)

        assert isinstance(vertragsteil_deserialized.vertragsteilbeginn, datetime)
        assert vertragsteil_deserialized.vertragsteilbeginn == datetime(2001, 3, 15, tzinfo=timezone.utc)
        assert isinstance(vertragsteil_deserialized.vertragsteilende, datetime)
        assert vertragsteil_deserialized.vertragsteilende == datetime(2007, 11, 27, tzinfo=timezone.utc)

    def test_vertragsteil_required_and_optional_attributes(self):
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

        schema = VertragsteilSchema()
        json_string = schema.dumps(vertragsteil, ensure_ascii=False)

        assert "2001-03-15T00:00:00+00:00" in json_string
        assert "2007-11-27T00:00:00+00:00" in json_string
        assert "Bar" in json_string
        assert "KWH" in json_string
        assert "0.111111" in json_string

        vertragsteil_deserialized = schema.loads(json_string)

        assert isinstance(vertragsteil_deserialized.vertragsteilbeginn, datetime)
        assert vertragsteil_deserialized.vertragsteilbeginn == datetime(2001, 3, 15, tzinfo=timezone.utc)
        assert isinstance(vertragsteil_deserialized.vertragsteilende, datetime)
        assert vertragsteil_deserialized.vertragsteilende == datetime(2007, 11, 27, tzinfo=timezone.utc)
        assert isinstance(vertragsteil_deserialized.lokation, str)
        assert vertragsteil_deserialized.lokation == "Bar"
        assert isinstance(vertragsteil_deserialized.minimale_abnahmemenge, Menge)
        assert vertragsteil_deserialized.minimale_abnahmemenge == Menge(wert=Decimal(2000), einheit=Mengeneinheit.KWH)

    def test_vertragsteil_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Vertragsteil(vertragsteilende=datetime(2007, 11, 27, tzinfo=timezone.utc))

        assert "missing 1 required" in str(excinfo.value)
