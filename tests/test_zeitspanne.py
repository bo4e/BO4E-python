from datetime import datetime, timezone

from bo4e.com.zeitspanne import Zeitspanne


class TestZeitspanne:
    def test_zeitspanne(self) -> None:
        """
        Test de-/serialisation of Zeitspanne
        """
        zeitspanne = Zeitspanne(
            start=datetime(2013, 5, 1, tzinfo=timezone.utc), ende=datetime(2022, 1, 28, tzinfo=timezone.utc)
        )

        json_string = zeitspanne.model_dump_json(by_alias=True)

        assert "2013-05-01T00:00:00Z" in json_string
        assert "2022-01-28T00:00:00Z" in json_string

        zeitspanne_deserialized = Zeitspanne.model_validate_json(json_string)
        assert zeitspanne_deserialized == zeitspanne
