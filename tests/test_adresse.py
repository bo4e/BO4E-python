from typing import Dict, Optional

import pytest
from py._path.local import LocalPath
from pydantic import ValidationError

from bo4e.com.adresse import Adresse
from bo4e.enum.landescode import Landescode

# import pydantic

# can be imported by other tests
example_adresse = Adresse(
    ort="Grünwald",
    landescode=Landescode.DE,  # type: ignore[attr-defined]
    hausnummer="27A",
    strasse="Nördliche Münchner Straße",
    postleitzahl="82031",
)


class TestAddress:
    def test_serialization_strasse(self) -> None:
        """
        Test serialization with strasse und hausnummer
        and default value of landescode
        """

        address_test_data = Adresse.parse_file(
            "./tests/test_data/test_data_adresse/test_data_adresse_only_required_fields.json",
            encoding="utf-8",
        )

        address_dict = address_test_data.json(by_alias=True, ensure_ascii=False)

        assert "Nördliche Münchner Straße" in address_dict
        assert "27A" in address_dict
        assert "82031" in address_dict
        assert "DE" in address_dict

        deserialized_address = Adresse.parse_raw(address_dict)

        assert isinstance(deserialized_address, Adresse)
        assert deserialized_address.strasse == "Nördliche Münchner Straße"
        assert deserialized_address.hausnummer == "27A"
        assert deserialized_address.postleitzahl == "82031"
        assert deserialized_address.landescode == Landescode.DE  # type: ignore[attr-defined]

    def test_serialization_only_postfach(self) -> None:
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

        address_json = a.json(by_alias=True, ensure_ascii=False)

        assert "10 64 38" in address_json
        assert "82031" in address_json
        assert "DE" in address_json

        deserialized_address = Adresse.parse_raw(address_json)

        assert isinstance(deserialized_address, Adresse)
        assert deserialized_address.postfach == "10 64 38"
        assert deserialized_address.postleitzahl == "82031"
        assert deserialized_address.landescode == Landescode.DE  # type: ignore[attr-defined]

    def test_serialization_only_required_fields(self) -> None:
        """Test serialization with just postleitzahl und ort"""
        address_test_data = {
            "postleitzahl": "82031",
            "ort": "Grünwald",
        }

        a = Adresse(
            postleitzahl=address_test_data["postleitzahl"],
            ort=address_test_data["ort"],
        )

        address_json = a.json(by_alias=True, ensure_ascii=False)

        assert "Grünwald" in address_json
        assert "82031" in address_json

        deserialized_address = Adresse.parse_raw(address_json)

        assert isinstance(deserialized_address, Adresse)
        assert deserialized_address.ort == "Grünwald"
        assert deserialized_address.postleitzahl == "82031"

    def test_serialization_only_required_fields_landescode_AT(self) -> None:

        address_test_data = Adresse.parse_file(
            "./tests/test_data/test_data_adresse/test_data_adresse_only_required_fields.json",
            encoding="utf-8",
        )
        address_test_data.landescode = Landescode.AT  # type: ignore[attr-defined]

        address_json = address_test_data.json(by_alias=True, ensure_ascii=False)
        deserialized_address = Adresse.parse_raw(address_json)

        assert deserialized_address.landescode == Landescode.AT  # type: ignore[attr-defined]

    def test_deserialization(self) -> None:
        json_string = r"""{"strasse":"Getreidegasse",
                 "hausnummer":"9",
                 "ort":"Salzburg",
                 "postleitzahl":"5020",
                 "landescode":"AT"}"""

        a: Adresse = Adresse.parse_raw(json_string)
        assert a.landescode is Landescode.AT  # type: ignore[attr-defined]

    @pytest.mark.datafiles("./tests/test_data/test_data_adresse/test_data_adresse_missing_plz.json")
    def test_missing_required_attribute(self, datafiles: LocalPath) -> None:
        """
        Test for getting an error message if a required attribute is missing
        """

        with pytest.raises(ValidationError) as excinfo:
            _ = Adresse.parse_file(datafiles / "test_data_adresse_missing_plz.json", encoding="utf-8")

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
                'You have to define either "strasse" and "hausnummer" or "postfach".',
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
                'You have to define either "strasse" and "hausnummer" or "postfach".',
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
                'You have to define either "strasse" and "hausnummer" or "postfach".',
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
                'You have to define either "strasse" and "hausnummer" or "postfach".',
                id="Postfach and hausnummer",
            ),
        ],
    )
    def test_strasse_xor_postfach(self, address_test_data: Dict[str, Optional[str]], expected: str) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Adresse(
                postleitzahl=address_test_data["postleitzahl"],  # type: ignore[arg-type]
                ort=address_test_data["ort"],  # type: ignore[arg-type]
                strasse=address_test_data["strasse"],
                hausnummer=address_test_data["hausnummer"],
                postfach=address_test_data["postfach"],
            )
        assert expected in str(excinfo.value)

    def test_serialization_of_non_german_address(self) -> None:
        """
        Minimal working example
        :return:
        """
        a = Adresse(
            postleitzahl="6413", ort="Wildermieming", strasse="Gerhardhof", hausnummer="1", landescode=Landescode.AT  # type: ignore[attr-defined]
        )
        assert a.landescode == Landescode.AT  # type: ignore[attr-defined]
        serialized_address = a.json(by_alias=True, ensure_ascii=False)
        assert '"AT"' in serialized_address
        deserialized_address = Adresse.parse_raw(serialized_address)
        assert deserialized_address.landescode == Landescode.AT  # type: ignore[attr-defined]
