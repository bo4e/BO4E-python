from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.betrag import Betrag
from bo4e.com.fremdkostenblock import Fremdkostenblock, FremdkostenblockSchema
from bo4e.com.fremdkostenposition import Fremdkostenposition
from bo4e.com.preis import Preis
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.waehrungscode import Waehrungscode
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


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
                                "wert": "3.5",
                                "einheit": "EUR",
                                "bezugswert": "KWH",
                                "status": "ENDGUELTIG",
                            },
                            "bis": None,
                            "menge": None,
                            "zeitmenge": None,
                            "artikelbezeichnung": "bsp",
                            "marktpartnername": None,
                            "artikeldetail": None,
                            "von": None,
                            "linkPreisblatt": None,
                            "betragKostenposition": {"wert": "12.5", "waehrung": "EUR"},
                            "gebietcodeEic": None,
                        }
                    ],
                    "summeKostenblock": {"wert": "98240", "waehrung": "EUR"},
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
    def test_serialization_roundtrip(self, fremdkostenblock, expected_json_dict):
        """
        Test de-/serialisation of Fremdkostenblock
        """
        assert_serialization_roundtrip(fremdkostenblock, FremdkostenblockSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Fremdkostenblock()
        assert "missing 1 required" in str(excinfo.value)
