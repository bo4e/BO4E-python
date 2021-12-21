from datetime import datetime, timezone
from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.aufabschlagproort import AufAbschlagProOrt
from bo4e.com.aufabschlagregional import AufAbschlagRegional, AufAbschlagRegionalSchema
from bo4e.com.aufabschlagstaffelproort import AufAbschlagstaffelProOrt
from bo4e.com.energieherkunft import Energieherkunft
from bo4e.com.energiemix import Energiemix
from bo4e.com.preisgarantie import Preisgarantie
from bo4e.com.tarifeinschraenkung import Tarifeinschraenkung
from bo4e.com.vertragskonditionen import Vertragskonditionen
from bo4e.com.zeitraum import Zeitraum
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.aufabschlagsziel import AufAbschlagsziel
from bo4e.enum.erzeugungsart import Erzeugungsart
from bo4e.enum.preisgarantietyp import Preisgarantietyp
from bo4e.enum.sparte import Sparte
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestAufAbschlagRegional:
    @pytest.mark.parametrize(
        "aufabschlagregional, expected_json_dict",
        [
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
                                    "wert": "2.5",
                                    "staffelgrenzeVon": "1",
                                    "staffelgrenzeBis": "5",
                                }
                            ],
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
                                    "wert": "2.5",
                                    "staffelgrenzeVon": "1",
                                    "staffelgrenzeBis": "5",
                                }
                            ],
                        },
                    ],
                    "beschreibung": "bar",
                    "aufAbschlagstyp": "RELATIV",
                    "aufAbschlagsziel": "ARBEITSPREIS_HT",
                    "einheit": "EUR",
                    "website": "foo.bar",
                    "zusatzprodukte": ["Asterix", "Obelix"],
                    "voraussetzungen": ["Petterson", "Findus"],
                    "tarifnamensaenderungen": "foobar",
                    "gueltigkeitszeitraum": {
                        "startdatum": "2020-01-01T00:00:00+00:00",
                        "endzeitpunkt": None,
                        "einheit": None,
                        "enddatum": "2020-04-01T00:00:00+00:00",
                        "startzeitpunkt": None,
                        "dauer": None,
                    },
                    "energiemixaenderung": {
                        "energiemixnummer": 2,
                        "energieart": "STROM",
                        "bezeichnung": "foo",
                        "gueltigkeitsjahr": 2021,
                        "anteil": [
                            {
                                "erzeugungsart": "BIOGAS",
                                "anteilProzent": "40",
                            }
                        ],
                        "oekolabel": [],
                        "bemerkung": None,
                        "co2Emission": None,
                        "atommuell": None,
                        "website": None,
                        "oekozertifikate": [],
                        "oekoTopTen": None,
                    },
                    "vertagskonditionsaenderung": {
                        "beschreibung": None,
                        "anzahlAbschlaege": None,
                        "vertragslaufzeit": None,
                        "kuendigungsfrist": None,
                        "vertragsverlaengerung": None,
                        "abschlagszyklus": None,
                    },
                    "garantieaenderung": {
                        "beschreibung": None,
                        "preisgarantietyp": "ALLE_PREISBESTANDTEILE_BRUTTO",
                        "zeitlicheGueltigkeit": {
                            "startdatum": "2020-01-01T00:00:00+00:00",
                            "endzeitpunkt": None,
                            "einheit": None,
                            "enddatum": "2020-04-01T00:00:00+00:00",
                            "startzeitpunkt": None,
                            "dauer": None,
                        },
                    },
                    "einschraenkungsaenderung": {
                        "zusatzprodukte": None,
                        "voraussetzungen": None,
                        "einschraenkungzaehler": None,
                        "einschraenkungleistung": None,
                    },
                },
                id="required and optional attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, aufabschlagregional, expected_json_dict):
        """
        Test de-/serialisation of AufAbschlagRegional with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlagregional, AufAbschlagRegionalSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = AufAbschlagRegional()

        assert "missing 2 required" in str(excinfo.value)

    def test_aufabschlagregional_betraege_required(self):
        with pytest.raises(ValueError) as excinfo:
            _ = (
                AufAbschlagRegional(
                    bezeichnung="foo",
                    betraege=[],
                ),
            )

        assert "List betraege must not be empty." in str(excinfo.value)
