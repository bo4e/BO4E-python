from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Gueltigkeitstyp, KriteriumWert, RegionaleGueltigkeit, Tarifregionskriterium
from tests.serialization_helper import assert_serialization_roundtrip


class TestRegionaleGueltigkeit:
    @pytest.mark.parametrize(
        "regionalegueltigkeit, expected_json_dict",
        [
            pytest.param(
                RegionaleGueltigkeit(
                    gueltigkeitstyp=Gueltigkeitstyp.NUR_IN,
                    kriteriums_werte=[
                        KriteriumWert(
                            kriterium=Tarifregionskriterium.NETZ_NUMMER,
                            wert="12345",
                        ),
                    ],
                ),
                {
                    "gueltigkeitstyp": "NUR_IN",
                    "kriteriumsWerte": [{"kriterium": "NETZ_NUMMER", "wert": "12345", "_id": None}],
                    "_id": None,
                },
                id="only required attributes",
            ),
        ],
    )
    def test_regionalegueltigkeit_serialization_roundtrip(
        self, regionalegueltigkeit: RegionaleGueltigkeit, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of RegionaleGueltigkeit with minimal attributes.
        """
        assert_serialization_roundtrip(regionalegueltigkeit, expected_json_dict)
