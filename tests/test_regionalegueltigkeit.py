from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.kriteriumwert import KriteriumWert
from bo4e.com.regionalegueltigkeit import RegionaleGueltigkeit
from bo4e.enum.gueltigkeitstyp import Gueltigkeitstyp
from bo4e.enum.tarifregionskriterium import Tarifregionskriterium
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
                    "kriteriumsWerte": [
                        {
                            "kriterium": "NETZ_NUMMER",
                            "wert": "12345",
                        }
                    ],
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

    def test_regionalegueltigkeit_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = RegionaleGueltigkeit()  # type: ignore[call-arg]

        assert "2 validation errors" in str(excinfo.value)

    def test_regionalegueltigkeit_kriteriumswerte_required(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = RegionaleGueltigkeit(
                gueltigkeitstyp=Gueltigkeitstyp.NUR_IN,
                kriteriums_werte=[],
            )

        assert "1 validation error" in str(excinfo.value)
        assert "too_short" in str(excinfo.value)
