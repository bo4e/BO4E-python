import pytest

from bo4e import Preiszeitreihe, Preiszeitreihenwert, Preistyp
from tests.serialization_helper import assert_serialization_roundtrip


class TestPreiszeitreihe:
    @pytest.mark.parametrize(
        "preiszeitreihe",
        [
            pytest.param(
                Preiszeitreihe(
                    preiszeitreihe_id="1-2-3",
                    bezeichnung="Bezeichnung",
                    preistyp=Preistyp.GESAMTPREIS_BRUTTO,
                    werte=[Preiszeitreihenwert()],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, preiszeitreihe: Preiszeitreihe) -> None:
        """
        Test de-/serialisation of Preiszeitreihe
        """
        assert_serialization_roundtrip(preiszeitreihe)
