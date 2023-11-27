from datetime import datetime, timezone
from decimal import Decimal

import pytest

from bo4e import (
    Betrag,
    Geschaeftspartner,
    Marktlokation,
    Menge,
    Mengeneinheit,
    Messlokation,
    NetznutzungRechnungsart,
    NetznutzungRechnungstyp,
    Preis,
    Rechnung,
    Rechnungsposition,
    Rechnungsstatus,
    Rechnungstyp,
    Sparte,
    Steuerbetrag,
    Steuerkennzeichen,
    Waehrungscode,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestRechnung:
    @pytest.mark.parametrize(
        "rechnung",
        [
            pytest.param(
                Rechnung(
                    rechnungstitel="Hüpfburg",
                    rechnungsstatus=Rechnungsstatus.UNGEPRUEFT,
                    ist_storno=True,
                    rechnungsnummer="202201211701",
                    rechnungsdatum=datetime.today(),
                    faelligkeitsdatum=datetime.today(),
                    rechnungstyp=Rechnungstyp.ENDKUNDENRECHNUNG,
                    original_rechnungsnummer="RE-2022-01-21_1701",
                    rechnungsperiode=Zeitraum(einheit=Mengeneinheit.TAG, dauer=Decimal(21)),
                    rechnungsersteller=Geschaeftspartner(),
                    rechnungsempfaenger=Geschaeftspartner(),
                    gesamtnetto=Betrag(wert=Decimal(12.5), waehrung=Waehrungscode.EUR),
                    gesamtsteuer=Betrag(wert=Decimal(12.5), waehrung=Waehrungscode.EUR),
                    gesamtbrutto=Betrag(wert=Decimal(12.5), waehrung=Waehrungscode.EUR),
                    vorausgezahlt=Betrag(wert=Decimal(12.5), waehrung=Waehrungscode.EUR),
                    rabatt_brutto=Betrag(wert=Decimal(12.5), waehrung=Waehrungscode.EUR),
                    zu_zahlen=Betrag(wert=Decimal(12.5), waehrung=Waehrungscode.EUR),
                    steuerbetraege=[
                        Steuerbetrag(
                            steuerkennzeichen=Steuerkennzeichen.UST_19,
                            basiswert=Decimal(20.25),
                            waehrung=Waehrungscode.EUR,
                            steuerwert=Decimal(10.5),
                        )
                    ],
                    rechnungspositionen=[
                        Rechnungsposition(
                            positionsnummer=1,
                            lieferung_von=datetime(2021, 3, 15, tzinfo=timezone.utc),
                            lieferung_bis=datetime(2022, 3, 15, tzinfo=timezone.utc),
                            positionstext="Besonders wertvolle Rechnungsposition",
                            positions_menge=Menge(),
                            einzelpreis=Preis(),
                            teilsumme_netto=Betrag(),
                            teilsumme_steuer=Steuerbetrag(),
                        )
                    ],
                    sparte=Sparte.STROM,
                    netznutzungrechnungsart=NetznutzungRechnungsart.SELBSTAUSGESTELLT,
                    netznutzungrechnungstyp=NetznutzungRechnungstyp.TURNUSRECHNUNG,
                    ist_original=True,
                    ist_simuliert=True,
                    marktlokation=Marktlokation(
                        marktlokations_id="51238696781",
                    ),
                    messlokation=Messlokation(
                        messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
                    ),
                ),
                id="maximal attributes",
            ),
            pytest.param(
                Rechnung(
                    ist_storno=True,
                    rechnungsnummer="202201211701",
                    rechnungsdatum=datetime.today(),
                    faelligkeitsdatum=datetime.today(),
                    rechnungstyp=Rechnungstyp.ENDKUNDENRECHNUNG,
                    original_rechnungsnummer="RE-2022-01-21_1701",
                    rechnungsperiode=Zeitraum(einheit=Mengeneinheit.TAG, dauer=Decimal(21)),
                    rechnungsersteller=Geschaeftspartner(),
                    rechnungsempfaenger=Geschaeftspartner(),
                    gesamtnetto=Betrag(wert=Decimal(12.5), waehrung=Waehrungscode.EUR),
                    gesamtsteuer=Betrag(wert=Decimal(12.5), waehrung=Waehrungscode.EUR),
                    gesamtbrutto=Betrag(wert=Decimal(12.5), waehrung=Waehrungscode.EUR),
                    zu_zahlen=Betrag(wert=Decimal(12.5), waehrung=Waehrungscode.EUR),
                    rechnungspositionen=[
                        Rechnungsposition(
                            positionsnummer=1,
                            lieferung_von=datetime(2021, 3, 15, tzinfo=timezone.utc),
                            lieferung_bis=datetime(2022, 3, 15, tzinfo=timezone.utc),
                            positionstext="Besonders wertvolle Rechnungsposition",
                            positions_menge=Menge(),
                            einzelpreis=Preis(),
                            teilsumme_netto=Betrag(),
                            teilsumme_steuer=Steuerbetrag(),
                        )
                    ],
                    sparte=Sparte.STROM,
                    netznutzungrechnungsart=NetznutzungRechnungsart.SELBSTAUSGESTELLT,
                    netznutzungrechnungstyp=NetznutzungRechnungstyp.TURNUSRECHNUNG,
                    ist_original=True,
                    ist_simuliert=True,
                    marktlokation=Marktlokation(
                        marktlokations_id="51238696781",
                    ),
                    messlokation=Messlokation(
                        messlokations_id="DE00056266802AO6G56M11SN51G21M24S",
                    ),
                ),
                id="minimal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, rechnung: Rechnung) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(rechnung)
