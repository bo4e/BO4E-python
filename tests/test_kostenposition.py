from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Betrag, Kostenposition, Mengeneinheit, Preis, Preisstatus, Waehrungscode, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_menge import example_menge
from tests.test_sigmoidparameter import example_sigmoidparameter


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
                    zeitmenge=example_menge,
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
                    menge=example_menge,
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
