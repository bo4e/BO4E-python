from typing import Any, Dict, List

import pytest
from pydantic import ValidationError

from bo4e import MarktgebietInfo, StandorteigenschaftenGas
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
                    "marktgebiete": [{"marktgebiet": "Gaspool", "marktgebietcode": "37Z701133MH0000B", "_id": None}],
                    "_id": None,
                },
            )
        ],
    )
    def test_standorteigenschaftengas_serialization_roundtrip(
        self, standorteigenschaftengas: StandorteigenschaftenGas, expected_json_dict: Dict[str, Any]
    ) -> None:
        assert_serialization_roundtrip(standorteigenschaftengas, expected_json_dict)
