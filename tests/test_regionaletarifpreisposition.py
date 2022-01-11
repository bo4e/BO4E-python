from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.kriteriumwert import KriteriumWert
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit
from bo4e.com.regionalepreisstaffel import RegionalePreisstaffel
from bo4e.com.regionaletarifpreisposition import RegionaleTarifpreisposition, RegionaleTarifpreispositionSchema
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preistyp import Preistyp
from bo4e.enum.tarifregionskriterium import Tarifregionskriterium
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_sigmoidparameter import example_sigmoidparameter  # type:ignore[import]


class TestRegionaleTarifpreisPosition:
    @pytest.mark.parametrize(
        "regionale_tarifpreis_position, expected_json_dict",
        [
            pytest.param(
                RegionaleTarifpreisposition(
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
                                kriteriums_werte=[
                                    KriteriumWert(kriterium=Tarifregionskriterium.POSTLEITZAHL, wert="01069")
                                ],
                            ),
                        ),
                    ],
                ),
                {
                    "bezugseinheit": "KWH",
                    "preisstaffeln": [
                        {
                            "regionaleGueltigkeit": {
                                "gueltigkeitstyp": "NUR_IN",
                                "kriteriumsWerte": [{"kriterium": "POSTLEITZAHL", "wert": "01069"}],
                            },
                            "einheitspreis": "40",
                            "sigmoidparameter": {"a": "1", "b": "2", "c": "3", "d": "4"},
                            "staffelgrenzeVon": "12.5",
                            "staffelgrenzeBis": "25",
                        }
                    ],
                    "einheit": "EUR",
                    "mengeneinheitstaffel": "WH",
                    "preistyp": "ARBEITSPREIS_NT",
                },
                id="all attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(
        self, regionale_tarifpreis_position: RegionaleTarifpreisposition, expected_json_dict: dict
    ):
        assert_serialization_roundtrip(
            regionale_tarifpreis_position, RegionaleTarifpreispositionSchema(), expected_json_dict
        )

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = RegionaleTarifpreisposition()

        assert "missing 4 required" in str(excinfo.value)
