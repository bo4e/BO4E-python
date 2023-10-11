from datetime import datetime, timezone
from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import (
    Adresse,
    Angebotsposition,
    Angebotsteil,
    Betrag,
    Bilanzierungsmethode,
    Energierichtung,
    Landescode,
    Marktlokation,
    Menge,
    Mengeneinheit,
    Netzebene,
    Preis,
    Sparte,
    Typ,
    Waehrungscode,
    Waehrungseinheit,
    Zeitraum,
)
from tests.serialization_helper import assert_serialization_roundtrip

example_angebotsteil: Angebotsteil = Angebotsteil(
    positionen=[
        Angebotsposition(
            positionsbezeichnung="teststring",
            positionsmenge=Menge(wert=Decimal(4000), einheit=Mengeneinheit.KWH),
            positionspreis=Preis(wert=Decimal(0.2456), einheit=Waehrungseinheit.EUR, bezugswert=Mengeneinheit.KWH),
            positionskosten=Betrag(
                waehrung=Waehrungscode.EUR,
                wert=Decimal(98240),
            ),
        )
    ],
)

example_angebotsteil_json = {
    "positionen": [
        {
            "positionsbezeichnung": "teststring",
            "positionsmenge": {"wert": Decimal("4000"), "einheit": Mengeneinheit.KWH, "_id": None},
            "positionskosten": {"waehrung": Waehrungseinheit.EUR, "wert": Decimal("98240"), "_id": None},
            "positionspreis": {
                "bezugswert": Mengeneinheit.KWH,
                "status": None,
                "wert": Decimal("0.2456000000000000127453603226967970840632915496826171875"),
                "einheit": Waehrungseinheit.EUR,
                "_id": None,
            },
            "_id": None,
        },
    ],
    "anfrageSubreferenz": None,
    "lieferstellenangebotsteil": None,
    "gesamtmengeangebotsteil": None,
    "gesamtkostenangebotsteil": None,
    "lieferzeitraum": None,
    "_id": None,
}


class TestAngebotsteil:
    @pytest.mark.parametrize(
        "angebotsteil",
        [
            pytest.param(
                Angebotsteil(
                    positionen=[Angebotsposition()],
                    anfrage_subreferenz="teststring",
                    lieferstellenangebotsteil=[Marktlokation()],
                    gesamtmengeangebotsteil=Menge(),
                    gesamtkostenangebotsteil=Betrag(),
                    lieferzeitraum=Zeitraum(),
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, angebotsteil: Angebotsteil) -> None:
        """
        Test de-/serialisation of Angebotsteil with minimal attributes.
        """
        assert_serialization_roundtrip(angebotsteil)
