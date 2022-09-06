from datetime import datetime, timezone

import pytest
from pydantic import ValidationError

from bo4e.com.rechnungsposition import Rechnungsposition
from bo4e.enum.bdewartikelnummer import BDEWArtikelnummer
from bo4e.enum.zeiteinheit import Zeiteinheit
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_betrag import example_betrag
from tests.test_menge import example_menge
from tests.test_preis import example_preis
from tests.test_steuerbetrag import example_steuerbetrag


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
                    zeiteinheit=Zeiteinheit.JAHR,
                    artikelnummer=BDEWArtikelnummer.AUSGLEICHSENERGIE_UNTERDECKUNG,
                    lokations_id="51238696781",
                    positions_menge=example_menge,
                    zeitbezogene_menge=example_menge,
                    einzelpreis=example_preis,
                    teilsumme_netto=example_betrag,
                    teilrabatt_netto=example_betrag,
                    teilsumme_steuer=example_steuerbetrag,
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

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Rechnungsposition()  # type: ignore[call-arg]
        assert "8 validation errors" in str(excinfo.value)
