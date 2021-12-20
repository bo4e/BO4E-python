from datetime import datetime, timezone

import pytest  # type:ignore[import]

from bo4e.com.preisgarantie import Preisgarantie, PreisgarantieSchema
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.preisgarantietyp import Preisgarantietyp
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestPreisgarantie:
    @pytest.mark.parametrize(
        "preisgarantie, expected_json_dict",
        [
            pytest.param(
                Preisgarantie(
                    preisgarantietyp=Preisgarantietyp.NUR_ENERGIEPREIS,
                    zeitliche_gueltigkeit=Zeitraum(
                        startdatum=datetime(2020, 1, 1, tzinfo=timezone.utc),
                        enddatum=datetime(2020, 4, 1, tzinfo=timezone.utc),
                    ),
                ),
                {
                    "beschreibung": None,
                    "preisgarantietyp": "NUR_ENERGIEPREIS",
                    "zeitlicheGueltigkeit": {
                        "startdatum": "2020-01-01T00:00:00+00:00",
                        "endzeitpunkt": None,
                        "einheit": None,
                        "enddatum": "2020-04-01T00:00:00+00:00",
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
        assert_serialization_roundtrip(preisgarantie, PreisgarantieSchema(), expected_json_dict)

    def test_preisgarantie_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Preisgarantie()

        assert "missing 2 required" in str(excinfo.value)
