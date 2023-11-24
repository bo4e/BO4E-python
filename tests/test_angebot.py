from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from bo4e import Angebot, Ansprechpartner, Geschaeftspartner, Geschaeftspartnerrolle, Sparte
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
                        ist_gewerbe=True,
                        geschaeftspartnerrolle=[Geschaeftspartnerrolle.LIEFERANT],
                        partneradresse=example_adresse,
                    ),
                    angebotsnehmer=Geschaeftspartner(
                        name1="Joker",
                        ist_gewerbe=False,
                        geschaeftspartnerrolle=[Geschaeftspartnerrolle.KUNDE],
                        partneradresse=example_adresse,
                    ),
                    unterzeichner_angebotsnehmer=Ansprechpartner(
                        nachname="Titans",
                        geschaeftspartner=Geschaeftspartner(
                            name1="Wonderwoman",
                            ist_gewerbe=False,
                            geschaeftspartnerrolle=[Geschaeftspartnerrolle.DIENSTLEISTER],
                            partneradresse=example_adresse,
                        ),
                    ),
                    unterzeichner_angebotsgeber=Ansprechpartner(
                        nachname="Titans",
                        geschaeftspartner=Geschaeftspartner(
                            name1="Robin",
                            ist_gewerbe=False,
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
                        ist_gewerbe=True,
                        geschaeftspartnerrolle=[Geschaeftspartnerrolle.LIEFERANT],
                        partneradresse=example_adresse,
                    ),
                    angebotsnehmer=Geschaeftspartner(
                        name1="Joker",
                        ist_gewerbe=False,
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
