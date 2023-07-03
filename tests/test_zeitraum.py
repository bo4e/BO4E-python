from datetime import datetime, timezone
from decimal import Decimal
from typing import Dict

import pytest
from pydantic import ValidationError

from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.zeiteinheit import Zeiteinheit

example_zeitraum = Zeitraum(
    einheit=Zeiteinheit.TAG,
    dauer=Decimal(5),
)
example_zeitraum_dict = {
    "dauer": Decimal("5"),
    "startdatum": None,
    "endzeitpunkt": None,
    "einheit": Zeiteinheit.TAG,
    "enddatum": None,
    "startzeitpunkt": None,
}


class TestZeitraum:
    def test_zeitraum_dauer(self) -> None:
        """
        Test de-/serialisation of Zeitraum (only has optional attributes) with option dauer and einheit.
        """
        zeitraum = Zeitraum(einheit=Zeiteinheit.TAG, dauer=Decimal(21))

        json_string = zeitraum.model_dump_json(by_alias=True)

        assert "21" in json_string
        assert "TAG" in json_string

        zeitraum_deserialized = Zeitraum.model_validate_json(json_string)

        assert isinstance(zeitraum_deserialized.einheit, Zeiteinheit)
        assert zeitraum_deserialized.einheit == Zeiteinheit.TAG
        assert isinstance(zeitraum_deserialized.dauer, Decimal)
        assert zeitraum_deserialized.dauer == Decimal(21)

    def test_zeitraum_daten(self) -> None:
        """
        Test de-/serialisation of Zeitraum (only has optional attributes) with option startdatum and enddatum.
        """
        zeitraum = Zeitraum(
            startdatum=datetime(2013, 5, 1, tzinfo=timezone.utc), enddatum=datetime(2022, 1, 28, tzinfo=timezone.utc)
        )

        json_string = zeitraum.model_dump_json(by_alias=True)

        assert "2013-05-01T00:00:00Z" in json_string
        assert "2022-01-28T00:00:00Z" in json_string

        zeitraum_deserialized = Zeitraum.model_validate_json(json_string)

        assert isinstance(zeitraum_deserialized.startdatum, datetime)
        assert zeitraum_deserialized.startdatum == datetime(2013, 5, 1, tzinfo=timezone.utc)
        assert isinstance(zeitraum_deserialized.enddatum, datetime)
        assert zeitraum_deserialized.enddatum == datetime(2022, 1, 28, tzinfo=timezone.utc)

    def test_zeitraum_zeitpunkte(self) -> None:
        """
        Test de-/serialisation of Zeitraum (only has optional attributes) with option startzeitpunkt and endzeitpunkt.
        """
        zeitraum = Zeitraum(
            startzeitpunkt=datetime(2011, 2, 5, 16, 43, tzinfo=timezone.utc),
            endzeitpunkt=datetime(2021, 7, 30, tzinfo=timezone.utc),
        )

        json_string = zeitraum.model_dump_json(by_alias=True)

        assert "2011-02-05T16:43:00Z" in json_string
        assert "2021-07-30T00:00:00Z" in json_string

        zeitraum_deserialized = Zeitraum.model_validate_json(json_string)

        assert isinstance(zeitraum_deserialized.startzeitpunkt, datetime)
        assert zeitraum_deserialized.startzeitpunkt == datetime(2011, 2, 5, 16, 43, tzinfo=timezone.utc)
        assert isinstance(zeitraum_deserialized.endzeitpunkt, datetime)
        assert zeitraum_deserialized.endzeitpunkt == datetime(2021, 7, 30, tzinfo=timezone.utc)

    @pytest.mark.parametrize(
        "arguments",
        [
            pytest.param({"startdatum": datetime(2013, 5, 1, tzinfo=timezone.utc)}),
            pytest.param(
                {
                    "startdatum": datetime(2013, 5, 1, tzinfo=timezone.utc),
                    "startzeitpunkt": datetime(2011, 2, 5, 16, 43, tzinfo=timezone.utc),
                    "endzeitpunkt": datetime(2021, 7, 30, tzinfo=timezone.utc),
                }
            ),
            pytest.param({}),
            pytest.param(
                {
                    "startdatum": datetime(2013, 5, 1, tzinfo=timezone.utc),
                    "endzeitpunkt": datetime(2021, 7, 30, tzinfo=timezone.utc),
                }
            ),
        ],
    )
    def test_validator_time_range_possibilities(self, arguments: Dict[str, datetime]) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Zeitraum(**arguments)  # type: ignore[arg-type]
        assert "Please choose from one of the three possibilities to specify the timerange:" in str(excinfo.value)
