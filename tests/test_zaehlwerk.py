from decimal import Decimal

import pytest

from bo4e import (
    Energierichtung,
    Konzessionsabgabe,
    Mengeneinheit,
    Messwert,
    Verbrauchsart,
    VerwendungszweckProMarktrolle,
    Waermenutzung,
    Zaehlwerk,
    Zaehlzeitregister,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestZaehlwerk:
    @pytest.mark.parametrize(
        "zaehlwerk",
        [
            pytest.param(
                Zaehlwerk(
                    zaehlwerk_id="zw-id",
                    bezeichnung="zw-bezeichnung",
                    richtung=Energierichtung.AUSSP,
                    obis_kennzahl="1-0:1.8.1",
                    wandlerfaktor=Decimal(1),
                    einheit=Mengeneinheit.KWH,
                    ist_schwachlastfaehig=True,
                    verwendungszwecke=[VerwendungszweckProMarktrolle()],
                    verbrauchsart=Verbrauchsart.W,
                    ist_unterbrechbar=True,
                    waermenutzung=Waermenutzung.WAERMEPUMPE,
                    konzessionsabgabe=Konzessionsabgabe(),
                    ist_steuerbefreit=True,
                    vorkommastelle=6,
                    nachkommastelle=3,
                    ist_abrechnungsrelevant=True,
                    anzahlAblesungen=42,
                    zaehlzeitregister=Zaehlzeitregister(),
                    messwerte=[Messwert()],
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, zaehlwerk: Zaehlwerk) -> None:
        """
        Test de-/serialisation of Zaehler.
        """
        assert_serialization_roundtrip(zaehlwerk)
