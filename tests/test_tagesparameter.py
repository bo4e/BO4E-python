import pytest

from bo4e.com.tagesparameter import Tagesparameter
from tests.serialization_helper import assert_serialization_roundtrip


class TestTagesparameter:
    @pytest.mark.parametrize(
        "tagesparameter",
        [
            pytest.param(
                Tagesparameter(
                    klimazone="7624q",
                    temperaturmessstelle="1234x",
                    dienstanbieter="ZT1",
                    herausgeber="BDEW",
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, tagesparameter: Tagesparameter) -> None:
        """
        Test de-/serialisation of Tagesparameter.
        """
        assert_serialization_roundtrip(tagesparameter)
