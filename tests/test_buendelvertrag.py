import pytest  # type:ignore[import]
from pydantic import ValidationError
from bo4e.bo.buendelvertrag import Buendelvertrag, Buendelvertrag
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
        assert_serialization_roundtrip(buendelvertrag)

    def test_missing_required_attribute(self):
        with pytest.raises(ValidationError) as excinfo:
            _ = Buendelvertrag()

        assert "1 validation error" in str(excinfo.value)
