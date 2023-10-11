from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import AufAbschlagstyp, PositionsAufAbschlag, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip


class TestPositionsAufAbschlag:
    @pytest.mark.parametrize(
        "positionsaufabschlag",
        [
            pytest.param(
                PositionsAufAbschlag(
                    bezeichnung="foo",
                    beschreibung="bar",
                    auf_abschlagstyp=AufAbschlagstyp.ABSOLUT,
                    auf_abschlagswert=Decimal(4.25),
                    auf_abschlagswaehrung=Waehrungseinheit.EUR,
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(
        self,
        positionsaufabschlag: PositionsAufAbschlag,
    ) -> None:
        """
        Test de-/serialisation of PositionsAufAbschlag
        """
        assert_serialization_roundtrip(positionsaufabschlag)
