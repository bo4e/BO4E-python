from typing import Any, Dict

import pytest

from bo4e.bo.geraet import Geraet
from bo4e.enum.geraeteklasse import Geraeteklasse
from bo4e.enum.geraetetyp import Geraetetyp
from bo4e.enum.typ import Typ
from tests.serialization_helper import assert_serialization_roundtrip

example_geraet = Geraet(
    geraetenummer="0815",
    geraeteklasse=Geraeteklasse.WANDLER,
    geraetetyp=Geraetetyp.BLOCKSTROMWANDLER,
    bezeichnung="56k Modem",
)


class TestGeraet:
    @pytest.mark.parametrize(
        "geraet, expected_json_dict",
        [
            pytest.param(
                Geraet(),
                {
                    "versionstruktur": "2",
                    "_typ": Typ.GERAET,
                    "externeReferenzen": None,
                    "geraetenummer": None,
                    "bezeichnung": None,
                    "geraeteklasse": None,
                    "geraetetyp": None,
                    "_id": None,
                },
                id="Minimal attributes",
            ),
            pytest.param(
                example_geraet,
                {
                    "versionstruktur": "2",
                    "_typ": Typ.GERAET,
                    "externeReferenzen": None,
                    "geraetenummer": "0815",
                    "geraeteklasse": "WANDLER",
                    "geraetetyp": "BLOCKSTROMWANDLER",
                    "bezeichnung": "56k Modem",
                    "_id": None,
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
