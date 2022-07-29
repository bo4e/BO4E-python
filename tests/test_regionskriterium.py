from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.regionskriterium import Regionskriterium
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp
from bo4e.enum.regionskriteriumtyp import Regionskriteriumtyp
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

    def test_regionskriterium_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Regionskriterium()  # type: ignore[call-arg]
        assert "3 validation errors" in str(excinfo.value)
