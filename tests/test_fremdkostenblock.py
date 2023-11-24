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
        "fremdkostenblock, expected_json_dict",
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
                {
                    "kostenblockbezeichnung": "teststring",
                    "kostenpositionen": [
                        {
                            "marktpartnercode": None,
                            "positionstitel": "fremdkostenblocktitel",
                            "einzelpreis": {
                                "wert": Decimal("3.5"),
                                "einheit": Waehrungseinheit.EUR,
                                "bezugswert": Mengeneinheit.KWH,
                                "status": Preisstatus.ENDGUELTIG,
                                "_id": None,
                            },
                            "bis": None,
                            "menge": None,
                            "zeitmenge": None,
                            "artikelbezeichnung": "bsp",
                            "marktpartnername": None,
                            "artikeldetail": None,
                            "von": None,
                            "linkPreisblatt": None,
                            "betragKostenposition": {
                                "wert": Decimal("12.5"),
                                "waehrung": Waehrungseinheit.EUR,
                                "_id": None,
                            },
                            "gebietcodeEic": None,
                            "_id": None,
                        }
                    ],
                    "summeKostenblock": {"wert": Decimal("98240"), "waehrung": Waehrungseinheit.EUR, "_id": None},
                    "_id": None,
                },
                id="maximal attributes",
            ),
            pytest.param(
                Fremdkostenblock(kostenblockbezeichnung="teststring"),
                {
                    "kostenblockbezeichnung": "teststring",
                    "kostenpositionen": None,
                    "summeKostenblock": None,
                    "_id": None,
                },
                id="minimal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(
        self, fremdkostenblock: Fremdkostenblock, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Fremdkostenblock
        """
        assert_serialization_roundtrip(fremdkostenblock, expected_json_dict)
