from typing import Any, Dict

import pytest

from bo4e import Geraet, Geraeteeigenschaften, Geraetemerkmal, Geraetetyp
from tests.serialization_helper import assert_serialization_roundtrip


class TestGeraet:
    @pytest.mark.parametrize(
        "geraet",
        [
            pytest.param(
                Geraet(
                    geraetenummer="0815",
                    geraeteeigenschaften=Geraeteeigenschaften(),
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
