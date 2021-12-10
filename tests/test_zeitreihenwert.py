from datetime import datetime, timezone
from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.zeitreihenwert import Zeitreihenwert, ZeitreihenwertSchema
from bo4e.enum.messwertstatus import Messwertstatus
from bo4e.enum.messwertstatuszusatz import Messwertstatuszusatz


class TestZeitreihenwert:
    def test_zeitreihenwert_only_required_attributes(self):
        """
        Test de-/serialisation of Zeitreihenwert with minimal attributes.
        """
        zeitreihenwert = Zeitreihenwert(
            wert=Decimal(2.5),
            datum_uhrzeit_von=datetime(2001, 3, 15, tzinfo=timezone.utc),
            datum_uhrzeit_bis=datetime(2007, 11, 27, tzinfo=timezone.utc),
        )

        schema = ZeitreihenwertSchema()
        json_string = schema.dumps(zeitreihenwert, ensure_ascii=False)

        assert "2001-03-15T00:00:00+00:00" in json_string
        assert "2007-11-27T00:00:00+00:00" in json_string

        zeitreihenwert_deserialized: Zeitreihenwert = schema.loads(json_string)
        assert zeitreihenwert_deserialized == zeitreihenwert

    def test_zeitreihenwert_required_and_optional_attributes(self):
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

        schema = ZeitreihenwertSchema()
        json_string = schema.dumps(zeitreihenwert, ensure_ascii=False)

        assert "2.5" in json_string
        assert "2001-03-15T00:00:00+00:00" in json_string
        assert "2007-11-27T00:00:00+00:00" in json_string
        assert "ABGELESEN" in json_string
        assert "Z78_GERAETEWECHSEL" in json_string

        zeitreihenwert_deserialized: Zeitreihenwert = schema.loads(json_string)
        assert zeitreihenwert_deserialized == zeitreihenwert

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Zeitreihenwert(datum_uhrzeit_von=datetime(2007, 11, 27, tzinfo=timezone.utc), wert=Decimal(1.5))

        assert "missing 1 required" in str(excinfo.value)

    def test_von_later_than_bis(self):
        with pytest.raises(ValueError) as excinfo:
            _ = Zeitreihenwert(
                datum_uhrzeit_von=datetime(2007, 11, 27, tzinfo=timezone.utc),
                datum_uhrzeit_bis=datetime(2006, 11, 27, tzinfo=timezone.utc),
                wert=Decimal(1.5),
            )

        assert ">=" in str(excinfo.value)
