from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e import Geokoordinaten
from tests.serialization_helper import assert_serialization_roundtrip


class TestGeokoordinaten:
    @pytest.mark.parametrize(
        "geokoordinaten",
        [
            pytest.param(
                Geokoordinaten(
                    breitengrad=Decimal(52.52149200439453),
                    laengengrad=Decimal(13.404866218566895),
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, geokoordinaten: Geokoordinaten) -> None:
        assert_serialization_roundtrip(geokoordinaten)

    def test_wrong_datatype(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Geokoordinaten(breitengrad="54,23", laengengrad=-23.2)  # type: ignore[arg-type]

        assert "breitengrad" in str(excinfo.value)
