from datetime import date
import pytest
from bo4e.com.unterschrift import Unterschrift, UnterschriftSchema


class TestUnterschrift:
    def test_unterschrift_only_required_attributes(self):
        """
        Test de-/serialisation of Unterschrift with minimal attributes.
        """
        unterschrift = Unterschrift(name="Foo")

        schema = UnterschriftSchema()
        json_string = schema.dumps(unterschrift, ensure_ascii=False)

        assert "Foo" in json_string

        unterschrift_deserialized = schema.loads(json_string)

        assert isinstance(unterschrift_deserialized.name, str)
        assert unterschrift_deserialized.name == "Foo"

    def test_unterschrift_required_and_optional_attributes(self):
        """
        Test de-/serialisation of Unterschrift with maximal attributes.
        """
        unterschrift = Unterschrift(name="Foo", ort="Grünwald", datum=date(2019, 6, 7))

        schema = UnterschriftSchema()
        json_string = schema.dumps(unterschrift, ensure_ascii=False)

        assert "Foo" in json_string
        assert "Grünwald" in json_string
        assert "2019-06-07" in json_string

        unterschrift_deserialized = schema.loads(json_string)

        assert isinstance(unterschrift_deserialized.name, str)
        assert unterschrift_deserialized.name == "Foo"
        assert isinstance(unterschrift_deserialized.ort, str)
        assert unterschrift_deserialized.ort == "Grünwald"
        assert isinstance(unterschrift_deserialized.datum, date)
        assert unterschrift_deserialized.datum == date(2019, 6, 7)

    def test_unterschrift_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Unterschrift()

        assert "missing 1 required" in str(excinfo.value)
