from datetime import datetime, timezone

import pytest

from bo4e import Unterschrift
from tests.serialization_helper import assert_serialization_roundtrip


class TestUnterschrift:
    @pytest.mark.parametrize(
        "unterschrift",
        [
            pytest.param(
                Unterschrift(
                    name="Foo",
                    ort="Grünwald",
                    datum=datetime(2019, 6, 7, tzinfo=timezone.utc),
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, unterschrift: Unterschrift) -> None:
        """
        Test de-/serialisation of Unterschrift.
        """
        assert_serialization_roundtrip(unterschrift)
