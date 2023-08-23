from datetime import datetime
from typing import Any, Dict

import pytest
from _decimal import Decimal

from bo4e.bo.avis import Avis
from bo4e.com.abweichung import Abweichung
from bo4e.com.abweichungsposition import Abweichungsposition
from bo4e.com.avisposition import Avisposition
from bo4e.com.betrag import Betrag
from bo4e.com.rueckmeldungsposition import Rueckmeldungsposition
from bo4e.enum.abweichungsgrund import Abweichungsgrund
from bo4e.enum.avistyp import AvisTyp
from bo4e.enum.botyp import BoTyp
from bo4e.enum.waehrungscode import Waehrungscode
from tests.serialization_helper import assert_serialization_roundtrip

#: full example
example_full_avis = Avis(
    avis_nummer="2",
    avis_typ=AvisTyp.ZAHLUNGSAVIS,
    positionen=[
        Avisposition(
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
            referenz="foo1",
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
                    abweichungsgrund=Abweichungsgrund.VORAUSBEZAHLTER_BETRAG_FALSCH,
                    abweichungsgrund_bemerkung="foo6",
                    zugehoerige_rechnung="foo7",
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
                            zugehoerige_rechnung="foo14",
                            zugehoerige_bestellung="foo15",
                        ),
                        Abweichungsposition(
                            abweichungsgrund_code="foo21",
                            abweichungsgrund_codeliste="foo22",
                            abweichungsgrund_bemerkung="foo23",
                            zugehoerige_rechnung="foo24",
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
                            zugehoerige_rechnung="foo114",
                            zugehoerige_bestellung="foo115",
                        ),
                        Abweichungsposition(
                            abweichungsgrund_code="foo221",
                            abweichungsgrund_codeliste="foo222",
                            abweichungsgrund_bemerkung="foo223",
                            zugehoerige_rechnung="foo224",
                            zugehoerige_bestellung="foo225",
                        ),
                    ],
                ),
            ],
        ),
        Avisposition(
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
        ),
    ],
    zu_zahlen=Betrag(
        wert=Decimal(15.5),
        waehrung=Waehrungscode.EUR,
    ),
)
#: min example
example_min_avis = Avis(
    avis_nummer="2",
    avis_typ=AvisTyp.ZAHLUNGSAVIS,
    positionen=[
        Avisposition(
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
        ),
        Avisposition(
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
        ),
    ],
    zu_zahlen=Betrag(
        wert=Decimal(15.5),
        waehrung=Waehrungscode.EUR,
    ),
)


class TestAvis:
    @pytest.mark.parametrize(
        "avis, expected_json_dict",
        [
            pytest.param(
                example_full_avis,
                {
                    "versionstruktur": "2",
                    "boTyp": BoTyp.AVIS,
                    "externeReferenzen": [],
                    "avisNummer": "2",
                    "avisTyp": AvisTyp.ZAHLUNGSAVIS,
                    "positionen": [
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
                            "referenz": "foo1",
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
                                    "abweichungsgrund": Abweichungsgrund.VORAUSBEZAHLTER_BETRAG_FALSCH,
                                    "abweichungsgrundBemerkung": "foo6",
                                    "zugehoerigeRechnung": "foo7",
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
                                            "zugehoerigeRechnung": "foo14",
                                            "zugehoerigeBestellung": "foo15",
                                        },
                                        {
                                            "abweichungsgrundCode": "foo21",
                                            "abweichungsgrundCodeliste": "foo22",
                                            "abweichungsgrundBemerkung": "foo23",
                                            "zugehoerigeRechnung": "foo24",
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
                                            "zugehoerigeRechnung": "foo114",
                                            "zugehoerigeBestellung": "foo115",
                                        },
                                        {
                                            "abweichungsgrundCode": "foo221",
                                            "abweichungsgrundCodeliste": "foo222",
                                            "abweichungsgrundBemerkung": "foo223",
                                            "zugehoerigeRechnung": "foo224",
                                            "zugehoerigeBestellung": "foo225",
                                        },
                                    ],
                                },
                            ],
                        },
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
                    ],
                    "zuZahlen": {
                        "wert": Decimal(15.5),
                        "waehrung": Waehrungscode.EUR,
                    },
                },
                id="full param test",
            ),
            pytest.param(
                example_min_avis,
                {
                    "versionstruktur": "2",
                    "boTyp": BoTyp.AVIS,
                    "externeReferenzen": [],
                    "avisNummer": "2",
                    "avisTyp": AvisTyp.ZAHLUNGSAVIS,
                    "positionen": [
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
                    ],
                    "zuZahlen": {
                        "wert": Decimal(15.5),
                        "waehrung": Waehrungscode.EUR,
                    },
                },
                id="min param test",
            ),
        ],
    )
    def test_serialization_roundtrip(self, avis: Avis, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of Avis with minimal attributes.
        """
        assert_serialization_roundtrip(avis, expected_json_dict)
