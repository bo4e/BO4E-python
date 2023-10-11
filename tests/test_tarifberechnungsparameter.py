from decimal import Decimal

import pytest

from bo4e import (
    Fremdkostenposition,
    Messpreistyp,
    Preis,
    Tarifberechnungsparameter,
    Tarifkalkulationsmethode,
    Tarifpreis,
)
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_preis import example_preis
from tests.test_tarifpreis import example_tarifpreis

example_tarifberechnungsparameter = Tarifberechnungsparameter(
    berechnungsmethode=Tarifkalkulationsmethode.ZONEN,
    ist_messpreis_in_grundpreis_enthalten=True,
    ist_messpreis_zu_beruecksichtigen=True,
    messpreistyp=Messpreistyp.MESSPREIS_G6,
    kw_inklusive=Decimal(12.5),
    kw_weitere_mengen=Decimal(12.5),
    hoechstpreis_n_t=Preis(),
    hoechstpreis_h_t=Preis(),
    mindestpreis=Preis(),
    zusatzpreise=[Tarifpreis()],
)


class TestFremdkostenposition:
    @pytest.mark.parametrize(
        "tarifberechnungsparameter",
        [
            pytest.param(
                example_tarifberechnungsparameter,
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifberechnungsparameter: Fremdkostenposition) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarifberechnungsparameter)

    def test_missing_required_attribute(self) -> None:
        _ = Tarifberechnungsparameter()
        # ok, we're done. no exception here because there are no required attributes
