from datetime import datetime, timezone
from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.zeitraum import Zeitraum, ZeitraumSchema
from bo4e.enum.zeiteinheit import Zeiteinheit

example_zeitraum = Zeitraum(
    einheit=Zeiteinheit.TAG,
    dauer=Decimal(5),
)


class TestZeitraum:
    def test_zeitraum_dauer(self):
        """
        Test de-/serialisation of Zeitraum (only has optional attributes) with option dauer and einheit.
        """
        zeitraum = Zeitraum(einheit=Zeiteinheit.TAG, dauer=Decimal(21))

        schema = ZeitraumSchema()
        json_string = schema.dumps(zeitraum, ensure_ascii=False)

        assert "21" in json_string
        assert "TAG" in json_string

        zeitraum_deserialized = schema.loads(json_string)

        assert isinstance(zeitraum_deserialized.einheit, Zeiteinheit)
        assert zeitraum_deserialized.einheit == Zeiteinheit.TAG
        assert isinstance(zeitraum_deserialized.dauer, Decimal)
        assert zeitraum_deserialized.dauer == Decimal(21)

    def test_zeitraum_daten(self):
        """
        Test de-/serialisation of Zeitraum (only has optional attributes) with option startdatum and enddatum.
        """
        zeitraum = Zeitraum(
            startdatum=datetime(2013, 5, 1, tzinfo=timezone.utc), enddatum=datetime(2022, 1, 28, tzinfo=timezone.utc)
        )

        schema = ZeitraumSchema()
        json_string = schema.dumps(zeitraum, ensure_ascii=False)

        assert "2013-05-01T00:00:00+00:00" in json_string
        assert "2022-01-28T00:00:00+00:00" in json_string

        zeitraum_deserialized = schema.loads(json_string)

        assert isinstance(zeitraum_deserialized.startdatum, datetime)
        assert zeitraum_deserialized.startdatum == datetime(2013, 5, 1, tzinfo=timezone.utc)
        assert isinstance(zeitraum_deserialized.enddatum, datetime)
        assert zeitraum_deserialized.enddatum == datetime(2022, 1, 28, tzinfo=timezone.utc)

    def test_zeitraum_zeitpunkte(self):
        """
        Test de-/serialisation of Zeitraum (only has optional attributes) with option startzeitpunkt and endzeitpunkt.
        """
        zeitraum = Zeitraum(
            startzeitpunkt=datetime(2011, 2, 5, 16, 43, tzinfo=timezone.utc),
            endzeitpunkt=datetime(2021, 7, 30, tzinfo=timezone.utc),
        )

        schema = ZeitraumSchema()
        json_string = schema.dumps(zeitraum, ensure_ascii=False)

        assert "2011-02-05T16:43:00+00:00" in json_string
        assert "2021-07-30T00:00:00+00:00" in json_string

        zeitraum_deserialized = schema.loads(json_string)

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
    def test_validator_time_range_possibilities(self, arguments):
        with pytest.raises(ValueError) as excinfo:
            _ = Zeitraum(**arguments)
        assert """
        Please choose from one of the three possibilities to specify the timerange:
        - einheit and dauer
        - startdatum and enddatum
        - startzeitpunkt and endzeitpunkt
        """ in str(
            excinfo.value
        )
