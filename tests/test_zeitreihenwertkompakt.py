from decimal import Decimal

import pytest
from pydantic import ValidationError

from bo4e import Messwertstatus, Messwertstatuszusatz, Zeitreihenwertkompakt
from tests.serialization_helper import assert_serialization_roundtrip


class TestZeitreihenwertkompakt:
    def test_wrong_datatype(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Zeitreihenwertkompakt(wert="helloooo")  # type: ignore[arg-type]

        assert "wert" in str(excinfo.value)

    @pytest.mark.parametrize(
        "zeitreihenwertkompakt",
        [
            pytest.param(
                Zeitreihenwertkompakt(
                    wert=Decimal(1.5),
                    status=Messwertstatus.ABGELESEN,
                    statuszusatz=Messwertstatuszusatz.Z78_GERAETEWECHSEL,
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, zeitreihenwertkompakt: Zeitreihenwertkompakt) -> None:
        """
        Test de-/serialisation of Zeitreihenwertkompakt.
        """
        assert_serialization_roundtrip(zeitreihenwertkompakt)
