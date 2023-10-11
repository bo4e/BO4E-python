from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import (
    Gueltigkeitstyp,
    KriteriumWert,
    RegionaleGueltigkeit,
    RegionalePreisgarantie,
    RegionalePreisstaffel,
    Tarifregionskriterium,
)
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_sigmoidparameter import example_sigmoidparameter

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
        "regionale_preisstaffel",
        [
            pytest.param(
                example_regionale_preisstaffel,
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
