import pytest

from bo4e import MarktgebietInfo
from tests.serialization_helper import assert_serialization_roundtrip


class TestMarktgebietinfo:
    @pytest.mark.parametrize(
        "marktgebietinfo",
        [
            pytest.param(
                MarktgebietInfo(marktgebiet="Gaspool", marktgebietcode="37Z701133MH0000B"),
            ),
        ],
    )
    def test_serialization(self, marktgebietinfo: MarktgebietInfo) -> None:
        """
        Test de-/serialisation of Marktgebietinfo.
        """

        assert_serialization_roundtrip(marktgebietinfo)
