from typing import Any, Dict, List

import pytest
from pydantic import ValidationError

from bo4e.com.marktgebietinfo import MarktgebietInfo
from bo4e.com.standorteigenschaftengas import StandorteigenschaftenGas
from tests.serialization_helper import assert_serialization_roundtrip

example_standorteigenschaften_gas = StandorteigenschaftenGas(
    netzkontonummern=["GASPOOLNH700xxxx"],
    marktgebiete=[MarktgebietInfo(marktgebiet="Gaspool", marktgebietcode="37Z701133MH0000B")],
)


class TestStandorteigenschaftenGas:
    @pytest.mark.parametrize(
        "standorteigenschaftengas, expected_json_dict",
        [
            pytest.param(
                example_standorteigenschaften_gas,
                {
                    "netzkontonummern": ["GASPOOLNH700xxxx"],
                    "marktgebiete": [{"marktgebiet": "Gaspool", "marktgebietcode": "37Z701133MH0000B"}],
                },
            )
        ],
    )
    def test_standorteigenschaftengas_serialization_roundtrip(
        self, standorteigenschaftengas: StandorteigenschaftenGas, expected_json_dict: Dict[str, Any]
    ) -> None:
        assert_serialization_roundtrip(standorteigenschaftengas, expected_json_dict)

    def test_standorteigenschaftengas_missing_required_attributes(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = StandorteigenschaftenGas()  # type: ignore[call-arg]

        assert "2 validation errors" in str(excinfo.value)

    @pytest.mark.parametrize(
        "wrong_netzkontonummern, expected_error_message",
        [
            pytest.param(
                [],
                "too_short",
            ),
            pytest.param(
                ["1", "2", "3"],
                "should have at most 2 items",
            ),
        ],
    )
    def test_standorteigenschaftengas_list_lenght_validation(
        self, wrong_netzkontonummern: List[str], expected_error_message: str
    ) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = StandorteigenschaftenGas(
                netzkontonummern=wrong_netzkontonummern,
                marktgebiete=[MarktgebietInfo(marktgebiet="Gaspool", marktgebietcode="37Z701133MH0000B")],
            )
        assert expected_error_message in str(excinfo.value)
