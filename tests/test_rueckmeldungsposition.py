from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.abweichungsposition import Abweichungsposition
from bo4e.com.rueckmeldungsposition import Rueckmeldungsposition
from tests.serialization_helper import assert_serialization_roundtrip

#: full example
example_rueckmeldungsposition = Rueckmeldungsposition(
    positionsnummer="1",
    abweichungspositionen=[
        Abweichungsposition(
            abweichungsgrund_code="A15",
            abweichungsgrund_codeliste="E_0210",
            abweichungsgrund_bemerkung="Umsatzsteuersatz",
            zugehoerige_rechnung="458011",
            zugehoerige_bestellung="foo",
        ),
    ],
)


class TestRueckmeldungsposition:
    @pytest.mark.parametrize(
        "rueckmeldungsposition, expected_json_dict",
        [
            pytest.param(
                example_rueckmeldungsposition,
                {
                    "positionsnummer": "1",
                    "abweichungspositionen": [
                        {
                            "abweichungsgrundCode": "A15",
                            "abweichungsgrundCodeliste": "E_0210",
                            "abweichungsgrundBemerkung": "Umsatzsteuersatz",
                            "zugehoerigeRechnung": "458011",
                            "zugehoerigeBestellung": "foo",
                        },
                    ],
                },
                id="max param test",
            ),
            pytest.param(
                Rueckmeldungsposition(),
                {
                    "positionsnummer": None,
                    "abweichungspositionen": None,
                },
                id="min param test",
            ),
        ],
    )
    def test_serialization_roundtrip(
        self, rueckmeldungsposition: Rueckmeldungsposition, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Rueckmeldungsposition with minimal/maximal attributes.
        """
        assert_serialization_roundtrip(rueckmeldungsposition, expected_json_dict)

    def test_required_field_combinations(self) -> None:
        """
        Test different Rueckmeldungspositionen.
          If one field is given the other is required as well.
        """
        # todo: is this useful?
        with pytest.raises(ValidationError) as excinfo:
            _ = Rueckmeldungsposition(positionsnummer="1")
        assert "1 validation error" in str(excinfo.value)

        with pytest.raises(ValidationError) as excinfo:
            _ = Rueckmeldungsposition(
                abweichungspositionen=[
                    Abweichungsposition(
                        abweichungsgrund_code="A15",
                        abweichungsgrund_codeliste="E_0210",
                        abweichungsgrund_bemerkung="Umsatzsteuersatz",
                        zugehoerige_rechnung="458011",
                        zugehoerige_bestellung="foo",
                    )
                ]
            )
        assert "1 validation error" in str(excinfo.value)
