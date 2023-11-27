from datetime import datetime

import pytest

from bo4e import ArithmetischeOperation, Messlokationszuordnung
from tests.serialization_helper import assert_serialization_roundtrip


class TestMesslokationszuordnung:
    @pytest.mark.parametrize(
        "messlokationszuordnung",
        [
            pytest.param(
                Messlokationszuordnung(
                    messlokations_id="DE0010688516810000000000000012345",
                    arithmetik=ArithmetischeOperation.ADDITION,
                    gueltig_seit=datetime(year=2021, month=1, day=13),
                    gueltig_bis=datetime(year=2021, month=5, day=4),
                )
            )
        ],
    )
    def test_serialization_roundtrip(self, messlokationszuordnung: Messlokationszuordnung) -> None:
        """
        Test de-/serialisation of Messlokationszuordnung.
        """

        assert_serialization_roundtrip(messlokationszuordnung)
