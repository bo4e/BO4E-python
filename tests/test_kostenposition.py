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
        "kostenposition, expected_json_dict",
        [
            pytest.param(
                Kostenposition(
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
                    "positionstitel": "Mudders Preisstaffel",
                    "einzelpreis": {
                        "status": Preisstatus.ENDGUELTIG,
                        "einheit": Waehrungseinheit.EUR,
                        "wert": Decimal("3.5"),
                        "bezugswert": Mengeneinheit.KWH,
                        "_id": None,
                    },
                    "bis": None,
                    "von": None,
                    "menge": None,
                    "zeitmenge": None,
                    "artikelbezeichnung": "Dei Mudder ihr Preisstaffel",
                    "artikeldetail": None,
                    "betragKostenposition": {"waehrung": Waehrungseinheit.EUR, "wert": Decimal("12.5"), "_id": None},
                    "_id": None,
                },
                id="only required attributes",
            ),
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
                {
                    "artikelbezeichnung": "Deim Vadder sei Kostenposition",
                    "positionstitel": "Vadders Kostenposition",
                    "menge": {
                        "wert": Decimal("3.410000000000000142108547152020037174224853515625"),
                        "einheit": Mengeneinheit.MWH,
                        "_id": None,
                    },
                    "artikeldetail": "foo",
                    "einzelpreis": {
                        "bezugswert": Mengeneinheit.KWH,
                        "status": Preisstatus.ENDGUELTIG,
                        "wert": Decimal("3.5"),
                        "einheit": Waehrungseinheit.EUR,
                        "_id": None,
                    },
                    "von": datetime(2013, 5, 1, 0, 0, tzinfo=timezone.utc),
                    "zeitmenge": {
                        "wert": Decimal("3.410000000000000142108547152020037174224853515625"),
                        "einheit": Mengeneinheit.MWH,
                        "_id": None,
                    },
                    "bis": datetime(2014, 5, 1, 0, 0, tzinfo=timezone.utc),
                    "betragKostenposition": {"wert": Decimal("12.5"), "waehrung": Waehrungseinheit.EUR, "_id": None},
                    "_id": None,
                },
                id="required and optional attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, kostenposition: Kostenposition, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of Kostenposition
        """
        assert_serialization_roundtrip(kostenposition, expected_json_dict)
