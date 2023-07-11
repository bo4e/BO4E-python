from pathlib import Path
from typing import Dict, Optional

import pytest
from pydantic import ValidationError

from bo4e.com.adresse import Adresse
from bo4e.enum import landescode
from bo4e.enum.landescode import Landescode
from tests.utils import parse_file

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

        address_test_data = parse_file(
            Adresse, "./tests/test_data/test_data_adresse/test_data_adresse_only_required_fields.json"
        )

        address_dict = address_test_data.model_dump_json(by_alias=True)

        assert "Nördliche Münchner Straße" in address_dict
        assert "27A" in address_dict
        assert "82031" in address_dict
        assert "DE" in address_dict

        deserialized_address = Adresse.model_validate_json(address_dict)

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

        address_json = a.model_dump_json(by_alias=True)

        assert "10 64 38" in address_json
        assert "82031" in address_json
        assert "DE" in address_json

        deserialized_address = Adresse.model_validate_json(address_json)

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

        address_json = a.model_dump_json(by_alias=True)

        assert "Grünwald" in address_json
        assert "82031" in address_json

        deserialized_address = Adresse.model_validate_json(address_json)

        assert isinstance(deserialized_address, Adresse)
        assert deserialized_address.ort == "Grünwald"
        assert deserialized_address.postleitzahl == "82031"

    def test_serialization_only_required_fields_landescode_AT(self) -> None:
        address_test_data = parse_file(
            Adresse, "./tests/test_data/test_data_adresse/test_data_adresse_only_required_fields.json"
        )
        address_test_data.landescode = Landescode.AT  # type: ignore[attr-defined]

        address_json = address_test_data.model_dump_json(by_alias=True)
        deserialized_address = Adresse.model_validate_json(address_json)

        assert deserialized_address.landescode == Landescode.AT  # type: ignore[attr-defined]

    def test_deserialization(self) -> None:
        json_string = r"""{"strasse":"Getreidegasse",
                 "hausnummer":"9",
                 "ort":"Salzburg",
                 "postleitzahl":"5020",
                 "landescode":"AT"}"""

        a: Adresse = Adresse.model_validate_json(json_string)
        assert a.landescode is Landescode.AT  # type: ignore[attr-defined]

    @pytest.mark.datafiles("./tests/test_data/test_data_adresse/test_data_adresse_missing_plz.json")
    def test_missing_required_attribute(self, datafiles: Path) -> None:
        """
        Test for getting an error message if a required attribute is missing
        """

        with pytest.raises(ValidationError) as excinfo:
            _ = parse_file(Adresse, datafiles / "test_data_adresse_missing_plz.json")

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
            _ = Adresse.model_validate(address_test_data)
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
        serialized_address = a.model_dump_json(by_alias=True)
        assert '"AT"' in serialized_address
        deserialized_address = Adresse.model_validate_json(serialized_address)
        assert deserialized_address.landescode == Landescode.AT  # type: ignore[attr-defined]

    @pytest.mark.parametrize(
        "address_json, adresse",
        [
            pytest.param(
                r"""{"postleitzahl": "12345",
                    "ort": "ISS spacestation",
                    "strasse": "Milky Way",
                    "hausnummer": "42",
                    "landescode": "FR",
                    "adresszusatz": "to whom it may concern",
                    "co_ergaenzung": "you will find me",
                    "ortsteil": "Mitte"}""",
                Adresse(
                    postleitzahl="12345",
                    ort="ISS spacestation",
                    strasse="Milky Way",
                    hausnummer="42",
                    landescode=Landescode.FR,  # type:ignore[attr-defined]
                    adresszusatz="to whom it may concern",
                    co_ergaenzung="you will find me",
                    ortsteil="Mitte",
                ),
            )
        ],
    )
    def test_serialization_with_all_possible_fields(self, address_json: str, adresse: Adresse) -> None:
        """
        Test serialization with all required and optional attributes
        """

        serialized_address = adresse.model_dump_json(by_alias=True)

        assert "ISS spacestation" in serialized_address
        assert "12345" in serialized_address
        assert "Milky Way" in serialized_address
        assert "42" in serialized_address
        assert "FR" in serialized_address
        assert "to whom it may concern" in serialized_address
        assert "you will find me" in serialized_address
        assert "Mitte" in serialized_address

        deserialized_address = Adresse.model_validate_json(address_json)

        assert deserialized_address == adresse
