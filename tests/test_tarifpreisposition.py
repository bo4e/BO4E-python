from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.preisstaffel import Preisstaffel
from bo4e.com.tarifpreisposition import Tarifpreisposition, TarifpreispositionSchema
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preistyp import Preistyp
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestTarifpreisposition:
    @pytest.mark.parametrize(
        "tarifpreisposition, expected_json_dict",
        [
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
                ),
                {
                    "preistyp": "ENTGELT_ABLESUNG",
                    "einheit": "EUR",
                    "bezugseinheit": "KWH",
                    "preisstaffeln": [
                        {
                            "einheitspreis": "40",
                            "sigmoidparameter": None,
                            "staffelgrenzeBis": "25",
                            "staffelgrenzeVon": "12.5",
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
                            "einheitspreis": "40",
                            "sigmoidparameter": None,
                            "staffelgrenzeBis": "25",
                            "staffelgrenzeVon": "12.5",
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
        assert_serialization_roundtrip(tarifpreisposition, TarifpreispositionSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Tarifpreisposition()

        assert "missing 4 required" in str(excinfo.value)

    def test_tarifpreisposition_betraege_required(self):
        with pytest.raises(ValueError) as excinfo:
            _ = Tarifpreisposition(
                preistyp=Preistyp.ENTGELT_ABLESUNG,
                einheit=Waehrungseinheit.EUR,
                bezugseinheit=Mengeneinheit.KWH,
                preisstaffeln=[],
            )

        assert "List preisstaffeln must not be empty." in str(excinfo.value)
