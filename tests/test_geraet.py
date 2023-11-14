import pytest

from bo4e import Geraet, Geraeteklasse, Geraetetyp
from tests.serialization_helper import assert_serialization_roundtrip

example_geraet = Geraet(
    geraetenummer="0815",
    geraeteklasse=Geraeteklasse.WANDLER,
    geraetetyp=Geraetetyp.BLOCKSTROMWANDLER,
    bezeichnung="56k Modem",
)


class TestGeraet:
    @pytest.mark.parametrize(
        "geraet",
        [
            pytest.param(
                Geraet(
                    geraetenummer="0815",
                    bezeichnung="56k Modem",
                    geraeteklasse=Geraeteklasse.WANDLER,
                    geraetetyp=Geraetetyp.BLOCKSTROMWANDLER,
                ),
                id="all attributes at first level",
            ),
        ],
    )
    def test_serialization_roundtrip(self, geraet: Geraet) -> None:
        """
        Test de-/serialisation of Geraet
        """
        assert_serialization_roundtrip(geraet)
