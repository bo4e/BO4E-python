import pytest

from bo4e import DynamischePreiszeitreihe, Marktlokation, Preiszeitreihe, Zaehler
from tests.serialization_helper import assert_serialization_roundtrip


class TestPreiszeitreihe:
    @pytest.mark.parametrize(
        "dynamische_preiszeitreihe",
        [
            pytest.param(
                DynamischePreiszeitreihe(
                    marktlokation=Marktlokation(),
                    zaehler=Zaehler(),
                    preiszeitreihen=[Preiszeitreihe()],
                )
            ),
        ],
    )
    def test_serialization_roundtrip(self, dynamische_preiszeitreihe: DynamischePreiszeitreihe) -> None:
        """
        Test de-/serialisation of Preiszeitreihe
        """
        assert_serialization_roundtrip(dynamische_preiszeitreihe)
