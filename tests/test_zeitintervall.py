import pytest
from pydantic import ValidationError

from bo4e import Zeiteinheit, Zeitintervall
from tests.serialization_helper import assert_serialization_roundtrip


class TestZeitintervall:
    def test_wrong_datatype(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Zeitintervall(wert="errrrrror", zeiteinheit=Zeiteinheit.TAG)  # type: ignore[arg-type]

        assert "1 validation error" in str(excinfo.value)
        assert "wert" in str(excinfo.value)
        assert "should be a valid integer" in str(excinfo.value)

    @pytest.mark.parametrize(
        "zeitintervall",
        [
            pytest.param(
                Zeitintervall(
                    wert=2,
                    zeiteinheit=Zeiteinheit.VIERTEL_STUNDE,
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, zeitintervall: Zeitintervall) -> None:
        """
        Test de-/serialisation of Zeitintervall.
        """
        assert_serialization_roundtrip(zeitintervall)
