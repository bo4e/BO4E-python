from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.betrag import Betrag
from bo4e.com.fremdkostenblock import Fremdkostenblock
from bo4e.com.fremdkostenposition import Fremdkostenposition
from bo4e.com.preis import Preis
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.waehrungscode import Waehrungscode
from bo4e.enum.waehrungseinheit import Waehrungseinheit
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
                            },
                            "bis": None,
                            "menge": None,
                            "zeitmenge": None,
                            "artikelbezeichnung": "bsp",
                            "marktpartnername": None,
                            "artikeldetail": None,
                            "von": None,
                            "linkPreisblatt": None,
                            "betragKostenposition": {"wert": Decimal("12.5"), "waehrung": Waehrungseinheit.EUR},
                            "gebietcodeEic": None,
                        }
                    ],
                    "summeKostenblock": {"wert": Decimal("98240"), "waehrung": Waehrungseinheit.EUR},
                },
                id="maximal attributes",
            ),
            pytest.param(
                Fremdkostenblock(kostenblockbezeichnung="teststring"),
                {
                    "kostenblockbezeichnung": "teststring",
                    "kostenpositionen": None,
                    "summeKostenblock": None,
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

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Fremdkostenblock()  # type: ignore[call-arg]
        assert "1 validation error" in str(excinfo.value)
