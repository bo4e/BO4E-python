from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from bo4e import Angebot, Angebotsvariante, Ansprechpartner, Geschaeftspartner, Geschaeftspartnerrolle, Sparte
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
                    angebotsgeber=Geschaeftspartner(),
                    angebotsnehmer=Geschaeftspartner(),
                    unterzeichner_angebotsnehmer=Ansprechpartner(),
                    unterzeichner_angebotsgeber=Ansprechpartner(),
                    varianten=[],
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, angebot: Angebot) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(angebot)
