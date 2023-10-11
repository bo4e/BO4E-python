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
        "regionale_tarifpreis_position",
        [
            pytest.param(
                example_regionale_tarifpreisposition,
                id="all attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, regionale_tarifpreis_position: RegionaleTarifpreisposition) -> None:
        assert_serialization_roundtrip(regionale_tarifpreis_position)
