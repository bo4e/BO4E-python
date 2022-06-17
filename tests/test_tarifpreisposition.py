from decimal import Decimal

import pytest  # type:ignore[import]
from pydantic import ValidationError
from bo4e.com.preisstaffel import Preisstaffel
from bo4e.com.tarifpreisposition import Tarifpreisposition, Tarifpreisposition
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preistyp import Preistyp
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]

example_tarifpreisposition = Tarifpreisposition(
    preistyp=Preistyp.ENTGELT_ABLESUNG,
    einheit=Waehrungseinheit.EUR,
    bezugseinheit=Mengeneinheit.KWH,
    preisstaffeln=[
        Preisstaffel(
            einheitspreis=Decimal(40.0),
            staffelgrenze_von=Decimal(12.5),
            staffelgrenze_bis=Decimal(25.0),
        ),
    ],
)


class TestTarifpreisposition:
    @pytest.mark.parametrize(
        "tarifpreisposition, expected_json_dict",
        [
            pytest.param(
                example_tarifpreisposition,
                {
                    "preistyp": "ENTGELT_ABLESUNG",
                    "einheit": "EUR",
                    "bezugseinheit": "KWH",
                    "preisstaffeln": [
                        {
                            "einheitspreis": Decimal("40"),
                            "sigmoidparameter": None,
                            "staffelgrenzeBis": Decimal("25"),
                            "staffelgrenzeVon": Decimal("12.5"),
                        }
                    ],
                    "mengeneinheitstaffel": None,
                },
                id="only required attributes",
            ),
            pytest.param(
                Tarifpreisposition(
                    preistyp=Preistyp.ENTGELT_ABLESUNG,
                    einheit=Waehrungseinheit.EUR,
                    bezugseinheit=Mengeneinheit.KWH,
                    preisstaffeln=[
                        Preisstaffel(
                            einheitspreis=Decimal(40.0),
                            staffelgrenze_von=Decimal(12.5),
                            staffelgrenze_bis=Decimal(25.0),
                        ),
                    ],
                    mengeneinheitstaffel=Mengeneinheit.STUECK,
                ),
                {
                    "preistyp": "ENTGELT_ABLESUNG",
                    "einheit": "EUR",
                    "bezugseinheit": "KWH",
                    "preisstaffeln": [
                        {
                            "einheitspreis": Decimal("40"),
                            "sigmoidparameter": None,
                            "staffelgrenzeBis": Decimal("25"),
                            "staffelgrenzeVon": Decimal("12.5"),
                        }
                    ],
                    "mengeneinheitstaffel": "STUECK",
                },
                id="optional and required attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifpreisposition: Tarifpreisposition, expected_json_dict: dict):
        """
        Test de-/serialisation of Tarifpreisposition.
        """
        assert_serialization_roundtrip(tarifpreisposition, expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(ValidationError) as excinfo:
            _ = Tarifpreisposition()

        assert "4 validation errors" in str(excinfo.value)

    def test_tarifpreisposition_betraege_required(self):
        with pytest.raises(ValidationError) as excinfo:
            _ = Tarifpreisposition(
                preistyp=Preistyp.ENTGELT_ABLESUNG,
                einheit=Waehrungseinheit.EUR,
                bezugseinheit=Mengeneinheit.KWH,
                preisstaffeln=[],
            )

        assert "1 validation error" in str(excinfo.value)
        assert "ensure this value has at least 1 item" in str(excinfo.value)
