from datetime import datetime, timezone

import pytest

from bo4e import (
    Buendelvertrag,
    Geschaeftspartner,
    Sparte,
    Unterschrift,
    Vertrag,
    Vertragsart,
    Vertragskonditionen,
    Vertragsstatus,
)
from tests.serialization_helper import assert_serialization_roundtrip


class TestBuendelvertrag:
    @pytest.mark.parametrize(
        "buendelvertrag",
        [
            pytest.param(
                Buendelvertrag(
                    vertragsnummer="1234567890",
                    vertragsart=Vertragsart.NETZNUTZUNGSVERTRAG,
                    vertragsstatus=Vertragsstatus.AKTIV,
                    sparte=Sparte.STROM,
                    vertragsbeginn=datetime(2021, 4, 30, 13, 45, tzinfo=timezone.utc),
                    vertragsende=datetime(2200, 4, 30, 13, 45, tzinfo=timezone.utc),
                    vertragspartner1=Geschaeftspartner(),
                    vertragspartner2=Geschaeftspartner(),
                    einzelvertraege=[Vertrag()],
                    vertragskonditionen=[Vertragskonditionen()],
                    unterzeichnervp1=[Unterschrift()],
                    unterzeichnervp2=[Unterschrift(), Unterschrift()],
                    beschreibung="Das ist ein Bündelvertrag mit allen optionalen Feldern ausgefüllt.",
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, buendelvertrag: Buendelvertrag) -> None:
        assert_serialization_roundtrip(buendelvertrag)
