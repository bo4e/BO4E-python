from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.fremdkostenposition import Fremdkostenposition
from bo4e.com.tarifberechnungsparameter import Tarifberechnungsparameter, TarifberechnungsparameterSchema
from bo4e.enum.messpreistyp import Messpreistyp
from bo4e.enum.tarifkalkulationsmethode import Tarifkalkulationsmethode
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_preis import example_preis  # type:ignore[import]
from tests.test_tarifpreis import example_tarifpreis  # type:ignore[import]

example_tarifberechnungsparameter = Tarifberechnungsparameter(
    berechnungsmethode=Tarifkalkulationsmethode.ZONEN,
    messpreis_in_gp_enthalten=True,
    kw_inklusive=Decimal(12.5),
    kw_weitere_mengen=Decimal(12.5),
    messpreistyp=Messpreistyp.MESSPREIS_G6,
    messpreis_beruecksichtigen=True,
    hoechstpreis_h_t=example_preis,
    hoechstpreis_n_t=example_preis,
    mindestpreis=example_preis,
    zusatzpreise=[example_tarifpreis],
)


class TestFremdkostenposition:
    @pytest.mark.parametrize(
        "tarifberechnungsparameter",
        [
            pytest.param(
                example_tarifberechnungsparameter,
                id="maximal attributes",
            ),
            pytest.param(
                Tarifberechnungsparameter(),
                id="minimal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, tarifberechnungsparameter: Fremdkostenposition):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(tarifberechnungsparameter, TarifberechnungsparameterSchema())

    def test_missing_required_attribute(self):
        _ = Tarifberechnungsparameter()
        # ok, we're done. no exception here because there are no required attributes
