import datetime

import pytest  # type:ignore[import]

from bo4e.com.angebotsvariante import Angebotsvariante, AngebotsvarianteSchema
from bo4e.enum.angebotsstatus import Angebotsstatus
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_angebotsteil import example_angebotsteil, example_angebotsteil_json  # type:ignore[import]
from tests.test_betrag import example_betrag, example_betrag_json  # type:ignore[import]
from tests.test_menge import example_menge  # type:ignore[import]


class TestAngebotsvariante:
    @pytest.mark.parametrize(
        "angebotsvariante, expected_json_dict",
        [
            pytest.param(
                Angebotsvariante(
                    angebotsstatus=Angebotsstatus.NACHGEFASST,
                    bindefrist=datetime.datetime(2022, 2, 1, 0, 0, 0, tzinfo=datetime.timezone.utc),
                    erstellungsdatum=datetime.datetime(2021, 12, 22, 0, 0, 0, tzinfo=datetime.timezone.utc),
                    teile=[example_angebotsteil],
                ),
                {
                    "gesamtmenge": None,
                    "angebotsstatus": "NACHGEFASST",
                    "erstellungsdatum": "2021-12-22T00:00:00+00:00",
                    "gesamtkosten": None,
                    "bindefrist": "2022-02-01T00:00:00+00:00",
                    "teile": [example_angebotsteil_json],
                },
                id="minimal attributes",
            ),
            pytest.param(
                Angebotsvariante(
                    angebotsstatus=Angebotsstatus.NACHGEFASST,
                    bindefrist=datetime.datetime(2022, 2, 1, 0, 0, 0, tzinfo=datetime.timezone.utc),
                    erstellungsdatum=datetime.datetime(2021, 12, 22, 0, 0, 0, tzinfo=datetime.timezone.utc),
                    teile=[example_angebotsteil],
                    gesamtmenge=example_menge,
                    gesamtkosten=example_betrag,
                ),
                {
                    "gesamtmenge": {"einheit": "MWH", "wert": "3.410000000000000142108547152020037174224853515625"},
                    # this is a problem for https://github.com/Hochfrequenz/BO4E-python/issues/249
                    # I just reused the example_menge but don't attempt to fix it in the context of the Angebotsvariante
                    "angebotsstatus": "NACHGEFASST",
                    "erstellungsdatum": "2021-12-22T00:00:00+00:00",
                    "gesamtkosten": example_betrag_json,
                    "bindefrist": "2022-02-01T00:00:00+00:00",
                    "teile": [example_angebotsteil_json],
                },
                id="max attributes",  # = min + menge and betrag
            ),
        ],
    )
    def test_serialization_roundtrip(self, angebotsvariante: Angebotsvariante, expected_json_dict: dict):
        """
        Test de-/serialisation roundtrip.
        """
        assert_serialization_roundtrip(angebotsvariante, AngebotsvarianteSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Angebotsvariante()

        assert "missing 4 required" in str(excinfo.value)
