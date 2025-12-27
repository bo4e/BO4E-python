from datetime import datetime, timezone

import pytest

from bo4e import BDEWArtikelnummer, Betrag, Menge, Mengeneinheit, Preis, Rechnungsposition, Steuerbetrag, Zeitraum
from tests.serialization_helper import assert_serialization_roundtrip


class TestRechnungsposition:
    @pytest.mark.parametrize(
        "rechnungsposition",
        [
            pytest.param(
                Rechnungsposition(
                    positionsnummer=1,
                    lieferungszeitraum=Zeitraum(
                        startdatum=datetime(2021, 3, 15, tzinfo=timezone.utc),
                        enddatum=datetime(2022, 3, 15, tzinfo=timezone.utc),
                    ),
                    positionstext="Besonders wertvolle Rechnungsposition",
                    zeiteinheit=Mengeneinheit.JAHR,
                    artikelnummer=BDEWArtikelnummer.AUSGLEICHSENERGIE_UNTERDECKUNG,
                    positions_menge=Menge(),
                    zeitbezogene_menge=Menge(),
                    einzelpreis=Preis(),
                    gesamtpreis=Betrag(),
                    steuerbetrag=Steuerbetrag(),
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
