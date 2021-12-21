from datetime import datetime, timezone
from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.betrag import Betrag
from bo4e.com.fremdkostenposition import Fremdkostenposition, FremdkostenpositionSchema
from bo4e.com.preis import Preis
from bo4e.com.preisstaffel import Preisstaffel
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.waehrungscode import Waehrungscode
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_menge import example_menge  # type:ignore[import]
from tests.test_sigmoidparameter import example_sigmoidparameter  # type:ignore[import]


class TestFremdkostenposition:
    @pytest.mark.parametrize(
        "fremdkostenposition, expected_json_dict",
        [
            pytest.param(
                Fremdkostenposition(
                    positionstitel="Mudders Preisstaffel",
                    von=datetime(2013, 5, 1, tzinfo=timezone.utc),
                    bis=datetime(2014, 5, 1, tzinfo=timezone.utc),
                    artikelbezeichnung="Dei Mudder ihr Preisstaffel",
                    link_preisblatt=None,
                    zeitmenge=None,
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
                    menge=None,
                    artikeldetail=None,
                    marktpartnercode=None,
                    marktpartnername=None,
                    gebietcode_eic=None,
                ),
                {
                    "einzelpreis": {"wert": "3.5", "status": "ENDGUELTIG", "bezugswert": "KWH", "einheit": "EUR"},
                    "bis": "2014-05-01T00:00:00+00:00",
                    "artikeldetail": None,
                    "positionstitel": "Mudders Preisstaffel",
                    "artikelbezeichnung": "Dei Mudder ihr Preisstaffel",
                    "von": "2013-05-01T00:00:00+00:00",
                    "marktpartnercode": None,
                    "menge": None,
                    "marktpartnername": None,
                    "zeitmenge": None,
                    "gebietcodeEic": None,
                    "betragKostenposition": {"wert": "12.5", "waehrung": "EUR"},
                    "linkPreisblatt": None,
                },
            ),
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
                {
                    "marktpartnername": "Mein MP",
                    "artikelbezeichnung": "Deim Vadder sei Preisstaffel",
                    "menge": {"einheit": "MWH", "wert": "3.410000000000000142108547152020037174224853515625"},
                    "artikeldetail": "foo",
                    "zeitmenge": {"einheit": "MWH", "wert": "3.410000000000000142108547152020037174224853515625"},
                    "positionstitel": "Vadders Preisstaffel",
                    "marktpartnercode": "986543210123",
                    "bis": "2014-05-01T00:00:00+00:00",
                    "von": "2013-05-01T00:00:00+00:00",
                    "einzelpreis": {"einheit": "EUR", "status": "ENDGUELTIG", "wert": "3.5", "bezugswert": "KWH"},
                    "betragKostenposition": {"wert": "12.5", "waehrung": "EUR"},
                    "gebietcodeEic": "not an eic code but validation will follow in ticket 146",
                    "linkPreisblatt": "http://foo.bar/",
                },
            ),
        ],
    )
    def test_serialization_roundtrip(self, fremdkostenposition: Fremdkostenposition, expected_json_dict: dict):
        """
        Test de-/serialisation of Fremdkostenposition.
        """
        assert_serialization_roundtrip(fremdkostenposition, FremdkostenpositionSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Fremdkostenposition()

        assert "missing 13 required" in str(excinfo.value)
