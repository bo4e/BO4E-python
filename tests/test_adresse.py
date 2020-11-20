import json
import jsons
import pytest

from bo4e.com.adresse import Adresse
from bo4e.enum.landescode import Landescode

test_data = [
    pytest.param(
        "test_data_adresse_only_required_fields.json",
        "DE",
        id="Test default DE",
    ),
    pytest.param(
        "test_data_adresse_only_required_fields_landescode_AT.json",
        "AT",
        id="Test different landescode",
    ),
]


class TestAddress:
    @pytest.mark.datafiles(
        "./tests/test_data/test_data_adresse/test_data_adresse_only_required_fields.json",
        "./tests/test_data/test_data_adresse/test_data_adresse_only_required_fields_landescode_AT.json",
    )
    @pytest.mark.parametrize("test_address_data, expected", test_data)
    def test_serialization(self, test_address_data, expected, datafiles):
        with open(
            datafiles / test_address_data,
            encoding="utf-8",
        ) as json_file:
            address_test_data = json.load(json_file)

        if "landescode" not in address_test_data:
            a = Adresse(
                postleitzahl=address_test_data["postleitzahl"],
                ort=address_test_data["ort"],
                strasse=address_test_data["strasse"],
                hausnummer=address_test_data["hausnummer"],
            )
        else:
            a = Adresse(
                postleitzahl=address_test_data["postleitzahl"],
                ort=address_test_data["ort"],
                strasse=address_test_data["strasse"],
                hausnummer=address_test_data["hausnummer"],
                landescode=address_test_data["landescode"],
            )

        address_json = a.dumps(
            strip_nulls=True,
            key_transformer=jsons.KEY_TRANSFORMER_CAMELCASE,
            jdkwargs={"ensure_ascii": False},
        )
        assert expected in address_json, f"Landescode does not contain '{expected}'"

    def test_deserialization(self):
        json_string = r"""{"strasse":"Getreidegasse",
                 "hausnummer":"9",
                 "ort":"Salzburg",
                 "postleitzahl":"5020",
                 "landescode":"AT"}"""
        a: Adresse = Adresse.loads(json_string)
        assert a.landescode == Landescode("Austria")

    @pytest.mark.datafiles(
        "./tests/test_data/test_data_adresse/test_data_adresse_missing_plz.json"
    )
    def test_missing_required_attribute(self, datafiles):
        """
        Test for getting an error message if a required attribute is missing
        """
        with open(
            datafiles / "test_data_adresse_missing_plz.json", encoding="utf-8"
        ) as json_file:
            adress_test_data = json.load(json_file)

        with pytest.raises(TypeError) as excinfo:

            _ = Adresse(
                ort=adress_test_data["ort"],
                strasse=adress_test_data["strasse"],
                hausnummer=adress_test_data["hausnummer"],
            )

        assert "postleitzahl" in str(excinfo.value)
