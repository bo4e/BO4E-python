from datetime import datetime
from typing import Any, Dict

import pytest
from _decimal import Decimal
from pydantic import ValidationError

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
    avis_nummer="654321",
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
                    abschlagsrechnung="4580112",
                    abweichungsgrund_code="28",
                    abweichungsgrund_codeliste="G_0081",
                ),
            ],
            positionen=[
                Rueckmeldungsposition(
                    positionsnummer="1",
                    abweichungspositionen=[
                        Abweichungsposition(
                            abweichungsgrund_code="foo",
                            abweichungsgrund_codeliste="foo",
                            abweichungsgrund_bemerkung="foo",
                            zugehoerige_rechnung="458011",
                            zugehoerige_bestellung="foo",
                        ),
                        Abweichungsposition(
                            abweichungsgrund_code="foo",
                            abweichungsgrund_codeliste="foo",
                            abweichungsgrund_bemerkung="foo",
                            zugehoerige_rechnung="458011",
                            zugehoerige_bestellung="foo",
                        ),
                    ],
                ),
                Rueckmeldungsposition(
                    positionsnummer="2",
                    abweichungspositionen=[
                        Abweichungsposition(
                            abweichungsgrund_code="foo",
                            abweichungsgrund_codeliste="foo",
                            abweichungsgrund_bemerkung="foo",
                            zugehoerige_rechnung="458011",
                            zugehoerige_bestellung="foo",
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
    avis_nummer="654321",
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
        )
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
                    "avisNummer": "654321",
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
                                    "abschlagsrechnung": "4580112",
                                    "abweichungsgrundCode": "28",
                                    "abweichungsgrundCodeliste": "G_0081",
                                },
                            ],
                            "positionen": [
                                {
                                    "positionsnummer": "1",
                                    "abweichungspositionen": [
                                        {
                                            "abweichungsgrundCode": "foo",
                                            "abweichungsgrundCodeliste": "foo",
                                            "abweichungsgrundBemerkung": "foo",
                                            "zugehoerigeRechnung": "458011",
                                            "zugehoerigeBestellung": "foo",
                                        },
                                        {
                                            "abweichungsgrundCode": "foo",
                                            "abweichungsgrundCodeliste": "foo",
                                            "abweichungsgrundBemerkung": "foo",
                                            "zugehoerigeRechnung": "458011",
                                            "zugehoerigeBestellung": "foo",
                                        },
                                    ],
                                },
                                {
                                    "positionsnummer": "2",
                                    "abweichungspositionen": [
                                        {
                                            "abweichungsgrundCode": "foo",
                                            "abweichungsgrundCodeliste": "foo",
                                            "abweichungsgrundBemerkung": "foo",
                                            "zugehoerigeRechnung": "458011",
                                            "zugehoerigeBestellung": "foo",
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
                    "avisNummer": "654321",
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

    def test_missing_required_attribute(self) -> None:
        """
        Check if missing required attributes are identified correctly
        """
        with pytest.raises(ValidationError) as excinfo:
            _ = Avis()  # type: ignore[call-arg]
        assert "4 validation errors" in str(excinfo.value)
