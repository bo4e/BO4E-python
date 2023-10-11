from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import (
    Gueltigkeitstyp,
    KriteriumWert,
    Mengeneinheit,
    Preistyp,
    RegionaleGueltigkeit,
    RegionalePreisstaffel,
    RegionaleTarifpreisposition,
    Tarifregionskriterium,
    Waehrungseinheit,
)
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_sigmoidparameter import example_sigmoidparameter

example_regionale_tarifpreisposition = RegionaleTarifpreisposition(
    preistyp=Preistyp.ARBEITSPREIS_NT,
    einheit=Waehrungseinheit.EUR,
    bezugseinheit=Mengeneinheit.KWH,
    mengeneinheitstaffel=Mengeneinheit.WH,
    preisstaffeln=[
        RegionalePreisstaffel(
            einheitspreis=Decimal(40.0),
            staffelgrenze_von=Decimal(12.5),
            staffelgrenze_bis=Decimal(25.0),
            sigmoidparameter=example_sigmoidparameter,
            regionale_gueltigkeit=RegionaleGueltigkeit(
                gueltigkeitstyp=Gueltigkeitstyp.NUR_IN,
                kriteriums_werte=[KriteriumWert(kriterium=Tarifregionskriterium.POSTLEITZAHL, wert="01069")],
            ),
        ),
    ],
)


class TestRegionaleTarifpreisPosition:
    @pytest.mark.parametrize(
        "regionale_tarifpreis_position, expected_json_dict",
        [
            pytest.param(
                example_regionale_tarifpreisposition,
                {
                    "bezugseinheit": Mengeneinheit.KWH,
                    "preisstaffeln": [
                        {
                            "regionaleGueltigkeit": {
                                "gueltigkeitstyp": "NUR_IN",
                                "kriteriumsWerte": [
                                    {"kriterium": Tarifregionskriterium.POSTLEITZAHL, "wert": "01069", "_id": None}
                                ],
                                "_id": None,
                            },
                            "einheitspreis": Decimal("40"),
                            "sigmoidparameter": {
                                "A": Decimal("1"),
                                "B": Decimal("2"),
                                "C": Decimal("3"),
                                "D": Decimal("4"),
                                "_id": None,
                            },
                            "staffelgrenzeVon": Decimal("12.5"),
                            "staffelgrenzeBis": Decimal("25"),
                            "_id": None,
                        }
                    ],
                    "einheit": Waehrungseinheit.EUR,
                    "mengeneinheitstaffel": Mengeneinheit.WH,
                    "preistyp": "ARBEITSPREIS_NT",
                    "_id": None,
                },
                id="all attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(
        self, regionale_tarifpreis_position: RegionaleTarifpreisposition, expected_json_dict: Dict[str, Any]
    ) -> None:
        assert_serialization_roundtrip(regionale_tarifpreis_position, expected_json_dict)
