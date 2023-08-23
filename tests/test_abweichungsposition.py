# todo: check camelizing
from typing import Any, Dict

import pytest

from bo4e.com.abweichungsposition import Abweichungsposition
from tests.serialization_helper import assert_serialization_roundtrip

#: full example
example_abweichungsposition = Abweichungsposition(
    abweichungsgrund_code="14",
    abweichungsgrund_codeliste="G_0081",
    abweichungsgrund_bemerkung="Umsatzsteuersatz",
    zugehoerige_rechnung="458011",
    zugehoerige_bestellung="foo",
)


class TestAbweichungsposition:
    @pytest.mark.parametrize(
        "abweichungsposition, expected_json_dict",
        [
            pytest.param(
                example_abweichungsposition,
                {
                    "abweichungsgrundCode": "14",
                    "abweichungsgrundCodeliste": "G_0081",
                    "abweichungsgrundBemerkung": "Umsatzsteuersatz",
                    "zugehoerigeRechnung": "458011",
                    "zugehoerigeBestellung": "foo",
                },
                id="max param test",
            ),
            pytest.param(
                Abweichungsposition(),
                {
                    "abweichungsgrundCode": None,
                    "abweichungsgrundCodeliste": None,
                    "abweichungsgrundBemerkung": None,
                    "zugehoerigeRechnung": None,
                    "zugehoerigeBestellung": None,
                },
                id="min param test",
            ),
        ],
    )
    def test_serialization_roundtrip(
        self, abweichungsposition: Abweichungsposition, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Abweichungsposition with minimal attributes.
        """
        assert_serialization_roundtrip(abweichungsposition, expected_json_dict)
