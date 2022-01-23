from datetime import datetime, timezone

import pytest  # type:ignore[import]

from bo4e.bo.angebot import Angebot, AngebotSchema
from bo4e.bo.ansprechpartner import Ansprechpartner
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.sparte import Sparte
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_adresse import example_adresse  # type:ignore[import]
from tests.test_angebotsvariante import example_angebotsvariante  # type:ignore[import]


class TestAngebot:
    @pytest.mark.parametrize(
        "angebot",
        [
            pytest.param(
                Angebot(
                    angebotsnummer="271828",
                    anfragereferenz="foo",
                    angebotsdatum=datetime(2020, 1, 1, tzinfo=timezone.utc),
                    sparte=Sparte.GAS,
                    bindefrist=datetime(2019, 3, 2, tzinfo=timezone.utc),
                    angebotsgeber=Geschaeftspartner(
                        name1="Batman",
                        gewerbekennzeichnung=True,
                        geschaeftspartnerrolle=[Geschaeftspartnerrolle.LIEFERANT],
                        partneradresse=example_adresse,
                    ),
                    angebotsnehmer=Geschaeftspartner(
                        name1="Joker",
                        gewerbekennzeichnung=False,
                        geschaeftspartnerrolle=[Geschaeftspartnerrolle.KUNDE],
                        partneradresse=example_adresse,
                    ),
                    unterzeichner_angebotsnehmer=Ansprechpartner(
                        nachname="Titans",
                        geschaeftspartner=Geschaeftspartner(
                            name1="Wonderwoman",
                            gewerbekennzeichnung=False,
                            geschaeftspartnerrolle=[Geschaeftspartnerrolle.DIENSTLEISTER],
                            partneradresse=example_adresse,
                        ),
                    ),
                    unterzeichner_angebotsgeber=Ansprechpartner(
                        nachname="Titans",
                        geschaeftspartner=Geschaeftspartner(
                            name1="Robin",
                            gewerbekennzeichnung=False,
                            geschaeftspartnerrolle=[Geschaeftspartnerrolle.KUNDE],
                            partneradresse=example_adresse,
                        ),
                    ),
                    varianten=[example_angebotsvariante],
                ),
                id="required and optional attributes",
            ),
            pytest.param(
                Angebot(
                    angebotsnummer="271828",
                    angebotsdatum=datetime(2020, 1, 1, tzinfo=timezone.utc),
                    sparte=Sparte.GAS,
                    angebotsgeber=Geschaeftspartner(
                        name1="Batman",
                        gewerbekennzeichnung=True,
                        geschaeftspartnerrolle=[Geschaeftspartnerrolle.LIEFERANT],
                        partneradresse=example_adresse,
                    ),
                    angebotsnehmer=Geschaeftspartner(
                        name1="Joker",
                        gewerbekennzeichnung=False,
                        geschaeftspartnerrolle=[Geschaeftspartnerrolle.KUNDE],
                        partneradresse=example_adresse,
                    ),
                    varianten=[example_angebotsvariante],
                ),
                id="required attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, angebot: Angebot):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(angebot, AngebotSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Angebot()
        assert "missing 6 required" in str(excinfo.value)
