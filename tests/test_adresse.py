import json
import jsons
import pytest

from bo4e.com.adresse import Adresse
from bo4e.enum.landescode import Landescode


class TestAddress:
    def test_serialization_only_required_fields_strasse(self):
        with open(
            "./tests/test_data/test_data_adresse/test_data_adresse_only_required_fields.json",
            encoding="utf-8",
        ) as json_file:
            address_test_data = json.load(json_file)

        a = Adresse(
            postleitzahl=address_test_data["postleitzahl"],
            ort=address_test_data["ort"],
            strasse=address_test_data["strasse"],
            hausnummer=address_test_data["hausnummer"],
        )

        address_json = a.dumps(
            strip_nulls=True,
            key_transformer=jsons.KEY_TRANSFORMER_CAMELCASE,
            jdkwargs={"ensure_ascii": False},
        )

        assert "Nördliche Münchner Straße" in address_json
        assert "27A" in address_json
        assert "82031" in address_json
        assert "DE" in address_json

        deserialized_address = Adresse.loads(address_json)

        assert isinstance(deserialized_address, Adresse)
        assert deserialized_address.strasse == "Nördliche Münchner Straße"
        assert deserialized_address.hausnummer == "27A"
        assert deserialized_address.postleitzahl == "82031"
        assert deserialized_address.landescode == Landescode.DE

    def test_serialization_only_required_fields_postfach(self):
        address_test_data = {
            "postleitzahl": "82031",
            "ort": "Grünwald",
            "postfach": "10 64 38",
        }

        a = Adresse(
            postleitzahl=address_test_data["postleitzahl"],
            ort=address_test_data["ort"],
            postfach=address_test_data["postfach"],
        )

        address_json = a.dumps(
            strip_nulls=True,
            key_transformer=jsons.KEY_TRANSFORMER_CAMELCASE,
            jdkwargs={"ensure_ascii": False},
        )

        assert "10 64 38" in address_json
        assert "82031" in address_json

        deserialized_address = Adresse.loads(address_json)

        assert isinstance(deserialized_address, Adresse)
        assert deserialized_address.postfach == "10 64 38"
        assert deserialized_address.postleitzahl == "82031"

    def test_serialization_only_required_fields_landescode_AT(self):
        with open(
            "./tests/test_data/test_data_adresse/test_data_adresse_only_required_fields.json",
            encoding="utf-8",
        ) as json_file:
            address_test_data = json.load(json_file)

        a = Adresse(
            postleitzahl=address_test_data["postleitzahl"],
            ort=address_test_data["ort"],
            strasse=address_test_data["strasse"],
            hausnummer=address_test_data["hausnummer"],
            landescode=Landescode.AT,
        )

        address_json = a.dumps(
            strip_nulls=True,
            key_transformer=jsons.KEY_TRANSFORMER_CAMELCASE,
            jdkwargs={"ensure_ascii": False},
        )

        assert json.loads(address_json)["landescode"] == "AT"

    def test_deserialization(self):
        json_string = r"""{"strasse":"Getreidegasse",
                 "hausnummer":"9",
                 "ort":"Salzburg",
                 "postleitzahl":"5020",
                 "landescode":"AT"}"""
        a: Adresse = Adresse.loads(json_string)
        assert a.landescode is Landescode.AT

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
            address_test_data = json.load(json_file)

        with pytest.raises(TypeError) as excinfo:

            _ = Adresse(
                ort=address_test_data["ort"],
                strasse=address_test_data["strasse"],
                hausnummer=address_test_data["hausnummer"],
            )

        assert "postleitzahl" in str(excinfo.value)

    @pytest.mark.parametrize(
        "address_test_data, expected",
        [
            pytest.param(
                {
                    "postleitzahl": "82031",
                    "ort": "Grünwald",
                    "strasse": None,
                    "hausnummer": "27A",
                    "postfach": None,
                },
                "Either",
                id="Missing strasse",
            ),
            pytest.param(
                {
                    "postleitzahl": "82031",
                    "ort": "Grünwald",
                    "strasse": "Nördliche Münchner Straße",
                    "hausnummer": None,
                    "postfach": None,
                },
                "Either",
                id="Missing hausnummer",
            ),
            pytest.param(
                {
                    "postleitzahl": "82031",
                    "ort": "Grünwald",
                    "strasse": None,
                    "hausnummer": None,
                    "postfach": None,
                },
                "Either",
                id="Missing postfach",
            ),
            pytest.param(
                {
                    "postleitzahl": "82031",
                    "ort": "Grünwald",
                    "strasse": None,
                    "hausnummer": "27A",
                    "postfach": "10 64 38",
                },
                "Only",
                id="Postfach and hausnummer",
            ),
        ],
    )
    def test_strasse_xor_postfach(self, address_test_data, expected):

        with pytest.raises(ValueError) as excinfo:

            _ = Adresse(
                postleitzahl=address_test_data["postleitzahl"],
                ort=address_test_data["ort"],
                strasse=address_test_data["strasse"],
                hausnummer=address_test_data["hausnummer"],
                postfach=address_test_data["postfach"],
            )
        assert expected in str(excinfo.value)
