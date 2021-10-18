from datetime import datetime, timezone
from decimal import Decimal

from bo4e.com.vertragskonditionen import Vertragskonditionen, VertragskonditionenSchema
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.zeiteinheit import Zeiteinheit


class TestVertragskonditionen:
    def test_vertragskonditionen_with_optional_attributes(self):
        """
        Test de-/serialisation of Vertragskonditionen (only has optional attributes).
        """
        vertragskonditionen = Vertragskonditionen(
            beschreibung="Foobar",
            anzahl_abschlaege=Decimal(3),
            vertragslaufzeit=Zeitraum(
                startdatum=datetime(2012, 9, 21, tzinfo=timezone.utc),
                enddatum=datetime(2013, 10, 11, tzinfo=timezone.utc),
            ),
            kuendigungsfrist=Zeitraum(einheit=Zeiteinheit.WOCHE, dauer=Decimal(3)),
            vertragsverlaengerung=Zeitraum(einheit=Zeiteinheit.TAG, dauer=Decimal(14)),
            abschlagszyklus=Zeitraum(einheit=Zeiteinheit.TAG, dauer=Decimal(5)),
        )

        schema = VertragskonditionenSchema()
        json_string = schema.dumps(vertragskonditionen, ensure_ascii=False)

        assert "Foobar" in json_string
        assert "3" in json_string
        assert "2013-10-11T00:00:00+00:00" in json_string
        assert "WOCHE" in json_string
        assert "TAG" in json_string
        assert "14" in json_string

        vertragskonditionen_deserialized = schema.loads(json_string)

        assert isinstance(vertragskonditionen_deserialized.beschreibung, str)
        assert vertragskonditionen_deserialized.beschreibung == "Foobar"
        assert isinstance(vertragskonditionen_deserialized.anzahl_abschlaege, Decimal)
        assert vertragskonditionen_deserialized.anzahl_abschlaege == Decimal(3)
        assert isinstance(vertragskonditionen_deserialized.vertragslaufzeit, Zeitraum)
        assert vertragskonditionen_deserialized.vertragslaufzeit == Zeitraum(
            startdatum=datetime(2012, 9, 21, tzinfo=timezone.utc), enddatum=datetime(2013, 10, 11, tzinfo=timezone.utc)
        )
        assert isinstance(vertragskonditionen_deserialized.vertragsverlaengerung, Zeitraum)
        assert vertragskonditionen_deserialized.vertragsverlaengerung == Zeitraum(
            einheit=Zeiteinheit.TAG, dauer=Decimal(14)
        )

    def test_vertragskonditionen_empty(self):
        """
        Test empty Vertragskonditionen (only has optional attributes).
        """
        empty_vertragskonditionen = Vertragskonditionen()

        assert isinstance(empty_vertragskonditionen, Vertragskonditionen)
