import pytest

from bo4e import KriteriumWert, Tarifregionskriterium
from tests.serialization_helper import assert_serialization_roundtrip


class TestKriteriumWert:
    @pytest.mark.parametrize(
        "kriteriumwert",
        [
            pytest.param(
                KriteriumWert(
                    kriterium=Tarifregionskriterium.ORT,
                    wert="Grünwald",
                ),
            ),
        ],
    )
    def test_kriteriumwert_serialization_roundtrip(self, kriteriumwert: KriteriumWert) -> None:
        """
        Test de-/serialisation of KriteriumWert.
        """
        assert_serialization_roundtrip(kriteriumwert)
