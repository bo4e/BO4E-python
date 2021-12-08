import pytest  # type:ignore[import]

from bo4e.com.standorteigenschaftenallgemein import StandorteigenschaftenAllgemein, StandorteigenschaftenAllgemeinSchema
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestStandorteigenschaftenAllgemein:
    @pytest.mark.parametrize(
        "standorteigenschaftenallgemein, expected_json_dict",
        [
            pytest.param(
                StandorteigenschaftenAllgemein(
                    postleitzahl="66646",
                    ort="Alsweiler",
                    kreisname="St. Wendel",
                    gemeindename="Marpingen",
                    gemeindekennziffer="10 0 46 112",
                    gemeindeeinwohner=9961,
                    bundesland="Saarland",
                ),
                {
                    "postleitzahl": "66646",
                    "ort": "Alsweiler",
                    "kreisname": "St. Wendel",
                    "gemeindename": "Marpingen",
                    "gemeindekennziffer": "10 0 46 112",
                    "gemeindeeinwohner": 9961,
                    "bundesland": "Saarland",
                },
            )
        ],
    )
    def test_standorteigenschaftenallgemein_serialization_roundtrip(
        self, standorteigenschaftenallgemein: StandorteigenschaftenAllgemein, expected_json_dict: dict
    ):
        """
        Test de-/serialisation of StandorteigenschaftenAllgemein with minimal attributes.
        """
        assert_serialization_roundtrip(
            standorteigenschaftenallgemein, StandorteigenschaftenAllgemeinSchema(), expected_json_dict
        )

    def test_standorteigenschaftenallgemein_missing_required_attributes(self):
        with pytest.raises(TypeError) as excinfo:
            _ = StandorteigenschaftenAllgemein()
        assert "missing 7 required" in str(excinfo.value)
