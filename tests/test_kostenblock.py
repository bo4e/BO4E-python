from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.betrag import Betrag
from bo4e.com.kostenblock import Kostenblock, KostenblockSchema
from bo4e.com.kostenposition import Kostenposition
from bo4e.com.preis import Preis
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.waehrungscode import Waehrungscode
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_sigmoidparameter import example_sigmoidparameter  # type:ignore[import]


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
                                "einheit": "EUR",
                                "status": "ENDGUELTIG",
                                "bezugswert": "KWH",
                                "wert": "3.5",
                            },
                            "menge": None,
                            "zeitmenge": None,
                            "von": None,
                            "artikelbezeichnung": "Dei Mudder ihr kostenposition",
                            "artikeldetail": None,
                            "bis": None,
                            "betragKostenposition": {"waehrung": "EUR", "wert": "12.5"},
                        }
                    ],
                    "summeKostenblock": {"waehrung": "EUR", "wert": "12.5"},
                },
                id="maximal",
            ),
        ],
    )
    def test_serialization_roundtrip(self, kostenblock: Kostenblock, expected_json_dict: dict):
        """
        Test de-/serialisation of kostenblock.
        """
        assert_serialization_roundtrip(kostenblock, KostenblockSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Kostenblock()

        assert "missing 1 required" in str(excinfo.value)
