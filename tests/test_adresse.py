import json

import pytest  # type:ignore[import]

from bo4e.com.adresse import Adresse, AdresseSchema
from bo4e.enum.landescode import Landescode

# can be imported by other tests
example_adresse = Adresse(
    ort="Grünwald",
    landescode=Landescode.DE,  # type:ignore[attr-defined]
    hausnummer="27A",
    strasse="Nördliche Münchner Straße",
    postleitzahl="82031",
)


class TestAddress:
    def test_serialization_strasse(self):
        """
        Test serialization with strasse und hausnummer
        and default value of landescode
        """
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

        schema = AdresseSchema()
        address_dict = schema.dump(a)

        assert address_dict["strasse"] == "Nördliche Münchner Straße"
        assert address_dict["hausnummer"] == "27A"
        assert address_dict["postleitzahl"] == "82031"
        assert address_dict["landescode"] == "DE"

        deserialized_address = schema.load(address_dict)

        assert isinstance(deserialized_address, Adresse)
        assert deserialized_address.strasse == "Nördliche Münchner Straße"
        assert deserialized_address.hausnummer == "27A"
        assert deserialized_address.postleitzahl == "82031"
        assert deserialized_address.landescode == Landescode.DE

    def test_serialization_only_postfach(self):
        """Test serialization with postfach"""
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

        schema = AdresseSchema()
        address_json = schema.dumps(a, ensure_ascii=False)

        assert "10 64 38" in address_json
        assert "82031" in address_json
        assert "DE" in address_json

        deserialized_address = schema.loads(address_json)

        assert isinstance(deserialized_address, Adresse)
        assert deserialized_address.postfach == "10 64 38"
        assert deserialized_address.postleitzahl == "82031"
        assert deserialized_address.landescode == Landescode.DE

    def test_serialization_only_required_fields(self):
        """Test serialization with just postleitzahl und ort"""
        address_test_data = {
            "postleitzahl": "82031",
            "ort": "Grünwald",
        }

        a = Adresse(
            postleitzahl=address_test_data["postleitzahl"],
            ort=address_test_data["ort"],
        )

        schema = AdresseSchema()
        address_json = schema.dumps(a, ensure_ascii=False)

        assert "Grünwald" in address_json
        assert "82031" in address_json

        deserialized_address = schema.loads(address_json)

        assert isinstance(deserialized_address, Adresse)
        assert deserialized_address.ort == "Grünwald"
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

        schema = AdresseSchema()
        address_json = schema.dumps(a, ensure_ascii=False)
        deserialized_address = schema.loads(address_json)

        assert deserialized_address.landescode == Landescode.AT

    def test_deserialization(self):
        json_string = r"""{"strasse":"Getreidegasse",
                 "hausnummer":"9",
                 "ort":"Salzburg",
                 "postleitzahl":"5020",
                 "landescode":"AT"}"""

        schema = AdresseSchema()
        a: Adresse = schema.loads(json_string)
        assert a.landescode is Landescode.AT

    @pytest.mark.datafiles("./tests/test_data/test_data_adresse/test_data_adresse_missing_plz.json")
    def test_missing_required_attribute(self, datafiles):
        """
        Test for getting an error message if a required attribute is missing
        """
        with open(datafiles / "test_data_adresse_missing_plz.json", encoding="utf-8") as json_file:
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
                    "strasse": "Nördliche Münchner Straße",
                    "hausnummer": None,
                    "postfach": None,
                },
                "Missing hausnummer",
                id="Missing hausnummer",
            ),
            pytest.param(
                {
                    "postleitzahl": "82031",
                    "ort": "Grünwald",
                    "strasse": "",
                    "hausnummer": "27A",
                    "postfach": None,
                },
                "Missing strasse",
                id="Missing strasse",
            ),
            pytest.param(
                {
                    "postleitzahl": "82031",
                    "ort": "Grünwald",
                    "strasse": "Nördliche Münchner Straße",
                    "hausnummer": "27A",
                    "postfach": "10 64 38",
                },
                "hausnummer OR postfach",
                id="Strasse, hausnummer and postfach",
            ),
            pytest.param(
                {
                    "postleitzahl": "82031",
                    "ort": "Grünwald",
                    "strasse": None,
                    "hausnummer": "27A",
                    "postfach": "10 64 38",
                },
                "hausnummer OR postfach",
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

    def test_serialization_of_non_german_address(self):
        """
        Minimal working example
        :return:
        """
        a = Adresse(
            postleitzahl="6413", ort="Wildermieming", strasse="Gerhardhof", hausnummer="1", landescode=Landescode.AT
        )
        assert a.landescode == Landescode.AT
        serialized_address = AdresseSchema().dumps(a)
        assert '"AT"' in serialized_address
        deserialized_address = AdresseSchema().loads(serialized_address)
        assert deserialized_address.landescode == Landescode.AT
