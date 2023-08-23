from datetime import datetime
from typing import Any, Dict

import pytest
from _decimal import Decimal

from bo4e.com.abweichung import Abweichung
from bo4e.com.abweichungsposition import Abweichungsposition
from bo4e.com.avisposition import Avisposition
from bo4e.com.betrag import Betrag
from bo4e.com.rueckmeldungsposition import Rueckmeldungsposition
from bo4e.enum.abweichungsgrund import Abweichungsgrund
from bo4e.enum.waehrungscode import Waehrungscode
from tests.serialization_helper import assert_serialization_roundtrip

#: full example
example_full_avisposition = Avisposition(
    rechnungs_nummer="12345",
    rechnungs_datum=datetime(2022, 1, 1, 0, 0, 0),
    ist_storno=True,
    gesamtbrutto=Betrag(
        wert=Decimal(100.5),
        waehrung=Waehrungscode.EUR,
    ),
    zu_zahlen=Betrag(
        wert=Decimal(15.5),
        waehrung=Waehrungscode.EUR,
    ),
    ist_selbstausgestellt=True,
    referenz="1234",
    abweichungen=[
        Abweichung(
            abweichungsgrund=Abweichungsgrund.UNBEKANNTE_MARKTLOKATION_MESSLOKATION,
            abweichungsgrund_bemerkung="sonst",
            zugehoerige_rechnung="458011",
            abschlagsrechnung="4580112",
            abweichungsgrund_code="14",
            abweichungsgrund_codeliste="G_0081",
        ),
        Abweichung(
            abweichungsgrund=Abweichungsgrund.SONSTIGER_ABWEICHUNGSGRUND,
            abweichungsgrund_bemerkung="sonst",
            zugehoerige_rechnung="458011",
            abschlagsrechnung="foo8",
            abweichungsgrund_code="foo9",
            abweichungsgrund_codeliste="foo0",
        ),
    ],
    positionen=[
        Rueckmeldungsposition(
            positionsnummer="1",
            abweichungspositionen=[
                Abweichungsposition(
                    abweichungsgrund_code="foo11",
                    abweichungsgrund_codeliste="foo12",
                    abweichungsgrund_bemerkung="foo13",
                    zugehoerige_rechnung="458011",
                    zugehoerige_bestellung="foo15",
                ),
                Abweichungsposition(
                    abweichungsgrund_code="foo21",
                    abweichungsgrund_codeliste="foo22",
                    abweichungsgrund_bemerkung="foo23",
                    zugehoerige_rechnung="458011",
                    zugehoerige_bestellung="foo25",
                ),
            ],
        ),
        Rueckmeldungsposition(
            positionsnummer="2",
            abweichungspositionen=[
                Abweichungsposition(
                    abweichungsgrund_code="foo111",
                    abweichungsgrund_codeliste="foo112",
                    abweichungsgrund_bemerkung="foo113",
                    zugehoerige_rechnung="458011",
                    zugehoerige_bestellung="foo115",
                ),
                Abweichungsposition(
                    abweichungsgrund_code="foo221",
                    abweichungsgrund_codeliste="foo222",
                    abweichungsgrund_bemerkung="foo223",
                    zugehoerige_rechnung="458011",
                    zugehoerige_bestellung="foo225",
                ),
            ],
        ),
    ],
)

example_min_avisposition = Avisposition(
    rechnungs_nummer="12345",
    rechnungs_datum=datetime(2022, 1, 1, 0, 0, 0),
    ist_storno=True,
    gesamtbrutto=Betrag(
        wert=Decimal(100.5),
        waehrung=Waehrungscode.EUR,
    ),
    zu_zahlen=Betrag(
        wert=Decimal(15.5),
        waehrung=Waehrungscode.EUR,
    ),
)


class TestAvisposition:
    @pytest.mark.parametrize(
        "avisposition, expected_json_dict",
        [
            pytest.param(
                example_full_avisposition,
                {
                    "rechnungsNummer": "12345",
                    "rechnungsDatum": datetime(2022, 1, 1, 0, 0, 0),
                    "istStorno": True,
                    "gesamtbrutto": {
                        "wert": Decimal(100.5),
                        "waehrung": Waehrungscode.EUR,
                    },
                    "zuZahlen": {
                        "wert": Decimal(15.5),
                        "waehrung": Waehrungscode.EUR,
                    },
                    "istSelbstausgestellt": True,
                    "referenz": "1234",
                    "abweichungen": [
                        {
                            "abweichungsgrund": Abweichungsgrund.UNBEKANNTE_MARKTLOKATION_MESSLOKATION,
                            "abweichungsgrundBemerkung": "sonst",
                            "zugehoerigeRechnung": "458011",
                            "abschlagsrechnung": "4580112",
                            "abweichungsgrundCode": "14",
                            "abweichungsgrundCodeliste": "G_0081",
                        },
                        {
                            "abweichungsgrund": Abweichungsgrund.SONSTIGER_ABWEICHUNGSGRUND,
                            "abweichungsgrundBemerkung": "sonst",
                            "zugehoerigeRechnung": "458011",
                            "abschlagsrechnung": "foo8",
                            "abweichungsgrundCode": "foo9",
                            "abweichungsgrundCodeliste": "foo0",
                        },
                    ],
                    "positionen": [
                        {
                            "positionsnummer": "1",
                            "abweichungspositionen": [
                                {
                                    "abweichungsgrundCode": "foo11",
                                    "abweichungsgrundCodeliste": "foo12",
                                    "abweichungsgrundBemerkung": "foo13",
                                    "zugehoerigeRechnung": "458011",
                                    "zugehoerigeBestellung": "foo15",
                                },
                                {
                                    "abweichungsgrundCode": "foo21",
                                    "abweichungsgrundCodeliste": "foo22",
                                    "abweichungsgrundBemerkung": "foo23",
                                    "zugehoerigeRechnung": "458011",
                                    "zugehoerigeBestellung": "foo25",
                                },
                            ],
                        },
                        {
                            "positionsnummer": "2",
                            "abweichungspositionen": [
                                {
                                    "abweichungsgrundCode": "foo111",
                                    "abweichungsgrundCodeliste": "foo112",
                                    "abweichungsgrundBemerkung": "foo113",
                                    "zugehoerigeRechnung": "458011",
                                    "zugehoerigeBestellung": "foo115",
                                },
                                {
                                    "abweichungsgrundCode": "foo221",
                                    "abweichungsgrundCodeliste": "foo222",
                                    "abweichungsgrundBemerkung": "foo223",
                                    "zugehoerigeRechnung": "458011",
                                    "zugehoerigeBestellung": "foo225",
                                },
                            ],
                        },
                    ],
                },
                id="max param test",
            ),
            pytest.param(
                example_min_avisposition,
                {
                    "rechnungsNummer": "12345",
                    "rechnungsDatum": datetime(2022, 1, 1, 0, 0, 0),
                    "istStorno": True,
                    "gesamtbrutto": {
                        "wert": Decimal(100.5),
                        "waehrung": Waehrungscode.EUR,
                    },
                    "zuZahlen": {
                        "wert": Decimal(15.5),
                        "waehrung": Waehrungscode.EUR,
                    },
                    "istSelbstausgestellt": None,
                    "referenz": None,
                    "abweichungen": None,
                    "positionen": None,
                },
                id="min param test",
            ),
        ],
    )
    def test_serialization_roundtrip(self, avisposition: Avisposition, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of Avisposition with minimal attributes.
        """
        assert_serialization_roundtrip(avisposition, expected_json_dict)
