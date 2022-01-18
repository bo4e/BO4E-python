import pytest  # type:ignore[import]

from bo4e.com.standorteigenschaftenstrom import StandorteigenschaftenStrom, StandorteigenschaftenStromSchema
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]

example_standorteigenschaften_strom = StandorteigenschaftenStrom(
    regelzone="Transnet BW",
    bilanzierungsgebiet_eic="11YW-ALBSTADT--5",
    regelzone_eic="10YDE-ENBW-----N",
)


class TestStandorteigenschaftenStrom:
    @pytest.mark.parametrize(
        "standorteigenschaften_strom, expected_json_dict",
        [
            pytest.param(
                example_standorteigenschaften_strom,
                {
                    "regelzone": "Transnet BW",
                    "bilanzierungsgebietEic": "11YW-ALBSTADT--5",
                    "regelzoneEic": "10YDE-ENBW-----N",
                },
            )
        ],
    )
    def test_serialization_roundtrip(
        self, standorteigenschaften_strom: StandorteigenschaftenStrom, expected_json_dict: dict
    ):
        assert_serialization_roundtrip(
            standorteigenschaften_strom, StandorteigenschaftenStromSchema(), expected_json_dict
        )

    def test_missing_required_attributes(self):
        with pytest.raises(TypeError) as excinfo:
            _ = StandorteigenschaftenStrom()

        assert "missing 3 required" in str(excinfo.value)
