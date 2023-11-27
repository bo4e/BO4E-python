from decimal import Decimal

import pytest

from bo4e import Betrag, Kostenblock, Kostenposition, Mengeneinheit, Preis, Preisstatus, Waehrungscode, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip


class TestKostenblock:
    @pytest.mark.parametrize(
        "kostenblock",
        [
            pytest.param(
                Kostenblock(
                    kostenblockbezeichnung="Mein Kostenblock",
                    summe_kostenblock=Betrag(
                        waehrung=Waehrungscode.EUR,
                        wert=Decimal(12.5),
                    ),
                    kostenpositionen=[
                        Kostenposition(
                            positionstitel="Mudders kostenposition",
                            artikelbezeichnung="Dei Mudder ihr kostenposition",
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
                        ),
                    ],
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, kostenblock: Kostenblock) -> None:
        """
        Test de-/serialisation of kostenblock.
        """
        assert_serialization_roundtrip(kostenblock)
