# todo: cf. alias_generator=camelize in geschaeftsobjekte.py
from typing import Any, Dict

import pytest

from bo4e.com.abweichung import Abweichung
from bo4e.enum.abweichungsgrund import Abweichungsgrund
from tests.serialization_helper import assert_serialization_roundtrip

#: create full example
example_abweichung = Abweichung(
    abweichungsgrund=Abweichungsgrund.UNBEKANNTE_MARKTLOKATION_MESSLOKATION,
    abweichungsgrund_bemerkung="sonst",
    zugehoerige_rechnung="458011",
    abschlagsrechnung="4580112",
    abweichungsgrund_code="14",
    abweichungsgrund_codeliste="G_0081",
)


class Test_Abweichung:
    @pytest.mark.parametrize(
        "abweichung, expected_json_dict",
        [
            pytest.param(
                example_abweichung,
                {
                    "abweichungsgrund": Abweichungsgrund.UNBEKANNTE_MARKTLOKATION_MESSLOKATION,
                    "abweichungsgrundBemerkung": "sonst",
                    "zugehoerigeRechnung": "458011",
                    "abschlagsrechnung": "4580112",
                    "abweichungsgrundCode": "14",
                    "abweichungsgrundCodeliste": "G_0081",
                },
                id="max param test",
            ),
            pytest.param(
                Abweichung(),
                {
                    "abweichungsgrund": None,
                    "abweichungsgrundBemerkung": None,
                    "zugehoerigeRechnung": None,
                    "abschlagsrechnung": None,
                    "abweichungsgrundCode": None,
                    "abweichungsgrundCodeliste": None,
                },
                id="min param test",
            ),
        ],
    )
    def test_serialization_roundtrip(self, abweichung: Abweichung, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of Abweichung with minimal attributes.
        """
        assert_serialization_roundtrip(abweichung, expected_json_dict)
