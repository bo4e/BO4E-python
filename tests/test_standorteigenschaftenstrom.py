from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import StandorteigenschaftenStrom
from tests.serialization_helper import assert_serialization_roundtrip

example_standorteigenschaften_strom = StandorteigenschaftenStrom(
    regelzone="Transnet BW",
    bilanzierungsgebiet_eic="11YW-ALBSTADT--5",
    regelzone_eic="10YDE-ENBW-----N",
)


class TestStandorteigenschaftenStrom:
    @pytest.mark.parametrize(
        "standorteigenschaften_strom",
        [
            pytest.param(
                example_standorteigenschaften_strom,
            )
        ],
    )
    def test_serialization_roundtrip(self, standorteigenschaften_strom: StandorteigenschaftenStrom) -> None:
        assert_serialization_roundtrip(standorteigenschaften_strom)
