from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from bo4e.com.unterschrift import Unterschrift


class TestUnterschrift:
    def test_unterschrift_only_required_attributes(self) -> None:
        """
        Test de-/serialisation of Unterschrift with minimal attributes.
        """
        unterschrift = Unterschrift(name="Foo")

        json_string = unterschrift.json(by_alias=True, ensure_ascii=False)

        assert "Foo" in json_string

        unterschrift_deserialized = Unterschrift.parse_raw(json_string)

        assert isinstance(unterschrift_deserialized.name, str)
        assert unterschrift_deserialized.name == "Foo"

    def test_unterschrift_required_and_optional_attributes(self) -> None:
        """
        Test de-/serialisation of Unterschrift with maximal attributes.
        """
        unterschrift = Unterschrift(name="Foo", ort="Grünwald", datum=datetime(2019, 6, 7, tzinfo=timezone.utc))

        json_string = unterschrift.json(by_alias=True, ensure_ascii=False)

        assert "Foo" in json_string
        assert "Grünwald" in json_string
        assert "2019-06-07T00:00:00+00:00" in json_string

        unterschrift_deserialized = Unterschrift.parse_raw(json_string)

        assert isinstance(unterschrift_deserialized.name, str)
        assert unterschrift_deserialized.name == "Foo"
        assert isinstance(unterschrift_deserialized.ort, str)
        assert unterschrift_deserialized.ort == "Grünwald"
        assert isinstance(unterschrift_deserialized.datum, datetime)
        assert unterschrift_deserialized.datum == datetime(2019, 6, 7, tzinfo=timezone.utc)

    def test_unterschrift_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Unterschrift()  # type: ignore[call-arg]

        assert "1 validation error" in str(excinfo.value)
