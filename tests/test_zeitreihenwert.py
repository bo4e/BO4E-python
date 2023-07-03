from datetime import datetime, timezone
from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e.com.zeitreihenwert import Zeitreihenwert
from bo4e.enum.messwertstatus import Messwertstatus
from bo4e.enum.messwertstatuszusatz import Messwertstatuszusatz

example_zeitreihenwert = Zeitreihenwert(
    wert=Decimal(2.5),
    datum_uhrzeit_von=datetime(2001, 3, 15, tzinfo=timezone.utc),
    datum_uhrzeit_bis=datetime(2007, 11, 27, tzinfo=timezone.utc),
)


class TestZeitreihenwert:
    def test_zeitreihenwert_only_required_attributes(self) -> None:
        """
        Test de-/serialisation of Zeitreihenwert with minimal attributes.
        """
        zeitreihenwert = example_zeitreihenwert

        json_string = zeitreihenwert.model_dump_json(by_alias=True)

        assert "2001-03-15T00:00:00Z" in json_string
        assert "2007-11-27T00:00:00Z" in json_string

        zeitreihenwert_deserialized: Zeitreihenwert = Zeitreihenwert.model_validate_json(json_string)
        assert zeitreihenwert_deserialized == zeitreihenwert

    def test_zeitreihenwert_required_and_optional_attributes(self) -> None:
        """
        Test de-/serialisation of Zeitreihenwert with maximal attributes.
        """
        zeitreihenwert = Zeitreihenwert(
            datum_uhrzeit_von=datetime(2001, 3, 15, tzinfo=timezone.utc),
            datum_uhrzeit_bis=datetime(2007, 11, 27, tzinfo=timezone.utc),
            wert=Decimal(2.5),
            status=Messwertstatus.ABGELESEN,
            statuszusatz=Messwertstatuszusatz.Z78_GERAETEWECHSEL,
        )

        json_string = zeitreihenwert.model_dump_json(by_alias=True)

        assert "2.5" in json_string
        assert "2001-03-15T00:00:00Z" in json_string
        assert "2007-11-27T00:00:00Z" in json_string
        assert "ABGELESEN" in json_string
        assert "Z78_GERAETEWECHSEL" in json_string

        zeitreihenwert_deserialized: Zeitreihenwert = Zeitreihenwert.model_validate_json(json_string)
        assert zeitreihenwert_deserialized == zeitreihenwert

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Zeitreihenwert(datum_uhrzeit_von=datetime(2007, 11, 27, tzinfo=timezone.utc), wert=Decimal(1.5))  # type: ignore[call-arg]

        assert "1 validation error" in str(excinfo.value)

    def test_von_later_than_bis(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Zeitreihenwert(
                datum_uhrzeit_von=datetime(2007, 11, 27, tzinfo=timezone.utc),
                datum_uhrzeit_bis=datetime(2006, 11, 27, tzinfo=timezone.utc),
                wert=Decimal(1.5),
            )

        assert "start" in str(excinfo.value)
        assert "end" in str(excinfo.value)
