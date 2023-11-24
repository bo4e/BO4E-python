from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Gueltigkeitstyp, Regionskriterium, Regionskriteriumtyp
from tests.serialization_helper import assert_serialization_roundtrip

example_regionskriterium = Regionskriterium(
    regionskriteriumtyp=Regionskriteriumtyp.REGELGEBIET_NAME,
    gueltigkeitstyp=Gueltigkeitstyp.NICHT_IN,
    wert="Was ist ein Regionskriterium?",
)


class TestRegionskriterium:
    @pytest.mark.parametrize(
        "regionskriterium, expected_json_dict",
        [
            pytest.param(
                example_regionskriterium,
                {
                    "gueltigkeitstyp": "NICHT_IN",
                    "regionskriteriumtyp": "REGELGEBIET_NAME",
                    "wert": "Was ist ein Regionskriterium?",
                    "_id": None,
                },
            ),
        ],
    )
    def test_regionskriterium_serialization_roundtrip(
        self, regionskriterium: Regionskriterium, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Regionskriterium with minimal attributes.
        """
        assert_serialization_roundtrip(regionskriterium, expected_json_dict)
