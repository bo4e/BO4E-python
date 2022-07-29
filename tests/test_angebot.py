from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from bo4e.bo.angebot import Angebot
from bo4e.bo.ansprechpartner import Ansprechpartner
from bo4e.bo.geschaeftspartner import Geschaeftspartner
from bo4e.enum.geschaeftspartnerrolle import Geschaeftspartnerrolle
from bo4e.enum.sparte import Sparte
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_adresse import example_adresse
from tests.test_angebotsvariante import example_angebotsvariante


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
    def test_serialization_roundtrip(self, angebot: Angebot) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(angebot)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Angebot()  # type: ignore[call-arg]
        assert "6 validation errors" in str(excinfo.value)
