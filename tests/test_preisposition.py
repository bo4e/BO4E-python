from decimal import Decimal

import pytest

from bo4e import (
    BDEWArtikelnummer,
    Bemessungsgroesse,
    Kalkulationsmethode,
    Leistungstyp,
    Mengeneinheit,
    Preisposition,
    Preisstaffel,
    Tarifzeit,
    Waehrungseinheit,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestPreisposition:
    @pytest.mark.parametrize(
        "preisposition",
        [
            pytest.param(
                Preisposition(
                    berechnungsmethode=Kalkulationsmethode.AP_TRANSPORT_ODER_VERTEILNETZ,
                    leistungstyp=Leistungstyp.SONSTIGER_PREIS,
                    leistungsbezeichnung="Foo",
                    preiseinheit=Waehrungseinheit.EUR,
                    bezugsgroesse=Mengeneinheit.KVARH,
                    zeitbasis=Mengeneinheit.HALBJAHR,
                    tarifzeit=Tarifzeit.TZ_HT,
                    bdew_artikelnummer=BDEWArtikelnummer.AUSGLEICHSENERGIE_UNTERDECKUNG,
                    zonungsgroesse=Bemessungsgroesse.BENUTZUNGSDAUER,
                    freimenge_blindarbeit=Decimal(50),  # %
                    freimenge_leistungsfaktor=Decimal(1.0),
                    preisstaffeln=[Preisstaffel()],
                    gruppenartikel_id="1-2-3",
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisposition: Preisposition) -> None:
        """
        Test de-/serialisation of Preisposition
        """
        assert_serialization_roundtrip(preisposition)
