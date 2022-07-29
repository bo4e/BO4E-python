from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.betrag import Betrag
from bo4e.com.fremdkostenposition import Fremdkostenposition
from bo4e.com.preis import Preis
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.waehrungscode import Waehrungscode
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_menge import example_menge
from tests.test_sigmoidparameter import example_sigmoidparameter


class TestFremdkostenposition:
    @pytest.mark.parametrize(
        "fremdkostenposition, expected_json_dict",
        [
            pytest.param(
                Fremdkostenposition(
                    positionstitel="Mudders Preisstaffel",
                    artikelbezeichnung="Dei Mudder ihr Preisstaffel",
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
                {
                    "marktpartnercode": None,
                    "positionstitel": "Mudders Preisstaffel",
                    "einzelpreis": {
                        "wert": Decimal("3.5"),
                        "einheit": Waehrungseinheit.EUR,
                        "bezugswert": Mengeneinheit.KWH,
                        "status": Preisstatus.ENDGUELTIG,
                    },
                    "bis": None,
                    "menge": None,
                    "zeitmenge": None,
                    "artikelbezeichnung": "Dei Mudder ihr Preisstaffel",
                    "marktpartnername": None,
                    "artikeldetail": None,
                    "von": None,
                    "linkPreisblatt": None,
                    "betragKostenposition": {"wert": Decimal("12.5"), "waehrung": Waehrungseinheit.EUR},
                    "gebietcodeEic": None,
                },
                id="only required attributes",
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
                    "artikelbezeichnung": "Deim Vadder sei Preisstaffel",
                    "artikeldetail": "foo",
                    "marktpartnername": "Mein MP",
                    "einzelpreis": {
                        "bezugswert": Mengeneinheit.KWH,
                        "status": Preisstatus.ENDGUELTIG,
                        "wert": Decimal("3.5"),
                        "einheit": Waehrungseinheit.EUR,
                    },
                    "menge": {
                        "wert": Decimal("3.410000000000000142108547152020037174224853515625"),
                        "einheit": Mengeneinheit.MWH,
                    },
                    "zeitmenge": {
                        "wert": Decimal("3.410000000000000142108547152020037174224853515625"),
                        "einheit": Mengeneinheit.MWH,
                    },
                    "marktpartnercode": "986543210123",
                    "bis": datetime(2014, 5, 1, 0, 0, tzinfo=timezone.utc),
                    "positionstitel": "Vadders Preisstaffel",
                    "von": datetime(2013, 5, 1, 0, 0, tzinfo=timezone.utc),
                    "betragKostenposition": {"wert": Decimal("12.5"), "waehrung": Waehrungseinheit.EUR},
                    "gebietcodeEic": "not an eic code but validation will follow in ticket 146",
                    "linkPreisblatt": "http://foo.bar/",
                },
                id="required and optional attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(
        self, fremdkostenposition: Fremdkostenposition, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Fremdkostenposition.
        """
        assert_serialization_roundtrip(fremdkostenposition, expected_json_dict)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Fremdkostenposition()  # type: ignore[call-arg]

        assert "4 validation errors" in str(excinfo.value)
