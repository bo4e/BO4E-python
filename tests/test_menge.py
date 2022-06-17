from decimal import Decimal

import pytest  # type:ignore[import]
from pydantic import ValidationError
from bo4e.com.menge import Menge, Menge
from bo4e.enum.mengeneinheit import Mengeneinheit

example_menge = Menge(wert=Decimal(3.41), einheit=Mengeneinheit.MWH)
# see issue https://github.com/Hochfrequenz/BO4E-python/issues/249
example_menge_dict = {"wert": Decimal("3.410000000000000142108547152020037174224853515625"), "einheit": "MWH"}


class TestMenge:
    def test_menge(self):
        """
        Test de-/serialisation of Menge (only has required attributes).
        """

        json_string = example_menge.json(by_alias=True, ensure_ascii=False)

        assert "3.41" in json_string
        assert "MWH" in json_string

        menge_deserialized = Menge.parse_raw(json_string)

        assert isinstance(menge_deserialized.wert, Decimal)
        assert menge_deserialized.wert == Decimal(3.41)
        assert isinstance(menge_deserialized.einheit, Mengeneinheit)
        assert menge_deserialized.einheit == Mengeneinheit.MWH.value

    def test_wrong_datatype(self):
        """
        A string "3.14" would be casted to decimal from pydantic therefore no validation error would occure in this case.
        """
        with pytest.raises(ValidationError) as excinfo:
            _ = Menge(wert="hallo", einheit=Mengeneinheit.MWH)

        assert "wert" in str(excinfo.value)

    def test_missing_required_attribute(self):
        with pytest.raises(ValidationError) as excinfo:
            _ = Menge(wert=Decimal(3.14))

        assert "1 validation error" in str(excinfo.value)
