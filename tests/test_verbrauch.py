from datetime import datetime, timezone
from decimal import Decimal

import pytest

from bo4e import Mengeneinheit, Messwertstatus, Verbrauch, Wertermittlungsverfahren
from tests.serialization_helper import assert_serialization_roundtrip


class TestVerbrauch:
    @pytest.mark.parametrize(
        "verbrauch",
        [
            pytest.param(
                Verbrauch(
                    wert=Decimal(40),
                    startdatum=datetime(2021, 12, 1, 0, 0, 0).replace(tzinfo=timezone.utc),
                    enddatum=datetime(2021, 12, 2, 0, 0, 0).replace(tzinfo=timezone.utc),
                    obis_kennzahl="1-0:1.8.1",
                    einheit=Mengeneinheit.KWH,
                    wertermittlungsverfahren=Wertermittlungsverfahren.MESSUNG,
                    messwertstatus=Messwertstatus.ABGELESEN,
                )
            ),
            pytest.param(
                Verbrauch(
                    wert=Decimal(40),
                    obis_kennzahl="1-0:1.8.1",
                    einheit=Mengeneinheit.KWH,
                    wertermittlungsverfahren=Wertermittlungsverfahren.MESSUNG,
                    messwertstatus=Messwertstatus.ABGELESEN,
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, verbrauch: Verbrauch) -> None:
        """
        Test de-/serialisation of Verbrauch.
        """
        assert_serialization_roundtrip(verbrauch)
