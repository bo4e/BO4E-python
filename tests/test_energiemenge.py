import pytest
from pydantic import ValidationError

from bo4e.bo.energiemenge import Energiemenge
from bo4e.enum.lokationstyp import Lokationstyp
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_verbrauch import example_verbrauch


class TestEnergiemenge:
    @pytest.mark.parametrize(
        "energiemenge",
        [
            pytest.param(
                Energiemenge(
                    lokations_id="DE0123456789012345678901234567890",
                    lokationstyp=Lokationstyp.MELO,
                    energieverbrauch=[example_verbrauch],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, energiemenge: Energiemenge) -> None:
        assert_serialization_roundtrip(energiemenge)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Energiemenge()  # type: ignore[call-arg]

        assert "3 validation errors" in str(excinfo.value)
