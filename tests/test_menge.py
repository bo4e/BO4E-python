from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e import Menge, Mengeneinheit
from tests.serialization_helper import assert_serialization_roundtrip


class TestMenge:
    @pytest.mark.parametrize(
        "menge",
        [
            pytest.param(
                Menge(wert=Decimal(3.41), einheit=Mengeneinheit.MWH),
            )
        ],
    )
    def test_serialization_roundtrip(self, menge: Menge) -> None:
        """
        Test de-/serialisation of Menge.
        """

        assert_serialization_roundtrip(menge)

    def test_wrong_datatype(self) -> None:
        """
        A string "3.14" would be casted to decimal from pydantic therefore no validation error would occure in this case.
        """
        with pytest.raises(ValidationError) as excinfo:
            _ = Menge(wert="hallo", einheit=Mengeneinheit.MWH)  # type: ignore[arg-type]

        assert "wert" in str(excinfo.value)
