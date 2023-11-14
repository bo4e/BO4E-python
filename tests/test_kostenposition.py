from datetime import datetime, timezone
from decimal import Decimal

import pytest

from bo4e import Betrag, Kostenposition, Menge, Mengeneinheit, Preis, Preisstatus, Waehrungscode, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip


class TestKostenposition:
    @pytest.mark.parametrize(
        "kostenposition",
        [
            pytest.param(
                Kostenposition(
                    positionstitel="Vadders Kostenposition",
                    von=datetime(2013, 5, 1, tzinfo=timezone.utc),
                    bis=datetime(2014, 5, 1, tzinfo=timezone.utc),
                    artikelbezeichnung="Deim Vadder sei Kostenposition",
                    zeitmenge=Menge(),
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
                    menge=Menge(),
                    artikeldetail="foo",
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, kostenposition: Kostenposition) -> None:
        """
        Test de-/serialisation of Kostenposition.
        """
        assert_serialization_roundtrip(kostenposition)
