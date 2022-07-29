import pytest
from pydantic import ValidationError

from bo4e.bo.buendelvertrag import Buendelvertrag
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_vertrag import TestVertrag


class TestBuendelvertrag:
    @pytest.mark.parametrize(
        "buendelvertrag",
        [
            pytest.param(Buendelvertrag(einzelvertraege=[TestVertrag().get_example_vertrag()])),
        ],
    )
    def test_serialization_roundtrip(self, buendelvertrag: Buendelvertrag) -> None:
        assert_serialization_roundtrip(buendelvertrag)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Buendelvertrag()  # type: ignore[call-arg]

        assert "1 validation error" in str(excinfo.value)
