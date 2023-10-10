from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Betrag, Kostenblock, Kostenposition, Mengeneinheit, Preis, Preisstatus, Waehrungscode, Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_sigmoidparameter import example_sigmoidparameter


class TestKostenblock:
    @pytest.mark.parametrize(
        "kostenblock, expected_json_dict",
        [
            pytest.param(
                Kostenblock(
                    kostenblockbezeichnung="Mein Kostenblock",
                ),
                {
                    "kostenblockbezeichnung": "Mein Kostenblock",
                    "summeKostenblock": None,
                    "kostenpositionen": None,
                    "_id": None,
                },
                id="minimal",
            ),
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
                {
                    "kostenblockbezeichnung": "Mein Kostenblock",
                    "kostenpositionen": [
                        {
                            "positionstitel": "Mudders kostenposition",
                            "einzelpreis": {
                                "einheit": Waehrungseinheit.EUR,
                                "status": Preisstatus.ENDGUELTIG,
                                "bezugswert": Mengeneinheit.KWH,
                                "wert": Decimal("3.5"),
                                "_id": None,
                            },
                            "menge": None,
                            "zeitmenge": None,
                            "von": None,
                            "artikelbezeichnung": "Dei Mudder ihr kostenposition",
                            "artikeldetail": None,
                            "bis": None,
                            "betragKostenposition": {
                                "waehrung": Waehrungseinheit.EUR,
                                "wert": Decimal("12.5"),
                                "_id": None,
                            },
                            "_id": None,
                        }
                    ],
                    "summeKostenblock": {"waehrung": Waehrungseinheit.EUR, "wert": Decimal("12.5"), "_id": None},
                    "_id": None,
                },
                id="maximal",
            ),
        ],
    )
    def test_serialization_roundtrip(self, kostenblock: Kostenblock, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of kostenblock.
        """
        assert_serialization_roundtrip(kostenblock, expected_json_dict)
