from datetime import datetime, timezone

import pytest

from bo4e import Betrag, Fremdkostenposition, Menge, Preis
from tests.serialization_helper import assert_serialization_roundtrip


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
                    zeitmenge=Menge(),
                    einzelpreis=Preis(),
                    betrag_kostenposition=Betrag(),
                    menge=Menge(),
                    artikeldetail="foo",
                    marktpartnercode="986543210123",
                    marktpartnername="Mein MP",
                    gebietcode_eic="not an eic code but validation will follow in ticket 146",
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, fremdkostenposition: Fremdkostenposition) -> None:
        """
        Test de-/serialisation of Fremdkostenposition.
        """
        assert_serialization_roundtrip(fremdkostenposition)
