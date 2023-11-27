from datetime import datetime, timezone

import pytest

from bo4e import BDEWArtikelnummer, Betrag, Menge, Mengeneinheit, Preis, Rechnungsposition, Steuerbetrag
from tests.serialization_helper import assert_serialization_roundtrip


class TestRechnungsposition:
    @pytest.mark.parametrize(
        "rechnungsposition",
        [
            pytest.param(
                Rechnungsposition(
                    positionsnummer=1,
                    lieferung_von=datetime(2021, 3, 15, tzinfo=timezone.utc),
                    lieferung_bis=datetime(2022, 3, 15, tzinfo=timezone.utc),
                    positionstext="Besonders wertvolle Rechnungsposition",
                    zeiteinheit=Mengeneinheit.JAHR,
                    artikelnummer=BDEWArtikelnummer.AUSGLEICHSENERGIE_UNTERDECKUNG,
                    lokations_id="51238696781",
                    positions_menge=Menge(),
                    zeitbezogene_menge=Menge(),
                    einzelpreis=Preis(),
                    teilsumme_netto=Betrag(),
                    teilrabatt_netto=Betrag(),
                    teilsumme_steuer=Steuerbetrag(),
                    artikel_id="7-8-9",
                ),
                id="maximal attributes",
            )
        ],
    )
    def test_serialization_roundtrip(self, rechnungsposition: Rechnungsposition) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(rechnungsposition)
