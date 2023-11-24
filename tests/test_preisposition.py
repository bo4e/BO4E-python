from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e import (
    BDEWArtikelnummer,
    Bemessungsgroesse,
    Kalkulationsmethode,
    Leistungstyp,
    Mengeneinheit,
    Preisposition,
    Tarifzeit,
    Waehrungseinheit,
    Zeiteinheit,
)
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_preisstaffel import example_preisstaffel

example_preisposition = Preisposition(
    berechnungsmethode=Kalkulationsmethode.AP_TRANSPORT_ODER_VERTEILNETZ,
    leistungstyp=Leistungstyp.SONSTIGER_PREIS,
    leistungsbezeichnung="Foo",
    preiseinheit=Waehrungseinheit.EUR,
    bezugsgroesse=Mengeneinheit.KVARH,
    zeitbasis=Zeiteinheit.HALBJAHR,
    tarifzeit=Tarifzeit.TZ_HT,
    bdew_artikelnummer=BDEWArtikelnummer.AUSGLEICHSENERGIE_UNTERDECKUNG,
    zonungsgroesse=Bemessungsgroesse.BENUTZUNGSDAUER,
    freimenge_blindarbeit=Decimal(50),  # %
    freimenge_leistungsfaktor=Decimal(1.0),
    preisstaffeln=[example_preisstaffel],
    gruppenartikel_id="1-2-3",
)


class TestPreisposition:
    @pytest.mark.parametrize(
        "preisposition",
        [
            pytest.param(example_preisposition),
        ],
    )
    def test_serialization_roundtrip(self, preisposition: Preisposition) -> None:
        """
        Test de-/serialisation of Preisposition
        """
        assert_serialization_roundtrip(preisposition)
