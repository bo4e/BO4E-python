import pytest

from bo4e import StandorteigenschaftenStrom
from tests.serialization_helper import assert_serialization_roundtrip


class TestStandorteigenschaftenStrom:
    @pytest.mark.parametrize(
        "standorteigenschaften_strom",
        [
            pytest.param(
                StandorteigenschaftenStrom(
                    regelzone="Transnet BW",
                    bilanzierungsgebiet_eic="11YW-ALBSTADT--5",
                    regelzone_eic="10YDE-ENBW-----N",
                ),
            )
        ],
    )
    def test_serialization_roundtrip(self, standorteigenschaften_strom: StandorteigenschaftenStrom) -> None:
        """
        Test de-/serialisation.
        """
        assert_serialization_roundtrip(standorteigenschaften_strom)
