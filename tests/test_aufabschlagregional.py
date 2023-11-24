from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import (
    AufAbschlagProOrt,
    AufAbschlagRegional,
    AufAbschlagstaffelProOrt,
    AufAbschlagstyp,
    AufAbschlagsziel,
    Energieherkunft,
    Energiemix,
    Erzeugungsart,
    Preisgarantie,
    Preisgarantietyp,
    Sparte,
    Tarifeinschraenkung,
    Vertragskonditionen,
    Waehrungseinheit,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip

example_aufabschlagregional = AufAbschlagRegional(
    bezeichnung="foo",
    betraege=[
        AufAbschlagProOrt(
            postleitzahl="01187",
            ort="Dresden",
            netznr="2",
            staffeln=[
                AufAbschlagstaffelProOrt(
                    wert=Decimal(2.5),
                    staffelgrenze_von=Decimal(1),
                    staffelgrenze_bis=Decimal(5),
                )
            ],
        ),
    ],
)


class TestAufAbschlagRegional:
    @pytest.mark.parametrize(
        "aufabschlagregional, expected_json_dict",
        [
            pytest.param(
                example_aufabschlagregional,
                {
                    "bezeichnung": "foo",
                    "betraege": [
                        {
                            "postleitzahl": "01187",
                            "ort": "Dresden",
                            "netznr": "2",
                            "staffeln": [
                                {
                                    "wert": Decimal("2.5"),
                                    "staffelgrenzeVon": Decimal("1"),
                                    "staffelgrenzeBis": Decimal("5"),
                                    "_id": None,
                                }
                            ],
                            "_id": None,
                        },
                    ],
                    "beschreibung": None,
                    "aufAbschlagstyp": None,
                    "aufAbschlagsziel": None,
                    "einheit": None,
                    "website": None,
                    "zusatzprodukte": None,
                    "voraussetzungen": None,
                    "tarifnamensaenderungen": None,
                    "gueltigkeitszeitraum": None,
                    "energiemixaenderung": None,
                    "vertagskonditionsaenderung": None,
                    "garantieaenderung": None,
                    "einschraenkungsaenderung": None,
                    "_id": None,
                },
                id="only required attributes",
            ),
            pytest.param(
                AufAbschlagRegional(
                    bezeichnung="foo",
                    betraege=[
                        AufAbschlagProOrt(
                            postleitzahl="01187",
                            ort="Dresden",
                            netznr="2",
                            staffeln=[
                                AufAbschlagstaffelProOrt(
                                    wert=Decimal(2.5),
                                    staffelgrenze_von=Decimal(1),
                                    staffelgrenze_bis=Decimal(5),
                                )
                            ],
                        ),
                    ],
                    beschreibung="bar",
                    auf_abschlagstyp=AufAbschlagstyp.RELATIV,
                    auf_abschlagsziel=AufAbschlagsziel.ARBEITSPREIS_HT,
                    einheit=Waehrungseinheit.EUR,
                    website="foo.bar",
                    zusatzprodukte=["Asterix", "Obelix"],
                    voraussetzungen=["Petterson", "Findus"],
                    tarifnamensaenderungen="foobar",
                    gueltigkeitszeitraum=Zeitraum(
                        startdatum=datetime(2020, 1, 1, tzinfo=timezone.utc),
                        enddatum=datetime(2020, 4, 1, tzinfo=timezone.utc),
                    ),
                    energiemixaenderung=Energiemix(
                        energiemixnummer=2,
                        energieart=Sparte.STROM,
                        bezeichnung="foo",
                        gueltigkeitsjahr=2021,
                        anteil=[
                            Energieherkunft(
                                erzeugungsart=Erzeugungsart.BIOGAS,
                                anteil_prozent=Decimal(40),
                            ),
                        ],
                    ),
                    vertagskonditionsaenderung=Vertragskonditionen(),
                    garantieaenderung=Preisgarantie(
                        preisgarantietyp=Preisgarantietyp.ALLE_PREISBESTANDTEILE_BRUTTO,
                        zeitliche_gueltigkeit=Zeitraum(
                            startdatum=datetime(2020, 1, 1, tzinfo=timezone.utc),
                            enddatum=datetime(2020, 4, 1, tzinfo=timezone.utc),
                        ),
                    ),
                    einschraenkungsaenderung=Tarifeinschraenkung(),
                ),
                {
                    "bezeichnung": "foo",
                    "betraege": [
                        {
                            "postleitzahl": "01187",
                            "ort": "Dresden",
                            "netznr": "2",
                            "staffeln": [
                                {
                                    "wert": Decimal("2.5"),
                                    "staffelgrenzeVon": Decimal("1"),
                                    "staffelgrenzeBis": Decimal("5"),
                                    "_id": None,
                                }
                            ],
                            "_id": None,
                        },
                    ],
                    "beschreibung": "bar",
                    "aufAbschlagstyp": AufAbschlagstyp.RELATIV,
                    "aufAbschlagsziel": "ARBEITSPREIS_HT",
                    "einheit": Waehrungseinheit.EUR,
                    "website": "foo.bar",
                    "zusatzprodukte": ["Asterix", "Obelix"],
                    "voraussetzungen": ["Petterson", "Findus"],
                    "tarifnamensaenderungen": "foobar",
                    "gueltigkeitszeitraum": {
                        "startdatum": datetime(2020, 1, 1, 0, 0, tzinfo=timezone.utc),
                        "endzeitpunkt": None,
                        "einheit": None,
                        "enddatum": datetime(2020, 4, 1, 0, 0, tzinfo=timezone.utc),
                        "startzeitpunkt": None,
                        "dauer": None,
                        "_id": None,
                    },
                    "energiemixaenderung": {
                        "energiemixnummer": 2,
                        "energieart": Sparte.STROM,
                        "bezeichnung": "foo",
                        "gueltigkeitsjahr": 2021,
                        "anteil": [
                            {"erzeugungsart": Erzeugungsart.BIOGAS, "anteilProzent": Decimal("40"), "_id": None}
                        ],
                        "oekolabel": None,
                        "bemerkung": None,
                        "co2Emission": None,
                        "atommuell": None,
                        "website": None,
                        "oekozertifikate": None,
                        "istInOekoTopTen": None,
                        "_id": None,
                    },
                    "vertagskonditionsaenderung": {
                        "beschreibung": None,
                        "anzahlAbschlaege": None,
                        "vertragslaufzeit": None,
                        "kuendigungsfrist": None,
                        "vertragsverlaengerung": None,
                        "abschlagszyklus": None,
                        "_id": None,
                    },
                    "garantieaenderung": {
                        "beschreibung": None,
                        "preisgarantietyp": "ALLE_PREISBESTANDTEILE_BRUTTO",
                        "zeitlicheGueltigkeit": {
                            "startdatum": datetime(2020, 1, 1, 0, 0, tzinfo=timezone.utc),
                            "endzeitpunkt": None,
                            "einheit": None,
                            "enddatum": datetime(2020, 4, 1, 0, 0, tzinfo=timezone.utc),
                            "startzeitpunkt": None,
                            "dauer": None,
                            "_id": None,
                        },
                        "_id": None,
                    },
                    "einschraenkungsaenderung": {
                        "zusatzprodukte": None,
                        "voraussetzungen": None,
                        "einschraenkungzaehler": None,
                        "einschraenkungleistung": None,
                        "_id": None,
                    },
                    "_id": None,
                },
                id="required and optional attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(
        self, aufabschlagregional: AufAbschlagRegional, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of AufAbschlagRegional with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlagregional, expected_json_dict)
