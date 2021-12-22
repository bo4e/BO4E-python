from datetime import datetime, timezone
from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.betrag import Betrag
from bo4e.com.kostenposition import Kostenposition, KostenpositionSchema
from bo4e.com.preis import Preis
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.preisstatus import Preisstatus
from bo4e.enum.waehrungscode import Waehrungscode
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_menge import example_menge  # type:ignore[import]
from tests.test_sigmoidparameter import example_sigmoidparameter  # type:ignore[import]


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
                    "einzelpreis": {"wert": "3.5", "status": "ENDGUELTIG", "bezugswert": "KWH", "einheit": "EUR"},
                    "bis": None,
                    "artikeldetail": None,
                    "positionstitel": "Mudders Preisstaffel",
                    "artikelbezeichnung": "Dei Mudder ihr Preisstaffel",
                    "von": None,
                    "menge": None,
                    "zeitmenge": None,
                    "betragKostenposition": {"wert": "12.5", "waehrung": "EUR"},
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
                    "marktpartnername": "Mein MP",
                    "artikelbezeichnung": "Deim Vadder sei Kostenposition",
                    "menge": {"einheit": "MWH", "wert": "3.410000000000000142108547152020037174224853515625"},
                    "artikeldetail": "foo",
                    "zeitmenge": {"einheit": "MWH", "wert": "3.410000000000000142108547152020037174224853515625"},
                    "positionstitel": "Vadders Kostenposition",
                    "bis": "2014-05-01T00:00:00+00:00",
                    "von": "2013-05-01T00:00:00+00:00",
                    "einzelpreis": {"einheit": "EUR", "status": "ENDGUELTIG", "wert": "3.5", "bezugswert": "KWH"},
                    "betragKostenposition": {"wert": "12.5", "waehrung": "EUR"},
                },
                id="required and optional attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, kostenposition: Kostenposition, expected_json_dict: dict):
        """
        Test de-/serialisation of Fremdkostenposition.
        """
        assert_serialization_roundtrip(kostenposition, KostenpositionSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Kostenposition()

        assert "missing 4 required" in str(excinfo.value)

    def test_von_bis_validation_attribute(self):
        with pytest.raises(ValueError) as excinfo:
            _ = Kostenposition(
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
                von=datetime(2014, 5, 1, tzinfo=timezone.utc),
                bis=datetime(2013, 5, 1, tzinfo=timezone.utc),
            )

        assert "has to be later than the start" in str(excinfo.value)
