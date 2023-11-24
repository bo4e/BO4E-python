from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Mengeneinheit, Preisstaffel, Preistyp, Tarifpreisposition, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip

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
                    "einheit": Waehrungseinheit.EUR,
                    "bezugseinheit": Mengeneinheit.KWH,
                    "preisstaffeln": [
                        {
                            "einheitspreis": Decimal("40"),
                            "sigmoidparameter": None,
                            "staffelgrenzeBis": Decimal("25"),
                            "staffelgrenzeVon": Decimal("12.5"),
                            "_id": None,
                        }
                    ],
                    "mengeneinheitstaffel": None,
                    "_id": None,
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
                    "einheit": Waehrungseinheit.EUR,
                    "bezugseinheit": Mengeneinheit.KWH,
                    "preisstaffeln": [
                        {
                            "einheitspreis": Decimal("40"),
                            "sigmoidparameter": None,
                            "staffelgrenzeBis": Decimal("25"),
                            "staffelgrenzeVon": Decimal("12.5"),
                            "_id": None,
                        }
                    ],
                    "mengeneinheitstaffel": Mengeneinheit.STUECK,
                    "_id": None,
                },
                id="optional and required attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(
        self, tarifpreisposition: Tarifpreisposition, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Tarifpreisposition.
        """
        assert_serialization_roundtrip(tarifpreisposition, expected_json_dict)
