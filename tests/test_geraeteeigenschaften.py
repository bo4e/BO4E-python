import pytest  # type:ignore[import]

from bo4e.com.geraeteeigenschaften import Geraeteeigenschaften, GeraeteeigenschaftenSchema
from bo4e.enum.geraetemerkmal import Geraetemerkmal
from bo4e.enum.geraetetyp import Geraetetyp
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestGeraeteeigenschaften:
    @pytest.mark.parametrize(
        "geraeteeigenschaften, expected_json_dict",
        [
            pytest.param(
                Geraeteeigenschaften(geraetemerkmal=Geraetemerkmal.GAS_G1000, geraetetyp=Geraetetyp.MULTIPLEXANLAGE),
                {"geraetemerkmal": "GAS_G1000", "geraetetyp": "MULTIPLEXANLAGE"},
            ),
        ],
    )
    def test_serialization_roundtrip(self, geraeteeigenschaften: Geraeteeigenschaften, expected_json_dict: dict):
        """
        Test de-/serialisation of Geraeteeigenschaften
        """
        assert_serialization_roundtrip(geraeteeigenschaften, GeraeteeigenschaftenSchema(), expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(TypeError) as excinfo:
            _ = Geraeteeigenschaften()

        assert "missing 1 required" in str(excinfo.value)

    @pytest.mark.parametrize(
        "not_a_geraetetyp",
        [
            pytest.param(17),  # not a geraetetyp
            pytest.param("foo"),  # not a geraetetyp
        ],
    )
    def test_failing_validation(self, not_a_geraetetyp):
        with pytest.raises(TypeError) as excinfo:
            _ = Geraeteeigenschaften(geraetemerkmal=Geraetemerkmal.GAS_G1000, geraetetyp=not_a_geraetetyp)

        assert "'geraetetyp' must be " in str(excinfo.value)
