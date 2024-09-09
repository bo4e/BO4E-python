from datetime import time, timezone

import pytest

from bo4e.com.zeitfenster import Zeitfenster
from tests.serialization_helper import assert_serialization_roundtrip


class TestZeitfenster:
    @pytest.mark.parametrize(
        "zeitfenster",
        [
            pytest.param(
                Zeitfenster(
                    startzeit=time(8, 00, tzinfo=timezone.utc),
                    endzeit=time(17, 00, tzinfo=timezone.utc),
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, zeitfenster: Zeitfenster) -> None:
        """
        Test de-/serialisation of Zeitfenster.
        """
        assert_serialization_roundtrip(zeitfenster)
