from datetime import datetime, timezone

import pytest  # type:ignore[import]
from pydantic import ValidationError

from bo4e.com.preisgarantie import Preisgarantie
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.preisgarantietyp import Preisgarantietyp
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]

example_preisgarantie = Preisgarantie(
    preisgarantietyp=Preisgarantietyp.NUR_ENERGIEPREIS,
    zeitliche_gueltigkeit=Zeitraum(
        startdatum=datetime(2020, 1, 1, tzinfo=timezone.utc),
        enddatum=datetime(2020, 4, 1, tzinfo=timezone.utc),
    ),
)


class TestPreisgarantie:
    @pytest.mark.parametrize(
        "preisgarantie, expected_json_dict",
        [
            pytest.param(
                example_preisgarantie,
                {
                    "beschreibung": None,
                    "preisgarantietyp": "NUR_ENERGIEPREIS",
                    "zeitlicheGueltigkeit": {
                        "startdatum": datetime(2020, 1, 1, 0, 0, tzinfo=timezone.utc),
                        "endzeitpunkt": None,
                        "einheit": None,
                        "enddatum": datetime(2020, 4, 1, 0, 0, tzinfo=timezone.utc),
                        "startzeitpunkt": None,
                        "dauer": None,
                    },
                },
            ),
        ],
    )
    def test_preisgarantie_required_attributes(self, preisgarantie, expected_json_dict):
        """
        Test de-/serialisation of Preisgarantie with minimal attributes.
        """
        assert_serialization_roundtrip(preisgarantie, expected_json_dict)

    def test_preisgarantie_missing_required_attribute(self):
        with pytest.raises(ValidationError) as excinfo:
            _ = Preisgarantie()

        assert "2 validation errors" in str(excinfo.value)
