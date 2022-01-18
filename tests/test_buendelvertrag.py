import pytest  # type:ignore[import]

from bo4e.bo.buendelvertrag import Buendelvertrag, BuendelvertragSchema
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_vertrag import TestVertrag  # type:ignore[import]


class TestBuendelvertrag:
    @pytest.mark.parametrize(
        "buendelvertrag",
        [
            pytest.param(Buendelvertrag(einzelvertraege=[TestVertrag().get_example_vertrag()])),
        ],
    )
    def test_serialization_roundtrip(self, buendelvertrag: Buendelvertrag):
        assert_serialization_roundtrip(buendelvertrag, BuendelvertragSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Buendelvertrag()

        assert "missing 1 required" in str(excinfo.value)
