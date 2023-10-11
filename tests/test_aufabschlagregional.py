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
        "aufabschlagregional",
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
                id="required and optional attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, aufabschlagregional: AufAbschlagRegional) -> None:
        """
        Test de-/serialisation of AufAbschlagRegional with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlagregional)
