from decimal import Decimal
from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e.com.aufabschlagstaffelproort import AufAbschlagstaffelProOrt
from tests.serialization_helper import assert_serialization_roundtrip


class TestAufAbschlagstaffelProOrt:
    @pytest.mark.parametrize(
        "aufabschlagstaffelproort, expected_json_dict",
        [
            pytest.param(
                AufAbschlagstaffelProOrt(
                    wert=Decimal(2.5),
                    staffelgrenze_von=Decimal(1),
                    staffelgrenze_bis=Decimal(5),
                ),
                {
                    "wert": Decimal("2.5"),
                    "staffelgrenzeVon": Decimal("1"),
                    "staffelgrenzeBis": Decimal("5"),
                },
            ),
        ],
    )
    def test_aufabschlagstaffelproort_required_attributes(
        self, aufabschlagstaffelproort: AufAbschlagstaffelProOrt, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of AufAbschlagstaffelProOrt with minimal attributes.
        """
        assert_serialization_roundtrip(aufabschlagstaffelproort, expected_json_dict)

    def test_aufabschlagstaffelproort_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = AufAbschlagstaffelProOrt()  # type: ignore[call-arg]

        assert "3 validation errors" in str(excinfo.value)
