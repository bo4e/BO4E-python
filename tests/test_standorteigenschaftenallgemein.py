from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.standorteigenschaftenallgemein import StandorteigenschaftenAllgemein
from tests.serialization_helper import assert_serialization_roundtrip

example_standorteigenschaften_allgemein = StandorteigenschaftenAllgemein(
    postleitzahl="66646",
    ort="Alsweiler",
    kreisname="St. Wendel",
    gemeindename="Marpingen",
    gemeindekennziffer="10 0 46 112",
    gemeindeeinwohner=9961,
    bundesland="Saarland",
)
example_standorteigenschaften_allgemein_dict = {
    "postleitzahl": "66646",
    "ort": "Alsweiler",
    "kreisname": "St. Wendel",
    "gemeindename": "Marpingen",
    "gemeindekennziffer": "10 0 46 112",
    "gemeindeeinwohner": 9961,
    "bundesland": "Saarland",
}


class TestStandorteigenschaftenAllgemein:
    @pytest.mark.parametrize(
        "standorteigenschaftenallgemein, expected_json_dict",
        [pytest.param(example_standorteigenschaften_allgemein, example_standorteigenschaften_allgemein_dict)],
    )
    def test_standorteigenschaftenallgemein_serialization_roundtrip(
        self, standorteigenschaftenallgemein: StandorteigenschaftenAllgemein, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of StandorteigenschaftenAllgemein with minimal attributes.
        """
        assert_serialization_roundtrip(standorteigenschaftenallgemein, expected_json_dict)

    def test_standorteigenschaftenallgemein_missing_required_attributes(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = StandorteigenschaftenAllgemein()  # type: ignore[call-arg]
        assert "7 validation errors" in str(excinfo.value)
