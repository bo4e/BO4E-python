from datetime import datetime, timezone

import pytest

from bo4e import Angebotsstatus, Angebotsteil, Angebotsvariante, Betrag, Menge
from tests.serialization_helper import assert_serialization_roundtrip


class TestAngebotsvariante:
    @pytest.mark.parametrize(
        "angebotsvariante",
        [
            pytest.param(
                Angebotsvariante(
                    angebotsstatus=Angebotsstatus.NACHGEFASST,
                    bindefrist=datetime(2022, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                    erstellungsdatum=datetime(2021, 12, 22, 0, 0, 0, tzinfo=timezone.utc),
                    teile=[Angebotsteil()],
                    gesamtmenge=Menge(),
                    gesamtkosten=Betrag(),
                ),
                id="all attributes at first level",  # = min + menge and betrag
            ),
        ],
    )
    def test_serialization_roundtrip(self, angebotsvariante: Angebotsvariante) -> None:
        """
        Test de-/serialisation roundtrip.
        """
        assert_serialization_roundtrip(angebotsvariante)
