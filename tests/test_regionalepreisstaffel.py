from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.kriteriumwert import KriteriumWert
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit
from bo4e.com.regionalepreisgarantie import RegionalePreisgarantie
from bo4e.com.regionalepreisstaffel import RegionalePreisstaffel, RegionalePreisstaffelSchema
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp
from bo4e.enum.tarifregionskriterium import Tarifregionskriterium
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_sigmoidparameter import example_sigmoidparameter  # type:ignore[import]

example_regionale_preisstaffel = RegionalePreisstaffel(
    einheitspreis=Decimal(40.0),
    staffelgrenze_von=Decimal(12.5),
    staffelgrenze_bis=Decimal(25.0),
    sigmoidparameter=example_sigmoidparameter,
    regionale_gueltigkeit=RegionaleGueltigkeit(
        gueltigkeitstyp=Gueltigkeitstyp.NUR_IN,
        kriteriums_werte=[KriteriumWert(kriterium=Tarifregionskriterium.POSTLEITZAHL, wert="01069")],
    ),
)


class TestRegionalePreisstaffel:
    @pytest.mark.parametrize(
        "regionale_preisstaffel, expected_json_dict",
        [
            pytest.param(
                example_regionale_preisstaffel,
                {
                    "regionaleGueltigkeit": {
                        "gueltigkeitstyp": "NUR_IN",
                        "kriteriumsWerte": [{"kriterium": "POSTLEITZAHL", "wert": "01069"}],
                    },
                    "einheitspreis": "40",
                    "sigmoidparameter": {"a": "1", "b": "2", "c": "3", "d": "4"},
                    "staffelgrenzeVon": "12.5",
                    "staffelgrenzeBis": "25",
                },
                id="maximal attributes"
                # the messing sigmoidparameter is tested in the Preisstaffel tests
            ),
        ],
    )
    def test_serialization_roundtrip(self, regionale_preisstaffel: RegionalePreisstaffel, expected_json_dict):
        """
        Test de-/serialisation of RegionalePreisgarantie with maximal attributes.
        """
        assert_serialization_roundtrip(regionale_preisstaffel, RegionalePreisstaffelSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = RegionalePreisgarantie()

        assert "missing 3 required" in str(excinfo.value)
