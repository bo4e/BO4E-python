from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import (
    Betrag,
    Fremdkostenblock,
    Fremdkostenposition,
    Mengeneinheit,
    Preis,
    Preisstatus,
    Waehrungscode,
    Waehrungseinheit,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestFremdkostenblock:
    @pytest.mark.parametrize(
        "fremdkostenblock",
        [
            pytest.param(
                Fremdkostenblock(
                    kostenblockbezeichnung="teststring",
                    kostenpositionen=[Fremdkostenposition()],
                    summe_kostenblock=Betrag(),
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, fremdkostenblock: Fremdkostenblock) -> None:
        """
        Test de-/serialisation of Fremdkostenblock
        """
        assert_serialization_roundtrip(fremdkostenblock)
