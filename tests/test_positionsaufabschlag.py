from decimal import Decimal

import pytest  # type:ignore[import]
from pydantic import ValidationError

from bo4e.com.positionsaufabschlag import PositionsAufAbschlag
from bo4e.enum.aufabschlagstyp import AufAbschlagstyp
from bo4e.enum.waehrungseinheit import Waehrungseinheit
from tests.serialization_helper import assert_serialization_roundtrip  # type:ignore[import]


class TestPositionsAufAbschlag:
    @pytest.mark.parametrize(
        "positionsaufabschlag, expected_json_dict",
        [
            pytest.param(
                PositionsAufAbschlag(
                    bezeichnung="foo",
                    beschreibung="bar",
                    auf_abschlagstyp=AufAbschlagstyp.ABSOLUT,
                    auf_abschlagswert=Decimal(4.25),
                    auf_abschlagswaehrung=Waehrungseinheit.EUR,
                ),
                {
                    "bezeichnung": "foo",
                    "beschreibung": "bar",
                    "aufAbschlagstyp": AufAbschlagstyp.ABSOLUT,
                    "aufAbschlagswert": Decimal("4.25"),
                    "aufAbschlagswaehrung": Waehrungseinheit.EUR,
                },
            ),
        ],
    )
    def test_serialization_roundtrip(self, positionsaufabschlag: PositionsAufAbschlag, expected_json_dict: dict):
        """
        Test de-/serialisation of PositionsAufAbschlag
        """
        assert_serialization_roundtrip(positionsaufabschlag, expected_json_dict)

    def test_missing_required_attribute(self):
        with pytest.raises(ValidationError) as excinfo:
            _ = PositionsAufAbschlag()

        assert "5 validation errors" in str(excinfo.value)
