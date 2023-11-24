from datetime import datetime, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e import Messwertstatus, Messwertstatuszusatz, Zeitreihenwert, Zeitspanne,

example_zeitreihenwert = Zeitreihenwert(
    wert=Decimal(2.5),
    zeitspanne=Zeitspanne(
        start=datetime(2013, 5, 1, tzinfo=timezone.utc), ende=datetime(2022, 1, 28, tzinfo=timezone.utc)
    ),
)


class TestZeitreihenwert:
    def test_zeitreihenwert_only_required_attributes(self) -> None:
        """
        Test de-/serialisation of Zeitreihenwert with minimal attributes.
        """
        zeitreihenwert = example_zeitreihenwert

        json_string = zeitreihenwert.model_dump_json(by_alias=True)

        assert "2013-05-01T00:00:00Z" in json_string
        assert "2022-01-28T00:00:00Z" in json_string

        zeitreihenwert_deserialized: Zeitreihenwert = Zeitreihenwert.model_validate_json(json_string)
        assert zeitreihenwert_deserialized == zeitreihenwert

    def test_zeitreihenwert_required_and_optional_attributes(self) -> None:
        """
        Test de-/serialisation of Zeitreihenwert with maximal attributes.
        """
        zeitreihenwert = Zeitreihenwert(
            zeitspanne=Zeitspanne(
                start=datetime(2013, 5, 1, tzinfo=timezone.utc), ende=datetime(2022, 1, 28, tzinfo=timezone.utc)
            ),
            wert=Decimal(2.5),
            status=Messwertstatus.ABGELESEN,
            statuszusatz=Messwertstatuszusatz.Z78_GERAETEWECHSEL,
        )

        json_string = zeitreihenwert.model_dump_json(by_alias=True)

        assert "2.5" in json_string
        assert "ABGELESEN" in json_string
        assert "Z78_GERAETEWECHSEL" in json_string
        assert "2013-05-01T00:00:00Z" in json_string
        assert "2022-01-28T00:00:00Z" in json_string

        zeitreihenwert_deserialized: Zeitreihenwert = Zeitreihenwert.model_validate_json(json_string)
        assert zeitreihenwert_deserialized == zeitreihenwert

        assert isinstance(zeitreihenwert_deserialized.wert, Decimal)
        assert isinstance(zeitreihenwert_deserialized.status, Messwertstatus)
        assert isinstance(zeitreihenwert_deserialized.statuszusatz, Messwertstatuszusatz)

    def test_wrong_datatype(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Zeitreihenwert(wert="helloooo")  # type: ignore[arg-type]

        assert "wert" in str(excinfo.value)
