from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.angebotsvariante import Angebotsvariante
from bo4e.enum.angebotsstatus import Angebotsstatus
from bo4e.enum.mengeneinheit import Mengeneinheit
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_angebotsteil import example_angebotsteil, example_angebotsteil_json
from tests.test_betrag import example_betrag, example_betrag_json
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
        "angebotsvariante, expected_json_dict",
        [
            pytest.param(
                example_angebotsvariante,
                {
                    "gesamtmenge": None,
                    "angebotsstatus": Angebotsstatus.NACHGEFASST,
                    "erstellungsdatum": datetime(2021, 12, 22, 0, 0, tzinfo=timezone.utc),
                    "gesamtkosten": None,
                    "bindefrist": datetime(2022, 2, 1, 0, 0, tzinfo=timezone.utc),
                    "teile": [example_angebotsteil_json],
                },
                id="minimal attributes",
            ),
            pytest.param(
                Angebotsvariante(
                    angebotsstatus=Angebotsstatus.NACHGEFASST,
                    bindefrist=datetime(2022, 2, 1, 0, 0, 0, tzinfo=timezone.utc),
                    erstellungsdatum=datetime(2021, 12, 22, 0, 0, 0, tzinfo=timezone.utc),
                    teile=[example_angebotsteil],
                    gesamtmenge=example_menge,
                    gesamtkosten=example_betrag,
                ),
                {
                    "gesamtmenge": {
                        "einheit": Mengeneinheit.MWH,
                        "wert": Decimal("3.410000000000000142108547152020037174224853515625"),
                    },
                    # this is a problem for https://github.com/Hochfrequenz/BO4E-python/issues/249
                    # I just reused the example_menge but don't attempt to fix it in the context of the Angebotsvariante
                    "angebotsstatus": Angebotsstatus.NACHGEFASST,
                    "erstellungsdatum": datetime(2021, 12, 22, 0, 0, tzinfo=timezone.utc),
                    "gesamtkosten": example_betrag_json,
                    "bindefrist": datetime(2022, 2, 1, 0, 0, tzinfo=timezone.utc),
                    "teile": [example_angebotsteil_json],
                },
                id="max attributes",  # = min + menge and betrag
            ),
        ],
    )
    def test_serialization_roundtrip(
        self, angebotsvariante: Angebotsvariante, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation roundtrip.
        """
        assert_serialization_roundtrip(angebotsvariante, expected_json_dict)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Angebotsvariante()  # type: ignore[call-arg]

        assert "4 validation errors" in str(excinfo.value)
