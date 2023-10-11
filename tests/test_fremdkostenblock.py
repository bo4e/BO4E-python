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
                    kostenpositionen=[
                        Fremdkostenposition(
                            positionstitel="fremdkostenblocktitel",
                            artikelbezeichnung="bsp",
                            einzelpreis=Preis(
                                wert=Decimal(3.50),
                                einheit=Waehrungseinheit.EUR,
                                bezugswert=Mengeneinheit.KWH,
                                status=Preisstatus.ENDGUELTIG,
                            ),
                            betrag_kostenposition=Betrag(
                                waehrung=Waehrungscode.EUR,
                                wert=Decimal(12.5),
                            ),
                        )
                    ],
                    summe_kostenblock=Betrag(
                        waehrung=Waehrungscode.EUR,
                        wert=Decimal(98240),
                    ),
                ),
                id="maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, fremdkostenblock: Fremdkostenblock) -> None:
        """
        Test de-/serialisation of Fremdkostenblock
        """
        assert_serialization_roundtrip(fremdkostenblock)
