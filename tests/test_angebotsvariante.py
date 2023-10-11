from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Angebotsstatus, Angebotsteil, Angebotsvariante, Betrag, Menge, Mengeneinheit
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_angebotsteil import example_angebotsteil, example_angebotsteil_json
from tests.test_betrag import example_betrag
from tests.test_menge import example_menge

# can be imported by other tests
example_angebotsvariante = Angebotsvariante(
    angebotsstatus=Angebotsstatus.NACHGEFASST,
    bindefrist=datetime(2022, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
    erstellungsdatum=datetime(2021, 12, 22, 0, 0, 0, tzinfo=timezone.utc),
    teile=[example_angebotsteil],
)


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
