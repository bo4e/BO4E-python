from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.kriteriumwert import KriteriumWert
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit
from bo4e.com.regionalepreisstaffel import RegionalePreisstaffel
from bo4e.com.regionaletarifpreisposition import RegionaleTarifpreisposition
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preistyp import Preistyp
from bo4e.enum.tarifregionskriterium import Tarifregionskriterium
from bo4e.enum.waehrungseinheit import Waehrungseinheit
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
                                "kriteriumsWerte": [{"kriterium": Tarifregionskriterium.POSTLEITZAHL, "wert": "01069"}],
                            },
                            "einheitspreis": Decimal("40"),
                            "sigmoidparameter": {
                                "A": Decimal("1"),
                                "B": Decimal("2"),
                                "C": Decimal("3"),
                                "D": Decimal("4"),
                            },
                            "staffelgrenzeVon": Decimal("12.5"),
                            "staffelgrenzeBis": Decimal("25"),
                        }
                    ],
                    "einheit": Waehrungseinheit.EUR,
                    "mengeneinheitstaffel": Mengeneinheit.WH,
                    "preistyp": "ARBEITSPREIS_NT",
                },
                id="all attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(
        self, regionale_tarifpreis_position: RegionaleTarifpreisposition, expected_json_dict: Dict[str, Any]
    ) -> None:
        assert_serialization_roundtrip(regionale_tarifpreis_position, expected_json_dict)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = RegionaleTarifpreisposition()  # type: ignore[call-arg]

        assert "4 validation errors" in str(excinfo.value)
