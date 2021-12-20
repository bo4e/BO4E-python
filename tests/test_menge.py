from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.menge import Menge, MengeSchema
from bo4e.enum.mengeneinheit import Mengeneinheit

example_menge = Menge(wert=Decimal(3.41), einheit=Mengeneinheit.MWH)


class TestMenge:
    def test_menge(self):
        """
        Test de-/serialisation of Menge (only has required attributes).
        """

        schema = MengeSchema()
        json_string = schema.dumps(example_menge, ensure_ascii=False)

        assert "3.41" in json_string
        assert "MWH" in json_string

        menge_deserialized = schema.loads(json_string)

        assert isinstance(menge_deserialized.wert, Decimal)
        assert menge_deserialized.wert == Decimal(3.41)
        assert isinstance(menge_deserialized.einheit, Mengeneinheit)
        assert menge_deserialized.einheit == Mengeneinheit.MWH

    def test_wrong_datatype(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Menge(wert="3.14", einheit=Mengeneinheit.MWH)

        assert "wert" in str(excinfo.value)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Menge(wert=Decimal(3.14))

        assert "missing 1 required" in str(excinfo.value)
