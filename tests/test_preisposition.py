from decimal import Decimal

import pytest  # type:ignore[import]

from bo4e.com.angebotsposition import Angebotsposition, AngebotspositionSchema
from bo4e.com.betrag import Betrag
from bo4e.com.menge import Menge
from bo4e.com.preis import Preis
from bo4e.com.preisposition import Preisposition, PreispositionSchema
from bo4e.enum.bdewartikelnummer import BDEWArtikelnummer
from bo4e.enum.bemessungsgroesse import Bemessungsgroesse
from bo4e.enum.kalkulationsmethode import Kalkulationsmethode
from bo4e.enum.leistungstyp import Leistungstyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.tarifzeit import Tarifzeit
from bo4e.enum.waehrungscode import Waehrungscode
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from bo4e.enum.zeiteinheit import Zeiteinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_preisstaffel import example_preisstaffel  # type:ignore[import]


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
                    zeitbasis=Zeiteinheit.HALBJAHR,
                    tarifzeit=Tarifzeit.TZ_HT,
                    bdew_artikelnummer=BDEWArtikelnummer.AUSGLEICHSENERGIE_UNTERDECKUNG,
                    zonungsgroesse=Bemessungsgroesse.BENUTZUNGSDAUER,
                    freimenge_blindarbeit=Decimal(50),  # %
                    freimenge_leistungsfaktor=Decimal(1.0),
                    preisstaffeln=[example_preisstaffel],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preisposition: Preisposition):
        """
        Test de-/serialisation of Preisposition
        """
        assert_serialization_roundtrip(preisposition, PreispositionSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Preisposition()
        assert "missing 6 required" in str(excinfo.value)
