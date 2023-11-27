import uuid

import pytest

from bo4e import Adresse, Landescode
from tests.serialization_helper import assert_serialization_roundtrip
from tests.utils import parse_file


class TestAddress:
    @pytest.mark.parametrize(
        "adresse",
        [
            pytest.param(
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
            ),
            pytest.param(
                parse_file(Adresse, "./tests/test_data/test_data_adresse/test_data_adresse_only_required_fields.json")
            ),
            pytest.param(
                Adresse(
                    postleitzahl="82031",
                    ort="Grünwald",
                    postfach="10 64 38",
                ),
            ),
            pytest.param(
                Adresse(
                    postleitzahl="82031",
                    ort="Grünwald",
                ),
            ),
            pytest.param(
                parse_file(Adresse, "./tests/test_data/test_data_adresse/test_data_adresse_only_required_fields.json")
            ),
            pytest.param(
                Adresse.model_validate_json(
                    r"""{"strasse":"Getreidegasse",
                 "hausnummer":"9",
                 "ort":"Salzburg",
                 "postleitzahl":"5020",
                 "landescode":"AT"}"""
                )
            ),
            pytest.param(
                Adresse(
                    postleitzahl="6413",
                    ort="Wildermieming",
                    strasse="Gerhardhof",
                    hausnummer="1",
                    landescode=Landescode.AT,  # type: ignore[attr-defined]
                ),
            ),
            pytest.param(
                Adresse(
                    id=str(uuid.uuid4()),
                    ort="Grünwald",
                    landescode=Landescode.DE,  # type: ignore[attr-defined]
                    hausnummer="27A",
                    strasse="Nördliche Münchner Straße",
                    postleitzahl="82031",
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, adresse: Adresse) -> None:
        """
        Test de-/serialisation of Adresse.
        """
        assert_serialization_roundtrip(adresse)
