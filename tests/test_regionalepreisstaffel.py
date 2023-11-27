from decimal import Decimal

import pytest

from bo4e import (
    Gueltigkeitstyp,
    KriteriumWert,
    RegionaleGueltigkeit,
    RegionalePreisstaffel,
    Sigmoidparameter,
    Tarifregionskriterium,
)
from tests.serialization_helper import assert_serialization_roundtrip

example_regionale_preisstaffel = RegionalePreisstaffel(
    einheitspreis=Decimal(40.0),
    staffelgrenze_von=Decimal(12.5),
    staffelgrenze_bis=Decimal(25.0),
    sigmoidparameter=Sigmoidparameter(),
    regionale_gueltigkeit=RegionaleGueltigkeit(
        gueltigkeitstyp=Gueltigkeitstyp.NUR_IN,
        kriteriums_werte=[KriteriumWert(kriterium=Tarifregionskriterium.POSTLEITZAHL, wert="01069")],
    ),
)


class TestRegionalePreisstaffel:
    @pytest.mark.parametrize(
        "regionale_preisstaffel",
        [
            pytest.param(
                RegionalePreisstaffel(
                    einheitspreis=Decimal(40.0),
                    staffelgrenze_von=Decimal(12.5),
                    staffelgrenze_bis=Decimal(25.0),
                    sigmoidparameter=Sigmoidparameter(),
                    regionale_gueltigkeit=RegionaleGueltigkeit(
                        gueltigkeitstyp=Gueltigkeitstyp.NUR_IN,
                        kriteriums_werte=[KriteriumWert(kriterium=Tarifregionskriterium.POSTLEITZAHL, wert="01069")],
                    ),
                ),
                id="maximal attributes"
                # the messing sigmoidparameter is tested in the Preisstaffel tests
            ),
        ],
    )
    def test_serialization_roundtrip(
        self,
        regionale_preisstaffel: RegionalePreisstaffel,
    ) -> None:
        """
        Test de-/serialisation of RegionalePreisgarantie with maximal attributes.
        """
        assert_serialization_roundtrip(regionale_preisstaffel)
