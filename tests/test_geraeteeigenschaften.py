from typing import Any, Dict

import pytest
from pydantic import ValidationError

from bo4e import Geraeteeigenschaften, Geraetemerkmal, Geraetetyp
from tests.serialization_helper import assert_serialization_roundtrip

example_geraeteeigenschaften = Geraeteeigenschaften(
    geraetemerkmal=Geraetemerkmal.GAS_G1000, geraetetyp=Geraetetyp.MULTIPLEXANLAGE
)


class TestGeraeteeigenschaften:
    @pytest.mark.parametrize(
        "geraeteeigenschaften, expected_json_dict",
        [
            pytest.param(
                example_geraeteeigenschaften,
                {"geraetemerkmal": "GAS_G1000", "geraetetyp": Geraetetyp.MULTIPLEXANLAGE, "_id": None},
            ),
        ],
    )
    def test_serialization_roundtrip(
        self, geraeteeigenschaften: Geraeteeigenschaften, expected_json_dict: Dict[str, Any]
    ) -> None:
        """
        Test de-/serialisation of Geraeteeigenschaften
        """
        assert_serialization_roundtrip(geraeteeigenschaften, expected_json_dict)

    @pytest.mark.parametrize(
        "not_a_geraetetyp",
        [
            pytest.param(17),  # not a geraetetyp
            pytest.param("foo"),  # not a geraetetyp
        ],
    )
    def test_failing_validation(self, not_a_geraetetyp: Any) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Geraeteeigenschaften(geraetemerkmal=Geraetemerkmal.GAS_G1000, geraetetyp=not_a_geraetetyp)

        assert "1 validation error" in str(excinfo.value)
        assert "string_type" in str(excinfo.value) or "type=enum" in str(excinfo.value)
