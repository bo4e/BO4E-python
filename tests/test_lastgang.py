import pytest
from pydantic import ValidationError

from bo4e.bo.lastgang import Lastgang
from bo4e.enum.lokationstyp import Lokationstyp
from bo4e.enum.mengeneinheit import Mengeneinheit
from bo4e.enum.sparte import Sparte
from tests.serialization_helper import assert_serialization_roundtrip
from tests.test_zeitreihenwert import example_zeitreihenwert


class TestLastgang:
    @pytest.mark.parametrize(
        "lastgang_kompakt",
        [
            pytest.param(
                Lastgang(
                    version="1.1",
                    sparte=Sparte.STROM,
                    lokations_id="DE0000011111222223333344444555556",
                    obis_kennzahl="1-0:1.8.1",
                    lokationstyp=Lokationstyp.MELO,
                    messgroesse=Mengeneinheit.KWH,
                    werte=[example_zeitreihenwert],
                ),
            ),
        ],
    )
    def test_serialization_roundtrip(self, lastgang_kompakt: Lastgang) -> None:
        """
        Test de-/serialisation
        """
        assert_serialization_roundtrip(lastgang_kompakt)

    def test_missing_required_attribute(self) -> None:
        with pytest.raises(ValidationError) as excinfo:
            _ = Lastgang()  # type: ignore[call-arg]

        assert "5 validation errors" in str(excinfo.value)
