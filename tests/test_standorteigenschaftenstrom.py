from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.standorteigenschaftenstrom import StandorteigenschaftenStrom
from tests.serialization_helper import assert_serialization_roundtrip

example_standorteigenschaften_strom = StandorteigenschaftenStrom(
    regelzone="Transnet BW",
    bilanzierungsgebiet_eic="11YW-ALBSTADT--5",
    regelzone_eic="10YDE-ENBW-----N",
)


class TestStandorteigenschaftenStrom:
    @pytest.mark.parametrize(
        "standorteigenschaften_strom, expected_json_dict",
        [
            pytest.param(
                example_standorteigenschaften_strom,
                {
                    "regelzone": "Transnet BW",
                    "bilanzierungsgebietEic": "11YW-ALBSTADT--5",
                    "regelzoneEic": "10YDE-ENBW-----N",
                },
            )
        ],
    )
    def test_serialization_roundtrip(
        self, standorteigenschaften_strom: StandorteigenschaftenStrom, expected_json_dict: Dict[str, Any]
    ) -> None:
        assert_serialization_roundtrip(standorteigenschaften_strom, expected_json_dict)

    def test_missing_required_attributes(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = StandorteigenschaftenStrom()  # type: ignore[call-arg]

        assert "3 validation errors" in str(excinfo.value)
