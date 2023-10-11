import pytest

from bo4e import Energiemenge, Lokationstyp, Verbrauch
from tests.serialization_helper import assert_serialization_roundtrip


class TestEnergiemenge:
    @pytest.mark.parametrize(
        "energiemenge",
        [
            pytest.param(
                Energiemenge(
                    lokations_id="DE0123456789012345678901234567890",
                    lokationstyp=Lokationstyp.MELO,
                    energieverbrauch=[Verbrauch()],
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, energiemenge: Energiemenge) -> None:
        assert_serialization_roundtrip(energiemenge)
