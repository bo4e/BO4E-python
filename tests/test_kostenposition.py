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
                    "positionstitel": "Mudders Preisstaffel",
                    "einzelpreis": {"status": "ENDGUELTIG", "einheit": "EUR", "wert": "3.5", "bezugswert": "KWH"},
                    "bis": None,
                    "von": None,
                    "menge": None,
                    "zeitmenge": None,
                    "artikelbezeichnung": "Dei Mudder ihr Preisstaffel",
                    "artikeldetail": None,
                    "betragKostenposition": {"waehrung": "EUR", "wert": "12.5"},
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
                    "menge": {"wert": "3.410000000000000142108547152020037174224853515625", "einheit": "MWH"},
                    "artikeldetail": "foo",
                    "einzelpreis": {"bezugswert": "KWH", "status": "ENDGUELTIG", "wert": "3.5", "einheit": "EUR"},
                    "von": "2013-05-01T00:00:00+00:00",
                    "zeitmenge": {"wert": "3.410000000000000142108547152020037174224853515625", "einheit": "MWH"},
                    "bis": "2014-05-01T00:00:00+00:00",
                    "betragKostenposition": {"wert": "12.5", "waehrung": "EUR"},
                },
                id="required and optional attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, kostenposition: Kostenposition, expected_json_dict: dict):
        """
        Test de-/serialisation of Kostenposition
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
