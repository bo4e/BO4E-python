import pytest

from bo4e import MarktgebietInfo, StandorteigenschaftenGas
from tests.serialization_helper import assert_serialization_roundtrip

example_standorteigenschaften_gas = StandorteigenschaftenGas(
    netzkontonummern=["GASPOOLNH700xxxx"],
    marktgebiete=[MarktgebietInfo(marktgebiet="Gaspool", marktgebietcode="37Z701133MH0000B")],
)


class TestStandorteigenschaftenGas:
    @pytest.mark.parametrize(
        "standorteigenschaftengas",
        [
            pytest.param(
                StandorteigenschaftenGas(
                    netzkontonummern=["GASPOOLNH700xxxx"],
                    marktgebiete=[MarktgebietInfo(marktgebiet="Gaspool", marktgebietcode="37Z701133MH0000B")],
                ),
            )
        ],
    )
    def test_standorteigenschaftengas_serialization_roundtrip(
        self, standorteigenschaftengas: StandorteigenschaftenGas
    ) -> None:
        assert_serialization_roundtrip(standorteigenschaftengas)
