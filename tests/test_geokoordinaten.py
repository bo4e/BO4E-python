from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e.com.geokoordinaten import Geokoordinaten


class TestGeokoordinaten:
    def test_serialization(self) -> None:
        geo = Geokoordinaten(
            breitengrad=Decimal(52.52149200439453),
            laengengrad=Decimal(13.404866218566895),
        )

        json_string = geo.json(by_alias=True, ensure_ascii=False)

        assert "breitengrad" in json_string
        assert str(geo.breitengrad) in json_string

        deserialized_geo: Geokoordinaten = Geokoordinaten.parse_raw(json_string)

        assert isinstance(deserialized_geo.breitengrad, Decimal)
        assert isinstance(deserialized_geo.laengengrad, Decimal)
        assert geo.breitengrad == deserialized_geo.breitengrad

    def test_wrong_datatype(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Geokoordinaten(breitengrad="54,23", laengengrad=-23.2)  # type: ignore[arg-type]

        assert "breitengrad" in str(excinfo.value)
