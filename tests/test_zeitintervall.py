from datetime import datetime, timezone
from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.zeitintervall import Zeitintervall, ZeitintervallSchema
from bo4e.enum.zeiteinheit import Zeiteinheit


class TestZeitintervall:
    def test_zeitintervall_daten(self):
        """
        Test de-/serialisation of Zeitintervall (only has optional attributes) with option startdatum and enddatum.
        """
        zeitintervall = Zeitintervall(wert=2, zeiteinheit=Zeiteinheit.VIERTEL_STUNDE)

        schema = ZeitintervallSchema()
        json_string = schema.dumps(zeitintervall, ensure_ascii=False)

        assert "2" in json_string
        assert "VIERTEL_STUNDE" in json_string

        zeitintervall_deserialized = schema.loads(json_string)

        assert isinstance(zeitintervall_deserialized.wert, int)
        assert zeitintervall_deserialized.wert == 2
        assert isinstance(zeitintervall_deserialized.zeiteinheit, Zeiteinheit)
        assert zeitintervall_deserialized.zeiteinheit == Zeiteinheit.VIERTEL_STUNDE.value

    def test_wrong_datatype(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Zeitintervall(wert="3", zeiteinheit=Zeiteinheit.TAG)

        assert "'wert' must be <class 'int'>" in str(excinfo.value)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Zeitintervall(wert=3)

        assert "missing 1 required keyword" in str(excinfo.value)
