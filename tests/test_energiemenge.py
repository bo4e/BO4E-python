import pytest

from bo4e import Energiemenge, Menge, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestEnergiemenge:
    @pytest.mark.parametrize(
        "energiemenge",
        [
            pytest.param(
                Energiemenge(
                    obis_kennzahl="1-0:1.8.1",
                    beschreibung="Eine Beschreibung",
                    zeitraum=Zeitraum(),
                    menge=Menge(),
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, energiemenge: Energiemenge) -> None:
        assert_serialization_roundtrip(energiemenge)
