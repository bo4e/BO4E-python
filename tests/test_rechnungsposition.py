from datetime import datetime, timezone

import pytest  # type:ignore[import]

from bo4e.com.rechnungsposition import Rechnungsposition, RechnungspositionSchema
from bo4e.enum.artikelid import ArtikelId
from bo4e.enum.bdewartikelnummer import BDEWArtikelnummer
from bo4e.enum.zeiteinheit import Zeiteinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]
from tests.test_betrag import example_betrag  # type:ignore[import]
from tests.test_menge import example_menge  # type:ignore[import]
from tests.test_preis import example_preis  # type:ignore[import]
from tests.test_steuerbetrag import example_steuerbetrag  # type:ignore[import]


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
                    artikel_id=ArtikelId.ARTIKEL_2017004,
                ),
                id="maximal attributes",
            )
        ],
    )
    def test_serialization_roundtrip(self, rechnungsposition):
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(rechnungsposition, RechnungspositionSchema())

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Rechnungsposition()
        assert "missing 8 required" in str(excinfo.value)
