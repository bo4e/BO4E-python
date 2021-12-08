import pytest
from bo4e.com.marktgebietinfo import MarktgebietInfo

from bo4e.com.standorteigenschaftengas import StandorteigenschaftenGas, StandorteigenschaftenGasSchema
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestStandorteigenschaftenGas:
    @pytest.mark.parametrize(
        "standorteigenschaftengas, expected_json_dict",
        [
            pytest.param(
                StandorteigenschaftenGas(
                    netzkontonummern=["GASPOOLNH700xxxx"],
                    marktgebiete=[MarktgebietInfo(marktgebiet="Gaspool", marktgebietcode="37Z701133MH0000B")],
                ),
                {
                    "netzkontonummern": ["GASPOOLNH700xxxx"],
                    "marktgebiete": [{"marktgebiet": "Gaspool", "marktgebietcode": "37Z701133MH0000B"}],
                },
            )
        ],
    )
    def test_standorteigenschaftengas_serialization_roundtrip(
        self, standorteigenschaftengas: StandorteigenschaftenGas, expected_json_dict: dict
    ):
        assert_serialization_roundtrip(standorteigenschaftengas, StandorteigenschaftenGasSchema(), expected_json_dict)

    def test_standorteigenschaftengas_missing_required_attributes(self):
        with pytest.raises(TypeError) as excinfo:
            _ = StandorteigenschaftenGas()

        assert "missing 2 required" in str(excinfo.value)
