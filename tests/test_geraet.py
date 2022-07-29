from typing import Any, Dict

import pytest

from bo4e.com.geraet import Geraet
from bo4e.com.geraeteeigenschaften import Geraeteeigenschaften
from bo4e.enum.geraetemerkmal import Geraetemerkmal
from bo4e.enum.geraetetyp import Geraetetyp
from tests.serialization_helper import assert_serialization_roundtrip


class TestGeraet:
    @pytest.mark.parametrize(
        "geraet, expected_json_dict",
        [
            pytest.param(Geraet(), {"geraetenummer": None, "geraeteeigenschaften": None}, id="Minimal attributes"),
            pytest.param(
                Geraet(
                    geraetenummer="0815",
                    geraeteeigenschaften=Geraeteeigenschaften(
                        geraetemerkmal=Geraetemerkmal.GAS_G1000,
                        geraetetyp=Geraetetyp.MULTIPLEXANLAGE,
                    ),
                ),
                {
                    "geraetenummer": "0815",
                    "geraeteeigenschaften": {"geraetemerkmal": "GAS_G1000", "geraetetyp": Geraetetyp.MULTIPLEXANLAGE},
                },
                id="Maximal attributes",
            ),
        ],
    )
    def test_serialization_roundtrip(self, geraet: Geraet, expected_json_dict: Dict[str, Any]) -> None:
        """
        Test de-/serialisation of Geraet
        """
        assert_serialization_roundtrip(geraet, expected_json_dict)
