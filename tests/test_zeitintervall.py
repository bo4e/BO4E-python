import pytest
from pydantic import ValidationError

from bo4e.com.zeitintervall import Zeitintervall
from bo4e.enum.zeiteinheit import Zeiteinheit


class TestZeitintervall:
    def test_zeitintervall_daten(self) -> None:
        """
        Test de-/serialisation of Zeitintervall (only has optional attributes) with option startdatum and enddatum.
        """
        zeitintervall = Zeitintervall(wert=2, zeiteinheit=Zeiteinheit.VIERTEL_STUNDE)

        json_string = zeitintervall.model_dump_json(by_alias=True)

        assert "2" in json_string
        assert "VIERTEL_STUNDE" in json_string

        zeitintervall_deserialized = Zeitintervall.model_validate_json(json_string)

        assert isinstance(zeitintervall_deserialized.wert, int)
        assert zeitintervall_deserialized.wert == 2
        assert isinstance(zeitintervall_deserialized.zeiteinheit, Zeiteinheit)
        assert zeitintervall_deserialized.zeiteinheit == Zeiteinheit.VIERTEL_STUNDE

    def test_wrong_datatype(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Zeitintervall(wert="errrrrror", zeiteinheit=Zeiteinheit.TAG)  # type: ignore[arg-type]

        assert "1 validation error" in str(excinfo.value)
        assert "wert" in str(excinfo.value)
        assert "should be a valid integer" in str(excinfo.value)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Zeitintervall(wert=3)  # type: ignore[call-arg]

        assert "1 validation error" in str(excinfo.value)
