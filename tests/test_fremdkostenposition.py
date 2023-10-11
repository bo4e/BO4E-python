from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Betrag, Fremdkostenposition, Mengeneinheit, Preis, Preisstatus, Waehrungscode, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_menge import example_menge
from tests.test_sigmoidparameter import example_sigmoidparameter


class TestFremdkostenposition:
    @pytest.mark.parametrize(
        "fremdkostenposition",
        [
            pytest.param(
                Fremdkostenposition(
                    positionstitel="Vadders Preisstaffel",
                    von=datetime(2013, 5, 1, tzinfo=timezone.utc),
                    bis=datetime(2014, 5, 1, tzinfo=timezone.utc),
                    artikelbezeichnung="Deim Vadder sei Preisstaffel",
                    link_preisblatt="http://foo.bar/",
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
                    marktpartnercode="986543210123",
                    marktpartnername="Mein MP",
                    gebietcode_eic="not an eic code but validation will follow in ticket 146",
                ),
                id="required and optional attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, fremdkostenposition: Fremdkostenposition) -> None:
        """
        Test de-/serialisation of Fremdkostenposition.
        """
        assert_serialization_roundtrip(fremdkostenposition)
