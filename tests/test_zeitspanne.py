from datetime import date, time

from bo4e.com.zeitspanne import Zeitspanne


class TestZeitspanne:

    def test_zeitspanne(self) -> None:
        """
        Test de-/serialisation of Zeitspanne
        """

        zeitspanne = Zeitspanne(
            startdatum=date(2013, 5, 1),  # date
            enddatum=date(2022, 1, 28),  # date
            startuhrzeit=time(12, 30),  # time
            enduhrzeit=time(15, 45),  # time
        )

        json_string = zeitspanne.model_dump_json(by_alias=True)

        assert "2013-05-01" in json_string
        assert "2022-01-28" in json_string
        assert "12:30:00" in json_string
        assert "15:45:00" in json_string

        zeitspanne_deserialized = Zeitspanne.model_validate_json(json_string)
        assert zeitspanne_deserialized == zeitspanne
