from datetime import datetime
from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e import (
    Energierichtung,
    Mengeneinheit,
    Registeranzahl,
    Sparte,
    Typ,
    Zaehler,
    Zaehlerauspraegung,
    Zaehlertyp,
    Zaehlwerk,
)
from bo4e.zusatzattribut import ZusatzAttribut
from tests.serialization_helper import assert_serialization_roundtrip

example_zaehler = Zaehler(
    zaehlernummer="000111222",
    sparte=Sparte.STROM,
    zaehlerauspraegung=Zaehlerauspraegung.EINRICHTUNGSZAEHLER,
    zaehlwerke=[
        Zaehlwerk(
            zaehlwerk_id="98765",
            einheit=Mengeneinheit.KW,
            richtung=Energierichtung.EINSP,
            bezeichnung="my zaehlwerk",
            obis_kennzahl="1-0:1.8.1",
            wandlerfaktor=Decimal(0.95),
        )
    ],
    zaehlertyp=Zaehlertyp.DREHSTROMZAEHLER,
    registeranzahl=Registeranzahl.ZWEITARIF,
    zaehlerkonstante=Decimal(0.9),
    eichung_bis=datetime(2022, 1, 1, 0, 0, 0),
    externe_referenzen=[ExterneReferenz(ex_ref_name="zaehler im anderen system", ex_ref_wert="7890")],
    letzte_eichung=datetime(2019, 6, 30, 0, 0, 0),
)


class TestZaehler:
    @pytest.mark.parametrize(
        "zaehler",
        [
            pytest.param(
                Zaehler(
                    zaehlernummer="000111222",
                    sparte=Sparte.STROM,
                    zaehlerauspraegung=Zaehlerauspraegung.EINRICHTUNGSZAEHLER,
                    zaehlwerke=[Zaehlwerk()],
                    zaehlertyp=Zaehlertyp.DREHSTROMZAEHLER,
                    tarifart=Tarifart.ZWEITARIF,
                    zaehlerkonstante=Decimal(0.9),
                    eichung_bis=datetime(2022, 1, 1, 0, 0, 0),
                    zusatz_attribute=[ZusatzAttribut(name="zaehler im anderen system", wert="7890")],
                    letzte_eichung=datetime(2019, 6, 30, 0, 0, 0),
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, zaehler: Zaehler) -> None:
        """
        Test de-/serialisation of Zaehler.
        """
        assert_serialization_roundtrip(zaehler)
